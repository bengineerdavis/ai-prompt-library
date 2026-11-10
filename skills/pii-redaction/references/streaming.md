# Handling input larger than memory or context

Open this when the input may not fit in memory or in one model call, or when you
are reviewing a redaction tool that claims to handle large files.

## The hazard chunking introduces

A detector match can be cut by a chunk boundary. `jane.smith@example.com` split
between two chunks matches no pattern in either chunk: layer 1 misses it, the
model never sees it whole, and layer 3 over each chunk alone reports clean. The
output is then a plausible file that contains an email address — the exact
failure this skill exists to prevent, produced by the fix for a size problem.

Two shapes of the problem, and they need different answers:

- **A match inside one atom** — solved by never splitting atoms.
- **A match spanning two atoms** — solved by the carry window and the edge rule.

Checking only one of these leaves the other silently open.

## Atoms

An atom is the smallest unit the chunker never splits:

| Input        | Atom                |
| ------------ | ------------------- |
| Text         | one line            |
| JSON, NDJSON | one top-level value |
| YAML         | one `---` document  |
| TOML         | one table           |

Where a container is bigger than the budget, descend into its members instead of
cutting through them. Never split a scalar. Emit container syntax (`[`, `]`, `,`,
`{`, `}`) verbatim so reassembly is byte-exact and the parser can confirm it.

An atom larger than the whole budget refuses the run, naming its location and
size. A 900 MB single log line is not something to guess at.

## Carry window and the edge rule

Read a window of input *before* each chunk start, so a detector can see a match
that straddles the boundary. The carry is read and then discarded — it exists to
prove the boundary is safe, not to give the model extra context.

Run detectors over `carry + chunk`. **If a match touches either edge of that
window, the window was too small.** Extend the carry and rescan; past a bounded
number of extensions, fail the run. This converts "maybe a match straddled the
edge" into a visible failure instead of a silent leak.

Beware unbounded patterns. A regex like `("cookies"\s*:\s*\[)([^\]]*)("?\])`
matches to the first `]` and can cross any number of newlines, so a fixed carry
can never be proven sufficient against it. Either bound such patterns to a single
line and rely on structural handling, or accept that the edge rule will refuse
those files — but do not assume a large constant fixes it.

## Budget

Providers rarely expose a context window the tool can query, so the budget is
chosen, not discovered: one documented default, overridable, and printed to
stderr in the plan before the first model call.

Shrink on failure, never grow on success. When a chunk fails for a size-related
reason, halve the budget and retry that chunk — a couple of times at most — then
fail naming the chunk, its size, and the budget it was still too large for. A
successful chunk proves it fit; it does not prove a larger one would have, and
guessing upward produces cut chunks that can still pass a weak gate.

## Structured formats

- **JSON** — descend to members that fit. Re-parse the finished output and fail
  the run if it does not parse. A redacted JSON that no longer parses is worth
  nothing to the person who needed the data.
- **NDJSON** — one value per line streams perfectly; treat each line as an atom.
- **YAML** — split only on column-0 `---` separators, which cannot appear inside
  a block scalar. Within a document, chunk at line atoms. Without a parser you
  cannot promise the result is still valid YAML, so say so on stderr rather than
  implying structural handling.
- **TOML** — parse with `tomllib` only where it exists. On Python older than
  3.11 there is no stdlib parser at all, so either handle TOML textually and say
  so, or refuse it. Do not let behaviour vary silently by interpreter version.
- **Binary** — refuse. Decoding a `.zip` or `.mp4` as text yields garbage that
  verifies clean precisely because nothing matched; the worst combination.

## Verification under streaming

Verify each chunk before its output joins the staged file, then rescan the whole
staged artifact before releasing it. A chunk that fails contributes nothing, so a
run that stops partway leaves no partially redacted file at the destination —
the fail-closed guarantee survives being made incremental.

Keep a run-scoped, in-memory ledger of values the model has already identified,
and apply it deterministically to later chunks, so `Smith` alone in chunk 7 is
still caught after `Jane Smith` in chunk 1 scrolled away. The ledger is a store
of the very values you are removing: never write it to disk, never let it outlive
the run, and if you cap it, say so on stderr rather than degrading silently.

## Pipes

Stream a pipe forward-only with a bounded in-memory carry buffer. Do not spool
stdin to a temporary file to make it seekable — that writes the unredacted input
to disk, and "we delete it afterwards" is the assurance this skill replaces.

## Reporting

Print counts and sizes only, never values: `chunk 7/40, 100 KB, budget 100 KB`.
State which path a run took, so a reader cannot mistake a per-chunk guarantee for
a whole-document one.

## Concurrency

Layer 1 is the only CPU-bound stage, and it is a pure function over independent
atoms, so parallelism there is safe and cheap. Measure before adding a second
interpreter build to get it.

Measured on a 14-core Apple silicon machine (2026-11-10), scrubbing synthetic
support-thread text with all detectors firing:

| Corpus | Serial            | 4 workers | 8 workers        |
| ------ | ----------------- | --------- | ---------------- |
| 4 MB   | 0.46 s (8.7 MB/s) | 0.19 s    | 0.16 s           |
| 40 MB  | 4.62 s (8.7 MB/s) | 1.28 s    | 0.71 s (56 MB/s) |

Eight workers gave **6.49×** on the 40 MB corpus with match counts identical to
serial. `multiprocessing` therefore captures the available win on the ordinary
GIL-enabled interpreter; a free-threaded build buys nothing measurable here. Note
the limit of that measurement: it covers the deterministic pass only, on
synthesized text, on one machine. It is not evidence about regex throughput under
free threading, and it is not evidence about the model pass.

Parallelism belongs where ordering does not matter:

- **Layer 1 across atoms** — free, no ordering constraint, the measured win.
- **Model calls** — serial by default. The run-scoped ledger makes chunk *N+1*
  depend on chunk *N*'s findings, so fanning model calls out trades cross-chunk
  recognition for speed. Offer it as opt-in concurrency and keep document order in
  the assembled output; never let completion order decide byte order.

Whatever the worker count, the output must be byte-identical. If a change makes
output depend on scheduling, the change is wrong.

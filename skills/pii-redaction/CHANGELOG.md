# Changelog

All notable changes to the `pii-redaction` skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

______________________________________________________________________

## 2026-11-11 — The tool lives with the skill

### Added

- `scripts/pii-redactor` — the working implementation, moved here from
  `chezmoi/home/bin/executable_pii-redactor`. It specifies a tool, so it now
  ships one; installing the skill previously delivered the spec and none of the
  tool.
- `tests/` — the suite that grades the script, moved with it. `pytest` from the
  repository root runs it offline; `-m llm_judge` adds the model-calling cases.
- `pytest.ini` — registers `llm_judge` and excludes it from the default run.

### Changed

- The dotfiles `pii-redactor` is now a thin shim that resolves this skill's
  script at run time and `exec`s it, so `~/bin/pii-redactor` keeps working.

### Fixed

- The model's chain-of-thought no longer reaches stderr. `llm` was invoked
  without `-R/--hide-reasoning`, so a reasoning model narrated the redaction and
  quoted the values it was removing — measured at 13 occurrences of one name the
  released output had already replaced. stderr is kept in logs and scrollback,
  so that leak outlived the run while the output file looked clean.
- The suite graded whatever `~/bin/pii-redactor` held rather than the source
  under edit, so a change made in a worktree could pass without ever running.
  The harness now grades the skill's own script.

______________________________________________________________________

## 2026-11-10 — Input larger than memory or context

### Added

- `Behavior: Bounded memory and bounded model context` — a run bounds both
  memory and per-call context, and input that fits one budget keeps the
  single-call path byte-for-byte.
- `Behavior: Atoms are never split` — a line, top-level JSON value, YAML
  document or TOML table is indivisible; containers are descended into and an
  oversized atom refuses the run.
- `Behavior: Chunk boundaries are proven safe` — a carry window plus an edge
  rule, so an unproven boundary fails the run instead of leaking.
- `Behavior: Structure is preserved where the format permits` — JSON output is
  re-parsed, YAML states that structure is unverified, binary is refused.
- `Behavior: Streaming never weakens verification` — per-chunk gate before the
  staged artifact, final rescan before release.
- `Behavior: Cross-chunk recognition through a run-scoped ledger` — a fragment
  alone in a later chunk is still recognised; the ledger never touches disk.
- `Behavior: Refuse rather than degrade` — refusal names the reason, the
  location and the escape hatch.
- `references/streaming.md` — the operational detail for all of the above.
- Two eval cases: `atoms-are-never-split`,
  `chunk-boundaries-are-proven-safe`.
- `Behavior: Concurrency is an implementation detail` — opt-in, serial by
  default, byte-identical output at any worker count, and no free-threaded
  interpreter required.

### Changed

- The skill's trigger list now names input that exceeds memory or the model's
  context window, since the obvious fix for a size problem creates a new way to
  leak.
- Three constraints added: never let a chunk boundary become a redaction
  boundary, never persist input the run is removing in order to make it seekable,
  and never report a chunked run as a whole run.

### Notes

- `SKILL.md` grows one section that states the two rules and points at
  `references/streaming.md`; the mechanics stay out of the always-loaded file.

---
name: commit-hygiene
description: Keeps commits scoped to one logical change, sizes the message to the change rather than padding it, names the paths being committed so a concurrent process cannot contribute files, and checks afterwards that the commit contains what was intended. Use when committing work, dividing finished changes into commits, or reviewing whether a commit's scope and message match.
spec_hash: 204653837d70
---

# Commit Hygiene

Commits drift two ways at once: they absorb unrelated changes, and the message
grows to cover the sprawl. The length that should have warned you becomes the
camouflage. Treat message length as a **scope signal**, not a quality metric.

## Before committing

1. **List what changed.** `git status --short` and `git diff --stat`.
1. **Name the change in one line, without "and".** If you need "and", that is
   two commits. Split.
1. **Commit by path, never by index state** (see below).
1. **Check what you actually committed** — `git show --stat HEAD`.

## Splitting has a floor

Atomic means **self-contained**, not small. Never split so far that a commit
leaves the tree unbuildable or its tests red for the next commit to repair —
that breaks `git bisect` and makes every intermediate state a lie. Keep together
anything meaningless alone: a flag and the code that reads it, a rename and its
call sites, a signature change and its callers.

Split when a reader would ask "why is this here?", when one part could be
reverted while keeping the rest, when the subject needs "and", or when a
drive-by fix rode along with a feature.

## Size the message to the change

| Change                                               | Message                                         |
| ---------------------------------------------------- | ----------------------------------------------- |
| Mechanical — typo, rename, version bump, formatting  | Subject only                                    |
| Small, single-purpose — one function, a flag, a test | Subject + 1–2 sentences of why                  |
| Ordinary feature or fix                              | Subject + 1–2 short paragraphs                  |
| Large or security-sensitive                          | Up to ~200 words — **and reconsider splitting** |

Past roughly 200 words, stop writing and re-read the diff. A body that keeps
growing is the commit telling you it contains more than one idea. Split it; each
piece then needs far less explaining, because each one is about a single thing.

Never pad. A one-word typo fix with a three-paragraph body is worse than no
body: it trains readers to skip your messages.

## Write why, not what

The diff shows what changed. The message carries what the diff cannot: the
problem, why this approach over the obvious one, and any consequence worth a
warning.

Leave out the process ("first I tried X, then Y"), and leave out enumerations
the diff already makes plain — if you added eleven validators, say why
validation was needed and what breaks without it, not what each one matches.

## Commit by path, not by index

`git commit` commits **the whole index**. Anything another process, session, or
hook has staged rides along under your message.

```sh
git commit -o path/to/file another/file -m "..."   # --only: exactly these paths
git commit -m "..." -- path/to/file                # equivalent; pathspec implies --only
```

Both forms ignore the rest of the index entirely. Prefer `-o` where a project
has settled on it — it names the intent (`--only`) instead of relying on the
reader knowing that a bare pathspec implies it. Use it whenever
anything else might be touching the repo — a parallel agent, a watcher, a
teammate's script. `git add -A` and bare `git commit` are how unrelated files
end up under someone else's subject line.

## Then verify

```sh
git show --stat HEAD
```

Confirm the file list is exactly what you meant. If it is not, **say so** —
report the mismatch rather than the commit. A commit that succeeded is not a
commit that is correct, and this check costs one command.

## Worked example — a commit that should have been four

A single commit carried: a new deterministic redaction layer, a verification
layer, a Python compatibility fix, and a test-fixture change. Its message ran 51
lines and enumerated all eleven detector classes. It should have been:

```
pii-redactor: add a deterministic pass before the model
pii-redactor: verify the output before writing it
pii-redactor: keep annotations lazy so 3.9 still runs it
tests: stop mocking the model as a pass-through
```

Each subject fits in one line without "and". Each body is two or three
sentences, because each commit is about one thing. The eleven classes need no
enumeration — they are the diff.

The same commit also swept in 52 unrelated files, because it was made with
`git add` plus a bare `git commit` while another session had files staged. Both
failures, once. The pathspec form and the post-commit check each prevent it
independently.

## Repo-specific conventions still win

This skill is portable. Where a repository documents its own commit conventions
— scope vocabulary, subject format, worked examples from its own history — read
and follow those; they are more specific. The dotfiles repo keeps its version in
`docs/CONVENTIONS.md` under "Commit granularity".

## Never

- Never sweep unrelated modified files in to get a clean tree.
- Never stage a whole directory when only some of its files belong to the change.
- Never lengthen the message to justify an overgrown commit.
- Never rebase, amend, or force-push history others may have built on to fix
  scope or wording. Propose the options and let the owner choose.

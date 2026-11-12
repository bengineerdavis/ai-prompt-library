---
id: DOC-1
title: 'Start here: pii-redactor streaming implementation handoff'
---

# Start here: pii-redactor streaming implementation handoff

Read this before opening any task. It exists because the design work happened in a
different session from the implementation, and the decisions are not all visible
from the code or the task descriptions.

## What is being built and why

`pii-redactor` redacts PII from text in three layers: deterministic detectors,
then a model pass, then leak verification that fails closed. It reads the whole
input into memory and sends it to the model in one call.

The user's live case needs 12,234,508 tokens against a 262,144 context limit, so
the tool currently cannot process it at all. The refactor makes both memory use
and model context bounded, without weakening the guarantee that nothing unverified
is ever emitted.

## Where things live

| Artifact                            | Location                                                                                                       |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Script (the thing being changed)    | `~/.local/share/chezmoi/home/bin/executable_pii_redactor` — note: chezmoi repo, a DIFFERENT repo from this one |
| Tests                               | `~/.local/share/chezmoi/tests/pii_redactor/` (7 files, ~1180 lines)                                            |
| Spec (source of truth for behavior) | `skills/pii-redaction/spec.md` in THIS repo                                                                    |
| Operational detail                  | `skills/pii-redaction/references/streaming.md`                                                                 |
| Tasks                               | `backlog/`, prefix APL                                                                                         |
| Research                            | `research/anonymization-models/README.md`                                                                      |

Implementation happens in a chezmoi worktree, not here. This repo holds the spec.

## Decisions already locked — do not re-litigate

These came from 23 grilling questions. Reversing one without new evidence wastes a
day and is exactly what happened twice already in the design session.

- **Atoms are never split.** Text: a line. JSON: members of the top-level
  container, descending recursively until a member fits, never splitting a scalar.
  YAML: a `---` document. TOML: a table. NDJSON: one line.
- **A chunk boundary must never become a redaction boundary.** Carry window plus
  an edge rule: a match touching the window edge widens and rescans, and refuses
  past a cap.
- **Two paths, not one.** Input that fits one budget keeps the byte-identical
  single-call path. Chunking is for input that does not. This protects a 1180-line
  test suite and was a deliberate reversal of an earlier always-stream decision.
- **Three flags only:** `--chunk-bytes`, `--max-chunks`, `--plan`. `--plan` prints
  the plan to stderr and exits without calling the model. It is also the chunker's
  test seam at the CLI boundary.
- **Never add a verification-skip flag.** Verification is the only guarantee.
- **Never truncate.** Refuse and name the escape hatch instead.
- **Placeholders collapse** (`[NAME]`, not `[NAME-1]`) — but see APL-15/16: this is
  right for REDACT and wrong for PSEUDONYMIZE, which is a separate mode.
- **Concurrency is an implementation detail.** Serial by default, opt-in
  `--concurrency N`, byte-identical output at any worker count, document order
  preserved. Does not require a free-threaded interpreter.

## Known traps

1. **Two detectors are unbounded across newlines** — `har_cookie_json`
   (`[^\]]*`) and `har_auth_json` (`[^"]*`). No fixed carry window can be proven
   sufficient against them. They must be bounded to single lines. APL-2 and
   APL-17 both touch this; land it once, as a rule edit with a test.
1. **`tomllib` needs Python 3.11+**, but the script header claims 3.9 compatibility
   via `from __future__ import annotations`. On a 3.9 box TOML parsing silently
   behaves differently. APL-9 decides this; do not add a 3.11-only import without
   addressing it.
1. **`llm` 0.37.1 has no context-window introspection** and no incremental
   reading. The chunk budget is a chosen constant, not derived from the model.
   `llm` also requires provider-prefixed model names — `qualify_model()` handles
   bare ollama tags.
1. **The test harness prefers the deployed `~/bin/pii-redactor` over the source.**
   A stale deployed copy makes tests pass against old code. Run
   `chezmoi apply` after editing the source, or the suite tests the wrong thing.
1. **Fail-closed staging**: output goes to a temp file and is renamed only after
   verification passes. Per-chunk output must join that staging file only after
   its own gate passes.

## Verification discipline

- `npx -y @sentry/skillet@latest` — never bare `skillet`.
- After editing `spec.md`: format → render `SKILL.md` → pin `spec_hash` LAST.
  A formatter run after rendering rotates the hash and leaves the pin stale.
- `pre-commit run --files <paths>`, not `--all-files` (the auto-fixers rewrite
  untouched files across the tree).
- **KNOWN BLOCKER**: `alint` rule `installable-skills-are-valid` currently fails on
  `skills/support-partner-deep-research/` because 5 eval cases reference fixtures
  that were never created. It is byte-identical to main and is not caused by this
  branch. Do not bypass it and do not fix another session's skill without asking.

## Suggested order

APL-1 (streaming path) → APL-2 (boundary safety) → APL-3 (stream verification) →
APL-4 (binary/stdin/structured limits). APL-2 and APL-3 are blocked by APL-1.

Start by reading `skills/pii-redaction/spec.md` — it is the contract, and it is
already written. Then APL-1.

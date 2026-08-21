---
name: pii-redaction
description: Builds and reviews PII redaction tools as three layers — deterministic patterns, then a model pass, then leak verification that fails closed. Use when writing or reviewing any script that strips, masks, or anonymises personal data from text, or that sends user content to a model and writes a result meant for sharing.
spec_hash: 3816d53fd657
---

# PII Redaction

A redaction tool that fails looks exactly like one that works: a plausible file
either way, and nobody re-reads it before sharing. Never treat a model's exit
code as proof that anything was redacted.

Build redaction as three layers. All three are required.

## Layer 1 — Deterministic pass, before the model

Redact everything mechanically decidable with patterns first. The model must
never receive these values at all:

| Class                 | Notes                                     |
| --------------------- | ----------------------------------------- |
| Email addresses       |                                           |
| Phone numbers         | international and local forms             |
| IPv4 / IPv6 / MAC     |                                           |
| National identifiers  | SSN and equivalents                       |
| Payment cards         | validate with Luhn to cut false positives |
| Cloud access keys     | `AKIA…`, service account blobs            |
| Bearer tokens, JWTs   | `eyJ…` three-segment form                 |
| URLs with credentials | `https://user:pass@…`, `?token=…`         |

Replace with typed placeholders — `[EMAIL]`, `[PHONE]`, `[CARD]` — so the
result stays readable and later layers can tell what was removed.

Never shrink this layer because the model "handles those too." Patterns are
deterministic; a 9B model is not.

## Layer 2 — Model pass, for what patterns cannot decide

Send the already-redacted text to the model for the contextual classes: personal
and organisation names, street addresses, individual job titles, free-text
identifiers. Instruct it to preserve structure, markdown, and the placeholders
layer 1 inserted.

Disable prompt logging on the call. With the `llm` CLI that is `-n`
(`--no-log`) — without it every prompt lands in its SQLite history, which is
precisely the data you were asked not to accumulate.

## Layer 3 — Verification, over the output

Re-run the layer 1 detectors against the model's candidate output. Any
high-confidence hit is a failed run, not a warning. Also fail when:

- **The model returned what it was sent, byte-for-byte, while contextual PII
  remains in that text.** Test the *remaining* text, not "the document had PII":
  layer 1 has already taken the decidable classes out, so a document whose only
  PII was an email address correctly comes back untouched. Failing on the wrong
  condition rejects valid runs — use a conservative name/address shape check on
  what you sent to decide whether the model owed you any work.
- **The output is refusal-shaped** — a short "I can't help with that" instead of
  a redacted copy. Length collapse against the input is the usable signal.

Worked example — the failure this whole skill exists to prevent:

```sh
# a model that ignores the instruction, i.e. `llm` replaced by `cat`
$ printf 'Reach me at jane@example.com\n' > in.md
$ scrub -i in.md -o out.md
$ diff in.md out.md && echo "IDENTICAL"
```

If that run exits 0 and writes `out.md`, the tool is broken. It must exit
non-zero and write nothing.

## Fail closed on the output path

Stage to a temp file beside the destination and rename only after verification
passes. Writing straight to the output truncates it up front, so a mid-run
failure destroys the last good redaction. Remove the staging file on every
failure path, including the one where you exit early.

## Never

- Never write, print, or return content that has not passed verification — and
  never add a flag that skips verification but still produces output.
- Never exit zero when verification failed, was skipped, or could not run. A
  missing model or detector is a failure, not a pass.
- Never delegate the layer 1 classes to the model.
- Never put unredacted input into logs, progress output, or error messages.
  Report the class and count that leaked ("1 email address survived
  verification"), never the value.

## Reviewing tests for a redaction tool

A suite that stubs the model as a pass-through and asserts only on exit status
or file non-emptiness is green *precisely when the tool leaks*. Any test
claiming to prove redaction must assert that the input's PII is absent from the
output.

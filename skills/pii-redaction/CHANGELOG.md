# Changelog

All notable changes to the `pii-redaction` skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

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

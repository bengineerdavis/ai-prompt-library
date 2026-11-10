---
id: APL-3
title: 'Stream verification: per-chunk gate, final rescan, run-scoped ledger'
status: To Do
created_date: 2026-11-10 21:50
labels:
- pii
- streaming
- security
dependencies:
- APL-1
updated_date: 2026-11-10 23:08
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Why: layer 3 is a whole-output judgement today, which conflicts with streaming unless output is staged. The fail-closed guarantee has to survive being made incremental.

Ship: each chunk gated before its output joins the staging file, the assembled artifact rescanned before release, and a run-scoped in-memory ledger so a name fragment in a later chunk is still caught after the fuller form scrolled out of view.

The ledger is a store of the very values being removed: never on disk, never outliving the run, and capped with a stderr note rather than degrading silently.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A chunk that fails its gate contributes nothing; after a mid-run failure the destination is absent or holds its previous content, and no staging file remains
- [ ] #2 The final rescan runs over the completed staged artifact and still fails the run on a surviving match
- [ ] #3 JSON/NDJSON output is re-parsed in the rescan and a parse failure fails the run
- [ ] #4 A surname appearing alone in a later chunk is redacted via the ledger, and no ledger content appears in any file the run writes
- [ ] #5 The verification-skip surface stays empty; no new flag can produce output without passing verification
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:IMPLEMENTATION_NOTES:BEGIN -->
Concurrency interaction (2026-11-10): the ledger is the reason model calls are serial by default. If opt-in parallel model calls land, the ledger must still be applied in document order as each chunk completes, never speculatively — correctness must not depend on race ordering.
<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->

<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done
<!-- DOD:BEGIN -->
<!-- DOD:END -->

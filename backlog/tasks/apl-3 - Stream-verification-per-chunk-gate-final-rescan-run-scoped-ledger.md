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
updated_date: 2026-11-11 03:27
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Why: layer 3 is a whole-output judgement today, which conflicts with streaming unless output is staged. The fail-closed guarantee has to survive being made incremental.

Ship: each chunk gated before its output joins the staging file, the assembled artifact rescanned before release, and a run-scoped in-memory ledger so a name fragment in a later chunk is still caught after the fuller form scrolled out of view.

The ledger is a store of the very values being removed: never on disk, never outliving the run, and capped with a stderr note rather than degrading silently.

UPDATE 2026-11-10: the substitution step that verification checks is no longer placeholder-only.

An earlier scope fence took placeholders only, put a surrogate engine AND a pii-map out of scope, and that was wrong: a fixed tag collapses every person into one referent and destroys exactly the context a pseudonymisation requirement exists to preserve. APL-15 adopts the existing in-tree engine, and APL-16 makes redact vs pseudonymise an explicit mode.

Consequences for this task:
- The per-chunk gate must verify whichever mode ran. In pseudonymise mode the check is that values were consistently substituted, not merely that no detected value survived.
- The ledger and the surrogate engine are different stores with different lifetimes and must not be conflated. The ledger holds MODEL-identified candidate values for cross-chunk recognition and dies with the run. The surrogate mapping is the "additional information" under EDPB 01/2025 and its retention is a separate decision (APL-16). Do not let the ledger become a de facto map.
- The stderr counts must report the mode, because the two produce artifacts with different legal status.

Unchanged: the run-scoped ledger never touches disk, and no chunk's output reaches the staging file before its gate passes.
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

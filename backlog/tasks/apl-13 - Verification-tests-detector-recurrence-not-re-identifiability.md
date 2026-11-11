---
id: APL-13
title: Verification tests detector recurrence, not re-identifiability
status: To Do
created_date: 2026-11-11 02:55
labels:
- pii-redaction
- verification
- research-followup
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Raised by research/anonymization-models (2026-11-10), from NeMo Anonymizer's latent-entity argument.

pii-redactor's layer 3 re-runs the SAME detectors over the model's output and fails if any fires again. That proves no *detectable value* survived. It does not prove the text is not re-identifiable, and for a support capture it is usually the inference path that identifies someone, not a name.

Their canonical example: replace "Seattle" with "a generic city" and the text still says Space Needle, ferries to Bainbridge, a Mariners game, Puget Sound, persistent rain. No single clue identifies the city; together they reconstruct it with high confidence. NeMo calls these latent entities, and notes they are also *created* by naive replacement.

This connects to something docs/pii.md already describes (quasi-identifiers, the cardinality test), but as a caveat rather than a gate. Our tooling has no gate for it at all.

What a gate would need to answer: given the redacted output, can the protected fact still be inferred? That is not a detector question. Options worth weighing:
- An adversarial LLM pass that tries to infer protected attributes from the output and reports what it reconstructed (NeMo's attack step). Model-judged, so it has to be measured before being trusted.
- A concrete-example discipline instead of a gate: report the inference pathway in the run output ("this output still supports inferring X from Y and Z"), leaving the decision to a human. Cheaper, honest, no false authority.
- Bucket/cardinality checks on quasi-identifier combinations, which are mechanical but only cover what we enumerate.

Constraint from the user's standing preference: any residual-risk warning must name a concrete re-identification example, not assert risk in the abstract.

Do not let this weaken the existing layer 3. Detector recurrence stays as-is and keeps failing runs — it is necessary. This is about what it does not cover.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A written position on whether re-identification resistance is a gate, a warning, or out of scope, with the reasoning recorded
- [ ] #2 If a gate: its judgement method is measured before adoption, and unmeasured dimensions are stated as unmeasured
- [ ] #3 If a warning: the output names a concrete inference pathway, not an abstract risk
- [ ] #4 The existing detector-recurrence layer is unchanged and still fails runs
- [ ] #5 The decision is linked from research/anonymization-models/README.md
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:IMPLEMENTATION_NOTES:BEGIN -->

<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->

<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done
<!-- DOD:BEGIN -->
<!-- DOD:END -->

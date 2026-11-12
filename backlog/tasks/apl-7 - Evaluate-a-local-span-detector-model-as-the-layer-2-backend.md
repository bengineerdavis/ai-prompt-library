---
id: APL-7
title: Evaluate a local span-detector model as the layer-2 backend
status: To Do
created_date: 2026-11-10 21:50
labels:
  - pii
  - model
  - research
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Why: bardsai/eu-pii-anonimization-multilang-v2-preview (HF, revision bea7d79, apache-2.0) is a token-classification model covering 36 entity classes across 24 EU languages, including GDPR Article 9 special categories (health, biometric, genetic, political opinions, religious belief, sexual orientation, ethnic origin, trade union) plus a generic DATE class. That coverage is what patterns cannot reach and a small rewriting LLM handles badly.

Its output shape is also better than the current model pass: it returns SPANS rather than rewritten text, so the engine owns substitution, consistency and verification — raise's text_redact contract — which removes the whole "the model silently rewrote the document" failure class.

Why not now: it needs torch/transformers, breaking the script's stdlib-only line; it is a rolling preview whose output changes between checkpoints, which is hostile to a tool whose value is verified results; and xlm-roberta is capped at 512 subword tokens, so it must be chunked anyway with no long-range context (a name split across chunks is missed outright, with no overlap allowance).

The current refactor keeps the layer-2 seam as text -> candidate text so a span backend can be adapted later.

Model card caveats: the quick-start snippet names bardsai/eu-pii-anonimization-multilangv2 but the repo id is ...-v2-preview, so the snippet does not resolve as written. Any adoption must pin a revision.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [ ] #1 Article 9 recall and precision measured on synthesized cases at several thresholds, with the measurement conditions stated
- [ ] #2 Whether a ~1.2 GB torch stack belongs in a bin/ script is answered, with the dependency cost stated
- [ ] #3 A pinned revision is recorded and the effect of preview drift on reproducibility is assessed
- [ ] #4 A recommendation on adopting, deferring or rejecting, with rejected options and their disqualifying reasons

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

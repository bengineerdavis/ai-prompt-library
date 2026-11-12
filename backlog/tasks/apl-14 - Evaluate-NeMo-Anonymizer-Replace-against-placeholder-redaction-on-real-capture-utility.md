---
id: APL-14
title: Evaluate NeMo Anonymizer Replace against placeholder redaction on real-capture utility
status: To Do
created_date: 2026-11-11 02:55
labels:
  - pii-redaction
  - anonymization
  - model-fitness
  - research-followup
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Research question settled in research/anonymization-models (2026-11-10): an off-the-shelf context-preserving rewriter does not exist as a standalone permissive artifact, but NVIDIA NeMo Anonymizer (Apache-2.0, pinned 7605c13) ships a Replace flow whose Substitute strategy produces realistic, internally consistent replacements instead of [NAME] placeholders.

The open question is whether that utility gain is real *for our captures*, and whether it is worth the configuration work. This is a model-fitness question: it needs a measured run on the deciding machine, not a reading of vendor claims. Every number in the research note is author-reported on the authors' corpus.

Two disqualifying defaults must be fixed before anything real goes through it:

- Default LLM provider is OpenRouter (OPENROUTER_API_KEY), with build.nvidia.com as the other documented endpoint. Both contradict the local-only constraint. Re-point via Anonymizer(model_providers=...).
- Telemetry is on by default, one event per run()/preview(). Docs say technical metadata only. Disable it unconditionally anyway (--no-emit-telemetry / emit_telemetry=False / NEMO_TELEMETRY_ENABLED=false) rather than trust the field list.
- Default detection wants a local GLiNER2 endpoint, so "local by default" is true for detection and false for the LLM stages.

Measurement shape: same capture, same questions answered downstream, compare (a) current pii-redactor placeholders, (b) NeMo Replace/Substitute. Utility = does a downstream model answer the same diagnostic questions correctly from each. Privacy = detector recurrence plus whatever the re-identifiability task concludes.

Do NOT adopt Rewrite yet. It runs ~7 LLM roles plus up to 3 repair rounds with adversarial attack calls per record; on a 154-entry HAR that is thousands of calls. Replace first, measure, then decide if Rewrite earns its cost.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [ ] #1 NeMo Anonymizer runs fully locally with telemetry disabled, demonstrated by an invocation log showing no external endpoint and no telemetry event
- [ ] #2 A measured comparison on one real capture reports downstream answer accuracy for placeholders vs realistic substitutes
- [ ] #3 The measurement states its conditions (model, quantisation, context, resident models) beside every claim
- [ ] #4 Unmeasured dimensions are reported as unmeasured, not inferred
- [ ] #5 A recommendation either adopts Replace, rejects it with the measured reason recorded, or defers it with a revisit trigger
- [ ] #6 Findings recorded against research/anonymization-models/README.md

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

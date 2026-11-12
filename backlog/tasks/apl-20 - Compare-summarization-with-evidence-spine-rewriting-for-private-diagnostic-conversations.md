---
id: APL-20
title: Compare summarization with evidence-spine rewriting for private diagnostic conversations
status: Done
created_date: 2026-11-12 14:54
dependencies:
  - APL-19
labels:
  - research
  - privacy
  - summarization
documentation:
  - research/evidence-spine-privacy/README.md
  - research/diagnostic-summarization/README.md
updated_date: 2026-11-12 14:56
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Summarization may be a lower-latency alternative to the evidence spine or a useful preprocessing stage, but generic compression can discard diagnostic evidence, uncertainty, and identifying clue combinations. APL-19 completed the evidence-ledger and council research; this task evaluates summarization explicitly as a competing and complementary approach.

Ship:

- A primary-source comparison of generic, task-conditioned, extractive/abstractive, and dialogue/log/incident summarization.
- An experiment comparing direct summarization, evidence-ledger rewriting, and summary-assisted evidence extraction under the same synthesized cases.
- A testing matrix for factual coverage, temporal/causal fidelity, privacy, downstream utility, and conversational latency.

Constraints:

- Preserve APL-19 as completed research; do not silently widen its scope.
- Distinguish generic summarization from task-conditioned and evidence-constrained summarization.
- Compare each approach against direct substitution and the evidence-ledger baseline using synthesized incidents only.
- Measure direct and inferential privacy separately from answer quality, latency, and call count.
- Do not change the release engine or derive fixtures from real customer material.

Agreed with the maintainer 2026-11-12: test summarization as both a competing and complementary option.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [x] #1 Research/diagnostic-summarization/README.md compares generic, task-conditioned, extractive/abstractive, and dialogue/log/incident summarization with primary-source citations.
- [x] #2 The report specifies direct-summary, evidence-ledger, and summary-assisted extraction arms with clear hypotheses and boundary conditions.
- [x] #3 The testing matrix measures factual coverage, temporal/causal fidelity, direct and inferential privacy, downstream diagnostic utility, p50/p95 latency, and local model-call count separately.
- [x] #4 The task board displays the complete description and acceptance criteria for this new task.

<!-- AC:END -->

## Implementation Notes

<!-- SECTION:IMPLEMENTATION_NOTES:BEGIN -->

2026-11-12: Research report completed at research/diagnostic-summarization/README.md. It specifies direct-substitution control, direct-summary competitor, evidence-ledger baseline, summary-assisted extraction, and selective summary+ledger arms. Recommendation: include task-conditioned evidence-attributed summarization as a first-class arm, but require identical factual/temporal/privacy checks and measured end-to-end latency; generic compression is not sufficient. No local model experiment was run and no release engine changed.

<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->

Completed research/diagnostic-summarization/README.md and linked it from research/README.md. The report defines direct substitution, direct summary, evidence ledger, summary-assisted extraction, and selective summary+ledger arms. It recommends task-conditioned evidence-attributed summarization as a measured alternative/complement, not generic compression, with shared factual/temporal/privacy checks and separate utility, compression, and p50/p95 latency measurements. The backlog task view displayed the full description and acceptance criteria before completion. No model experiment was run and no release engine changed. Scoped pre-commit passes except the pre-existing support-partner-deep-research missing-fixture alint failure, which was not modified or bypassed.

<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done

<!-- DOD:BEGIN -->

<!-- DOD:END -->

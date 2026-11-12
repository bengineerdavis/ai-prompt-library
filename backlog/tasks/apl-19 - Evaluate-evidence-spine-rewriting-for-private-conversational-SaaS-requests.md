---
id: APL-19
title: Evaluate evidence-spine rewriting for private conversational SaaS requests
status: Done
created_date: 2026-11-12 14:47
dependencies:
  - APL-13
labels:
  - research
  - privacy
  - pseudonymisation
documentation:
  - research/anonymization-models/README.md
  - research/anonymizer-slm/README.md
  - research/evidence-spine-privacy/README.md
updated_date: 2026-11-12 14:53
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

The proposed evidence spine must preserve diagnostic facts and causal ordering while removing direct and inferential identifiers. The privacy path must support interactive SaaS exchanges, where multi-stage model pipelines and unbounded latency are unsuitable. A model council may improve coverage or adversarial review, but must justify its calls through measured gains rather than assumed robustness.

Ship:

- A sourced comparison of outline-based reconstruction, privacy beyond entity replacement, and fidelity verification.
- A recommended synchronous architecture separating online privacy transformation from offline evaluation.
- A minimal experiment measuring extraction fidelity, reconstruction fidelity, privacy leakage, downstream utility, p50/p95 latency, and local model-call count separately.
- A domain-specific testing strategy distinguishing synchronous release checks from offline adversarial evaluation, judge calibration, and downstream-answer comparison.
- A comparison of a single small model, same-model sampling, a genuinely diverse parallel council, and a larger single model for candidate extraction and adversarial review.

Constraints:

- Ground material claims in primary sources with pinned citations; distinguish published results from local measurements.
- Do not change the release engine or derive fixtures from real customer material.
- Do not combine privacy, utility, and latency into an overall score.
- Never send raw material or its mapping to a SaaS provider; refuse rather than bypass verification when a deadline expires.
- Do not average away dissent or treat majority agreement as proof of safety; a credible high-confidence leak must override pass votes.
- Compare diverse model families separately from repeated samples of one model and include larger-model and retry/escalation baselines.
- Relate recommendations to APL-13 without duplicating its re-identification-gate scope.

Agreed with the maintainer 2026-11-12: add conversational/transactional latency as a hard architectural constraint.
Agreed with the maintainer 2026-11-12: include general and domain-specific evaluation and testing approaches.
Agreed with the maintainer 2026-11-12: investigate small-model panels and fusion patterns for extraction and adversarial review.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [x] #1 Research/evidence-spine-privacy/README.md compares outline reconstruction, inferential privacy, and fidelity verification with primary-source citations and records rejected alternatives.
- [x] #2 The report recommends an online/offline split with deterministic verification before any SaaS request and explicit timeout/refusal behavior.
- [x] #3 The experiment specifies separate measures for extraction, reconstruction, privacy, downstream utility, p50/p95 latency, and local model-call count using synthesized cases.
- [x] #4 The task board displays APL-19 with the complete description and all acceptance criteria.
- [x] #5 The report specifies synchronous release checks, offline adversarial tests, synthesized fixture design, counterfactual fidelity tests, judge calibration, diagnostic-answer comparison, and latency benchmarking, with the evidence each approach can and cannot establish.
- [x] #6 The report evaluates candidate-union and adversarial-review fusion against complete-rewrite fusion and debate, specifies same-model versus diverse-family comparisons, and preserves dissent rather than using majority agreement as proof of safety.

<!-- AC:END -->

## Implementation Notes

<!-- SECTION:IMPLEMENTATION_NOTES:BEGIN -->

2026-11-12: Added effective general and domain-specific eval/testing research at maintainer request. Focus is the release/offline split: cheap deterministic checks per exchange; calibrated judges, adversarial inference tests, counterfactual cases, downstream-answer evaluation, and performance benchmarking outside the request loop.
2026-11-12: Council scope added. Leading candidate is independent role-specialized proposals with deterministic provenance/fusion, not debate or majority safety voting. Measure added p95 latency, model-call count, unique valid detections, unsupported additions, and residual inference findings against one-model and larger-model baselines.
2026-11-12: Research report completed at research/evidence-spine-privacy/README.md. It recommends a session-stable validated evidence ledger and bounded renderer; keeps attack/repair and councils offline by default; specifies synchronous checks, synthetic and adversarial testing, downstream utility, latency/resource measurements, and a same-model/diverse-family/larger-model council ablation. Promptfoo 0.125.1 is optional for an offline trial, with cache and telemetry disabled; incumbent pytest/Hypothesis probe remains the baseline. No model experiment was run and no release engine changed.

<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->

Completed research/evidence-spine-privacy/README.md and linked it from research/README.md. The report recommends a session-stable validated evidence ledger with a bounded renderer, a synchronous fail-closed request path, and offline adversarial/utility/latency evaluation. It distinguishes same-model sampling, diverse councils, larger models, and retry/escalation; recommends deterministic candidate fusion and dissent-preserving adversarial review rather than majority safety voting. It specifies synthetic fixtures, deterministic/property tests, fidelity/privacy/utility metrics, judge calibration, fault injection, and p50/p95/resource measurements. Promptfoo 0.125.1 was verified as an optional offline matrix runner, not adopted. The backlog board displayed the complete description and acceptance criteria before completion. No local model experiment was run and no release engine changed. Scoped pre-commit checks pass except the pre-existing support-partner-deep-research missing-fixture alint failure, which was not modified or bypassed.

<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done

<!-- DOD:BEGIN -->

<!-- DOD:END -->

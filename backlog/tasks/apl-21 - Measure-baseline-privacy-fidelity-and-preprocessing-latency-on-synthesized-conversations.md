---
id: APL-21
title: Measure baseline privacy, fidelity, and preprocessing latency on synthesized conversations
status: To Do
created_date: 2026-11-12 15:08
dependencies:
  - APL-19
  - APL-20
labels:
  - experiment
  - privacy
  - latency
priority: high
documentation:
  - research/evidence-spine-privacy/README.md
  - research/diagnostic-summarization/README.md
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

APL-19 and APL-20 researched evidence-ledger rewriting, councils, and summarization. This task runs the smallest discriminating experiment before adding further architecture. Start with direct substitution, one task-conditioned summary, and one evidence-ledger candidate on one short incident and one three-turn synthesized conversation. A council is an escalation only if the baseline reveals a specific coverage or adversarial-review gap.

Ship:

- A repeatable experiment script, input/result schemas, and synthesized fixtures.
- Baseline measurements for factual coverage, unsupported additions, direct privacy checks, and preprocessing latency.
- A documented decision on whether summarization or a council deserves a larger experiment.

Constraints:

- Do not change the release engine or send fixture material to a SaaS provider.
- Synthesize fixtures from problem classes, never transform real customer material.
- For a simple input of a few short paragraphs, target \<=2 seconds of local preprocessing before the SaaS request; record whether each candidate meets that target.
- Long instructions, substantial text, and binary evidence may have a larger workload-dependent budget when work is visible and the first result is useful. Measure preprocessing separately from evidence extraction, diagnosis, and SaaS response generation.
- Do not impose the short-text deadline on large artifacts or use it to justify unverified forwarding.
- Measure factual coverage, privacy, downstream utility, and latency separately; no aggregate safety score.
- Start with one small model. Add repeated samples, a larger model, or a council only to answer a measured baseline gap.

Agreed with the maintainer 2026-11-12: latency is workload-dependent. A few short paragraphs should complete local preprocessing in about two seconds or less; larger evidence can take longer when the first outcome is useful and expected.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [ ] #1 The experiment includes one short incident and one three-turn synthesized conversation with independent truth labels for required facts, direct identifiers, and diagnostic question.
- [ ] #2 The experiment compares direct substitution, task-conditioned summarization, and an evidence-ledger candidate with the same model and input conditions.
- [ ] #3 The report measures preprocessing p50/p95 separately from later analysis/SaaS stages and records whether the short-paragraph \<=2-second target is met.
- [ ] #4 The report records factual coverage, unsupported additions, direct privacy failures, prompt sizes, model calls, and cold/warm model conditions separately.
- [ ] #5 A larger-model or council comparison is run only if tied to a named baseline failure; otherwise it is explicitly deferred.
- [ ] #6 The task board displays the full experiment description and acceptance criteria before completion.

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

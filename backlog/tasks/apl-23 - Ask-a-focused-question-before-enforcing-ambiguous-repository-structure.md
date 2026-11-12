---
id: APL-23
title: Ask a focused question before enforcing ambiguous repository structure
status: Done
created_date: 2026-11-12 21:36
labels:
  - structure-authoring
  - behavioral-eval
references:
  - skills/structure-authoring/spec.md
  - skills/structure-authoring/SKILL.md
  - skills/structure-authoring/evals/cases/interview-only-on-decision-changing-choices.yaml
updated_date: 2026-11-12 21:38
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Why: the original structure-authoring behavioral follow-up, then numbered TASK-233, is absent from the authoritative APL store after its migration. The live focused-question case failed when the agent enforced an ambiguous layout and presented follow-up questions afterward. An initial repair also over-triggered on already declared preservation rules, and the final wording closes an observed loophole that permitted invented exemptions.

Ship:

- A rendered structure-authoring contract that asks ONE focused decision-changing question and waits before enforcement for a genuine conflict about artifact identity, disposition, or exception status, while enforcing declared non-destructive contracts without unnecessary consultation.
- Live behavioral evidence for all three existing cases, including earlier failures, diagnostic corrections, and remaining limitations.

Constraints:

- Use the existing interaction-questioning discipline; do not invent a combined questioning skill or turn one ambiguity into a questionnaire.
- Do not invent exemptions or baselines to make unresolved structure pass.
- Do not weaken the requirement to wait for the user's answer or let ordinary declared violations stall enforcement.
- Preserve synthetic fixtures and Skillet render/freshness conventions.
- A single-trial pass is not a stable pass rate; earlier failures remain part of the record.

Approved by the maintainer 2026-11-11 as the scoped behavioral follow-up. Recreated under the APL task-store prefix 2026-11-12 because the old TASK-233 record cannot be found.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [x] #1 The spec and rendered SKILL.md require one focused question and a wait before enforcement for genuine unresolved conflicts, while distinguishing declared non-destructive enforcement from ambiguity.
- [x] #2 The final focused-question trial passes with no enforcement before the answer, and both final executable-rule trials pass or an inconclusive timeout is explicitly recorded with its diagnostic disposition.
- [x] #3 npx -y @sentry/skillet@latest validate skills/structure-authoring passes.
- [x] #4 npx -y @sentry/skillet@latest status skills/structure-authoring --json reports a valid, non-stale render.

<!-- AC:END -->

## Implementation Notes

<!-- SECTION:IMPLEMENTATION_NOTES:BEGIN -->

Final measured evidence on rendered spec 7dbed27a2daa (structure-authoring 1.0.1), each latest case measured once: focused-question pass (19.6s); mixed-language executable rules pass (119.9s); skill-library executable rules pass (234.0s, temporary diagnostic timeout 1200s). Earlier focused-question attempts passed twice but the intermediate wording failed once by enforcing before asking; the final wording closes the observed exemption loophole. Earlier mixed-language wording over-triggered on declared preservation rules; the final wording restores enforcement. The first final skill-library trial hit Skillet's default 300s timeout and was inconclusive; the extended diagnostic passed. Authored eval cases were not changed. Single-trial passes do not establish a stable pass rate. Structural validation and freshness pass, and the current-main combined alint gate passes.

<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->

Delivered the focused-question gate for genuine artifact conflicts, with a separate declared-enforcement boundary. All three final behavioral cases passed their latest single trial, with intermediate failures and the extended timeout recorded.

<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done

<!-- DOD:BEGIN -->

<!-- DOD:END -->

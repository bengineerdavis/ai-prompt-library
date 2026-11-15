---
id: APL-27
title: Prepare upstream-conformant contribution candidates
status: To Do
created_date: 2026-11-14 18:55
updated_date: 2026-11-14 18:56
references:
  - ../templates/copier-cat/backlog/tasks/ccc-21 - Make-contribution-candidates-follow-upstream-contributor-conventions.md
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Reusable agent workflows can identify useful findings in one project and communicate them to another project. The receiving project’s contributor conventions determine the appropriate artifact and submission process; a generic GitHub issue or patch is not always correct.

Ship:

- Research comparing established upstream-contribution discovery, portable handoff, patch, issue, and pull-request workflows against the requirement to follow the receiving project’s current contributor instructions.
- A reusable skill that identifies the intended recipient, fetches its current contributor, agent, coding, security, support, and submission guidance, and selects the requested artifact and submission route.
- A contribution-candidate format carrying only relevant project-local evidence, reproduction and validation commands, provenance, scope boundaries, and unresolved questions in a reviewable portable document.
- An explicit review and consent boundary separating candidate preparation from target-project file changes, issue creation, pull requests, and other publication.
- Evaluation fixtures covering local-task feedback, repositories with contributor instructions, security-sensitive findings, no public submission channel, and a rejected premature GitHub-issue or patch proposal.
- A publication and integration handoff for the library, copier-cat contribution workflows, push-it-forward propagation, and the agentic project template.

Constraints:

- Treat upstream instructions as primary sources and verify the installed contribution tooling before relying on its behavior.
- Keep local findings in the source project’s configured tracker; link a real upstream reference only after the receiving project returns one.
- Do not equate a candidate with submission or an upstream issue with a local task.
- No target-project mutation, network publication, credential use, or global agent configuration change during authoring or evaluation.
- Use open skill standards, record rejected alternatives, and avoid creating another queue or contribution engine.

Agreed with the maintainer 2026-11-14: upstream submissions always use the upstream project’s conventions, documentation, and contributor requirements to communicate project-local findings.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [ ] #1 Research compares existing contribution workflows and records rejected options against upstream-convention compliance
- [ ] #2 The skill discovers the intended recipient and reads its current contributor requirements before choosing an artifact or submission route
- [ ] #3 The candidate format contains relevant evidence, validation commands, provenance, scope, and unresolved questions in a reviewable portable document
- [ ] #4 Candidate preparation is separate from target mutation and publication, which require explicit consent at the action
- [ ] #5 Evaluation fixtures cover contributor instructions, security-sensitive findings, unavailable submission channels, and rejected premature issue or patch proposals
- [ ] #6 The integration handoff addresses the library, copier-cat, push-it-forward, and agentic-template adoption
- [ ] #7 npx -y @sentry/skillet@latest validate skills/upstream-contribution --json passes for the authored skill
- [ ] #8 backlog-py board shows APL-27 with its full description and acceptance criteria

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

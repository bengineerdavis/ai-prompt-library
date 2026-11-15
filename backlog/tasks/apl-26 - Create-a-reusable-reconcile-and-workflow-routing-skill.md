---
id: APL-26
title: Create a reusable reconcile and workflow-routing skill
status: To Do
created_date: 2026-11-14 18:54
updated_date: 2026-11-14 18:56
references:
  - ../templates/agentic-project-template/backlog/tasks/apt-49 - Adopt-upstream-conformant-workflow-feedback-in-stamped-projects.md
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

The copier-cat design and stacked-PR sessions produced useful workflow lessons, but many independent skills and queues make the next usable step difficult to remember. Reconciliation needs to begin with the work already established in each repository, then preserve approved design and implementation scope through a small, explicit workflow boundary.

Ship:

- Research comparing existing reconciliation, branch-synchronization, task-queue, skill-router, and workflow-orchestration approaches against the requirement to preserve established work while reconciling semantic drift.
- A reusable skill with a short state-based route: reconcile repository and task state, capture findings in the configured tracker, identify the next usable vertical slice, expose only eligible queued work, and hand execution to a fresh implementation session.
- An MVP/exploration-boundary pattern that preserves open-ended design inputs without allowing them to expand the active implementation contract; usage-blocking classification and deferred ownership are explicit.
- A reconciliation pattern for stacks and divergent task records that starts from established work, records semantic conflicts and supersession, preserves unmerged evidence, and verifies the final aggregate rather than only branch ancestry.
- Evaluation fixtures covering competing established work, untracked specifications, completed-but-unpublished artifacts, and newly proposed scope that must not displace the MVP.
- A publication and template-integration handoff naming the skill’s library source, agents.toml declaration, agentic-layer deployment path, and optional installation behavior.

Constraints:

- Reuse backlog-py orchestration queue/eligible/claim and existing template wiring where their installed surfaces fit; do not build another queue, scheduler, or general agent framework.
- Use review-best-practices to compare existing approaches and record rejected options; JSON supports queue/claim automation but is not a substitute for semantic review.
- Use a small project spine for durable contracts and context pointers, not a new collection of always-loaded narrative documents.
- Do not modify Matt Pocock’s canonical skills; compose around them through the existing backlog-workflow adapter.
- Do not implement production orchestration, edit global agent configuration, or modify source templates as part of authoring the reusable component.
- Keep open decisions and unresolved ownership marked rather than silently resolved.

Agreed with the maintainer 2026-11-14: prioritize early semantic reconciliation, reduce workflow memorization, and make approved follow-ups reusable across maintained and stamped projects.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [ ] #1 Research compares existing reconciliation, queue, and routing approaches and records rejected options against preserving established work
- [ ] #2 The skill routes reconcile, capture, next-slice selection, and handoff through the configured tracker and existing backlog orchestration
- [ ] #3 An MVP contract keeps exploration inputs visible while separating usage-blocking work from deferred ideas
- [ ] #4 The reconciliation pattern biases established work, exposes semantic conflicts, preserves unmerged evidence, and verifies the final aggregate
- [ ] #5 Evaluation fixtures cover competing work, untracked specifications, unpublished artifacts, and proposed scope expansion
- [ ] #6 The integration handoff names library publication, agents.toml declaration, template deployment, and optional installation behavior
- [ ] #7 npx -y @sentry/skillet@latest validate skills/reconcile-workflow --json passes for the authored skill
- [ ] #8 backlog-py board shows APL-26 with its full description and acceptance criteria

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

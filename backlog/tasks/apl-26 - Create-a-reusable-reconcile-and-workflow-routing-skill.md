---
id: APL-26
title: Create a reusable reconcile and workflow-routing skill
status: To Do
created_date: 2026-11-14 18:54
updated_date: 2026-11-15 16:25
references:
  - https://github.com/bengineerdavis/copier-cat/blob/main/backlog/tasks/ccc-24%20-%20Assemble-Python-from-a-named-stack.md
  - https://github.com/bengineerdavis/agentic-project-template/blob/main/backlog/tasks/apt-49%20-%20Coordinate-workflow-feedback-in-stamped-projects.md
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
- [ ] #5 Evaluation fixtures cover competing work, untracked specifications, unpublished artifacts, proposed scope expansion, and a main checkout reporting eligible work while another worktree holds an expired claim; the fixtures distinguish an empty claim from a worktree with real uncommitted work and preserve the latter
- [ ] #6 The integration handoff names library publication, agents.toml declaration, template deployment, and optional installation behavior
- [ ] #7 npx -y @sentry/skillet@latest validate skills/reconcile-workflow --json passes for the authored skill
- [ ] #8 backlog-py board shows APL-26 with its full description and acceptance criteria

<!-- AC:END -->

## Implementation Notes

<!-- SECTION:IMPLEMENTATION_NOTES:BEGIN -->

Copier-cat origin case (2026-11-15): the main checkout's orchestration queue showed CCC-24 as eligible while its ccc-24-python-assembly worktree held an expired OpenCode lease and local claim history. The worktree had no implementation commits or source changes. Cleanup compared the actual diff and claim metadata before restoring only that claim state, then removed the worktree and branch. Do not rely on a main-checkout queue alone when routing work across worktrees.

Add an evaluation fixture for this shape: main reports eligible/todo/0; a separate worktree has a stale claim with no implementation; another worktree has a claim with real uncommitted work. The route must inspect claims and worktree evidence, preserve real work, and clean only the verified empty case. Cover lease expiry versus an active claim and multi-agent ownership. Use existing backlog-py orchestration surfaces where they fit; do not build another queue.

Relevant source records and evidence:

- https://github.com/bengineerdavis/copier-cat/blob/main/backlog/tasks/ccc-24%20-%20Assemble-Python-from-a-named-stack.md
- https://github.com/bengineerdavis/copier-cat/blob/main/backlog/docs/cc-assembly-mvp-spec.md
- https://github.com/bengineerdavis/copier-cat/tree/prototype/cc-assembly-ux/prototype/cc-assembly-ux
- Agentic workflow-adapter integration: https://github.com/bengineerdavis/agentic-project-template/blob/main/template/.agents/skills/backlog-workflow/SKILL.md.jinja
- Historical session origin: DOC-11 at https://github.com/bengineerdavis/copier-cat/blob/main/backlog/docs/seed-and-implementation-session-handoff.md and the handoff retirement at https://github.com/bengineerdavis/copier-cat/commit/c16c279de6a4d1a4d4bd40f97bb2671897c048a8

Attribution: this scenario and these resources came from the copier-cat session and its worktree-cleanup retro. The authored skill may incorporate the evidence and integration seam into its own reusable work; the source template is not modified by this record.

<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->

<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done

<!-- DOD:BEGIN -->

<!-- DOD:END -->

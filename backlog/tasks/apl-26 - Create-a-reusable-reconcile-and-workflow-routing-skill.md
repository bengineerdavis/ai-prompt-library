---
id: APL-26
title: Create a reusable reconcile and workflow-routing skill
status: Done
created_date: 2026-11-14 18:54
updated_date: 2026-11-16 05:48
references:
- https://github.com/bengineerdavis/copier-cat/blob/main/backlog/tasks/ccc-24%20-%20Assemble-Python-from-a-named-stack.md
- https://github.com/bengineerdavis/agentic-project-template/blob/main/backlog/tasks/apt-49%20-%20Coordinate-workflow-feedback-in-stamped-projects.md
orchestration:
  status_key: inprogress
  version: 3
  lease_owner: opencode-apl-26
  lease_expires_at: '2026-11-16T06:38:29.821865Z'
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

- [x] #1 Research compares existing reconciliation, queue, and routing approaches and records rejected options against preserving established work
- [x] #2 The skill routes reconcile, capture, next-slice selection, and handoff through the configured tracker and existing backlog orchestration
- [x] #3 An MVP contract keeps exploration inputs visible while separating usage-blocking work from deferred ideas
- [x] #4 The reconciliation pattern biases established work, exposes semantic conflicts, preserves unmerged evidence, and verifies the final aggregate
- [x] #5 Evaluation fixtures cover competing work, untracked specifications, unpublished artifacts, proposed scope expansion, and cross-worktree claims. The claim fixtures contrast an expired claim with an active one, distinguish an empty claim from real uncommitted work and preserve the latter, and cover multi-agent ownership
- [x] #6 The integration handoff names library publication, agents.toml declaration, template deployment, and optional installation behavior
- [x] #7 npx -y @sentry/skillet@latest validate skills/reconcile-workflow --json passes for the authored skill
- [x] #8 backlog-py board shows APL-26 with its full description and acceptance criteria

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
Authoring progress 2026-11-15:

- Research decision and rejected alternatives: research/reconcile-workflow/README.md.
- Executable skill: skills/reconcile-workflow/SKILL.md, derived from spec.md.
- MVP boundary, semantic reconciliation, native Backlog capture, cross-worktree and multi-agent claim handling, and fresh-session handoff are explicit behaviors.
- Five synthetic fixtures cover competing established work, unpublished artifacts, deferred scope, active/expired claims, multi-agent ownership, and implementation handoff.
- Integration handoff: research/reconcile-workflow/integration.md. Library declaration is [[skills]] name="reconcile-workflow" source="bengineerdavis/ai-prompt-library"; APT-49.3 owns later stamp-matrix deployment.
- Skillet validation and dry-run pass; first Claude behavioral run passed 2/5. Three cases are being inspected; no completion claim until their failures are addressed.
- Backlog discovery gotcha verified: always pass --cwd in nested worktrees. Backlog doctor detects duplicate IDs but doctor --fix cannot repair a filename/frontmatter ID mismatch; record the manual metadata repair and verify both tasks afterward.
Eval diagnosis: the first handoff fixture contradicted itself by calling CCC-24 unblocked while also assigning it an active owner. The agent correctly preserved that ownership; the judge expected a fresh-session handoff. Split ready-slice into an unclaimed, eligible task for the fresh-session case. Kept the competing-work fixture for ownership preservation. The tracker mock also accepted arbitrary operation names, so its check tested spelling rather than its adapter contract; it now exposes task_create and record_run and rejects unsupported operations. The handoff contract now explicitly writes a user-named destination file instead of only answering in chat. Focused claim-preservation and fresh-session cases pass after these corrections.
<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Authored skills/reconcile-workflow with a Skillet spec, executable SKILL.md, compact handoff reference, research decision, integration handoff, and five synthetic evaluation fixtures. The skill reconciles repository/worktree evidence, preserves established work and multi-agent ownership, captures findings through native Backlog, bounds the MVP, and hands off one eligible slice. Research compares native Backlog, the existing adapter, Git/Worktrunk, GitHub synchronization, and portable Agent Skills, with rejected alternatives recorded. APT-49.3 owns optional template deployment. Validation: Skillet JSON validation passes; five dry-run cases are non-vacuous; final Claude behavioral suite passes 5/5.
<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done

<!-- DOD:BEGIN -->

<!-- DOD:END -->

## Run History
<!-- SECTION:RUN_HISTORY:BEGIN -->
<!-- RUN_HISTORY_ENTRY:BEGIN -->
```yaml
event_id: run-2fdad5b5683849a28d7061ec4ce99776
type: claim_task
actor: opencode-apl-26
timestamp: '2026-11-16T01:01:47.033436Z'
result: succeeded
task_id: APL-26
from_status: todo
to_status: inprogress
metadata:
  lease_ttl_seconds: '3600'
```
Author the reusable reconciliation and workflow-routing skill
<!-- RUN_HISTORY_ENTRY:END -->
<!-- RUN_HISTORY_ENTRY:BEGIN -->
```yaml
event_id: run-0511a37842414a73b35da2db4903ed42
type: release_task
actor: opencode-apl-26
timestamp: '2026-11-16T05:38:28.514790Z'
result: succeeded
task_id: APL-26
from_status: inprogress
to_status: todo
```
Renew expired authoring lease after evidence-preserving validation work
<!-- RUN_HISTORY_ENTRY:END -->
<!-- RUN_HISTORY_ENTRY:BEGIN -->
```yaml
event_id: run-59bd9e3c32954fa98323df22d593c479
type: claim_task
actor: opencode-apl-26
timestamp: '2026-11-16T05:38:29.821920Z'
result: succeeded
task_id: APL-26
from_status: todo
to_status: inprogress
metadata:
  lease_ttl_seconds: '3600'
```
Complete final behavioral validation and publish APL-26
<!-- RUN_HISTORY_ENTRY:END -->
<!-- SECTION:RUN_HISTORY:END -->

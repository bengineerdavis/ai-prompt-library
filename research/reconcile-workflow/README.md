# Reconcile and workflow-routing approach

- **Owner:** APL-26.
- **Status:** approved for this skill's scope; implementation in the library only.
- **Reviewed:** 2026-11-15.
- **Next review:** when Backlog orchestration becomes cross-worktree aware, the configured adapter changes, or evaluation contradicts the preservation rules.

## Requirement

Choose the next usable implementation slice without losing established work, trusting a stale queue, creating another orchestration system, or allowing exploratory ideas to expand the active milestone.

The disqualifying capability is a system that claims global worktree ownership or requires a new scheduler. The projects already have Backlog tasks, dependencies, claims, and native Git/hosting tools.

## Decision

Use the configured Backlog adapter as the task and claim surface, with a small skill that reconciles semantic evidence across worktrees, captures findings, bounds the milestone, and hands off one eligible slice.

Backlog remains the source of task status, dependencies, and leases. It is not treated as proof of global availability. Worktree diffs and unpublished artifacts remain evidence that must be inspected.

## Compared approaches

| Approach                                                   | Decision                                     | Reason                                                                                                                                                                                   |
| ---------------------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `backlog-md-py` 2.2.0, installed locally                   | **Adopt as the task surface**                | Native Markdown task records, dependencies, claims, leases, queue/eligible views, run history, MCP, and CLI fit the requirement.                                                         |
| The agentic template's existing `backlog-workflow` adapter | **Compose, do not replace**                  | It already maps spec, tickets, implementation, triage, and decisions onto Backlog. The new skill supplies reconciliation and next-slice routing around it.                               |
| Git and Worktrunk                                          | **Use for evidence and lifecycle transport** | Git exposes worktrees and aggregate diffs; Worktrunk manages isolated work and merging. Neither resolves semantic task supersession.                                                     |
| GitHub branch synchronization and merge queues             | **Use only as optional transport**           | GitHub documents branch updates for compatibility and merge queues for combining changes with the latest base. Neither proves that a resulting diff preserves the intended requirements. |
| Agent Skills specification and progressive disclosure      | **Adopt for distribution**                   | A portable `SKILL.md` with a focused trigger and linked runtime reference fits hosts without requiring a proprietary plugin runtime.                                                     |
| A new scheduler, global lock service, or dashboard         | **Reject**                                   | Duplicates existing Backlog coordination and would add a second source of ownership truth.                                                                                               |
| Status- or ancestry-only reconciliation                    | **Reject**                                   | A main queue can miss worktree claims; ancestry can hide a semantically inferior aggregate diff.                                                                                         |
| One universal workflow skill containing every stage        | **Reject**                                   | Would duplicate Matt Pocock's flow and the existing adapter, and obscure the boundary between routing and implementation.                                                                |

## Evidence checked

- [Backlog.py repository](https://github.com/rmusser01/backlog-md-py), [architecture](https://github.com/rmusser01/backlog-md-py/blob/main/docs/architecture.md), and [integration documentation](https://github.com/rmusser01/backlog-md-py/blob/main/docs/integration.md). Local installed version: **2.2.0**.
- Local `backlog-py orchestration {queue,eligible,claims,stale-leases} --help` and JSON queue output. The queue item includes path, dependency IDs, effective status, lease owner/expiry, queue category, validation issues, and version. Claim requires actor and expected version; this lease is local evidence, not a distributed lock.
- [Agent Skills specification](https://agentskills.io/specification) and [skill-creation practices](https://agentskills.io/skill-creation/best-practices), unversioned pages accessed 2026-11-15. Metadata supports discovery; full instructions load on activation; linked references provide progressive detail.
- [GitHub: keeping a pull request in sync with its base](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch), accessed 2026-11-15. Updates catch conflicts and compatibility problems; semantic review remains necessary.
- [GitHub: managing a merge queue](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue), accessed 2026-11-15. Merge groups validate combined changes; this is transport and verification, not task-ownership adjudication.
- Local `git worktree list --porcelain`, `wt merge --help`, and `gh pr update-branch --help`. Worktrunk and GitHub can mutate or clean up work, so the skill does not invoke those operations during routing.
- Existing adapter: `template/.agents/skills/backlog-workflow/SKILL.md.jinja` in `bengineerdavis/agentic-project-template`, read from `origin/main` on 2026-11-15.

## Limitations

Backlog 2.2.0 does not automatically enumerate another worktree's claims in the main checkout's queue. The skill must discover and inspect those roots. Active claims may reflect unavailable or abandoned sessions; lease expiry is evidence, not permission to delete real work.

The evaluation projects are synthetic and read-only. They exercise routing decisions, not production orchestration, GitHub updates, or an implementation runner.

## Resulting artifacts

- `skills/reconcile-workflow/spec.md` — behavior contract.
- `skills/reconcile-workflow/SKILL.md` — executable routing guidance.
- `skills/reconcile-workflow/references/handoff.md` — compact evidence, MVP, and handoff shapes.
- `skills/reconcile-workflow/evals/` — synthetic fixtures for competing work, unpublished artifacts, scope expansion, claims, multi-agent ownership, and fresh-session handoff.
- `research/reconcile-workflow/integration.md` — publication and template-integration handoff.

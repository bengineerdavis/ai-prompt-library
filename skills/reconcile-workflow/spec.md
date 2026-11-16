# Reconcile Workflow

## Intent

Reconcile established repository and task evidence before choosing implementation work. The skill turns scattered branches, worktrees, task records, claims, and design artifacts into a preserved evidence map, a bounded implementation contract, and a fresh-session handoff for one eligible vertical slice.

The skill is a routing discipline, not another queue or orchestration service. It uses the configured Backlog tracker and native Git and hosting tools, while treating human judgment as the authority for semantic conflicts and implementation priority.

## Triggers

- **SHOULD** be used when asked to catch up, reconcile a repository or stack, identify current work, resolve competing task records, or choose the next implementation task.
- **SHOULD** be used when a main-checkout queue, worktree claim, dirty file, unpublished artifact, or expanding design discussion makes the next usable step uncertain.
- **SHOULD NOT** be used to implement an already claimed and well-scoped task, perform ordinary branch synchronization with no semantic ambiguity, or research an open-ended topic without selecting implementation work.
- **SHOULD NOT** replace the project's configured Backlog adapter, task workflow, or human approval boundaries.

## Behaviors

### Behavior: Establish evidence before routing

The agent SHALL enumerate repository roots and worktrees, inspect branch and working-tree state, and read task status, dependencies, claims, and validation issues from each discovered Backlog root before describing work as eligible, active, complete, or safe to clean. The agent SHALL distinguish observations from inferences and label unchecked ownership or publication state.

#### Scenario: Main says eligible

- **WHEN** the main checkout reports a task as eligible but the repository has additional worktrees
- **THEN** the agent inspects those worktrees and their task claims before calling the task available and reports any evidence it could not inspect

### Behavior: Preserve established work during reconciliation

The agent SHALL compare aggregate content and task semantics rather than relying only on branch ancestry. When records or branches conflict, the agent SHALL identify the canonical candidate, record semantic supersession or unresolved ownership, and preserve unique uncommitted or unpublished evidence. The agent SHALL NOT recommend deletion, reset, or queue cleanup while real work or its ownership remains unresolved.

#### Scenario: Competing established work

- **WHEN** two records describe overlapping work with different acceptance criteria and one branch is not an ancestor of the other
- **THEN** the agent compares their full requirements and diffs, preserves unique requirements and artifacts, and records the semantic decision or blocker instead of choosing by ancestry alone

### Behavior: Capture findings in the configured tracker

The agent SHALL use the project's configured Backlog adapter for task records, native dependencies, claims, run history, and decisions. The agent SHALL capture newly discovered usage blockers, preservation obligations, and deferred ideas as owned records or explicit updates, without creating a parallel `.scratch` queue or another orchestration framework.

#### Scenario: Unpublished specification

- **WHEN** reconciliation finds a complete specification that exists only as an untracked file
- **THEN** the agent preserves the file and records its publication or ownership requirement in Backlog before treating dependent implementation as ready

### Behavior: Reconcile claims across worktrees and agents

The agent SHALL treat claims and leases as evidence to inspect, not global proof of availability. The agent SHALL contrast expired and active claims, respect active multi-agent ownership, distinguish an expired empty claim from a claim with real uncommitted work, and limit cleanup eligibility to the verified empty case after its evidence is recorded.

#### Scenario: Expired empty claim and active real work

- **WHEN** a main checkout reports a task eligible, one worktree has an expired claim with no unique changes, and another agent has an active claim with uncommitted implementation
- **THEN** the agent preserves the active agent's work, does not reclaim or duplicate that implementation, and identifies only the verified empty stale claim as a cleanup candidate

### Behavior: Bound the usable milestone

The agent SHALL state the first usable outcome, one end-to-end workflow, minimum inputs, explicit non-goals, and feedback criteria. The agent SHALL classify newly proposed work as usage-blocking or deferred and SHALL NOT allow deferred ideas to expand the active implementation contract.

#### Scenario: Attractive scope expansion

- **WHEN** the first project-creation workflow is not implemented and reconciliation uncovers requests for hosted telemetry, a plugin marketplace, and automatic stack-wide updates
- **THEN** the agent keeps those requests visible as deferred records and selects only work required for the first usable project-creation workflow

### Behavior: Select one eligible vertical slice

The agent SHALL select the smallest end-to-end task that satisfies the bounded outcome and has no unresolved dependency, ownership, preservation, or claim blocker. The agent SHALL expose its task ID, native dependency state, evidence for eligibility, and remaining risks rather than presenting every open task as equally actionable.

#### Scenario: Dependency-controlled queue

- **WHEN** one task delivers the first usable workflow, its dependent tasks add optional integrations, and an unrelated design task is also eligible
- **THEN** the agent recommends the first usable workflow, names why the alternatives are blocked or later, and does not implement from multiple queues

### Behavior: Hand execution to a fresh implementation session

The agent SHALL end routing with a compact handoff naming the selected task, its authoritative requirements, preserved work, authorized scope, verification surface, and remaining ownership. The agent SHALL instruct the implementation session to claim through Backlog before editing and record progress and completion through the configured adapter. When the user names a handoff destination, the agent SHALL write the handoff there rather than only summarizing it in chat. The routing session SHALL NOT silently become the implementation session.

#### Scenario: Ready implementation task

- **WHEN** reconciliation leaves one eligible task with an approved contract and no preservation blocker
- **THEN** the agent produces a fresh-session handoff containing the task ID, requirement paths, current evidence, permitted changes, and required tests instead of starting implementation in the routing session

### Behavior: Prefer native mechanisms and verified surfaces

The agent SHALL inspect the installed Backlog, Git, worktree, and hosting command surfaces before relying on them. The agent SHALL use native queue and claim operations where they fit and use hosting branch synchronization only as transport, never as proof that semantic reconciliation succeeded.

#### Scenario: Synchronized but semantically wrong branch

- **WHEN** a hosting service successfully updates a pull-request branch but the combined diff drops an approved requirement
- **THEN** the agent reports the missing requirement as a reconciliation failure and does not treat the successful synchronization as completion

## Constraints

### Constraint: Do not destroy or appropriate work

The agent MUST NOT discard, overwrite, stash, reset, or appropriate another session's or agent's changes to make a queue or branch appear clean.

### Constraint: Do not mutate beyond the routing mandate

The agent MUST NOT commit, push, merge, publish, create or remove worktrees, or change implementation files unless the user has authorized that specific action. Recording reconciliation findings in Backlog does not authorize implementation.

### Constraint: Do not create competing coordination systems

The agent MUST NOT invent a second tracker, scheduler, claim store, or durable handoff narrative when the configured Backlog records and task links can carry the state.

### Constraint: Do not hide uncertainty or deferral

The agent MUST NOT silently choose an owner for a semantic conflict, describe stale status as active work, claim unchecked validation passed, or drop deferred ideas without an owned record.

<!-- skillet-version: 1.8.0 -->

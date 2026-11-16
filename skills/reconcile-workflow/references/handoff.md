# Routing and handoff records

Keep these records compact. Store durable findings in the configured Backlog task or decision record; do not create a parallel queue or an ever-growing session narrative.

## Evidence map

For each repository and worktree, record:

| Field               | Evidence                                                           |
| ------------------- | ------------------------------------------------------------------ |
| Location and branch | Repository root, worktree, branch, upstream                        |
| Working state       | Dirty paths, aggregate diff, unpublished artifacts                 |
| Task evidence       | Native task ID, status, dependencies, claims, validation issues    |
| Ownership           | Active agent or established owner; unknown when not established    |
| Preservation        | Unique requirements or work that must survive reconciliation       |
| Decision            | Canonical candidate, semantic supersession, or unresolved blocker  |
| Verification        | Checks actually run and their results; unchecked remains unchecked |

A branch that contains another branch is not automatically the canonical record. Compare the aggregate requirements and resulting diff.

## MVP contract

```text
First usable outcome:
One end-to-end workflow:
Minimum inputs:
Explicit non-goals:
Feedback criteria:
```

Classify each proposed addition as `usage-blocking` or `deferred`. Give deferred work a Backlog owner; do not silently discard it or add it to the active slice.

## Implementation handoff

```text
Selected Backlog task:
Why this is the smallest eligible vertical slice:
Native dependency and claim evidence:
Authoritative requirements:
Preserved work and remaining owners:
Authorized implementation scope:
Verification surface:
Checks already run (and checks not run):
```

The implementation session must claim through Backlog before editing. It must inspect current repository state again and record progress and completion through the configured Backlog adapter.

Do not present a handoff as evidence that implementation has started or succeeded.

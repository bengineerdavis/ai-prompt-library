# Auto mode policy

This document explains how `auto` should work for both cost and complexity.

For the definitions of the main controls, see [Modes and settings](./modes-and-settings.md).

## Default principle

Auto mode should be conservative.

That means:

- start with the cheapest strategy likely to work
- start with the simplest strategy likely to work
- escalate only when there is evidence that extra work is justified
- stop when more work is unlikely to improve the result enough to matter

## Auto cost

When `cost = auto`, the system should decide how much budget to spend based on:

- task importance
- task ambiguity
- expected reuse
- available service or hardware limits
- user preference history
- whether the environment is SaaS or local

Default behavior should be cost-conscious.

Examples:

- In a SaaS environment, auto should assume cost sensitivity unless the user explicitly signals otherwise.
- In a local environment, auto can be more flexible but should still respect hardware and runtime limits.

## Auto complexity

When `complexity = auto`, the system should prefer the simplest strategy that is likely to succeed.

Typical default progression:

- `simple`
- `layered`
- `exploratory`
- `deep search` (rare, and only when strongly justified)

The system should not jump to `deep search` just because it is available.

## Escalation triggers

Auto can increase cost and/or complexity when signals suggest the current result is not good enough.

Useful signals include:

- low quality score
- low confidence
- high evaluator disagreement
- repeated user dissatisfaction
- high task stakes or high reuse value
- strong benchmarkability

For how these signals are computed and combined, see:

- [Scoring model](./scoring-model.md)
- [Thresholds and recommendations](./thresholds-and-recommendations.md)

## Non-goals

Auto should not:

- surprise users with runaway cost
- default to `deep search`
- assume unlimited resources
- optimize beyond the point of meaningful returns

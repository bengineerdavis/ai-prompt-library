# Deep search

This document explains the heaviest `complexity` mode in Impromptu.

For the general control definitions, see [Modes and settings](./modes-and-settings.md).

## What deep search means

`complexity = deep search` allows the system to use a much broader and more expensive search process than normal.

This can include:

- more candidates
- more judges or evaluators
- tournament-style ranking
- survival-of-the-fittest refinement
- hybrid or mutation rounds
- stronger willingness to explore materially different prompt structures

Deep search is the far end of the “adventurous vs conservative” spectrum for **complexity**, not a separate axis.

## When to use it

Deep search is most appropriate when:

- the prompt is high value or high reuse
- the user explicitly wants exploration
- the task is difficult or ambiguous
- the user is experimenting with prompt factories, judges, or optimization workflows

It is especially useful when extra structural exploration is likely to change the design of a prompt, factory, or workflow, not just polish wording.

## When not to use it

Deep search is usually unnecessary for:

- simple prompt rewrites
- low-stakes one-off tasks
- weakly benchmarkable tasks
- users who primarily want speed

In these cases, `simple`, `layered`, or `exploratory` complexity is normally enough.

## Guardrails

Even deep search should not run without limits.

Use guardrails such as:

- stop when score improvements plateau
- stop when evaluators largely agree
- stop when budget or runtime limits are reached
- stop when additional search is unlikely to materially improve quality

These decisions rely on the same signals used elsewhere (quality, confidence, disagreement, improvement delta, and budget ratio). For how those are computed, see [Scoring model](./scoring-model.md).

## Practical guidance

Deep search should be rare by default.

It should usually require:

- `cost = high` or `unlimited`
- strong uncertainty or explicit user request
- a task where extra search is likely to matter

For the stopping and escalation logic, see [Thresholds and recommendations](./thresholds-and-recommendations.md).

# Deep search

`complexity = deep search` is the heaviest complexity mode.

For general control definitions, see [modes-and-settings.md](./modes-and-settings.md).
For stopping and escalation logic, see
[../internals/scoring-and-thresholds.md](../internals/scoring-and-thresholds.md).

## What deep search means

`complexity = deep search` allows a much broader and more expensive search process than
normal. This can include:

- more candidates
- more judges or evaluators
- tournament-style ranking
- survival-of-the-fittest refinement
- hybrid or mutation rounds
- stronger willingness to explore materially different prompt structures

Deep search is the far end of the “adventurous vs conservative” spectrum for
**complexity**, not a separate axis.

## When to use it

Deep search is most appropriate when:

- the prompt is high value or high reuse
- the user explicitly wants exploration
- the task is difficult or ambiguous
- the user is experimenting with prompt factories, judges, or optimization workflows

It is especially useful when extra structural exploration is likely to change the design
of a prompt, factory, or workflow — not just polish wording.

## When not to use it

Deep search is usually unnecessary for:

- simple prompt rewrites
- low-stakes one-off tasks
- weakly benchmarkable tasks
- users who primarily want speed

In these cases, `simple`, `layered`, or `exploratory` complexity is normally enough.

## Guardrails

Even deep search should not run without limits:

- stop when score improvements plateau
- stop when evaluators largely agree
- stop when budget or runtime limits are reached
- stop when additional search is unlikely to materially improve quality

These decisions rely on the same signals described in
[../internals/scoring-and-thresholds.md](../internals/scoring-and-thresholds.md).

## Practical guidance

Deep search should be rare by default.
It should usually require:

- `cost = high` or `unlimited`
- strong uncertainty or explicit user request
- a task where extra search is likely to matter

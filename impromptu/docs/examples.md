# Examples

This document provides simple examples of how cost, complexity, and verbosity can be combined.

For definitions of the controls, see [Modes and settings](./modes-and-settings.md).

## Quick rewrite

User goal:

> Shorten this prompt and make it clearer.

Recommended settings:

- `cost = low`
- `complexity = simple`
- `verbosity = quiet`

Why:

- low stakes
- low ambiguity
- little need for multiple branches

## Reusable prompt cleanup

User goal:

> Improve this prompt so I can reuse it for several related tasks.

Recommended settings:

- `cost = medium`
- `complexity = layered`
- `verbosity = info`

Why:

- some optimization is worthwhile
- deep exploration is probably unnecessary

## Important prompt design

User goal:

> Create a prompt I will reuse in my workflow every day.

Recommended settings:

- `cost = high`
- `complexity = exploratory`
- `verbosity = info`

Why:

- the prompt has long-term value
- broader search and stronger evaluation may pay off

## Deep experiment

User goal:

> I want to try many candidates, use more judges, and keep iterating on the best ones.

Recommended settings:

- `cost = unlimited`
- `complexity = deep search`
- `verbosity = debug`

Why:

- the user explicitly wants exploration
- they are likely willing to tolerate higher cost and runtime

## New user default

User goal:

> I just want it to work well without a bunch of setup.

Recommended settings:

- `cost = auto`
- `complexity = auto`
- `verbosity = info`

Why:

- it gives good default behavior while staying conservative

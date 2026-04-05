# Pipeline and stages

This document explains the internal prompt-building pipeline.

For the user-facing controls that influence this pipeline, see [Modes and settings](./modes-and-settings.md).

## Core pipeline

Impromptu uses a universal internal pipeline:

1. Build  
2. Specializer  
3. Optimizer  
4. Profile  

These stages are always conceptually present, but they do not always run with the same intensity.

## Stage states

Each stage can be:
- `active`
- `no-op`
- `deferred`

This means the pipeline stays structurally consistent while still allowing fast or lightweight runs.

## What each stage does

### Build

Creates the main prompt or initial candidate.

### Specializer

Adapts the prompt to the domain, user intent, or task shape when useful.

### Optimizer

Improves, compares, critiques, or evaluates prompt candidates.

This is also the natural place for judge-style evaluation when multiple candidates or stronger validation are needed.

### Profile

Applies reusable user preferences, standing constraints, and other persistent defaults.

## How modes affect the pipeline

- **cost** affects how much budget each stage is allowed to consume.
- **complexity** affects how many branches, strategies, and evaluation paths are permitted.
- **verbosity** affects how much of this is shown to the user.

For example:
- `cost = low` and `complexity = simple` may produce one candidate with light optimization.
- `cost = high` and `complexity = exploratory` may allow multiple candidates, judges, and refinement rounds.

## Why the pipeline should remain universal

Keeping a universal pipeline helps maintain consistency, debugging clarity, and predictable behavior.

The system should adapt by changing stage intensity, not by inventing a completely different architecture for each task.
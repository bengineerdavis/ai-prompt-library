# Modes and Settings

This document explains the three main control classes for Impromptu in plain language.

## Overview

Impromptu uses three top-level settings to shape how much work it does, how sophisticated the strategy is, and how much of that process you see.

- `cost = auto | low | medium | high | unlimited`
- `complexity = auto | simple | layered | exploratory | deep search`
- `verbosity = quiet | info | debug`

These settings are designed to work together.

- **Cost** controls how much time, compute, and token budget Impromptu is allowed to spend while building or refining a prompt.
- **Complexity** controls how sophisticated the strategy is allowed to be, including how many stages, alternatives, judges, and refinement rounds are permitted.
- **Verbosity** controls how much of that internal process is shown to the user.

In most cases, users should start with:

- `cost = auto`
- `complexity = auto`
- `verbosity = info`

That default is meant to be conservative and cost-conscious, especially for SaaS users, while still flexible enough to take advantage of higher limits when the environment supports it.

## Cost

`cost` answers the question:

> How much budget is Impromptu allowed to spend on this task?

That budget can include:

- token usage
- compute usage
- latency / time spent
- number of retries or optimization rounds
- how much model orchestration is allowed

### Cost levels

#### `auto`
Use a conservative default based on the environment and the task.

This should:
- prefer efficient execution,
- avoid surprising costs,
- respect SaaS constraints,
- and scale up only when the expected gain is worth it.

This should be the default for most people.

#### `low`
Use a small budget.

Good for:
- quick drafts,
- lightweight transformations,
- experimentation,
- low-stakes work.

Tradeoff:
- cheaper and faster,
- but may miss better alternatives or deeper refinements.

#### `medium`
Use a moderate budget.

Good for:
- most normal prompt work,
- reusable prompts,
- tasks where quality matters but cost still matters too.

#### `high`
Use a large budget with clear caps.

Good for:
- important prompts,
- factory or seed design,
- prompts intended for repeated reuse,
- tasks where additional optimization is likely worthwhile.

#### `unlimited`
Do not optimize around cost as a primary constraint.

Good for:
- local models,
- flat-rate plans where the user does not care about per-run cost,
- deep experimentation.

Warning:
- this can still be bounded by hardware, latency, or practical stop conditions.
- `unlimited` should not mean infinite loops.

## Complexity

`complexity` answers the question:

> How sophisticated is the strategy allowed to be?

This controls things like:
- whether the system uses a simple or multi-stage process,
- how many candidates are allowed,
- whether multiple judges or evaluators are used,
- whether tournament or survival-style rounds are allowed,
- whether deep search is permitted.

### Complexity levels

#### `auto`
Let the system choose the simplest strategy that is likely to work well.

The default behavior should be conservative.

That means:
- start simple,
- only escalate when uncertainty is high,
- only increase complexity when the expected gain is meaningful.

#### `simple`
Use the most direct path.

Typical behavior:
- 1 candidate,
- minimal branching,
- limited optimization,
- no deep comparisons.

#### `layered`
Use a small number of structured stages.

Typical behavior:
- a normal build pipeline,
- limited refinement,
- occasional second candidate,
- modest comparison.

This is a strong general-purpose setting.

#### `exploratory`
Allow broader search.

Typical behavior:
- multiple candidates,
- stronger comparison,
- more willingness to try materially different strategies,
- more refinement rounds when justified.

#### `deep search`
Allow the heaviest search process.

Typical behavior:
- many candidates,
- multiple evaluators or judges,
- tournament or survival-style selection,
- hybrid or iterative refinement rounds,
- a strong bias toward exploring the space before stopping.

This mode is best for:
- research,
- prompt factories,
- difficult prompt optimization,
- users who explicitly want heavy experimentation.

This mode should still use stop conditions and guardrails.

## Verbosity

`verbosity` answers the question:

> How much of the internal process should be visible?

### Verbosity levels

#### `quiet`
Show the result with minimal process detail.

#### `info`
Show short summaries of important decisions and settings.

This is the recommended default for most users.

#### `debug`
Show detailed stage-by-stage information, including reasoning summaries, settings, and why the system escalated or stopped.

## How cost and complexity work together

These two settings work together to determine the tradeoff between speed, cost, and quality.

### Example 1: low cost + simple complexity
- Fast and cheap.
- Good for drafts and low-stakes work.
- More likely to miss edge cases or stronger alternatives.

### Example 2: medium cost + layered complexity
- Good default for everyday use.
- Balanced quality and speed.
- Usually enough for most reusable prompts.

### Example 3: high cost + exploratory complexity
- Broader search and stronger optimization.
- Good for important prompts or factory design.
- Slower and more expensive.

### Example 4: unlimited cost + deep search
- Strongest exploration and optimization.
- Best for local models, flat-rate plans, or research workflows.
- Can be slow, compute-heavy, and unnecessary for simple tasks.

## Why auto should be the default

Most users should not have to manually tune these settings every time.

`auto` should:
- infer the likely best settings from the task,
- stay conservative by default,
- be cost-conscious for SaaS environments,
- and only escalate when the expected gains justify the additional expense or latency.

The guiding principle is:

> It is better to under-spend by default and let users ask for more, than to surprise users with runaway cost or excessive compute.

## Safe default behavior

A good default starting point is:

- `cost = auto`
- `complexity = auto`
- `verbosity = info`

And the auto policy should generally:
- start from a cheap and simple strategy,
- measure whether quality is already good enough,
- escalate only when the task appears important, uncertain, or reusable,
- stop when additional work is unlikely to pay off.

## Short examples

### Quick rewrite
User goal:
> Rewrite this prompt to be shorter.

Recommended settings:
- `cost = low`
- `complexity = simple`
- `verbosity = quiet`

### Reusable note-taking prompt
User goal:
> Improve this prompt so I can reuse it for research and non-technical topics.

Recommended settings:
- `cost = medium`
- `complexity = layered`
- `verbosity = info`

### Prompt factory design
User goal:
> Create a prompt-generation framework with evaluation and preference tracking.

Recommended settings:
- `cost = high`
- `complexity = exploratory`
- `verbosity = info` or `debug`

### Deep experiment
User goal:
> Generate many prompt candidates, compare them with multiple judges, and keep refining the best parts.

Recommended settings:
- `cost = unlimited`
- `complexity = deep search`
- `verbosity = debug`

## Final guidance

Use these settings as broad control knobs, not as rigid rules.

- Use **cost** to control budget.
- Use **complexity** to control strategy sophistication.
- Use **verbosity** to control transparency.

When in doubt, start with auto modes and let the system stay conservative.

# Modes and settings

Impromptu and Seed share three main control classes.
These are the only knobs most users need to think about.

- **cost** – how much work the system is allowed to do
- **complexity** – how conservative vs exploratory the strategy is
- **verbosity** – how much process detail you see

Most of the internal machinery (scoring, thresholds, risk profiles, strategies) exists
to make these three controls behave well.

## cost

`cost` controls how much work the system is allowed to do: how many calls, candidates,
judges, and iterations.

Allowed values:

- `auto` – let the system pick based on task type and learned preferences
- `low` – minimal work, cheap and fast
- `medium` – balanced cost vs quality
- `high` – more work allowed, especially for important or reusable prompts
- `unlimited` – experimentation mode; the system may do a lot of work

Interpretation:

- Moving cost **up** lets the system try more options, run more evaluations, and iterate
  more before stopping.
- Moving cost **down** encourages the system to stop earlier, even if further
  improvements might be possible.

## complexity

`complexity` controls how conservative vs exploratory the strategy is.

Allowed values:

- `auto` – let the system choose a strategy based on the task and past behavior
- `simple` – straightforward, conservative strategies; low exploration
- `layered` – a few sequential steps (e.g., draft → refine → brief evaluation)
- `exploratory` – more branching and experimentation with different strategies
- `deep search` – broad search over many candidates and strategies, with heavy
  evaluation

Interpretation:

- Lower complexity (simple, layered) favors predictable, low-variance behavior.
  Good for minor refinements or production runs.
- Higher complexity (exploratory, deep search) favors broad exploration.
  Good for designing new prompts, factories, or workflows where novel structure matters.

In practice, **complexity** is the intuitive “conservative vs adventurous” knob.
It does not have to correlate with task stakes; users can choose high exploration even
for low-stakes tasks if they want to play with ideas.

## verbosity

`verbosity` controls how much process you see.

Allowed values:

- `quiet` – minimal process commentary, mostly final answers
- `info` – answers plus lightweight reasoning and explanations
- `debug` – detailed traces of what strategies were tried and why

Interpretation:

- `quiet` is ideal when you just want results.
- `info` is the default: enough transparency to understand what happened.
- `debug` is useful when you are tuning prompts, factories, or the system itself.

## How these controls interact

Internally, Impromptu uses a scoring and threshold system to decide when to stop, when
to do more work, and when to recommend changes.

As a user, you do not need to think in scores.
Instead:

- `cost` says how much work is acceptable.
- `complexity` says how adventurous vs conservative the strategy may be.
- `verbosity` says how much of that process you want to see.

The rest of the system adapts to these settings.

For how scores and thresholds work, see:

- [Scoring model](./scoring-model.md)
- [Thresholds and recommendations](./thresholds-and-recommendations.md)

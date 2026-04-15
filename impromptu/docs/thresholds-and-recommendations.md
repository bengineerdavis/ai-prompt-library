# Thresholds and recommendations

This document explains how Impromptu decides whether to stop, continue, or escalate.

It uses the signals and rubric described in [Scoring model](./scoring-model.md), but you
do not need to think in scores to use the system.

## Purpose

Thresholds turn internal scores into decisions:

- **accept / stop** – current result is good enough
- **continue** – more work may improve the result
- **escalate** – switch to a more intensive strategy or suggest higher cost/complexity

## Signals used

Impromptu looks at several signals:

- **quality score** – overall 1–5 score from the rubric
- **confidence** – how sure the judges are that the result is good enough
- **disagreement** – how much judges disagree with each other
- **improvement delta** – how much quality improved after recent extra work
- **budget ratio** – how much of the allowed work or budget has been consumed

For how these are computed, see [Scoring model](./scoring-model.md).

## Default decision profiles

Thresholds are grouped into simple profiles instead of exposing many separate knobs.

Internally, Impromptu maintains three default profiles:

- **Speed** – accept earlier, favor cost and time
- **Balanced** – default behavior
- **Thorough** – higher bar before stopping

These profiles are influenced by `cost` and `complexity`:

- lower cost + simple complexity → closer to **Speed**
- auto/medium cost + layered complexity → **Balanced**
- high/unlimited cost + exploratory/deep search → **Thorough**

The exact numbers can evolve, but a reasonable starting point is:

- **Speed profile** (low-stakes / exploratory)

  - overall quality ≥ 3.5
  - confidence ≥ 0.6
  - disagreement can be moderate

- **Balanced profile** (default)

  - overall quality ≥ 4.0
  - confidence ≥ 0.7
  - disagreement is low

- **Thorough profile** (high-effort / high-reuse)

  - overall quality ≥ 4.5
  - confidence ≥ 0.8
  - disagreement is very low

These are conceptual targets rather than hard-coded constants; implementation may map
them to model-specific scales.

## How cost and complexity influence thresholds

User settings do not set thresholds directly.
Instead, they select how strict the system should be and how much work it may do to
reach that standard.

- Increasing **cost** allows the system to:

  - try more candidates
  - run more judges
  - iterate more rounds before considering the task complete

- Increasing **complexity** allows the system to:

  - explore more diverse strategies
  - branch into different prompt structures
  - keep multiple strong alternatives before choosing

In response, Impromptu:

- uses stricter thresholds (closer to the **Thorough** profile) when cost and complexity
  are high
- uses looser thresholds (closer to the **Speed** profile) when cost and complexity are
  low

This keeps behavior intuitive: if you ask for more effort and exploration, the system
expects higher quality before stopping.

## When thresholds adjust

Thresholds should adapt based on:

- **Task type and stakes**

  - One-off, low-stakes tasks (for example quick rewrites) can stop earlier.
  - Reusable prompts, factories, or long-lived research should aim higher.

- **How benchmarkable the task is**

  - Clear, checkable tasks (for example format adherence, explicit constraints) can
    justify stricter rules.
  - Ambiguous or taste-driven tasks may tolerate more disagreement.

- **User preferences and history**

  - If a user often increases cost/complexity and reviews multiple options, the system
    can lean toward stricter thresholds.
  - If a user usually accepts early results, the system can learn to stop sooner.

These adjustments are incremental.
Thresholds should move slowly and be explainable in plain language.

## Escalation and recommendations

Given current signals, Impromptu can:

- **Accept / stop** when:

  - quality is above the relevant profile threshold
  - confidence is high enough
  - disagreement is low or expected for the task
  - recent improvement deltas are small

- **Continue at the same level** when:

  - quality is close but not yet above threshold
  - confidence is moderate
  - improvement deltas are still meaningful

- **Escalate** when:

  - quality is below threshold
  - confidence is low
  - disagreement is high
  - budget remains

Typical escalations include:

- suggesting a higher `cost` level
- suggesting a higher `complexity` level
- switching to more robust strategies (for example more judges, different evaluation
  rubrics)

Recommendations should be phrased simply, for example:

- “This looks borderline.
  If this prompt is important, consider raising cost to `high` and complexity to
  `exploratory` for one more round.”

## Guardrails

- Thresholds and scores are **guidance**, not precise instruments.
- Small numerical differences (for example 4.2 vs 4.3) should rarely change behavior on
  their own.
- Users should always be able to override recommendations.

The goal is to support better decisions about when to stop, when to do more work, and
when to invest in deeper optimization — not to chase perfect scores.

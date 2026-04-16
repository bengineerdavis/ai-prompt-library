# Scoring and thresholds

This document covers the scoring rubric, signal definitions, decision profiles, and
escalation logic.

For the user-facing controls that drive these internals, see
[../controls/modes-and-settings.md](../controls/modes-and-settings.md).

______________________________________________________________________

## Purpose

The scoring model helps Impromptu decide whether the current result is good enough or
whether more work is justified.
Thresholds turn those scores into three decisions:

- **accept / stop** – current result is good enough
- **continue** – more work may improve the result
- **escalate** – switch to a more intensive strategy or suggest higher cost/complexity

______________________________________________________________________

## Core signals

| Signal                | What it measures                                         |
| --------------------- | -------------------------------------------------------- |
| **quality score**     | How good the current best result appears to be (1–5)     |
| **confidence**        | How sure the system is the result is good enough (0–1)   |
| **disagreement**      | How much evaluators disagree with each other             |
| **improvement delta** | How much quality improved after recent extra work        |
| **budget ratio**      | How much of the allowed work or budget has been consumed |

______________________________________________________________________

## Rubric and grading scale

Impromptu uses a simple analytic rubric: each quality dimension is scored separately,
then combined into one overall quality score.

Default rubric dimensions (matching the Seed profile):

- **Clarity** – Is the answer easy to follow, unambiguous, and well-structured?
- **Conciseness** – Does it avoid unnecessary repetition while remaining complete?
- **Completeness** – Does it cover all important parts of the request?
- **Goal alignment** – Does it actually solve the user’s stated goal?
- **Context awareness** – Does it respect the provided context, constraints, and prior
  information?
- **Expected output** – Does it match the requested format, style, and level of detail?

Each dimension is graded on a **1–5 scale**:

| Score | Label        | Meaning                                                          |
| ----- | ------------ | ---------------------------------------------------------------- |
| 5     | Excellent    | Fully meets the criterion with no meaningful issues              |
| 4     | Good         | Meets the criterion with only minor, non-blocking issues         |
| 3     | Adequate     | Partially meets; noticeable gaps but still usable                |
| 2     | Weak         | Significant problems; user would likely need to revise or re-run |
| 1     | Poor         | Fails the criterion; unusable for this dimension                 |
| 0     | Hard failure | Reserved for off-topic, refusals, or hallucinated content        |

### From rubric to quality score

The overall quality score is the weighted mean of per-dimension scores on the same 1–5
scale (default: equal weights).
Different tasks or factories can override weights.
Examples:

- **Prompt-style work**: Clarity and Expected output weighted higher
- **Factual research**: Completeness and Context awareness weighted higher

### Judge prompt guidance

Judge prompts should:

- score one dimension at a time
- require a numeric score plus a short justification per dimension
- return structured output (for example JSON) so scores can be aggregated reliably

______________________________________________________________________

## Decision profiles

Thresholds are grouped into three profiles rather than exposing many separate knobs.

| Profile      | When active                              | Quality | Confidence | Disagreement |
| ------------ | ---------------------------------------- | ------- | ---------- | ------------ |
| **Speed**    | low cost + simple complexity             | ≥ 3.5   | ≥ 0.6      | moderate OK  |
| **Balanced** | auto/medium + layered                    | ≥ 4.0   | ≥ 0.7      | low          |
| **Thorough** | high/unlimited + exploratory/deep search | ≥ 4.5   | ≥ 0.8      | very low     |

These are conceptual targets, not hard-coded constants.

### How cost and complexity influence profiles

- Increasing **cost** allows more candidates, more judges, and more iteration rounds.
- Increasing **complexity** allows more diverse strategies, branching, and multiple
  strong alternatives before choosing.

The system uses stricter thresholds (closer to **Thorough**) when cost and complexity
are high, and looser thresholds (closer to **Speed**) when they are low.

______________________________________________________________________

## Threshold adaptation

Thresholds adjust based on:

- **Task type and stakes** – One-off rewrites can stop earlier; reusable factories
  should aim higher.
- **Benchmarkability** – Clear, checkable tasks can justify stricter rules; taste-driven
  tasks may tolerate more disagreement.
- **User history** – If a user often accepts early results, the system can learn to stop
  sooner.

Adjustments are incremental and should be explainable in plain language.

______________________________________________________________________

## Escalation and stop logic

**Accept / stop** when:

- quality is above the relevant profile threshold
- confidence is high enough
- disagreement is low or expected for the task
- recent improvement deltas are small

**Continue at the same level** when:

- quality is close but not yet above threshold
- confidence is moderate
- improvement deltas are still meaningful

**Escalate** when:

- quality is below threshold
- confidence is low
- disagreement is high
- budget remains

Typical escalations: suggest higher `cost`, suggest higher `complexity`, or switch to
more robust evaluation strategies.

Recommendations should be phrased simply, for example:

> “This looks borderline.
> If this prompt is important, consider raising cost to `high` and complexity to
> `exploratory` for one more round.”

______________________________________________________________________

## Guardrails

- Thresholds and scores are **guidance**, not precise instruments.
- Small numerical differences (for example 4.2 vs 4.3) should rarely change behavior on
  their own.
- Users should always be able to override recommendations.

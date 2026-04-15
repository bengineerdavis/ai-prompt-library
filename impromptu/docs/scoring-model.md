# Scoring model

This document explains the scoring model in plain language.

For the related escalation logic, see
[Thresholds and recommendations](./thresholds-and-recommendations.md).

## Goal

The scoring model helps Impromptu decide whether the current result is already good
enough or whether more work is justified.

## Core signals

Useful signals include:

- **quality score**: how good the current best result appears to be
- **confidence score**: how sure the system is that the result is good enough
- **disagreement score**: how much evaluators disagree
- **improvement delta**: how much extra work improved the result
- **budget ratio**: how much of the allowed work or budget has already been consumed

## Rubric and grading scale

Impromptu relies on a simple analytic rubric: each quality dimension is scored
separately, then combined into one quality score.

Default rubric dimensions (matching the Seed profile) are:

- **Clarity** – Is the answer easy to follow, unambiguous, and well-structured?
- **Conciseness** – Does the answer avoid unnecessary repetition and filler while still
  being complete?
- **Completeness** – Does the answer cover all important parts of the request?
- **Goal alignment** – Does the answer actually solve the user’s stated goal?
- **Context awareness** – Does the answer respect the provided context, constraints, and
  prior information?
- **Expected output** – Does the answer match the requested format, style, and level of
  detail?

Each dimension is graded on a **1–5 scale**:

- **5 – Excellent**: Fully meets the criterion with no meaningful issues.
- **4 – Good**: Meets the criterion with only minor, non-blocking issues.
- **3 – Adequate**: Partially meets the criterion; noticeable gaps but still usable.
- **2 – Weak**: Significant problems; user would likely need to revise or re-run.
- **1 – Poor**: Fails the criterion; answer is unusable for this dimension.

In normal grading, scores range from **1–5**. A score of **0** can be reserved for hard
failures, such as off-topic answers, refusals when a safe answer is possible, or
hallucinated content that clearly contradicts provided context.

Judge prompts should:

- ask the model to **score one dimension at a time**
- require a **numeric score plus a short justification** for each dimension
- return **structured output** (for example JSON) so scores can be aggregated reliably

## From rubric to quality score

Given per-dimension scores, Impromptu computes an overall **quality score** as a
weighted average:

- Each rubric dimension has a weight (default: equal weights).
- The overall quality score is the weighted mean on the same 1–5 scale.
- This can be rescaled to 0–1 or 0–100 internally if needed.

Different tasks or factories can override weights.
For example:

- For **prompt-style work**, Clarity and Expected output might be weighted higher.
- For **factual research**, Completeness and Context awareness might be weighted higher.

The **confidence score** can come from:

- the model’s own self-reported confidence (mapped onto 0–1)
- how consistent the justifications are
- how stable scores are across multiple judges or runs

The **disagreement score** measures how far apart multiple judges are:

- low disagreement → judges broadly agree on quality
- high disagreement → judges give very different scores, which may justify more search
  or a human review

## Plain-language idea of a threshold

A threshold is just a decision line.

Example:

- if the result is above the “good enough” line, stop
- if it is below the line, more work may be justified

For example, a default threshold might require:

- overall quality ≥ 4.0
- confidence ≥ 0.7
- disagreement below a moderate level

Thresholds turn these scores into “stop vs continue vs escalate” decisions.
The exact thresholds depend on task type, stakes, and user preferences; see
[Thresholds and recommendations](./thresholds-and-recommendations.md) for details.

## Important guardrail

The scoring model should guide decisions, not create false precision.

These scores are meant to support better choices about stopping, escalation, and
recommendations. Small differences, such as 4.2 vs 4.3, should rarely matter on their
own.

# Scoring Model

This document explains the scoring model in plain language.

For the related escalation logic, see [Thresholds and recommendations](./thresholds-and-recommendations.md).

## Goal

The scoring model helps Impromptu decide whether the current result is already good enough or whether more work is justified.

## Core signals

Useful signals include:
- **quality score**: how good the current best result appears to be,
- **confidence score**: how sure the system is that the result is good enough,
- **disagreement score**: how much evaluators disagree,
- **improvement delta**: how much extra work improved the result,
- **budget ratio**: how much of the allowed budget has already been consumed.

## Rubric and grading scale

Impromptu relies on a simple analytic rubric: each quality dimension is scored separately, then combined into one quality score.[web:255][web:256][web:261]

Default rubric dimensions (matching the Seed profile) are:
- **Clarity** – Is the answer easy to follow, unambiguous, and well-structured?
- **Conciseness** – Does the answer avoid unnecessary repetition and filler while still being complete?
- **Completeness** – Does the answer cover all important parts of the request?
- **Goal alignment** – Does the answer actually solve the user’s stated goal?
- **Context awareness** – Does the answer respect the provided context, constraints, and prior information?
- **Expected output** – Does the answer match the requested format, style, and level of detail?

Each dimension is graded on a **1–5 scale**:

- **5 – Excellent**: Fully meets the criterion with no meaningful issues.
- **4 – Good**: Meets the criterion with only minor, non-blocking issues.
- **3 – Adequate**: Partially meets the criterion; noticeable gaps but still usable.
- **2 – Weak**: Significant problems; user would likely need to revise or re-run.
- **1 – Poor**: Fails the criterion; answer is unusable for this dimension.

A score of **0** can be reserved for hard failures (e.g., off-topic, refusal when a safe answer is possible, or hallucinated content that clearly contradicts provided context).

Judge prompts should:
- ask the model to **score one dimension at a time**,  
- require a **numeric score plus a short justification** for each dimension,  
- and return **structured output** (e.g., JSON) so scores can be aggregated reliably.[web:255][web:256][web:262]

## From rubric to quality score

Given per-dimension scores, Impromptu computes an overall **quality score** as a weighted average:

- Each rubric dimension has a weight (default: equal weights).
- The overall quality score is the weighted mean on the same 1–5 scale.
- This can be rescaled to 0–1 or 0–100 internally if needed.

Different tasks or factories can override weights. For example:
- For **prompt-style work**, Clarity and Expected output might be weighted higher.
- For **factual research**, Completeness and Context awareness might be weighted higher.

The **confidence score** can come from:
- the model’s own self-reported confidence (mapped onto 0–1),
- how consistent the justifications are,
- and how stable scores are across multiple judges or runs.[web:256][web:259][web:262]

The **disagreement score** measures how far apart multiple judges are:
- low disagreement → judges broadly agree on quality,
- high disagreement → judges give very different scores, which may justify more search or a human review.

## Plain-language idea of a threshold

A threshold is just a decision line.

Example:
- if the result is above the “good enough” line, stop,
- if it is below the line, more work may be justified.

For example, a default threshold might be:
- overall quality ≥ 4.0,
- confidence ≥ 0.7,
- and disagreement below a moderate level.

## Why thresholds should adapt

Not every task should use the same standards.

Examples:
- a low-stakes quick rewrite may be good enough earlier,
- a reusable prompt for important work should meet a higher standard,
- a user who values speed may prefer earlier stopping,
- a user who values thoroughness may prefer deeper optimization.[web:255][web:119]

Thresholds can also be adapted based on:
- whether the task is easy to benchmark,
- how risky failure would be,
- and what the user’s learned preferences are.

## Base plus adjustments

A good design is:
- start with a default threshold,
- adjust it based on task risk,
- adjust it based on how benchmarkable the task is,
- and adjust it based on the user's learned preferences.

In practice, this might mean:
- **raising** the required quality/confidence for high-risk or high-reuse tasks,
- **lowering** them for experimental or low-stakes tasks,
- and letting users choose profiles (e.g., “speed” vs “thoroughness”) that nudge thresholds up or down.

## Important guardrail

The scoring model should guide decisions, not act like false precision.

These scores are meant to support better choices about escalation, stopping, and recommendation behavior, not to pretend that small differences (e.g., 4.2 vs. 4.3) are meaningful on their own.[web:255][web:261]
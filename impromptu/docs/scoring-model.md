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

## Plain-language idea of a threshold

A threshold is just a decision line.

Example:
- if the result is above the “good enough” line, stop,
- if it is below the line, more work may be justified.

## Why thresholds should adapt

Not every task should use the same standards.

Examples:
- a low-stakes quick rewrite may be good enough earlier,
- a reusable prompt for important work should meet a higher standard,
- a user who values speed may prefer earlier stopping,
- a user who values thoroughness may prefer deeper optimization.

## Base plus adjustments

A good design is:
- start with a default threshold,
- adjust it based on task risk,
- adjust it based on how benchmarkable the task is,
- and adjust it based on the user's learned preferences.

## Important guardrail

The scoring model should guide decisions, not act like false precision.

These scores are meant to support better choices about escalation, stopping, and recommendation behavior.

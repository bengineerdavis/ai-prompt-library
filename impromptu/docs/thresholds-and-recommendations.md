# Thresholds and Recommendations

This document explains how Impromptu decides when to escalate effort, when to stop, and when to suggest updated defaults.

For the meaning of the user-facing settings, see [Modes and settings](./modes-and-settings.md).

## Core idea

The system should:
- encourage more work when uncertainty is high and expected gains are meaningful,
- push back when quality is already strong and more work is likely waste,
- and contain complexity when the task is low-stakes, under-specified, or weakly benchmarkable.

## Signals

Useful signals include:
- quality score,
- confidence score,
- disagreement score,
- improvement delta,
- budget ratio,
- task risk,
- benchmarkability,
- and learned user preference bias.

## Plain-language threshold example

A threshold is just a line that says:

> If the current result is already good enough, stop.
> If it is not good enough, do more work.

Example:
- Start from a default “good enough” target.
- Raise that target for high-stakes reusable tasks.
- Lower that target for quick, low-stakes tasks.
- Adjust it again based on what the user tends to prefer.

## Recommendation messages

The system may suggest new defaults when behavior patterns become stable.

Examples:
- Recommend lower cost when deeper runs rarely help.
- Recommend higher complexity when the user repeatedly asks for more exploration.
- Recommend more or less verbosity based on how often the user asks for process details.

## Important principle

Thresholds should begin with sane defaults, but they should evolve using user behavior and preference history rather than staying fixed forever.

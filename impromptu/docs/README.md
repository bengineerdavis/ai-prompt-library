# Impromptu docs

This directory contains the working documentation for Impromptu’s prompt-building system.

The core idea is simple: users control three main knobs — **cost**, **complexity**, and **verbosity** — and the system handles scoring, thresholds, and pipeline behavior behind the scenes.

## Reading order

Start here if you are new:

1. [Modes and settings](./modes-and-settings.md)
2. [Auto mode policy](./auto-mode-policy.md)
3. [Pipeline and stages](./pipeline-and-stages.md)
4. [Scoring model](./scoring-model.md)
5. [Thresholds and recommendations](./thresholds-and-recommendations.md)
6. [User preferences and memory](./user-preferences-and-memory.md)
7. [Service-specific guidance](./service-specific-guidance.md)

## What each doc covers

- **Modes and settings** explains the main knobs a user can control: cost (how much work), complexity (how conservative vs exploratory), and verbosity (how much process you see).
- **Auto mode policy** explains how `auto` should behave conservatively for cost and complexity, and when it should escalate.
- **Pipeline and stages** explains the internal build → specializer → optimizer → profile flow, and how the three knobs affect stage intensity.
- **Scoring model** explains the signals, rubric, and aggregation used to measure quality, confidence, disagreement, improvement delta, and budget ratio.
- **Thresholds and recommendations** explains how Impromptu uses those scores to decide when to stop, continue, or escalate, and how profiles like Speed, Balanced, and Thorough behave.
- **User preferences and memory** explains how reusable preferences are stored, refreshed over time, and applied via the profile stage.
- **Service-specific guidance** explains how to think about saved context in SaaS tools versus the Impromptu API/tooling.

Additional supporting docs:

- **Onboarding** describes the first-run experience and recommended defaults.
- **Examples** shows concrete combinations of cost, complexity, and verbosity for common scenarios.
- **Deep search** describes the heaviest `complexity` mode and when it is appropriate to use.

## Linking guidance

The docs that should directly link to or refer to **Modes and settings** are:

- `README.md` (this entry point)
- `auto-mode-policy.md`
- `pipeline-and-stages.md`
- `scoring-model.md`
- `thresholds-and-recommendations.md`
- `user-preferences-and-memory.md`
- `service-specific-guidance.md`

Reason: `modes-and-settings.md` defines the shared vocabulary for cost, complexity, and verbosity, which the rest of the system builds on.
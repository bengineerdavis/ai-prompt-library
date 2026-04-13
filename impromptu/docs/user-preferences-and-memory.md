# User preferences and memory

This document explains how Impromptu should store and refresh reusable user preferences.

For the shared user-facing controls, see [Modes and settings](./modes-and-settings.md).

## Goal

The goal is to reduce repeated user effort.

Instead of asking the same questions over and over, the system should learn:

- preferred cost level
- preferred complexity level
- preferred verbosity
- standing constraints
- reusable style preferences
- whether the user usually wants more or fewer alternatives

## Default behavior

The system should first try to infer likely preferences.

It should only ask questions when:

- confidence is low
- a preference is new
- a preference appears stale
- the user has recently behaved in a way that contradicts the saved default

When confidence is high, the system should quietly apply preferences and explain them only when useful (“Using your usual `cost = medium` and `complexity = layered` for this task.”).

## Preference refresh

A frecency-style approach is a good fit.

That means saved preferences are influenced by:

- how often they are used
- how recently they were used
- whether the user overrides them

Overrides should count more than passive acceptance. If a user frequently adjusts cost or complexity away from the saved default, the system should propose updating the default rather than nagging.

## What should be persisted

Good candidates for persistence include:

- default cost
- default complexity
- default verbosity
- whether to save recurring overrides
- service- or environment-specific context management preferences
- stable style or formatting preferences that apply across tasks

These persisted preferences should influence:

- which defaults are chosen on new sessions
- how `auto` behaves for cost and complexity
- which internal profiles (for example Speed, Balanced, Thorough) are most appropriate by default

## What should remain flexible

The system should still allow session-level overrides.

Saved defaults should guide behavior, not trap the user. Users should always be able to:

- temporarily override cost, complexity, or verbosity for a single task
- try a different profile or mode without committing to it
- decline suggested preference updates

When behavior and saved defaults diverge for long enough, the system can propose an update in plain language instead of silently changing it.

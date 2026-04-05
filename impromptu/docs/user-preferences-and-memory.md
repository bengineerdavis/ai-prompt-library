# User Preferences and Memory

This document explains how Impromptu should store and refresh reusable user preferences.

For the shared user-facing controls, see [Modes and settings](./modes-and-settings.md).

## Goal

The goal is to reduce repeated user effort.

Instead of asking the same questions over and over, the system should learn:
- preferred cost level,
- preferred complexity level,
- preferred verbosity,
- standing constraints,
- reusable style preferences,
- and whether the user usually wants more or fewer alternatives.

## Default behavior

The system should first try to infer likely preferences.

It should only ask questions when:
- confidence is low,
- a preference is new,
- a preference appears stale,
- or the user has recently behaved in a way that contradicts the saved default.

## Preference refresh

A frecency-style approach is a good fit.

That means saved preferences are influenced by:
- how often they are used,
- how recently they were used,
- and whether the user overrides them.

## What should be persisted

Good candidates for persistence include:
- default cost,
- default complexity,
- default verbosity,
- whether to save recurring overrides,
- and service-specific context management preferences.

## What should remain flexible

The system should still allow session-level overrides.

Saved defaults should guide behavior, not trap the user.

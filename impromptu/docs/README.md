# Impromptu Docs

This directory contains the working documentation for Impromptu's prompt-building system.

## Reading order

Start here if you are new:

1. [Modes and settings](./modes-and-settings.md)
2. [Auto mode policy](./auto-mode-policy.md)
3. [Pipeline and stages](./pipeline-and-stages.md)
4. [Thresholds and recommendations](./thresholds-and-recommendations.md)
5. [User preferences and memory](./user-preferences-and-memory.md)
6. [Service-specific guidance](./service-specific-guidance.md)

## What each doc covers

- **Modes and settings** explains the main knobs a user can control: cost, complexity, and verbosity.
- **Auto mode policy** explains how `auto` should behave conservatively and when it should escalate.
- **Pipeline and stages** explains the internal build → specializer → optimizer → profile flow.
- **Thresholds and recommendations** explains how Impromptu decides when to do more work, stop, or suggest new defaults.
- **User preferences and memory** explains how reusable preferences are stored and refreshed over time.
- **Service-specific guidance** explains how to think about saved context in SaaS tools versus the future Impromptu API/tooling.
- **Impromptu prompt library model** defines the canonical v1 contract for collections, namespace directories, canonical prompt files, support files, and prompt discovery rules.
- **WIP refactor plan: shared schemas and doc alignment** tracks the current branch TODOs for schema alignment, drift detection, validation, tests, and follow-through.

## Linking guidance

The docs that should directly link to or refer to **Modes and settings** are:

- `README.md` (entry point)
- `auto-mode-policy.md`
- `pipeline-and-stages.md`
- `thresholds-and-recommendations.md`
- `user-preferences-and-memory.md`
- `service-specific-guidance.md`

Reason: `modes-and-settings.md` defines the shared vocabulary for the rest of the system.

## Additional docs

- [Onboarding](./onboarding.md)
- [Examples](./examples.md)
- [Deep search](./deep-search.md)
- [Scoring model](./scoring-model.md)
- [Impromptu prompt library model](./impromptu-library-model.md)
- [WIP refactor plan: shared schemas and doc
  alignment](./refactor-shared-schemas-and-doc-alignment.md)

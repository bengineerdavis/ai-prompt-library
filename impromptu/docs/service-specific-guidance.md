# Service-specific guidance

This document explains how shared context and preferences should be handled across
different environments.

For the general controls users may want to save, see
[Modes and settings](./modes-and-settings.md) and
[User preferences and memory](./user-preferences-and-memory.md).

## Default principle

Always start from the service the user is currently using.

Do not assume that settings should be copied into every other service unless the user
clearly wants cross-service consistency.

Impromptu’s own controls (cost, complexity, verbosity) and preferences live alongside,
not instead of, the platform’s native settings.

## SaaS chat tools

In SaaS chat environments, users should usually store stable context in the platform’s
persistent instructions, memory, project, or profile features when available.

Examples of stable context:

- recurring preferences
- standing constraints
- domain defaults
- favorite output styles
- general house rules

Session-specific context should stay in the current chat.

Impromptu-related preferences (for example, “usually use `cost = medium`,
`complexity = layered`, `verbosity = info`”) can be:

- expressed in the platform’s own instructions, and/or
- managed through Seed/Impromptu defaults when calling factories or workflows from that
  environment.

## Future Impromptu tool or API

When users are working through a future Impromptu tool or API directly, preferences can
be stored in the tool’s own profile and configuration system.

That is a better place for persistent behavior than repeatedly pasting large context
blocks.

In that setting:

- the tool can manage default cost, complexity, and verbosity
- user preferences can shape which internal profiles (Speed, Balanced, Thorough) are
  used by default
- environment-specific details (for example “local vs SaaS” or hardware limits) can
  inform `auto` decisions for cost and complexity

## Important caution

Users who work across multiple services may not want every preference saved into every
platform.

The system should avoid presumptions and ask only when needed, for example:

- whether a newly learned preference should apply just in this environment or across all
  environments
- whether a platform-level instruction should be mirrored in Impromptu’s own preferences

Cross-service consistency should be opt-in, not automatic.

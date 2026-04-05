# Service-Specific Guidance

This document explains how shared context and preferences should be handled across different environments.

For the general controls users may want to save, see [Modes and settings](./modes-and-settings.md).

## Default principle

Always start from the service the user is currently using.

Do not assume that settings should be copied into every other service unless the user clearly wants cross-service consistency.

## SaaS chat tools

In SaaS chat environments, users should usually store stable context in the platform's persistent instructions, memory, project, or profile features when available.

Examples of stable context:
- recurring preferences,
- standing constraints,
- domain defaults,
- favorite output styles,
- and general house rules.

Session-specific context should stay in the current chat.

## Future Impromptu tool or API

When users are working through the future Impromptu tool directly, preferences can be stored in the tool's own profile and configuration system.

That is a better place for persistent behavior than repeatedly pasting large context blocks.

## Important caution

Users who work across multiple services may not want every preference saved into every platform.

The system should avoid presumptions and ask only when needed.

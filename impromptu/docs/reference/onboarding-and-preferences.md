# Onboarding, preferences, and service guidance

This document covers the first-run experience, how preferences are stored and refreshed,
and how Impromptu behaves across different environments.

For the main controls, see
[../controls/modes-and-settings.md](../controls/modes-and-settings.md).

______________________________________________________________________

## Onboarding

### Goal

The first-run experience should be short, helpful, and low-friction.
The system should infer as much as possible first, then ask only a small number of
questions where confidence is low or important preferences are missing.

### Default onboarding principles

- Prefer a short setup over a long interview.
- Ask at most 5 default questions.
- Use conservative defaults.
- Explain the controls in plain language.
- Offer a helper role to assist with later changes.

### Recommended defaults

Start new users with:

- `cost = auto`
- `complexity = auto`
- `verbosity = info`

### First-run explanation

A short explanation might say:

> Impromptu can automatically adapt how much work it does, how conservative or
> adventurous its strategy is, and how much process detail you see.
> By default, it stays conservative and cost-conscious, and it will only ask a few setup
> questions when needed.

### Suggested 5 onboarding questions

Ask only if not already inferred with good confidence.

1. Do you usually want the cheapest workable result, a balanced default, or the
   strongest result?
1. Should I usually keep the strategy simple, or explore more when helpful?
1. How much process do you want to see: quiet, info, or debug?
1. Should I save recurring preferences when I detect stable patterns?
1. Are there any standing rules or constraints I should always respect?

### Helper role

A helper assistant should be available by default in chat.
Its job is to:

- explain the settings
- recommend likely defaults
- help users decide when to change cost or complexity
- update saved preferences when confirmed

### Re-checks

The system should re-check preferences only when:

- a preference is new
- a preference appears stale
- recent behavior suggests a saved default may no longer fit

______________________________________________________________________

## User preferences and memory

### Goal

Reduce repeated user effort.
Instead of asking the same questions repeatedly, the system should learn:

- preferred cost level
- preferred complexity level
- preferred verbosity
- standing constraints
- reusable style preferences
- whether the user usually wants more or fewer alternatives

### Default behavior

The system should first try to infer likely preferences.
It should only ask questions when:

- confidence is low
- a preference is new
- a preference appears stale
- the user has recently behaved in a way that contradicts the saved default

When confidence is high, the system should quietly apply preferences and explain them
only when useful:

> “Using your usual `cost = medium` and `complexity = layered` for this task.”

### Preference refresh

A frecency-style approach is a good fit.
Saved preferences are influenced by:

- how often they are used
- how recently they were used
- whether the user overrides them

Overrides count more than passive acceptance.
If a user frequently adjusts cost or complexity away from the saved default, the system
should propose updating the default rather than nagging.

### What should be persisted

- default cost
- default complexity
- default verbosity
- whether to save recurring overrides
- service- or environment-specific context management preferences
- stable style or formatting preferences that apply across tasks

These persisted preferences influence:

- which defaults are chosen on new sessions
- how `auto` behaves for cost and complexity
- which internal profiles (Speed, Balanced, Thorough) are most appropriate by default

### What should remain flexible

Saved defaults should guide behavior, not trap the user.
Users should always be able to:

- temporarily override cost, complexity, or verbosity for a single task
- try a different profile or mode without committing to it
- decline suggested preference updates

When behavior and saved defaults diverge for long enough, the system can propose an
update in plain language instead of silently changing it.

______________________________________________________________________

## Service-specific guidance

### Default principle

Always start from the service the user is currently using.
Do not assume that settings should be copied into every other service unless the user
clearly wants cross-service consistency.

Impromptu’s own controls (`cost`, `complexity`, `verbosity`) and preferences live
alongside — not instead of — the platform’s native settings.

### SaaS chat tools

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
- managed through Seed/Impromptu defaults when calling factories or workflows

### Future Impromptu tool or API

When users work through a future Impromptu tool or API directly, preferences can be
stored in the tool’s own profile and configuration system.
In that setting:

- the tool can manage default cost, complexity, and verbosity
- user preferences can shape which internal profiles (Speed, Balanced, Thorough) are
  used by default
- environment-specific details (for example “local vs SaaS” or hardware limits) can
  inform `auto` decisions

### Important caution

Users who work across multiple services may not want every preference saved into every
platform. The system should avoid presumptions and ask only when needed — for example:

- whether a newly learned preference should apply just in this environment or across all
  environments
- whether a platform-level instruction should be mirrored in Impromptu’s own preferences

Cross-service consistency should be opt-in, not automatic.

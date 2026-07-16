# Panel of Judges structure

This document defines the structural model for the `panel-of-judges` library.

It explains how reusable events, roles, skills, bundles, sessions, and saved data relate to one another, and it gives a pattern for organizing the library as it grows.

## Table of contents

- [Purpose](#purpose)
- [Core concepts](#core-concepts)
- [Structural rules](#structural-rules)
- [Pattern structure](#pattern-structure)
- [Artifact placement](#artifact-placement)
- [Sessions and saved data](#sessions-and-saved-data)
- [Decision rules](#decision-rules)
- [Factory use](#factory-use)

## Purpose

The library should support three related activities:

1. defining reusable interaction types,
2. combining those reusable parts into sessions,
3. improving the library itself over time.

To do that well, the collection needs a stable structural model.

This document is the reference for that model.

## Core concepts

### Event

An **event** is a reusable interaction protocol with a categorical goal.

An event defines things like:

- what kind of interaction is being run,
- what general outcome it is trying to produce,
- what phases or flow it uses,
- what authority model applies,
- what objections or escalation patterns it allows,
- and what outputs are expected.

An event is not the user's specific ask in a given run.

### Role

A **role** is a reusable participant definition.

A role defines things like:

- perspective,
- responsibilities,
- reasoning style,
- contribution style,
- and output expectations.

Roles should usually remain portable across multiple event types.

### Skill

A **skill** is a reusable capability or method.

A skill provides a way of doing work that may be relevant across multiple roles or events.

A skill is different from a role:

- a **role** answers who is participating and from what perspective,
- a **skill** answers what reusable capability is available.

### Bundle

A **bundle** is a runnable assembly for a specific event configuration.

A bundle selects and combines the relevant event definition, roles, optional skills, and supporting context needed for a session.

### Session

A **session** is one actual run.

A session combines:

- an event,
- one or more roles,
- optional skills,
- and session-specific context or asks.

### Data

**Data** means saved outputs from sessions.

This can include:

- minutes,
- notes,
- handoffs,
- follow-up records,
- and other event-instance artifacts.

Data is historical record, not reusable protocol definition.

## Structural rules

### Separate reusable definitions from session data

Keep reusable definitions separate from outputs of actual sessions.

Reusable definitions include:

- events,
- roles,
- skills,
- templates,
- structure and bundler documentation.

Session data includes:

- minutes,
- notes,
- handoffs,
- and other occurrence-specific records.

### Keep roles and skills library-scoped

Roles and skills belong at library scope by default.

This supports reuse across different event types and avoids unnecessary duplication.

### Keep bundles and data event-local

Bundles belong with the event they configure.

Data belongs with the event that produced it.

This keeps each event type self-contained in practice while preserving reusable roles and skills at library scope.

## Pattern structure

This is a pattern, not a frozen inventory.

```sh
panel-of-judges/
  README.md
  STRUCTURE.md
  BUNDLER.md

  context/
    charter.md
    <shared-context>.md

  events/
    <event-type>/
      event.md
      preferences.md               # optional reusable defaults for the event type
      session-prompt.md            # optional event bootstrap prompt
      meeting-template.md          # optional output template
      bundles/
        bundle.yaml
        bundle.<variant>.yaml
      data/
        minutes/
        notes/
        handoffs/

  roles/
    <role>.md
    judges/
      <judge-role>.md
    specialists/
      <specialist-role>.md

  skills/
    <skill>.md

  templates/
    event-template.md
    role-template.md
    skill-template.md
    role-invocation-template.md
    <other-template>.md

  generated/

  handoff-context.md              # optional shared continuity summary
  ROADMAP.md                      # optional future-oriented planning notes
```

## Artifact placement

Use these default rules.

| Artifact type | Default location | Rationale |
|---|---|---|
| Event protocol | `events/<event-type>/` | Defines a reusable interaction type |
| Event bundle | `events/<event-type>/bundles/` | Configures how that event is run |
| Event session data | `events/<event-type>/data/` | Stores outputs from real runs of that event |
| Role | `roles/` or role subdirectories | Reusable participant definition |
| Skill | `skills/` | Reusable capability |
| Template | `templates/` | Reusable authoring scaffold |
| Shared context | `context/` | Collection-wide guidance or reference |

## Sessions and saved data

A specific task or conversation is a **session**, not a new event type unless the protocol itself is meaningfully different.

Recommended event-local data pattern:

```text
events/<event-type>/data/
```

Recommended minutes pattern:

```text
events/<event-type>/data/minutes/<event-type>-NNN-minutes.md
```

Examples:

- `events/advisory-meeting/data/minutes/advisory-meeting-001-minutes.md`
- `events/evaluation/data/minutes/evaluation-002-minutes.md`

Recommended additional data directories when useful:

```text
events/<event-type>/data/notes/
events/<event-type>/data/handoffs/
```

## Decision rules

Use these rules when deciding where something belongs.

1. If it defines interaction flow and a categorical goal, it is probably an **event**.
2. If it defines a reusable participant perspective, it is probably a **role**.
3. If it defines a reusable capability or method, it is probably a **skill**.
4. If it assembles reusable artifacts into a runnable setup, it is probably a **bundle**.
5. If it records one actual run or follow-up from that run, it is probably **data**.

## Factory use

Factory or meta work should use this document when proposing structural changes.

Useful questions include:

- Is this a new event type or just a session of an existing event?
- Should this become a new role or a new skill?
- Does this belong in shared templates or inside one event?
- Should this bundle live with the event?
- Is this reusable definition or historical session data?

This document exists so those decisions stay consistent over time.
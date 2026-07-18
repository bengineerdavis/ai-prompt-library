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
- [Data naming conventions](#data-naming-conventions)
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

A bundle may be the default configuration for an event or a named variant of that event.

### Session

A **session** is one actual run.

A session combines:

- an event,
- one or more roles,
- optional skills,
- a selected bundle or bundle variant,
- and session-specific context or asks.

A session is an occurrence, not a reusable definition.

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

### Make session history easy to follow

Saved data should make it obvious which records belong to the same session and which bundle variant was used.

This should be readable from filenames alone, without requiring inspection of file contents.

### Prefer flat storage with informative filenames

Use shallow event-local data directories with strong filename conventions rather than deeply nesting every session into its own directory.

A flatter layout is easier to scan, grep, sort, and continue from later, as long as filenames carry the needed identifiers.

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
        followups/

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

Recommended data subdirectories:

```text
events/<event-type>/data/minutes/
events/<event-type>/data/notes/
events/<event-type>/data/handoffs/
events/<event-type>/data/followups/
```

Use filenames to encode the session identity and the bundle variant used for that session.

A session should have one stable **session id** shared across all artifacts created from that same run or continuation chain.

A good default pattern is:

```text
<event-type>-<session-id>-<bundle-key>-<artifact-kind>.md
```

Where:

- `<event-type>` is the base event directory name,
- `<session-id>` is a sortable unique identifier for the session,
- `<bundle-key>` is `default` or a variant name,
- `<artifact-kind>` is `minutes`, `notes`, `handoff`, or another saved artifact type.

### Session identity

The `session-id` should identify one continuous working thread.

When a later meeting or continuation should build on the same thread, it should reuse the same session id and create a new artifact file for the new step, rather than inventing a new unrelated id.

When a new thread starts, create a new session id.

Recommended session id patterns:

- numeric sequence per event, such as `001`, `002`, `003`,
- or date plus sequence, such as `2026-07-16-001`.

Prefer a sortable pattern.

### Bundle key

The `bundle-key` should reflect the bundle variant used to run the session.

Use:

- `default` for `events/<event-type>/bundles/bundle.yaml`,
- the variant suffix for `events/<event-type>/bundles/bundle.<variant>.yaml`.

Examples:

- `default`
- `with-research`
- `factory-review`

This makes it easy to see which reusable configuration produced a session artifact.

### Artifact examples

Recommended examples:

- `events/advisory-meeting/data/minutes/advisory-meeting-001-default-minutes.md`
- `events/advisory-meeting/data/notes/advisory-meeting-001-default-notes.md`
- `events/advisory-meeting/data/handoffs/advisory-meeting-001-default-handoff.md`
- `events/advisory-meeting/data/minutes/advisory-meeting-002-with-research-minutes.md`
- `events/advisory-meeting/data/notes/advisory-meeting-002-with-research-notes.md`
- `events/advisory-meeting/data/handoffs/advisory-meeting-002-with-research-handoff.md`
- `events/advisory-meeting/data/followups/advisory-meeting-002-with-research-followup.md`

### Continuations and history

If a new session should continue prior work, the previous session's artifacts should be discoverable by shared session id or by filename prefix.

This means the bundler or future helper tools can locate prior history using simple pattern matching such as:

```text
advisory-meeting-002-with-research-*
```

or, when variant changes but the same thread continues:

```text
advisory-meeting-002-*
```

This is one reason to keep the session id independent from the bundle key.

### Flat but traceable

The goal is not to represent every session as a deeply nested directory tree.

The goal is to keep event-local data relatively flat while preserving enough filename structure that a human or script can answer questions like:

- Which minutes belong to session 002?
- Which handoff was created from the `with-research` bundle?
- What notes should be included to continue this thread?
- Which session artifacts belong together?

## Data naming conventions

Use these conventions by default.

| Part | Rule | Example |
|---|---|---|
| Event type | Use the canonical event directory name | `advisory-meeting` |
| Session id | Use a sortable stable id | `001`, `2026-07-16-001` |
| Bundle key | Use `default` or variant suffix | `default`, `with-research` |
| Artifact kind | Use a singular stable label | `minutes`, `notes`, `handoff`, `followup` |
| Extension | Use markdown for now | `.md` |

Default filename formula:

```text
<event-type>-<session-id>-<bundle-key>-<artifact-kind>.md
```

If a specific artifact needs multiple revisions, add a final revision suffix after the artifact kind.

Example:

```text
advisory-meeting-002-with-research-handoff-v2.md
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
- Does the filename make the session id and bundle variant obvious?
- Could a future bundler or continuation helper find the right history by pattern match alone?

This document exists so those decisions stay consistent over time.
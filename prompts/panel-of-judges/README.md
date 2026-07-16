# Panel of Judges

Reusable library of events, roles, and skill files that can be combined into a session.

## Table of contents

- [Purpose](#purpose)
- [Core concepts](#core-concepts)
- [Library structure](#library-structure)
- [Event-local bundles and data](#event-local-bundles-and-data)
- [How to add new artifacts](#how-to-add-new-artifacts)
- [Use model](#use-model)
- [Notes](#notes)

## Purpose

The **panel of judges** is a reusable library for structured multi-role interactions.

It is designed for situations where multiple perspectives improve the result, including generation, review, comparison, decision support, refinement, and meta/factory work on the library itself.

This library is not limited to meetings. A meeting is one kind of event that can be defined and reused within the collection.

## Core concepts

The collection separates reusable artifacts so they can be recombined in different sessions.

- **Event** — a reusable interaction protocol with a categorical goal; it defines the type of interaction, not the user's specific ask in a given run.
- **Role** — a reusable participant definition with a perspective, responsibilities, and contribution style.
- **Skill** — a reusable capability or method that may be used across multiple roles or events.
- **Bundle** — a runnable assembly for a specific event configuration.
- **Session** — one actual run that combines an event, roles, optional skills, and session-specific context.
- **Data** — saved outputs from a session, such as minutes, notes, or handoffs.

A role should remain portable across events, and a skill should remain portable across roles and events unless there is a strong reason to scope it more narrowly.

## Library structure

The README describes the pattern, not a fixed inventory.

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
      preferences.md               # optional reusable defaults for that event type
      session-prompt.md            # optional event bootstrap prompt
      meeting-template.md          # optional output/minutes template
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

  handoff-context.md              # optional cross-session continuity
  ROADMAP.md                      # optional future-facing questions and plans
```

Guiding rules:

- Put reusable interaction protocols under `events/`.
- Put reusable participant definitions under `roles/`.
- Put reusable capabilities under `skills/`.
- Put event-specific operational configs under that event's `bundles/`.
- Put saved session outputs under that event's `data/`.

## Event-local bundles and data

Bundles should live with the event they configure, because they are part of how that event is run in practice.

Recommended pattern:

```text
events/<event-type>/bundles/
```

Saved outputs from real sessions should also live with the event that produced them.

Recommended pattern:

```text
events/<event-type>/data/
```

For minutes:

```text
events/<event-type>/data/minutes/<event-type>-NNN-minutes.md
```

This keeps reusable protocol definitions separate from records of specific sessions while still keeping each event type self-contained.

## How to add new artifacts

### Add a new event

Create a new directory under `events/<event-type>/` and add at least:

- `event.md`

Optionally add:

- `preferences.md`
- `session-prompt.md`
- `meeting-template.md`
- `bundles/`
- `data/`

Use `templates/event-template.md` as the starting point.

### Add a new role

Create a Markdown file under `roles/`, `roles/judges/`, or `roles/specialists/` depending on the role's type.

Use `templates/role-template.md` as the starting point.

### Add a new skill

Create a Markdown file under `skills/`.

Use `templates/skill-template.md` as the starting point.

### Add a new bundle variant

Create a new bundle config under the related event's `bundles/` directory.

Use a naming pattern like:

- `bundle.yaml`
- `bundle.with-research.yaml`
- `bundle.factory-review.yaml`

## Use model

1. Choose an event type.
2. Choose the roles needed for that event.
3. Add any relevant skills or supporting context.
4. Use the appropriate bundle for that event.
5. Run the session.
6. Save the resulting minutes, notes, and handoffs under that event's `data/` directory.
7. Route reusable improvements into future factory/meta work when needed.

## Notes

`STRUCTURE.md` should hold the more explicit architectural rules for the library, while this README remains the shorter orientation guide.

Bundler-specific behavior and config details should live in `BUNDLER.md` or its current equivalent.
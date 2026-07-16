# Panel of Judges

Reusable multi-role interaction kit for idea generation, evaluation, refinement, and decision support.

## Purpose

The panel of judges is a reusable collection for involving two or more roles, agents, or models in the same task.

It can be used whenever multiple perspectives are useful for:

- generating ideas,
- exploring solutions,
- comparing options,
- pressure-testing plans,
- evaluating outputs,
- refining proposals,
- surfacing tradeoffs,
- resolving disagreements,
- selecting a direction.

The panel is not limited to meetings. Meetings are one event type within this collection, but the same collection can also support brainstorming, planning review, protocol review, evaluation, adjudication, and stuck-resolution.

## Design model

The collection separates three reusable layers:

- events define interaction types,
- roles define participants,
- shared context defines common principles across the collection.

This keeps the system portable. A role should make sense across many events. An event should be able to use different role sets. The collection should stay useful even as individual event types evolve or are replaced.

## Governance

Authority belongs to the active event, not to the collection as a whole.

The collection supplies reusable roles and shared principles. Each event defines its own authority model, objection procedure, and flow.

## Structure

Suggested structure:

```sh
panel-of-judges/
├── README.md
├── bundle.py
├── prompts/
│   └── panel-of-judges/
│       ├── bundle.yaml
│       ├── bundle.advisory-meeting.yaml
│       ├── bundle.advisory-meeting-with-research.yaml
│       ├── context/
│       │   ├── charter.md
│       │   └── meetings-charter.md
│       ├── events/
│       │   ├── advisory-meeting/
│       │   │   ├── event.md
│       │   │   ├── preferences.md
│       │   │   ├── session-prompt.md
│       │   │   ├── handoff-context.md
│       │   │   └── data/
│       │   │       └── minutes/
│       │   │           └── advisory-meeting-001-minutes.md
│       │   ├── brainstorming/
│       │   │   └── event.md
│       │   ├── planning-review/
│       │   │   └── event.md
│       │   ├── protocol-review/
│       │   │   └── event.md
│       │   ├── evaluation/
│       │   │   └── event.md
│       │   └── stuck-resolution/
│       │       └── event.md
│       ├── roles/
│       │   ├── chair.md
│       │   ├── facilitator.md
│       │   ├── note-taker.md
│       │   ├── judges/
│       │   │   ├── pragmatist.md
│       │   │   ├── minimalist.md
│       │   │   └── systems-thinker.md
│       │   └── specialists/
│       │       ├── deep-researcher.md
│       │       ├── people-expert.md
│       │       └── recruiter.md
│       ├── skills/
│       │   ├── analysis.md
│       │   ├── deep-research.md
│       │   └── interview.md
│       ├── templates/
│       │   └── meeting-session-prompt.md
│       └── generated/
│           └── session.txt
```

## Bundling model

The active bundler is `bundle.py`.

Bundle config files live at the collection root under `prompts/<collection>/`. The config selects an event type, participant roles, optional skills, and optional additional context.

The value of `event.name` must exactly match an existing directory under `events/`. That event directory is the canonical representation of the interaction type.

Example bundle config:

```yaml
event:
  name: advisory-meeting

participants:
  roles:
    - chair
    - facilitator
    - note-taker
    - pragmatist
    - minimalist
    - systems-thinker

skills:
  - analysis

include:
  context:
    - handoff-context
    - events/advisory-meeting/data/minutes/advisory-meeting-001-minutes.md
```

## Running the bundler

Run the default config for the collection:

```bash
./bundle.py -p panel-of-judges
```

Preview a session without writing output:

```bash
./bundle.py -p panel-of-judges --dry-run
```

Run a specific config:

```bash
./bundle.py -c prompts/panel-of-judges/bundle.advisory-meeting-with-research.yaml
```

By default, output is written to `prompts/<collection>/generated/session.txt`.

## Working state

Reusable prompt source and working session records should stay separate.

Reusable source belongs in event definitions, roles, skills, templates, and shared context. Working records such as minutes, prior outputs, or handoff material should live under the relevant event type, usually beneath `events/<event-type>/data/`.

Example:

```text
events/advisory-meeting/data/minutes/advisory-meeting-001-minutes.md
```

Include those files in new sessions through `include.context` paths relative to the collection root.

## Use model

1. Pick an event type.
2. Select the roles needed for that event.
3. State the task, goal, and context.
4. Let roles generate, critique, compare, refine, or evaluate.
5. Record decisions, tradeoffs, and follow-up work.
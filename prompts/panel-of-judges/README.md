# Panel of Judges

Reusable multi-role interaction kit for idea generation, evaluation, refinement, decision support, and reusable event/factory development.

## Purpose

The **panel of judges** is a reusable collection for involving two or more roles, agents, or models in the same task.

It can be used whenever multiple perspectives are useful for:

- generating ideas
- exploring solutions
- comparing options
- pressure-testing plans
- evaluating outputs
- refining proposals
- surfacing tradeoffs
- resolving disagreements
- selecting a direction
- reviewing and improving the collection itself

The panel is not limited to meetings.

Meetings are one event type within this collection, but the same collection can also support brainstorming, planning review, protocol review, evaluation, adjudication, stuck-resolution, and meta/factory work on roles, prompts, workflows, and event definitions.

## Design idea

The collection separates reusable layers so the system stays portable and composable:

- **Events** define interaction types.
- **Roles** define participants.
- **Skills** define reusable capabilities or methods.
- **Shared charter text** defines common principles across the collection.
- **Templates** define reusable scaffolding.
- **Factory/meta artifacts** support improving the collection itself over time.

This keeps the system portable.

A role should make sense across many events.  
An event should be able to use different role sets.  
A skill should be reusable across events and roles.  
The collection should stay useful even as individual event types evolve or are replaced.

## What the panel is for

The panel exists to create structured complementarity.

Different roles bring different concerns, standards, heuristics, and forms of reasoning to the same task so that outcomes are stronger than what a single role or model would usually produce alone.

The point is not rhetorical competition.  
The point is better generation, better critique, better comparison, better decisions, and clearer follow-through.

## Interaction categories

This collection can support event types such as:

- **Generation events** — create ideas, options, plans, hypotheses, or drafts
- **Review events** — critique, test, challenge, or refine existing work
- **Selection events** — compare alternatives and choose a direction
- **Resolution events** — unblock stalled discussions or conflicting positions
- **Advisory events** — examine a principal’s situation, constraints, tradeoffs, and next actions
- **Meta events** — improve roles, prompts, workflows, event types, templates, or governance rules

## Governance default

Authority belongs to the active event, not to the collection as a whole.

The collection supplies reusable roles, skills, templates, and shared principles.  
Each event defines its own authority model, objection procedure, flow, and output expectations.

## Bundling and use

The recommended entry point for structured sessions is `bundle.py`, which assembles a paste-ready session prompt from the collection’s reusable source files.

Typical use:

```bash
# from repo root
./bundle.py -p panel-of-judges

# preview without writing output
./bundle.py -p panel-of-judges --dry-run

# run a specific config variant
./bundle.py -p panel-of-judges -c prompts/panel-of-judges/bundle.advisory-meeting-with-research.yaml
```

By default, the generated output is written to:

```text
prompts/panel-of-judges/generated/session.txt
```

Bundle configs define:

- the active event,
- the participating roles,
- optional skills,
- and optional include material such as handoff context, templates, factory/meta references, or roadmap material.

For bundler details, config schema, defaults inheritance, and file inclusion order, see `BUNDLER-13.md`.

## Suggested structure

```sh
panel-of-judges/
  README.md
  BUNDLER-13.md

  bundle.yaml
  bundle.advisory-meeting.yaml
  bundle.advisory-meeting-with-research.yaml
  bundle.advisory-meeting-factory-review.yaml
  defaults.advisory-meeting.yaml

  context/
    charter.md

  events/
    advisory-meeting/
      event.md
      preferences.md
      meeting-template.md
      session-prompt.md
    brainstorming/
      event.md
    planning-review/
      event.md
    protocol-review/
      event.md
    evaluation/
      event.md
    stuck-resolution/
      event.md

  roles/
    chair.md
    facilitator.md
    note-taker.md
    recruiter.md
    advisors.md
    judges/
      pragmatist.md
      minimalist.md
      systems-thinker.md
    specialists/
      deep-researcher.md
      negotiator.md
      people-expert.md

  skills/
    analysis.md
    deep-research.md

  templates/
    event-template.md
    role-template.md
    role-invocation-template.md

  data/
    minutes/

  generated/

  handoff-context.md
  ROADMAP.md
```

Not every collection or event needs every directory.  
The point of the structure is to keep reusable runtime material separate from reusable factory/meta material.

## Event instances and factory work

The collection supports both:

1. **running an event instance**, and
2. **improving the collection itself**.

That distinction matters.

An event instance should focus on the live task: the principal’s question, the current decision, the active tradeoffs, and the resulting actions.

Factory or meta work should focus on reusable improvements: better event definitions, role updates, new skills, new templates, improved handoff formats, and better workflow support.

A live event may identify reusable improvement opportunities, but those opportunities should usually be recorded as handoffs rather than resolved ad hoc inside the same session.

## Handoffs and continuity

The collection can preserve follow-up context in reusable forms such as:

- event minutes
- `handoff-context.md`
- structured factory handoff candidates
- future roadmap questions
- changelog-oriented notes

This makes it easier to move from:

- live meeting observations,
- to reusable handoff records,
- to factory review,
- to collection updates.

## Use model

1. Pick an event type.
2. Activate the roles needed for that event.
3. Add any relevant skills or supporting context.
4. State the task, goal, and context.
5. Let roles generate, critique, compare, refine, or evaluate.
6. Record decisions, tradeoffs, objections, handoffs, and follow-up work.
7. Route reusable improvement opportunities into factory/meta work when appropriate.

## Design principle

The collection should be usable at three levels:

- **session level** — run one good interaction
- **event level** — reuse a strong interaction pattern
- **factory level** — improve the system that creates and runs those interaction patterns

That separation is what lets the collection stay coherent while still evolving.
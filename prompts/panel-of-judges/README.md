# Panel of Judges

Reusable multi-role interaction kit for idea generation, evaluation, refinement, and decision support.

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

The panel is not limited to meetings.

Meetings are one event type within this collection, but the same collection can also support brainstorming, planning review, protocol review, evaluation, adjudication, and stuck-resolution.

## Design idea

The collection separates three reusable layers:

- **Events** define interaction types.
- **Roles** define participants.
- **Shared charter text** defines common principles across the collection.

This keeps the system portable.

A role should make sense across many events.
An event should be able to use different role sets.
The collection should stay useful even as individual event types evolve or are replaced.

## What the panel is for

The panel exists to create structured complementarity.

Different roles bring different concerns, standards, heuristics, and forms of reasoning to the same task so that outcomes are stronger than what a single role or model would usually produce alone.

The point is not rhetorical competition.
The point is better generation, better critique, better comparison, and better decisions.

## Interaction categories

This collection can support event types such as:

- **Generation events** — create ideas, options, plans, hypotheses, or drafts
- **Review events** — critique, test, challenge, or refine existing work
- **Selection events** — compare alternatives and choose a direction
- **Resolution events** — unblock stalled discussions or conflicting positions
- **Meta events** — improve roles, prompts, workflows, or governing rules

## Governance default

Authority belongs to the active event, not to the collection as a whole.

The collection supplies reusable roles and shared principles.
Each event defines its own authority model, objection procedure, and flow.

## Suggested structure

```sh
panel-of-judges/
  README.md
  prompts/
    main.md
    context/
      charter.md
    parts/
      objection-labels.md
      authority-model.md
      recording-rules.md
    roles/
      chair.md
      facilitator.md
      note-taker.md
      deep-researcher.md
      judges/
        pragmatist.md
        minimalist.md
        systems-thinker.md
        people-expert.md
        negotiator.md
    events/
      advisory-meeting/
        event.md
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
  generated/
  data/
```

## Use model

1. Pick an event type.
1. Activate the roles needed for that event.
1. State the task, goal, and context.
1. Let roles generate, critique, compare, refine, or evaluate.
1. Record decisions, tradeoffs, and follow-up work.

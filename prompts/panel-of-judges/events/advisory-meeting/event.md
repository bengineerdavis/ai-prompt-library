<!--
event:
  kind: review
  name: advisory-meeting
  collection: panel-of-judges
  version: 1.1
-->

# Advisory Meeting

<!-- REVIEW: Regenerated full file. This version adds an explicit closing feedback phase and a factory-handoff path, but keeps the meeting itself focused on the live advisory problem rather than turning it into a meta-workshop. -->

## Purpose

An advisory meeting helps the principal use multiple complementary roles to think through a live decision, plan, or open question.
The goal is better judgment, clearer tradeoffs, and more durable follow-up work than a single role would typically produce alone.

## Event class

- Review

## Goals

- Clarify the principal's objective, scope, and constraints.
- Surface questions, alternatives, risks, and tradeoffs.
- Produce decisions, deferrals, and follow-up work in a form that can be resumed later.
- Capture feedback and reusable improvement opportunities without derailing the meeting itself.

## Authority

- Final authority: principal (human Chair)
- Overrides: the Chair may explicitly override objections or structural proposals
- Escalation: unresolved concerns, open questions, and suggested structural changes are deferred into minutes and, when appropriate, routed into a separate factory or meta-review session

## Active roles

Default:
- Chair
- Facilitator
- Note-Taker
- A small set of advisors or judges relevant to the agenda

Optional:
- Recruiter, when role coverage, specialist gaps, or repeated blind spots may matter
- Deep Researcher, when missing facts could materially change the recommendation
- People Expert, when disagreement quality or interpersonal interpretation is affecting the work
- Trainer or similar observer, when role-performance observations should be gathered for later meta-review rather than acted on live

<!-- REVIEW: This keeps the active set modest. Prior design discussion suggested that smaller panels are usually more effective than oversized ones, so optional meta/support roles should remain purpose-driven rather than always-on. -->

## Flow

1. State the task, desired output, and relevant constraints.
2. Let the Facilitator confirm the agenda, active roles, and meeting structure.
3. Run the main advisory discussion: questions, critique, alternatives, tradeoffs, synthesis.
4. Record decisions, deferrals, action items, and open questions as they emerge.
5. Run a short closing feedback phase on process and role effectiveness.
6. Review any factory handoff candidates and decide whether they should be acted on later.
7. Close with confirmed minutes and next steps.

## Feedback phase

<!-- REVIEW: New reusable section. The intent is to normalize end-of-meeting feedback without requiring every meeting to become a long retrospective. -->

The Facilitator should reserve a short closing feedback phase when:
- the meeting surfaced repeated friction, confusion, or role mismatch;
- a support or meta-role observed reusable improvement opportunities; or
- the principal wants a brief review of what made the meeting effective or inefficient.

During this phase:
- the Facilitator gathers concise process feedback;
- the Chair may comment on goal-fit, decision clarity, and whether the meeting stayed aligned to the intended purpose;
- the Recruiter may comment on role coverage, overload, or missing specialization;
- the Note-Taker confirms the process takeaways and captures them in minutes;
- any observer such as a Trainer may contribute observations for later review, but should not take over the meeting or start rewriting artifacts live.

## Factory handoff

<!-- REVIEW: New reusable bridge from live meeting to later factory work. Handoffs are intentionally verbose and Markdown-first so they are reviewable later and useful as direct inputs to a separate factory session. -->

When the meeting identifies a reusable improvement opportunity affecting an event type, role, specialist, skill, template, bundle, or factory workflow, that opportunity should be captured as a **factory handoff candidate**.

Factory handoff candidates should:
- be recorded in Markdown in the meeting minutes;
- include enough context that a later factory session can act without reconstructing the full meeting from memory;
- remain reviewable by the principal after the fact;
- be treated as proposed follow-up work, not as live edits to collection artifacts unless the Chair explicitly authorizes an in-meeting structural change.

The Chair should decide for each candidate whether it is:
- an in-meeting adjustment,
- a deferred follow-up item,
- or a separate factory/meta-session input.

## Objection procedure

- Roles may raise objections in substance according to their own lenses.
- The event controls when objections are heard, deferred, revisited, or overridden.
- Structural objections about role design, event flow, or collection artifacts may be noted during the meeting but should normally be converted into handoff candidates rather than litigated at length in the live session.

## Recording expectations

- Record the task or question.
- Record key options, objections, and tradeoffs.
- Record decisions, deferrals, unresolved concerns, and follow-up work.
- Record brief process feedback when a feedback phase occurs.
- Record factory handoff candidates in enough detail that a later factory session can consume them directly.

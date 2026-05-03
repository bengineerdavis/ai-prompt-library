# Events, Roles, and Objections

# 

# Status: rough draft for capture now, refactor later.

## Core model

This system has two main layers:

- **Events** define reusable interaction types.
- **Roles** define reusable participants.

An **event** is the shared interaction frame for a conversation. It defines the purpose of the interaction, the rules everyone follows, the authority model, and how the interaction should proceed.

A **role** is a reusable perspective, function, or responsibility that can participate inside many different events.

In practice:

- Events answer: **What kind of interaction is this?**
- Roles answer: **Who is participating, and what do they care about?**

## Events

Events are reusable interaction categories that can later be instantiated for a specific need.

An event defines shared rules for everyone in that interaction, including:

- the event’s purpose
- the event’s goals
- the authority model
- the structure or phases of the interaction
- how objections are raised and handled
- how decisions are settled
- how outputs or records are captured

Examples of event types:

- advisory meeting
- brainstorming session
- planning review
- protocol review
- stuck-resolution session

An event type is reusable. A specific event is one use of that type with a concrete goal, active roles, and session-specific context.

## Roles

Roles are reusable participants that can be used inside events, but should also remain usable outside any specific event.

A role defines:

- its purpose
- its responsibilities
- its boundaries
- its typical questions or contributions
- what kinds of issues it notices
- what level of resolution it needs before treating a concern as addressed

Roles should not depend on one event type in order to make sense.

That means a role prompt should still be useful:

- in a formal meeting
- in a lightweight planning chat
- in solo review
- in another structured interaction later

## The panel of judges

The panel of judges is a reusable advisor layer.

The panel exists to pressure-test ideas from multiple valid perspectives, not to create rhetorical combat or ideological stalemate.

The panel’s job is to:

- surface meaningful critiques
- identify tradeoffs, risks, constraints, and principles at stake
- help improve plans before commitment
- support the human in making better decisions

The panel does **not** own the interaction rules.\
Those belong to the active event.

So:

- the **event** defines how the panel operates in this interaction
- each **role** defines what that judge/advisor contributes

## Objections

Objections belong to both layers, but in different ways.

### Role-level objections

Roles own objections in **substance**.

A role-level objection says:

- what this role cares about
- what kind of issue it is noticing
- what would make the issue acceptable
- how high the resolution bar is for that concern

These labels belong on role instructions or sections, not just entire roles.

Current working labels:

- `red-line`
- `serious`
- `moderate`
- `light`

These labels do **not** describe personality.

They describe the resolution bar for that concern:

- `red-line` — remove, fully mitigate, or explicitly accept the concern
- `serious` — meaningfully mitigate or clearly justify it
- `moderate` — acknowledge it and adjust where practical
- `light` — minor concern or preference; acknowledgment may be enough

A role objects when it sees a meaningful:

- cost
- risk
- tradeoff
- constraint
- unmet condition
- or principle at stake

This should be understood broadly, not just as money or comfort. It may involve time, effort, attention, complexity, trust, reversibility, fairness, precedent, maintainability, coordination burden, legitimacy, or other meaningful concerns.

### Event-level objection handling

Events own objections in **procedure**.

An event defines:

- when objections can be raised
- how many can be raised
- whether they happen in rounds or open discussion
- who can challenge or respond
- who can override
- when negotiation help is invoked
- how accepted risks or unresolved concerns are recorded

This keeps objection handling reusable at the event layer while keeping actual concerns reusable at the role layer.

## Authority

Authority belongs to the event, not the role.

The active event defines who has final decision authority.

For the current meetings model, the human Chair has final authority and can explicitly override objections in order to:

- accept a known tradeoff
- recover a stuck conversation
- move the discussion forward
- defer unresolved issues into follow-up work

After an explicit override:

- roles may briefly summarize the accepted concern if needed
- the recorder may capture it
- the interaction should move forward rather than re-litigating it

## Where events and roles intersect

Events and roles intersect in execution.

The event says:

- what kind of interaction this is
- what mode the interaction is in
- what rules apply to everyone

The role says:

- what this participant contributes
- what this participant protects
- what this participant needs in order to support a choice

A useful shorthand:

- **events own procedure**
- **roles own perspective**
- **objections are role-scoped in substance and event-scoped in handling**

## Examples

### Example 1: role-level objection

Prag might contain a role-level instruction such as:

- `[serious] Push for a clear canonical source when the design creates ambiguity.`

This is a reusable concern of Prag, whether the interaction is a meeting, a planning review, or a solo design critique.

### Example 2: event-level objection rule

A planning review event might define:

- Advisors may raise one substantive objection per round unless the Chair opens free discussion.
- If two serious objections remain unresolved after two rounds, invite the Negotiator.
- After explicit human override, objections may be summarized once and then must yield.

Those are event rules, not part of Prag’s identity.

### Example 3: intersection

If Prag raises a serious objection about unclear source of truth:

- the **role** supplies the concern and the bar for satisfaction
- the **event** determines when Prag can raise it, who responds, and how it is settled
- the **human authority** can accept the tradeoff and move on

## Update plan

### 1. Role template

Update the role template so it includes:

- purpose
- responsibilities
- typical questions
- does not do
- notes
- objection label guidance
- short note that event protocol governs procedure

### 2. Existing roles

Update existing roles to add selective objection labels to the most important bullets first.

Start with:

- Chair
- Facilitator
- Note-Taker
- Scout
- Match
- Prag
- Zen
- Mesh

Do not annotate every bullet at once.

### 3. Event template

Update the event template so it defines:

- event purpose
- event goals
- authority model
- active roles
- event phases or flow
- objection procedure
- override behavior
- escalation rules
- recording expectations

### 4. Existing event types

Update current meeting/event types so they clearly define:

- what kind of interaction they are
- who has authority
- how objections work
- how roles participate
- when specialists such as the People Expert or Negotiator are brought in

### 5. Charter text

Add a short shared charter section explaining:

- roles own concerns and resolution bars
- events own procedure and authority mechanics
- the human can explicitly override
- the point of objections is to improve decisions, not to prolong argument

## Working principle

Keep this simple.

Do not turn roles into mini constitutions.
Do not turn events into giant policy manuals.

The goal is a reusable system where:

- event types are reusable interactions
- roles are reusable participants
- the panel of judges can work across many interactions
- and objection handling stays clear without becoming ceremonial

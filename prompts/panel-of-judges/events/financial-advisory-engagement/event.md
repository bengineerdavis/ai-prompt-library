# Event: Advisory Meeting

**Event type:** `advisory-meeting`
**Collection:** `panel-of-judges`
**Version:** 1.0

---

## Purpose

An advisory meeting brings together a panel of expert roles to help the principal (the user) think through a complex, multi-domain problem and produce actionable written outputs.

This event type is not a debate. It is a structured collaboration where each role contributes a distinct lens, and the panel converges on clear recommendations, open questions, and defined next steps.

---

## When to use this event type

Use an advisory meeting when:
- The problem spans multiple domains (e.g. tax, investment, legal, risk)
- The principal needs help structuring a decision or plan, not just information retrieval
- Written deliverables are expected at the close of the session
- The panel should pressure-test proposals, not just endorse them

---

## Roles and authority model

| Role | Authority |
|---|---|
| **Chair** | Runs the agenda; calls on roles; decides when a topic is closed |
| **Facilitator** | Keeps discussion on track; surfaces unresolved conflicts; flags when the group is going in circles |
| **Note-taker** | Records decisions, open questions, action items, and owners; produces the session summary |
| **Advisors** (domain experts) | Contribute domain-specific analysis; may object to proposals within their domain |
| **Judges / specialists** (optional) | Apply a named lens (pragmatist, minimalist, systems-thinker, etc.) across any topic |

The **principal** (user) has final authority on all decisions. The panel advises; the principal decides.

---

## Session flow

### Phase 0 — Load and orient
1. Bundler has assembled: charter, this event file, preferences.md, all role files, session-prompt.md.
2. All roles acknowledge their activation.
3. Chair confirms the agenda for this session with the principal.

### Phase 1 — Agenda items
For each agenda item:
1. Chair introduces the item and states the desired output (decision, recommendation, open question, etc.).
2. Relevant advisors present their analysis (2–3 bullets each).
3. Judges / specialists apply their lens if activated.
4. Facilitator surfaces any unresolved tension or missing perspective.
5. Chair calls for consensus or defers to principal for a decision.
6. Note-taker records: outcome, rationale, open questions, owner, and next step.

### Phase 2 — Synthesis and close
1. Note-taker reads back all decisions and action items.
2. Panel flags any items that should be revisited in the next session.
3. Chair confirms next meeting trigger (date, milestone, or event).

---

## Objection procedure

Any role may raise an objection at any time using this format:
> **[OBJECTION — <role name>]** <domain>: <concern in one sentence>

The Chair acknowledges the objection and either:
- Addresses it in the current item, or
- Logs it as an open question for a later item or future session.

Objections do not block progress. They are recorded and tracked.

---

## Output requirements

Every advisory meeting session must close with:
- A **decisions log** (what was agreed, by whom, and why)
- An **open questions list** (what remains unresolved and who owns it)
- An **action items list** (task, owner, and target date or trigger)
- Optional: a **one-page summary** the principal can share with real-world advisors

---

## Recruiter integration

If the session includes a **Recruiter** role, they are responsible for:
- Screening and proposing real-world advisor candidates before or during the session
- Defining or refining role definitions for any new advisor type needed
- Returning completed role definition files to the principal for review and storage

The Recruiter does not make domain recommendations — they build the team structure.

---

## Notes for bundling

The bundler assembles this event in this order:
1. `context/charter.md`
2. `events/advisory-meeting/event.md` ← this file
3. `events/advisory-meeting/preferences.md` ← user preferences (separate, portable)
4. Role files (in config order)
5. `events/advisory-meeting/session-prompt.md`

`preferences.md` is the correct location for all user-specific context.
This file (`event.md`) must remain generic and reusable across principals.

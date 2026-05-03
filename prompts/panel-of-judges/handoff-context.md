We refactored the old reusable meetings kit toward a broader **panel-of-judges** model.

Core decision:

- "Panel of judges" is now the top-level reusable collection.
- Meetings are only one event type inside that collection.
- The collection is for any case where 2+ roles/agents/models help generate ideas, evaluate outputs, compare options, refine proposals, surface tradeoffs, or select a direction.

Why we changed it:

- The old framing treated the advisor panel too narrowly as a meeting-only mechanism.
- We broadened it into a reusable multi-role interaction framework.
- This makes the system portable to brainstorming, planning review, protocol review, evaluation, adjudication, and stuck-resolution.

Architecture decisions:

- Events define interaction types.
- Roles define reusable participants.
- Shared charter text defines collection-wide principles.
- Authority belongs to the active event, not to the collection as a whole.
- Roles own objections in substance.
- Events own objections in procedure.
- Objection labels express resolution bar, not personality.

Key wording:

- The point of the panel is structured complementarity.
- The point is not rhetorical competition.
- The point is better generation, critique, comparison, and decisions.

Collection shape we drafted:

- README.md becomes a broad collection overview for panel-of-judges.
- A shared charter explains events, roles, objections, authority, and recording.
- Roles remain reusable across multiple event types.
- Event templates hold flow, authority, objection procedure, specialist triggers, and recording expectations.
- Meetings remain one concrete event type, not the definition of the whole system.

Role changes:

- Chair remains final decision-maker when the active event says so.
- Facilitator manages flow rather than owning final authority.
- Note-Taker records durable, resumable, machine-friendly minutes.
- Deep Researcher becomes an explicit specialist for evidence, precedent, missing facts, uncertainty, and external context.
- Negotiator becomes an explicit specialist for stalled or circular disagreement.
- People Expert becomes an explicit specialist for keeping disagreement constructive and interpretable.
- Pragmatist, Minimalist, and Systems Thinker stay as core judges with portable viewpoints.

Important procedural move:

- Meeting-specific rules should move out of shared panel/role files and into event definitions.
- Example: "each advisor gets one substantive question per round" is event procedure, not enduring role identity.

Files and draft artifacts created or rewritten conceptually:

- New broad README for Panel of Judges.
- New/rewritten charter language.
- New role template.
- New event template.
- Expanded judge roster with Pragmatist, Minimalist, Systems Thinker, People Expert, Negotiator.
- Deep Researcher rewritten in the broader panel model.
- Prompt project structure notes kept aligned with source/generated/data separation.

Current quality bar:

- Keep files self-describing.
- Keep the system simple and portable.
- Avoid turning roles into mini-constitutions.
- Avoid turning events into giant policy manuals.
- Start with rough drafts that are usable now and refactor later after real use.

Immediate next steps:

1. Finish moving from "meetings kit" wording to "panel-of-judges collection" wording where appropriate.
1. Update the charter to express the broader model directly.
1. Move meeting-only protocol rules from shared roles/advisors text into event files.
1. Land role and event templates.
1. Expand role files incrementally with objection-bar labels where useful.
1. Add or refine event definitions for advisory meeting, brainstorming, planning review, protocol review, evaluation, and stuck-resolution.
1. Review naming and placement against the broader prompt project structure draft.

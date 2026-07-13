<!--
skill:
  name: analysis
  collection: panel-of-judges
  version: 1.0
  type: skill
  usable_by: [all]
  triggers: [on_request, feedback_phase, meta_review]
  description: >
    Reusable analysis skill for synthesizing meeting chat, minutes, handoff
    candidates, and related artifacts into structured findings for
    self-reflection, process review, and factory follow-up.
-->

# Skill: Analysis

<!-- REVIEW: New skill. This is the artifact-aware reflection layer that can look at chat and minutes together, summarize what happened, identify friction and reusable patterns, and support Trainer, Recruiter, Facilitator, or other roles during self-analysis. -->

## What this skill does

The Analysis skill examines one or more meeting artifacts and turns them into structured findings.
It is designed for self-reflection, process review, role evaluation, and factory-aware follow-up.

Typical inputs include:
- current chat context;
- meeting minutes;
- process takeaways;
- factory handoff candidates;
- prior review notes or backlog items.

## Invocation

Any role may invoke this skill in Markdown:

> `[ANALYSIS — <Role Name>]` scope: <chat | minutes | handoffs | combined>, goal: <one-sentence analysis question>

Examples:

> `[ANALYSIS — Trainer]` scope: combined, goal: identify reusable role-definition issues from this meeting.
> `[ANALYSIS — Facilitator]` scope: chat, goal: summarize where discussion looped or lost clarity.
> `[ANALYSIS — Recruiter]` scope: combined, goal: determine whether repeated role gaps justify a new specialist.
> `[ANALYSIS — Note-Taker]` scope: minutes, goal: extract the strongest process takeaways and handoff-ready observations.

## Execution

### Step 1 — State the scope and materials

Name what is being analyzed.
Examples:
- current chat only;
- current minutes only;
- chat + minutes;
- minutes + existing handoff candidates;
- cross-meeting backlog and role-review notes.

### Step 2 — Extract the key structure

Summarize the core structure of what happened:
- goal or agenda;
- active roles;
- main decisions, deferrals, and open questions;
- moments of friction, ambiguity, duplication, or overload;
- any process takeaways already recorded.

### Step 3 — Classify findings

For each meaningful observation, classify it as one of:

- `instance-only` — local to this meeting; not worth structural change
- `role-related` — likely points to a role definition, scope, or activation issue
- `event-related` — likely points to meeting flow, timing, or event design
- `skill-related` — likely points to reusable task behavior that should be extracted or improved
- `factory-related` — likely points to the generation/update workflow itself
- `unknown` — interesting but not yet clear enough to classify

### Step 4 — Rate confidence and reuse value

For each finding, add:
- **Confidence:** high | medium | low
- **Reuse value:** high | medium | low
- **Recommended next step:** note only | monitor | handoff candidate | role-review | single update | batch update

### Step 5 — Return structured findings

Return findings in Markdown using a format like:

```md
## Analysis Findings

- Finding: <plain-language observation>
  Type: <classification>
  Confidence: <high|medium|low>
  Reuse value: <high|medium|low>
  Evidence:
    - <specific supporting point>
    - <specific supporting point>
  Recommended next step: <option>
```

If appropriate, also include:
- a short summary of key takeaways;
- a shortlist of candidate factory handoffs;
- or a note that no structural follow-up is currently warranted.

## What this skill does NOT do

- It does not make final governance decisions.
- It does not replace research when external evidence is missing.
- It does not automatically turn every finding into a handoff candidate.
- It does not apply changes to artifacts directly.

## Notes

- This skill works especially well with `interview`, `self-improve`, and Note-Taker minutes.
- It is intentionally Markdown-first so its outputs can be pasted into minutes, review notes, or factory sessions with minimal transformation.
- When confidence is low, the skill should say so explicitly rather than overstating certainty.

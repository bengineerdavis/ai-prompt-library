
<!--
skill:
  name: interview
  collection: panel-of-judges
  version: 1.0
  type: skill
  usable_by: [all]
  triggers: [on_request, feedback_phase]
  description: >
    Reusable interviewing pattern any role can use to gather structured
    feedback or clarifying input from other roles or the principal, especially
    during closing feedback phases and self-analysis.
-->

# Skill: Interview

<!-- REVIEW: New skill optimized for process feedback and self-reflection. It stays generic enough to use across events, but includes a specific pattern for end-of-meeting feedback and meta-sessions. -->

## What this skill does

The Interview skill provides a lightweight, reusable way to ask structured questions of other roles or the principal.
It is especially useful for closing feedback phases, role self-reflection, and gathering inputs for factory handoff candidates.

## Invocation

Any role may invoke this skill using Markdown:

> `[INTERVIEW — <Interviewer Role>]` target: <Role or "panel">, topic: <process | role | decision | factory>, goal: <one-sentence aim>

Examples:

> `[INTERVIEW — Facilitator]` target: panel, topic: process, goal: gather one improvement for next meeting.
> `[INTERVIEW — Recruiter]` target: advisors, topic: role, goal: understand where coverage felt thin or overloaded.
> `[INTERVIEW — Trainer]` target: Chair, topic: factory, goal: clarify which structural findings should become handoff candidates.

## Execution

### Step 1 — Frame the interview

State in one or two sentences what you are asking about and why.
Keep scope narrow: one topic per invocation.

### Step 2 — Ask 2–3 focused questions

Pick from a small library of reusable prompts, tailored to the topic.

**Process-focused prompts (feedback phase):**

- What helped you do your role well in this session?
- Where did you feel stuck, unsure, or overloaded?
- What one change would make the next similar meeting more effective?

**Role-focused prompts (Recruiter / Trainer):**

- Did your responsibilities feel clear throughout the session?
- Were there situations where you wished for another role or specialist?
- Is any part of your current definition misleading or too broad?

**Decision-focused prompts (Chair / advisors):**

- Did you feel the decision was well-supported enough to move forward?
- What tradeoffs still feel under-explored?
- Is there a follow-up you want to see before committing fully?

**Factory-focused prompts (meta-roles):**

- Which observations from this meeting deserve a factory handoff candidate?
- Are there event or template changes that would have prevented friction?
- Should this issue be handled as a single-artifact update or a batch review?

### Step 3 — Capture concise answers

Ask each target to respond briefly.
The Note-Taker or interviewer should summarize answers in Markdown, grouping by topic.

### Step 4 — Convert into artifacts

Use the interview outputs to:

- populate the `Process Takeaways` section in minutes;
- identify and draft factory handoff candidates when patterns emerge;
- inform Trainer or factory sessions about where roles, events, or skills may need refinement.

## What this skill does NOT do

- It does not make decisions or apply structural changes on its own.
- It does not replace the Chair, Facilitator, Recruiter, or Trainer; it supports their work.
- It does not turn every observation into a handoff; it helps distinguish between local and reusable patterns.

## Notes

- The Interview skill is portable across events: advisory meetings, brainstorming, planning review, protocol review, evaluation, and meta-events.
- It is most powerful when used sparingly and with clear goals, especially at the end of a meeting.
- Markdown is the default format for interview prompts and summaries.

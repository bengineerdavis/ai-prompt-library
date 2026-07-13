<!--
skill:
  name: deep-research
  collection: panel-of-judges
  version: 1.0
  type: skill
  usable_by: [all]
  triggers: [on_request, on_specialist_trigger]
  description: >
    Reusable deep research protocol any role can invoke when external facts,
    precedents, comparisons, or evidence are needed to proceed.
    Structured to avoid fabrication, surface uncertainty, and return citable findings.
-->

# Skill: Deep Research

## What this skill does

When a role needs external information — facts, precedents, alternatives, data,
regulatory context, or market evidence — it invokes this skill rather than
stating information from memory without verification.

This skill enforces a discipline: **claim nothing you cannot source, and flag
everything you are uncertain about.**

---

## Invocation

Any role may invoke this skill:

> `[DEEP-RESEARCH — <Role Name>]` <question or information gap in one sentence>

Examples:
> `[DEEP-RESEARCH — Tax Strategist]` What are the 2026 HSA contribution limits and catch-up rules?
> `[DEEP-RESEARCH — AI/Tech Advisor]` What is the historical drawdown range for AI/tech-heavy ETFs during the 2022 correction?
> `[DEEP-RESEARCH — Wealth Planner]` What do Boglehead-aligned planners recommend for non-US allocation percentage in a 70-retirement portfolio?

The event's **Specialist Trigger** for Deep Researcher may also activate this skill
automatically when a key fact is missing and no researcher role is active.

---

## Execution

### Step 1 — State the question precisely

Restate the research question in one sentence with:
- The specific fact, range, or comparison needed
- The time horizon or recency requirement (if relevant)
- The decision it will inform

### Step 2 — Attempt to answer

Try to answer from available context (pasted files, session history, prior findings).

For each claim, tag it:
- `[verified]` — found in a pasted source file or confirmed by the principal
- `[confident]` — well-established, low risk of being wrong
- `[uncertain]` — based on general knowledge, may be stale or context-dependent
- `[unknown]` — cannot answer without external lookup; flag for follow-up

### Step 3 — Surface gaps

List any `[unknown]` items explicitly:

> **Research gap:** <question> — needs external verification before this decision should proceed.

The principal decides whether to pause and verify, proceed with `[uncertain]` tags, or defer.

### Step 4 — Return findings

Structure findings as:

> **Finding:** <claim> `[verified|confident|uncertain|unknown]`
> **Source:** <file name, session reference, or "general knowledge — verify">
> **Relevance:** <one sentence on how this informs the current decision>

---

## What this skill does NOT do

- Does not fabricate sources or statistics.
- Does not assert `[verified]` for information not found in a pasted file or confirmed by the principal.
- Does not replace a human research step for high-stakes decisions — it surfaces what is known and flags what is not.

---

## Notes

- When the **Deep Researcher** specialist role is active in the session, they own this
  skill's execution. Other roles defer their research invocations to the Deep Researcher.
- When no Deep Researcher is active, any role may invoke this skill directly.
- Skills are inlined by the bundler when the role declares `skills: [deep-research]`
  in its front-matter.

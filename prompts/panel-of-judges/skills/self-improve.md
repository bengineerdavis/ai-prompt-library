<!--
skill:
  name: self-improve
  collection: panel-of-judges
  version: 1.0
  type: skill
  usable_by: [all]
  triggers: [on_request, post_output, on_flag]
  description: >
    Reusable self-critique and improvement loop any role can invoke.
    Evaluates the role's own output or definition against its template,
    produces a scored audit, and optionally generates a revised version.
-->

# Skill: Self-Improve

## What this skill does

When invoked, this skill runs a structured self-critique loop on:
- A role's **output from the current session** (did I do my job well?), or
- The role's **own definition file** (is my role well-designed?).

It produces a scored audit and, if the score falls below threshold, generates
a concrete improvement proposal the principal or trainer can accept, reject, or modify.

---

## Invocation

Any role may invoke this skill at any time using:

> `[SELF-IMPROVE — <Role Name>]` <target: output | definition> <optional: reason>

Examples:
> `[SELF-IMPROVE — Tax Strategist]` output — my contribution to agenda item 3 felt incomplete.
> `[SELF-IMPROVE — Pragmatist]` definition — I'm not sure my "Does not do" section is specific enough.

The Chair or Trainer may also invoke this skill on behalf of a role:
> `[SELF-IMPROVE — Pragmatist requested by Trainer]` definition

---

## Execution

### Step 1 — Identify the target

State clearly what is being evaluated:
- For **output**: quote or summarize the specific contribution being reviewed.
- For **definition**: reference the role file by name and version.

### Step 2 — Score against criteria

Score the target 1–10 on each criterion. Use severity labels to weight findings.

**For output:**

| Criterion | Weight | Score /10 | Notes |
|---|---|---|---|
| Role fidelity | 30% | | Did the output stay within the role's purpose and boundaries? |
| Completeness | 25% | | Were all expected contributions made? |
| Clarity | 25% | | Is the output actionable and unambiguous? |
| Epistemic honesty | 20% | | Were uncertainty, caveats, and tradeoffs surfaced? |

**For definition:**

| Criterion | Weight | Score /10 | Notes |
|---|---|---|---|
| Template conformance | 30% | | All required sections present and correctly structured? |
| Portability | 25% | | No engagement-specific content baked in? |
| Negative-space clarity | 25% | | Are the "Does not do" boundaries specific and enforceable? |
| Internal consistency | 20% | | Does the role's stance align with its responsibilities and limits? |

**Minimum passing score: 7.5 weighted average.**

### Step 3 — Produce findings

For each criterion scoring below 8:
- Name the gap in one sentence.
- Label it `[light]`, `[moderate]`, `[serious]`, or `[red-line]`.
- Propose a specific fix (not just a direction).

### Step 4 — Decide

Present the principal (or Trainer, if active) with:

> **Score: X.X / 10**
> **Gaps found: N**
>
> Options:
> - `[A]` Accept as-is (score is passing; gaps are noted only)
> - `[B]` Apply proposed fixes now and return revised version
> - `[C]` Defer to a future session (log as open improvement item)

Do not apply changes without explicit `[B]` confirmation.

---

## Output

If `[B]` is chosen:
- Return the revised output or definition with changes marked using `→` inline.
- Return a changelog entry: what changed, why, and the version bump.
- If the target is a definition file, flag whether the change requires a registry update.

---

## Notes

- This skill does not replace the Trainer role. The Trainer applies this skill across
  multiple roles in a structured review session; this skill is for ad hoc self-correction.
- This skill may be invoked silently (the role improves without announcing it) only for
  [light] gaps. For [moderate] or higher, the invocation must be visible to the panel.
- Skills are inlined by the bundler — this file's content is merged into the role file
  at bundle time when the role declares `skills: [self-improve]` in its front-matter.

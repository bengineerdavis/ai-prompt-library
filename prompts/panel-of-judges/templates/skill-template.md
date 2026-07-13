<!--
skill:
  name: <skill-slug>
  collection: panel-of-judges
  version: 1.0
  type: skill
  usable_by: [all | list of role slugs]
  triggers: [on_request | on_specialist_trigger | post_output | on_flag]
  description: >
    One sentence describing what this skill does and when to use it.
-->

# Skill: <Skill Name>

## What this skill does

Describe the capability this skill provides.
Focus on the problem it solves, not the mechanism.
One short paragraph.

---

## Invocation

How a role invokes this skill:

> `[SKILL-NAME — <Role Name>]` <context or trigger in one sentence>

Who else can invoke it (Chair, Trainer, event trigger):

> `[SKILL-NAME — <Role> requested by <invoker>]` <reason>

---

## Execution

### Step 1 — <Step name>

What the role does in this step.

### Step 2 — <Step name>

What the role does in this step.

### Step N — Return findings

How the skill returns its output.
What format, what labels, what the principal or panel receives.

---

## What this skill does NOT do

- Hard limits on scope.
- What the skill defers to other roles or human judgment.
- What it will not fabricate or assert.

---

## Notes

- When this skill conflicts with another active role's responsibilities, <resolution rule>.
- Skills are inlined by the bundler when a role declares `skills: [<skill-slug>]` in its front-matter.
- This skill is portable across any collection that uses compatible role and event structures.

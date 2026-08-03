---
name: interaction-questioning
description: Clarifies unclear requests by asking one question at a time. Use when requirements, constraints, preferences, or output shape are unclear. Uses adaptive-auto routing to decide when deeper branching will help.
license: MIT
metadata:
  version: "2.2.3"
  latest: true
  mode-default: "adaptive-auto"
  supports:
    - adaptive-auto
    - direct
    - divergent
***

# Interaction Questioning

Ask only the minimum number of questions needed to reach a clear, actionable result.

## Purpose

Use this skill to help the user:
- clarify what they want
- resolve uncertainty or conflicting preferences
- define a session goal clearly enough to act on
- improve the final quality of the answer, artifact, or plan

This skill is not just for filling missing fields.
It also helps the user discover the right question, not only the first question they happened to ask.
Treat exploratory sessions as valid.
When the user is still forming the goal, help them define a clear session goal before optimizing the final output.

## When to Use

Use this skill when:
- the request is ambiguous, missing details, or internally inconsistent;
- the result depends on unknown constraints, audience, vendor target, or output shape;
- the user appears exploratory and does not yet have a settled goal;
- another skill needs better inputs before it can do good work;
- there are multiple plausible solution paths.

Do not use this skill when:
- the request is already clear enough to answer well;
- a safe default is obvious and low-risk;
- the user explicitly wants a quick default answer;
- asking more would add more friction than value.

## Composition

This is a support skill.
It works with research, writing, coding, planning, review, and other task skills.
Use it to improve the request and session goal, then return control to the active task skill.

## Core Rules

- Ask one question at a time.
- Wait for the answer before asking the next.
- Prefer the question most likely to improve the result.
- Stop as soon as the goal and next step are actionable.
- Default silently when the missing detail is low-risk.
- If more than 7 questions seem necessary, explain why and ask permission to continue.
- If the session goal is unclear, ask questions that help the user define it before narrowing implementation details.

## Default Policy

Use adaptive-auto by default.

In adaptive-auto:
- start with direct questioning when one missing detail is most likely to improve the result;
- switch to an internal tree when multiple paths, constraints, or goal interpretations could change the answer;
- switch back to direct questioning once one path is clearly best and only one or two important unknowns remain.

Never expose the internal tree unless verbose or deep-trace mode is requested.
Always ask only one user-facing question at a time.

## Direct mode

Use direct questioning when:
- one missing answer would clearly improve the result;
- the session goal is already clear;
- the user wants speed more than exploration;
- deeper branching is unlikely to change the answer materially.

## Adaptive tree use

Use the internal tree when:
- the user is exploratory and the real session goal is still forming;
- multiple plausible downstream artifact shapes or implementation paths exist;
- high-stakes ambiguity could change what good looks like;
- another skill depends on choosing the right frame before execution begins.

The tree should help the user move from an initial answer to the answer they actually need.
Treat this as guided clarification, not interrogation.
Use it to help the user reach a clear decision when they are uncertain or only partly informed.

## Tree structure

When tree mode is active, maintain an internal three-level question tree:
- primary: goal-shaping or path-selection questions;
- secondary: branch-refining questions;
- tertiary: questions that unblock the active path.

Track internally:
- active_branch
- candidate_frontier
- pruned_nodes
- replaced_nodes
- unresolved_risks
- inferred_defaults
- reideation_reason

Prune branches that are low-value or already implied after each answer.
Replace a branch when a narrower, higher-value question becomes available.

## Session-goal lens

Watch for a difference between:
- the question the user asked first;
- the goal the user actually wants to reach;
- the decision or output they need in order to move forward.

If these differ, ask questions that help the user state a clear session goal in plain language.
Do this without adding a separate mode.
Treat it as part of good questioning.

## Goal-deduction confirmation

When the session goal is not fully clear, infer the likely goal from the answers so far.
Then decide whether to proceed, confirm it, or offer a few candidates.

Default behavior:
- if confidence is high and the risk of being wrong is low, proceed without an explicit goal check;
- if confidence is high enough to form a clear hypothesis but drift is still a real risk, state the inferred goal in plain language and ask for yes or no confirmation;
- if confidence is medium or low and there are a few strong candidate goals, present 2 to 4 options and ask which is closest.

Use a single inferred goal first.
Escalate to multiple-choice goal options only when the signal is mixed or disagreement is likely.

### Confidence guide

Treat confidence as a practical judgment based on how consistent and useful the evidence is so far.

- High confidence: one goal best fits the user's ask, answers, and constraints.
- Medium confidence: one goal is leading, but one or two alternatives could still change the best next step.
- Low confidence: multiple goals still fit, or the user's answers point in different directions.

### Confirmation templates

Use plain language and active voice.
Examples:
- "It sounds like your goal is to ____. Is that right?"
- "I think you want to ____ so you can ____. Is that right?"
- "Based on what you've said, I see three likely goals: A, B, or C. Which is closest?"
- "I think the goal is X, but it could also be Y. Which one is the better fit?"

### Correction triggers

Treat these as signals to refine or reopen goal inference without restarting the whole flow:
- direct rejection: "no", "not quite", "that's not it";
- partial correction: "close, but", "more specifically", "partly";
- redirection: "actually, I need", "the real issue is", "what I'm really trying to do is";
- frustration: "this is not helping", "that's not what I asked".

When correction appears:
- keep what is still useful from prior answers;
- update the inferred goal;
- ask the smallest next question needed to recover alignment.

## Pruning Policy

### Primary
Keep only branches that could change the session goal, architecture, output format, vendor target, or decision criteria.
Prune if the answer makes the branch irrelevant.
Replace if a narrower, more decisive branch appears.

### Secondary
Keep only branches that could change the next 1 to 3 questions or materially improve the result.
Prune if implied by prior answers.
Replace if a more specific clarifier removes more uncertainty.

### Tertiary
Keep only branches needed to unblock execution on the active path.
Prune if low-risk, duplicate, or safe to default.
Replace if a newly revealed dependency is more important.

## Re-ideation Triggers

Rethink the question plan only when:
- the best next question is no longer clear;
- a new answer invalidates branch ordering;
- the emerging session goal differs from the starting request;
- the active task skill changes what matters;
- a policy conflict appears across current, session, or persistent instructions.

## Output Style

Normal mode:
- ask only the next question;
- keep confidence and internal reasoning hidden unless another rule already calls for a brief explanation.

Verbose mode:
- show confidence only when the skill is making a goal inference, confirmation choice, or branch-selection decision that could materially change the path;
- when shown, include the confidence level as high, medium, or low;
- when shown, include one short sentence explaining why;
- include a one-line reason for why this question is next only when it would help the user stay aligned.

Deep-trace mode:
- include the current branch label;
- include prune or replace notes and the remaining high-value unknowns;
- include the reasoning steps between questions;
- include confidence shifts, goal-inference updates, and correction recovery steps.

## Vendors

### Portable chat paste
Artifact: plain markdown prompt block.
Install:
1. Paste this skill into the system prompt or conversation setup.
2. If supported, save it as a reusable custom instruction.
Keywords:
- ask one question at a time
- clarify the session goal
- adaptive questioning
- deep trace

### ChatGPT
Artifact: Custom Instructions text.
Install:
1. Open Settings and Personalization.
2. Enable Custom Instructions.
3. Paste the Core Rules, Default Policy, and Session-goal lens sections.
4. Save and test with a realistic prompt.
Keywords:
- quick mode
- goal clarification
- deep trace

### Claude-style skills
Artifact: skill folder with SKILL.md and optional references.
Install:
1. Create a folder named interaction-questioning.
2. Save this file as SKILL.md.
3. Add references later only if needed.
Keywords:
- clarifying questions
- one question at a time
- adaptive-auto routing
---
name: research
description: Researches open-ended questions, options, prior art, trade-offs, and current information, then synthesizes findings into a clear answer or report. Use when the user asks to search, research, compare, investigate the landscape, or understand how something works. Works with or without a native skills runtime and composes with the questioning skill when clarification is needed.
---

# Research

## Purpose

This skill defines **how to search, validate, and synthesize information**.
It focuses on turning a question into a researched answer, not on defining how clarifying questions are asked.
If clarification is needed, it should delegate that behavior to the questioning skill when available.

## When to Use

Use this skill when the user asks to:

- Research a topic.
- Search for options, tools, vendors, examples, or prior art.
- Compare alternatives.
- Understand how something works.
- Gather evidence before choosing a direction.
- Produce a structured answer, report, shortlist, or recommendation.

## When Not to Use

Do not use this skill when:

- The user wants code implementation more than research.
- The user wants a pure writing/editing pass with no factual investigation.
- The task is a bug diagnosis, root-cause analysis, or incident triage.
- The request is already fully answered by existing context and no research is needed.

## Scope Gate

Before researching, classify the request:

- **Narrow**: a focused factual or explanatory question.
- **Comparative**: two or more options, vendors, tools, or approaches must be compared.
- **Broad**: many options, open scope, or multiple dimensions must be explored.

Let this set the research depth and the number of clarification questions needed.
Do not run a broad process on a narrow question unless the user explicitly asks for depth.

## Interaction Preference Check

Before asking clarifying questions:

- Check whether a questioning skill, interaction policy, or equivalent user preference is already active in context.
- If such a preference exists, use it for how questions are asked.

If clarification is needed and no questioning preference is active:

- Ask once whether the user has any interaction preferences for how questions should be asked.
- If the user provides preferences, apply them for the remainder of the task.
- If the user declines or says they have none, continue using this skill's default clarification behavior.
- Do not repeatedly re-ask about interaction preferences during the same task.

## Default Clarification Behavior

If clarification is needed and no external questioning skill is available:

- Ask only what is required to improve the answer materially.
- Prefer goal, scope, constraints, and output format over low-value preferences.
- Ask one question at a time.
- Use compact labeled options when helpful.
- Stop as soon as enough is known.

## Research Process

### Phase 1: Clarify

- Resolve ambiguity first.
- Confirm the practical goal when it affects the shape of the research.
- Avoid unnecessary questions.

### Phase 2: Diverge

- Search broadly before judging.
- Look across multiple independent sources, angles, and source types.
- Do not settle for the first plausible result.

### Phase 3: Validate

- Prefer primary or authoritative sources when possible.
- Cross-check meaningful claims.
- Distinguish clearly between corroborated facts, single-source claims, and reasoned inference.

### Phase 4: Converge

- Rank or cluster findings against the user's goal.
- Recommend an option when the evidence supports it.
- If the evidence is insufficient, say so directly instead of forcing certainty.

### Phase 5: Deliver

- Narrow: direct answer with concise context.
- Comparative: structured comparison, usually with a table.
- Broad: fuller structured synthesis or report.
- Lead with the answer, then support it.

## Evidence Labels

When practical, label non-trivial claims as one of:

- `verified` — supported by multiple credible sources or authoritative evidence.
- `single-source` — found but not independently confirmed.
- `reasoned` — inference or synthesis, not directly established by a source.

Do not present a `reasoned` claim with the confidence of a `verified` one.

## Composition

This skill composes with:

- **questioning** for clarification behavior.
- Writing/report skills for final packaging.
- Coding or planning skills after the research phase is complete.

This skill owns the research workflow.
It does not own user-interaction style unless no separate questioning policy exists.

## Progressive Disclosure Model

Use a three-tier model where the runtime supports it:

- **Tier 1:** short name/description or summary available at all times so the system knows this skill exists.
- **Tier 2:** full skill body loaded only when the task matches.
- **Tier 3:** optional reference files, vendor artifacts, or templates loaded only when needed.

If the runtime does not support native skills, simulate this by keeping a short always-on summary in the base prompt and loading the longer body only in your orchestrator or manually when needed.

## Portable Fallback

If this skill is pasted directly into a chat:

- Treat this markdown as the active research policy.
- If clarification is required, run the Interaction Preference Check above.
- If the user has no preferences, use the default clarification behavior.
- Continue with the research process and match answer depth to scope.

## Vendors

The portable core is canonical.
Vendor artifacts are derived outputs used to install or operationalize this skill in specific tools.

### Portable Chat

Use when: any AI chat with no native skill loader.
Artifact: plain markdown or condensed system-prompt block.
Install:

1. Paste the condensed research artifact into the system prompt or top of a new chat.
1. Optionally pair it with the questioning artifact.
1. For best results, keep only the short trigger summary always present and paste the full body only when needed.

### ChatGPT

Use when: ChatGPT with persistent customization.
Artifact: condensed Custom Instructions or reusable project prompt.
Install:

1. Open Settings > Personalization > Custom Instructions.
1. Paste a condensed version of this skill.
1. Optionally add a note to consult the questioning skill first when clarification is needed.
1. Save and test.

### Claude Code / Agent Skills

Use when: a native skill runtime supports automatic discovery.
Artifact: skill folder with `SKILL.md` plus optional references.
Install:

1. Create a `research` folder.
1. Put this file into `SKILL.md`.
1. Add reference files for templates, vendor snippets, or report formats.
1. Keep the `description` specific about what the skill does and when to use it.

### OpenRouter / API Orchestrator

Use when: you control assembly across models and providers.
Artifact: base summary + lazily injected full skill body + optional vendor/reference fragments.
Install:

1. Store this file as canonical source markdown.
1. Extract Tier 1 summary into the always-on system prompt.
1. Inject Tier 2 full body only when the task is research-shaped.
1. Inject Tier 3 references only if required by the selected model, vendor, or output format.
1. Pair with the questioning skill so clarification style remains consistent across providers.
   Notes:

- Progressive disclosure works here as an orchestration pattern, even if the underlying provider has no native skills feature.

# Onboarding

This document explains the first-run experience for Impromptu.

For the main controls users may configure, see [Modes and settings](./modes-and-settings.md).

## Goal

The first-run experience should be short, helpful, and low-friction.

The system should infer as much as possible first, then ask only a small number of questions where confidence is low or important preferences are missing.

## Default onboarding principles

- Prefer a short setup over a long interview.
- Ask at most 5 default questions.
- Use conservative defaults.
- Explain the controls in plain language.
- Offer a helper role to assist with later changes.

## Recommended defaults

Start new users with:

- `cost = auto`
- `complexity = auto`
- `verbosity = info`

These defaults should work well for most newcomers.

## First-run explanation

A short explanation might say:

> Impromptu can automatically adapt how much work it does, how conservative or adventurous its strategy is, and how much process detail you see. By default, it stays conservative and cost-conscious, and it will only ask a few setup questions when needed.

## Suggested 5 onboarding questions

Ask only if not already inferred with good confidence.

1. Do you usually want the cheapest workable result, a balanced default, or the strongest result?
2. Should I usually keep the strategy simple, or explore more when helpful?
3. How much process do you want to see: quiet, info, or debug?
4. Should I save recurring preferences when I detect stable patterns?
5. Are there any standing rules or constraints I should always respect?

## Helper role

A helper assistant should be available by default in chat.

Its job is to:

- explain the settings
- recommend likely defaults
- help users decide when to change cost or complexity
- update saved preferences when confirmed

## Re-checks

The system should avoid repeatedly asking the same questions.

Instead, it should re-check preferences only when:

- a preference is new
- a preference appears stale
- recent behavior suggests that a saved default may no longer fit

For more, see [User preferences and memory](./user-preferences-and-memory.md).
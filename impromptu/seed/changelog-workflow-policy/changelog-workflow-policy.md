# Changelog Workflow Policy

## Purpose

Standardize changelog handling across Seed prompt work, factory work, impromptu work, and direct-use library prompts.

## Rules

### 1. Always ask before changelog updates are omitted

Whenever a Seed prompt, factory prompt, direct-use prompt, or related library file is created, modified, renamed, moved, or deleted, the workflow must ask whether the relevant changelog should also be updated.

Default expectation: **yes, update the changelog**.

### 2. Impromptu changelog is required for prompt/factory changes

If work affects files under `prompts/impromptu/`, the workflow should look for:

- `prompts/impromptu/CHANGELOG.md`
- or the nearest nested `CHANGELOG.md` that governs the modified subtree

If found, update it.
If not found, ask the user to provide it or confirm creation of a new one.

### 3. Library changelog is required for direct-use prompts

If work creates or changes a prompt intended for direct use in the user's general library, the workflow should also update the library-level changelog.

Expected source order:

1. Existing library `CHANGELOG.md` found by bootstrap/script context
1. Attached `CHANGELOG.md` supplied by the user
1. Ask the user to provide one or approve creating one

### 4. Bootstrap should provide changelog context when available

Bootstrap context loading should include the repo root `CHANGELOG.md` by default when available.
If nested prompt/factory changelogs are later added to bootstrap, they should also be injected when relevant to the selected prompt/factory scope.

### 5. Required trigger events

Ask about changelog updates for all of the following:

- New factory prompt creation
- Existing factory prompt modification
- Factory prompt rename
- Factory prompt deletion
- New Seed prompt creation
- Existing Seed prompt modification
- Seed prompt rename or move
- Direct-use prompt creation or modification
- Library structure/documentation changes that alter usage, scope, or expected workflow

### 6. Minimum changelog entry content

A changelog update should include:

- Date/session label
- Scope (`seed/`, `factories/`, `impromptu/`, direct-use library, etc.)
- Added / Changed / Deleted as appropriate
- A brief explanation of workflow impact when behavior changes

### 7. Factory-builder / prompt-builder workflow requirement

Any factory or prompt generation workflow should include a final review step:

1. Identify changed files
1. Identify the governing changelog(s)
1. Ask the user whether to update them if not already requested
1. Draft the changelog entry
1. Return changed files together

## Standard prompt to ask

Use this question whenever triggered:

> This change affects prompt/library behavior. Do you want me to update the relevant `CHANGELOG.md` file(s) too? If you already have one, attach it or point me to it; otherwise I can draft one.

## Notes

- README files are not a substitute for changelog history.
- If the user declines changelog updates, proceed but note that the history was intentionally left unchanged.
- For direct-use prompt work, both the prompt artifact and the library changelog should be treated as deliverables when the user approves the update.

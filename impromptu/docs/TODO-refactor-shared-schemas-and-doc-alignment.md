# WIP Refactor Plan: Shared Schemas and Doc Alignment

Branch: `refactor/shared-schemas-and-doc-alignment`
Status: WIP temporary branch TODO
Lifecycle: Working document for this branch; may be edited heavily, replaced, or removed before or after merge

## Goal

Stabilize the prompt-library contract in documentation first, then align shared schemas, drift detection, validation, and tests to that contract.

## Why this is WIP

This file is not intended to be a permanent product or architecture document.

It exists to:
- keep the branch scoped
- break the work into reviewable commits
- track remaining implementation tasks
- make it easy to delete or rewrite the plan once the branch work is complete

## Scope

This branch covers:

- canonical design documentation
- shared schema updates
- prompt discovery alignment
- drift detection completion
- validation rules
- tests and fixtures
- changelog follow-through

This branch does not cover:

- repo migration to the official Impromptu app repository
- include-file prompt composition
- higher-order prompt inheritance or assembly

## Commit-by-commit plan

### 1. Canonical model doc
Commit:

- `docs(impromptu): add canonical prompt library model`

Deliverables:

- `docs/impromptu-library-model.md`

Status:

- [x] Done

### 2. Branch execution doc
Commit:

- `docs(refactor): add WIP shared schemas and drift-detection plan`

Deliverables:

- `docs/refactor-shared-schemas-and-doc-alignment.md`

Status:

- [x] Done

### 3. Docs entrypoint links
Commit:

- `docs(readme): link prompt library model and refactor plan`

Deliverables:

- minimal updates to root README and docs hub references

Status:

- [ ] Todo

### 4. Shared schema alignment
Commit:

- `feat(schema): align manifest schema with namespace-based prompt discovery`

Deliverables:

- schema fields for collection path, prompt extensions, and filename policy
- examples aligned with the canonical model

Status:

- [ ] Todo

### 5. Discovery alignment
Commit:

- `feat(discovery): enforce one-prompt-per-directory namespace convention`

Deliverables:

- namespace-based prompt discovery
- canonical filename enforcement

Status:

- [ ] Todo

### 6. Drift detection completion
Commit:

- `feat(drift): detect schema and filesystem mismatches for prompt namespaces`

Deliverables:

- actionable reporting for drift cases
- warnings or failures aligned with documented rules

Status:

- [ ] Todo

### 7. Validation guardrails
Commit:

- `feat(validation): reject hidden, non-text, and non-file prompt candidates`

Deliverables:

- structural prompt candidate validation
- text-file checks separated from extension-only logic

Status:

- [ ] Todo

### 8. Tests and fixtures
Commit:

- `test(discovery): add valid and invalid namespace fixtures`

Deliverables:

- fixture trees for valid and invalid layouts
- tests for schema alignment and drift reporting

Status:

- [ ] Todo

### 9. Deferred work recorded
Commit:

- `docs(roadmap): defer include composition and repo migration`

Deliverables:

- roadmap notes for post-branch work

Status:

- [ ] Todo

### 10. Changelog follow-through
Commit:

- `chore(changelog): record shared schema and prompt discovery alignment changes`

Deliverables:

- updates to the governing changelog(s)

Status:

- [ ] Todo

## Working rules for this branch

- One conceptual change per commit.
- Docs before behavior.
- Schema before drift logic.
- Tests immediately after enforcement.
- Changelog follow-through before branch completion.

## Validation checklist

- [x] Canonical library model documented
- [x] Branch execution plan documented
- [ ] README or docs hub linked
- [ ] Shared schema updated
- [ ] Discovery aligned to schema
- [ ] Drift detection completed
- [ ] Validation guardrails added
- [ ] Fixtures and tests added
- [ ] Changelog updated
- [ ] Post-branch migration captured as follow-up

## Post-branch follow-up

After this branch lands, plan a separate migration phase to export or move the stabilized implementation into the official Impromptu app repository.

That later phase should clarify:

- source-of-truth ownership between repositories
- runtime code migration boundaries
- documentation ownership after migration
- bootstrap and tooling path updates
- release and changelog flow after export
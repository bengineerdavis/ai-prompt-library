# WIP Refactor Plan: Shared Schemas and Doc Alignment

Branch: `refactor/shared-schemas-and-doc-alignment`
Status: WIP temporary branch TODO
Lifecycle: Working document for this branch; may be edited heavily, replaced, or removed before or after merge

## Goal

Stabilize the canonical prompt-library contract in documentation first, then align shared schemas, discovery, drift detection, validation, and tests to that contract.

## Current canonical model

The branch now assumes the following v1 model:

- one library belongs to exactly one repository
- one library declares exactly one prompts root
- collections are explicit subdirectories under that prompts root
- collections must be unique, un-nested, and non-overlapping
- groups are future organizational units for searching multiple collections together
- namespace uniqueness is collection-scoped
- canonical prompt files follow the namespace-directory basename rule
- configured library instances are user-specific app config, not repo-local app code

## Config-location assumptions

This branch should remain compatible with future user-specific library config under a path like:

- `~/.config/impromptu/libraries/`

However, this branch does not implement multi-library runtime behavior. It only ensures the docs and schema do not block that future layout.

## Why this file is WIP

This file is a temporary execution tracker for the branch, not a permanent design artifact.

It exists to:

- keep the branch scoped
- track completed versus remaining work
- separate schema work from behavior changes
- make it easy to remove or rewrite the branch plan later

## Scope

This branch covers:

- canonical design documentation
- docs entrypoint updates
- shared schema updates
- prompt discovery alignment
- drift detection completion
- validation rules
- tests and fixtures
- changelog follow-through

This branch does not cover:

- repo migration to the official Impromptu app repository
- one library spanning multiple repositories
- multiple prompts roots inside one library
- nested or overlapping collections
- include-file prompt composition
- higher-order prompt inheritance or assembly
- collection parent-child ownership rules
- groups changing prompt ownership or discovery precedence
- multi-library management tooling
- multi-library runtime selection

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

- [x] Done

### 4. Canonical model refinement
Commit:

- `docs(impromptu): refine library model for repo-bound roots and disjoint collections`

Deliverables:

- update `docs/impromptu-library-model.md` to reflect:
  - one library to one repo
  - one explicit prompts root
  - disjoint collections only
  - future groups instead of nested collections
  - collection-scoped namespace uniqueness
  - future user-specific config location compatibility

Status:

- [x] Done

### 5. Shared schema alignment
Commit:

- `feat(schema): align manifest schema with repo-bound prompt library model`

Deliverables:

- schema file for a single library definition
- library-level metadata fields nested under `library`
- explicit repository assignment
- explicit `prompts_root`
- collection schema aligned to disjoint collection paths
- allowed prompt extensions
- canonical filename policy
- examples aligned with the canonical model

Status:

- [ ] Todo

### 6. Discovery alignment
Commit:

- `feat(discovery): enforce collection-scoped namespace discovery rules`

Deliverables:

- discovery rooted at the declared prompts root
- discovery limited to declared collections
- canonical filename enforcement
- collection overlap treated as invalid configuration, not resolved dynamically

Status:

- [ ] Todo

### 7. Drift detection completion
Commit:

- `feat(drift): detect schema and filesystem mismatches for prompt libraries`

Deliverables:

- actionable reporting for:
  - repo/root mismatch assumptions
  - undeclared collection paths
  - overlapping or invalid collection paths
  - namespace/file naming drift
- warnings or failures aligned with documented rules

Status:

- [ ] Todo

### 8. Validation guardrails
Commit:

- `feat(validation): reject hidden, non-text, and structurally invalid prompt candidates`

Deliverables:

- structural prompt candidate validation
- text-file checks separated from extension-only logic
- collection path validation
- prompts-root boundary validation

Status:

- [ ] Todo

### 9. Tests and fixtures
Commit:

- `test(discovery): add valid and invalid prompt library fixtures`

Deliverables:

- fixture trees for valid and invalid layouts
- tests for schema alignment
- tests for disjoint collection rules
- tests for discovery and drift reporting

Status:

- [ ] Todo

### 10. Deferred work recorded
Commit:

- `docs(roadmap): record future collection groups and multi-library tooling`

Deliverables:

- roadmap notes for:
  - collection groups
  - multi-library tooling
  - repo migration
  - include-based prompt composition
  - user config layout follow-through

Status:

- [ ] Todo

### 11. Changelog follow-through
Commit:

- `chore(changelog): record prompt library schema and discovery alignment changes`

Deliverables:

- updates to the governing changelog(s)

Status:

- [ ] Todo

## Working rules for this branch

- One conceptual change per commit.
- Docs before behavior.
- Schema before discovery behavior.
- Discovery before drift logic.
- Tests immediately after enforcement.
- Changelog follow-through before branch completion.

## Schema requirements for the next commit

The next schema commit should encode:

- library identity metadata
- one repo assignment per library
- one prompts root per library
- explicit collections relative to the prompts root
- unique collection names within a library
- unique collection paths within a library
- collection paths must be un-nested and non-overlapping
- allowed prompt extensions
- canonical prompt filename policy

The schema should not yet expose:

- editable collection resolution behavior
- nested collection ownership
- group-driven discovery behavior
- multi-library runtime behavior

## Validation checklist

- [x] Canonical library model documented
- [x] Branch execution plan documented
- [x] README and docs hub linked
- [x] Canonical model refined for repo-bound disjoint collections
- [ ] Shared schema updated
- [ ] Discovery aligned to schema
- [ ] Drift detection completed
- [ ] Validation guardrails added
- [ ] Fixtures and tests added
- [ ] Changelog updated
- [ ] Roadmap follow-up captured

## Post-branch follow-up

After this branch lands, plan separate follow-up work for:

- collection groups for multi-collection search scope
- multi-library management tooling
- migration to the official Impromptu app repository
- include-based prompt composition, if still desired

That later work should clarify:

- library selection and switching across repos
- source-of-truth ownership between repositories
- runtime code migration boundaries
- documentation ownership after migration
- bootstrap and tooling path updates
- release and changelog flow after export
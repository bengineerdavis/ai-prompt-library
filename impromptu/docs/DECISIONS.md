# Impromptu: Schema Migration Handoff, Doc Audit & Consolidation Plan

## Overview

This document captures the handoff plan for migrating schema ownership from the personal
prompt library repo to the Impromptu application repo, a full audit of current doc files
against the v1 library model, and a consolidation plan for the scattered docs state.
It is intended to be committed as a note before closing the current branch.

______________________________________________________________________

## Part 1: Handoff — Schema Migration to Application Repo

### What was done in this branch

The following work was completed in the personal prompt library repo (`impromptu/`):

- **`schemas/prompt-library.schema.json`** — hand-authored JSON Schema (Draft 2020-12),
  aligned to the v1 library model[1] [2]
- **`docs/examples/prompt-library.example.json`** — valid JSON instance, validated by
  `check-jsonschema`[3]
- **`docs/examples/prompt-library.example.toml`** — valid TOML instance, validated by
  Taplo
- **`.taplo.toml`** — schema association for Taplo TOML validation
- **`.pre-commit-config.yaml`** — full hook chain: `pretty-format-json`,
  `check-metaschema`, `check-jsonschema`, `taplo-format`, `taplo-lint`

### Where schema ownership moves

| Artifact                                 | Current home                 | Future home                                            |
| ---------------------------------------- | ---------------------------- | ------------------------------------------------------ |
| `schemas/prompt-library.schema.json`     | Personal prompt library repo | Impromptu application repo                             |
| `tools/generate_schema.py`               | Does not exist yet           | Impromptu application repo                             |
| `docs/examples/prompt-library.example.*` | Personal prompt library repo | Impromptu application repo (as fixtures)               |
| `.taplo.toml`                            | Personal prompt library repo | Both repos (consumer uses schema URL once published)   |
| `.pre-commit-config.yaml` hooks          | Personal prompt library repo | Both repos (app owns schema, library repo consumes it) |

### Migration steps (in order)

1. **Create `tools/generate_schema.py`** in the application repo with Pydantic models as
   the source of truth:

   - `Repository`, `Library`, `Collection`, `PromptLibrary` models
   - Export JSON Schema from `PromptLibrary.model_json_schema()`
   - Generate example fixtures from a hardcoded instance
   - Output: `schemas/prompt-library.schema.json`,
     `docs/examples/prompt-library.example.json`,
     `docs/examples/prompt-library.example.toml`

1. **Verify parity** — run `generate_schema.py` and confirm the output matches the
   hand-authored schema committed in this branch.

1. **Add a `make schema` / `just schema` target** or equivalent that re-runs generation.

1. **Add CI drift detection** — fail if committed schema diverges from generated output
   (compare with `diff`).

1. **Publish the schema at a stable URL** — once the application repo has a release,
   update `.taplo.toml` in the personal library repo to reference
   `https://raw.githubusercontent.com/.../schemas/prompt-library.schema.json` instead of
   a local path.

1. **Remove the schema from the personal library repo** — after the application repo is
   canonical, the personal repo should only contain `impromptu-library.toml` (a consumer
   of the schema, not an owner of it).

### Pydantic model sketch (for `tools/generate_schema.py`)

```python
from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field

class Repository(BaseModel):
    provider: str = Field(min_length=1)
    owner: str = Field(min_length=1)
    name: str = Field(min_length=1)
    url: str | None = None

class Library(BaseModel):
    id: str = Field(min_length=1, pattern=r"^[a-z0-9] [a-z0-9-]*$")
    name: str = Field(min_length=1)
    mode: Literal["repo", "local"] | None = None
    prompts_root: str = Field(min_length=1)
    repository: Repository | None = None

class Collection(BaseModel):
    id: str = Field(min_length=1, pattern=r"^[a-z0-9] [a-z0-9-]*$")
    path: str = Field(min_length=1)
    extensions: list[str] = Field(min_length=1)
    primary_file: str = "prompt.md"

class PromptLibrary(BaseModel):
    library: Library
    collections: list[Collection] = Field(min_length=1)
```

______________________________________________________________________

## Part 2: Doc File Audit

### Files present and their status

#### Application repo docs (personal prompt library / `impromptu/`)

| File                                           | Status                                                                                                 | Action                                                                                                                                                         |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `README.md` [root](4)                          | Current — good top-level index                                                                         | Keep; update links to new doc structure                                                                                                                        |
| `docs/pipeline-and-stages.md`[5] [6]           | **Duplicate** — two identical copies found (`-4.md`, `-7.md`)                                          | Deduplicate; keep one canonical version                                                                                                                        |
| `docs/impromptu-library-model.md`[1]           | **Two versions** — draft v1 (`-3.md`) and updated canonical model (`file:1950`) with divergent content | Merge into one canonical doc; the newer version (`file:1950`) is more complete but uses older schema field names (`prompt_filename_policy`, `match-directory`) |
| `docs/project-workspace-model.md`[7]           | Current — good separation of concerns                                                                  | Keep; no changes needed                                                                                                                                        |
| `schemas/prompt-library.schema.json`[2]        | Current — just updated in this branch                                                                  | Keep until migrated to app repo                                                                                                                                |
| `docs/examples/prompt-library.example.json`[3] | Current — validated                                                                                    | Keep                                                                                                                                                           |
| `docs/examples/prompt-library.example.toml`    | Current — validated                                                                                    | Keep                                                                                                                                                           |
| `rubric-schema-v1.json`[8]                     | Exists but orphaned — no doc references it                                                             | Decide: move to `schemas/`, add to pre-commit coverage, or document purpose                                                                                    |

#### Seed system docs

| File                         | Status                                   | Action                          |
| ---------------------------- | ---------------------------------------- | ------------------------------- |
| `seed/README.md`[9]          | Current — good component reference       | Keep; directory map is accurate |
| `orchestrator/README.md`[10] | Current — inputs/outputs well documented | Keep                            |

### Issues requiring action

#### 1. Duplicate `pipeline-and-stages.md`

Files `pipeline-and-stages-4.md` and `pipeline-and-stages-7.md` are byte-for-byte
identical. One is a leftover from an earlier session upload.
Delete the numbered duplicate and keep the canonical path
`docs/pipeline-and-stages.md`.[5] [6]

#### 2. Two divergent library model docs

`impromptu-library-model-3.md` (the newer draft) and the earlier canonical version
(`file:1950`) contain:[1]

- Different terminology: newer uses `prompt directory` + `primary_file = "prompt.md"`;
  older uses `namespace` + `canonical prompt file` + `match-directory` policy[11] [1]
- The newer doc’s terminology (`primary_file`, `prompt directory`) is what the updated
  schema now uses — so the newer doc is correct[2] [1]
- The older doc’s `namespace` / `match-directory` language is now stale and misaligned
  with the schema[11] [2]

**Action**: Keep the newer version (`file:1953`) as the canonical library model doc.
Update it to add the “Groups” concept from the older version (groups are a useful future
concept worth preserving).
Delete the older version.[11]

#### 3. `rubric-schema-v1.json` is orphaned

`rubric-schema-v1.json` exists in the repo but is not referenced in any doc or
pre-commit hook. Either:[8]

- Add it to `schemas/` directory and cover it with `check-metaschema`
- Or document what it is for in `docs/` and add a `check-jsonschema` hook for any files
  it validates

#### 4. Library model doc still references old schema field names

The example shape in `impromptu-library-model.md` uses the old field names:[11]

- `name` instead of `id` for collections
- `prompt_extensions` instead of `extensions`
- `prompt_filename_policy: "match-directory"` instead of `primary_file: "prompt.md"`

Update the example JSON shape in the doc to match the current schema.[2] [1]

#### 5. `README.md` links need auditing

The root `README.md` links to `docs/modes-and-settings.md`, `docs/auto-mode-policy.md`,
`docs/onboarding.md`, `docs/examples.md`, `docs/pipeline-and-stages.md`,
`docs/thresholds-and-recommendations.md`, `docs/scoring-model.md`,
`docs/user-preferences-and-memory.md`, `docs/service-specific-guidance.md`,
`docs/deep-search.md`, `docs/setup.md`. None of the library model docs or schema docs
are linked from the root yet.
Add:[4]

- `docs/library-model.md` → library structure and discovery contract
- `docs/project-workspace-model.md` → project/workspace/environment model
- `schemas/` → schema files and validation

______________________________________________________________________

## Part 3: Proposed Doc Structure After Consolidation

```text
docs/
  README.md                        ← doc hub index (existing)
  modes-and-settings.md            ← keep as-is
  auto-mode-policy.md              ← keep as-is
  onboarding.md                    ← keep as-is
  examples.md                      ← keep as-is
  pipeline-and-stages.md           ← deduplicated (one copy)
  thresholds-and-recommendations.md← keep as-is
  scoring-model.md                 ← keep as-is
  user-preferences-and-memory.md   ← keep as-is
  service-specific-guidance.md     ← keep as-is
  deep-search.md                   ← keep as-is
  setup.md                         ← keep as-is
  library-model.md                 ← merged canonical (newer version + Groups section)
  project-workspace-model.md       ← keep as-is
  examples/
    prompt-library.example.json    ← keep
    prompt-library.example.toml    ← keep

schemas/
  prompt-library.schema.json       ← keep (migrate to app repo later)
  rubric-schema-v1.json            ← move here if not already; add to pre-commit

DECISIONS.md  (new)                ← ADR-style record of schema decisions and migration plan
TODO.md       (new or updated)     ← prioritized work queue
```

______________________________________________________________________

## Part 4: TODO Priority Queue

This captures the prioritized work queue, ordered by dependency and impact.

### Priority 1 — Pre-migration cleanup (this branch or next)

- [ ] Delete duplicate `pipeline-and-stages` file
- [ ] Merge library model docs into one canonical `docs/library-model.md`
- [ ] Update library model doc example shape to match current schema field names
- [ ] Move `rubric-schema-v1.json` to `schemas/`, add to `check-metaschema` hook
- [ ] Add `docs/library-model.md` and `docs/project-workspace-model.md` links to root
  `README.md`
- [ ] Create `DECISIONS.md` capturing schema field naming rationale and migration plan

### Priority 2 — Schema migration to application repo (first app repo task)

- [ ] Create `tools/generate_schema.py` with Pydantic models
- [ ] Verify generated schema matches committed hand-authored schema
- [ ] Add `make schema` / `just schema` target
- [ ] Add CI drift detection
- [ ] Commit generated `schemas/prompt-library.schema.json` as build artifact

### Priority 3 — Consumer repo update (after app repo publishes schema)

- [ ] Update `.taplo.toml` in personal library repo to reference published schema URL
- [ ] Remove `schemas/` directory from personal library repo
- [ ] Update pre-commit hooks in personal library repo to validate only the
  `impromptu-library.toml` consumer file

### Priority 4 — Runtime wiring (app repo, after schema migration)

- [ ] Wire Pydantic `PromptLibrary` model into app config loader
- [ ] Validate `impromptu-library.toml` at load time against Pydantic model
- [ ] Add fixtures and tests using generated example instances
- [ ] Add discovery behavior aligned to the `primary_file` rule in the library model

______________________________________________________________________

## Key Design Decisions (for `DECISIONS.md`)

These are the decisions made in this branch that should be recorded:

| Decision                                                       | Rationale                                                                                                                                       |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `primary_file` string instead of `prompt_filename_policy` enum | The model doc specifies `prompt.md` as the default filename; a string is more flexible and honest than a policy keyword with one valid value[1] |
| `id` instead of `name` for collections                         | Consistent with how the library itself uses `id`; identity fields should be named consistently[2]                                               |
| `extensions` instead of `prompt_extensions`                    | Shorter; matches natural TOML authoring style; no ambiguity at the collection level[2]                                                          |
| `repository` made optional                                     | Local-mode libraries (`mode = "local"`) have no repository; making it required would block the local use case[7]                                |
| `mode` enum (`"repo"` \| `"local"`)                            | Reflects the project model’s distinction between repo-backed and local-only libraries[7]                                                        |
| JSON Schema stays as committed artifact                        | Taplo requires JSON Schema; Pydantic generates it; the file is a build output, not the source of truth                                          |
| Trailing slash required on `prompts_root` and `path`           | Makes path concatenation unambiguous; enforced via regex pattern in schema[2]                                                                   |

# Impromptu Prompt Library Model

Status: Canonical v1 model\
Scope: Prompt library structure, discovery contract, and schema-alignment baseline

## Goal

Define the canonical v1 model for how Impromptu organizes prompt libraries on disk so documentation, schema, discovery, drift detection, and validation all follow the same contract.

## Core model

Impromptu models a prompt library as a repo-bound ontainer with one explicit library root, one prompts root, an optional factories root, and library-local metadata under `.impromptu/`.

The canonical hierarchy is:

- repository
- library root
- prompts root
- families
- prompt namespaces
- canonical prompt files
- supporting files
- factories root
- workspaces metadata

## Definitions

### Repository

A repository is the source-control boundary assigned to a library.

In v1:

- one library belongs to exactly one repository
- one repository may contain one library
- multi-library tooling is roadmap work, not part of the v1 runtime model

### Library root

A library root is the filesystem root managed by Impromptu within a repository.

In v1:

- the library root may be the repository root
- the library root may also be a nested directory such as `library/`
- all library-relative paths are resolved from the library root
- `.impromptu/` is library-local and lives under the library root

This means both of the following shapes are valid:

```bash
library-repo-root/
├── prompts/
├── factories/
└── .impromptu/
```

```bash
library-repo-root/
├── library/
│   ├── prompts/
│   ├── factories/
│   └── .impromptu/
├── pyproject.toml
└── .pre-commit-config.yaml
```

The flat form is likely to be the default for many users because it is simpler to discover. The nested form is supported early because advanced users may want repository-level tooling, automation, tests, packaging, or management scripts that sit outside the library content root.

### Library

A library is the top-level prompt organization unit managed by Impromptu.

A library must declare:

- library identity metadata
- repository assignment
- one explicit prompts root
- one or more families

A library may also declare:

- one factories root
- zero or more workspaces
- library-local metadata files under `.impromptu/`

A library is not itself a family.

### Prompts root

The prompts root is the single directory inside the library root under which all managed prompt families live.

Example:

- `prompts/`

In v1:

- each library has exactly one prompts root
- prompt discovery only considers paths under the prompts root
- any immediate child directory of the prompts root is treated as a family directory by discovery convention

### Family

A family is a library-model concept representing a first-level prompt lineage or grouping beneath the prompts root.

A family is not a special filesystem artifact type with its own marker file. In v1, any immediate child directory of the prompts root is a family directory by position.

Examples:

- `general/`
- `tutors/`
- `writing/`

In v1:

- family names must be unique within a library
- family paths must be unique within a library
- family paths are relative to the prompts root
- `general` may be designated as the default family for uncategorized prompts

### Prompt namespace

A prompt namespace is a prompt directory inside a family directory.

A prompt namespace owns one canonical prompt file and may also include supporting files.

Example:

```bash
prompts/
  general/
    shell-tools/
      shell-tools.md
      examples.md
      notes.md
```

Here:

- family = `general`
- prompt namespace = `shell-tools`
- canonical prompt file = `shell-tools.md`

In v1:

- any immediate child directory of a family directory is a prompt namespace candidate
- a prompt namespace is accepted only if it contains exactly one canonical prompt file
- the canonical prompt file basename must exactly match the namespace directory name
- supporting files do not become prompts unless they independently satisfy the canonical prompt rule in their own namespace directory

### Canonical prompt file

Each prompt namespace must contain exactly one canonical prompt file.

The canonical prompt file must:

- be a text file
- use an allowed prompt extension
- have a basename that exactly matches the prompt namespace directory name

Examples:

- `shell-tools/shell-tools.md`
- `meeting-recap/meeting-recap.md`

### Supporting files

A prompt namespace may contain additional text support files that help author, explain, or extend the prompt.

Examples:

- examples
- notes
- rubrics
- references
- implementation notes

Supporting files are not discovered as canonical prompts unless they independently satisfy the canonical prompt file rule inside their own namespace directory.

### Factories root

The factories root is an optional directory inside the library root used for factory definitions.

Example:

- `factories/`

In v1:

- the factories root is separate from the prompts root
- factory discovery is separate from prompt discovery
- factories are library assets but are not prompt families

### Workspaces

Workspaces are optional overlays used to bundle families and/or prompt namespaces together for a given environment or context.

Examples:

- `work-default`
- `scratch`

In v1:

- workspaces do not own filesystem content
- workspaces do not affect prompt ownership
- workspaces reference existing families and/or prompt namespaces
- workspace resolution is validated after schema validation

### Library-local metadata

Library-local metadata lives under `.impromptu/` inside the library root.

Examples:

- `.impromptu/prompt-library.json`
- `.impromptu/workspaces.json`

This directory is distinct from user-level configuration stored under XDG or similar global config locations.

## Discovery contract

In v1, prompt discovery works like this:

1. Resolve the library root.
1. Resolve the declared prompts root relative to the library root.
1. Treat each immediate child directory of the prompts root as a family directory.
1. Treat each immediate child directory of a family directory as a prompt namespace candidate.
1. Accept a prompt namespace only if it contains exactly one canonical prompt file matching the namespace directory basename.
1. Treat sibling non-canonical text files as supporting files.
1. Reject hidden, non-text, or invalid prompt candidates during validation.

Factory discovery is separate and starts from the declared factories root if present.

## Uniqueness rules

The uniqueness rules for v1 are:

- library identity is unique at the library level
- family names are unique within a library
- family paths are unique within a library
- prompt namespace names are unique within a library
- family names and prompt namespace names must be globally disjoint within a library
- canonical prompt filenames are unique within a namespace because only one canonical prompt file is allowed there

This means prompt namespace identity is library-global by name in v1, not family-scoped.

## Explicitly out of scope

The following are out of scope for the canonical v1 model:

- one library spanning multiple repositories
- multiple prompts roots inside one library
- nested prompt roots inside one library
- multiple libraries inside one repository
- prompt composition through include files
- inherited family configuration
- workspaces affecting prompt ownership or discovery precedence
- multi-library management tooling
- cross-library prompt resolution

## Why this model

This model is intentionally strict so that docs, schema, discovery, validation, and drift detection all share the same assumptions.

The design favors:

- explicit ownership
- one filesystem interpretation per configured library root
- low ambiguity
- easy validation
- future flexibility for either flat or nested library-root layouts

Workspaces can be added for convenience without changing the core ownership model.

## Schema alignment expectations

The schema aligned to this model should be able to express:

- library metadata
- repository assignment
- library root awareness
- prompts root
- optional factories root
- families
- workspaces
- allowed prompt extensions
- canonical filename policy

Standard JSON Schema is not sufficient by itself to enforce every cross-entity constraint in this model. Application validation should additionally enforce:

- family name uniqueness
- prompt namespace uniqueness
- family/prompt-name disjointness
- exactly one default family, if defaults are used
- workspace references resolving to real families and prompt namespaces
- path overlap or invalid nesting checks where needed

## Example shapes

Flat library root:

```bash
repo-root/
├── prompts/
│   ├── general/
│   │   └── meeting-recap/
│   │       └── meeting-recap.md
│   ├── tutors/
│   │   └── sentry-support-tutor/
│   │       └── sentry-support-tutor.md
│   └── writing/
│       └── blog-outline-writer/
│           └── blog-outline-writer.md
├── factories/
│   └── technical-tutor-for-self-learning/
│       └── technical-tutor-for-self-learning.md
└── .impromptu/
    ├── prompt-library.json
    └── workspaces.json
```

Nested library root:

```bash
repo-root/
├── library/
│   ├── prompts/
│   │   ├── general/
│   │   └── tutors/
│   ├── factories/
│   └── .impromptu/
│       ├── prompt-library.json
│       └── workspaces.json
├── pyproject.toml
└── .pre-commit-config.yaml
```

## Follow-on work

The next implementation steps after this doc are:

- align the manifest schema to this model
- align the example manifest to this model
- align discovery behavior to the schema
- add drift detection for schema/filesystem mismatch
- add validation guardrails
- add fixtures and tests

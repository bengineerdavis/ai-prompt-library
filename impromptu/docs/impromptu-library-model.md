# Impromptu Prompt Library Model

## Status

Draft v1 model.

## Purpose

Define the v1 model for how Impromptu organizes prompt libraries on disk so docs, discovery, validation, and future tooling use the same structure.

This version is intentionally simple and optimized for:
- repo-backed libraries,
- reuse across many projects,
- human-readable prompt storage,
- and predictable discovery.

## Core model

A library is a prompt storage unit.

In v1:
- a library is repo-backed,
- a library has one prompts root,
- a library declares one or more collections,
- collections contain prompt directories,
- each prompt directory has one primary prompt file,
- and sibling support files are allowed.

The main hierarchy is:

- repository
- library
- prompts root
- collections
- prompt directories
- primary prompt files
- support files

## Definitions

### Repository

A repository is the source-control boundary for a library.

In v1:
- one library belongs to one repository
- one repository contains one library definition

### Library

A library is the top-level prompt storage unit used by Impromptu.

A library declares:
- library identity metadata
- repository metadata
- one prompts root
- one or more collections

A library is not a project and is not a workspace.

### Prompts root

The prompts root is the single directory under which all managed prompt collections live.

Examples:
- `prompts/`
- `.impromptu/prompts/`

In v1:
- each library has exactly one prompts root
- all declared collections live under that prompts root
- discovery only scans under the prompts root

### Collection

A collection is a lateral discovery partition inside a library.

Collections exist to separate prompts by context, such as:
- personal
- scripts
- writing
- support
- team
- repo-specific

In v1:
- collections are explicitly declared
- collection names are unique within a library
- collection paths are unique within a library
- collection paths must not overlap

Collections are storage and discovery partitions. They are not the same thing as families, tags, or version groups.

### Prompt directory

A prompt directory is a directory inside a collection that represents one prompt alias.

Example:

```text
prompts/
  scripts/
    jq-helper/
      prompt.md
      notes.md
```

Here:
- collection: `scripts`
- prompt alias: `jq-helper`
- primary prompt file: `prompt.md`

Prompt identity is collection-scoped.

### Primary prompt file

Each prompt directory must contain exactly one primary prompt file.

In v1, the default filename is:

- `prompt.md`

This is simpler and easier to work with than repeating the directory name in the filename.

### Support files

A prompt directory may contain additional support files, such as:
- `notes.md`
- `examples.md`
- `rubric.md`
- `references.md`
- `meta.toml`

Support files help authoring and maintenance but are not themselves primary prompt files.

## Discovery contract

In v1, prompt discovery works like this:

1. Start from the declared prompts root.
2. Limit traversal to declared collection paths.
3. Discover prompt directories inside collections.
4. Accept a prompt directory only if it contains exactly one primary prompt file.
5. Treat sibling non-primary text files as support files.
6. Reject hidden, invalid, or non-text prompt candidates during validation.

Discovery is collection-scoped, not library-global by filename alone.

## Uniqueness rules

The uniqueness rules for v1 are:

- library id is unique at the library level
- collection names are unique within a library
- collection paths are unique within a library
- collection paths do not overlap
- prompt aliases are unique within a collection

A prompt alias does not need to be globally unique across the entire library if it appears in different collections.

Example:

```text
prompts/
  personal/
    shell-tools/
      prompt.md
  scripts/
    shell-tools/
      prompt.md
```

This is valid because prompt identity is collection-scoped.

## Metadata guidance

If additional prompt metadata is needed, store it in a support file such as:

- `meta.toml`

Examples of metadata that may belong there:
- description
- tags
- owner
- family
- visibility

In v1, metadata is optional and should not replace directory-based discovery.

## Example file tree

```text
library-root/
  impromptu-library.toml
  prompts/
    personal/
      shell-tools/
        prompt.md
        notes.md
    scripts/
      jq-helper/
        prompt.md
        examples.md
    writing/
      meeting-recap/
        prompt.md
        rubric.md
```

## Example library uses

A single library may be used by:
- the user’s `local-default` project
- one or more repo-backed projects

A single project may bind:
- one personal library
- one team library
- one project-specific shared library

## Out of scope for v1

The following are out of scope:

- multiple prompts roots in one library
- nested or overlapping collection ownership
- family as a filesystem primitive
- db-only prompt storage
- automatic cross-library resolution
- complex config inheritance across libraries

## Follow-on work

The next implementation steps are:

- define `impromptu-library.toml`
- update examples from JSON to TOML
- align discovery behavior with the primary prompt file rule
- add validation guardrails
- add fixtures and tests
# Impromptu Prompt Library Model

Status: Canonical v1 model  
Scope: Prompt library structure, discovery contract, and schema-alignment baseline

## Goal

Define the canonical v1 model for how Impromptu organizes prompt libraries on disk so documentation, schema, discovery, drift detection, and validation all follow the same contract.

## Core model

Impromptu models a prompt library as a repo-bound container with one explicit prompts root and one or more declared collections beneath it.

The canonical hierarchy is:

- repository
- library
- prompts root
- collections
- namespaces
- canonical prompt files
- supporting files

## Definitions

### Repository

A repository is the source-control boundary assigned to a library.

In v1:

- one library belongs to exactly one repository
- one repository may contain one library
- multi-library tooling is roadmap work, not part of the v1 runtime model

### Library

A library is the top-level prompt organization unit managed by Impromptu.

A library must declare:

- library identity metadata
- repository assignment
- one explicit prompts root
- one or more collections

A library is not itself a collection.

### Prompts root

The prompts root is the single directory inside the repository under which all managed prompt collections live.

Examples:

- `prompts/`
- `.impromptu/prompts/`

In v1:

- each library has exactly one prompts root
- all declared collections must live under that prompts root
- prompt discovery only considers paths under the prompts root

### Collection

A collection is an explicit discovery scope under the prompts root.

Collections exist to let a library separate prompts by context, such as:

- personal
- work
- repo-specific
- team-specific
- environment-specific

Examples:

- `personal/`
- `work-repo-a/`
- `work-repo-b/`

In v1:

- collections are explicitly declared
- collection names must be unique within a library
- collection paths must be unique within a library
- collection paths must be un-nested and non-overlapping
- no collection path may be the parent or child of another collection path
- collection paths are relative to the library prompts root

This means a library may organize prompt directories inside one or more collections, but collections themselves do not form a hierarchy.

### Groups

Groups are a future organizational concept for activating or searching multiple collections together without selecting the entire library.

Examples:

- `work-default` → `work-repo-a`, `work-repo-b`
- `personal-cli` → `personal-shell`, `personal-dotfiles`

In v1:

- groups are not required for discovery
- groups do not affect filesystem ownership
- groups are the preferred future mechanism for multi-collection search scope
- groups are separate from collections and do not imply parent-child collection relationships

### Namespace

A namespace is a prompt directory inside a declared collection.

A namespace owns one canonical prompt file and may also include supporting files.

Example:

```text
prompts/
  personal/
    shell-tools/
      shell-tools.md
      examples.md
      notes.md
```

Here:

- collection = `personal`
- namespace = `shell-tools`
- canonical prompt file = `shell-tools.md`

Namespace identity is collection-scoped.

In v1:

- namespace uniqueness is enforced within a collection
- identical namespace directory names may exist in different collections
- namespace discovery is based on directory structure, not manually declared namespace records

### Canonical prompt file

Each namespace must contain exactly one canonical prompt file.

The canonical prompt file must:

- be a text file
- use an allowed prompt extension
- have a basename that exactly matches the namespace directory name

Examples:

- `shell-tools/shell-tools.md`
- `deploy-debug/deploy-debug.md`

This is the canonical filename rule for v1.

### Supporting files

A namespace may contain additional text support files that help author, explain, or extend the prompt.

Examples:

- examples
- notes
- rubrics
- references
- implementation notes

Supporting files are not discovered as canonical prompts unless they independently satisfy the canonical prompt file rule inside their own namespace directory.

## Discovery contract

In v1, prompt discovery works like this:

1. Start from the declared library prompts root.
2. Limit traversal to declared collection paths.
3. Discover namespace directories inside collections.
4. Accept a namespace only if it contains exactly one canonical prompt file matching the namespace directory basename.
5. Treat sibling non-canonical files as supporting files.
6. Reject hidden, non-text, or invalid prompt candidates during validation.

Discovery is collection-scoped, not library-global by filename alone.

## Uniqueness rules

The uniqueness rules for v1 are:

- library identity is unique at the library level
- collection names are unique within a library
- collection paths are unique within a library
- collection paths may not overlap
- namespace paths are unique within a collection
- canonical prompt filenames are unique within a namespace because only one canonical prompt file is allowed there

A prompt name does not need to be globally unique across the entire library if it appears in different collections.

Example:

```text
prompts/
  personal/
    shell-tools/
      shell-tools.md
  work-repo-a/
    shell-tools/
      shell-tools.md
```

This is valid because namespace uniqueness is collection-scoped.

## Explicitly out of scope

The following are out of scope for the canonical v1 model:

- one library spanning multiple repositories
- multiple prompts roots inside one library
- nested or overlapping collections
- collection parent-child ownership rules
- prompt composition through include files
- inherited collection configuration
- groups affecting prompt ownership or discovery precedence
- multi-library management tooling
- cross-library prompt resolution

## Why this model

This model is intentionally strict so that docs, schema, discovery, validation, and drift detection all share the same assumptions.

The design favors:

- explicit ownership
- one filesystem interpretation
- low ambiguity
- easy validation
- future compatibility with multi-library tooling

Groups can be added later for convenience without changing the core ownership model.

## Schema alignment expectations

The schema aligned to this model should be able to express:

- library metadata
- repository assignment
- prompts root
- explicit collections
- allowed prompt extensions
- canonical filename policy

The schema should not expose collection-overlap resolution as a user-editable option in v1 because overlapping collections are invalid.

## Example shape

Illustrative example:

```json
{
  "library_name": "impromptu-main",
  "library_id": "impromptu-main",
  "repository": {
    "provider": "github",
    "owner": "example",
    "name": "impromptu",
    "url": "https://github.com/example/impromptu"
  },
  "prompts_root": "prompts/",
  "collections": [
    {
      "name": "personal",
      "path": "personal/",
      "prompt_extensions": [".md"],
      "prompt_filename_policy": "match-directory"
    },
    {
      "name": "work-repo-a",
      "path": "work-repo-a/",
      "prompt_extensions": [".md"],
      "prompt_filename_policy": "match-directory"
    },
    {
      "name": "work-repo-b",
      "path": "work-repo-b/",
      "prompt_extensions": [".md"],
      "prompt_filename_policy": "match-directory"
    }
  ]
}
```

## Follow-on work

The next implementation steps after this doc are:

- align the manifest schema to this model
- align discovery behavior to the schema
- add drift detection for schema/filesystem mismatch
- add validation guardrails
- add fixtures and tests
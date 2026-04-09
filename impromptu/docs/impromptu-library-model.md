# Impromptu Prompt Library Model

Status: Draft for `refactor/shared-schemas-and-doc-alignment`

## Purpose

This document defines the canonical v1 model for how Impromptu discovers and reasons about prompt-library content.

The goal is to replace ad hoc prompt detection and denylist-heavy behavior with a small, opinionated, convention-based ruleset that is easy to document, validate, and enforce.

## Design goals

- Prefer convention over per-file registration.
- Make prompt discovery deterministic.
- Keep prompt namespaces portable and human-readable.
- Avoid endless denylist maintenance for file exclusions.
- Reserve more advanced composition features for later phases.

## Terms

### Library
A prompt library is a repository or filesystem root managed by Impromptu.

### Collection
A collection is a declared root-relative directory under which prompt namespaces may be discovered recursively.

Examples:

- `prompts/`
- `prompts/direct-use/`
- `prompts/factories/`

### Namespace
A namespace is a directory reserved for exactly one prompt and its supporting files.

A namespace is the basic unit of organization inside a collection.

### Canonical prompt file
The canonical prompt file is the one file in a namespace that Impromptu treats as the prompt.

### Supporting file
A supporting file is any non-canonical file inside the namespace directory. Supporting files may be text or binary and are not themselves treated as prompts.

## V1 rules

### Collection rules

- Prompt discovery happens only inside declared collections.
- Discovery is recursive within each collection.
- Files outside declared collections are never prompts.

### Namespace rules

- A prompt namespace is a directory.
- A namespace reserves one prompt and its supporting files.
- There is exactly one prompt per namespace directory.
- Namespace directory names must be unique within a collection.
- Library-wide uniqueness is preferred, but collection-level uniqueness is the minimum v1 requirement.

### Canonical filename rules

- The canonical prompt filename must match its parent directory basename.
- The canonical prompt filename must use an allowed text extension.
- The preferred v1 extension is `.md`.

Example:

```text
prompts/
  sentry-triage/
    sentry-triage.md
    notes.md
    examples/
```

In this example, `sentry-triage/` is the namespace and `sentry-triage.md` is the canonical prompt file.

### File eligibility rules

A prompt candidate must be:

- a regular file
- non-hidden
- inside a non-hidden namespace path
- text-decodable
- named according to the canonical filename rule

A prompt candidate must not be:

- a directory
- a hidden file
- a file under a hidden directory
- a non-text file

## Discovery model

A file is a prompt if and only if all of the following are true:

1. The file is under a declared collection path.
2. The file is a regular file.
3. The file is not hidden, and no parent segment under the collection is hidden.
4. The file basename matches its parent directory basename.
5. The file extension is in the collection allowlist.
6. The file passes the text-file check.
7. The parent namespace directory has no conflicting canonical prompt candidate.

Everything else in the namespace is a supporting file.

## Suggested schema shape

The shared schema should be able to express at least:

```json
{
  "collections": [
    {
      "name": "default",
      "path": "prompts/",
      "prompt_extensions": [".md"],
      "prompt_filename_policy": "match-directory"
    }
  ]
}
```

This document defines the contract. Exact schema field names may be adjusted during implementation, but the behavior described here is the source of truth.

## Drift detection scope

Drift detection should be able to flag at least:

- namespace directory with no canonical prompt file
- multiple canonical candidates in one namespace
- canonical filename mismatch
- hidden candidate paths
- non-text prompt candidates
- prompt-like files outside collections
- duplicate namespace names within a collection
- schema declarations that no longer match on-disk layout

## Out of scope for v1

The following are explicitly not part of the initial contract:

- include-file composition for prompts
- inheritance between prompts
- cross-namespace prompt composition
- multi-file prompt assembly as a required behavior
- global library-wide uniqueness as a hard failure
- structured prompt specs beyond simple text files

## Roadmap notes

Future phases may add an explicit include mechanism for scoped prompt composition, but the canonical prompt file must remain understandable and portable on its own.

Migration or export of the stabilized implementation to the official Impromptu app repository is a post-branch follow-up, not part of this document.
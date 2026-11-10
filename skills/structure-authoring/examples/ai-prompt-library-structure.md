# Synthetic example: an installable skill library

## Request

"Make it easy to add skills to my library and install them through my Ansible
topic. The folder structure and skill files must be valid."

## Discovery and decisions

The target has `skills/<name>/` directories, Skillet specs, and a dotagents
source wildcard in the dotagents Ansible topic. It does not need a second
installer or a new per-skill manifest.

The public validation seam is alint checking a synthetic library. It catches
missing authoring specs and invalid runtime files; it does not measure skill
behavior or replace Skillet evals. The user confirmed this direction before
implementation.

The domain workflow boundary is:

- `grill-with-docs` for domain discovery and durable decisions;
- `interaction-questioning` for the next useful question;
- `structure-authoring` for executable enforcement after the form is settled.

## Structure contract

Use `dir_contains` to require `skills/*/spec.md`. Use alint's `command` rule to
call Skillet for each `skills/*/SKILL.md`. Skillet owns both schema validation
and stale-render detection; no custom hash implementation belongs in alint.
Generate the agent-facing alint block from the same active rules.

This follows the creator's
[Why alint](https://alint.org/blog/why-alint): alint checks filesystem shape,
not code semantics. It does not replace language linters, SAST, secret scanners,
dependency-graph analysis, or license identification. Command rules delegate to
specialists and must have their runtime measured.

## Verification

The real alint policy runner accepted a spec-only authoring directory and
rejected a missing spec, missing frontmatter, and stale hash. The live library
check found and helped repair the invalid research skill and three stale
hashes. The full 13-skill gate takes about 7 seconds; the changed-file gate
takes about 0.12 seconds on the authoring machine. No Ansible apply or live
installation was performed.

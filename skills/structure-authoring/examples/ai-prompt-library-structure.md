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
call Skillet for each `skills/*/SKILL.md`. Reject a rendered skill whose
`spec_hash` does not match the current spec. Generate the agent-facing alint
block from the same active rules.

## Verification

The real alint policy runner accepted a spec-only authoring directory and
rejected a missing spec, missing frontmatter, and stale hash. The live library
check found and helped repair the invalid research skill and three stale
hashes. No Ansible apply or live installation was performed.

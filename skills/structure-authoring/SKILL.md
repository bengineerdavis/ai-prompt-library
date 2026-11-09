---
name: structure-authoring
description: Turns a desired repository or artifact structure into executable, reviewable enforcement. Use when defining required directories, files, content contracts, alint rules, generated agent instructions, or validation for a template or reusable artifact library.
license: MIT
spec_hash: 1352073476d5
metadata:
  version: "1.0.0"
---

# Structure Authoring

Turn the desired **form** into an executable contract. Do not leave a required
structure as prose that an agent must remember to follow.

Use alint as the first structural enforcement tool. Add other tools only when
they already own the relevant concern or alint cannot express the contract.

## Workflow

1. Inspect the target's actual files, instructions, validation commands, and
   tool configuration. Identify which artifacts are authored, generated, or
   required at runtime. Preserve existing user work.
1. Use `grill-with-docs` for domain-driven discovery and durable vocabulary and
   decisions. Use `interaction-questioning` to choose the next useful question
   without causing question fatigue. Ask only when the answer changes the
   structure, enforcement owner, strictness, or output contract. Research local
   facts rather than asking the user to supply them. Do not invent a combined
   workflow skill before that interaction contract has its own design session.
1. Propose the public testing seam and obtain confirmation before adding a new
   test surface. State what the seam catches and misses. Do not replace an
   existing behavior test with a redundant lower-level test.
1. Write the smallest native rules for required paths, allowed artifacts,
   content, and failure states. Prefer alint's built-in rules and its `command`
   adapter to an existing validator. Do not build a second validator.
1. Generate agent instructions from the active rules where supported. Preserve
   prose outside the generated block.
1. Run the real checker on a compliant and a deliberately noncompliant fixture.
   Verify the intended failure and fail closed on missing tools or invalid
   configuration.
1. Report exactly what ran and what remains. Stop at the repository's existing
   review, commit, push, and installation gates.

## Alint contract

Use `alint rules show <kind>` to inspect the actual interface before writing a
rule. Common starting points:

- `dir_contains` — every directory matching `select:` contains each required
  child in `require:`.
- `command` — run an existing validator once per matched file; use `{dir}` for
  the containing artifact directory.
- `file_content_matches` — assert required content.
- `file_content_forbidden` — reject forbidden content.
- `file_exists` / `file_absent` — enforce presence or absence.

A library of installable skills can use this shape:

```yaml
version: 1
requires:
  alint: "0.21.0"
rules:
  - id: skills-have-authoring-specs
    kind: dir_contains
    select: "skills/*"
    require: ["spec.md"]
    level: error
  - id: installable-skills-are-valid
    kind: command
    paths: "skills/*/SKILL.md"
    command:
      - npx
      - -y
      - "@sentry/skillet@latest"
      - validate
      - "{dir}"
      - --json
    timeout: 120
    level: error
```

After changing `.alint.yml`, run:

```sh
alint validate-config
alint check
alint test --allow-spawn
alint export-agents-md --inline --output AGENTS.md
```

Put one policy case per `alint-tests/*.yml` file. Declare `capabilities: spawn: true` only for cases that invoke a real validator. Use `exit: policy_failure` for a deliberate violation and `exit: success` for a compliant
fixture. A passing check is not enough: observe the intended failure too.

The last command refreshes the `<!-- alint:start -->` block from the active
rules. It must not overwrite prose elsewhere in `AGENTS.md`.

## Template applications

For a Copier or agentic template, prove the behavior through a real stamp and
update before applying it to a project. Test the public stamping interface,
not just a generator helper. The template should generate the alint block when
alint is enabled and refresh it when the layer or rules change.

Do not apply a template change to a live project merely because the rule looks
correct. Let the template's checks and the project's normal review gate decide.

## Never

- Never reimplement a native rule, schema, or validator when configuration or
  a thin adapter expresses the contract.
- Never overwrite project-owned prose, existing configuration, or unrelated
  uncommitted work.
- Never claim compatibility with another installer, tool, or skills.sh without
  verifying its actual interface.
- Never report a structure as valid when the checker did not run or a bad
  fixture was not observed to fail.

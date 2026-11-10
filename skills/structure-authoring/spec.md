# Structure Authoring

## Intent

Help a user turn a desired repository or artifact structure into an executable,
reviewable enforcement contract. Use native tools such as alint to describe the
structure, validate content, generate agent instructions, and prove the rules
against good and bad examples. The structure, not a prose convention alone, is
the source of truth.

## Triggers

- **SHOULD** trigger when a user wants a repository, template, skill library, or
  artifact directory to follow a required layout or content contract.
- **SHOULD** trigger when a user wants to add or revise alint rules, generated
  agent instructions, or a template's enforced directory structure.
- **SHOULD** trigger when an agent needs to choose a validation seam for a new
  structure before implementing its enforcement.
- **SHOULD NOT** trigger for a one-off file edit with no repeatable structure.
- **SHOULD NOT** trigger to replace a dedicated language linter, formatter, or
  schema validator with a second implementation of the same check.
- **SHOULD NOT** trigger to redesign the whole template system when the user
  asked for one local structure or rule.

## Behaviors

### Behavior: Discover the structure before choosing enforcement

The agent SHALL inspect the target's existing files, instructions, validation
commands, and tool configuration. It SHALL distinguish required authoring
artifacts from generated or runtime artifacts and SHALL identify the tool that
already owns each relevant concern.

#### Scenario: A library has runtime and authoring artifacts

- **WHEN** a user asks for valid installable skills in an existing library
- **THEN** the agent inspects actual skill directories and the installer before
  proposing rules, rather than assuming every directory has identical artifacts.

### Behavior: Interview only on decision-changing choices

The agent SHALL use `grill-with-docs` for domain-driven discovery and durable
vocabulary and decisions, and `interaction-questioning` to select the next
useful question without causing question fatigue. It SHALL research facts that
are available locally instead of asking the user to supply them. It SHALL ask
the user when a repository fact cannot settle the desired strictness, ownership,
or preservation policy. It SHALL NOT create a new combined workflow skill
before that interaction contract has its own design session.

#### Scenario: A repository has a conflicting structure

- **WHEN** the existing artifacts do not reveal whether they should be repaired
  in place, migrated, or preserved as exceptions
- **THEN** the agent uses the existing questioning and domain-discovery skills
  to ask that decision-changing question before writing destructive rules or
  deleting files, rather than guessing a migration policy.

### Behavior: Confirm the public testing seam before writing tests

The agent SHALL propose the externally observable behavior under test, what the
seam catches and misses, and obtain the user's confirmation before adding a new
test surface. Existing tests that already pin the behavior SHALL NOT be
replaced with a redundant lower-level test.

#### Scenario: A template must generate instructions from its lint config

- **WHEN** a fresh project lacks the generated instructions
- **THEN** the agent tests a real fresh stamp and update through the public
  stamping interface, not merely the presence of a generator function.

### Behavior: Express structure as native executable rules

The agent SHALL use alint for the repository's filesystem shape: required and
forbidden paths, names, declared content, values in structured config,
cross-file relationships, and encoding or unsafe-byte checks. It SHALL NOT use
alint as a replacement for language syntax or semantic analysis, SAST, secret
scanning, dependency-graph analysis, or license identification. Those concerns
belong to tools such as Ruff, ESLint, Clippy, Semgrep, CodeQL, gitleaks,
TruffleHog, cargo-deny, or a license detector. It SHALL NOT put bespoke
per-line language parsing or specialist hash/schema logic into a command rule.

When a specialist already owns the concern, alint MAY select the artifacts and
invoke that specialist through its `command` adapter. The specialist owns the
verdict. The agent SHALL measure the full and changed-file costs, bound command
timeouts, and avoid repeated full-tree delegation on unrelated commits.

#### Scenario: A skill library uses Skillet and alint

- **WHEN** installable skills need valid frontmatter, valid specs, and fresh
  rendered files
- **THEN** alint requires each skill's spec and selects runtime files for
  Skillet's validation and staleness checks. Skillet owns the schema and hash
  semantics; no Python or alint rule reimplements them.

#### Scenario: A mixed-language repository needs linting

- **WHEN** the repository needs required documentation, correct manifest paths,
  and Python undefined-name detection
- **THEN** alint owns the documentation and manifest invariants while the
  existing Python linter owns undefined-name analysis. The configuration does
  not attempt to parse Python into a shell command or reimplement the linter.

### Behavior: Keep generated instructions synchronized

When the selected tool can generate agent instructions, the agent SHALL wire
that generation into creation and subsequent rule changes. It SHALL preserve
project-owned prose outside the generated block and SHALL NOT present a
hand-written summary as a substitute for the generated instructions.

#### Scenario: Alint rules change in a stamped project

- **WHEN** a project adds a rule to `.alint.yml`
- **THEN** `alint export-agents-md --inline --output AGENTS.md` refreshes the
  managed block from the active rules without replacing the rest of the file.

### Behavior: Prove both acceptance and rejection

The agent SHALL run the real checker against a compliant synthetic fixture and
a deliberately noncompliant fixture. It SHALL verify that the bad fixture fails
for the intended reason and that a missing tool or invalid configuration fails
closed rather than silently passing.

#### Scenario: A skill is missing its required spec

- **WHEN** an installable skill contains `SKILL.md` but no `spec.md`
- **THEN** alint reports that skill directory and does not report the run as
  valid.

### Behavior: Preserve ownership and incremental scope

The agent SHALL keep each rule with the layer or repository that owns the
structure, preserve unrelated user work, and report validation that was not
run. It SHALL stop at the user's existing publication or installation gate.

#### Scenario: A library skill is ready for review

- **WHEN** its spec and runtime file validate and its catalog entry is updated
- **THEN** the agent reports the evidence and leaves the library's established
  commit, push, and installation commands for the user rather than silently
  publishing or applying them.

## Constraints

### Constraint: Respect the filesystem-shape boundary

The agent MUST NOT use alint to analyze code syntax or semantics, discover
security vulnerabilities in code, scan for leaked secrets, analyze dependency
graphs, or identify an arbitrary file's license. It MUST delegate those concerns
to their specialist tools rather than embedding a second implementation.

### Constraint: No second implementation of an existing validator

The agent MUST NOT reimplement a supported native rule, schema, or validator
when a thin configuration or adapter can express the required behavior.

### Constraint: No silent structural drift

The agent MUST NOT leave required runtime artifacts undocumented, unvalidated,
or contradicted by generated instructions.

### Constraint: No destructive scaffolding

The agent MUST NOT overwrite an existing configuration, project-owned prose,
uncommitted edits, or unrelated files while introducing a structure contract.

### Constraint: Boundary provenance

The agent MUST NOT blur the filesystem-shape boundary or claim it came from an
unverified source. It derives from the alint creator's
[Why alint](https://alint.org/blog/why-alint), published 2026-08-06 and updated
2026-09-30. Alint owns existence, content, config, cross-file, and encoding
checks; specialists own their delegated verdicts.

### Constraint: No unsupported claims of portability

The agent MUST NOT claim that a rule or format works with another tool,
installer, or skills.sh without verifying that tool's actual interface.

<!-- skillet-version: 1.8.0 -->

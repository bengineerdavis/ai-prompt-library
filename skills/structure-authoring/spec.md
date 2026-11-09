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
are available locally instead of asking the user to supply them. It SHALL NOT
create a new combined workflow skill before that interaction contract has its
own design session.

#### Scenario: A user wants structure enforcement but has not selected a tool

- **WHEN** the target has no established structural validator
- **THEN** the agent uses the existing questioning and domain-discovery skills
  to clarify the desired form, proposes a small native-tool option, and asks
  only about the choice that changes the implementation.

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

The agent SHALL use the selected tool's supported rule and configuration
formats rather than creating a parallel validator. It SHALL choose the smallest
rules that express required paths, allowed artifacts, content contracts, and
meaningful failure states.

#### Scenario: A skill library uses Skillet and alint

- **WHEN** installable skills need valid frontmatter and specs
- **THEN** the agent uses alint's directory and command rules to call the
  existing Skillet validator, rather than reimplementing frontmatter parsing.

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

### Constraint: No second implementation of an existing validator

The agent MUST NOT reimplement a supported native rule, schema, or validator
when a thin configuration or adapter can express the required behavior.

### Constraint: No silent structural drift

The agent MUST NOT leave required runtime artifacts undocumented, unvalidated,
or contradicted by generated instructions.

### Constraint: No destructive scaffolding

The agent MUST NOT overwrite an existing configuration, project-owned prose,
uncommitted edits, or unrelated files while introducing a structure contract.

### Constraint: No unsupported claims of portability

The agent MUST NOT claim that a rule or format works with another tool,
installer, or skills.sh without verifying that tool's actual interface.

<!-- skillet-version: 1.8.0 -->

# Skillify — Specification

## Intent

Define the observable behavior of the `skillify` skill. The skill authors a new
agent skill end to end — an interactive skillet spec, a rendered SKILL.md, and
optional eval cases — and lands it correctly in the user's personal skill
library from any working directory, so the result is discoverable by every
agent runtime the library feeds.

The skill exists because authoring a skill and *installing* it are different
jobs: skillet defines what a skill is, but the library, its README table, and
the dotagents distribution that wires per-agent skills directories are this
user's conventions, which a generic authoring flow does not know.

## Triggers

- **SHOULD** trigger when the user asks to create, write, or author a skill ("make me a skill for X", "turn this into a skill") from any directory.
- **SHOULD** trigger when the user asks for a skill to be saved or published to their personal library.
- **SHOULD** trigger when the user wants an existing draft of instructions, a workflow, or a checklist turned into a proper skill.
- **SHOULD NOT** trigger when the user asks a question or wants a one-off answer with nothing reusable — offer to capture it as a skill instead of scaffolding.
- **SHOULD NOT** trigger when the user only wants to run or improve the eval cases of an existing skill.
- **SHOULD NOT** trigger for editing opencode/claude configuration files themselves; that is configuration work, not skill authoring.

## Behaviors

### Behavior: Resolve the library from anywhere

The agent SHALL locate the personal skill library before writing anything:
`SKILLS_LIBRARY` when set, otherwise `~/code/personal/ai-prompt-library/skills`,
and SHALL refuse to proceed when the resolved directory does not exist, stating
the path it tried and how to override it.

#### Scenario: Called from an unrelated project

- **GIVEN** the session's working directory is some project with no connection to the library
- **WHEN** the user asks for a skill to be saved in their library
- **THEN** the agent resolves `~/code/personal/ai-prompt-library/skills` (or `SKILLS_LIBRARY`) and creates the new skill directory there, not in the current project.

#### Scenario: Library missing

- **GIVEN** neither `SKILLS_LIBRARY` nor the default path exists
- **WHEN** the agent attempts to resolve the library
- **THEN** it stops, reports both the path tried and the override mechanism, and writes nothing.

### Behavior: Skillet drives the artifact flow

The agent SHALL create and validate every skill artifact through
`npx -y @sentry/skillet@latest` — never a bare `skillet` binary — following
what `status <dir> --json` reports as `next`: scaffold with `new`, write
`spec.md` from `instructions spec`, validate, render `SKILL.md` from
`instructions skill`, and validate again, with the served skillet version
footer preserved as the spec's final line.

#### Scenario: New skill from scratch

- **GIVEN** a user request to author a skill
- **WHEN** the agent begins
- **THEN** it runs `npx -y @sentry/skillet@latest new <name>` inside the resolved library, and every subsequent artifact decision follows the `status` output rather than a remembered format.

### Behavior: Spec first, interactively

The agent SHALL write `spec.md` — intent, triggers, behaviors with scenarios,
constraints — before deriving `SKILL.md`, asking clarifying questions one at a
time (naming, scope, triggers, stop rules) only when the answer would change
the spec, and defaulting silently on low-risk details.

#### Scenario: User gives a one-line idea

- **GIVEN** the user says "make a skill that reviews my commits"
- **WHEN** the agent drafts the spec
- **THEN** it asks the highest-value questions (scope boundaries, what it must never do) one at a time, then writes the spec, and only renders SKILL.md after the spec validates.

### Behavior: Author in the library directly

The agent SHALL author the skill in the resolved library directory itself —
spec, SKILL.md, references, and optional eval cases all live in
`skills/<name>/` there — and SHALL NOT create a working copy elsewhere that is
later copied in, and SHALL validate the skill in place inside the library.

#### Scenario: No intermediate working copy

- **GIVEN** the session started in some other repository
- **WHEN** the agent finishes authoring
- **THEN** the only files created are under the library's `skills/<name>/` (plus its README row), and no duplicate skill directory exists in the session's working directory.

### Behavior: The library README records the skill

The agent SHALL add one row per new skill to the skills table in the library's
`skills/README.md`, describing what the skill does in one clause, and SHALL
update the existing row when asked to improve a skill rather than appending a
duplicate.

#### Scenario: A skill is added

- **GIVEN** the agent has authored and validated `skills/<name>/`
- **WHEN** it finishes the publish preparation
- **THEN** `skills/README.md`'s table contains a row for `<name>` matching the skill's purpose, and no second row for the same name exists.

### Behavior: Distribution stops at the review gate

The agent SHALL prepare the library for distribution but SHALL NOT run
`git add`, `git commit`, `git push`, or `dotagents install` itself: skills
distribute through dotagents resolving the library's GitHub remote at a
commit, so the agent SHALL print the exact commands to review, commit, push,
and install (`dotagents install`), name what each does, and stop for explicit
human approval.

#### Scenario: Skill is ready to distribute

- **GIVEN** the spec and SKILL.md validate and the README row exists
- **WHEN** the agent reaches the distribution step
- **THEN** it prints the `git add`/`git commit`/`git push` commands scoped to the new skill's paths and `dotagents install`, explains that install resolves the pushed commit and writes `agents.lock` plus the per-agent skills links, and performs none of them without an explicit go-ahead.

#### Scenario: User asks why install is not enough

- **GIVEN** the user asks to just run `dotagents install` without pushing
- **WHEN** the agent responds
- **THEN** it explains that dotagents resolves skills from the GitHub remote at a pinned commit, so an unpushed skill will not install, and offers the gate commands again.

### Behavior: Validation is reported honestly

The agent SHALL run `npx -y @sentry/skillet@latest validate` before declaring
the skill done and SHALL report every error; it SHALL author eval cases only
when asked, and when no eval harness (`codex` or `claude` CLI) is available it
SHALL report evals as authored-but-not-run instead of claiming they pass.

#### Scenario: Validation error remains

- **GIVEN** `validate` reports a spec or SKILL.md error
- **WHEN** the agent considers the skill complete
- **THEN** it fixes the error and re-validates, and does not present the skill as done while any error remains.

#### Scenario: Evals authored but no harness

- **GIVEN** the user asked for eval cases and no `codex` or `claude` CLI is on PATH
- **WHEN** the agent finishes
- **THEN** the final report states the cases were written and validated but not executed, rather than implying they pass.

## Constraints

### Constraint: No commits, pushes, or installs without approval

The agent MUST NOT run `git add`, `git commit`, `git push`, or
`dotagents install`; the review gate commands are its output, not its actions.

### Constraint: No ticket or PII content in fixtures

The agent MUST NOT copy content from `tickets/` or any other PII-tainted path
into skill specs, fixtures, or examples; fixtures are synthesized.

### Constraint: Never fabricate skillet formats

The agent MUST NOT write `spec.md`, `SKILL.md`, or eval case YAML from a
remembered format; `instructions spec|skill|evals` output is fetched for each
artifact, and `validate` gates every step.

<!-- skillet-version: 1.8.0 -->

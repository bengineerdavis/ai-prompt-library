# Backlog Task

## Intent

This skill makes the agent write backlog-md-py task records that a reader can
scan: deliverables as bullets under Ship, boundaries under Constraints, and a
done-definition that lives only in the acceptance-criteria block. It exists
because task files fail two ways in practice: a dense single paragraph buries
the deliverables, and the done-definition drifts across description, ACs, and
the Definition of Done section until no single source says what done means.

## Triggers

- **SHOULD** the user asks to create a backlog task in a backlog-md-py store (`backlog/` task files)
- **SHOULD** the user asks to draft, rewrite, or reshape a task's description or its acceptance criteria
- **SHOULD NOT** the user asks to close, claim, reassign, or transition a task — status and bookkeeping edits are not shape work
- **SHOULD NOT** the task store is not backlog-md-py (a different tracker or file format)

## Behaviors

### Behavior: CLI task creation

The agent SHALL create tasks with `uvx --from backlog-md-py backlog-py task create "<title>" --no-dod-defaults` and SHALL NOT hand-write the task file.

#### Scenario: new task from a request

- **WHEN** the user describes a piece of work and asks for a backlog task
- **THEN** the agent runs the create command with the title, reports the assigned id (for example APT-25), and no hand-written file appears under `backlog/tasks/`

### Behavior: description shape

The agent SHALL structure every task description as: a why of one or two factual sentences, then `Ship:` with one bullet per deliverable, then `Constraints:` with one bullet per boundary, then a dated one-sentence decision record when a decision exists.

#### Scenario: filling a new task's description

- **WHEN** the agent fills the description markers of a just-created task
- **THEN** the description block contains the why sentences, a `Ship:` bullet list, a `Constraints:` bullet list, and — only if a decision was made — a dated sentence such as "Agreed with the maintainer 2026-10-26: shape-first over tooling."

#### Scenario: sentence that fits no bullet

- **WHEN** the agent drafts a description sentence that names no deliverable
- **THEN** the agent moves it into the why or deletes it, and it does not appear as a Ship bullet

### Behavior: AC coverage

The agent SHALL give every Ship bullet exactly one matching acceptance criterion, and SHALL give each verification command (for example `mise run test`) its own criterion.

#### Scenario: three Ship bullets

- **WHEN** a description carries three Ship bullets and two verification commands
- **THEN** the AC block carries at least five criteria: one per bullet plus one per command, each with the `- [ ] #N` numbering

### Behavior: single done source

The agent SHALL keep the AC block the only done-definition: the DOD section stays empty unless the store's convention fills it, and the description carries no restatement of the ACs.

#### Scenario: done-definition drift

- **WHEN** the agent drafts a task whose stamping requirements appear in the DOD section
- **THEN** the agent moves them into the AC block as criteria and leaves the DOD block empty, matching the store's other tasks

### Behavior: marker contract preserved

The agent SHALL edit prose only inside section markers and SHALL confirm with `task_board` after any hand edit to a task file.

#### Scenario: reshaping an existing task's description

- **WHEN** the agent rewrites the description between the DESCRIPTION section's BEGIN and END marker comments
- **THEN** the frontmatter, marker comments, and `- [ ] #N` checklist lines are byte-identical, and `task_board` returns the new description text

### Behavior: repository rules carried in

The agent SHALL read the repository's steering docs (AGENTS.md, ai-rules) when the task touches them and SHALL carry the rules they name into the task's Constraints bullets.

#### Scenario: repo declares a skill-declaration rule

- **WHEN** the repo's ai-rules states that every referenced skill must be declared in `agents.toml` in the same change
- **THEN** the task that ships such a skill carries a Ship bullet and a matching AC for the declaration

## Constraints

### Constraint: marker frame is untouchable

The agent MUST NOT create, move, rename, or delete the section marker comments (`SECTION`, `AC:BEGIN`, `DOD:BEGIN`) or alter the `- [ ] #N` checklist format — backlog-py parses them, and a broken frame takes the task off the board.

### Constraint: no hand-written task files

The agent MUST NOT write a task file under `backlog/tasks/` by hand when the CLI can create it — hand-writing skips id assignment and the store's structure writer.

### Constraint: no unverified hand edits

The agent MUST NOT declare a hand edit to a task file complete before `task_board` confirms the store still parses the file and shows the edited text.

<!-- skillet-version: 1.8.0 -->

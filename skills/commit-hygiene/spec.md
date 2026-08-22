# Commit Hygiene

## Intent

This skill governs how work gets committed: what belongs in one commit, how much
prose that commit earns, and how to make sure the commit contains what its
message claims. It exists because commits drift in two directions at once — they
absorb unrelated changes until no single sentence describes them, and their
messages grow to cover the sprawl, so the message length that should have been a
warning becomes camouflage.

The discipline is proportionality plus verification. One logical change per
commit, a message whose detail matches the size and risk of that change, and a
check after committing that the contents are what was intended. A message longer
than the change warrants is not thoroughness; it is evidence the commit should
have been two, and the right response is to split rather than to keep writing.

## Triggers

- **SHOULD** apply whenever committing work, including the decision of how to
  divide finished changes into commits.
- **SHOULD** apply when the working tree holds more than one logical change, or
  when another process or session may be writing to the same repository.
- **SHOULD** apply when reviewing a commit or a proposed message for whether its
  scope and its prose match.
- **SHOULD NOT** apply to authoring pull request descriptions, release notes, or
  changelogs, which summarise many commits for a different audience.
- **SHOULD NOT** apply to rewriting already-published history; the rules here
  are for commits being created, and rebasing shared branches carries risks this
  skill does not weigh.

## Behaviors

### Behavior: One logical change per commit

The agent SHALL commit one logical change at a time, and SHALL split unrelated
changes into separate commits even when they were made in the same sitting.
A logical change is one whose subject line needs no "and".

#### Scenario: Two unrelated edits are ready at once

- **GIVEN** a working tree with a bug fix in `parser.py` and an unrelated
  dependency bump in `pyproject.toml`
- **WHEN** the agent is asked to commit the work
- **THEN** it creates two commits, each naming only its own change

#### Scenario: Splitting would break the intermediate state

- **GIVEN** a change that adds a configuration flag and the code that reads it,
  where the flag alone does nothing and the reader alone does not compile
- **WHEN** the agent commits the work
- **THEN** it keeps them in one commit, because atomic means self-contained
  rather than small

### Behavior: Commit contents are stated explicitly, not inherited

The agent SHALL name the paths it intends to commit on the `git commit` command
itself rather than relying on whatever is already staged, so that a concurrently
running process cannot contribute files to the commit.

#### Scenario: Another session has staged an unrelated file

- **GIVEN** a repository where `other.py` is already staged by another process,
  and the agent has just edited `mine.py`
- **WHEN** the agent commits its own work
- **THEN** the resulting commit contains `mine.py` and not `other.py`

### Behavior: Message detail is proportional to the change

The agent SHALL match the message to the change: a subject line alone for
mechanical edits, a sentence or two of rationale for small single-purpose
changes, and one to two short paragraphs for ordinary features and fixes. It
SHALL treat a body that keeps growing past roughly two hundred words as evidence
the commit is doing too much, and SHALL reconsider splitting before writing more
prose.

#### Scenario: A typo fix

- **WHEN** the agent commits a one-word spelling correction in a comment
- **THEN** the message is a subject line, with no explanatory body

#### Scenario: A substantial change wants a long message

- **GIVEN** a change that adds a subsystem and also refactors two callers and
  also fixes an unrelated lint error
- **WHEN** the agent finds itself writing a fourth paragraph to cover it
- **THEN** it splits the work into separate commits rather than continuing the
  message

### Behavior: The message explains why, not what

The agent SHALL use the body for the reasoning a reader cannot recover from the
diff — the problem, why this approach, any consequence worth warning about — and
SHALL NOT enumerate what the diff already shows, narrate the process that led to
the change, or list every case handled.

#### Scenario: A change adding several validators

- **GIVEN** a commit adding pattern validators whose names and behaviour are
  evident in the diff
- **WHEN** the agent writes the message
- **THEN** it states why validation was needed and what breaks without it,
  without listing each validator

### Behavior: Verify the commit after making it

The agent SHALL inspect what the commit actually contains after creating it, and
SHALL report a mismatch rather than assuming success.

#### Scenario: The commit captured the wrong files

- **GIVEN** a commit the agent has just created
- **WHEN** its file list does not match what the agent intended to commit
- **THEN** the agent says so explicitly instead of reporting the commit as done

## Constraints

### Constraint: Never split into commits that cannot stand alone

The agent MUST NOT create a commit that leaves the tree unbuildable or its tests
failing so that a following commit can repair it. That breaks `git bisect` and
makes every intermediate state a lie, which is worse than a slightly coarse
commit. Splitting is bounded by self-containment, not pursued for its own sake.

### Constraint: Never commit unrelated changes to reach a green state

The agent MUST NOT sweep unrelated modified files into a commit to make the tree
clean, and MUST NOT stage a directory wholesale when only some of its files
belong to the change.

### Constraint: Never let the message outgrow the change

The agent MUST NOT compensate for an overgrown commit by writing a longer
message. Message length is a scope signal, and burying a sprawling change under
thorough prose removes the only cue a reviewer had.

### Constraint: Never rewrite shared history to tidy up

The agent MUST NOT rebase, amend, or force-push commits that others may have
built on in order to correct scope or message problems, and MUST propose the
options instead when history is already wrong.

<!-- skillet-version: 1.7.0 -->

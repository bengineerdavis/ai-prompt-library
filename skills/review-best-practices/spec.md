# Review Best Practices

## Intent

This is a research skill, and its output is an input to planning. It runs before
a decision is made — about a tool, a process, a format, an approach — and its job
is to find what already exists: a standard, a tool, a documented practice, a
convention the community converged on, and what practitioners quietly stopped
doing. Planning then works from findings rather than from invention.

Its purpose is to make an existing answer the default and a custom one the
exception, taken only when the search comes back empty or nothing fits.

It exists because building is more satisfying than searching, and because an
agent asked to solve a problem will usually solve it rather than ask whether it
is already solved. The result is a bespoke mechanism where a well-tested one
existed, carrying maintenance nobody budgeted for and lacking every affordance
the community version accumulated.

"Best practices" in the name is a description of what is searched for, not a
standard of proof. What most people do is evidence about options, never evidence
about fit — which is why ranking here is against the stated requirement and the
constraints below forbid treating adoption as an argument.

The discipline is search, then evaluate against the actual requirement, then
decide with the rejected options recorded. The last part matters as much as the
first: a decision to build that does not say what was rejected and why is
indistinguishable from never having looked, and the next person re-runs the same
search or, worse, does not.

Reinventing is sometimes right. This skill is not a prohibition on building. It
is a prohibition on building *by default*, without having looked.

## Triggers

- **SHOULD** run before a planning stage that will commit to an approach, so
  the plan is built from findings rather than from invention.
- **SHOULD** pair with `interaction-questioning`, which establishes what is
  actually being attempted. Questioning pins the requirement; this skill ranks
  options against it. Running this first produces a ranking against a
  requirement nobody confirmed.
- **SHOULD** apply before building any mechanism, tool, format, or process that
  is plausibly a solved problem — templating, dependency management, testing
  strategy, release process, configuration, permissions, documentation
  structure.
- **SHOULD** apply when adopting a practice or convention, to check what the
  community already does and what it stopped doing.
- **SHOULD** apply when a claim about an external tool's capability is load
  bearing for a decision, since an unverified capability claim and a missing
  search are the same failure wearing different clothes.
- **SHOULD NOT** apply to work whose whole value is that it is specific — a
  project's own domain logic, its own data, its own requirements.
- **SHOULD NOT** apply where a dependency is itself the cost being avoided, such
  as a deliberately zero-dependency script; state that constraint and skip the
  search rather than performing it and ignoring the result.
- **SHOULD NOT** become a reason to defer. A time-boxed search that finds
  nothing is a completed search, and the work proceeds.

## Behaviors

### Behavior: Search before deciding

The agent SHALL search for existing solutions before recommending an approach,
and SHALL NOT present a custom design as the first option for a problem that is
plausibly already solved.

The search SHALL cover more than one kind of source: established tools, relevant
standards or specifications, and what practitioners actually report doing. One
source answering does not end the search, because each of those three is blind
to different things.

#### Scenario: A task asks for a mechanism that sounds generic

- **GIVEN** a request to build something like a templating system, a plugin
  loader, or a config resolver
- **WHEN** the agent begins work
- **THEN** it searches for existing options first and reports what it found,
  including the ones it will not recommend

#### Scenario: The search returns nothing usable

- **WHEN** a time-boxed search finds no fitting option
- **THEN** the agent says so explicitly and proceeds to build. A search that
  found nothing is a result, and recording it prevents the next person repeating
  it

### Behavior: Evaluate against the stated requirement, not popularity

The agent SHALL rank candidates against the requirement actually given, and
SHALL NOT recommend an option on the basis of adoption, familiarity, or
recency alone.

Where the requirement includes a capability most candidates lack, that
capability SHALL be ranked first, because it is what eliminates.

#### Scenario: A popular tool lacks the one required capability

- **GIVEN** a requirement to update generated projects after the template
  changes
- **WHEN** the most widely used tool cannot do that
- **THEN** it is ranked below a less popular tool that can, and the report says
  plainly that popularity was not the criterion

#### Scenario: An incumbent is already in use

- **GIVEN** a tool already installed or already used in the project
- **WHEN** alternatives are evaluated
- **THEN** the incumbent is treated as the baseline to beat rather than the
  default to keep, and the report says what would have to be true for a switch
  to be worth its cost

### Behavior: Verify capability claims against the artifact

The agent SHALL confirm a claimed capability against the tool itself — its
source, its help output, or a run — and SHALL NOT rely on recollection when the
claim is load bearing.

#### Scenario: A capability is asserted from memory

- **WHEN** the agent is about to state that a tool supports something
- **THEN** it checks. Recollection of a fast-moving tool's feature set is a
  guess with good grammar, and a wrong one sends the whole design down a path
  the tool cannot follow

#### Scenario: A verified check contradicts the expectation

- **WHEN** the artifact disagrees with what the agent expected
- **THEN** the correction is recorded where the claim was made, not only
  mentioned. A claim already written down and later disproved is corrected in
  place

### Behavior: Return findings that invalidate the requirement

Where the search shows the stated requirement is mis-framed, self-contradictory,
or already satisfied, the agent SHALL say so and send the question back, and
SHALL NOT quietly pick the least-bad option against a requirement that does not
hold.

Research is the cheapest place to discover that a plan does not fit its goal.
Every later place costs more.

#### Scenario: Every candidate fails the stated requirement

- **GIVEN** a requirement that no available option satisfies
- **WHEN** the ranking comes back with nothing above the bar
- **THEN** the agent reports that the requirement itself needs revisiting rather
  than recommending the closest miss. A ranking of options that all fail reads
  as a recommendation and is not one

#### Scenario: The goal turns out to be already met

- **WHEN** the search finds the outcome is already achieved by something in
  place
- **THEN** the agent says so instead of recommending a replacement. The
  requirement was for an outcome, not for a new component

### Behavior: Record what was rejected

The agent SHALL record the options considered and the reason each was not
chosen, alongside the decision.

#### Scenario: A custom solution is chosen after a search

- **WHEN** the agent concludes that building is correct
- **THEN** the record names what was evaluated and what disqualified each
  option. Without it the decision cannot be revisited when a rejected option
  improves, and it is indistinguishable from never having searched

## Constraints

### Constraint: A search is not a substitute for a decision

The agent MUST NOT return a survey of options in place of a recommendation. The
deliverable is a decision with its reasoning, not a list for someone else to
work through.

### Constraint: Adoption is not evidence of fit

The agent MUST NOT treat popularity, star counts, or the fact that a tool is
already installed as evidence that it meets the requirement.

<!-- skillet-version: 1.7.0 -->

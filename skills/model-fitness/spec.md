# Model fitness

## Intent

This skill decides whether a model is fit for a *named role*, and produces a
verdict backed by numbers the deciding machine measured itself.

It exists because model selection is unusually easy to do badly while feeling
rigorous. A release lands with a benchmark table, the numbers are real, and they
answer a question nobody here asked — on other hardware, at another quantisation,
for a task the role does not perform. The result is a confident choice that
cannot be defended six months later, and cannot be re-derived because nobody
recorded what "better" meant.

It owns the judgement — what to measure, per role, and what a result licenses.
It does not own the harness that produces raw timings, nor the decision to adopt,
which stays a human commit.

## Triggers

- **SHOULD** apply when a candidate model has passed triage and needs evidence
  before adoption.
- **SHOULD** apply when an incumbent is suspected of regressing after a runtime
  or quantisation change.
- **SHOULD NOT** apply to choosing a judge model — that is a calibration
  question with its own harness, and importing its scores is the specific error
  this skill exists to prevent.
- **SHOULD NOT** apply to ranking models in the abstract. A ranking without a
  role is not a finding.

## Behaviors

### Behavior: Measure per role, never across roles

The agent SHALL evaluate a model only for roles it is a candidate for, and SHALL
report results per role. The agent SHALL NOT combine per-role results into an
overall score, and SHALL NOT use a result from one role as evidence for another.

#### Scenario: Candidate measured well on one role, proposed for a second

- **WHEN** a model scores well as a chat candidate and someone proposes it for
  the code role on that basis
- **THEN** the agent states that no code-role evidence exists and either runs the
  code-role cases or reports the role as unmeasured — it does not transfer the
  chat result

### Behavior: State the measurement beside every claim

The agent SHALL attach, to each quality claim, the case that produced it, the
date, and the machine conditions that affect it — model tag, quantisation,
context, and whether anything else was resident. A claim without those is a
recollection, not a result.

#### Scenario: Reporting a comparison

- **WHEN** reporting that a candidate beat an incumbent
- **THEN** the report names the cases, the date, both exact tags, and the
  conditions — not "faster and better at following instructions"

### Behavior: Report unmeasured dimensions as unmeasured

The agent SHALL name the dimensions it did not measure, rather than omitting
them. A recommendation SHALL be marked provisional when any dimension material
to the role is unmeasured, and the marker SHALL say which one.

#### Scenario: Speed measured, quality not

- **WHEN** a candidate is faster and smaller but no quality case has been run
- **THEN** the recommendation says so explicitly and is marked provisional,
  rather than presenting the speed result as a fitness verdict

### Behavior: Invalidate runs whose conditions differ

The agent SHALL record harness conditions and SHALL treat a run as
non-comparable when they differ from the run it is compared against — a
different context length, quantisation, runtime version, or a model already
resident. The agent SHALL re-run rather than reconcile.

#### Scenario: Another model was loaded during the run

- **WHEN** the harness records that a second model was resident, so timings
  reflect contention
- **THEN** the run is discarded and repeated, because a slow result here is
  indistinguishable from a slow model

### Behavior: Prefer mechanical checks to judged ones

For each property, the agent SHALL use a mechanically decidable check where one
exists — schema conformance, exact-match recall, well-formed tool calls — and
SHALL reserve model-judged scoring for properties with no mechanical form. Where
judging is unavoidable, the agent SHALL report it as judged.

#### Scenario: Checking instruction adherence

- **WHEN** testing whether a model respects a requested output shape
- **THEN** the case requests a shape a script can validate, and the check
  validates it, rather than asking a model whether the shape looks right

### Behavior: Grow coverage from blocked decisions, not from symmetry

The agent SHALL add a property or role to the matrix when a decision could not
be made without it, and SHALL NOT fill the matrix for completeness. Coverage
starts at the smallest useful set and grows on demand.

#### Scenario: A role has no cases and no pending decision

- **WHEN** the matrix covers chat and code, and no candidate exists for the
  vision role
- **THEN** the agent leaves vision uncovered and records it as a known gap,
  rather than authoring cases nothing is waiting on

### Behavior: Source cases by provenance, not by convenience

Eval cases SHALL be synthesised — written from general understanding of a
problem class. The agent SHALL NOT create a case by transforming real work
material, including by replacing names or identifiers, because scrubbing changes
what is recognisable and not where the case came from.

When real usage reveals an uncovered problem class, the agent SHALL prompt for a
synthesised case describing that class, and SHALL NOT copy the material that
prompted it.

#### Scenario: A real interaction exposes a gap

- **WHEN** a live task shows the model mishandling a class of input for which no
  case exists
- **THEN** the agent describes the class and asks for a case to be written from
  understanding, rather than saving the transcript as a fixture

## Constraints

### Constraint: Published benchmarks are not evidence

The agent MUST NOT cite a model card, announcement, leaderboard, or its own
recall as evidence of fitness. Those may motivate a candidate; they may not
support a verdict.

### Constraint: No cross-task score transfer

The agent MUST NOT promote a model on a measurement taken for a different task,
including judge-calibration scores used as generation evidence.

### Constraint: No unmeasured superlatives

The agent MUST NOT describe a model as better, best, or improved on a dimension
it has not measured on the deciding machine.

<!-- skillet-version: 1.7.0 -->

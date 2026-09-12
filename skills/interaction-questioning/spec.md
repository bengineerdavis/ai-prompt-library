# Interaction Questioning — Specification

## Intent

Define the observable behavior of the `interaction-questioning` skill. The skill helps an agent discover, clarify, stress-test, and confirm a user’s real goal efficiently, without assuming the user knows all relevant requirements or expecting perfect information before acting.

The spec treats questioning as one possible next move among research, explanation, expectation calibration, safe defaults, planning, direct answers, and escalation. It requires a plain-English understanding confirmation once discovery is good enough and preserves reusable learning signals from questions and outcomes.

## Triggers

- **SHOULD** trigger when a user request is ambiguous, exploratory, incomplete, internally inconsistent, materially constrained, high-stakes, or likely to involve unknown unknowns.
- **SHOULD** trigger when another active task skill needs a better goal, scope, audience, constraint, provider target, decision criterion, or output shape.
- **SHOULD** trigger when the user’s stated request may be instrumental to a broader outcome and the distinction could materially change the work.
- **SHOULD NOT** trigger a user-facing question merely because a detail is absent.
- **SHOULD NOT** trigger when research can resolve the gap, a safe low-risk default is available, the request is already actionable, or a question would add more friction than value.

## Behaviors

### Behavior: Natural-language-first discovery

The skill SHALL accept an ordinary user request as a valid starting point. It SHALL NOT require the user to complete an intake form, know specialist vocabulary, or explicitly state that they lack domain knowledge before discovery begins.

#### Scenario: Novice service request

- **GIVEN** a user says, “I need someone to help with a problem in my house”
- **WHEN** the skill is active
- **THEN** it first orients to plausible service categories and identifies one high-value next move rather than asking the user to provide a complete technical scope.

#### Scenario: User provides a detailed brief

- **GIVEN** a user supplies goal, deadline, constraints, and preferred output
- **WHEN** the skill is active
- **THEN** it recognizes the request as already actionable and does not force redundant discovery questions.

### Behavior: Two-sided understanding

The skill SHALL consider both user-understanding gaps and agent-understanding gaps before committing to a solution.

- A user-understanding gap is a relevant factor, option, risk, or term the user would not reasonably know to mention.
- An agent-understanding gap is a fact about the user’s situation, constraints, priorities, or environment that cannot be safely inferred.

#### Scenario: User does not know a category-specific risk

- **GIVEN** a user asks for a provider in an unfamiliar category
- **WHEN** material method or asset risks may exist
- **THEN** the skill identifies those risks internally and either researches, explains, defaults, or asks one focused question as appropriate.

#### Scenario: Private constraint matters

- **GIVEN** selecting a provider depends on whether an item can be transported
- **WHEN** public research cannot answer that fact
- **THEN** the skill may ask one plain-language question about transport/access instead of guessing.

### Behavior: Goal stack and contribution framing

The skill SHALL distinguish the initial request, session task, underlying outcome, and session contribution.

#### Scenario: Instrumental request

- **GIVEN** a user asks, “Compare three providers”
- **WHEN** surrounding context shows the user ultimately needs to choose a reliable provider without making a costly mistake
- **THEN** the skill treats comparison as the session task and provider selection confidence as the underlying outcome.

#### Scenario: Misframed request

- **GIVEN** a requested action is unlikely to achieve the likely outcome
- **WHEN** the mismatch is material
- **THEN** the skill explains the tradeoff constructively and offers a better framing or one goal-shaping question.

#### Scenario: Aligned request

- **GIVEN** the initial request directly serves a clear, low-risk outcome
- **WHEN** no material goal gap exists
- **THEN** the skill proceeds without unnecessary goal confirmation.

### Behavior: Unknown classification

The skill SHALL classify missing information as decision-changing, helpful later, safe-default, research-resolvable, or noise.

#### Scenario: Research-resolvable unknown

- **GIVEN** the user needs a current public fact
- **WHEN** credible research can answer it
- **THEN** the skill researches before asking the user.

#### Scenario: Safe default

- **GIVEN** a missing preference has low downside and a reasonable default exists
- **WHEN** the next action remains useful under that default
- **THEN** the skill states or records the default and proceeds.

#### Scenario: Noise

- **GIVEN** a detail would not change the next decision or output
- **WHEN** it is missing
- **THEN** the skill does not ask for it.

### Behavior: Stakes-sensitive depth

The skill SHALL scale discovery depth to reversibility, harm, financial/time commitment, uncertainty, downstream dependency, and user vulnerability.

#### Scenario: Low-stakes request

- **GIVEN** a low-risk request with a clear likely answer
- **WHEN** a minor preference is missing
- **THEN** the skill uses a safe default or asks at most one high-value question.

#### Scenario: High-stakes ambiguity

- **GIVEN** a costly, safety-sensitive, legally consequential, or difficult-to-reverse decision
- **WHEN** material facts are unknown
- **THEN** the skill surfaces relevant risks, asks focused questions as needed, states uncertainty, and recommends qualified help where appropriate.

### Behavior: Next-move routing

The skill SHALL decide whether a question, research, explanation, expectation calibration, safe default, plan, answer, or escalation is the best next move.

#### Scenario: Vocabulary gap

- **GIVEN** the user cannot reasonably answer a technical question without context
- **WHEN** that information matters
- **THEN** the skill explains the distinction in plain language before asking a simplified question, if a question remains necessary.

#### Scenario: Enough information

- **GIVEN** the current information supports a useful decision or plan
- **WHEN** remaining unknowns are low risk or deferrable
- **THEN** the skill gives the plan instead of asking another question.

### Behavior: One-question user interface

The skill SHALL ask no more than one user-facing question at a time.

#### Scenario: Multiple material unknowns

- **GIVEN** several unknowns could matter
- **WHEN** the skill must seek user input
- **THEN** it selects the highest-value question, waits for the answer, updates the internal map, and only then chooses another question if needed.

### Behavior: Question selection

The skill SHALL choose questions based on decision impact, unknown-unknown value, stakes reduction, goal alignment, research leverage, and user burden/question fatigue.

#### Scenario: Goal clarification versus implementation detail

- **GIVEN** one question would clarify the underlying outcome and another would clarify a low-level preference
- **WHEN** the outcome answer could change the provider type or plan
- **THEN** the skill asks the goal-shaping question first.

### Behavior: Constructive expectation calibration

The skill SHALL surface material conflicts among desired quality, budget, timeline, safety, method, certainty, or evidence without overriding the user’s agency.

#### Scenario: Incompatible expectations

- **GIVEN** research indicates that speed, lowest price, and specialist quality are unlikely to coexist
- **WHEN** the tradeoff affects the recommendation
- **THEN** the skill states the user’s goal respectfully, explains the tradeoff plainly, and offers an adjustment, option, or one focused question.

### Behavior: Good-enough stopping and question-fatigue protection

The skill SHALL stop discovery once the likely outcome, session contribution, material constraints, and next action are clear enough. It SHALL NOT seek perfect information.

#### Scenario: Repeated questioning

- **GIVEN** the user has answered several questions and remaining details are helpful later
- **WHEN** further questioning is less valuable than action
- **THEN** the skill summarizes known facts and assumptions, proceeds with the best plan, and defers low-value questions.

#### Scenario: More-than-seven threshold

- **GIVEN** more than seven user questions appear necessary
- **WHEN** the skill has not reached a good-enough threshold
- **THEN** it explains why, summarizes what is known, and asks permission before continuing.

### Behavior: Understanding confirmation

Before handing work to another task skill or completing a decision, the skill SHALL reflect its understanding in plain English using the format required by active task/project context when one exists.

The confirmation SHALL include, as relevant: immediate problem, underlying outcome, session contribution, key constraints/priorities, material assumptions/open items, and concrete next action.

#### Scenario: Clear low-risk request

- **GIVEN** goal and next action are clear with low correction risk
- **WHEN** discovery completes
- **THEN** the skill briefly states its understanding and proceeds without requiring confirmation.

#### Scenario: Material correction risk

- **GIVEN** a mistaken goal interpretation would materially change the work
- **WHEN** discovery completes
- **THEN** the skill gives a concise understanding summary and asks a yes/no confirmation.

#### Scenario: Context-specific summary

- **GIVEN** an active task or project requires a defined format such as incident framing, procurement summary, or meeting minutes
- **WHEN** understanding confirmation is needed
- **THEN** the skill uses that format without duplicating the same summary in generic prose.

### Behavior: Correction recovery

The skill SHALL treat direct rejection, partial correction, redirection, and frustration as signals to update its inferred goal without discarding useful prior context.

#### Scenario: User says “not quite”

- **GIVEN** the skill states an inferred goal
- **WHEN** the user says “not quite; what I really need is…”
- **THEN** the skill retains still-relevant constraints, updates the goal stack, and asks the smallest question needed to restore alignment.

### Behavior: Advisor composition

In multi-agent or panel settings, advisors MAY propose unknowns, safe defaults, and candidate questions, but the questioning skill SHALL select the single user-facing question, if any.

#### Scenario: Service-provider panel

- **GIVEN** a domain specialist, deep researcher, pragmatist, and provider-due-diligence advisor identify several unknowns
- **WHEN** the panel needs user input
- **THEN** the questioning skill asks only the one question with the highest decision value and records the rest as research/default/deferred items.

### Behavior: Learning handoffs

The skill SHALL preserve reusable learning candidates when questions or answers reveal recurring blind spots, unsafe assumptions, useful defaults, missing skills/roles/templates, or repeated gaps between initial request and underlying outcome.

#### Scenario: Repeated service-purchase blind spot

- **GIVEN** several sessions show that buyers do not know to distinguish a base service from optional specialty work
- **WHEN** the pattern changes decision quality
- **THEN** the Note-Taker records a learning handoff that identifies the observed gap, useful question/default, outcome, and proposed artifact target.

## Constraints

### Constraint: No hidden interrogation

The skill MUST NOT expose a long internal tree or transform unknown-unknown discovery into a required form unless the user explicitly requests deep trace or exhaustive intake.

### Constraint: No fake certainty

The skill MUST NOT present assumptions, vendor claims, plausible inferences, or incomplete research as established fact.

### Constraint: No goal overreach

The skill MUST NOT replace a user’s stated request with a more ambitious inferred goal without evidence that the distinction is material and without preserving the useful part of the request.

### Constraint: No unnecessary confirmation gate

The skill MUST NOT demand a user reply after understanding confirmation when correction risk is low and the next action is clear.

### Constraint: Plain-language default

The skill MUST NOT expect the user to understand technical terms that have not first been defined in plain language.

### Constraint: Active-context precedence

The skill MUST NOT override task-, project-, safety-, or output-format instructions that specify a different confirmation format, risk protocol, or decision process.

## Acceptance Criteria

The skill is complete only when:

- all behaviors above are represented in `SKILL.md`;
- eval cases cover each behavior and key constraint;
- the rendered skill preserves one-question interaction, safe defaults, good-enough stopping, and understanding confirmation;
- the skill can start from a natural-language request without demanding domain expertise; and
- validation/evaluation through the current Skillet CLI completes without errors or uncovered-behavior warnings.

<!-- skillet-version: 1.4.1 -->

# News Intelligence

## Intent

Help a person understand a supplied news item or current claim, check what is true when needed, and decide whether anything practical should change. The skill cuts through hype, marketing, political framing, and misinformation without treating skepticism, research volume, or action as goals in themselves.

Success is the smallest reliable result that answers the user's actual question. It must be responsive, traceable, calibrated, supported by good-faith due diligence, and proportionate to the cost of being wrong. The agent must be able to give a concise decision record for any important conclusion if asked.

## Triggers

- **SHOULD** apply when the user asks to digest, interpret, verify, investigate, or act on news, a headline, a public event, or a consequential commercial or industry claim
- **SHOULD** apply when the user asks whether a current development matters to them or what to monitor, prepare for, defer, or ignore
- **SHOULD NOT** turn a clear request to summarize supplied material into independent research or personal advice unless either is needed to prevent meaningful misinterpretation
- **SHOULD NOT** run proactively without a user-supplied topic, claim, source, or decision
- **SHOULD NOT** replace emergency authorities or individualized medical, legal, tax, or investment advice

## Behaviors

### Behavior: Match the task

The agent SHALL identify whether the user needs a digest, interpretation, verification, practical assessment, or deeper investigation, and perform only the stages needed to answer responsibly. It SHALL infer context when safe and ask one focused question only when the answer could materially change the work or conclusion.

#### Scenario: Clear article summary

- **GIVEN** the user supplies a clear article and asks only for a summary
- **WHEN** independent verification is not needed to prevent meaningful misinterpretation
- **THEN** the agent gives a faithful concise digest without adding a fact-check, action plan, or ritual caveats

#### Scenario: Decision-critical ambiguity

- **GIVEN** jurisdiction or personal exposure could change practical advice and cannot be inferred safely
- **WHEN** the user asks what to do
- **THEN** the agent asks one focused question before making the affected recommendation

### Behavior: Check runtime and handle failure

Before making a current or source-grounded claim, the agent SHALL check whether it can access current information and inspect needed sources. If a material source or tool fails, it SHALL attach the gap to the affected claim, try an equivalent source or narrower conclusion, and ask for approval before using a fallback that could materially change the conclusion or lower the required evidence standard.

#### Scenario: Material source cannot be fetched

- **GIVEN** a search result points to the only source supporting a claim that would change the advice
- **WHEN** the full source cannot be inspected
- **THEN** the agent treats the snippet as a lead rather than verification, states what cannot be checked and why it matters, proposes a fallback, and waits for approval before relying on a materially weaker plan

#### Scenario: Independent evidence survives a failure

- **GIVEN** one source fails but accessible direct evidence and independent reporting still support the same narrow conclusion
- **WHEN** the agent evaluates the remaining evidence
- **THEN** it may proceed while attaching the source limitation to the affected claim and avoiding unsupported scope

### Behavior: Perform due diligence

For every conclusion that could change what the user believes, chooses, spends, or does, the agent SHALL define and meet an evidence threshold suited to the stakes, urgency, reversibility, and downside of error. It SHALL examine origin, access, method, scope, date, incentives, relevant counterevidence, and corroboration; distinguish no evidence from weak or conflicting evidence; and test whether removing one external source changes the conclusion.

#### Scenario: Consequential single-source claim

- **GIVEN** an uncorroborated external claim is the only support for a costly or irreversible action
- **WHEN** the agent tests the conclusion without that source
- **THEN** it labels the claim single-source, does not use it as the sole basis for the action, and states what evidence would reopen the decision

#### Scenario: No evidence differs from contradiction

- **GIVEN** one claim has not been checked because evidence is unavailable and another has been checked against contrary evidence
- **WHEN** the agent reports their status
- **THEN** it labels the first as no evidence or unverified and the second as contradicted rather than merging both into uncertain

### Behavior: Examine media and framing

For a media source that materially affects the answer, the agent SHALL examine sourcing and corrections, headline-to-body fit, political orientation, ownership, sponsorship, audience and access incentives, personal or institutional motivations, omissions, and independent support. It SHALL use these as signals for added scrutiny, not as proof that a claim is true or false.

#### Scenario: Partisan outlet reports a checkable fact

- **GIVEN** a politically aligned outlet reports a factual claim supported by a direct record
- **WHEN** the agent evaluates the claim
- **THEN** it checks the record and relevant framing without rejecting the fact solely because of the outlet's political orientation

#### Scenario: Accurate fact with misleading frame

- **GIVEN** a headline uses a narrow true fact to imply broader scope, certainty, causation, or urgency than the article and evidence support
- **WHEN** the agent explains the item
- **THEN** it states the narrow fact, identifies the framing gap, and does not repeat the stronger implication as established

### Behavior: Assess practical effect

When the user asks what a development means for them, the agent SHALL identify a realistic path by which it could affect their safety, rights, money, work, health, travel, household, or digital life. It SHALL recommend action, reversible preparation, monitoring, deferral, escalation, or no action only when the evidence and exposure justify it; for a material decision it SHALL explain why plausible alternatives were not chosen and what would change the result.

#### Scenario: Dramatic event without exposure

- **GIVEN** a verified dramatic event has no realistic path to affect the user's situation or decision
- **WHEN** the user asks what to do
- **THEN** the agent recommends no action or limited monitoring, explains why stronger responses are not justified, and names a concrete trigger for reconsideration

#### Scenario: Plausible exposure under uncertainty

- **GIVEN** credible evidence shows a plausible personal exposure but important uncertainty remains
- **WHEN** a low-cost reversible precaution limits downside
- **THEN** the agent may recommend that precaution while deferring costly or irreversible action

### Behavior: Preserve provenance and traceability

The agent SHALL make the origin of every important point clear as user context, source finding, supplied-source claim, or agent assessment. It SHALL introduce an inferred concern as a counterpoint or implication rather than as something the user said, and SHALL make decision-bearing claims traceable to inspectable sources. If it uses `S#`, `C#`, or `A#` identifiers, it SHALL include a short legend in the same response and ensure every identifier resolves.

#### Scenario: Agent introduces a stronger counterpoint

- **GIVEN** the user expresses a nuanced view that implies a useful opposing concern
- **WHEN** the agent raises that concern
- **THEN** it introduces it as a counterpoint or implication, explains its relevance briefly, and does not place an invented user position in quotation marks

#### Scenario: Lightweight claim identifiers

- **GIVEN** several material claims and assessments need cross-referencing
- **WHEN** the agent uses source, claim, and assessment identifiers
- **THEN** it includes `Legend: S = source; C = claim or interpretation; A = assessment` near first use and every cited identifier resolves to its source or basis

### Behavior: Validate the outcome

Before responding, the agent SHALL test whether the result answers the user's real question, contains enough checking for the stakes, makes important origins and evidence clear, survives meaningful counterevidence and source-removal tests, adds only useful caveats, and supports any action or no-action advice. It SHALL repair a material failure or disclose the narrow gap and smallest next step. If asked why, it SHALL provide a concise decision record covering the evidence threshold, checks performed, sources or alternatives weighted or rejected, stopping reason, remaining limits, and reopening trigger.

#### Scenario: Research answers the topic but not the decision

- **GIVEN** the draft accurately describes an event but the user asked whether to change a practical plan
- **WHEN** the agent performs its final check
- **THEN** it adds the missing exposure and decision analysis or states the user context needed rather than returning only the event summary

#### Scenario: User asks why

- **GIVEN** the agent has made an important conclusion or recommendation
- **WHEN** the user asks why it trusted the evidence or stopped researching
- **THEN** it gives a concise, auditable decision record without exposing private chain-of-thought

## Constraints

### Constraint: No false verification

The agent MUST NOT present an unread source, search snippet, repeated source chain, source reputation, political rating, or its own assessment as verified evidence.

### Constraint: No invented voice

The agent MUST NOT fabricate a quotation or present an inferred, simplified, or adversarial version of the user's position as user-stated.

### Constraint: No hidden downgrade

The agent MUST NOT silently lower the evidence standard, hide a material source failure, force a conclusion when evidence is insufficient, or let a single uncorroborated external source solely support consequential advice.

### Constraint: No embedded personal data

The reusable skill and references MUST NOT embed a user's location or other personal information; runtime context may be inferred or requested only when needed for the current task.

<!-- skillet-version: 1.8.0 -->

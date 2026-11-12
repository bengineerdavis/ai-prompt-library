# Support Partner Deep Research

## Intent

Investigate a reported customer issue interactively, from intake through evidence gathering, hypothesis testing, and ranked resolution, and emit a machine-readable investigation summary plus a rendered Markdown report. The skill exists because support diagnosis fails in two directions: jumping to a fix before the problem is validated, and circling without eliminating hypotheses. Both share a root cause — treating inference as evidence. This skill forbids that substitution: an unknown is a question to ask or a stated gap, never a guess, and every conclusion carries its evidence and a stated confidence.

Investigation material is the highest-PII-density content in the support workflow — raw logs, stack traces, configuration, and customer identifiers. No diagnostic model sees raw input: the skill pseudonymizes attachments through the `context-anonymizer` engine, then redacts with the fail-closed layers, so the diagnostic model reasons over faithful but pseudonymous text. Heavy diagnosis may run on a powerful frontier model only downstream of the engine's judge gate, with the residual re-identification risk disclosed; material that may never leave the host stays on the local-only path. A detector pass over the emitted summary is the last step before anything leaves. The skill ends at a resolution path or a named handoff; it detects when escalation is warranted but never writes the escalation ticket itself.

## Triggers

- **SHOULD** apply when the user asks to diagnose, investigate, troubleshoot, or figure out why a reported issue is happening.
- **SHOULD** apply when the user supplies a customer issue, log, stack trace, or support thread and asks for a root cause or a resolution path.
- **SHOULD** apply when the user asks to rank candidate fixes for an issue by feasibility, risk, and impact.
- **SHOULD NOT** apply when the user wants an open-ended research question answered or a landscape surveyed — that is `research`, which ends at a report and never diagnoses a bug.
- **SHOULD NOT** apply when the user wants an escalation ticket or handoff message written — that is `support-escalation` or `escalation-writing`; this skill only detects that escalation is warranted and hands off.
- **SHOULD NOT** apply to a product or documentation question that happens to mention a customer, where no issue is being investigated.

## Behaviors

### Behavior: Script owns the pipeline

The agent SHALL run the investigation as a terminal script that owns the stage order — read input, parse and redact, gather evidence, form hypotheses, test, rank solutions, emit summary — and SHALL invoke the model only for the judgment steps through a role resolved by `ollama-role`, never a hardcoded model tag. The script SHALL enforce ordering, the privacy gate, and rendering in code; the agent skill that wraps it SHALL NOT re-implement that logic.

#### Scenario: An agent reaches for the investigation

- **WHEN** an agent with the `SKILL.md` loaded is asked to diagnose a reported issue
- **THEN** it invokes the investigation script rather than improvising the phase order in prose, and the model tag it uses comes from role resolution, not a literal in the skill text

### Behavior: Input is parsed by detected type with override

The agent SHALL sniff the input's type from a fixed set — support thread or plain text, JSON or JSONL, log or stack trace, HAR, and configuration — select a streaming parser for that type, and honor an explicit `--type` override when sniffing is wrong. An unknown type SHALL fall back to plain text with a note on stderr, never a silent guess.

#### Scenario: HAR input is parsed as HAR

- **WHEN** the user supplies `attachments/dirty/sentry.io.har` without a `--type` flag
- **THEN** the script detects a HAR, streams it through the HAR parser, and does not treat it as opaque text

#### Scenario: Unknown type is announced, not guessed

- **WHEN** the input matches none of the known types
- **THEN** the script processes it as plain text and says so on stderr

### Behavior: Anonymize then redact before the model

The agent SHALL pseudonymize raw input through the `context-anonymizer` engine, then apply the fail-closed redaction layers, before any diagnostic model call, so the diagnostic model receives only pseudonymous, redacted text. The agent SHALL hold the real→substitute mapping in the calling process and SHALL NOT send it to any model or write it to any artifact. Anonymization and redaction SHALL preserve the technical literals the diagnosis depends on — error strings, version numbers, timestamps.

#### Scenario: Raw log with an email and a name

- **WHEN** a log containing `jane.smith@example.com` and the name `Jane Smith` is supplied
- **THEN** the engine substitutes a realistic name and email before redaction, the mapping stays in the calling process, and the diagnostic model never receives the real values

#### Scenario: Anonymization that eats evidence fails

- **WHEN** anonymization or redaction removes or alters an error string, version number, or timestamp that the diagnosis depends on
- **THEN** the run is treated as failed rather than allowed to proceed on degraded evidence

### Behavior: Output passes a detector backstop

The agent SHALL re-run the deterministic detectors over the final investigation summary before emitting it, guarding against the model re-resolving a placeholder into a live identifier, and SHALL fail closed — emitting nothing — on a high-confidence hit.

#### Scenario: Model re-resolves a placeholder

- **WHEN** the model's summary replaces a `[HOME]` placeholder with a real filesystem path
- **THEN** the backstop detects the path, the run exits non-zero, and no summary is written

### Behavior: Frontier handoff is downstream of the gate and disclosed

The agent MAY run heavy diagnosis on a powerful frontier model only when the input has passed the `context-anonymizer` judge gate, and SHALL disclose that the material is pseudonymous and that distinctive context may still re-identify the subject. When the material may never leave the host, the agent SHALL keep diagnosis on the local-only path and SHALL NOT make a frontier call.

#### Scenario: Operator allows a frontier diagnosis

- **WHEN** the operator permits a powerful hosted model and the attachment has passed the judge gate
- **THEN** the diagnosis runs on the frontier model over pseudonymous text, the handoff discloses the residual re-identification risk, and the mapping never leaves the calling process

#### Scenario: Material may not leave the host

- **WHEN** the issue material may never leave the host
- **THEN** diagnosis stays on the local path and no frontier call is made, regardless of operator convenience

### Behavior: Mis-invocation is refused loudly

The agent SHALL reject duplicate input or output flags, and SHALL refuse to read stdin when stdin is a terminal and no input was supplied, printing the reason on stderr and exiting non-zero instead of hanging.

#### Scenario: Output flag used for the input path

- **WHEN** the user runs the script with the input path passed to the output flag and no input flag, from a terminal
- **THEN** the script reports that no input was supplied and stdin is a terminal, and exits non-zero rather than waiting on stdin

### Behavior: Phased diagnosis with ranked hypotheses

The agent SHALL validate the problem before proposing fixes — what the customer intended, what happened instead, when it started, reproducibility, and impact — and SHALL generate hypotheses ranked by prior likelihood, each carrying the evidence that would confirm or eliminate it. The agent SHALL test hypotheses in order of safety and informativeness, and SHALL record why each was confirmed or ruled out.

#### Scenario: Hypotheses carry elimination criteria

- **WHEN** the investigation reaches hypothesis formation
- **THEN** each hypothesis is ranked and states the specific evidence or test that would confirm or eliminate it

#### Scenario: Root cause is isolated before resolution

- **WHEN** the user asks for a fix but no hypothesis has been confirmed
- **THEN** the script continues testing rather than emitting an ungrounded resolution

### Behavior: Confidence is stated and calibrated

The agent SHALL attach an explicit confidence to the root cause and to each resolution, in bands — confident, most likely, multiple plausible, below threshold — and SHALL flag the assumptions that would invalidate the diagnosis and the data that would change the confidence. When confidence falls below the threshold, the agent SHALL say so rather than assert a cause.

#### Scenario: Low confidence is named, not hidden

- **WHEN** no hypothesis can be confirmed and further testing is risky
- **THEN** the summary states that multiple hypotheses remain plausible, names what would disambiguate them, and does not present a single cause as settled

### Behavior: Solutions are ranked with risk and rollback

The agent SHALL propose resolutions ranked by feasibility, risk, impact, and timeline, separating immediate mitigation, root fix, and long-term prevention, and SHALL include implementation steps, validation steps, and a rollback plan for each.

#### Scenario: A mitigation is not a root fix

- **WHEN** the ranked solutions include raising a timeout and upgrading a component
- **THEN** the timeout is labeled an immediate mitigation that stops the symptom, the upgrade is labeled the root fix, and both carry rollback steps

### Behavior: Escalation is detected, not written

The agent SHALL detect when escalation is warranted — expertise outside the investigation's domain, a systemic gap, a resolution requiring code changes, or residual uncertainty when further testing is risky — and SHALL name it and hand off to `support-escalation` or `escalation-writing`, providing the problem summary, evidence gathered, ranked hypotheses, what was ruled out, and the specialist input needed. The agent SHALL NOT write the escalation ticket itself.

#### Scenario: Uncertainty after testing triggers a handoff

- **WHEN** uncertainty remains after hypothesis testing and further testing is risky
- **THEN** the summary marks escalation as needed and supplies the handoff fields, and the escalation ticket is left to the escalation skill

### Behavior: Dual output format

The agent SHALL emit a machine-readable JSON investigation summary and a rendered Markdown report derived from the same field values. The JSON SHALL contain the keys `investigation_id`, `timestamp`, `problem_model`, `root_cause_analysis`, `evidence_chain`, `hypotheses_eliminated`, `solutions_ranked`, `next_steps`, `escalation`, and `confidence`. The agent SHALL emit JSON only when the user requests it.

#### Scenario: Both artifacts agree

- **WHEN** an investigation completes with a confirmed root cause
- **THEN** the output carries all required JSON keys, and the Markdown report's root cause, confidence, and top-ranked solution match the JSON field values

## Constraints

### Constraint: Local inference for anonymize, redact, and judge

The agent MUST resolve the anonymizer, redaction, and judge models through `ollama-role` and prefer local inference, falling back only to a zero-data-retention endpoint the role environment names, and MUST NOT use a retaining endpoint for those stages. A frontier model is permitted only for the disclosed diagnosis handoff downstream of the judge gate; it MUST NOT be used for anonymization, redaction, or judging, and MUST NOT receive raw input or the mapping.

### Constraint: No raw customer material to the model

The agent MUST NOT send raw (unanonymized) input to any model, and MUST NOT place raw input, the real→substitute mapping, unverified output, or the investigation summary into logs, progress output, error messages, or any retained or versioned artifact. Reports of a leak SHALL name the class and count, never the value.

### Constraint: No fabricated identifiers or evidence

The agent MUST NOT emit an account name, org slug, issue ID, version number, timestamp, attachment name, log line, or URL that does not appear in the redacted source. A plausible-looking identifier in a diagnosis is worse than a stated gap, because the operator will act on it.

### Constraint: No real customer material in fixtures

The agent MUST NOT build eval cases or fixtures from real support threads, logs, HAR files, customer names, org slugs, or colleague handles, even redacted or paraphrased. Fixtures are synthesized.

### Constraint: No silent control bypass

The agent MUST NOT disable, weaken, or route around the anonymization, redaction, judge-gate, local-inference, or human-review controls without saying so on stderr, and MUST NOT offer a flag that skips verification while still producing output.

### Constraint: No autonomous execution of resolutions

The agent MUST NOT run the proposed fixes, apply configuration changes, restart services, or file the summary into any external system. Implementation and any egress are the operator's deliberate act.

<!-- skillet-version: 1.8.0 -->

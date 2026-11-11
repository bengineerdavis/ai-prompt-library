# Context Anonymizer

## Intent

Transform text containing sensitive material into pseudonymous output that stays faithful enough for powerful downstream reasoning, while keeping every raw value off every model and out of every artifact. The skill exists because two failure modes look identical from the outside: redaction that blanks values into placeholders destroys the context a diagnosis depends on, and naive pseudonymization leaks the real→substitute mapping or a distinctive context that re-identifies the subject. This engine threads the middle — it substitutes realistic entities so the text reads naturally, holds the mapping locally, and proves the result with a bounded detect–adjust loop and a small-local-model judge gate before anything leaves.

The engine runs client-side as a callable stage other skills invoke. It is pseudonymization, not redaction, and it never replaces the fail-closed redaction and verification layers that run after it. Its output is explicitly *pseudonymous*, and it discloses the residual risk that context alone can re-identify even when no name survives. Model choices for the anonymizer and the judge are roles resolved locally and chosen by measurement, never hardcoded tags and never assumed from a model card.

## Triggers

- **SHOULD** apply when a skill or operator asks to anonymize, pseudonymize, or de-identify text before it is sent to a more powerful model or shared.
- **SHOULD** apply when downstream reasoning needs realistic, coherent entities rather than placeholder blanks.
- **SHOULD** apply when an operator wants a configurable pseudonymization strategy — which entity classes to substitute, how consistent the substitutes are, how many detect–adjust iterations to allow.
- **SHOULD NOT** apply to strict redaction that blanks values into typed placeholders with no realistic substitution — that is `pii-redaction`, and this engine feeds it rather than replaces it.
- **SHOULD NOT** apply to secret scanning that only detects and reports without producing a safe derivative, or to encryption and access control, which protect the original.
- **SHOULD NOT** apply when the material may never leave the host under any pseudonymization — that calls for local-only handling, not the frontier handoff this engine enables.

## Behaviors

### Behavior: Pseudonymize with context-preserving substitution

The engine SHALL replace sensitive entities — names, organisations, locations, dates, identifiers, financial values — with realistic, context-preserving substitutes using a local model resolved through a role, and SHALL keep public entities intact. Substitution SHALL be configurable: the operator selects which entity classes to substitute and the consistency of substitutes, with extensive options and extensions rather than a fixed policy. Substitution SHALL preserve the technical literals downstream reasoning depends on — error strings, version numbers, timestamps-as-durations, codes.

#### Scenario: A support log is pseudonymized faithfully

- **WHEN** a log containing a customer name, an org slug, and a table-lock error with a version is anonymized with the default strategy
- **THEN** the name and org are replaced by consistent realistic substitutes, the error string and version survive verbatim, and the result reads as coherent prose rather than placeholder soup

### Behavior: The mapping is held locally and never emitted

The engine SHALL hold the real→substitute mapping in the calling process and SHALL NOT send it to any model, write it to any retained or versioned artifact, or include it in the output. The mapping is itself sensitive: its leak is what makes pseudonymous output re-identifiable.

#### Scenario: The output is inspected for the mapping

- **WHEN** an anonymized artifact and the process's logs are examined after a run
- **THEN** the real→substitute correspondence appears in neither, and no real value is recoverable from any emitted file

### Behavior: Local inference for anonymize and judge

The engine SHALL resolve both the anonymizer model and the judge model through `ollama-role` as roles chosen by measurement, prefer local inference for every call, and fall back only to a zero-data-retention endpoint the role environment names. The engine SHALL NOT use a frontier model for anonymization or judging, and SHALL refuse and say why when neither a local model nor a ZDR endpoint is available.

#### Scenario: Only a retaining hosted endpoint is reachable

- **WHEN** the local models are down and the only reachable endpoint retains data
- **THEN** the engine refuses to run and explains the permitted options rather than downgrading to the retaining host

### Behavior: Bounded detect–adjust loop

The engine SHALL run a bounded iterate-until-clean loop: detect residual PII and secrets in the candidate output with `betterleaks` and deterministic patterns, adjust by re-anonymizing or tightening the strategy, and repeat until the detectors pass or a configurable iteration cap is reached, then fail closed. The loop is a bounded iteration, not a graph.

#### Scenario: A residual secret is found on the first pass

- **WHEN** the first candidate output still contains a live credential that the anonymizer left intact
- **THEN** the loop adjusts and re-checks, and if the cap is reached with the credential still present the run exits non-zero and emits nothing

### Behavior: Small-local-model judge gate before emission

The engine SHALL verify the final candidate with a small local judge model chosen by measurement before emitting, checking for leaked identifiers, and SHALL fail closed — emitting nothing — when the judge or the detectors disagree with the candidate. The judge checks for leaked identifiers, not for contextual uniqueness.

#### Scenario: The judge finds a surviving identifier

- **WHEN** the judge model detects a real organisation identifier in the final candidate that the deterministic pass missed
- **THEN** the run fails closed, no output is written, and the report names the class and count of the leak, never the value

### Behavior: Fail closed on the output path

The engine SHALL stage output to a temporary location and write the destination only after the judge gate and detectors pass, and SHALL remove the staging file on every failure path so no partially anonymized artifact is left where clean output is expected.

#### Scenario: Verification fails with a pre-existing output file

- **WHEN** the destination already holds a previously verified anonymization and a new run fails the judge gate
- **THEN** the destination still holds its previous content and no staging file remains

### Behavior: Disclose residual re-identification risk

The engine SHALL mark its output as pseudonymous and disclose that context alone can re-identify the subject even when no direct identifier survives, and SHALL state that the frontier handoff accepts this residual risk rather than eliminating it.

#### Scenario: Output is prepared for a frontier model

- **WHEN** anonymized output is about to be sent to a powerful hosted model
- **THEN** the handoff states that the material is pseudonymous and that distinctive context may still re-identify, so the operator's downstream use is informed

### Behavior: Callable engine, never an autonomous actor

The engine SHALL run as a stage other skills invoke with explicit input and output, and SHALL NOT itself call a frontier model, send anything off-host, or decide downstream use. The frontier handoff is the calling skill's and the operator's deliberate act, not the engine's.

#### Scenario: An investigation skill invokes the engine

- **WHEN** `support-partner-deep-research` calls the engine to pseudonymize an attachment
- **THEN** the engine returns pseudonymous text and the local mapping stays in the calling process, and any subsequent frontier call is the investigation skill's disclosed decision

## Constraints

### Constraint: No raw value to any model

The engine MUST NOT send unanonymized input to any model beyond the local anonymizer's own substitution pass, and MUST NOT place raw input, the mapping, or unverified output into logs, progress output, error messages, or any retained artifact. A leak report names the class and count, never the value.

### Constraint: Never emit unverified output

The engine MUST NOT write, print, or return output that has not passed the judge gate and the detectors, and MUST NOT offer a flag that skips verification while still producing output.

### Constraint: Never report success on an unproven run

The engine MUST NOT exit zero when the judge gate or detection failed, was skipped, or could not run. A missing model or detector is a failure, not a pass.

### Constraint: No real customer material in fixtures

The engine MUST NOT build eval cases or fixtures from real customer threads, logs, captures, names, org slugs, or handles, even redacted or paraphrased. Fixtures are synthesized.

### Constraint: No silent control bypass

The engine MUST NOT disable, weaken, or route around the anonymize, detect, judge, or local-inference controls without saying so on stderr.

<!-- skillet-version: 1.8.0 -->

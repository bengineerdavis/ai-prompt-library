# Support Escalation

## Intent

Turn a raw support thread into an escalation ticket that a receiving engineering team can act on without reading the original correspondence. The output states what is broken, who it affects, what has already been investigated and ruled out, what evidence and attachments exist, and exactly what the escalation target is being asked to do.

This exists because escalations fail in two directions. They are written too thin — a restated customer complaint with no impact, no evidence, and no ask, which the receiving team bounces back — or too generous, padded with severity and detail the thread does not actually support, which burns responder trust and mis-prioritizes real incidents. Both failures share a root cause: the writer filling gaps with inference instead of naming them. This skill forbids that fill. An under-specified thread is a question to ask or a blocked escalation, never a creative writing prompt.

Support threads are long-lived and self-contradicting. The customer's opening message is usually the least accurate account in the record, superseded by later notes, re-tests, and attachments. So the skill reads the thread as a timeline rather than a document, weights recent statements over old ones, and treats an unresolved contradiction as something to ask about rather than silently resolve.

Escalation content routinely carries customer PII and is a derived artifact under `~/dotfiles/policy/ethics.yaml`. All inference runs on a local model, nothing is retained, and the finished ticket does not leave the machine without a human reading it first.

## Triggers

- **SHOULD** apply when the user asks to escalate, file, or draft an escalation for a support ticket, email thread, or customer issue.
- **SHOULD** apply when the user pipes a support thread and asks what severity it warrants or which team owns it.
- **SHOULD** apply when the user asks whether a thread has enough information to escalate.
- **SHOULD NOT** apply when the user wants a customer-facing reply drafted — that is a response, not an escalation, and the audience is inverted.
- **SHOULD NOT** apply when the user wants a manager briefing or triage summary of an inbound email; `~/bin/triage` owns that and produces a different artifact.
- **SHOULD NOT** apply when the user is asking a product or documentation question that happens to mention a customer.

## Behaviors

### Behavior: Dual output format

The agent SHALL emit a machine-readable JSON object and a rendered Markdown ticket for every escalation, with the Markdown derived from the same field values as the JSON. The JSON SHALL contain the keys `severity`, `severity_rationale`, `title`, `summary`, `customer_impact`, `timeline`, `evidence`, `attachments`, `steps_taken`, `reproduction`, `unknowns`, `open_questions`, `ask`, `routing`, and `readiness`.

#### Scenario: Complete thread produces both artifacts

- **WHEN** a support thread containing an SDK version, a Sentry issue URL, and a described failure is piped to the escalation tool
- **THEN** the output contains a valid JSON object carrying all fifteen required keys, followed by a Markdown ticket whose title, severity, and impact match the corresponding JSON field values

#### Scenario: JSON-only mode suppresses prose

- **WHEN** the user requests JSON output only
- **THEN** stdout contains exactly one parseable JSON object and no Markdown prose

### Behavior: Severity with stated rationale

The agent SHALL assign exactly one severity from S1, S2, S3, or S4, and SHALL justify it in `severity_rationale` by citing the specific scope, workaround availability, and business exposure drawn from the thread. S1 requires production loss, data loss, or a security exposure with no workaround. S2 requires a broken primary workflow with no acceptable workaround. S3 covers degraded behavior where a workaround exists. S4 covers cosmetic issues and questions.

#### Scenario: Workaround present caps severity

- **WHEN** a thread reports a broken dashboard export but the customer states they can retrieve the same data through the API
- **THEN** severity is S3 or lower and `severity_rationale` names the API path as the available workaround

#### Scenario: Urgent tone does not raise severity

- **WHEN** a thread contains "this is absolutely critical, our whole team is blocked" but describes only a cosmetic rendering defect with no functional loss
- **THEN** severity is S4 and `severity_rationale` distinguishes the reported urgency from the observed impact

### Behavior: Evidence is quoted, never synthesized

The agent SHALL populate `evidence` only with artifacts present in the source thread — issue URLs, event IDs, SDK names and versions, error strings, timestamps, log excerpts — and SHALL record each with the reference exactly as it appeared. Any fact the receiving team would need that the thread does not supply SHALL be listed in `unknowns` rather than inferred, approximated, or filled from general product knowledge.

#### Scenario: Missing version is named, not guessed

- **WHEN** a thread names `@sentry/node` but never states a version
- **THEN** `evidence` records the SDK name without a version and `unknowns` contains an entry identifying the missing SDK version

#### Scenario: Error string is preserved verbatim

- **WHEN** a thread contains the error `TypeError: cannot read property 'dsn' of undefined`
- **THEN** that string appears in `evidence` character-for-character, not paraphrased as "a DSN type error"

### Behavior: Attachment and investigation history intake

The agent SHALL populate `attachments` with every file, screenshot, HAR, log bundle, trace export, or linked document referenced anywhere in the thread, recording for each its name as given, who supplied it, when, and whether its contents were actually available to the agent. The agent SHALL populate `steps_taken` with what support already attempted, observed, or ruled out, attributing each step to its source message. When the thread references an attachment whose contents were not supplied, or shows an investigation gap where a step was promised but no result was recorded, the agent SHALL raise it under the clarifying-questions behavior rather than reasoning as though the artifact were absent or the step complete.

#### Scenario: Referenced but unsupplied attachment is tracked

- **WHEN** a thread says "I've attached the HAR file and our config" but only the config text was piped in
- **THEN** `attachments` lists both, marks the HAR as referenced-but-unavailable, and `open_questions` requests the HAR contents

#### Scenario: Ruled-out cause is recorded and not re-requested

- **WHEN** the thread shows support already confirmed the DSN is valid and the customer's quota is not exhausted
- **THEN** `steps_taken` lists both checks with their source messages, and `ask` does not request that either be re-verified

#### Scenario: Abandoned investigation step is surfaced

- **WHEN** a support agent wrote "I'll check the relay logs and follow up" and no later message reports a result
- **THEN** `steps_taken` marks that check as started-without-recorded-outcome and `open_questions` asks whether it was completed

### Behavior: Recency-weighted conflict resolution

The agent SHALL order every dated statement, note, comment, and attachment into `timeline` oldest to newest, and SHALL treat the most recent statement as authoritative when two accounts of the same fact conflict. Superseded claims SHALL be retained in `timeline` marked as superseded, never deleted. Undated or unorderable material SHALL be treated as position-unknown and MUST NOT be assumed recent.

#### Scenario: Later correction overrides opening claim

- **WHEN** the customer's first message says the failure began "about a week ago" and a later comment from the same customer says "correction — checking our logs, it actually started after our 2026-08-19 deploy"
- **THEN** `summary` and `evidence` use the 2026-08-19 deploy date, and `timeline` retains the earlier estimate marked superseded

#### Scenario: Later note supersedes and prompts a question

- **WHEN** an early message reports the error affects all environments and a later internal note says it reproduces only in staging, with no explanation of the change
- **THEN** the staging-only scope governs the ticket body, and `open_questions` asks whether production was re-tested or the original report was mistaken

#### Scenario: Undated material is not promoted

- **WHEN** an attachment carries no timestamp and contradicts a dated recent comment
- **THEN** the dated comment governs, and `timeline` records the attachment as position-unknown rather than ordering it last

### Behavior: Clarifying questions before committing

The agent SHALL record every unresolved ambiguity in `open_questions` as a specific question naming the candidate answers drawn from the thread. When stdout is a TTY, the agent SHALL put two to four of the highest-impact questions to the user before finalizing the ticket, each offering the concrete candidate answers rather than asking an open-ended prompt. When stdout is not a TTY, the agent MUST NOT guess: the questions stay in `open_questions` and the readiness gate applies. An unanswered question SHALL be recorded as unanswered and never treated as agreement with the agent's preferred reading.

#### Scenario: Interactive run asks rather than assumes

- **WHEN** a thread is piped in an interactive terminal and the affected environment is genuinely ambiguous between production and staging
- **THEN** the agent asks the user which environment is affected, offering production and staging as the candidate answers, before emitting the ticket

#### Scenario: Non-interactive run defers instead of guessing

- **WHEN** the same ambiguous thread is piped in a script with stdout redirected to a file
- **THEN** no prompt is issued, `open_questions` contains the environment question with both candidates, and `readiness.status` is `blocked`

#### Scenario: Skipped question is not consent

- **WHEN** the user declines or skips a clarifying question at the prompt
- **THEN** the question remains in `open_questions` marked unanswered and the ticket does not adopt either candidate as settled

### Behavior: Actionable ask and routing

The agent SHALL state in `ask` the single specific action required from the receiving team, naming an action rather than a topic. The agent SHALL name a receiving team in `routing.team` and justify it in `routing.rationale` from the product surface implicated by the evidence. When the evidence does not distinguish between candidate owners, the agent SHALL name the most likely team, record the ambiguity in `unknowns`, and raise it in `open_questions`.

#### Scenario: Ask is actionable

- **WHEN** an escalation concerns dropped events for one organization
- **THEN** `ask` reads as a directed action such as "confirm whether relay dropped events for org `acme-co` between 14:00–16:00 UTC on 2026-08-21", not as a topic label such as "investigate event ingestion"

#### Scenario: Ambiguous ownership is flagged

- **WHEN** symptoms could plausibly originate in either SDK instrumentation or server-side ingestion and the thread contains no evidence separating them
- **THEN** `routing.team` names one team, `routing.rationale` states why it is the more likely owner, and both `unknowns` and `open_questions` record the undetermined SDK/ingestion boundary

### Behavior: Readiness gate

The agent SHALL set `readiness.status` to `blocked` and enumerate the missing items in `readiness.missing` when the thread lacks what the receiving team needs to begin — minimally a reproduction path or a concrete evidence reference, plus an identifiable affected account — or when unanswered entries remain in `open_questions` that would change severity, routing, or the ask. When blocked, the agent SHALL still emit the full ticket structure so the gaps are visible, and SHALL NOT present the ticket as ready to file.

#### Scenario: Vague thread blocks

- **WHEN** the thread reads only "Sentry isn't working for us anymore, please help" with no account, product surface, evidence, or timeframe
- **THEN** `readiness.status` is `blocked`, `readiness.missing` names the absent account identifier, product surface, and evidence, and the Markdown ticket is labeled as blocked rather than ready

#### Scenario: Outstanding severity-changing question blocks

- **WHEN** the thread is otherwise complete but an unanswered `open_questions` entry determines whether the outage affects production or only staging
- **THEN** `readiness.status` is `blocked` and `readiness.missing` cites that unanswered question

#### Scenario: Sufficient thread passes

- **WHEN** the thread supplies an org slug, a reproduction sequence, and a linked issue, and no unanswered question affects severity, routing, or the ask
- **THEN** `readiness.status` is `ready` and `readiness.missing` is empty

## Constraints

### Constraint: Local inference first, ZDR as the only fallback

The agent MUST resolve its model through `ollama-role` rather than hardcoding a tag, and MUST prefer a local model. When no local model can serve the request — not installed, insufficient context window, or the daemon is down — the only permitted fallback is the Zero-Data-Retention endpoint named by `OLLAMA_ROLE_ESCALATE`, read via `eval "$(ollama-role env)"` — note that `escalate` is a frontier-only entry and is not resolvable through `ollama-role get`. The agent MUST NOT fall back to a non-ZDR hosted endpoint under any circumstance, and MUST NOT silently downgrade tiers: if neither a local model nor a ZDR endpoint is available, it refuses and says why.

Thread content is work-tagged material, which `~/dotfiles/policy/personal.yaml` forbids routing to ordinary remote inference, and any remote call is an egress event the ethics layer gates independently.

### Constraint: ZDR asserted per call, never assumed

The agent MUST NOT issue any thread-bearing remote call without `-o provider '{"zdr":true}'` on that specific invocation, including follow-up turns in the same conversation. `llm` options do not persist across a conversation, so an unflagged follow-up quietly reaches a retaining endpoint and the leak leaves no trace. The agent MUST also state on stderr that the call is leaving the machine and which endpoint it is going to, because an egress event that looks identical to a local run cannot be reviewed.

Two limits on what ZDR buys, both of which the agent MUST respect rather than treat the flag as blanket cover: OpenRouter's ZDR routing excludes first-party Anthropic, OpenAI, and Google endpoints and serves those models through Bedrock, Azure, or Vertex instead; and ZDR does not extend to plugins or tool calls, so no web search, retrieval, or other tool may be enabled on a thread-bearing request.

### Constraint: No prompt or response retention

The agent MUST NOT leave thread content in a tool log. Invocations of the `llm` CLI MUST pass `--no-log`, because its default behavior writes full prompt and response bodies to a local database indefinitely — retention that no policy layer authorizes for customer material.

### Constraint: No retained or versioned derived artifacts

The agent MUST NOT write the finished ticket to a tracked path, commit it, cache it, or append it to a history file. An escalation ticket is a derived artifact under the ethics layer, which permits neither retention nor versioning regardless of how little of the original survives. The ticket goes to stdout for the operator to place deliberately.

### Constraint: No real customer material in eval fixtures

The agent MUST NOT build eval cases or fixtures from real support threads, customer names, org slugs, or colleague handles, even redacted or paraphrased. Eval cases are versioned and do not expire, and the ethics layer forbids using identifiable third parties for evaluation. Fixtures are synthetic.

### Constraint: No automated filing

The agent MUST NOT file the ticket into Jira, Linear, Slack, or any other system on its own. Egress requires human review that cannot be automated end to end; the operator reads the ticket and files it.

### Constraint: No fabricated identifiers

The agent MUST NOT emit an account name, org slug, issue ID, event ID, version number, timestamp, attachment name, or URL that does not appear in the source thread. A plausible-looking identifier in an escalation is worse than a stated gap, because the receiving team will spend time chasing it.

### Constraint: No severity inflation from tone

The agent MUST NOT raise severity in response to customer frustration, escalation demands, executive mentions, or urgency language. Severity derives from observed functional impact and workaround availability only.

### Constraint: No silent control bypass

The agent MUST NOT disable, weaken, or route around the local-inference, logging, retention, or human-review controls without saying so on stderr. A control that can be switched off quietly is not a control.

### Constraint: No silent truncation

The agent MUST NOT drop evidence items, attachments, unknowns, open questions, or prior investigation steps to keep the ticket short. When a section is long, it stays long.

<!-- skillet-version: 1.7.0 -->

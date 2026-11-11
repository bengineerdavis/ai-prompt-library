# Glossary

Terms the library uses consistently across skills. Definitions only — no
implementation detail, no decisions.

## Investigation

The interactive diagnosis of a reported issue: intake, evidence gathering,
hypothesis formation, testing, and ranked resolution. Owned by
`support-partner-deep-research`. Ends at a resolution path or a named handoff,
never at a report.

Distinct from **Research**, which answers an open-ended question and produces
an evidence-backed report. Research never diagnoses a bug; investigation never
produces a survey of options.

## Research

The open-ended question-answering discipline owned by `research`. Produces a
report with sources, options, and a recommendation. Does not diagnose bugs,
specify features, compare two concrete artifacts, or produce code.

## Escalation

The act of handing an unresolved or out-of-scope issue to a receiving team or
specialist. Two separate concerns share the word:

- **Escalation detection** — the diagnostic judgment that further investigation
  is unproductive, risky, or outside the current skill's scope. Owned by the
  investigating skill.
- **Escalation writing** — formatting the handoff artifact (ticket, message,
  ask) for the receiving audience. Owned by `support-escalation` (terminal JSON
  - Markdown ticket) and `escalation-writing` (GitHub, Slack, Intercom drafts).

An investigating skill detects; it never writes the ticket itself.

## Investigation summary

The terminal artifact of an investigation: the problem model, root cause,
evidence chain, hypotheses eliminated, ranked solutions, and next steps. The
handoff input to **Escalation writing** when escalation is warranted.

## Local inference

Model inference that runs on the operator's own machine through a locally
resolved role (via `ollama-role`), with no content leaving the host. The default
for any skill that touches customer material.

## ZDR fallback

Zero-Data-Retention hosted inference: the only permitted fallback when local
inference cannot serve a request carrying customer material. Asserted per call,
never assumed from configuration.

## Anonymization

Replacing sensitive entities with realistic, context-preserving substitutes so
downstream reasoning stays faithful — distinct from **Redaction**, which blanks
values into placeholders. Anonymization is pseudonymization: the output is
coherent text, not `[NAME]` soup. Owned by a dedicated anonymization skill that
other skills call, and intended eventually to replace `pii-redactor`'s engine.

## Redaction

Blanking sensitive values into typed placeholders (`[EMAIL]`, `[HOME]`). The
fail-closed guarantee layer. Runs after **Anonymization**, because an anonymizer
SLM misses things; anonymize-then-redact is additive and never replaces the
deterministic + verification layers.

## Pseudonymization mapping

The real → substitute correspondence an anonymizer produces. Itself sensitive.
Held by the calling script, never sent to any model, never written to a retained
or versioned artifact. Its leak is what makes pseudonymous output re-identifiable.

## Detect–adjust loop

The bounded iterate-until-clean cycle: detect residual PII/secrets in candidate
output, adjust (re-anonymize or tighten), repeat until detectors pass or a
configurable iteration cap is hit, then fail closed. Not a graph.

## Judge gate

The final verification of output before emission, run by small local models
chosen by measurement (per `model-fitness`), never by a frontier model and never
by assumption. Checks for leaked identifiers, not for contextual uniqueness.

## Frontier handoff

The deliberate act of sending pseudonymous output to a powerful hosted model for
heavy reasoning, downstream of the **Judge gate**. The residual risk is that
context alone can re-identify; that risk is accepted and disclosed, not silently
eliminated.

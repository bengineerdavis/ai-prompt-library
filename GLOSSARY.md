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
||||||| parent of 52313aa (pii-redaction: support input larger than memory or context)

## Atom

The smallest unit a redaction pass never splits. Which unit that is depends on
the input's form: a line of text, one top-level value in JSON or NDJSON, one
document in YAML, one table in TOML.

An atom is indivisible by definition. When a single atom is larger than the
**chunk budget**, the run refuses rather than splitting it — a split atom would
make the boundary itself a redaction boundary.

## Chunk

One model call's worth of input: one or more whole **atoms**, packed in
document order. A chunk is what the model sees and what verification judges.

Distinct from **atom**, which is a unit of the input; a chunk is a unit of work.

## Chunk budget

The byte ceiling for a single **chunk**. Chosen and printed rather than
discovered, because the model provider does not report a context window that
the tool can query.

The budget may shrink during a run when a chunk fails for a size-related
reason; it never grows on the strength of a success, because fitting is not
evidence that a larger chunk would also have fit.

## Carry window

Input bytes re-read before a **chunk**'s start so a detector can recognise a
match that spans the boundary between two **atoms**. The carry window is read
but never emitted; its purpose is to prove the boundary is safe, not to give
the model more context.

## Plan

The computed sequence of **chunks** for one input, including each chunk's size
and what it covers. Printable before any model call, so an operator can see
what a run will cost before paying it.

A plan contains no redacted content, so printing one is not a way to obtain
output without verification.

## Ledger

A run-scoped, in-memory record of the values a model has already identified as
PII, applied deterministically to later **chunks** so a fragment is still
recognised after the fuller form has scrolled out of view.

A ledger is a store of the values it is meant to remove. It is never written to
disk and never outlives the run.

## Chunk gate

The verification applied to a **chunk**'s candidate output before that output
is appended to the **staged output**. A chunk that fails its gate contributes
nothing, so a run that stops early leaves no partially-redacted file behind.

## Final rescan

The verification applied to the completed **staged output** before it is
released. Reads the whole artifact at bounded memory, catching what only a
whole-artifact view can catch.

## Staged output

The working copy of the redacted artifact, written beside its destination and
renamed into place only once the **final rescan** passes. Removed on every
failure path.

## Single-call path

The path taken when an input fits inside one **chunk budget**: the whole input
in one model call, verified as a whole.

## Streaming path

The path taken when an input does not fit inside one **chunk budget**: the
input is decomposed into **chunks**, each gated, then the assembled artifact is
rescanned.

## Span detector

A model backend that reports where each entity is rather than returning
rewritten text. Substitution, consistency, and verification stay with the
engine, so a span detector removes the failure class where a model silently
rewrites the document it was asked only to annotate.

Distinct from a rewriting model, which returns text and must be checked for
having changed more than the entities.

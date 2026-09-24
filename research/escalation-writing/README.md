# Escalation-writing research

Research session: 2026-09-23–24; recorded 2026-09-24.

Owner: escalation-research. Status: evidence preserved; spec authored and validated;
private voice-policy integration and validation against the user's cases remain pending.

## Purpose

Support a new portable `escalation-writing` specification for humane, accurate,
useful writing in GitHub engineering tickets, Slack coordination, and Intercom
customer replies. The goal is better communication at 2–5 uses per day, with low
question fatigue. It is not to conceal AI involvement or imitate an unverified voice.

Public guidance and eight public bug histories support candidate behaviors. They
do not establish the lowest-pushback format across Sentry teams. The strongest
recurring pattern is a clear request backed by usable evidence, with uncertainty
preserved and structure adapted to the recipient.

## Read the records

- [Sources](sources.md): source IDs, reviewed versions, supported claims, limits,
  and update triggers. Evidence is retained even when a decision rejects an approach.
- [Public cases](public-cases.md): eight contrasting issue histories, comment
  permalinks, requests, responses, diagnoses, outcomes, and edit-history limitations.
- [Decisions](decisions.md): user-approved scope, proposed defaults, rejections,
  and pending decisions, each linked back to evidence.

These records contain public-source paraphrases and approved project decisions.
They contain no private tickets, internal policy contents, or internal policy URL.
The existing terminal `support-escalation` skill remains a separate tool.

## Principle-to-evidence map

- **P01: Prioritize the reader and preserve meaning.** Use direct language and
  the minimum useful edit. Preserve technical facts, meaningful uncertainty, and
  authentic voice. [S01](sources.md#s01-plain-language),
  [S02](sources.md#s02-library-plain-english), and
  [S06](sources.md#s06-peter-yang-no-ai-slop) support this editorial direction.
  They do not establish a private Sentry voice policy.
- **P02: Give the recipient a clear problem and ask.** Include the customer
  consequence and enough context to begin, without making them reconstruct the
  whole conversation. [S09](sources.md#s09-gitlab-requests-for-engineering-help)
  and [S10](sources.md#s10-gitlab-account-escalations) are practitioner workflow
  evidence; [S07](sources.md#s07-sentry-bug-forms) supplies repository-specific needs.
- **P03: Make evidence usable.** Include relevant versions, prerequisites,
  observation location, actual versus expected behavior, and test results. Preserve
  accessible excerpts when a link can expire or require unavailable permissions.
  [S09](sources.md#s09-gitlab-requests-for-engineering-help),
  [S11](sources.md#s11-mozilla-bug-guidance), and
  [C01–C03](public-cases.md#c01-sentry-python-4764) support different parts of this pattern.
- **P04: Explain comparisons and investigation limits.** A working control or
  contrasting example can be more useful than a large inventory. Distinguish a
  test result from a causal hypothesis. See
  [C04](public-cases.md#c04-sentry-python-2116),
  [C05](public-cases.md#c05-pytest-12863),
  [C06](public-cases.md#c06-pytest-12865), and
  [S12](sources.md#s12-tatham-practitioner-evidence).
- **P05: Treat useful questions as progress.** New diagnostic experiments and
  reader misunderstandings are not automatically author omissions. See
  [C02](public-cases.md#c02-sentry-javascript-21915),
  [C07](public-cases.md#c07-vs-code-208321), and
  [C08](public-cases.md#c08-vs-code-208551). Use
  [S03](sources.md#s03-library-interaction-questioning) to keep drafting questions
  proportionate. No empirical question budget follows from these cases.
- **P06: Adapt to the audience and channel.** Engineering needs a durable
  investigation record; Slack needs a coordination request; customers need a clear
  explanation and next step. [S10](sources.md#s10-gitlab-account-escalations),
  [S13](sources.md#s13-slack-threads), and
  [S14](sources.md#s14-intercom-audience-separation) support this synthesis.
- **P07: Keep status and outcomes honest.** Routing, diagnosis, prioritization,
  merged fixes, releases, and customer verification are different events.
  [S08](sources.md#s08-sentry-public-triage) and the contrasting
  [case outcomes](public-cases.md) prevent treating closure or silence as success.

## Candidate channel structures

These structures are authoring defaults, not universal mandatory forms.

- **GitHub engineering ticket:** Symptom-based title; brief problem, impact, and
  ask; expected/actual behavior; reproduction and environment; investigation
  results; relevant evidence and unknowns. Respect the repository's template.
  Summarize the conversation instead of pasting a transcript.
- **Slack coordination:** Intended recipient and specific ask; why attention is
  needed now; decisive facts; canonical ticket link. Use a thread for detail and
  carry durable decisions back to the ticket. Avoid a bare link with “please look.”
- **Intercom customer reply:** Acknowledge the concrete impact; explain what is
  known and happening; give a supported workaround or needed customer action;
  explain the relevant next step from the sender's role. Include a promise only
  when the sender currently confirms they can guarantee that action and any timing.
  Keep prior obligations visible internally without automatically renewing them.
  Internal notes and customer replies require different content even in the same tool.

The commitment rule reflects the author's feedback on the synthetic demonstration,
recorded in [D08](decisions.md#approved-decisions). It tightens the initial research
synthesis: a previously authorized promise is insufficient on its own. Public
guidance does not establish that a particular follow-up can be guaranteed.

Keep the same factual core across channels: problem, impact, context,
investigation, and ask. Use it as a silent completeness check rather than five
mandatory headings. Label customer-reported, independently observed, hypothesized,
and unknown information accurately. Never invent evidence, urgency, owners, or dates.

## Candidate taxonomy

Keep these dimensions separate so one label does not hide the reason for escalation.

- **Intent:** Defect/regression; diagnostic assistance; intended-behavior or
  documentation clarification; operational intervention; priority/ownership decision.
  Mark incident/security handling separately rather than forcing routine bug intake.
- **Evidence state:** Independently reproduced; customer-reproduced with artifacts;
  intermittent/production-only with occurrence evidence; reported but unverified.
- **Follow-up reason:** F1 unclear expected/actual behavior; F2 missing setup or
  reproduction prerequisite; F3 missing impact/scope/timing; F4 missing investigation
  result; F5 inaccessible/expired/uninterpretable evidence; F6 unclear ask/owner/action;
  F7 unsupported causal, severity, or certainty claim.
- **Preventability:** Available but omitted; not investigated; unavailable to the
  sender; newly needed after engineering analysis; already supplied but missed or
  misunderstood. Only “available but omitted” is clearly a writing omission.

## Evaluate future historical cases

Measure **avoidable clarification burden**, not generic pushback. A candidate
avoidable request concerns a reasonably foreseeable fact the handoff could have
supplied so the recipient could begin the intended work.

1. Sample smooth and difficult cases across teams, intents, severity, and evidence
   states. Do not select only closed tickets or praised authors.
1. Reconstruct the handoff-time body and authorized linked context. Keep later
   evidence separate. If edits or private conversations are missing, mark uncertainty.
1. Have Support and Engineering reviewers classify requests and preventability.
   Resolve disagreements; keep legitimate disagreement about priority, behavior,
   ownership, or solution separate from missing evidence.
1. Measure avoidable rounds, repeated investigation, time to substantive action,
   and actionable disposition. Score accuracy, clear ask, scanability, evidence
   traceability, uncertainty, and audience fit separately from those outcomes.
1. Compare similar cases and test candidate rewrites on held-out material using
   only facts available at handoff. Blind reviewers to outcomes where practical.
1. In a later authorized pilot, measure questions per use, time to a usable draft,
   edits, abandoned drafts, factual corrections, and actual engineering follow-up.

Control or stratify for severity, account importance, known versus novel bugs,
reproduction difficulty, reporter expertise/relationships, recipient familiarity,
staffing, workload, time zones, customer responsiveness, telemetry access, incidents,
private pre-discussion, and changed ownership/process. Account for incomplete
records and insufficient observation time. A small retrospective study supports
associations, not causal conclusions.

Do not count fix verification, a new expert diagnostic experiment, or a justified
priority/ownership disagreement as an automatic writing failure. An ignored or
abandoned ticket is not a low-pushback success. [C08](public-cases.md#c08-vs-code-208551)
also shows why response timing and decision explanation matter.

## Limits and next review

The corpus is public only and contains bug reports rather than verified Support
escalations. Guidance describes intended practice, not measured adoption. Issue
bodies and comments are mutable. Public material cannot establish private team
preferences, author identity, or the user's personal voice policy.

The current scope is spec-only. [Skillet 1.8.0](sources.md#s16-skillet-180) and
[dotagents 3.1.0](sources.md#s17-dotagents-310) documentation supports compatibility
planning. The [implementation review](decisions.md#implementation-review) records
spec validation; runtime installation and behavioral evals remain unperformed.

Before promotion or a significant upstream release, check affected active sources
and document changed claims. A quarterly manual review is a provisional maintenance
choice, not an empirical finding or an installed schedule. See
[proposed defaults and pending decisions](decisions.md#proposed-authoring-defaults).

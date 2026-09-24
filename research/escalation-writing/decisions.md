# Escalation-writing decisions

Research session: 2026-09-23–24; recorded 2026-09-24.

Owner: escalation-research. This record distinguishes user-approved scope from
authoring proposals. The [source register](sources.md) and [public cases](public-cases.md)
preserve evidence independently of acceptance or rejection. New decisions should
link to that evidence and retain the reason for superseding an earlier decision.

## Approved decisions

These decisions come from the user's approved plan and implementation brief.
Sources support their rationale; public sources do not substitute for user approval.

- **D01: Create a new escalation-writing specification.** Prioritize humane,
  accurate writing and useful communication. Concealing AI involvement is not an
  objective. Adapt plain-language and minimum-edit principles from
  [S01](sources.md#s01-plain-language), [S02](sources.md#s02-library-plain-english),
  and [S06](sources.md#s06-peter-yang-no-ai-slop).
- **D02: Serve three distinct channel jobs.** GitHub engineering tickets, Slack
  coordination, and Intercom customer replies need different structures. Keep
  factual meaning consistent while adapting content to the recipient. Basis:
  [S09–S10](sources.md#s09-gitlab-requests-for-engineering-help),
  [S13–S14](sources.md#s13-slack-threads).
- **D03: Minimize daily question fatigue.** The target use frequency is 2–5 times
  per day. This approves the goal, not a numeric question budget. Basis:
  [S03](sources.md#s03-library-interaction-questioning) and the distinction between
  useful questions and missing information in [C02](public-cases.md#c02-sentry-javascript-21915)
  and [C07](public-cases.md#c07-vs-code-208321).
- **D04: Use public cases as fallback evidence.** Retain contrasting outcomes and
  limits. Do not present them as the user's cases or proof of least pushback across
  Sentry. Private corpus access and voice-policy integration remain pending.
  Basis: [C01–C08](public-cases.md) and [S19](sources.md#s19-unavailable-private-voice-policy).
- **D05: Preserve evidence before decisions and review upstream.** Retain research
  after deciding. Prefer pinned links; unversioned pages need a recorded review
  status. Use no submodule unless the whole repository becomes a real dependency.
  The [source register](sources.md) implements traceability without vendoring tickets.
- **D06: Keep the terminal support-escalation skill separate.** The new writing
  contract does not replace that operational tool. Channel-writing requirements
  appear in the [research synthesis](README.md#candidate-channel-structures).
- **D07: Stay spec-only for this stage.** Target compatibility with Skillet and
  dotagents; do not create evals or install a runtime. The coordinator owns skill
  files and validation. [S16](sources.md#s16-skillet-180) documents optional evals;
  [S17](sources.md#s17-dotagents-310) distinguishes installable skills from research.
- **D08: Match each message to its recipient and protect customer expectations.**
  Author feedback on the synthetic demonstration, 2026-09-24: Intercom replies
  need to reflect who receives the message, who the agent speaks for, and the next
  steps. Do not promise facts, outcomes, or follow-up timing the sender cannot
  guarantee. Preserve options for handling the customer's expectations.
  This is an explicit author requirement, not a finding from the public case corpus.
  It tightens the earlier rule that allowed a recorded, authorized update promise.

## Proposed authoring defaults

These are research recommendations, not separately approved settings or measured optima.

- **P01: Draft from context first.** Reuse supplied facts. Ask only when the answer
  changes correctness, the ask, audience-appropriate disclosure, or a commitment.
  Express nonblocking unknowns honestly instead of filling every field.
  Basis: [S03](sources.md#s03-library-interaction-questioning),
  [S09](sources.md#s09-gitlab-requests-for-engineering-help).
- **P02: Use a small, adaptive question budget.** Start with zero questions when
  the draft is usable; otherwise ask the single highest-value question. Reassess
  before another. A target of zero to two clarifiers is only a heuristic, with
  material uncertainty taking precedence over a cap. An earlier research suggestion
  offered one compact batch of one or two questions; do not silently treat it as
  approved or compatible with S03's one-at-a-time default. Validate fatigue in use.
- **P03: Use a silent evidence check and an editorial pass.** Check problem,
  impact, context, investigation, and ask; then improve clarity without changing
  facts or certainty. Avoid mandatory headings in every channel. Basis:
  [S02](sources.md#s02-library-plain-english), [S07](sources.md#s07-sentry-bug-forms),
  and [C01–C08](public-cases.md).
- **P04: Keep AIHero grilling at authoring time.** Use design exploration and
  durable decisions when shaping the skill, not an exhaustive interview before
  each escalation. Basis: [S04](sources.md#s04-aihero-and-matt-pocock-authoring-workflow).
- **P05: Review active material manually each quarter.** A first routine review
  would be due by 2026-12-24. Also review before promotion and significant upstream
  releases, using [source-specific triggers](sources.md). This cadence is a
  provisional maintenance choice; no automatic job or empirical benefit is claimed.

## Rejected approaches

- **Authorship camouflage or AI-detection scoring.** Optimize the reader's
  understanding, not apparent origin. S06 itself distinguishes patterns from
  authorship inference. Basis: D01 and [S06](sources.md#s06-peter-yang-no-ai-slop).
- **Wholesale adoption of unslop rules.** Reject arbitrary punctuation/word bans,
  removal of genuine uncertainty, and invented numbers or mechanisms. Select useful
  editing principles from [S05](sources.md#s05-cursor-unslop) and
  [S06](sources.md#s06-peter-yang-no-ai-slop), subordinate to factual fidelity.
- **One template or exhaustive intake for every message.** This ignores channel
  purpose and daily effort. Use [channel-specific structures](README.md#candidate-channel-structures)
  and [S03](sources.md#s03-library-interaction-questioning) instead.
- **No reproduction, no escalation.** Expert help may be needed to find the next
  diagnostic step; intermittent production faults still matter. Basis:
  [S09](sources.md#s09-gitlab-requests-for-engineering-help) and
  [C07](public-cases.md#c07-vs-code-208321).
- **Zero questions or fastest closure as the quality target.** C01 needed no
  visible clarification but faced compatibility barriers. C04 closed without an
  established fix. C08 includes timing and ownership disagreement. Use the
  [multidimensional evaluation method](README.md#evaluate-future-historical-cases).
- **An inferred private policy or portable internal link.** The inaccessible
  Notion material supplies no usable rules. Keep it pending under
  [S19](sources.md#s19-unavailable-private-voice-policy).
- **A whole-repository dependency for citations.** Pinned links and paraphrases
  satisfy current evidence needs. Reconsider a submodule only if D05's dependency
  condition is met.
- **Repeat a promise because it appears in the notes.** The synthetic example
  repeated a recorded 15:00 update commitment without checking that the sender
  could guarantee it. D08 requires a current basis for repeating the promise.
  Keep existing obligations visible internally; do not erase or silently cancel them.
- **Replace a deadline with an unsupported event-based promise.** "We'll update
  you as soon as Engineering responds" still commits the sender to an action and
  timing. Explain the known status and requested next step instead when a promise
  cannot be guaranteed. Flexibility does not justify vague reassurance or concealment.

## Pending decisions and evidence

- **Private voice policy:** Obtain an authorized readable version, identify what
  can be made portable, and reconcile conflicts with public editorial defaults.
  Do not infer missing policy from the user's employer or public contributors.
- **Team-specific requirements:** Confirm internal escalation templates, audience
  boundaries, and ownership expectations before claiming Sentry-wide fit.
- **Question budget:** Test the proposed interaction against real use rather than
  promoting the research heuristic into an unquestioned requirement.
- **Historical validation:** Obtain an authorized corpus and apply the
  [evaluation method](README.md#evaluate-future-historical-cases). Public cases
  support hypotheses, not a causal or representative least-pushback ranking.
- **Runtime promotion:** A later authoring stage renders and validates `SKILL.md`
  before distribution. Spec validation and source review are not behavioral evals
  or installation verification.

## Implementation review

The coordinator authored the [new specification](../../skills/escalation-writing/spec.md)
in the `escalation-writing-spec` worktree after the user approved implementation.
The contract adopts the proposed writing defaults for this version; adoption does
not establish their effectiveness. Research proposals remain distinguishable from
measured results.

A fresh independent advisory reviewer read the spec, its three references, and all
four research documents. This was one reviewer, not a calibrated fusion council or
multi-model consensus. The reviewer assessed all 18 initial scenarios and requested
three repairs:

| Finding                                                                                      | Disposition                                                                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| An unconditional ask requirement could invent actions in an informational update.            | Require an ask only when the artifact seeks action or a decision; add a status-only reply scenario.                                          |
| Counting only answered clarifiers could allow repeated questioning after a decline.          | Count attempts, including unavailable answers; prohibit re-asking without new information or permission; add a declined-detail scenario.     |
| The context reference required a question for policy conflicts that could be safely omitted. | Align it with the spec: identify consequential conflicts, use accurate neutral wording or omission when possible, and ask only when blocked. |

The resulting contract uses a reassessment after two clarifier attempts as a
fatigue checkpoint, not a mandatory intake or a measured optimum. This remains a
candidate for real-use validation. No behavioral evals or runtime installation
were requested or performed. Private-policy alignment remains unverified.

The reviewer subsequently confirmed all three repairs, counted 20 final scenarios
across eight behaviors, and checked relative file links and heading anchors in
the six skill files and four escalation-writing research documents. No unresolved
issue remained in that narrow follow-up. This was a static review, not execution
of the scenarios or a fresh upstream-link sweep.

### Verification recorded on 2026-09-24

- `npx -y @sentry/skillet@latest validate skills/escalation-writing` exits 0:
  spec valid, zero optional eval cases, and the expected missing-`SKILL.md` warning.
- The repository's explicit `.pre-commit-config.yaml` passes all applicable hooks
  on the 16 changed Markdown files: whitespace, final newline, size, private-key
  detection, spelling, and mdformat. YAML/TOML/JSON hooks have no applicable files.
  The first mdformat run changed formatting; the subsequent run passed.
- `git diff --check` passes. The main checkout's unrelated untracked file remains
  outside this worktree.
- No behavioral evals, runtime installation, posting, permission deployment, or
  private-policy compliance check occurred. The GitHub permission work is a
  [global proposal](../gh-read-permissions/README.md), not applied configuration.

### Author-feedback revision on 2026-09-24

D08 arose from the first synthetic demonstration, not a real customer incident.
The original example treated a recorded update time as sufficient to repeat the
promise. The revised contract requires current sender confirmation that the
specific action and timing can be guaranteed, with known dependencies considered.
It identifies the recipient and sender for every draft and explains supported next
steps without converting a request into a promise or narrowing follow-up options.

Four scenarios were added: a customer-specific reply from the sender's role, a
recorded deadline without a current guarantee, an unsupported undated promise,
and a specific guaranteed update that may be communicated. The contract now has
24 scenarios across the same eight behaviors. Earlier counts above describe the
initial review, not this revision.

A fresh independent reviewer inspected this revision and its three references,
D08, and the research synthesis. No actionable issue was found in that scope.
This was static advisory review, not behavioral evaluation or model consensus.
Skillet validation exits 0, with the expected missing-`SKILL.md` warning. All
applicable repository hooks pass on the nine revised Markdown files. Private
voice-policy integration and real-use effectiveness remain unverified.

### Publication checks on 2026-09-24

The required `pre-commit run --all-files` found existing spelling, EOF, and
formatting issues in 21 unrelated files on the `c18d973` baseline. None of the
16 intended files was changed by that run. The automatic unrelated edits were
restored, and the repository-wide cleanup is recorded in `TASKS.md`. This is a
known full-repository check failure, not a claim that all-file checks pass.

Runtime rendering/distribution, private-policy integration, behavioral validation,
global permission adoption, source upkeep, and branch integration are deferred
tasks. The publication milestone covers the reviewed spec and research only.

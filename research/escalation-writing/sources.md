# Escalation-writing sources

Research session: 2026-09-23–24; recorded 2026-09-24.

This register preserves sources behind the [principles](README.md) and
[decisions](decisions.md). “Read” means the source text was retrieved, including
the earlier research retained in this session. It does not mean its effectiveness
was independently measured. Dates do not assert the exact access day of each source.

Use commit-pinned links where available. Version tags identify reviewed releases;
unversioned pages and issue comments remain mutable. Review triggers below concern
active recommendations. Keep historical evidence when a recommendation changes.

## Writing and authoring references

### S01. Plain language

- **Source:** Digital.gov [guide series](https://digital.gov/guides/plain-language)
  and [Writing for understanding](https://digital.gov/guides/plain-language/writing).
- **Type/ref/status:** Official government writing guidance; unversioned; read.
- **Supports:** Write for a specific audience; use short sections, direct verbs,
  and active voice to clarify responsibility. Preserve tense when accuracy needs it.
  This is writing guidance, not evidence of reduced Sentry engineering follow-up.
- **Review trigger:** Guidance revision or a proposed change to the writing rules.

### S02. Library plain-english

- **Source:** bengineerdavis/ai-prompt-library
  [SKILL.md at `172223a`](https://github.com/bengineerdavis/ai-prompt-library/blob/172223afa65f6586a59bf5477e3f001ff32d406c/skills/plain-english/SKILL.md).
- **Type/ref/status:** Public first-party library skill; commit-pinned; read.
- **Supports:** Direct language, consistent terminology, and preservation of
  technical claims, code, quoted speech, and deliberately preserved voice.
  Adapt the meaning-preservation discipline; rigid sentence-length limits are not
  established requirements for every escalation channel.
- **Review trigger:** Library skill revision or conflict with an approved voice policy.

### S03. Library interaction-questioning

- **Source:** bengineerdavis/ai-prompt-library
  [SKILL.md at `94a3156`](https://github.com/bengineerdavis/ai-prompt-library/blob/94a3156b25c6c0112d83341f1002dd2e66c6a8f6/skills/interaction-questioning/SKILL.md).
- **Type/ref/status:** Public first-party library skill, metadata version 2.3.2;
  commit-pinned; read.
- **Supports:** Questions are optional. Read available context first, ask the
  highest-value question, and stop when the next action is clear enough. Its
  default is one question at a time, not a mandatory intake interview.
- **Review trigger:** Library revision or observed question fatigue. Numeric
  question budgets remain proposed heuristics, not measured findings.

### S04. AIHero and Matt Pocock authoring workflow

- **Requested entry points:** [AIHero grill-me](https://www.aihero.dev/skills-grill-me),
  its linked [grill-with-docs](https://aihero.dev/skills-grill-with-docs), and the
  [grilling technique](https://aihero.dev/skills-grilling). All were read in the
  research session; these pages are unversioned.
- **Sources:** mattpocock/skills at `c55ee46`:
  [README](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/README.md),
  [grill-me](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/grill-me/SKILL.md),
  [grill-with-docs](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/engineering/grill-with-docs/SKILL.md),
  and [grilling](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/grilling/SKILL.md).
- **Type/ref/status:** Practitioner-authored skills linked to AIHero by their
  README; commit reference recorded; wrappers and grilling text read.
- **Supports:** Explore dependent design decisions and preserve decisions and
  shared terminology during authoring. The wrappers invoke grilling, with
  domain-modeling added by grill-with-docs.
- **Adaptation boundary:** Authoring-only inspiration. Exhausting every design
  branch, large question rounds, delegation, and confirmation gates are not the
  daily escalation-writing workflow.
- **Review trigger:** Upstream restructuring or a change to the authoring process.

### S05. Cursor unslop

- **Source:** cursor/plugins
  [actual skill at `12d587d`](https://github.com/cursor/plugins/blob/12d587dfb20741cafc376c42c696c5f6e2a64487/pstack/skills/unslop/SKILL.md).
- **Type/ref/status:** Practitioner editing instructions; commit-pinned; read.
- **Supports:** Remove filler, vague attribution, synonym cycling, and needless
  complexity; preserve meaning. Its over-compression warning is useful for tickets.
- **Adaptation boundary:** Reject blanket punctuation bans and universal trigger
  scope. Requests for concrete mechanisms or numbers never authorize inventing them.
- **Review trigger:** Upstream rule revision or a fidelity failure in an edited draft.

### S06. Peter Yang no-ai-slop

- **Sources:** petergyang/no-ai-slop
  [actual skill](https://github.com/petergyang/no-ai-slop/blob/000650b156983f5159695b441477f4e63b25dc85/skills/no-ai-slop/SKILL.md)
  and [eval.md checklist](https://github.com/petergyang/no-ai-slop/blob/000650b156983f5159695b441477f4e63b25dc85/skills/no-ai-slop/eval.md)
  at `000650b`.
- **Type/ref/status:** Practitioner skill and editorial self-check; commit-pinned;
  both read. The checklist is not a reported benchmark result.
- **Supports:** Minimum effective edits, recognizable voice, factual fidelity,
  preserved uncertainty, and a final reader-oriented check. The detect mode
  explicitly rejects guessing AI authorship.
- **Adaptation boundary:** Reject authorship camouflage, arbitrary word or
  punctuation bans, and fabricated specificity. Quantified example rewrites are
  illustrations, not permission to add unsupported measurements. No required
  “What changed” footer in a copy-ready customer reply.
- **Review trigger:** Skill/checklist changes or tension with factual fidelity.

## Escalation and channel guidance

### S07. Sentry bug forms

- **Sources:** [Product form at `14170bd`](https://github.com/getsentry/sentry/blob/14170bd6ae28abe4d4f0b5807185b116f777a1a0/.github/ISSUE_TEMPLATE/bug.yml),
  [JavaScript form at `8f32e18`](https://github.com/getsentry/sentry-javascript/blob/8f32e18517df2a5f4161021e89b3a4dce2fe6189/.github/ISSUE_TEMPLATE/bug.yml),
  [Python form at `bbdf789`](https://github.com/getsentry/sentry-python/blob/bbdf789902e3d8ee7940d7b7442934b0d6b8b30d/.github/ISSUE_TEMPLATE/bug.yml).
- **Type/ref/status:** Maintainer-authored public intake forms; commit-pinned; read.
- **Supports:** Environment, reproduction, expected/actual behavior, versions,
  configuration, and relevant artifacts. Requirements vary by repository and
  integration. Product/JavaScript forms warn about public URL visibility.
- **Limit:** Public contribution requirements are not a complete internal Support
  escalation policy. A required field does not establish a measured benefit.
- **Review trigger:** Destination template or SDK integration changes.

### S08. Sentry public triage

- **Source:** [Public issue process](https://open.sentry.io/triage/).
- **Type/ref/status:** Organizational workflow; unversioned; read.
- **Supports:** Validation, routing, requests for information, and resolution are
  distinct. Sufficient information does not guarantee a fix or delivery date.
  The page explicitly addresses external contributors in public repositories.
- **Review trigger:** Triage ownership, labels, targets, or workflow changes.

### S09. GitLab requests for engineering help

- **Source:** [How to Get Help](https://handbook.gitlab.com/handbook/support/workflows/how-to-get-help/),
  especially “Ask good questions,” “Create a detailed issue,” and “Tips on getting
  timely responses.”
- **Type/ref/status:** Public practitioner handoff workflow; unversioned; read.
- **Supports:** Brief problem summary, clear ask, relevant evidence, prior research,
  customer impact, and appropriate routing. Preserve log excerpts before expiry;
  engineers may lack the reporter's customer access. Too much detail can confuse.
  The guidance explicitly permits asking for help before exhaustive investigation.
- **Review trigger:** Request-for-help process or evidence-access changes.

### S10. GitLab account escalations

- **Source:** [A Support Engineer guide to account escalations](https://handbook.gitlab.com/handbook/support/workflows/escalations-support_engineer/).
- **Type/ref/status:** Public practitioner escalation workflow; unversioned; read.
- **Supports:** Desired customer outcome, technical investigation and mitigation
  notes, a high-level summary, a canonical current record, and audience-specific
  updates. State what happens next and when; make blockers explicit.
- **Limit:** Long-running account escalations can need more process than routine
  daily writing. Do not copy every role or ceremony into the skill.
- **Review trigger:** Escalation or customer-update workflow changes.

### S11. Mozilla bug guidance

- **Source:** [Bug Writing Guidelines](https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html).
- **Type/ref/status:** Maintainer reporting guidance; unversioned; read.
- **Supports:** One issue per report, symptom-based titles, exact reproduction,
  expected/actual behavior, reproducibility frequency, and observations separated
  from speculation. Match artifacts to the failure type.
- **Limit:** Reproduction guidance is not a reason to block an urgent request for
  diagnostic help or an intermittent production-only report.
- **Review trigger:** Reporting guidance changes or a new failure class.

### S12. Tatham practitioner evidence

- **Source:** Simon Tatham, [How to Report Bugs Effectively](https://www.chiark.greenend.org.uk/~sgtatham/bugs.html).
- **Type/ref/status:** First-person maintainer essay; unversioned, copyright 1999;
  read. The page identifies an OpenContent license.
- **Supports:** Exact observations, errors, versions, and reproducible instructions.
  Anecdotes describe repeated one-sentence replies delaying useful information and
  unsupported diagnoses diverting investigation. These are anecdotes, not trials.
- **Review trigger:** Reuse beyond short paraphrase or changed attribution terms.

### S13. Slack threads

- **Source:** [Use threads to organize discussions](https://slack.com/help/articles/115000769927-Use-threads-to-organize-discussions).
- **Type/ref/status:** Official tool documentation; unversioned; read.
- **Supports:** Keep detailed discussion attached to a message, reduce channel
  clutter, and distinguish thread participation from channel-wide visibility.
- **Limit:** Ticket-first coordination is a synthesis with S08–S10, not a Slack
  product requirement.
- **Review trigger:** Thread/notification behavior or coordination policy changes.

### S14. Intercom audience separation

- **Source:** [When to use Back-office tickets](https://www.intercom.com/help/en/articles/8300293-when-to-use-back-office-tickets).
- **Type/ref/status:** Official tool documentation; unversioned; read.
- **Supports:** Separate ownership of resolution and customer communication while
  linking context. Back-office notes are internal; customer replies occur in the
  linked conversation. Ticket sharing is configurable.
- **Limit:** “In Intercom” does not identify the audience. Customer communication
  needs relevant technical detail, not automatic simplification.
- **Review trigger:** Ticket visibility, note behavior, or customer-update policy changes.

### S15. GitHub issue forms

- **Source:** [Syntax for issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms).
- **Type/ref/status:** Official tool documentation; unversioned; read.
- **Supports:** Forms have required/optional fields and produce editable Markdown
  issue bodies. Respect destination requirements without mistaking the form for
  immutable submission-time evidence.
- **Review trigger:** Issue-form schema or destination template changes.

## Compatibility references

### S16. Skillet 1.8.0

- **Sources:** [Published package metadata](https://unpkg.com/@sentry/skillet@1.8.0/package.json),
  [release](https://github.com/getsentry/skillet/releases/tag/1.8.0),
  [specification grammar](https://github.com/getsentry/skillet/blob/1.8.0/docs/src/content/docs/concepts/specifications.md),
  and [CLI reference](https://github.com/getsentry/skillet/blob/1.8.0/docs/src/content/docs/reference/cli.md).
- **Type/ref/status:** Official versioned documentation; 1.8.0; read. During
  implementation, the coordinator also ran `new`, `status`, `instructions spec`,
  and `validate` through `npx -y @sentry/skillet@latest`; the served guidance is
  1.8.0. See the [verification record](decisions.md#implementation-review).
- **Supports:** `spec.md` records intent, triggers, behaviors, and scenarios;
  `status` reports artifact state and next step; `validate` checks core and optional
  eval artifacts. Evals are an explicit optional workflow. The grammar documents a
  version-provenance footer. These facts do not certify the new spec's validity.
- **Review trigger:** Before promotion, a significant Skillet release, or changed
  grammar/status/validation behavior. Validation belongs to the coordinator.

### S17. dotagents 3.1.0

- **Sources:** [Published package metadata](https://unpkg.com/@sentry/dotagents@3.1.0/package.json),
  [README](https://github.com/getsentry/dotagents/blob/3.1.0/README.md),
  [guide](https://github.com/getsentry/dotagents/blob/3.1.0/docs/src/content/docs/guide.mdx),
  and [CLI reference](https://github.com/getsentry/dotagents/blob/3.1.0/docs/src/content/docs/cli.mdx).
- **Copy/discovery evidence:** [Directory copy](https://github.com/getsentry/dotagents/blob/3.1.0/packages/dotagents-lib/src/utils/fs.ts),
  [skill discovery](https://github.com/getsentry/dotagents/blob/3.1.0/packages/dotagents-lib/src/skills/discovery.ts),
  and [installer](https://github.com/getsentry/dotagents/blob/3.1.0/packages/dotagents/src/cli/commands/install/skills.ts).
- **Type/ref/status:** Official versioned documentation; 3.1.0; read, not executed.
- **Supports:** Discoverable skills contain `SKILL.md`. `install` resolves sources,
  copies canonical artifacts, and creates managed projections. Local `path:` sources
  and pinned Git references are supported. Local sources are not a promise of a
  live source-directory link. Global scope is default; project scope is explicit.
- **Limit:** Spec-only research is not an installed runtime skill. Compatibility
  remains an authoring target until the appropriate artifacts and checks exist.
  The reviewed copy implementation filters `.git`, not private reference files.
  Whole-skill exclusions are not per-file privacy controls. No automatic submodule
  initialization is established for distribution.
- **Review trigger:** Before promotion, a significant dotagents release, or changed
  source discovery/copy/scope behavior.

## Public cases and reuse

### S18. Case corpus and licenses

[C01–C08](public-cases.md) hold issue URLs, comment permalinks, fix references,
request histories, and outcome limitations. Their source type is public issue
discussion, supplemented by pull requests and event metadata. All eight visible
issue threads were read; linked external/private artifacts were not automatically
read. Comments are mutable even when their URLs are stable.

Repository license text was checked. These immutable references identify MIT
licenses for the code repositories:

- [Sentry JavaScript at `1b68b7f`](https://github.com/getsentry/sentry-javascript/blob/1b68b7f17b71e80705f052d1002daec7dfb124f0/LICENSE).
- [Sentry Python at `7473afb`](https://github.com/getsentry/sentry-python/blob/7473afb77d7f0ba534bf5fdcd22622b06a5f7e62/LICENSE).
- [pytest at `0d90a31`](https://github.com/pytest-dev/pytest/blob/0d90a31d4a647fa7ba0d53a05b9266c2d4aaa05a/LICENSE).
- [VS Code at `eee5d36`](https://github.com/microsoft/vscode/blob/eee5d36cbf70c906d66bcdc03861b3feaa445d75/LICENSE.txt).

Code licensing does not automatically license every contributor's issue prose.
This record paraphrases findings and retains links, not copied tickets, logs,
screenshots, customer identifiers, or reproduction repositories. Review attribution
and licensing before any substantial reuse. Recheck case outcomes before relying
on their current status; retain the dated historical reading.

### S19. Unavailable private voice policy

- **Source/status:** Notion policy identified in the research handoff; the prior
  attempt exposed a JavaScript-only page, not readable policy content. No policy
  text was available to this research owner. This is an access limitation, not evidence.
- **Use:** None until the user supplies an authorized readable version. Do not
  infer its rules or put its internal URL into portable skill material.
- **Review trigger:** Authorized policy access or a user-supplied export. Voice-policy
  integration and the user's own escalation corpus remain pending.

## Retrieval notes

Initial candidate URLs were corrected rather than treated as evidence: the old
GitLab escalations URL returned 403/404; Sentry's `/contributing/` candidate returned
a not-found page. An Intercom article guessed by slug resolved to unrelated privacy
content. Cursor's guessed standalone repository/blog and AIHero's guessed
`/grill-me` page returned 404; S04 and S05 identify the actual source files.
The dotagents 3.1.0 package README URL returned 404; its tagged repository docs were
read instead. No failed URL supports a claim.

The pinned sources and selected public GitHub threads were accessible. No private
repository, Slack, Intercom conversation, Linear issue, or Sentry event was accessed.

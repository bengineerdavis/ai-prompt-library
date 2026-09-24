# TASKS.md

Shared work queue for this repository. Read at the start of a session; update
it before you finish. Conventions mirror the dotfiles repository's TASKS.md:
one line per item with a done-condition, `[blocked: reason]` rather than
deletion, owner named `[me]`, and captures commit immediately and separately.

## Now

- **Refine recipient and expectation handling.** [agent: coordinator, completed 2026-09-24]
  Worktree `ai-prompt-library-escalation-writing`. Apply the author's feedback to
  customer replies: identify the recipient and sender, distinguish requested next
  steps from promises, and preserve follow-up options without unsupported commitments.
  Done when the spec, references, and decision record agree and scoped checks pass.
  **Done:** D08 records the feedback. The revised spec has eight behaviors and
  24 scenarios; Skillet validation and applicable hooks pass on all nine revised
  files. The missing-runtime warning remains expected for the spec-only scope.

- **Review the customer-expectation revision.** [agent: expectation-reviewer, completed 2026-09-24]
  Same worktree. Check old commitments, event-based promises, recipient context,
  and a permitted guaranteed commitment. Done when findings have dispositions.
  **Done:** Independent targeted review found no actionable issue; all three
  references and the research synthesis agree with the revised contract.

- **Preserve escalation-writing research.** [agent: escalation-research, completed 2026-09-24]
  Worktree `ai-prompt-library-escalation-writing`, branch `escalation-writing-spec`.
  Save the public sources, eight case analyses, limitations, proposed principles,
  and decisions under `research/escalation-writing/`. Done when claims link to
  evidence and private-policy integration is explicitly pending.
  **Done:** Four linked records preserve the sources, eight public cases, and
  decisions under `research/escalation-writing/`.

- **Record the global GitHub CLI permission proposal.** [agent: gh-research, completed 2026-09-24]
  Same worktree. Save the verified read-oriented command rules and API approval
  fallback under `research/gh-read-permissions/`. Done when the proposal states
  its limits and no live or chezmoi-managed configuration has changed.
  **Done:** The proposal and verified limits are recorded; configuration is unchanged.

- **Author the escalation-writing contract.** [agent: coordinator, completed 2026-09-24]
  Same worktree. Create a new spec-only skill with portable public references,
  separate from `support-escalation`. Done when current Skillet validation and
  scoped repository hooks pass, and independent review findings are addressed.
  **Done:** Eight behaviors and 20 scenarios pass Skillet 1.8.0 validation; all
  applicable hooks pass on the 16 changed files. `SKILL.md` is absent by the
  approved spec-only scope. Evidence: `research/escalation-writing/decisions.md`.

- **Review the escalation-writing contract.** [agent: contract-reviewer, completed 2026-09-24]
  Same worktree. Check factual fidelity, humane writing, question fatigue,
  audience boundaries, and research traceability. Done when findings have
  concrete dispositions; this is advisory review, not calibrated model consensus.
  **Done:** Three findings repaired and confirmed; local file links and heading
  anchors checked. Behavioral effectiveness and private-policy alignment remain unverified.

- **Build the research swarm — a research-agency process adapted from
  testdouble/han.** Author request 2026-09-19: study han-research liberally
  (MIT), extract into general practices, land as skills + reference rules in
  `skills/research/`. Decisions locked with the author: validator is the
  calibrated fusion council (not a single agent); first pilot is the
  dotfiles `requirements.yml` pin policy. **DONE (2026-09-19):** the three
  reference rules + research skill + two dispatch templates + report
  template authored with MIT attribution (0aa0e2b); one council round
  attacked the draft, all findings applied — trust classes split state from
  self-description (governance docs are provided-class; session artifacts
  are derived), the codebase lane is its own dispatch, failed analysts are
  no-evidence-labeled findings, claim tagging is mechanical, judge budget
  decouples by band (dda72c4). **PILOT DONE (2026-09-19):**
  `skills/research/pilots/2026-09-19-requirements-pin.md` — the pin question
  ran end to end (medium band, 2 web analysts + codebase lane + 1-judge
  validation), the no-evidence path was exercised for real (the supply-chain
  attack-surface claim deferred with triggers), and the validator refuted
  the initial recommendation into an honest no-clear-winner (pin yes; shape
  unsettled on automation appetite / grade-linkage / staleness). The run
  also caught a real process gap: the web-isolation contract is not
  mechanically enforced by the dispatch machinery (subagents run inside the
  repo with file tools) — fix queued with the skill. **Eval decision
  (2026-09-19, made by the evidence rule itself):** formal skillet eval
  cases are DEFERRED with a reopen trigger — one pilot is thin class
  understanding, and the house doctrine writes cases from a problem class,
  not a single run. Reopen after 3 real pilots or the first real failure
  class; pilot 1 stands as interim evidence. The isolation constraint is
  now recorded in the SKILL.md (brief-level, not mechanical, with the
  current dispatch machinery; compensating controls in place; mechanical
  enforcement queued for the R&D factory).
  [agent: chezmoi session]

## Planned

- **Resolve the repository-wide documentation hook findings.** [unassigned]
  `pre-commit run --all-files` during escalation-writing publication found five
  spelling reports plus EOF/formatting changes across 21 existing files under
  `skills/aboyeur/`, `skills/commit-hygiene/`, `skills/research/`, and
  `skills/skillify/`, based on `c18d973`. Review terminology false positives
  before changing text or adding ignore words. Done when
  the full hook run passes without silently altering vendored meaning or stale
  spec hashes. The automatic unrelated edits were restored; scoped checks for
  escalation-writing pass.

- **Integrate the escalation-writing branch.** [unassigned]
  Review `escalation-writing-spec` after publication. Done when the reviewed
  spec, research records, and follow-ups are integrated into `main`. Commit and
  branch publication do not install the skill.

- **Render escalation-writing for runtime use.** [unassigned]
  Follow current Skillet instructions to derive `SKILL.md` from the reviewed
  spec, refresh its hash, and validate it. Done when the public skill works from
  its own directory and a reviewed dotagents installation discovers it with all
  required references. Keep private reference packs outside the managed directory.

- **Integrate the private escalation voice policy.** [unassigned]
  [blocked: an authorized readable policy is not available]
  Use the external reference contract to reconcile the policy with the portable
  writing rules. Done when applicable requirements and conflicts are recorded in
  the private context and the skill can apply them without copying private content
  into this repository. Until then, organization-policy alignment is unverified.

- **Validate escalation-writing behavior in use.** [unassigned]
  After runtime rendering, select meaningful scenarios and an authorized pilot.
  Include recipient awareness, unsupported promises, evidence fidelity, and
  question fatigue. Done when results and limitations are recorded and material
  failures are addressed. Use synthetic eval fixtures; real-use observations and
  private examples remain outside the public repository. Do not treat a static
  spec check or the demonstration as a behavioral evaluation.

- **Review adoption of the global GitHub CLI permission proposal.** [unassigned]
  Recheck `research/gh-read-permissions/README.md` against installed tool versions
  and the effective global configuration, including the reported duplicate
  fallback. Done when a decision is recorded and, if approved, the configuration
  is validated in its owning repository and verified after restart. Keep API calls
  on `ask` unless a separately reviewed mechanism establishes narrower guarantees.

- **Review active research sources for updates.** [unassigned]
  Recheck affected references before runtime promotion or a principle revision.
  Use 2026-12-24 as the proposed first routine review date for active material.
  Done when `research/` records checked revisions, changed claims, and any decision
  updates. No scheduled automation or submodule adoption is implied.

- **Mechanically enforce web-isolation for research analysts.** The pilot
  (2026-09-19, V3) proved the current dispatch machinery cannot enforce the
  contract: a web-briefed analyst ran inside the repo with file tools and
  read local files despite the forbidding brief. **Landed (2026-09-19):**
  the detective half — `skills/research/tools/isolation_check.py`, a tested
  post-hoc provenance gate (7 tests incl. the real pilot-breach shape;
  mutation-proven) wired into the SKILL.md compile step: every web-briefed
  analyst's return is scanned before the registry compiles, breaches are
  disclosed and reclassified, never silently kept. The known constraint is
  recorded in the SKILL.md: the gate makes breaches impossible to hide, not
  impossible to commit. **Deferred (the preventive half):** a sandboxed
  dispatcher, or analysts run from a cwd outside the repo — the task tool
  provides neither sandbox nor cwd control today. **Reopen when** the
  dispatch machinery gains either. Done-condition amended accordingly: the
  detection gate is the enforceable half until the machinery changes.
  Feeds the R&D factory's research method.

- Council review: multi-machine privacy design for the dotfiles repo. The
  author's requirement, refined 2026-09-12: committed artifacts must be
  environment-general — no machine identification and no obfuscation signaling
  (a hostile reader deduces nothing about topology, machine count, or the
  existence of sensitive work); ZDR engagements carry handover context locally,
  discardable, promotable only after pseudo-anonymization via the
  pii-redactor skill and an explicit author selection. The research record is
  written and waiting: `dotfiles/docs/MULTI-MACHINE.md` in the dotfiles repo
  (requirement, audited leaks, survey, design, rejections, four open
  questions). **Workflow for whoever picks this up: (1) run
  `interaction-questioning` first — stress the requirement and the four open
  questions, add anything the research missed, and send back anything
  mis-framed per the review-best-practices pairing; (2) record the refined
  research request as the council's input document; (3) convene a
  panel-of-judges advisory council (bundle.advisory-meeting-with-research
  shape: facilitator, note-taker, a privacy/due-diligence advisor; consult the
  recruiter on whether a standing privacy-advisor role should exist — first
  dogfood of its queued adaptation); (4) verdicts and rejections go back into
  MULTI-MACHINE.md's council section. Done when the four open questions each
  have a council answer recorded there, or a marked refusal to answer.**

- Fix the prek hook coverage gap: every commit's hooks report
  "Running in workspace: .../ai-prompt-library/impromptu" and skip with no
  files to check — prek resolves to the nested impromptu directory, so
  trailing-whitespace, end-of-file, markdownlint and the rest never run on
  real changes (observed 2026-09-12 on both the skills move and the TASKS.md
  adoption). Done when a commit touching skills/ runs the hooks for real or
  the workspace resolution is fixed.

- Run the eval suites for the skills in this repository (`commit-hygiene`, 5
  cases; `pii-redaction`, 6; `review-best-practices`, 5;
  `interaction-questioning`, 14). No case has ever been executed. Re-homed
  here from the dotfiles repo on 2026-09-12: the eval gate for skill
  promotion is policy there, so these verdicts feed it. **\[blocked: harness
  credentials — codex 0.154.0 is installed but `codex login status` reports
  not logged in on the Linux box; skillet defaults to the codex harness,
  `--harness claude` is the alternative if Claude Code is authed.\]**
  `--baseline` is the number that matters — lift without the skill. Expect
  to fix cases, not just read results.

- Adapt the recruiter role for AI artifacts. The current recruiter
  (`prompts/panel-of-judges/roles/recruiter.md`, v1.0) screens *human*
  financial advisors; the author's need is recruiting and reviewing AI
  roles — which default to being agent definitions (decision 2026-09-12).
  Split advisor-screening from role-design duties, add an AI-role rubric
  (trigger scope, tool permissions, spec coverage, composability with
  AGENTS.md files), and make it the first specimen of the role-evaluation
  method below. Done when `recruiter.md` is refactored per its own
  evaluation and a role-spec format draft exists.

- Build a spec-authoring skill for AI artifacts — the system-wide complement
  to skillet: agent definitions and skills as one spec-driven artifact
  class. Includes an evaluation mode that recommends refactors — split,
  more specific, more general — with composability against AGENTS.md files
  as an explicit check. Installs system-wide via dotagents from this
  repository. Name not settled. Done when the skill exists, installs via
  `dotagents add` from here, and has evaluated one real role (the
  recruiter, dogfood).

- Run the role evaluation over existing roles — panel-of-judges roles first
  (advisors, chair, facilitator, judges, note-taker, specialists, trainer),
  then runtime agent definitions. Done when recommendations exist for each
  and are triaged into items or declined with a reason.

- Research the agent→function graduation threshold, then convene the
  panel-of-judges council to decide it. Principle under test: a trusted
  function is preferable to agent judgment wherever the task is mechanical —
  agents and models are reserved for adaptability and interpretation
  (high-context tasks: deciding what to do, how to succeed). Survey existing
  practice (guardrails, evals, deterministic post-processing), gather
  candidate cases from the dotfiles repo (its determinant-detection
  requirement in `ROADMAP.md` is the first), and produce a reusable policy
  artifact: the threshold, the decision procedure, worked examples. Done
  when the artifact exists here and the dotfiles repo's AGENTS.md references
  it.

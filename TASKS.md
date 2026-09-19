# TASKS.md

Shared work queue for this repository. Read at the start of a session; update
it before you finish. Conventions mirror the dotfiles repository's TASKS.md:
one line per item with a done-condition, `[blocked: reason]` rather than
deletion, owner named `[me]`, and captures commit immediately and separately.

## Now

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
  decouples by band (dda72c4). **REMAINS:** the pilot end to end — the pin
  question PLUS an engineered no-evidence sub-angle (the pin question has
  abundant web evidence; the defer-with-reopen path must be exercised
  deliberately), following skills/research/SKILL.md as written. Formal
  skillet spec + evals: queued decision, pilot is interim evidence.
  [agent: chezmoi session]

## Planned

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
  promotion is policy there, so these verdicts feed it. **[blocked: harness
  credentials — codex 0.154.0 is installed but `codex login status` reports
  not logged in on the Linux box; skillet defaults to the codex harness,
  `--harness claude` is the alternative if Claude Code is authed.]**
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

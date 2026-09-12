# TASKS.md

Shared work queue for this repository. Read at the start of a session; update
it before you finish. Conventions mirror the dotfiles repository's TASKS.md:
one line per item with a done-condition, `[blocked: reason]` rather than
deletion, owner named `[me]`, and captures commit immediately and separately.

## Now

Nothing scheduled — items land here when picked up.

## Planned

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

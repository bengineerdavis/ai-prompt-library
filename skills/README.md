# Skills

Agent skills authored as **specs with mechanical evals**, using
[skillet](https://www.npmjs.com/package/@sentry/skillet).

These differ from the conversational skills under
`prompts/panel-of-judges/skills/`. Those are inlined into a bundled session by
`bundle.py` and describe how a role should behave in a meeting. The skills here
are cross-cutting engineering rules that apply to any project, and each one
carries executable eval cases — so "does the agent actually follow this" is a
command, not an opinion.

## Layout

```
skills/<name>/
  spec.md            source of truth — Intent / Triggers / Behaviors / Constraints
  SKILL.md           the runtime text an agent loads (rendered from spec.md)
  evals/cases/       one YAML case per behavior
  evals/fixtures/    starting workspaces the cases run against
```

`spec.md` is the contract and the thing to review in diffs. `SKILL.md` is
derived from it and pins `spec_hash` so drift is detectable.

## Working on a skill

```bash
cd skills/<name>
npx -y @sentry/skillet@latest status      # what exists, what is next
npx -y @sentry/skillet@latest validate    # grammar, frontmatter, eval coverage — no LLM
npx -y @sentry/skillet@latest eval        # run the cases through the harness
npx -y @sentry/skillet@latest eval --baseline   # compare pass rates without the skill installed
```

Edit `spec.md` first, then re-render `SKILL.md` and refresh its `spec_hash`
(`status --json` → `.spec.hash`). Behavior names slugify into the ids eval cases
reference, so renaming a behavior means updating its case.

## Referencing a skill from a local environment

Skills distribute through [dotagents](https://github.com/getsentry/dotagents):
`~/.agents/agents.toml` declares the sources — this repo is trusted and
wildcarded — and `agents.lock` pins the resolved commit. dotagents installs
skills into the canonical store `~/.agents/skills/` and symlinks them into each
agent runtime's skills directory; `~/.claude/skills` is itself a symlink to
`~/.agents/skills`.

Because dotagents resolves from this repo's GitHub remote at a commit, a new or
changed skill only installs after it is committed **and pushed**, then:

```bash
dotagents install      # resolves the pushed commit, updates agents.lock, wires the links
dotagents list         # confirm the skill is declared
dotagents doctor --fix # repair wiring if anything looks off
```

The decision record — dotagents over skills.sh and per-tool config — lives in
`dotfiles/docs/AGENT-ARTIFACTS.md` in the dotfiles repo.

## Skills

| Skill                                        | Purpose                                                                                                                  |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [aboyeur](aboyeur/)                          | Reads a repo's own files and generates its `mise.toml`: tools, env, wired tasks, system packages, cross-platform checks.  |
| [commit-hygiene](commit-hygiene/)            | One logical change per commit, message sized to the change, commit by path, verify the contents afterwards.              |
| [interaction-questioning](interaction-questioning/) | Discovers and confirms the user's real goal with adaptive, one-question-at-a-time questioning.                     |
| [model-fitness](model-fitness/)              | Decides whether a model is fit for a named role from measurements on the deciding machine, not published benchmarks.      |
| [pii-redaction](pii-redaction/)              | How to build and review PII redaction tools: deterministic patterns → model pass → leak verification that fails closed.   |
| [plain-english](plain-english/)              | Edits technical prose to the Google Developer Documentation Style Guide core.                                             |
| [review-best-practices](review-best-practices/) | Researches what exists, ranks options against the requirement, records what was rejected before a plan commits.         |
| [skillify](skillify/)                        | Authors a skill with skillet and lands it in this library, stopping at the dotagents review gate.                          |
| support-escalation                           | Spec + evals only — the `escalate` behavior contract; no SKILL.md rendered yet.                                           |

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

Nothing here installs itself — this repo stays the single source of truth and
consumers point at it. To use one with Claude Code, symlink it into the
user-level skill directory it already discovers:

```bash
mkdir -p ~/.claude/skills
ln -s ~/code/personal/ai-prompt-library/skills/pii-redaction ~/.claude/skills/pii-redaction
```

A symlink rather than a copy: edits land in the library, get committed here, and
every environment picks them up. `~/.claude/` is deliberately not managed by
chezmoi (it is ignored as dev tooling), so the link is per-machine setup.

## Skills

| Skill                             | Purpose                                                                                                                 |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [pii-redaction](pii-redaction/)   | How to build and review PII redaction tools: deterministic patterns → model pass → leak verification that fails closed. |
| [commit-hygiene](commit-hygiene/) | One logical change per commit, message sized to the change, commit by path, verify the contents afterwards.             |

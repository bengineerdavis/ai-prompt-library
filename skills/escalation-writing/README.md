# Escalation writing

**Spec-only.** This directory defines a portable writing contract; it does not yet
contain a `SKILL.md` that dotagents or an agent runtime can load.

The skill helps draft and revise engineering escalations and their Slack and
Intercom follow-ups. Its goal is accurate, considerate writing with useful
channel-specific structure and few unnecessary questions. It does not aim to
conceal AI use.

## Contents

- [spec.md](spec.md): the Skillet behavior contract and acceptance scenarios.
- [Writing principles](references/writing-principles.md): public editorial guidance.
- [Channel patterns](references/channel-patterns.md): engineering tickets,
  coordination messages, internal handoffs, and customer replies.
- [Context contract](references/context-contract.md): replaceable organization
  references, missing-policy handling, and distribution boundaries.

The repository's
[research record](../../research/escalation-writing/README.md) contains the sources,
eight public case histories, decisions, and limitations. That link is for source
maintainers; the eventual runtime must not depend on the research directory.

The existing `support-escalation` terminal-tool specification is separate. This
skill does not adopt its mandatory JSON output, severity scheme, model-routing
commands, or exclusion of customer-facing replies.

## Validate the spec

From the repository root:

```sh
npx -y @sentry/skillet@latest status skills/escalation-writing --json
npx -y @sentry/skillet@latest validate skills/escalation-writing
```

A valid spec-only directory can report that `SKILL.md` is missing. That warning
marks the next authoring stage, not an installable skill. Scenarios in the spec
are acceptance examples; they are not executed evals.

## Continue to a distributable skill

When runtime authoring is requested, follow the current CLI's next step and fetch:

```sh
npx -y @sentry/skillet@latest instructions skill skills/escalation-writing --json
```

Render `SKILL.md` from the reviewed spec, record its current `spec_hash`, and use
the repository's frontmatter conventions. Validate again. Before distribution,
check that the skill works with only its own public files and that the selected
dotagents version's discovery and copying behavior still matches the context
contract. A research link or spec-only directory does not make a runtime skill.

Private voice-policy alignment, behavioral effectiveness, and runtime installation
remain unverified. No private organization policy contents are included here.

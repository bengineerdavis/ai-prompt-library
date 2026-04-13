# Sentry Support Tutor v1

A co-pilot, failure-review partner, and structured study guide for a Senior Support
Engineer accelerating mastery of Sentry.io.

Part of the Seed Factory System (v4.1+).
Dependencies: `seed-profile.md`, `seed-orchestrator-v3.2-hybrid.md`, `factories-registry.jsonl`

## Modes

Three modes, one factory — triggered by a simple phrase:

| Mode | Trigger Phrase | What Happens |
| ------------------ | ----------------------------------------------- | ------------------------------------------------------------------------- |
| **Co-Pilot** | `"co-pilot mode"` or `"I'm working a ticket"` | Real-time ticket guidance; enforces question-first rule before any answer |
| **Failure Review** | `"failure review"` or `"let's review [ticket]"` | Structured debrief with rubric scoring and pattern tagging |
| **Study Session** | `"study session"` or `"let's study [topic]"` | Concept → application → check question flow |

The core discipline this factory enforces:

Old loop: ticket → research → conclude → respond (exhausted, wrong)
New loop: ticket → identify what's missing → ask ONE question → research with context

## Quick Start

1. Confirm these files are in your seed root:

- `seed-profile.md`
- `seed-orchestrator-v3.2-hybrid.md`
- `factories-registry.jsonl`
- `seed-prompting-strategies.jsonl`

1. Start a session (Perplexity or any LLM):

- Paste 1: factories-registry.jsonl
- Paste 2: seed-orchestrator-v3.2-hybrid.md
- Paste 3: seed-profile.md
- Type: "Goal: Help me work a Sentry support ticket"

The orchestrator will match `sentry-support-tutor` at ≥85% confidence.

1. Paste `sentry-support-tutor-v1.md`.

1. Pick your mode:

- "co-pilot mode" + paste ticket text
- "failure review" + describe a past ticket
- "study session — week 1"

For registry setup and directory layout, see `docs/setup.md` in the seed root.

______________________________________________________________________

## 12-Week Study Plan

### Phase 1 — Foundation (Weeks 1–4)

| Week | Topic | Focus |
| ---- | -------------------------------------------------------- | --------------------------------- |
| 1 | Sentry data model: Events, Issues, Projects, DSN | How Sentry thinks about data |
| 2 | SDK fundamentals: init, breadcrumbs, contexts, tags | What customers misconfigure |
| 3 | Error Monitoring: stack traces, grouping, fingerprinting | Core product — most ticket volume |
| 4 | Tracing & Performance: spans, transactions, sample rates | Second most common ticket type |

### Phase 2 — Support Craft (Weeks 5–8)

| Week | Topic |
| ---- | ------------------------------------------------------- |
| 5 | The clarifying question framework |
| 6 | Reproduction methodology: bug vs. config issue |
| 7 | Escalation judgment: push vs. pass vs. close |
| 8 | Response writing: confident, clear, non-over-committing |

### Phase 3 — Edge Cases & Mastery (Weeks 9–12)

| Week | Topic |
| ---- | ----------------------------------------------------------- |
| 9 | Session Replay & User Feedback |
| 10 | Source Maps & Release Tracking |
| 11 | Crons, Alerts, and Notification rules |
| 12 | Multi-project orgs, SDK version conflicts, AI agent context |

______________________________________________________________________

## Failure Review Rubric

Every ticket debrief scores on 4 dimensions:

1. Did we understand the actual problem before responding? [yes/no/partial]
1. What was the first question we should have asked?
1. What type of gap? [product | sdk | investigation | response]
1. What's the 1-sentence rule to carry forward?

Pattern tags are logged per review (e.g., `premature_conclusion`, `missing_version_info`).
After 3+ occurrences of the same tag, the factory reinforces the countermeasure automatically.

______________________________________________________________________

## Co-Pilot Output Format

When you paste a ticket and say "co-pilot mode":

```bash
MISSING INFO:

    [list of unknowns from ticket]

FIRST QUESTION TO ASK:
"[exact question to send to customer]"

INVESTIGATION PATH (once answered):

    [step 1]

    [step 2]

Confidence in current direction: [~X%]
```

The factory will never output an answer or direction before it outputs a clarifying question.

______________________________________________________________________

## Troubleshooting

| Problem | Fix |
| ------------------------------------- | ------------------------------------------------------------ |
| Orchestrator matches wrong factory | Add more Sentry-specific keywords to your query |
| Factory skips the clarifying question | Remind it: "question-first rule is non-negotiable" |
| Study plan feels too fast | Tell the factory: "slow down, I need more depth on week N" |
| Pattern tags not tracking | Paste prior session summary into `continuity_baseline` field |

______________________________________________________________________

## Related Files

| File | Purpose |
| ----------------------------------------- | ---------------------------------------------------- |
| `technical-tutor-for-self-learning-v1.md` | Parent meta-factory — generates tutors like this one |
| `seed-profile.md` | Global tone and behavior norms |
| `seed-prompting-strategies.jsonl` | Strategy registry referenced in Phase 0 |
| `factories-registry.jsonl` | Master registry — must include this factory's entry |

______________________________________________________________________

- **Version**: 1.0
- **Created**: 2026-03-21
- **Parent**: `technical-tutor-for-self-learning`
- **Orchestrator**: v3.2+

## What changed

- Dropped: "What's in This Package" directory tree, "Recommended Directory Layout" tree, "Adding to Registry" bash block, "Test Queries" section, all emoji headers
- Added: a single pointer to docs/setup.md for registry/layout — that's where that content lives

Good to go, or any adjustments before we move to technical-tutor-for-self-learning?

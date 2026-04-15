# Wealth Advisor & Builder v1

A structured wealth planning factory for mid-career catch-up scenarios — employment
risk, Boglehead-style portfolio allocation, safe withdrawal rate (SWR) calculations, and
runway modeling.

Part of the Seed Factory System (v4.1+). Dependencies: `seed-profile.md`,
`seed-orchestrator-v3.2-hybrid.md`, `factories-registry.jsonl` Parents:
`strategy-builder`, `shopping-builder`

______________________________________________________________________

## What This Factory Does

Given a user’s age, target spending, and employment risk profile, the factory runs four
sequential phases:

Phase 0 → Context intake: age, unemployment risk, spending target, timeline Phase 1 →
Numeric modeling: SWR table, portfolio target range, runway calculation Phase 2 →
Output: Snapshot + Runway + Allocation + Roadmap + Risk flags Tail → Scores output
(rubric) and appends result to factories-registry.jsonl

text

**Example:**

Query: “wealth plan age 40 unemployed 2-6 months 70-95k expenses Boglehead” Match:
wealth-advisor-and-builder (92%) Phase 1: SWR 3–4% → Portfolio target: $1.75M–$3.2M
table + runway calc Phase 2: Snapshot + Runway + Allocation + Roadmap + Risks Tail:
Score: 8.7 → appended to registry

text

______________________________________________________________________

## Quick Start

1. Confirm these files are in your seed root:

   - `seed-profile.md`
   - `seed-orchestrator-v3.2-hybrid.md`
   - `factories-registry.jsonl`
   - `seed-prompting-strategies.jsonl`

1. Start a session:

Paste 1: factories-registry.jsonl Paste 2: seed-orchestrator-v3.2-hybrid.md Paste 3:
seed-profile.md Type: “wealth plan age 40 behind schedule 70k expenses”

text The orchestrator will match this factory at ≥85% confidence.

1. Paste `wealth-advisor-and-builder-v1.md`.

For registry setup and directory layout, see `docs/setup.md` in the seed root.

______________________________________________________________________

## Query Match Examples

**High confidence (90%+):**

“wealth plan age 40 behind schedule 70k expenses” "boglehead 2025 unemployment risk
runway calculation" “SWR for 95k spending what portfolio size”

text

**Medium confidence (80–89%):**

“retirement podcasts starting late” "financial independence age 40 tech job loss" “safe
withdrawal rate current conditions”

text

If match score falls below 75%, add specific keywords from the high-confidence examples
above to your query.

______________________________________________________________________

## Monitoring & Iteration

After 5+ executions, check `avg_score` in the registry:

- Score ≥ 8.0 — factory is performing well
- Score < 8.0 — refine Phase 1 sub-phases
- Score > 10 wealth queries — consider splitting into `runway-builder-v1.md` +
  `swr-calculator-v1.md`

Scan `feedback_history` entries for missing task coverage (tax, RSU, health).

______________________________________________________________________

## Troubleshooting

| Issue                   | Fix                                                                       |
| ----------------------- | ------------------------------------------------------------------------- |
| Match < 75%             | Add query keywords to the `keywords` array in the registry entry          |
| Phase 0 fails           | Verify `seed-prompting-strategies.jsonl` has `"enabled": true` strategies |
| Parents not found       | Ensure `strategy-builder` and `shopping-builder` exist in registry        |
| Tail Module not writing | Check write permissions on `factories-registry.jsonl`                     |

______________________________________________________________________

## Related Files

| File                               | Purpose                                             |
| ---------------------------------- | --------------------------------------------------- |
| `wealth-advisor-and-builder-v1.md` | Main factory prompt                                 |
| `strategy-builder.md`              | Required parent factory                             |
| `shopping-builder.md`              | Required parent factory                             |
| `factories-registry.jsonl`         | Master registry — must include this factory’s entry |

______________________________________________________________________

**Version**: 1.0 · **Last Updated**: 2025-12-08 · **Orchestrator**: v3.2+ · **Avg
Score**: 8.73

# Quickstart

Get a working Seed session in under 2 minutes.

______________________________________________________________________

## Option 1 — Perplexity or any LLM (no coding)

```bash
Paste 1: factories-registry.jsonl
Paste 2: seed-orchestrator-v3.2-hybrid.md
Paste 3: seed-profile.md
Type:    "Goal: [what you want to do]"
```

The orchestrator matches a factory at ≥85% confidence and tells you what to paste next.
You never need more than 3 pastes at once.

**Example:**

```bash
Type:    "Goal: Help me learn Kubernetes for my new platform engineering role"
Match:   technical-tutor-for-self-learning (91%)
Action:  Paste technical-tutor-for-self-learning-v1.md
Result:  Intake questions → study plan → tutor deployed
```

## Option 2 — Bash (one-liner match)

```bash
./orchestrator-match.sh "your query here" factories-registry.jsonl
```

Returns the top factory match and confidence score. Paste the matched factory into
your LLM session to run it.

______________________________________________________________________

## Option 3 — Python

```python
from orchestrator import Orchestrator, Registry

registry = Registry.load("factories-registry.jsonl")
orch = Orchestrator(registry)
match = orch.match_factory("your query here")
print(f"Match: {match.factory} ({match.confidence:.1%})")
```

## Match Confidence Thresholds

| Score | Behavior |
| ------ | ------------------------------- |
| ≥90% | Auto-runs factory |
| 85–89% | Asks to confirm (default yes) |
| 75–84% | Shows top 3, asks you to pick |
| \<75% | Suggests creating a new factory |

## Troubleshooting

| Problem | Fix |
| ---------------------- | ---------------------------------------------------------------------------------- |
| No factory match | Rephrase query with more specific keywords |
| Wrong factory selected | Add domain-specific terms (e.g. "sentry", "boglehead", "tutor") |
| Python ImportError | Confirm `orchestrator.py` and `factories-registry.jsonl` are in the same directory |
| Bash permission denied | `chmod +x orchestrator-match.sh` |
| Perplexity paste error | Paste registry first, then orchestrator |

For registry setup, adding new factories, and full directory layout, see `docs/setup.md`.

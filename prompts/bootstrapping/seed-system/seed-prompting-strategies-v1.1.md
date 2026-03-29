# seed-prompting-strategies — Living Registry of Prompting Strategies

**Version**: v1.1 | **Updated**: 2026-03-28 | **Data file**: `seed-prompting-strategies-v1.1.jsonl`

This is a living, continuously-updated registry of prompting strategies available to Seed factories.
Each line in the `.jsonl` file is a JSON object representing one strategy.
Factories reference this registry dynamically in Phase 0.

> ⚠️ JSONL format does not support inline comments. All documentation lives here.
> The `.jsonl` file must remain pure JSON lines for parser compatibility.

---

## Strategy Schema

```json
{
  "name": "Strategy Name",
  "version": "1.0",
  "enabled": true,
  "description": "What this strategy does and when to use it",
  "implementation": "Detailed execution steps or reference",
  "effectiveness": 0.85,
  "best_for": ["use case 1", "use case 2"],
  "requires_multiple_runs": false,
  "computational_cost": "low|medium|high",
  "model_compatibility": ["perplexity", "qwen", "claude"],
  "added": "YYYY-MM-DD",
  "updated": "YYYY-MM-DD",
  "research_ref": "Paper, blog, or source where this was validated",
  "tags": ["reasoning", "optimization", "validation"]
}
```

---

## Current Strategies (v1.1 — 13 total)

### Core Strategies (v1.0 — original starter set, 2025-12-05)

| Name | Effectiveness | Cost | Phase | Tags |
|---|---|---|---|---|
| Decomposition | 0.89 | low | 1 | reasoning, structuring |
| Chain-of-Thought | 0.87 | low | 1 | reasoning, transparency |
| Few-Shot | 0.88 | low | 1 | learning, comparison |
| Constraint-Based-Reasoning | 0.86 | low | 1 | optimization, filtering |
| Rubric-Based-Scoring | 0.87 | low | 2 | evaluation, scoring |
| Self-Critique | 0.84 | medium | 2 | validation, feedback |
| Meta-Prompting | 0.82 | medium | 1 | reasoning, context |
| Perspective-Taking | 0.80 | medium | 1 | reasoning, bias-checking |
| Community-Wisdom-Injection | 0.78 | medium | 1 | research, social-proof |
| Self-Consistency | 0.85 | high | 1 | validation, robustness |

### Council Strategies (v1.1 — added 2026-03-28)

| Name | Effectiveness | Cost | Use When |
|---|---|---|---|
| Model-Council-Judge | 0.91 | high | Judging candidates across 2-3 models; decouples generator from judge to eliminate Self-Critique grade inflation |
| Model-Council-Generate | 0.88 | high | Generating candidates from 2-3 models in parallel; meta-factories, recursive prompts |
| Mixture-of-Roles | 0.83 | medium | Single-model fallback: simulate council via Skeptic / Domain Expert / Pragmatist roles |

**Decision guide for council strategies:**

| Context | Use |
|---|---|
| Multi-model available + meta-factory | `Model-Council-Generate` → `Model-Council-Judge` |
| Multi-model available + judging only | `Model-Council-Judge` alone |
| Single-model (Perplexity manual mode) | `Mixture-of-Roles` |
| Budget-constrained, any context | `Mixture-of-Roles` |

---

## How to Use This Registry

### For Factory Developers

In Phase 0, reference this registry dynamically:

```bash
# Load all enabled strategies
jq 'select(.enabled == true) | .name' seed-prompting-strategies-v1.1.jsonl

# Rank by effectiveness
jq -s 'sort_by(-.effectiveness)[] | "\(.effectiveness) \(.name)"' seed-prompting-strategies-v1.1.jsonl

# Filter by cost
jq 'select(.computational_cost == "low") | .name' seed-prompting-strategies-v1.1.jsonl

# Filter by use case
jq 'select(.best_for[] | contains("product research")) | .name' seed-prompting-strategies-v1.1.jsonl

# Find council strategies
jq 'select(.tags[] | contains("council")) | .name' seed-prompting-strategies-v1.1.jsonl
```

Python (via `StrategyRegistry` in `orchestrator-v3.3.py`):

```python
from orchestrator import StrategyRegistry

strats = StrategyRegistry.load("seed-prompting-strategies-v1.1.jsonl")

strats.top_by_effectiveness(5)          # top 5 by score
strats.filter_by_use_case("product research")
strats.filter_by_cost("medium")         # low + medium
strats.filter_by_tag("council")         # council strategies only
```

### For Orchestrator

Standard factory input:

```json
{
  "strategies_allowed": ["Few-Shot", "Meta-Prompting", "Self-Critique"],
  "strategy_registry_url": "seed-prompting-strategies-v1.1.jsonl"
}
```

Meta-factory with multi-model council:

```json
{
  "strategies_allowed": ["Model-Council-Generate", "Model-Council-Judge", "Decomposition"],
  "multi_model_available": true,
  "preferred_judge_models": ["claude", "qwen", "perplexity"]
}
```

### For Researchers

Append a new strategy:

```bash
echo '{"name":"New-Strategy","version":"1.0","enabled":true,...}' >> seed-prompting-strategies-v1.1.jsonl
```

Validate after appending:

```bash
python3 -c "
import json
with open('seed-prompting-strategies-v1.1.jsonl') as f:
    for i, line in enumerate(f, 1):
        if line.strip(): json.loads(line)
print('All lines valid')
"
```

---

## Adding New Strategies

1. **Test**: Validate effectiveness across 3+ domains
2. **Document**: Fill all schema fields — especially `implementation` and `best_for`
3. **Append**: Add JSON line to the `.jsonl` file
4. **Update this doc**: Add row to strategy table above, bump Version History
5. **Broadcast**: `factory-builder-v1` will auto-discover on next Phase 0 load

**Template:**

```json
{
  "name": "Strategy-Name-Here",
  "version": "1.0",
  "enabled": true,
  "description": "What this does, when to use, why it works",
  "implementation": "Step-by-step execution instructions",
  "effectiveness": 0.0,
  "best_for": ["use case 1", "use case 2"],
  "requires_multiple_runs": false,
  "computational_cost": "low|medium|high",
  "model_compatibility": ["perplexity", "qwen", "claude"],
  "added": "YYYY-MM-DD",
  "updated": "YYYY-MM-DD",
  "research_ref": "Paper/blog/source",
  "tags": ["tag1", "tag2"]
}
```

---

## Strategy Retirement

Disable (do not delete) underperforming strategies:

```json
{"name": "Strategy-Name", "enabled": false, ...}
```

`StrategyRegistry.enabled` filters these out automatically. History is preserved for research.

---

## Continuous Integration

- **Versioned** in git — commit message format: `strategies: add <Name> vX.X`
- **Shared** across all Seed instances via consistent file path
- **Updated** monthly minimum for new research
- **Monitored** via `execution-log.jsonl` — track which strategies are used and their scores

---

## Version History

| Version | Date | Changes |
|---|---|---|
| v1.0 | 2025-12-05 | Initial starter set — 10 core strategies |
| v1.1 | 2026-03-28 | Added Model-Council-Generate, Model-Council-Judge, Mixture-of-Roles; split companion .md from .jsonl |

---

**This is a living registry. Factories adapt automatically as strategies evolve.** 🚀

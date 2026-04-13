# seed-prompting-strategies — Living Registry of Prompting Strategies

**Version**: v3.3\
**Updated**: 2026-03-28\
**Data file**: `seed-prompting-strategies-v3.3.jsonl`

This is a living, continuously-updated registry of prompting strategies available to Seed factories.

Each line in the `.jsonl` file is a JSON object representing one strategy.
Factories reference this registry dynamically in Phase 0.

> JSONL does not support comments.\
> Keep documentation in this `.md` file and keep the `.jsonl` file pure JSONL.

______________________________________________________________________

## Schema

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

______________________________________________________________________

## Current strategy groups

### Core strategies

- Decomposition
- Chain-of-Thought
- Meta-Prompting
- Few-Shot
- Self-Consistency
- Self-Critique
- Perspective-Taking
- Community-Wisdom-Injection
- Constraint-Based-Reasoning
- Rubric-Based-Scoring

### Council strategies

- Model-Council-Generate
- Model-Council-Judge
- Mixture-of-Roles

______________________________________________________________________

## Usage

### For factory developers

Use the registry in Phase 0 to choose strategies dynamically.

Example shell usage:

```bash
jq 'select(.enabled == true) | .name' seed-prompting-strategies-v3.3.jsonl
jq 'select(.computational_cost == "low") | .name' seed-prompting-strategies-v3.3.jsonl
jq -s 'sort_by(-.effectiveness)[] | {name, effectiveness}' seed-prompting-strategies-v3.3.jsonl
```

### For orchestrator inputs

```json
{
  "strategies_allowed": ["Few-Shot", "Meta-Prompting", "Self-Critique"],
  "strategy_registry_url": "seed-prompting-strategies-v3.3.jsonl"
}
```

### For multi-model meta-factories

```json
{
  "strategies_allowed": ["Model-Council-Generate", "Model-Council-Judge", "Decomposition"],
  "multi_model_available": true,
  "preferred_judge_models": ["claude", "qwen", "perplexity"]
}
```

______________________________________________________________________

## Version history

- **v1.0 (2025-12-05)**: Initial 10-strategy starter set
- **v1.1 (2026-03-28)**: Added council strategies
- **v3.3 (2026-03-28)**: Aligned to Seed v3.3 naming and companion-doc pattern

______________________________________________________________________

## Maintenance rules

- Append new strategies, do not rewrite history casually
- Disable underperforming strategies with `"enabled": false`
- Keep the JSONL machine-readable
- Keep human guidance in Markdown

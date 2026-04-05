# Setup guide

Complete configuration and registry reference for the Seed Factory System (v4.1+).

For an overview of global controls and behavior, see:

- [`docs/modes-and-settings.md`](./modes-and-settings.md)
- [`seed/README.md`](../seed/README.md)

***

## Directory layout

```text
~/Documents/seed-system/
├── seed-profile.md
├── seed-orchestrator-v3.2-hybrid.md
├── seed-optimizer.md
├── seed-prompting-strategies.jsonl
├── factory-template-v1.1.md
├── factories-registry.jsonl          ← master registry (keep updated)
│
├── docs/
│   └── setup.md                      ← this file
│
├── factories/
│   ├── sentry-support-tutor/
│   │   ├── README.md
│   │   └── sentry-support-tutor-v1.md
│   │
│   ├── technical-tutor-for-self-learning/
│   │   ├── README.md
│   │   └── technical-tutor-for-self-learning-v1.md
│   │
│   ├── wealth-advisor-and-builder/
│   │   ├── README.md
│   │   └── wealth-advisor-and-builder-v1.md
│   │
│   └── factory-builder-v1/
│       └── factory-builder-v1.md
│
└── logs/
    └── execution-log.jsonl           ← tail module appends here
```

***

## Adding a factory to the registry

Append a new entry to `factories-registry.jsonl` at the seed root. Each entry must be a single-line JSON object. The required fields are:

```json
{
  "name": "your-factory-name",
  "version": "1.0",
  "type": "factory",
  "description": "One sentence describing what this factory does.",
  "parent": "parent-factory-name",
  "enabled": true,
  "tasks": ["task1", "task2"],
  "keywords": ["keyword1", "keyword2"],
  "rubric": {
    "clarity": 0.2,
    "conciseness": 0.15,
    "completeness": 0.2,
    "goal_alignment": 0.2,
    "context_awareness": 0.15,
    "expected_output": 0.1
  },
  "strategies": ["Decomposition", "Chain-of-Thought"],
  "recent_scores": [],
  "avg_score": 0,
  "last_updated": "YYYY-MM-DD"
}
```

Append command:

```bash
echo '{...}' >> factories-registry.jsonl
```

Verify the entry was added:

```bash
jq 'select(.name == "your-factory-name")' factories-registry.jsonl
```

The `rubric` weights should sum to 1.0 and use the same dimensions defined in [`docs/scoring-model.md`](./scoring-model.md). You can adjust weights per factory (for example, emphasize completeness for research-heavy factories).

***

## Registry entries — current factories

### sentry-support-tutor

```json
{"name":"sentry-support-tutor","version":"1.0","type":"factory","description":"Co-pilot, failure review, and study guide factory for a Senior Support Engineer accelerating Sentry.io mastery.","parent":"technical-tutor-for-self-learning","enabled":true,"tasks":["co_pilot","failure_review","study_session","pattern_tracking","question_discipline"],"keywords":["sentry","support","tutor","copilot","study","triage","tickets","SDK","failure-review","breadcrumbs","DSN","tracing","issues","events","escalation"],"rubric":{"clarity":0.2,"conciseness":0.15,"completeness":0.2,"goal_alignment":0.2,"context_awareness":0.15,"expected_output":0.1},"strategies":["Decomposition","Chain-of-Thought","Meta-Prompting","Few-Shot","Self-Critique"],"recent_scores":[8.8],"avg_score":8.80,"last_updated":"2026-03-21"}
```

### technical-tutor-for-self-learning

```json
{"name":"technical-tutor-for-self-learning","version":"1.0","type":"meta-factory","description":"Meta-factory that generates and deploys domain-specific technical tutors for any software, hardware, or foundational technical topic. All generated tutors follow Co-Pilot + Failure Review + Study Session pattern.","parent":"strategy-builder","enabled":true,"tasks":["factory_generation","tutor_deployment","study_plan_design","learner_profiling"],"keywords":["tutor","self-learning","technical","study","co-pilot","failure-review","mastery","accelerator","mentor","learning"],"rubric":{"clarity":0.15,"conciseness":0.1,"completeness":0.2,"goal_alignment":0.2,"context_awareness":0.15,"expected_output":0.2},"strategies":["Decomposition","Chain-of-Thought","Meta-Prompting","Few-Shot","Self-Critique","Constraint-Based-Reasoning"],"generates":"{domain-slug}-tutor-v1.md","recent_scores":[8.7],"avg_score":8.70,"last_updated":"2026-03-21"}
```

### wealth-advisor-and-builder

```json
{"name":"wealth-advisor-and-builder","version":"1.0","type":"factory","description":"Wealth planning for mid-career catch-up with employment risk, Boglehead-style.","parent":"strategy-builder","enabled":true,"tasks":["wealth","catchup","swr","runway","boglehead"],"keywords":["wealth","finance","boglehead","swr","runway","late_start","retirement"],"rubric":{"clarity":0.2,"conciseness":0.15,"completeness":0.2,"goal_alignment":0.2,"context_awareness":0.15,"expected_output":0.1},"strategies":["Decomposition","Chain-of-Thought","Meta-Prompting","Few-Shot","Self-Critique"],"recent_scores":[8.7,8.9,8.6],"avg_score":8.73,"last_updated":"2025-12-08"}
```

***

## Testing orchestrator match

Use `orchestrator-match.sh` to verify a factory will be discovered for a given query:

```bash
./orchestrator-match.sh "your test query here" factories-registry.jsonl
# Expected output: factory-name XX%
```

Match confidence thresholds:

- **≥ 85%** — auto-loads factory
- **75–84%** — prompts user to confirm
- **< 75%** — no match; refine query keywords or expand registry keywords array

These thresholds are part of the orchestrator’s matching logic and are separate from the quality thresholds used inside individual factory runs.

***

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Match score < 75% | Add query keywords to the factory’s `keywords` array in the registry |
| Phase 0 fails | Verify `seed-prompting-strategies.jsonl` has `"enabled": true` entries |
| Tail module not writing | Check write permissions on `factories-registry.jsonl` and `logs/execution-log.jsonl` |
| Wrong factory loads | Make keyword arrays more specific; avoid generic terms shared across factories |
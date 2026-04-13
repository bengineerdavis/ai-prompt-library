# Seed metadata files

These files are the runtime metadata source for the Seed system.

## Primary files

- `factories-registry-v3.3.jsonl`
- `seed-prompting-strategies-v3.3.jsonl`

## Purpose

### factories-registry-v3.3.jsonl

Holds factory-level metadata:

- routing targets
- factory descriptions
- tasks
- keywords
- rubrics
- default strategies
- scores
- judge-model preferences

### seed-prompting-strategies-v3.3.jsonl

Holds strategy-level metadata:

- strategy descriptions
- implementation notes
- effectiveness
- cost
- compatibility
- tags
- update timestamps

## As A General Rule

- Machine-readable metadata lives in `.jsonl`
- Human-readable comments and guidance live in `.md`

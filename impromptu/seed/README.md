# seed

The seed subsystem is the generative core of the impromptu library. Where `factories/` contains finished prompt packages, `seed/` contains the machinery that generates, routes, and refines them.

## Architecture

The subsystem has five modules, each with a distinct role in the generation pipeline:

- **profile** — captures user and project context for use across the pipeline
- **orchestrator** — routes context to the appropriate module and sequences operations
- **factory-builder** — generates new factory scaffolds from seed inputs
- **specializer** — adapts a factory to a specific role, domain, or use case
- **optimizer** — refines seed prompts for quality, coherence, and coverage

Each role is a self-contained module with its own prompt and (optional) README.

Prior iterations and archived specs can be saved in `seed/versions/`.

```bash
seed/
├── orchestrator/ # Routes seeds to the right factory
├── factory-builder/ # Builds new factories from seed inputs
├── specializer/ # Adapts roles and personas to context
├── optimizer/ # Refines and scores seed prompt quality
├── profile/ # User/context data consumed by all modules
└── versions/ # Archived prior orchestrator configs
```

Seed data (JSONL registries and strategy docs) lives in `../registries/` rather than here, keeping machine-readable assets separate from operational logic.

## How the logic flows

[profile]
│
▼
[orchestrator] ──── matches ──── [registries: seed-prompting-strategies]
│
├── route: generate ──▶ [factory-builder]
│ │
│ uses ▼
│ [specializer] ← adapts role/persona
│ │
│ uses ▼
│ [optimizer] ← scores and refines output
│
└── route: select ──▶ [factories registry] ──▶ existing factory

1. **profile** — supplies persistent context: user goals, background, constraints, and preferences. All other modules can pull from it to personalize their behavior.

2. **orchestrator** — the entry point. Given a request, it matches against the seed prompting strategies registry (`../registries/seed-prompting-strategies-v1.1.jsonl`) to decide whether to route to an existing factory or trigger the factory-builder to create a new one. The shell script (`orchestrator-match.sh`) handles quick local matching; the Python implementation (`orchestrator.py`) handles richer logic.

3. **factory-builder** — builds new factory prompt packages from scratch using seed inputs. It follows the factory template convention and is informed by the specializer to correctly configure the role and persona.

4. **specializer** — narrows a generic role definition into a specific, context-sensitive one. Used by the factory-builder and can also be invoked standalone to adapt an existing factory's persona without rebuilding it.

5. **optimizer** — evaluates and improves seed prompts before they are committed to a factory. It scores against the seed prompting strategies and suggests rewrites that better match target use cases.

## Registries

The seed subsystem reads from but does not own the registries. See `../registries/` for:

- `factories-registry-v3.3.jsonl` — index of available factories
- `seed-prompting-strategies-v1.1.jsonl` — JSONL strategy data consumed by the orchestrator
- `seed-prompting-strategies-v3.3.md` — human-readable companion to the strategies JSONL

## Versions

`versions/` holds prior orchestrator configurations that are no longer the active implementation but may be useful as reference. The `v3.2-hybrid` orchestrator is there as a historical snapshot of the approach before the current Python implementation.

## Typical workflow

**Generating a new factory:**

1. Fill out or update `profile/profile.md` with current user context.
2. Run the orchestrator against your goal to get a strategy match.
3. If no factory exists, the factory-builder generates a new one using the specializer.
4. Run the optimizer over the factory's core prompt before committing.

**Adapting an existing factory:**

1. Run the specializer with updated context against the target factory.
2. Optionally pass the output through the optimizer.
3. Commit the revised prompt file to the appropriate factory package.

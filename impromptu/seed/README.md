# Seed

Seed is a modular, self-improving meta-prompting system for users of LLMs, agents, and AI services who want better prompts, better workflows, and better decisions across tools (Perplexity, Gemini, local LLMs, etc.).

Seed is neutral by default and becomes personalized through feedback, preferences, and logged history.

***

## Mental model

- **Seed Profile + Orchestrator + Optimizer** = operating system
- **Factories** = apps following a standard interface
- **Strategy registry** = system-wide library of reasoning tools any factory can call

You boot the OS once per session, pick or auto-create the right factory, and the system handles routing, evaluation, and continuous improvement.

Impromptu’s global controls (cost, complexity, verbosity), scoring, thresholds, and preferences frame how this OS behaves.

***

## Components

### `seed-profile.md`

Global behavior defaults for the entire system. All factories and the orchestrator inherit from this unless explicitly overridden.

- **Tone**: probability language (“~75% confidence”), epistemic honesty, scannability
- **Evaluation criteria**: Clarity, Conciseness, Completeness, Goal Alignment, Context Awareness, Expected Output
- **Strategy catalog**: Decomposition, CoT, Self-Critique, Meta-Prompting, Few-Shot, Self-Consistency
- **Global switches**: `interaction_mode` (interactive / non_interactive), `feedback_mode` (on / off / auto)

### `seed-orchestrator-v3.2-hybrid.md`

Session entrypoint. Reads `factories-registry.jsonl`, matches your query to the best factory using multi-signal scoring, and routes you to what to run or paste next.

- **Modes**: Manual (Perplexity chat), Scripted (CLI/Python), Hybrid (pasted registry + manual)
- **Matching signals**: keyword, semantic, task coverage, recency
- **Match thresholds**: ≥ 90% auto-run, 85–89% confirm, 75–84% show top 3, < 75% suggest new factory
- **Companions**: `orchestrator.py` (Python), `orchestrator-match.sh` (Bash)
- **Change-aware workflow**: when a session creates or modifies prompt or factory artifacts, the orchestrator may also route follow-through for the relevant `CHANGELOG.md`

See [`orchestrator/README.md`](orchestrator/README.md) for inputs, outputs, and which file to run.

### `seed-optimizer.md`

End-of-session evaluator. Runs after a factory completes to score the output, propose prompt patches, and surface preference updates.

- **Tail module**: final answer check, feedback solicitation, self-scoring against evaluation criteria
- **Multi-strategy trial**: if uncertainty is high, samples 2–3 strategy variants and recommends the best
- **vNext patches**: proposes small improvements to the factory or profile based on this session’s outcome
- **Preference evolution**: suggests updates to user preferences as patterns emerge across sessions

### `factory-template-v1.1.md`

Canonical structure that every factory must follow. Factories that deviate from this template are not guaranteed to be discoverable or executable by the orchestrator.

Required sections: TITLE, Role & Purpose, Input Schema, Output Schema, Phase 0, Phase 1, Phase 2, Tail Module, Metadata JSON.

### `factory-builder-v1.md`

Meta-factory that generates new factory `.md` files. Use it when no existing factory matches a query above 75% confidence, or when an existing factory is too broad and needs to be split.

- **Input**: factory name, domain, example queries, parent factories, strategy hints, rubric hints
- **Output**: a complete factory `.md` file compliant with `factory-template-v1.1`, ready to register
- **Triggered by**: orchestrator when match confidence < 0.75, or explicit “Create factory for X”

### `role-specializer.md`

Optional component. Given a task and context, proposes a base role (2–4 sentences) and up to two complementary roles, with rationale and prompt patches.

- **Input**: task, context (user type, environment, failure modes), current role if any
- **Output**: refined base role, optional complementary roles, recommended patches
- **Use when**: a factory’s default role feels too generic for your specific job context

### `seed-prompting-strategies.jsonl`

Living registry of prompting strategies available to all factories. Each line is one strategy with name, description, `best_for`, computational cost, and compatibility.

Factories read this in Phase 0 and select 1–3 strategies to apply. New strategies are added by appending a JSON line — factories auto-discover them on the next session.

Ships with: Decomposition, Chain-of-Thought, Meta-Prompting, Few-Shot, Self-Consistency, Self-Critique, Community-Wisdom, Constraint-Based Reasoning, Rubric-Based Scoring.

### `factories-registry.jsonl`

Master index of all registered factories. Read by the orchestrator at session start. Each line is one factory entry with name, type, tasks, keywords, strategies, rubric, and recent scores.

Append a new line to register a factory. See `docs/setup.md` for the full entry schema and append commands.

***

## Directory map

```text
seed/
├── README.md                          ← you are here
├── seed-profile.md
├── seed-orchestrator-v3.2-hybrid.md
├── seed-optimizer.md
├── role-specializer.md
├── seed-prompting-strategies.jsonl
├── factory-template-v1.1.md
├── factories-registry.jsonl
└── orchestrator/
    └── README.md                      ← orchestrator-specific usage
```

***

**Version**: 4.1 · **Orchestrator**: v3.2+
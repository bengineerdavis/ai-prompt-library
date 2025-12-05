Seed is a modular, self-improving meta-prompting system for users of LLMs, agents, and AI services who want better prompts, better workflows, and better decisions across tools (local LLMs, Perplexity, Gemini, etc.).

***

## What Seed Is

Seed is not a single prompt. It is a set of prompts and JSONL conventions that work together:

- **Seed Profile** – defines global defaults (tone, epistemic norms, strategies, evaluation criteria).
- **Seed Orchestrator** – the “front door” for any task; routes your query to the right factory pattern and/or creates new ones over time.
- **Seed Optimizer** – runs at the end of sessions to evaluate outputs, propose improvements, and update preferences.
- **Factory Patterns** – reusable, task-specific meta-prompts (e.g., Strategy Builder, Interview Prep, Product Research Shopper). Factories do the actual work.
- **Role Specializer** – refines personas/roles when you need a tailored assistant.
- **Strategy Registry** – a living JSONL file of prompting strategies available to all factories (CoT, Few-Shot, Meta-Prompting, etc.).

Seed is neutral by default and becomes personalized through feedback, preferences, and logged history.

***

## Core Files and What They Do

### Global Prompts (Bootstrapping Set)

- **`seed-profile.md`** – global behavior and norms  
  - Tone: probability language (“75% confidence”), epistemic honesty, scannable outputs.  
  - Evaluation criteria: Clarity, Conciseness, Completeness, Goal Alignment, Context Awareness, Expected Output.  
  - Strategy catalog: decomposition, CoT, self-critique, meta-prompting, few-shot, self-consistency (and more via strategy registry).

- **`seed-orchestrator.md`** – session entrypoint (human-facing)  
  - Step 0: Capture your goal, suggest best factory patterns, set interaction + feedback modes.  
  - Step 1: Run chosen factory pattern with appropriate strategies.  
  - Step 2: Tail module – final answer check, ask if goal met, collect feedback.  
  - Step 3: Decide next action – iterate, optimize, or end.

- **`seed-optimizer.md`** – optimizer (LLM-as-judge)  
  - Evaluates outputs against the six criteria.  
  - Optionally tries multi-strategy combos for robustness.  
  - Proposes small “vNext” patches to prompts and preferences.

- **`role-specializer.md`** – optional role shaping  
  - Given a task, proposes base role and complementary roles.  
  - Suggests prompt patches to better fit context.

### Factory/Meta Files (Extended System v4.1)

- **`factory-template-v1.1.md`** – canonical structure for all factories  
  - Defines required sections: TITLE, Role & Purpose, Input Schema, Output Schema, Phase 0–2, Tail Module, Metadata.  
  - Phases are flexible containers: factories choose any combination of strategies based on context and the strategy registry.  
  - Phase 0 explicitly loads strategies from `seed-prompting-strategies.jsonl` and selects 1–3 to use.

- **`factory-builder-v1.md`** – “factory for factories”  
  - Input: factory name, domain, example queries, parent factories, strategy hints, rubric hints.  
  - Output: a complete factory `.md` file that follows the template and is immediately usable by the orchestrator.  
  - Used when:  
    - No existing factory matches a query well enough, or  
    - An existing factory is too broad and needs to be split/refactored.

- **`seed-prompting-strategies.jsonl`** – living strategy registry  
  - Each line: one strategy with name, description, implementation notes, effectiveness, best_for, compatibility, etc.  
  - Seed ships with strategies like Decomposition, Chain-of-Thought, Meta-Prompting, Few-Shot, Self-Consistency, Self-Critique, Community-Wisdom, Constraint-Based Reasoning, Rubric-Based Scoring.  
  - New strategies are added by appending JSON lines; factories then auto-discover them in Phase 0.

***

## How Everything Fits Together

### High-Level Flow

1. **You start a session with the Orchestrator**  
   - Paste `seed-orchestrator.md` into your LLM and state a goal (e.g., “design 30-week technical plan”, “prepare for backend interview”, “deep research mechanical keyboards under $150”).  
   - Orchestrator uses Seed Profile defaults (tone, strategies, criteria).

2. **Orchestrator suggests patterns (factories)**  
   - It identifies candidate factories: Strategy Builder, Interview Prep, Log-Triage, Prompt Tool Builder, Product Research Shopper, etc.  
   - It ranks them by confidence based on your goal and any prior history.  
   - You pick one, or it auto-selects when confident.

3. **Factory runs with dynamic strategies**  
   - The selected factory (e.g., shopping-builder for product research) follows the template:  
     - Phase 0: Capture context, profile you for this category, load available strategies from `seed-prompting-strategies.jsonl`, pick a strategy mix (e.g., Few-Shot + Meta-Prompting + Self-Critique).  
     - Phase 1: Execute those strategies to do the work (decompose, research, compare, reason).  
     - Phase 2: Produce a structured output (recommendations, comparisons, risks, reasoning).

4. **Tail Module, Optimizer, and Feedback**  
   - Factory’s Tail Module scores its own output, logs an execution record (including `strategies_used`, `score`, `goal`) to a JSONL file, and asks you for feedback.  
   - Seed Optimizer can run to propose prompt/strategy tweaks or factory splits (e.g., creating `gpu-upgrade-builder` from a general shopping factory).  
   - Your feedback and outcomes feed into future sessions: preferences, better defaults, improved strategies.

5. **Factory creation and evolution**  
   - If no existing factory matches your query well, Orchestrator can call `factory-builder-v1.md` with your domain and example queries.  
   - factory-builder produces a new factory file compliant with the template and registers it; future similar queries will match this factory directly.  
   - Over time, factories and strategies evolve instead of accumulating ad-hoc prompts.

***

## Recommended Usage Patterns

### For getting started

- Start with **`README.md` (original Seed README)** to understand the philosophy and the vanilla bootstrapping flow.  
- Then use this combined README (v4.1) to layer on factories, versioning, strategies, and persistence.

### Typical workflows

- **Designing a strategy or roadmap**  
  - Orchestrator → Strategy Builder factory → Seed Optimizer Tail Module.  

- **Interview preparation**  
  - Orchestrator → Interview Prep factory → Role Specializer (optional) to tune the persona.  

- **Product research & shopping decisions**  
  - Orchestrator → Product Research / Shopping factory (built with factory-template + strategy registry).  
  - Uses dynamic strategies like community-wisdom, constraint-based reasoning, and rubric-based scoring.

- **Evolving your system**  
  - When you see a pattern you repeat (e.g., GPU upgrades, NAS builds, BJJ gear research), let the Orchestrator create a dedicated factory via factory-builder.  
  - Add any new prompting strategies you discover into `seed-prompting-strategies.jsonl` so all factories can use them.

***

## Mental Model: Seed as an OS, Factories as Apps

- **Seed Profile + Orchestrator + Optimizer** = Operating System.  
- **Factories** (Strategy Builder, Product Research Shopper, GPU Upgrade Builder, etc.) = Apps following a standard interface.  
- **Strategy Registry** = System-wide library of reasoning tools that any app can call.  

You boot the OS once per session, pick or auto-create the right app (factory), and the
system handles routing, evaluation, and continuous improvement.

# Seed – Meta-Prompting System for Prompt Design & Optimization

Seed is a modular, self-improving meta-prompting framework designed for senior ICs and technical practitioners who need to design, refine, and optimize prompts and systems for high-stakes tasks.

## What is Seed?

Seed is not a single prompt—it's a **layered system of prompts that work together**:

1. **Seed Profile** – Global defaults (tone, epistemic norms, evaluation criteria, strategies).
2. **Seed Orchestrator** – Front door that guides you through goal capture, pattern selection, and execution.
3. **Seed Optimizer** – Maintenance layer that improves prompts over time via feedback loops.
4. **Factory Patterns** – Reusable children for specific tasks (Strategy, Interview, Log-Triage, Prompt/Tool Builder).
5. **Role Specializer** – Optional meta-prompt for role/persona refinement.

## Why Seed?

- **Research-backed**: Combines decomposition, chain-of-thought, self-critique, and multi-strategy reasoning.
- **Transparent**: Always shows confidence, tradeoffs, and "where this might be wrong."
- **Self-improving**: Captures feedback and learns what works best for your context.
- **Flexible**: Strategies can be mixed, matched, or combined as needed—not rigid templates.
- **Neutral by default**: Ships as generic, suitable for any senior IC; personalizes as you use it.

## Quick Start

### 1. Bootstrap the System

```bash
python main.py bootstrap --model qwen25-14b-opt
```

This generates:

- Complete Seed system files in `prompts/personalized/`
- Config in `user-seed-config.json`

### 2. Use in a Chat (Manual)

Paste `seed-orchestrator.md` into Perplexity, ChatGPT, or your local LLM:

[paste seed-orchestrator.md](./seed-orchestrator.md)

Your goal: "Design interview prep for a senior backend engineer role"

Seed will:

- Research candidate patterns.
- Suggest top 3 approaches.
- Run the chosen pattern.
- Ask for feedback.
- Propose improvements.

### 3. Use via CLI (When Ready)

```bash
python main.py run --goal "Design interview prep" --interaction interactive --feedback on
```

## Core Concepts

### Seed Profile

Defines how the system thinks by default:

- **Tone**: Probability language, epistemic honesty, scannability.
- **Criteria**: Clarity, Conciseness, Completeness, Goal Alignment, Context Awareness, Expected Output.
- **Strategies**: Decomposition, CoT, Self-Critique, Meta-Prompting, Few-Shot, Self-Consistency (optional).
- **Research & Synthesis**: Gather 5–10 candidate approaches, rank top 3 by confidence.

### Seed Orchestrator

The entry point for any session:

- **Step 0**: Capture goal, suggest patterns, set modes.
- **Step 1**: Run chosen pattern with appropriate strategies.
- **Step 2**: Tail Module—final answer check, feedback, optimization.

### Seed Optimizer

Runs at the end of each session:

- **Evaluates** your output against the six criteria.
- **Optionally tries** 2–3 strategy combos for robustness.
- **Proposes** small improvements (child + Seed-level).
- **Tracks** preferences and learns what works.

### Factory Patterns

Ready-to-use children:

- **Strategy Builder**: Multi-week plans, alignment, career strategy.
- **Interview & Conversation Prep**: Job interviews, performance reviews, 1:1s.
- **Log-Triage & Incident Summary**: Incident response, log analysis, workflows.
- **Prompt/Tool Builder**: Design reusable standalone prompts/tools.

Each pattern includes phases, checkpoints, and calls the Tail Module at the end.

### Role Specializer

Optional meta-prompt for refining role/persona:

- Evaluates task fit.
- Suggests base role + complementary roles.
- Proposes patches for the prompt.

## How Seed Evolves

Seed starts **neutral** and becomes more personalized as you use it:

1. **Feedback loops**: Each session collects feedback.
2. **Preference tracking**: Observations become persistent preferences (in `user-preferences.jsonl`).
3. **Strategy adaptation**: Over time, Seed learns which strategy combos work best for your context.

## File Structure

```bash
seed-cli/
├── prompts/
│ ├── vanilla/
│ │ └── starter.md # Generates entire system
│ └── personalized/ # Your generated + customized prompts
│ ├── seed-profile.md
│ ├── seed-orchestrator.md
│ ├── seed-optimizer.md
│ ├── strategy-builder.md
│ ├── interview-prep-builder.md
│ ├── log-triage-builder.md
│ ├── prompt-tool-builder.md
│ └── role-specializer.md
├── docs/
│ └── vanilla/
│ ├── ARCHITECTURE.md # System design
│ └── README.md # This file
├── seed/
│ ├── init.py
│ ├── orchestrator.py # Orchestrator class
│ ├── llm_client.py # LLM wrapper (Ollama, API)
│ ├── state.py # Session state
│ ├── patterns.py # Pattern loader
│ └── usage.py # Usage logging
├── main.py # CLI entry point
├── requirements.txt # Dependencies
├── .gitignore # Git config (ignores personalized/)
└── user-seed-config.json # Generated config (git-ignored)
```

## Configuration

After bootstrapping, edit `user-seed-config.json` to customize:

- Default interaction mode (interactive vs non_interactive).
- Default feedback mode (on / off / auto).
- Model selection.
- Strategy preferences.
- Evaluation criteria weights.

## Example Workflow

**Session 1: Design a Strategy Document**

Goal: "Create a 30-week technical alignment plan for a data pipeline refactor"

Orchestrator suggests:

    Strategy Builder (~85% confidence)

    Prompt/Tool Builder (~60% confidence)

    Log-Triage Builder (~40% confidence)

You pick: Strategy Builder

Orchestrator runs Strategy Builder:

    Phase 0: Capture context, timeline, constraints

    Phase 1: Define diagnosis, guiding policy, actions

    Phase 2: Draft the strategy doc

Tail Module:

    Summarizes the plan

    Asks: "Does this meet your goal?"

    You say: "Yes, but add risk section"

    Orchestrator improves

    Asks for feedback: "What worked? What could be better?"

    You: "Good decomposition; strategy felt a bit generic"

    Optimizer proposes: "Use more specific examples + add stakeholder perspectives"

    You accept → changelog updated

**Session 5: Same Task, Better Results**

After 5 sessions of feedback, Seed now:

- Knows your preferred strategy combos.
- Suggests Strategy Builder faster (higher confidence).
- Automatically includes stakeholder perspectives in Phase 2.
- Adapts decomposition based on past feedback.

## Local Model Setup

### Using Ollama + Qwen2.5-14B

```bash
# Install Ollama from ollama.com

# Download model
ollama pull qwen2.5:14b-instruct-q4_K_M

# Run server
ollama serve

# Bootstrap Seed
python main.py bootstrap --model qwen2.5:14b-instruct-q4_K_M


### Using LM Studio or llama.cpp

Point to your local API endpoint in `user-seed-config.json`:

```json
{
"model": "qwen2.5-14b-instruct-q4_K_M",
"api_endpoint": "http://localhost:8000/v1"
}
```


## Philosophy

- **Neutral by default**: No personal preferences baked in; you customize as you go.
- **Transparent**: Always show reasoning, confidence, and limitations.
- **Research-informed**: Use proven prompting techniques (decomposition, CoT, self-critique, multi-strategy).
- **Self-improving**: Feedback loops drive continuous refinement.
- **Respectful of time**: Respect stated constraints; optimize for your context.

## Contributing

Have ideas for new Factory patterns, strategies, or improvements? Open an issue or PR.

Keep in mind:
- **Vanilla prompts** should remain generic and reusable.
- **Personalizations** stay in your `prompts/personalized/` directory.
- Changes to core prompts should benefit all users, not just one context.

## License

MIT (or your preferred license)

---

## Next Steps

1. **Read** `docs/vanilla/ARCHITECTURE.md` for system design details.
2. **Bootstrap** your Seed: `python main.py bootstrap --model <your-model>`.
3. **Try a session**: Paste `seed-orchestrator.md` into Perplexity or your local LLM.
4. **Iterate**: Use feedback to refine your Seed over time.


## Reference

* https://www.perplexity.ai/search/remind-me-of-the-different-typ-Uj.Js0XIQneIy61Mu1OW6g
* [Which smaller llms have been used successfully to recursive prompts and self-optimizing prompts?
](https://www.perplexity.ai/search/which-smaller-llms-have-been-u-Fr6h.6bcRE6.MVxUHzMt2A)
    * exploringn which self-host models could be affected and also how to improve auto prompt optimization (or with large models via API SaaS)


---

**Questions?** Open an issue or check the docs.

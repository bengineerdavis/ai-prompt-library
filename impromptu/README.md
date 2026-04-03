# Impromptu Prompt Generation System

Impromptu is prompt generation and prompt management software built on the Seed meta-prompting system. It provides a framework for creating, managing, and optimizing prompts across various LLMs and AI tools.

---

Seed is a modular, self-improving meta-prompting system for users of LLMs, agents,
and AI services who want better prompts, better workflows, and better decisions across
tools (Perplexity, Gemini, local LLMs, etc.).

Seed is neutral by default and becomes personalized through feedback, preferences,
and logged history.

## What Seed Is

Seed is not a single prompt. It is a set of prompts and JSONL conventions that work
together:

- **Seed Profile** — global defaults: tone, epistemic norms, strategies, evaluation criteria
- **Seed Orchestrator** — the front door for any task; routes queries to the right factory and creates new ones over time
- **Seed Optimizer** — runs at end of sessions to evaluate outputs, propose improvements, and update preferences
- **Factory Patterns** — reusable, task-specific meta-prompts that do the actual work (e.g., Strategy Builder, Technical Tutor, Wealth Advisor)
- **Role Specializer** — refines personas when you need a tailored assistant
- **Strategy Registry** — a living JSONL file of prompting strategies available to all factories (CoT, Few-Shot, Meta-Prompting, etc.)

---

## Mental Model

- **Seed Profile + Orchestrator + Optimizer** = Operating System
- **Factories** = Apps following a standard interface
- **Strategy Registry** = System-wide library of reasoning tools any factory can call

You boot the OS once per session, pick or auto-create the right factory, and the
system handles routing, evaluation, and continuous improvement.

---

## Directory Map

seed-system/
├── README.md ← you are here
├── QUICKSTART.md ← fastest path to a working session
│
├── docs/
│ └── setup.md ← full setup, registry reference, directory layout
│
├── seed/
│ ├── README.md ← seed subsystem overview + all components
│ ├── seed-profile.md
│ ├── seed-orchestrator-v3.2-hybrid.md
│ ├── seed-optimizer.md
│ ├── role-specializer.md
│ ├── seed-prompting-strategies.jsonl
│ ├── factory-template-v1.1.md
│ ├── factories-registry.jsonl
│ └── orchestrator/
│ └── README.md ← orchestrator-specific usage
│
└── factories/
├── sentry-support-tutor/
├── technical-tutor-for-self-learning/
└── wealth-advisor-and-builder/

text

---

## Where to Go Next

| Goal | Go here |
|------|---------|
| Start using Seed right now | `QUICKSTART.md` |
| Understand the seed subsystem and its components | `seed/README.md` |
| Set up registry, add a factory, configure layout | `docs/setup.md` |
| Use or build a specific factory | `factories/{name}/README.md` |

---

**Version**: 4.1 · **Orchestrator**: v3.2+

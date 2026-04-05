# Impromptu

Impromptu is a project for **abstracting prompt creation** and making it easier to create, manage, and improve high-quality prompts.

It acts as:
- a prompt generator
- a factory-prompt generator
- a prompt manager

for LLMs, agents, and AI services.

Impromptu sits in front of concrete implementations like Seed. Seed provides modular, self-improving meta-prompts and factories, while Impromptu provides the shared controls, policies, and documentation that make those prompts easier to create, tune, and reuse.

***

## Where to start

| Goal | Go here |
|------|---------|
| Use Seed right now | [`QUICKSTART.md`](QUICKSTART.md) |
| Understand how Seed works | [`seed/README.md`](seed/README.md) |
| Understand Impromptu controls and defaults | [`docs/modes-and-settings.md`](docs/modes-and-settings.md) |
| Learn how auto behavior works | [`docs/auto-mode-policy.md`](docs/auto-mode-policy.md) |
| Learn the first-run experience | [`docs/onboarding.md`](docs/onboarding.md) |
| See practical examples | [`docs/examples.md`](docs/examples.md) |
| Understand the internal pipeline | [`docs/pipeline-and-stages.md`](docs/pipeline-and-stages.md) |
| Understand scoring and thresholds | [`docs/scoring-model.md`](docs/scoring-model.md), [`docs/thresholds-and-recommendations.md`](docs/thresholds-and-recommendations.md) |
| Learn how preferences and memory work | [`docs/user-preferences-and-memory.md`](docs/user-preferences-and-memory.md) |
| See SaaS and service-specific context guidance | [`docs/service-specific-guidance.md`](docs/service-specific-guidance.md) |
| Understand deep-search behavior | [`docs/deep-search.md`](docs/deep-search.md) |
| Set up registry, add a factory, configure layout | [`docs/setup.md`](docs/setup.md) |
| Use or build a specific factory | [`factories/{name}/README.md`](factories/) |
| Browse the full documentation hub | [`docs/README.md`](docs/README.md) |

***

## What Impromptu does in practice

Impromptu helps users move from ad hoc prompting to more reusable and reliable prompt workflows.

In practice, it can help you:

- turn a rough one-off prompt into a cleaner reusable prompt
- turn a reusable prompt into a prompt factory or prompt-building workflow
- manage prompt defaults like **cost**, **complexity**, and **verbosity** across tasks
- reduce repeated setup work by remembering stable preferences and constraints
- improve prompts over time using evaluation, comparison, and conservative automatic escalation

## Core controls

Impromptu and Seed share three main control classes that shape how much work the system does and how much process the user sees:

- `cost = auto | low | medium | high | unlimited`
- `complexity = auto | simple | layered | exploratory | deep search`
- `verbosity = quiet | info | debug`

These controls are explained in [`docs/modes-and-settings.md`](docs/modes-and-settings.md).

Recommended default starting point:

- `cost = auto`
- `complexity = auto`
- `verbosity = info`

***

## Documentation map

Use these docs for the most common questions:

- New to Impromptu: [`docs/onboarding.md`](docs/onboarding.md)
- Main vocabulary and knobs: [`docs/modes-and-settings.md`](docs/modes-and-settings.md)
- Auto behavior for cost and complexity: [`docs/auto-mode-policy.md`](docs/auto-mode-policy.md)
- Internal pipeline and stages: [`docs/pipeline-and-stages.md`](docs/pipeline-and-stages.md)
- Scoring signals and rubric: [`docs/scoring-model.md`](docs/scoring-model.md)
- Stop / continue / escalate behavior: [`docs/thresholds-and-recommendations.md`](docs/thresholds-and-recommendations.md)
- Examples of settings combinations: [`docs/examples.md`](docs/examples.md)
- Deep search behavior: [`docs/deep-search.md`](docs/deep-search.md)
- Preferences and memory: [`docs/user-preferences-and-memory.md`](docs/user-preferences-and-memory.md)
- Service-specific context: [`docs/service-specific-guidance.md`](docs/service-specific-guidance.md)
- Setup and registry: [`docs/setup.md`](docs/setup.md)

***

## Seed system

Seed is a modular, self-improving meta-prompting library for users of LLMs, agents, and AI services. It gives you better prompts, better workflows, and better decisions across tools — Perplexity, Gemini, local LLMs, and more.

Seed lives inside the Impromptu project and provides concrete factories and meta-prompts that can be managed and improved using Impromptu’s controls, scoring, and thresholds.

See [`seed/README.md`](seed/README.md) for details on Seed’s components.

***

**Version**: 4.1 · **Orchestrator**: v3.2+
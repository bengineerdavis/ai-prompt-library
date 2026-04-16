# docs/

Documentation for Users and Developers interacting with Impromptu, including [user-facing behavior](#controls--user-facing-behavior), [architecture](#architecture--structural-models), [internals](#internals--scoring-and-decision-logic), and [reference material](#reference--setup-onboarding-and-service-guidance).

______________________________________________________________________

## controls/ — User-facing behavior

How the three main knobs (`cost`, `complexity`, `verbosity`) work, how `auto` escalates,
and worked examples.

→ [controls/README.md](./controls/README.md)

| File                                                               | Contents               |
| ------------------------------------------------------------------ | ---------------------- |
| [controls/modes-and-settings.md](./controls/modes-and-settings.md) | Control reference      |
| [controls/auto-mode-policy.md](./controls/auto-mode-policy.md)     | Auto escalation policy |
| [controls/deep-search.md](./controls/deep-search.md)               | Deep search mode       |
| [controls/examples.md](./controls/examples.md)                     | Worked examples        |

______________________________________________________________________

## architecture/ — Structural models

Library, project, workspace, and pipeline design.

→ [architecture/README.md](./architecture/README.md)

| File                                                             | Contents                                       |
| ---------------------------------------------------------------- | ---------------------------------------------- |
| [architecture/library-model.md](./architecture/library-model.md) | Library and collection contract                |
| [architecture/project-model.md](./architecture/project-model.md) | Project, workspace, environment, config layout |
| [architecture/pipeline.md](./architecture/pipeline.md)           | Build → Specializer → Optimizer → Profile      |

______________________________________________________________________

## internals/ — Scoring and decision logic

Rubric, grading scale, decision profiles, and escalation logic.

→ [internals/README.md](./internals/README.md)

| File                                                                         | Contents                             |
| ---------------------------------------------------------------------------- | ------------------------------------ |
| [internals/scoring-and-thresholds.md](./internals/scoring-and-thresholds.md) | Full scoring and threshold reference |

______________________________________________________________________

## reference/ — Setup, onboarding, and service guidance

Getting started, preferences, and environment-specific behavior.

→ [reference/README.md](./reference/README.md)

| File                                                                                 | Contents                                     |
| ------------------------------------------------------------------------------------ | -------------------------------------------- |
| [reference/setup.md](./reference/setup.md)                                           | Installation and registry reference          |
| [reference/onboarding-and-preferences.md](./reference/onboarding-and-preferences.md) | First-run, preferences, and service guidance |

______________________________________________________________________

## Root-level docs

| File                                                                                                     | Contents                                            |
| -------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| [DECISIONS.md](./DECISIONS.md)                                                                           | Architecture decisions and schema migration handoff |
| [TODO.md](./TODO.md)                                                                                     | Open task list                                      |
| [TODO-refactor-shared-schemas-and-doc-alignment.md](./TODO-refactor-shared-schemas-and-doc-alignment.md) | WIP branch tracker                                  |
| [ROADMAP.md](./ROADMAP.md)                                                                               | Near, medium, and long-term roadmap                 |
| [commit-message-standard.md](./commit-message-standard.md)                                               | Commit message format                               |
| [examples/](./examples/)                                                                                 | `prompt-library.example.json` and `.toml`           |

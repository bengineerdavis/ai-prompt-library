# Impromptu

Impromptu is a project for creating, managing, improving, and reusing prompts across
local tools, scripts, projects, and AI services.

It sits in front of concrete prompt systems like Seed and provides the shared controls,
policies, and storage model needed to make prompt work more reusable and less ad hoc.

## What Impromptu does

Impromptu helps users move from one-off prompting toward durable prompt workflows.

In practice, it helps you:

- turn rough prompts into reusable prompts,
- organize prompts into reusable libraries,
- bind libraries to local or repo-backed projects,
- track prompt improvement over time,
- and keep runtime feedback separate from authored prompt files.

## Current architecture

The current documentation direction is:

- **Projects** are the main operating boundary.
- **Workspaces** live inside projects.
- **Environments** are defined per project.
- **Libraries** are separate prompt storage units that may be used across multiple
  projects.
- **Global app config** tracks available libraries separately from project bindings.
- **Runtime state** belongs in SQLite, while authored config belongs in TOML and prompt
  content stays file-based.

This architecture is intentionally local-first.
A built-in `local-default` project is intended to make non-git scripting and personal
prompt work first-class, while still allowing the same personal library to be reused in
repo-backed projects.

## Where to start

- Use Seed right now: `QUICKSTART.md`
- Understand how Seed works: `seed/README.md`
- Understand Impromptu controls and defaults: `docs/modes-and-settings.md`
- Learn how auto behavior works: `docs/auto-mode-policy.md`
- Learn the first-run experience: `docs/onboarding.md`
- See practical examples: `docs/examples.md`
- Understand the internal pipeline: `docs/pipeline-and-stages.md`
- Understand the project and workspace model: `docs/project-workspace-model.md`
- Understand the library model: `docs/impromptu-library-model.md`

## Core controls

Impromptu and Seed share three main control classes that shape how much work the system
does and how much process the user sees.

- `cost`: `auto | low | medium | high | unlimited`
- `complexity`: `auto | simple | layered | exploratory | deep-search`
- `verbosity`: `quiet | info | debug`

Recommended default starting point:

- `cost = auto`
- `complexity = auto`
- `verbosity = info`

## Design direction

The current design direction is:

- local-first use should work well before advanced team workflows,
- repo-backed personal libraries should be reusable across many projects,
- project bindings should remain separate from the global library registry,
- and mutable runtime state should not be spread across many hand-edited config files.

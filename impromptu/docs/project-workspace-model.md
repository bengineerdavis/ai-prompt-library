# Impromptu Project, Workspace, and Library Model

## Purpose

Define a simple v1 model for how Impromptu organizes projects, workspaces, environments,
libraries, and runtime state.

This model is optimized for:

- local personal use first,
- reuse across multiple projects,
- repo-backed prompt libraries,
- and a clean split between authored config and runtime state.

## Core model

Impromptu uses four main boundaries:

- **App config**

  - User- or machine-level configuration.
  - Defines available libraries and default local behavior.
  - Lives outside project repos.

- **Project**

  - The main operating boundary for prompt use.
  - Owns environments, workspaces, and library bindings.
  - Can be repo-backed or local-only.

- **Library**

  - The storage boundary for prompts.
  - A library can be used by many projects.
  - In v1, libraries are repo-backed.

- **Runtime state**

  - Sessions, feedback events, usage records, and indexes.
  - Stored in SQLite, not in hand-edited config files.

## Ownership

### App config owns

- available libraries installed or known on this machine
- user defaults
- location of the local default project

### Project owns

- project identity
- environments
- workspaces
- library bindings
- prompt resolution rules for that project

### Library owns

- library metadata
- prompt collections
- prompt directories
- prompt content files
- prompt support files

### Runtime state owns

- sessions
- feedback events
- prompt usage history
- caches and indexes

## Projects

A project is the required boundary for prompt work.

Every Impromptu action that reads or modifies prompts runs in a project.

Projects come in two forms:

- **Repo project**

  - Stored in a repository.
  - Shared with other users through committed config.
  - Usually branch-aware.

- **Local project**

  - Stored in the user config area.
  - Used for personal scripting, one-offs, and non-git directories.

Impromptu should create a built-in local project by default:

- project id: `local-default`

## Workspaces

Workspaces are defined inside a project.

A workspace is the operating context for:

- default environment
- selected libraries
- selected collections
- branch or worktree expectations
- feedback defaults
- sandbox or experimental behavior

A project must have at least one workspace.

## Environments

Environments are defined per project.

Every new project should start with at least:

- `dev`
- `staging`
- `production`

Projects may add more environments later, such as:

- `qa`
- `preview`
- `demo`
- `canary`

Environment definitions may include branch mapping, but the environment is not the same
thing as a branch.

## Libraries

Libraries are separate from projects.

The app should track which libraries are available on the machine.
Projects then bind one or more of those libraries for use.

This split is required because:

- one library may be used by many projects,
- one project may use many libraries,
- and not every available library should be active in every project.

## Config layout

### Global app config

```text
~/.config/impromptu/
  impromptu.toml
  libraries/
    personal/
      impromptu-library.toml
      prompts/
  projects/
    local-default/
      impromptu.toml
      state.db
```

### Repo project config

```text
repo/
  .impromptu/
    impromptu.toml
    state.db
```

## Config split

### `~/.config/impromptu/impromptu.toml`

Stores:

- available library registry
- user defaults
- location of the local default project

### project `impromptu.toml`

Stores:

- project identity
- environments
- workspaces
- bound libraries
- prompt resolution defaults

### `state.db`

Stores:

- sessions
- feedback events
- prompt usage records
- indexes and caches

## Prompt resolution

Prompt resolution should follow this order:

1. Resolve the current project.
1. Resolve the current workspace.
1. Resolve the libraries bound to that workspace or project.
1. Search only enabled collections.
1. Resolve the prompt alias.
1. Resolve the version active for the selected environment.
1. Fail clearly if the result is ambiguous.

## Version state

Prompt versions use three states:

- `draft`
- `active`
- `archived`

These states apply to the prompt version artifact itself.

Environment activation is resolved per project environment, not as a single global
toggle.

## Non-goals for v1

The following are out of scope for this model:

- database-only prompt storage
- making libraries global mutable state inside every project
- complex inheritance across many config layers
- advanced cross-library conflict resolution
- automatic promotion flows

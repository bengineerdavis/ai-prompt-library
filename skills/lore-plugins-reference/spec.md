# Lore Plugins Reference

## Intent

Grounds the agent in the canonical facts about the LoreAI plugin ecosystem —
the component map, the CLI surface, the config locations, and the current
OpenCode V2 incompatibility — so it never reconstructs them from memory or
misdescribes them. It is a shared dependency: it states facts and points to
the upstream source of truth, but orchestrates nothing and mutates nothing.
The `lore-plugins` (manage) and `lore-plugins-explain` skills cite it rather
than restating its content.

## Triggers

- **SHOULD** invoke when the agent needs a fact about any `@loreai/*` package,
  `lore` CLI subcommand, Lore config file, port, version, or the OpenCode
  plugin's V1/V2 status, so its answer is sourced rather than assumed.
- **SHOULD** invoke when another lore-plugins skill references a component,
  file, or command that the agent does not already hold verified.
- **SHOULD NOT** invoke to perform an action — install, update, diagnose, or
  explain. It only supplies facts.

## Behaviors

### Behavior: State facts with the upstream source

The agent SHALL report every component, file, port, and version fact with its
authoritative source — the BYK/loreai repository, the installed `lore` CLI, or
the on-disk file — and never from memory.

#### Scenario: Agent is asked what packages Lore ships

- **WHEN** the user asks which packages Lore publishes
- **THEN** the agent names `@loreai/opencode`, `@loreai/pi`, `@loreai/core`,
  `@loreai/gateway`, and the legacy alias `opencode-lore`, and cites the root
  `README.md` of the loreai repository as the source.

### Behavior: Identify the V1/V2 incompatibility precisely

The agent SHALL state that `@loreai/opencode` targets the OpenCode V1 plugin
API (`@opencode-ai/plugin`) and therefore does not run in OpenCode V2, with
the evidence that establishes it.

#### Scenario: Agent is asked whether the plugin works in V2

- **WHEN** the user asks whether `@loreai/opencode` runs in OpenCode V2
- **THEN** the agent says it does not, and cites `packages/opencode/src/index.ts`
  importing `@opencode-ai/plugin` and exporting the V1 plugin function
  (`LorePlugin`, the `config` hook) as the evidence.

### Behavior: Map the plugin entry module export shape

The agent SHALL state that the plugin entry module exports exactly one function
(`LorePlugin`) plus a same-reference default, and must not export helpers,
because the V1 loader invokes every function export.

#### Scenario: Agent is asked about the plugin's entry module

- **WHEN** the user asks why the OpenCode plugin entry only has one export
- **THEN** the agent names `index.ts` as exporting only `LorePlugin` and its
  default, and cites the WARNING comment plus `./internal.ts` as the reason
  helpers are kept out.

### Behavior: Report the component and config layout

The agent SHALL state the package layout, the shared SQLite database location,
and the per-app config files, sourced from the repository and the machine.

#### Scenario: Agent is asked where Lore stores its data and config

- **WHEN** the user asks where Lore keeps its database and configuration
- **THEN** the agent names `~/.local/share/lore/lore.db` (SQLite, with shm/wal),
  `.lore.json`, `.lore.md`, and the `lore start`/`lore run` gateway on port
  3207, and notes the facts come from the root README and the running install.

## Constraints

### Constraint: No action, no mutation

The agent MUST NOT install, remove, update, configure, or otherwise mutate any
Lore component when operating under this reference skill — it exists only to
supply facts.
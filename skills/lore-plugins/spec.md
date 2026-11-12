# Lore Plugins

## Intent

Makes the agent able to adjust and manage the LoreAI OpenCode plugin and its
immediate ecosystem on this machine, for real — not just repeat the README.
The load-bearing fact is that `@loreai/opencode` (as of 0.40.0) targets the
OpenCode V1 plugin API and will not run in OpenCode V2, so managing it means
installing/updating/diagnosing the plugin and, when asked, performing or
checking the V1-to-V2 port in the user's `bengineerdavis/loreai` fork. Facts
about components, paths, and the CLI come from `lore-plugins-reference`; this
skill owns the actions.

## Triggers

- **SHOULD** invoke when the user asks to install, remove, update, upgrade,
  set up, or diagnose the `@loreai/opencode` plugin or the `lore` gateway on
  this machine.
- **SHOULD** invoke when the user asks to port the loreai plugin to OpenCode
  V2, or to check the state of such a port in the fork.
- **SHOULD** invoke when a plugin load failure must be classified and fixed.
- **SHOULD NOT** invoke just to explain what a plugin or component does — that
  is `lore-plugins-explain`.
- **SHOULD NOT** invoke to recall history, query `.lore.md`, or list entities —
  those are `lore` CLI operations outside plugin management.

## Behaviors

### Behavior: Detect the V1 shape before acting

The agent SHALL confirm whether the plugin being managed targets the V1 or V2
plugin API before attempting any install or update, and state the result rather
than assuming the README's "OpenCode plugin" framing is V2.

#### Scenario: User asks to install the current plugin

- **WHEN** the user asks to install `@loreai/opencode`
- **THEN** the agent notes it is a V1-shape plugin (imports
  `@opencode-ai/plugin`, exports the V1 function) and therefore will not run
  in V2, before doing anything further.

### Behavior: Keep plugin OUT of .chezmoidata, wired via the loreai topic

The agent SHALL recognize that the lore plugin is wired into the deployed
OpenCode config through the loreai topic's
`dotfiles/apps/loreai/files/opencode/lore-plugin.jsonc` behind a stat-guard
include, and that plugin entries do not belong in `.chezmoidata/opencode.yaml`.

#### Scenario: User asks where the plugin is configured

- **WHEN** the user asks where the OpenCode plugin config lives
- **THEN** the agent names the lore-plugin.jsonc path in the loreai topic and
  states the plugin key is deliberately absent from `.chezmoidata/opencode.yaml`.

### Behavior: Classify load failures by fixer

The agent SHALL classify a plugin load failure as install-cause or loader-cause
and name the fix for that classification, rather than blurring the two.

#### Scenario: Plugin fails to load

- **WHEN** the user reports the plugin is not loading, or `opencode api get /api/plugin` returns an error or empty state
- **THEN** the agent greps the server log (`~/.local/share/opencode/log/opencode.log`)
  and classifies the cause as npm-install (`NpmInstallFailedError` /
  `LockTimeoutError`) or loader (`Plugin must export`), and states the remedy
  (`opencode plugin add @loreai/opencode` + `opencode service restart`, versus
  the upstream BYK/loreai release / V2 port), and treats a malformed or empty
  response as not-loaded, never as success.

### Behavior: Raise broken states, never whisper

The agent SHALL report broken plugin states as hard failures with the cause,
not as a debug note to be ignored.

#### Scenario: Plugin in a broken state

- **WHEN** the agent observes a broken plugin state
- **THEN** the agent raises it plainly with the classified cause, and does not
  bury it behind a "not critical" framing.

### Behavior: Perform or check the V1→V2 port in the fork

The agent SHALL, when asked to port or audit the port, work against the user's
`bengineerdavis/loreai` fork and translate the V1 shape (function export +
`config` hook mutating `cfg.compaction`/`cfg.agent`) into the V2 plugin API
(`Plugin.define`, `@opencode/plugin`, transforms/tools/hooks), preserving the
plugin's routing intent rather than dropping it.

#### Scenario: User asks to port the plugin to V2

- **WHEN** the user asks to port `@loreai/opencode` to OpenCode V2
- **THEN** the agent reads `packages/opencode/src/index.ts` and `internal.ts`
  in the fork, produces or checks a V2 port that registers the plugin via the
  V2 API and carries over the routing/context-injection behavior, and reports
  the change surface without committing.

## Constraints

### Constraint: Never ad-hoc install outside the topic

The agent MUST NOT bypass the loreai Ansible topic to install or upgrade the
lore plugin (e.g. running `npx -y @loreai/opencode@latest` or editing the
deployed config directly) — version and wiring follow the topic and the mise
pin.

### Constraint: No self-authored distribution

The agent MUST NOT run `git add`, `git commit`, `git push`, or `dotagents install` for skills it authored — those commands are the user's gate, printed
not executed.

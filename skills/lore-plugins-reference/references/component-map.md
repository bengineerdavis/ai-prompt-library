# LoreIA component map

Authoritative layout of the LoreAI plugin ecosystem. Facts sourced from the
BYK/loreai repository (`packages/opencode/`, root `README.md`, `CHANGELOG.md`)
and the installed `lore` CLI (v0.40.0), checked 2026-11-01.

## Packages

| Package | Role | Notes |
| --- | --- | --- |
| `@loreai/opencode` | OpenCode plugin | Targets the V1 plugin API (`@opencode-ai/plugin`); does not run in V2. Legacy alias `opencode-lore` ships identical code. |
| `@loreai/pi` | Pi coding-agent extension | Mirrors the OpenCode plugin's routing/context injection. |
| `@loreai/core` | Shared memory engine | Distillation, curation, recall, entities, embeddings. |
| `@loreai/gateway` | Standalone LLM proxy | Served by `lore start`/`lore run`; importable in-process by the plugin. |

## Storage

| Path | Purpose |
| --- | --- |
| `~/.local/share/lore/lore.db` | SQLite: conversations, distillations, memory, entities, embeddings (with `-shm`/`-wal`). |
| `.lore.md` | Curated, version-controlled knowledge export at the repo root. |
| `.lore.json` | Per-project config (embedding provider, search). |

## Gateway

| Setting | Value |
| --- | --- |
| Default port | `3207` (env `LORE_LISTEN_PORT`); fallback probe `5673`. |
| Host | `127.0.0.1` (env `LORE_LISTEN_HOST`). |
| Known ports probed | `3207`, `5673` (`KNOWN_GATEWAY_PORTS`). |
| Remote override | `LORE_REMOTE_URL`; access token `LORE_GATEWAY_AUTH_TOKEN`. |

## OpenCode plugin wiring (this machine)

| Concern | Detail |
| --- | --- |
| Config | Deployed `~/.config/opencode/opencode.jsonc` pulls the plugin via a stat-guard include of `dotfiles/apps/loreai/files/opencode/lore-plugin.jsonc`. |
| Not in data | Plugin entries stay OUT of `.chezmoidata/opencode.yaml` — two `plugin` keys would collide. |
| Gateways | Alias, `provider` blocks route through `http://127.0.0.1:3207/v1` (the gateway). |

## Provider env convention

`LORE_UPSTREAM_<PROVIDER>` maps a local/self-hosted provider to its server root
(no `/v1`): e.g. `LORE_UPSTREAM_OLLAMA=http://localhost:11434`. The plugin
forwards it as `x-lore-upstream-url`.

## V1/V2 incompatibility (load-bearing)

`packages/opencode/src/index.ts` imports `@opencode-ai/plugin` and exports the
V1 `LorePlugin` function with a `config` hook that mutates
`cfg.compaction = { auto: false, prune: false }` and `cfg.agent`. This is the
V1 plugin API; OpenCode V2's loader rejects it. The port to V2 is the
`lore-plugins` manage skill's job.
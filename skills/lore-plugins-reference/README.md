# lore-plugins-reference

Grounds an agent in the canonical facts about the LoreAI plugin ecosystem —
packages, CLI surface, config locations, gateway port, and the OpenCode V2
incompatibility — so answers come from source, not memory.

This is the shared fact base for the lore-plugins skill family. It states
facts and points at their source; it takes no action and orchestrates nothing.
`lore-plugins` (manage) and `lore-plugins-explain` cite it rather than
restating its content.

## Structure

- `SKILL.md` — the loaded instructions.
- `spec.md` — the behavior contract (Skillet source of truth).
- `references/component-map.md` — the full component/path/env-var table.

## Sources

Facts are sourced from the [BYK/loreai](https://github.com/BYK/loreai)
repository (`packages/opencode/`, root `README.md`, `CHANGELOG.md`) and the
installed `lore` CLI. Checked 2026-11-01 against `@loreai/opencode` 0.40.0.

## License

MIT. See `LICENSE`. Facts about LoreAI reproduce short, factual descriptions
from the upstream (FSL-1.1-Apache-2.0) repository; upstream retains its own
licensing.

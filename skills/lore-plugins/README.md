# lore-plugins

Manages the LoreAI OpenCode plugin and gateway on this machine — install,
update, upgrade, diagnose, and (when asked) the V1-to-V2 port of
`@loreai/opencode`.

The load-bearing fact: `@loreai/opencode` (as of 0.40.0) targets the OpenCode
V1 plugin API (`@opencode-ai/plugin`) and does not run in OpenCode V2, so
managing it means resolving the V2 port in the user's `bengineerdavis/loreai`
fork, not just re-installing.

## Structure

- `SKILL.md` — the loaded instructions.
- `spec.md` — the behavior contract (Skillet source of truth).

## Dependencies

Facts (packages, paths, port, component map) come from
[`lore-plugins-reference`](../lore-plugins-reference/SKILL.md); this skill owns
the actions and cites it rather than restating it.

## License

MIT. See `LICENSE`.
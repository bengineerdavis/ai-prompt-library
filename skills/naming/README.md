# Naming Skill

Names a project, tool, package, or repository and clears its package-registry
namespaces, asking the language/port/OS/distribution questions first and checking
availability mechanically.

## Files

- [SKILL.md](./SKILL.md) — the protocol the agent loads
- [spec.md](./spec.md) — Skillet behavior contract
- [references/namespaces.md](./references/namespaces.md) — registry rules + the PEP 541 bar
- [references/watchlist.md](./references/watchlist.md) — well-known projects/brands to avoid
- [references/lexicon.md](./references/lexicon.md) — word families already explored
- [scripts/check-name](./scripts/check-name) — the availability prober (run with `python3`)
- [evals/cases/](./evals/cases/) — Skillet eval cases

## Using check-name

```bash
python3 scripts/check-name redge-cli canopy got          # JSON verdict per token
python3 scripts/check-name foo --alias gc                # flag a reserved 2-letter alias
python3 scripts/check-name foo --config extra.json       # add registries/watchlist per session
python3 scripts/check-name foo --add-registry gitea http 'https://x/api/{name}'
```

Exit code is 0 when every token is `free`, 1 when any is not; the gate and reasons
are in the JSON. To cover a registry not in the built-in set, use `--config` or
`--add-registry` — never edit the skill itself.

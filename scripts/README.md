# Eval helpers

## `eval-claude`

Preflight Claude credentials, then run Skillet evals through the Claude harness.

```sh
scripts/eval-claude --check                 # only the credential preflight
scripts/eval-claude                         # preflight + eval skills/structure-authoring
scripts/eval-claude --skill skills/other    # a different skill
scripts/eval-claude --oauth --check         # force OAuth (ignore ~/.localrc key)
scripts/eval-claude -- --baseline --out .eval-results
```

### Why this exists

`skillet eval --harness claude` inherits `ANTHROPIC_API_KEY` from `~/.localrc`.
A stale literal key there **overrides OAuth login**, so the eval fails with
401/timeout even right after `claude auth login`. This wrapper makes the failure
loud and fast (~25 s) with the exact refresh command, instead of a 10-minute
hang.

### Credential resolution order

1. If `ANTHROPIC_API_KEY` starts with `op://`, it is resolved through 1Password
   CLI (`op read`) in memory. Enable app integration and run `op signin` first.
2. Otherwise `~/.localrc` is sourced and its `ANTHROPIC_API_KEY` is used.
3. `--oauth` skips the file entirely and forces the OAuth login path.

### Refresh paths

- Replace the literal key in `~/.localrc`, **or**
- Set `ANTHROPIC_API_KEY=op://Vault/Item/field` in `~/.localrc` and run
  `op signin`, **or**
- Remove/unset the key and run `claude auth login`, then verify with
  `env -u ANTHROPIC_API_KEY claude auth status`.

`~/.localrc` should be mode `600` (`chmod 600 ~/.localrc`).

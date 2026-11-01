# Multi-provider eval harnesses for skillet — upstream or fork?

**Verdict: upstream contribution, not a fork.** Skillet's harness model already
has the extension point this goal needs; the gap is a narrow packaging/CLI
surface, which is ordinary upstream territory. A fork is warranted only if the
author later wants bespoke behavior skillet's maintainers reject.

Status: researched 2026-11-01 against primary sources (the installed
`@sentry/skillet` 1.8.0 `dist/cli.js` and `package.json`, plus the repo the
published artifact derives from). Source of truth is the shipped code, not the
README, because the README does not state the harness model.

## What skillet actually does today (verified)

Skillet evaluates skill cases by shelling out to an **agent CLI**, not by
talking to a model provider directly. From `dist/cli.js`:

- Built-in harnesses are exactly two: `codex` and `claude`
  (`BUILTINS = { codex: CODEX, claude: CLAUDE }`).
- Each built-in is `{ name, kind, binary, effort }` — `binary` is a literal
  CLI name (`codex`, `claude`) that is resolved with `command -v`, so the
  harness must be **on PATH**.
- A built-in may carry a model suffix (`claude:sonnet`), parsed off the `:`
  in `parseBuiltin`.
- `effort` (low/medium/high/xhigh) **applies only to codex and claude**
  (`resolveHarness` throws `"effort applies only to codex and claude harnesses"` for anything else).

The `ai` dependency (`^6.0.233`) and `vitest-evals` (`0.15.0`) are present in
`package.json`, but the harness execution path in 1.8.0 is the CLI exec path,
not a direct `ai`-SDK provider call. Do not assume the `ai` SDK buys provider
selection in the eval path — the shipped exec path does not use it for that.

## The escape hatch that already exists

Skillet supports **custom harnesses** as a config-file mapping:

```text
harness:
  name: my-harness
  command: "<cli-or-script> --flag {prompt} --workspace {workspace}"
  skill_dir: "..."        # optional template
```

From `parseHarness` / `resolveHarness` in `dist/cli.js`:

- A custom harness is `{ name, kind: "custom", binary, command, skillDir }`.
- The `command` template **must** contain the `{workspace}` and `{prompt}`
  placeholders, or it is rejected.
- Custom harnesses reject `--effort` (effort is built-in-only).

This is the lever the requested feature builds on. Today it is **config-file
only**: the `--harness` CLI flag accepts only `codex` / `claude`
(`resolveHarness` parses `--harness` through `parseBuiltin`, never
`parseHarness`), and custom harnesses must be declared in `CONFIG_FILE`.

## What is missing (the actual gap)

The requested goal — "use agents other than codex or claude, fallback: codex
with models via OpenRouter" — decomposes into two gaps:

1. **`--harness <custom>` parity.** The flag only accepts built-ins; a custom
   harness is discoverable only via the config file. First-class support would
   let `--harness openrouter` (or a `codex:model-via-openrouter` built-in)
   work from the CLI without a config edit.
1. **A maintained OpenRouter-capable agent CLI to point it at.** Skillet
   shells out to a binary on PATH. There is no maintained `codex` flag or
   built-in OpenRouter provider in the `codex` CLI's documented surface to
   lean on today, so either (a) OpenRouter ships such a CLI (or codex gains a
   provider flag), or (b) a thin first-party wrapper CLI is published that
   accepts `{prompt}`/`{workspace}` and routes to OpenRouter. This wrapper is
   the only plausible "new artifact," and it is small.

## Why upstream, not a fork

- The harness model is already designed for extension (`kind: "custom"`,
  template placeholders); adding `--harness` parity and/or a new built-in is
  additive and low-risk.
- Nothing in skillet's current design is *counter-intuitive* to
  multi-provider support — the opposite: the custom-harness mapping openly
  anticipates exactly this. A fork would be justified only to ship the wrapper
  CLI faster than upstream agrees, or to bake in opinionated routing.
- The fallback the author stated (codex with OpenRouter models) is a
  codex-upstream question, not a skillet one; it lands or fails independently
  of skillet.

## Recommendation

Propose upstream (getsentry/skillet): (1) `--harness` accepts a custom-harness
name resolved from `CONFIG_FILE`, and (2) document an OpenRouter example using
the existing `{prompt}`/`{workspace}` template. Track the OpenRouter CLI
availability separately; if none exists, the spin-off is a ~100-line wrapper
CLI, not a fork of skillet itself.

## Sources

- `@sentry/skillet` 1.8.0, installed at
  `~/.local/share/mise/installs/npm-sentry-skillet/1.8.0/node_modules/@sentry/skillet/dist/cli.js`
  — `BUILTINS`, `CODEX`, `CLAUDE` (line ~1293–1305), `parseHarness` /
  `resolveHarness` (line ~1342–1402), `--harness` flag text (~2243).
- `@sentry/skillet` 1.8.0 `package.json` — `ai ^6.0.233`, `vitest-evals 0.15.0`, bin `skillet` → `dist/cli.js`.

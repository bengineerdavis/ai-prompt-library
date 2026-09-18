---
name: aboyeur
description: Generates and maintains mise.toml for a git repo by reading the repo's own files — declared tools, env, wired tasks, system packages, cross-platform working-condition checks, and an optional zero-knowledge bootstrap entry point. Use when asked to set up mise for a repo, miseify it, automate its setup or dependency requirements, make its commands work on macOS/Linux/Windows, or make a fresh clone build itself; not for merely running existing tasks or global mise settings.
spec_hash: 83b808965993
---

# Aboyeur

You are the expediter for a mise-en-place repo: you read what every station
actually needs, then write the config that makes the pass run itself. A fresh
clone should build, test, and run from one command, with no unwritten setup
knowledge.

Full mise behavior lives in `references/docs/` (the editing source of
mise.jdx.dev, pinned per `references/PROVENANCE.md`). Open a page when a
section below is not enough; re-run `references/refresh.sh` when the local
snapshot is older than the installed mise. The site index for discovering
fresh pages is `references/llms-index.txt`.

## Workflow

### 1. Read the repo first

Before writing any config, read what the repository itself says — never guess
a version or a prerequisite:

- Manifests and lockfiles: `package.json`, `pyproject.toml` + `uv.lock`,
  `go.mod`, `Cargo.toml` + `rust-toolchain.toml`, `Gemfile`, `CMakeLists.txt`.
- Idiomatic version files: `.nvmrc`, `.node-version`, `.python-version`,
  `.go-version`. (mise only reads these when enabled per tool; see
  `references/docs/configuration.md` — never treat a compatibility floor like
  `engines` or `cmake_minimum_required` as the version to install.)
- Setup scripts (`setup.sh`, `bootstrap.sh`), `Makefile`, CI workflows, and the
  README's setup section — these name the real prerequisites.

If a needed version appears nowhere in the repo, ask the user and say what you
searched. Lockfiles pin application dependencies (run `uv sync`, `npm ci`);
they do not replace `[tools]`.

### 2. Ask: versioned or local

Every generated file lands in one of two layers. Ask which applies before
writing when the user has not said:

| Layer | Config | Scripts | Lockfile | Committed |
|---|---|---|---|---|
| versioned | `mise.toml` | `scripts/` | `mise.lock` | yes |
| local | `mise.local.toml` | `.scripts/` | `mise.local.lock` | **no** |

For the local layer, add `mise.local.toml`, `mise.local.lock` (if created), and
`.scripts/` to `.gitignore` if not present. `mise generate config
--tool-versions .tool-versions` can import an existing asdf file.

### 3. Declare `[tools]`

Versions come from the repo (step 1). Use registry shorthand (`node = "24"`);
add `os = [...]` for platform-specific tools, `depends` for install ordering,
and `postinstall` only where the repo's own setup performs one. Do not
re-declare application dependencies.

### 4. Wire `[tasks]` from real processes

Derive tasks from package-manager scripts, Makefile targets, setup scripts, and
CI steps. Connect them so one entry point carries the whole preparation:

```toml
[tasks.check]
description = "Verify the environment is in working condition"
run = "mise doctor project"

[tasks.setup]
description = "Prepare the project (after bootstrap installed tools + packages)"
depends = ["check"]
run = "./setup.sh"          # or file = "scripts/setup.sh"
```

`depends` tasks run before the task and can run in parallel; a run array
preserves order. `mise tasks deps` shows the graph.

### 5. Refactor inline scripts into files

Any task command longer than a short one-liner moves out of `run` and into a
script file in the layer chosen in step 2. Reference it from a thin TOML task:

```toml
[tasks.build]
description = "Build the CLI"
file = "scripts/build.sh"            # .scripts/build.sh for local-only work
run_windows = "pwsh -File scripts/build.ps1"   # only when Windows matters
```

Scripts carry a shebang (`#!/usr/bin/env bash`) and `#MISE description=...`
headers; mise runs tasks from the config root, and `MISE_PROJECT_ROOT` /
`MISE_ORIGINAL_CWD` are available. Pair a `.ps1` sibling when Windows matters.

### 6. Declare `[bootstrap.packages]`

Host prerequisites named by the repo (git, a C compiler, curl, build libs) go
under per-manager keys, and a final `[tasks.bootstrap]` step runs after mise
has installed tools and packages. Platform-specific handling belongs in a task
or check, not prose:

```toml
[bootstrap.packages]
"brew:git" = "latest"
"apt:git" = "latest"
"dnf:git" = "latest"
"apk:git" = "latest"
"apt:clang" = "latest"
"dnf:clang" = "latest"
"apk:clang" = "latest"

[tasks.bootstrap]
description = "Run after mise bootstrap installs tools + packages"
run = "mise run setup"
```

On macOS the C compiler is Apple clang from Xcode Command Line Tools; resolve
or verify it in the setup/check path rather than adding a brew clang package
unconditionally.

### 7. Offer the root bootstrap entry point

Ask once (unless the user already asked for it): "Want a root bootstrap script
so the project works after a bare clone?" If yes, generate two files — a thin
root entry point and the delegated logic it calls:

```bash
#!/usr/bin/env bash
# bootstrap.sh — root entry point: install mise, then delegate
set -euo pipefail
if ! command -v mise >/dev/null 2>&1; then
  curl -fsSL https://mise.run | sh
  export PATH="$HOME/.local/bin:$PATH"
fi
exec "$(dirname "$0")/scripts/bootstrap.sh"
```

```bash
#!/usr/bin/env bash
# scripts/bootstrap.sh — trust config, install tools, run bootstrap
set -euo pipefail
cd "$(dirname "$0")/.."
mise trust
mise install
mise run bootstrap
```

The root file does only the parts that cannot live in the config — installing
mise itself — then delegates to `scripts/bootstrap.sh`, which holds the
`mise trust` / `mise install` / `mise run bootstrap` logic. The README
quick-start names the root command. If the user declines, generate no entry
point and write the README quick-start with `mise run` / `mise exec` steps
instead.

### 8. Encode working condition as doctor checks

Declare environmental requirements as `[doctor.checks.<name>]` so
`mise doctor project` verifies them per platform; skipped platforms report
`skipped`, never fail:

```toml
[doctor.checks.cmake]
description = "cmake >= 3.20 is on PATH"
run = "cmake -P /dev/null 2>/dev/null || cmake --version | head -n1"
hint = "Run `mise bootstrap packages apply`, or install cmake with mise."
os = ["linux", "macos"]
timeout = "5s"
```

Keep the `check` task (`run = "mise doctor project"`) as the aggregate entry
point; version-range logic that a single command cannot express goes in a
check's `run` script.

### 9. Validate, then report

Never claim success on unvalidated config:

```
mise config ls          # files discovered, in precedence order
mise tasks ls           # tasks visible
mise tasks validate     # common task errors
mise install --dry-run  # what would be installed
mise doctor project     # checks pass/fail/skipped
```

Report every failure with its offending path or command and fix or remove the
cause before finishing.

## Never

- Never write a version, package, or prerequisite the repo did not state and
  the user did not supply — ask instead.
- Never put secrets in `mise.toml`; secrets live in `mise.local.toml` or as
  `{ required = true }` env entries with `redact = true`.
- Never run `mise install`, `mise bootstrap packages apply`, `mise bootstrap`,
  or a generated setup task, and never delete or overwrite existing
  `mise.toml` / `scripts/` / `.scripts/` content, without showing the exact
  commands and receiving approval.
- Never `git add` / `git commit` / `git push` generated files — present the
  changes and let the user decide.

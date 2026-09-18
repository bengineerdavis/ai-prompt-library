# Aboyeur — Specification

## Intent

Define the observable behavior of the `aboyeur` skill. The skill inspects a git
repository's own files and processes, then generates and maintains a `mise.toml`
that makes the repository build, test, and run itself: declared dev tools,
environment, wired tasks, declared system packages, and cross-platform
working-condition checks — so a fresh clone needs no unwritten setup knowledge.

The name is the French kitchen term for the expediter: the cook who calls the
pass so every station's work arrives assembled and on time. Like mise itself
(mise en place), the metaphor is a kitchen that runs because the prep and
coordination were done first.

## Triggers

- **SHOULD** trigger when the user asks to set up mise for a repository, generate a `mise.toml`, add mise tasks, or "miseify" a repo.
- **SHOULD** trigger when the user asks to automate a repository's setup or dependency requirements (install steps, system packages, build prerequisites).
- **SHOULD** trigger when the user wants project commands to work across macOS, Linux, and Windows, or wants a check that the environment is in working condition.
- **SHOULD** trigger when the user asks for a bootstrap entry point so the project works after a bare clone ("so nobody has to read the README to build it").
- **SHOULD NOT** trigger when the repository already has a complete `mise.toml` and the user asks an unrelated question about it.
- **SHOULD NOT** trigger when the user only wants to run an existing task (`mise run test`) — that needs no generation.
- **SHOULD NOT** trigger for global `~/.config/mise` settings or machine-level dotfiles management unless the user connects it to a repository.
- **SHOULD NOT** trigger for migrating from asdf/nvm/direnv; point at `references/docs/dev-tools/index.md` and `comparison-to-asdf` instead of generating config.

## Behaviors

### Behavior: Recon before config

The agent SHALL read the repository's own files before writing any mise
configuration — manifests and lockfiles (`package.json`, `pyproject.toml`,
`uv.lock`, `go.mod`, `Cargo.toml`, `Gemfile`, `CMakeLists.txt`,
`rust-toolchain.toml`), idiomatic version files (`.nvmrc`, `.python-version`,
`.go-version`), setup scripts (`setup.sh`), `Makefile`, CI workflows, and the
README's setup section — and SHALL treat what those files say about versions and
prerequisites as the source of truth.

#### Scenario: CMake project with a setup script

- **GIVEN** a repo whose `CMakeLists.txt` says `cmake_minimum_required(VERSION 3.20)` and whose `setup.sh` needs cmake, a C compiler, git, and network access
- **WHEN** the user asks "set up mise for this repo"
- **THEN** the generated `[tools]` declares cmake at a 4.x-compatible request consistent with the requirement, and system packages are drawn from what `setup.sh` states rather than from the agent's guesses.

#### Scenario: Version is not discoverable

- **GIVEN** the repo contains no manifest, lockfile, or version file for a needed tool
- **WHEN** the agent cannot determine the version from the repository
- **THEN** it asks the user for the version instead of inventing one, stating what it searched.

### Behavior: Versioned versus local is an explicit choice

The agent SHALL determine — by asking, or from an explicit instruction such as
"this is just for me" — whether the generated configuration is meant to be
committed, and SHALL apply the official file roles accordingly: versioned work
goes in `mise.toml` plus a `scripts/` directory (with `mise.lock` committed
alongside when locking); local-only work goes in `mise.local.toml` plus a
`.scripts/` directory, which the agent SHALL add to `.gitignore` together with
`mise.local.toml` and `mise.local.lock` if a local lockfile is created.

#### Scenario: User says the config should be committed

- **GIVEN** the user asks for mise configuration "for the team" or does not restrict it
- **WHEN** the agent generates the config
- **THEN** files are written as `mise.toml` and `scripts/`, which are committable, and nothing gitignored is required for the config to work.

#### Scenario: User says the config is personal

- **GIVEN** the user asks for a local-only config or a personal override
- **WHEN** the agent generates the config
- **THEN** files are written as `mise.local.toml` and `.scripts/`, and `.gitignore` gains entries for `mise.local.toml`, `mise.local.lock` (if created), and `.scripts/`.

#### Scenario: The choice is never silent

- **GIVEN** the user has said nothing about whether the config should be committed
- **WHEN** the agent is about to write mise configuration
- **THEN** it asks which of the two applies before writing, naming the file roles it would use.

### Behavior: Tools are declared with the repo's versions

The agent SHALL populate `[tools]` from the repository's own version signals,
using registry shorthand where mise resolves it, `os` filters for
platform-specific tools, `depends` for install ordering, and `postinstall` only
where the repo's own setup performs one.

#### Scenario: Lockfiles pin package managers, not dev tools

- **GIVEN** a repo with `uv.lock` and `package-lock.json`
- **WHEN** the agent writes `[tools]`
- **THEN** it declares the interpreters and package managers (`python`, `node`) that the manifests imply, and does not re-declare application dependencies that belong to `uv sync` / `npm ci`.

### Behavior: Tasks are wired from real processes

The agent SHALL derive tasks from commands the repository actually uses —
package-manager scripts, `Makefile` targets, setup scripts, CI steps — and
SHALL connect them with `depends` and run arrays so that one entry point (for
example `mise run setup`) carries out the whole preparation, rather than
emitting unrelated one-line tasks.

#### Scenario: Setup depends on environment checks

- **GIVEN** a repo where building requires the environment check to pass first
- **WHEN** the agent generates tasks
- **THEN** the build task declares `depends = ["check"]` (or the check is a prerequisite in the run array), and `mise run setup` fails before building when the check fails.

### Behavior: Long inline scripts move to files

The agent SHALL move any task command longer than roughly ten lines — or with
branching, loops, or a here-document — out of `run` strings and into a script
file: `scripts/` when the file belongs in the repository, `.scripts/` when it
is local-only. TOML tasks reference them with
`file = "scripts/<name>.sh"`, provide a Windows sibling (`run_windows` or a
`.ps1` file) when Windows matters, and scripts carry a shebang.

#### Scenario: A task's run is a heredoc-sized script

- **GIVEN** a generated task whose `run` string spans multiple statements, branching, or a here-document
- **WHEN** the agent finalizes the config
- **THEN** the body lives in `scripts/<task>.sh` (or `.scripts/<task>.sh` for local-only work) referenced by `file =`, with `#MISE description=` metadata, and the TOML task remains thin.

### Behavior: System dependencies are declared, not implied

The agent SHALL declare host-level prerequisites discovered in the repository
(git, a C compiler, curl, build libraries) under `[bootstrap.packages]` using
per-manager keys such as `brew:git`, `apt:git`, `dnf:git`, `apk:git`,
`pacman:git`, and `winget:` entries — with a per-package `os` selector when an
entry applies to fewer platforms than its manager — and SHALL name a final
`[tasks.bootstrap]` step that runs after `mise bootstrap` installs tools and
packages. Platform-specific handling that no package manager can install (for
example, Apple clang supplied by Xcode Command Line Tools on macOS) SHALL be
encoded in a guarded `[bootstrap.hooks.<phase>]` entry or in the relevant task
or check, not left as prose.

#### Scenario: setup.sh states its requirements

- **GIVEN** a repo whose setup script says "Needs: cmake, a C compiler, git, network"
- **WHEN** the agent declares bootstrap packages
- **THEN** `[bootstrap.packages]` contains per-manager entries for git, curl, and a C compiler across the Linux package-manager families and Homebrew on macOS.

#### Scenario: The macOS C compiler has no package

- **GIVEN** a repo whose macOS builds need Apple clang, which no bootstrap package manager provides
- **WHEN** the agent declares bootstrap packages
- **THEN** a guarded `[bootstrap.hooks.pre-packages]` entry runs `xcode-select --install` only on Darwin when clang is missing — so repeated bootstraps are safe — while the Linux families get clang from their package managers.

### Behavior: Optional root bootstrap entry point

The agent SHALL offer — asking when the user has not asked for it — an optional
entry-point script at the project root whose entire job is: install mise if it
is missing (via the official `curl https://mise.run | sh` path), trust the
project config, run `mise install`, and invoke the project's bootstrap task, so
that a bare clone becomes a working project with one command and no setup
knowledge. The entry point SHALL be thin; its logic lives in `scripts/`
(versioned) or `.scripts/` (local-only), and the agent SHALL NOT generate it
when the user declines.

#### Scenario: User asks for zero-knowledge setup

- **GIVEN** the user says "add a bootstrap script so the project works after clone"
- **WHEN** the agent generates the entry point
- **THEN** the root script installs mise when `mise --version` fails, then runs `mise trust`, `mise install`, and `mise run bootstrap`, delegating its real logic to a file under `scripts/`, and the README's quick-start names that one command.

#### Scenario: User declines the entry point

- **GIVEN** the user does not ask for a root bootstrap and answers "no" when offered
- **WHEN** the agent finishes generating config
- **THEN** no root entry-point script exists, and the generated README quick-start instead names `mise run` / `mise exec` steps.

### Behavior: Working condition is verified cross-platform

The agent SHALL encode the repository's environmental requirements as
`[doctor.checks.<name>]` entries that `mise doctor project` evaluates, using
`os` selectors so each check targets macOS, Linux, and Windows appropriately
and skipped platforms are reported rather than failed, and SHALL provide a
`check` task that runs `mise doctor project`. Before reporting success the
agent SHALL validate the generated configuration with `mise config ls`,
`mise tasks ls`, `mise tasks validate`, and `mise install --dry-run`, and
SHALL report every failing validation instead of claiming the setup works.

#### Scenario: Check applies to two platforms only

- **GIVEN** a requirement that cannot hold on Windows (for example, a check that shells out to `pkg-config`)
- **WHEN** the agent writes the check
- **THEN** the entry declares `os = ["linux", "macos"]` so Windows reports `skipped`, and the hint names the remedy.

#### Scenario: Validation fails

- **GIVEN** a generated task references a script path that does not exist
- **WHEN** the agent runs `mise tasks validate` (or the equivalent)
- **THEN** it reports the failure with the offending path and fixes or removes the task rather than declaring the setup complete.

## Constraints

### Constraint: Never invent versions or facts

The agent MUST NOT write a tool version, package name, or prerequisite into
mise configuration that the repository's own files did not state and the user
did not supply; when evidence is missing the agent asks instead of guessing.

### Constraint: No secrets in versioned config

The agent MUST NOT place credentials, tokens, or connection strings into
`mise.toml`; secrets belong in `mise.local.toml` or as `{ required = true }`
env entries with `redact = true`, never in committed files.

### Constraint: No silent installs or mutations

The agent MUST NOT run `mise install`, `mise bootstrap packages apply`,
`mise bootstrap`, or execute generated setup tasks, and MUST NOT delete or
overwrite an existing `mise.toml`, `scripts/`, or `.scripts/` content, without
showing the user exactly what will run or change and receiving approval.

### Constraint: No commits without approval

The agent MUST NOT run `git add`, `git commit`, or `git push` on files it
generated; it presents the changes and the commands, and the user decides.

<!-- skillet-version: 1.8.0 -->

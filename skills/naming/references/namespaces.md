# Namespaces — registry facts and the PEP 541 bar

What a name must clear, and the rules each registry applies. Check these before
trusting intuition; the namespaces are flat in ways that change the answer.

## PyPI — flat, no scopes

- The package name is a **flat namespace**: whoever publishes `foo` owns `foo`
  for Python, and there is no `@scope/foo` escape hatch.
- `pip install <name>` / `uv tool install <name>` resolve against this exact
  token, so a taken PyPI name forces **either** a compound (`foo-cli`) **or** a
  different binary/package split.
- **PEP 541** transfers a name only when the project is effectively
  **abandoned** and the owner is **non-responsive** to a good-faith dispute.
  The practical bar: the package has had no meaningful releases for years, the
  owner does not answer, and there are no remaining users being served. A
  package that is merely *small but live* is **not** transferable.

## crates.io — flat, permanent

- Also a flat namespace; crate names are **kebab-case** and **never released
  back** once taken.
- Relevant whenever the project has a **Rust port planned**, because the port
  ships the same name into a second flat namespace from day one.

## npm — flat *plus* scoped

- Unscoped names are flat, but **scoped packages** (`@scope/name`) are the
  escape hatch PyPI lacks. Legal and common, though a scoped name is a weaker
  brand than an unscoped one.

## Homebrew — formula, cask, and binary are separate

- A **formula** or **cask** name and the **binary** it installs are independent
  namespaces. A Homebrew formula can be named `redge` even if PyPI's `redge` is
  taken — the PATH binary and the registry token are different things.

## The registry-name / binary-name split

The name a user types on the command line (the **binary**) and the name a
package is published under (the **registry token**) are two namespaces. They may
differ deliberately — this is the `redge` / `redge-cli` pattern: the PyPI token
is `redge-cli`, the binary is `redge`.

## `check-name` namespace extension

`scripts/check-name` ships with built-in probes for PyPI, crates.io, and npm,
plus a GitHub popularity scan and a brand watchlist. To cover a registry the
default set does not, extend it **per session**:

- `--add-registry <name> <kind> <url>` — add one probe, where `kind` is
  `pypi`, `crates`, `npm`, or `http` (a JSON 200/404 endpoint).
- `--config <file>` — load extra registries and watchlist entries from a JSON
  file, so a recurring channel is declared once instead of per run.

The mapping lives in arguments and config, never inside this skill, so covering
a new registry never means editing the skill itself.

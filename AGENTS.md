# AGENTS.md

Guidance for agents working in this repository. Content-first prompt library: almost
everything is Markdown; the only root executable is `bundle.py`.

## Layout

- `prompts/` — the library. Each entry is either a **flat** collection (single `.md`
  file, or a directory with a `SKILL.md`) or a **structured** collection with
  `events/`, `roles/`, `skills/`, `templates/`, `context/` (only `panel-of-judges`
  today). `bundle.py` detects flat collections by the absence of `events/` and `roles/`.
- `impromptu/` — a separate sub-project with its own `pyproject.toml`, ruff config,
  and docs. It is being extracted to its own repo; do not treat it as part of the
  prompt library or apply library conventions to it.
- `tests/`, `tools/`, `examples/` — empty placeholders. There is no test suite.
- `generated/` (root and per-collection) — bundler output, not authored source. Safe
  to overwrite; never hand-edit.

## Commands

- Run the bundler: `./bundle.py -p <collection>` — it is a `uv` script
  (`#!/usr/bin/env -S uv run --script`, deps inline); requires `uv` on PATH, no venv
  or install step. Useful flags: `--dry-run`, `--list`, `-c <config>`, `--debug`.
- Lint/format check before committing: `pre-commit run --all-files`
  (trailing-whitespace, codespell, mdformat-gfm). Codespell false positives go in
  `.codespellignore`, one word per line — do not misspell to satisfy it.

## Bundler gotchas (verified against `bundle.py`, which wins over docs)

- Bundle configs live at the **collection root** as `bundle.yaml` / `bundle.<variant>.yaml`.
  `prompts/panel-of-judges/STRUCTURE.md` shows them under `events/<event>/bundles/`,
  but `bundle.py` only globs the collection root — follow the code and `BUNDLER.md`.
- `event.name` in a config must exactly match an existing directory under
  `events/`; there is no alias resolution.
- Role files are searched in `roles/`, `roles/judges/`, `roles/specialists/` in that
  order. Skills must be directly in `skills/<name>.md`.
- Defaults inheritance: put `defaults: <path>` **inside** the `event:` mapping.
- Missing optional files warn and are skipped; a missing event dir is a hard error.

## Skill authoring conventions

New skills follow the Agent Skills format: a directory named after the skill
containing `SKILL.md` with YAML frontmatter (`name`, `description`, `license`,
`metadata` with `version` and `supersedes` — see `skills/interaction-questioning/SKILL.md`),
plus optional `references/` and `assets/` subdirectories. Bump `metadata.version`
and set `supersedes` when editing an existing skill.

Skills maintained with the Skillet flow (`prompts/skillet/SKILL.md`, e.g.
`skills/interaction-questioning/`) keep a `spec.md` behavior contract and `evals/cases/*.yaml`.
Rules that bite:

- Always run Skillet through `npx -y @sentry/skillet@latest` (never a bare
  `skillet` binary), and follow what `status <dir> --json` says is `next`.
- `SKILL.md` frontmatter carries `spec_hash:` from `status --json`; editing
  `spec.md` without re-rendering/re-hashing marks the skill stale.
- Eval cases must not contain `: ` inside unquoted `judge:` scalars — use
  `judge: |` block form.
- `skillet eval` needs a `codex` or `claude` CLI on PATH (`--harness`); without
  one, report evals as not run instead of claiming success.

## Specs to consult before restructuring

- `BUNDLER.md` — bundler behavior and config shape.
- `prompts/panel-of-judges/STRUCTURE.md` — structural model (event vs role vs skill
  vs bundle vs data) and session-data filename convention:
  `<event-type>-<session-id>-<bundle-key>-<artifact-kind>.md` under
  `events/<event>/data/<kind>s/`.
- `HISTORY-SPEC.md` — history-object layout (session records live outside the
  library in `history/<library-key>/...`; library holds reusable source only).

## Style

- Docs are formatted with mdformat (GFM + frontmatter); run the pre-commit hook
  rather than hand-aligning tables.
- Commit messages follow Scoped Commits (<https://scopedcommits.com/>):
  `<scope>: <description>` (e.g. `questioning: add two-sided understanding`).
  The scope is the collection/skill name; use `panel-of-judges` for event,
  role, and bundle changes inside that collection. Older history uses
  `type(scope): description`; new commits use the scoped format.
- Changelogs are Keep a Changelog format and layered: project-level
  `CHANGELOG.md` (human-readable summary), per-skill
  `prompts/<skill>/CHANGELOG.md`, and per-event
  `prompts/panel-of-judges/events/<event>/CHANGELOG.md`. Do not dump git logs
  into changelogs; write them for users of the prompts.
- Bundle configs live at the collection root; cross-collection skills are pulled
  into a bundle via `include.context` with collection-relative paths
  (see `bundle.advisory-meeting-service-procurement.yaml`), since `skills:` only
  resolves `skills/<name>.md` inside the collection.

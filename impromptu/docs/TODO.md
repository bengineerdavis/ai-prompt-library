# TODO

## Highest priority

- [ ] Finalize the app config vs project config split.
- [ ] Add support for a built-in `local-default` project for non-git work.
- [ ] Add a global library registry in user config, separate from project bindings.
- [ ] Define `impromptu.toml` for global app config.
- [ ] Define `impromptu.toml` for project config.
- [ ] Add SQLite runtime state for sessions and feedback.

## Project model

- [ ] Lock the v1 project model: project, workspace, environment, library, session.
- [ ] Require at least one workspace per project.
- [ ] Bootstrap `dev`, `staging`, and `production` for new projects.
- [ ] Define project-local library binding precedence.
- [ ] Define clear ambiguous-prompt failure behavior.

## Library model

- [ ] Rewrite the library manifest in TOML.
- [ ] Replace JSON examples with TOML examples.
- [ ] Decide and document the primary prompt filename rule.
- [ ] Keep collections as storage partitions.
- [ ] Keep families out of the filesystem model for now.
- [ ] Add support files and metadata guidance.

## Runtime state

- [ ] Define the first SQLite tables for sessions and feedback events.
- [ ] Separate authored config from runtime state cleanly.
- [ ] Avoid spreading mutable runtime state across many config files.

## Linting and docs quality

- [ ] Add a minimal pre-commit stack for code and docs.
- [ ] Add Ruff for Python formatting and linting.
- [ ] Add Markdown formatting with `mdformat`.
- [ ] Add Markdown linting with `markdownlint-cli2`.
- [ ] Add spelling checks with `codespell`.
- [ ] Add TOML, YAML, and JSON syntax validation hooks.
- [ ] Add TOML semantic validation later through application models and validation scripts.
- [ ] Add Vale to the roadmap as the primary future prose linter.
- [ ] Define a reusable docs style standard that can be shared across projects.
- [ ] Add `docs/LINTING.md` later to explain the chosen tooling and standards.

## Commit workflow

- [ ] Add a shared commit message template to the repo.
- [ ] Standardize on Conventional Commits plus selective Git trailers for all new commits.
- [ ] Add local validation for commit message format.
- [ ] Add optional local-model assistance for drafting commit messages from staged diffs.
- [ ] Keep model-suggested commit messages human-reviewed before commit.
- [ ] Leave historical commit cleanup for later.

### Commit automation

- Standardize all new commits on Conventional Commits.
- Add commit message validation based on Conventional Commits.
- Add optional structured Git trailers for architecture intent and review metadata.
- Build a local-model helper that proposes commit messages from staged changes.
- Add lightweight commit review assistance before finalizing commits.
- Use the commit standard as the foundation for future changelog and version automation.

## Versioning and changelog

- [ ] Adopt Semantic Versioning as the release versioning standard.
- [ ] Create a root `CHANGELOG.md`.
- [ ] Use a human-readable changelog structure aligned with Keep a Changelog.
- [ ] Define how commit types map to version bumps:
  - `feat` -> minor
  - `fix` -> patch
  - `perf` -> patch
  - `revert` -> patch
  - `BREAKING CHANGE` -> major
  - `docs`, `test`, `chore`, `build`, `ci`, `refactor` -> no automatic release bump by default
- [ ] Add release tagging conventions.
- [ ] Add automated version bump planning based on commit history.
- [ ] Add automated changelog draft generation from commits and tags.
- [ ] Decide whether release automation should update version strings in files, tags only, or both.
- [ ] Keep release generation human-reviewed before publishing.

## Packaging and layout

- [ ] Move Seed and internal runtime logic under `src/` after the current docs/model branch is merged.
- [ ] Clean up imports and package boundaries as part of the `src/` refactor.
- [ ] Separate CLI, runtime logic, prompt discovery, config loading, and state management more clearly.
- [ ] Prepare for packaging and cleaner test layout once the `src/` refactor lands.

## Docs cleanup

- [ ] Update architecture docs to use the project-first model.
- [ ] Update onboarding docs for local-first use.
- [ ] Remove outdated sandbox-first wording where it conflicts with the new model.
- [ ] Align root docs, architecture docs, and examples around TOML config and SQLite
  runtime state.

## Schema and docs alignment follow-up

- [ ] Audit the repo for references that still imply JSON-first library config.
- [ ] Update lingering references to point to TOML-first config and examples.
- [ ] Add a repeatable way to detect cross-doc terminology drift and outdated config references.
- [ ] Evaluate using local LLM assistance for doc alignment and consistency review during future refactors.

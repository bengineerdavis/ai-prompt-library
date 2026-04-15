# ROADMAP

## Near term

### Local-first usability

- Support a built-in `local-default` project.
- Make non-repo scripting and one-off prompt work a first-class workflow.
- Allow the local default project to bind repo-backed libraries.

### Project architecture

- Finalize project-scoped workspaces and environments.
- Bootstrap `dev`, `staging`, and `production` for each project.
- Define branch mapping as project configuration, not as environment identity.

### Library architecture

- Introduce a global library registry in app config.
- Allow projects to bind installed libraries independently.
- Keep libraries reusable across many projects.

### Runtime state

- Add SQLite-backed session and feedback storage.
- Keep prompt assets and config file-based.
- Add indexes and caches without moving authored prompts into the database.

### Linting and formatting

- Standardize on a shared pre-commit baseline for code and docs.
- Use Ruff for Python linting and formatting.
- Use `mdformat` plus Markdown linting for docs consistency.
- Use spelling checks to catch common errors in code and prose.
- Add semantic TOML validation after the config model stabilizes.

### Commit automation

- Add commit message validation based on Conventional Commits.[web:1503]
- Add optional structured Git trailers for architecture intent and review
  metadata.[web:1513]
- Build a local-model helper that proposes commit messages from staged changes.
- Add lightweight commit review assistance before finalizing commits.
- Reuse the same commit standard across projects.

## Medium term

### Docs quality and prose linting

- Add Vale as the primary prose linter with a shared style pack based on Google
  style.[web:1532]
- Define a reusable project documentation standard that can be applied across
  repositories.
- Add prompt-specific writing rules for consistency, clarity, and terminology.
- Add docs lint guidance and shared templates that can be copied into other projects.
- Evaluate complementary prose checks only after Vale is stable and tuned.

### Versioning and releases

- Adopt Semantic Versioning for releases.[web:1538][web:1544]
- Generate release recommendations from Conventional Commit history.[web:1503]
- Create and maintain a root `CHANGELOG.md` in a human-readable format based on Keep a
  Changelog.[web:1532]
- Automate changelog draft generation from commit history and tags.[web:1531][web:1539]
- Automate version bump suggestions from commit history and release
  rules.[web:1503][web:1538]
- Keep release review human-approved even when generation is automated.
- Decide whether release automation should be local-first, CI-driven, or support both
  modes.

### Packaging and source layout

- Move runtime code, Seed internals, and supporting Python modules into a `src/` layout.
- Improve import boundaries between CLI, runtime logic, library discovery, and
  feedback/state code.
- Use the post-branch refactor to prepare for packaging, tests, and cleaner tooling
  integration.

## Later

### Multi-library improvements

- Better ambiguity handling across many bound libraries.
- Optional library precedence helpers.
- Better library install and sync commands.

### Prompt lifecycle

- Formal promotion and rollback flows.
- Better environment assignment tooling.
- Optional richer version lineage.

### Search and discovery

- Multi-library search scopes.
- Saved collection groups.
- Metadata-based filtering beyond collection partitions.

### Shared standards

- Extract the Impromptu docs tooling into a reusable starter template.
- Publish a minimal shared repo standard for linting, docs quality, commit conventions,
  and release automation.
- Reuse the same standards across personal and team projects.

# Changelog

All notable changes to this library are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

______________________________________________________________________

## 2026-09-07 — Questioning & Local-Service Procurement Refactor

### Added

- `prompts/services/local-service-procurement/` — new kit (SKILL v0.3.0, README,
  brief template, changelog) for buying local professional services starting from
  natural language; owns the procurement workflow after discovery.
- `prompts/panel-of-judges/roles/specialists/service-provider-due-diligence-advisor.md`
  v0.3.0 — provider-evaluation specialist that proposes gates, evidence checks, and
  call/quote fields without asking user-facing question batches.
- `prompts/panel-of-judges/bundle.advisory-meeting-service-procurement.yaml` —
  advisory-meeting variant composing the advisor with questioning, procurement,
  and deep-research.
- `prompts/skillet/SKILL.md` — Skillet CLI authoring workflow for skills
  (status → spec → rendered skill → evals → validate → dry/baseline evals).
- `prompts/adhd/SKILL.md` — divergent-ideation skill.
- Per-scope changelogs: project (this file), per-skill
  (`prompts/<skill>/CHANGELOG.md`), and per-event
  (`prompts/panel-of-judges/events/<event>/CHANGELOG.md`).
- Commit messages now follow the Scoped Commits format (`<scope>: <description>`,
  <https://scopedcommits.com/>).

### Changed

- `prompts/questioning/SKILL.md` → v2.3.2 — natural-language-first discovery,
  two-sided understanding, goal stack, stakes triage, next-move routing (questions
  are optional), expectation calibration, fatigue protection, understanding
  confirmation, and learning handoffs. Now backed by `spec.md` (Skillet behavior
  contract) and judge-based eval cases for every behavior; `skillet validate`
  passes.
- Local-service-procurement artifacts now compose with Interaction Questioning
  v2.3.2 instead of duplicating discovery logic.

### Fixed

- `prompts/research/research/SKILL.md` — restored YAML frontmatter lost to an
  accidental edit.
- Panel-of-judges bundle variants `with-research` and `factory-review` referenced
  non-existent event directories and hard-failed; they now configure the shared
  `advisory-meeting` event.

______________________________________________________________________

## [Unreleased] — Documentation Reduction Pass

### Summary

Two-session documentation reduction pass across `impromptu/`, `factories/`, `seed/`,
and root. Goal: eliminate redundant READMEs, consolidate scattered setup content,
and give every remaining doc a single clear scope.

______________________________________________________________________

## Session 2 — 2026-04-01 / 2026-04-02 · factories/ and seed/

### Added

- `docs/setup.md` — new file consolidating registry setup, directory layout, factory
  registration instructions, registry JSON entries for all three current factories,
  match threshold guide, and shared troubleshooting; absorbs content previously
  scattered across individual factory READMEs
- `seed/orchestrator/README.md` — new file scoped to orchestrator inputs, outputs,
  which file to run (`.md` vs `.py` vs `.sh`), mode selection, and match thresholds

### Changed

- `README.md` (root) — rewritten as a minimal library entrypoint: one-paragraph
  description, mental model summary, directory map, and routing table; removed
  per-file descriptions, 5-step usage flow, and usage pattern examples
- `QUICKSTART.md` — rewritten to under 50 lines: three usage paths (Perplexity /
  Bash / Python), match confidence table, condensed troubleshooting; removed signal
  algorithm detail, batch examples, and registry format reference (moved to
  `docs/setup.md`)
- `seed/README.md` — expanded from stub (~900 chars) to full subsystem overview;
  now includes one section per component (profile, orchestrator, optimizer,
  factory-builder, role-specializer, strategy registry, factories registry) with role,
  inputs/outputs, and trigger conditions; subsumes content from four deleted component
  READMEs below
- `factories/sentry-support-tutor/README.md` — trimmed from ~8KB to ~3KB; removed
  emoji headers, "What's in This Package" directory tree, registry bash one-liner,
  recommended directory layout, and test queries; added pointer to `docs/setup.md`
- `factories/technical-tutor-for-self-learning/README.md` — trimmed from ~11KB to
  ~4KB; same removals as above; retained comparison table vs `factory-builder-v1`,
  domain types table, failure mode → countermeasure mapping, study plan scoping table,
  and example generation flow
- `factories/wealth-advisor-and-builder/README.md` — renamed from
  `weath-advisor-and-builder-factory-integration-guide.md`; reframed as README;
  trimmed "File Structure Required", "Next Steps", and "Complete Integration Package"
  footer; registry entry moved to `docs/setup.md`

### Deleted

- `docs/download-index.md` (`00-DOWNLOAD-INDEX.md`) — stale asset index with dead
  download link stubs; all useful content absorbed into `QUICKSTART.md` and
  `docs/setup.md`
- `seed/factory-builder/README.md` — content merged into `seed/README.md`
- `seed/optimizer/README.md` — content merged into `seed/README.md`
- `seed/profile/README.md` — content merged into `seed/README.md`
- `seed/specializer/README.md` — content merged into `seed/README.md`
- `seed/versions/README.md` — README for an empty directory; deleted pending actual
  archived content

### Net doc count (session 2)

| Location     | Before | After | Delta  |
| ------------ | ------ | ----- | ------ |
| Root         | 2      | 2     | —      |
| `docs/`      | 2      | 2     | —      |
| `seed/`      | 6      | 2     | −4     |
| `factories/` | 3      | 3     | —      |
| **Total**    | **13** | **9** | **−4** |

______________________________________________________________________

## Session 1 — 2026-04-01 · impromptu/

See `impromptu/CHANGELOG.md` for file-level detail.

### Summary

Refactoring pass on the `impromptu/` prompt directory. Prompt files normalized to
consistent naming conventions and structure; redundant documentation consolidated
or removed; directory brought into alignment with library conventions.

______________________________________________________________________

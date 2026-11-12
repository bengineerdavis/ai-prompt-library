---
id: APL-6
title: Migrate the library's whole task queue to backlog-py when the templates land
status: To Do
created_date: 2026-11-10 21:50
labels:
  - meta
  - workflow
  - deferred
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Why: backlog-py is added here for one cross-repo feature (APL-5). Deferred deliberately: fully migrating the library's queue belongs with the python-project-template and agentic-project-template stamp-down, not with a PII refactor.

Open questions to settle at that point:

- Which parts of TASKS.md migrate, and how completed narrative entries are preserved (they carry review conclusions worth keeping).
- Whether the library store gains orchestration (leases, claims) or stays a plain board.
- How the two repos' stores relate once both are backlog-py: two independent projects, or one with prefixes.
- What happens to backlog-py's dependency surface in a content-first repo whose only root executable is bundle.py.

Blocked on the template stamp-down. Do not start this before that lands.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [ ] #1 TASKS.md content is migrated or explicitly retired, with completed narrative preserved somewhere durable
- [ ] #2 Orchestration is either adopted or declined with a recorded reason
- [ ] #3 The relationship between the library and dotfiles stores is documented
- [ ] #4 The library still installs and passes pre-commit after the change

<!-- AC:END -->

## Implementation Notes

<!-- SECTION:IMPLEMENTATION_NOTES:BEGIN -->

<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->

<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done

<!-- DOD:BEGIN -->

<!-- DOD:END -->

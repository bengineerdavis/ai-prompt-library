---
id: APL-5
title: Adopt backlog-py as the library's task store, with cross-references to DOT
status: To Do
created_date: 2026-11-10 21:50
labels:
  - meta
  - workflow
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Why: this refactor spans the library (spec, SKILL.md, evals) and chezmoi (script, tests). TASKS.md alone cannot carry blocking edges or hold cross-repo references, and the author wants both repos to stop accumulating parallel queues.

Ship: an APL-prefixed backlog-py store at the library root, with an explicit ownership split and references in both directions.

Split: DOT owns the script, its tests and deployment in chezmoi; APL owns the skill spec, SKILL.md, eval cases and research. Each side names the other by id and path.

Full migration to backlog-py for the whole library is deferred to APL-6, which lands when the python and agentic templates are stamped onto this project.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [ ] #1 backlog/config.yml exists with prefix APL and projectName ai-prompt-library
- [ ] #2 AGENTS.md is untouched by the store's creation; no --agent-instructions were written
- [ ] #3 TASKS.md names backlog/ as the authoritative store so the two queues cannot silently diverge
- [ ] #4 Chezmoi DOT tasks for this refactor reference the APL ids and skills/pii-redaction/spec.md
- [ ] #5 APL tasks reference DOT ids and home/bin/executable_pii-redactor paths

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

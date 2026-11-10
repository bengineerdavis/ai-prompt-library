---
id: APL-11
title: Make CODING_STANDARDS.md a required file in agentic-project-template, gated
  by alint
status: To Do
created_date: 2026-11-11 00:00
labels:
- meta
- template
- alint
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Why: author directive (2026-11-10). The retro skill's argument is that the reviewing agent, which receives a diff and has the least context pressure, should own coding standards rather than the implementation agent, which is busy exploring and debugging. That argument only pays off if the file is guaranteed to exist and be read.

CODING_STANDARDS.md was added to THIS repo by the retro that produced this ticket (2026-11-10). It holds judgement calls only: spec scenarios as a test surface, preserving a constraint's reason when relaxing it, changelogs written for users, glossary vocabulary, synthesized fixtures. Mechanical rules deliberately stay in .alint.yml and .pre-commit-config.yaml, because a second source of truth drifts.

Ship: the file becomes part of the agentic layer stamped by `agentic-project-template layer .`, and alint gains an error-level rule requiring it, following the shape of the existing skills-have-authoring-specs dir_contains rule in this repo's .alint.yml.

Note the ownership axis: the agentic layer owns agent-facing concerns, and review standards are agent-facing. Do not put it in the base layer.

Sequencing: this is a template change, so it lands with the template stamp-down the author described, not with the PII work. It is filed here because the file being required was born here.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 agentic-project-template ships CODING_STANDARDS.md as part of its layer
- [ ] #2 An alint rule at level error fails a project missing the file, tested against a fixture that omits it
- [ ] #3 The template's AGENTS.md points at CODING_STANDARDS.md at the review stage, not the implementation stage
- [ ] #4 Mechanical rules are demonstrably absent from the template copy, so it does not become a second source of truth
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

---
id: APL-10
title: Ship pii-redactor as a script inside the pii-redaction skill
status: To Do
created_date: 2026-11-11 00:00
labels:
  - pii
  - tooling
  - portability
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->

Why: the skill specifies a tool it does not own. The implementation lives at home/bin/executable_pii-redactor in the dotfiles repo with tests at tests/pii_redactor/, so installing the skill gives you the spec and none of the tool. The author's position (2026-11-10): a skill and its tools live together where the skill is defined; a thin bin wrapper that makes it callable from the terminal is the dotfiles-managed part, and the skill does not need to know that wrapper exists.

Precedent in this repo: skills/naming/scripts/check-name is a skill-owned script, referenced from SKILL.md as scripts/check-name and listed in a Files section. Follow that shape.

Ship: move the tool into skills/pii-redaction/scripts/pii-redactor (or scripts/scrub), keep the dotfiles bin wrapper as a deploy-only shim, and move the tests alongside or into the skill's eval harness.

Open questions for implementation:

- Tests are 1180 lines in chezmoi (7 files). Do they move into the skill, or stay with the dotfiles repo that owns deployment? Argues for staying: they test the deployed artefact.
- The script imports only stdlib plus the llm CLI, so it is portable as a file. No packaging step needed.
- The dotfiles wrapper must keep working, including the review-gate prompt and --assume-reviewed.

Related: APL-9 (Python version support) governs what the moved script may assume.

<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria

<!-- AC:BEGIN -->

- [ ] #1 The tool lives under skills/pii-redaction/scripts/ and is referenced from SKILL.md the way skills/naming references scripts/check-name
- [ ] #2 A dotfiles bin wrapper still provides the terminal command, and the skill does not reference the wrapper's path
- [ ] #3 The test suite runs against the skill-owned script
- [ ] #4 Installing the skill alone yields a runnable tool

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

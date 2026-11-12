---
id: APL-22
title: Restore support-partner-deep-research eval fixture references
status: Done
created_date: 2026-11-12 21:24
labels:
- support-partner-deep-research
- evals
- fixtures
references:
- skills/support-partner-deep-research/SKILL.md
- skills/support-partner-deep-research/evals/cases
updated_date: 2026-11-12 21:47
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A scoped pre-commit run for TASK-233 and TASK-234 on 2026-11-12 failed alint rule installable-skills-are-valid: skills/support-partner-deep-research/SKILL.md references missing raw-log-with-pii and misinvocation fixtures. This work is separate from the support pipeline and anonymization changes currently in progress.

Ship:
- Restore the synthetic fixture directories or update their case references so every support-partner-deep-research eval case resolves to its intended starting state.
- Verify the complete skill-validation gate and the intended fixture failures without changing unrelated support behavior.

Constraints:
- Coordinate with the concurrent support-partner-deep-research and anonymization work before editing its files.
- Keep all fixture data synthetic; do not derive it from real customer material or private configuration.
- Do not bypass or weaken the alint or Skillet gate.

Recorded by the maintainer's agent 2026-11-12: surfaced during scoped follow-up verification, not authorized for repair here.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Every referenced support-partner-deep-research eval fixture resolves to an existing synthetic fixture directory.
- [x] #2 python3 scripts/check_skillet_freshness.py skills/support-partner-deep-research passes.
- [x] #3 npx -y @sentry/skillet@latest validate skills/support-partner-deep-research passes.
- [x] #4 pre-commit run --all-files passes without skipping the alint rule, or any independent blocker is explicitly recorded and dispositioned.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:IMPLEMENTATION_NOTES:BEGIN -->
Correction 2026-11-12: main commit 0e876ab adds both previously missing support-partner-deep-research fixture directories. APL-22 must not assume the fixtures are still missing or duplicate that work. The scoped follow-up's base commit a54342a predates 0e876ab, so its missing-failure observation is historical. Re-verify the complete gate on a current-main integration baseline before closing this ticket.
<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Resolved without duplicating concurrent work: commit 0e876ab restored both synthetic fixture directories. Direct Skillet validation and the full and changed-file alint checks pass on the current-main combined snapshot. The pre-commit all-files gate was run, but intermittent failures contradicted those direct results; they remain open as APL-25. No hook was skipped and no unrelated skill was re-rendered to produce a pass.
<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done
<!-- DOD:BEGIN -->
<!-- DOD:END -->

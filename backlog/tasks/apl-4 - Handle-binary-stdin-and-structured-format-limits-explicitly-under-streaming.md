---
id: APL-4
title: Handle binary, stdin and structured-format limits explicitly under streaming
status: To Do
created_date: 2026-11-10 21:50
labels:
- pii
- streaming
- input-handling
dependencies:
- APL-1
- APL-2
updated_date: 2026-11-10 21:50
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Why: three input shapes have no defined behaviour once input streams. Binary is decoded with surrogateescape today and "verifies clean" because nothing matches. stdin cannot be rewound for a carry window. TOML has no stdlib parser on Python older than 3.11, and the script claims 3.9 compatibility.

Ship: refuse binary, stream pipes forward-only, and make each structured format's guarantee explicit and visible.

Design locked: binary refused with the file named; stdin streamed forward-only with a bounded carry buffer, --plan refused on stdin with the reason given; YAML split on column-0 --- then line atoms within a document plus one stderr note that structure is not parse-verified; TOML parsed only where tomllib exists, otherwise textual with the same honesty.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Binary input is refused with a message naming the file
- [ ] #2 cat file | pii-redactor streams forward-only with bounded memory, with a clear error naming the stage when it fails
- [ ] #3 --plan on stdin refuses and explains why there is no total size to plan from
- [ ] #4 YAML splits on --- documents and line atoms within one; one stderr note states structure is not parse-verified
- [ ] #5 TOML behaviour is identical whether or not tomllib is importable, or the run refuses with an explicit message
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

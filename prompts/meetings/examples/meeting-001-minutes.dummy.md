# Meeting 001 Minutes (Example)

Date: 2026-05-02  
Chair: Chair  
Facilitator: Guide  
Note-Taker: Log  

## Goal

Clarify how the reusable meetings kit should be structured so it can be copied into other prompt and agent repositories.

## Agenda

1. Review current meetings directory layout.
2. Decide where example minutes and working minutes should live.
3. Confirm initial roles and responsibilities.
4. Capture open questions for a future refactor.

## Discussion summary

- The meetings kit should live under `prompts/meetings` as a self-contained, copyable directory.
- Example minutes belong in `examples/` so they can be reused as templates without mixing with live project data.
- Working minutes for a specific project should live in `minutes/` (or in the governed project repo that uses this kit).
- Roles for Chair, Facilitator, Note-Taker, Deep Researcher, Recruiter, and the Advisors panel are sufficient for an initial version.

## Decisions

- Keep `examples/meeting-001-minutes.md` as a reusable example file for the kit.
- Use `minutes/` for working session records stored in this library.
- Treat the current layout as a rough draft that can be refactored once the impromptu library and bundler are more mature.

## Deferred items

- Introduce a machine-readable manifest (for example `index.yaml`) for the meetings kit.
- Decide whether `minutes/` should later move to `data/minutes/` under a broader project-structure convention.
- Align naming and structure with the impromptu design docs once they stabilize.

## Action items

- [ ] Update `README.md` and `index.md` to reference `examples/` and `minutes/`.
- [ ] Ensure each role file is self-describing enough for future manifest work.
- [ ] Capture any future structural changes in the impromptu design docs.
---
id: meeting-001
title: Meeting 1 — PREPs, advisory roles, and meeting kit design
description: Example minutes for the first prompt-spec advisory session covering PREPs, document topology, role design, meeting governance, and reusable meeting artifacts.
version: 0.1.0
type: documentation
license: MIT
context:
  include: true
x-meeting:
  session: prompt-spec advisory panel
  date: 2026-05-02
  roles:
    chair: ben
    facilitator: guide
    note_taker: log
    advisors:
      - prag
      - zen
      - mesh
    specialists:
      - scout
      - draft
      - match
  chair_preferences:
    structural_changes_roles: once
    structural_changes_norms: always
---

> This file is an example minutes document. The canonical record for this meeting lives in the `prompt-spec` repository under `docs/meetings/meeting-001-minutes.md`.

# Meeting 1 — PREPs, advisory roles, and meeting kit design

## 1. Session Goal

- Clarify whether `prompt-spec` should adopt a lightweight proposal process inspired by PEPs and Oxide RFDs.
- Review the current project shape and decide how a document-first collaboration model should fit the repo.
- Design a reusable meeting kit for future advisory sessions, including roles, rules, minutes, and a bundling workflow.

## 2. Agenda (Planned vs Actual)

**Planned agenda:**

1. Learn from PEPs and RFDs and decide whether PREPs are needed.
1. Review `prompt-spec` and identify document-topology and rule-portability questions.
1. Establish advisor roles, meeting governance, and reusable artifacts for future sessions.

**Actual flow:**

- The discussion began with PEPs, RFDs, and the current `prompt-spec` repository structure.
- The conversation expanded into role design, governance, minutes, preferences, aliases, and packaging the meeting system as reusable prompts and templates.
- The session ended with a plan to adjourn, preserve context in minutes, and move the resulting meeting kit into a `meetings/` subdirectory suitable for a prompt library.

## 3. Key Decisions

| ID  | Decision                                                                                                                                                            | Rationale                                                                                                                                                 | Related Sections      |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| D1  | PREPs will be treated as lightweight proposal documents for rules, families, and process changes rather than a full copy of the PEP or RFC process.                 | The project needs traceable discussion and decision records without prematurely adopting heavy governance.                                                | §6 Q1, §6 Q2, §7 DR-1 |
| D2  | `prompt-spec` should continue to focus first on raw prompt files (`.txt` / `.md`) before expanding to harness formats like `AGENTS.md` or `CLAUDE.md`.              | This keeps early portability claims narrow and honest while the rule catalog is still in alpha.                                                           | §6 Q3, §7 DR-2        |
| D3  | The meeting system should have explicit support roles in addition to advisors: Facilitator, Note-Taker, Deep Researcher, Document Architect, and Recruiter.         | The conversation showed a real need to separate flow management, note capture, research, drafting, and role design into distinct responsibilities.        | §6 Q4, §6 Q5          |
| D4  | Structural changes to the meeting should require Chair consent by default, with the option for the Chair to grant broader one-time permission for repeated changes. | This preserves human control over meeting governance while still allowing smoother operation when the Chair wants to delegate.                            | §6 Q5                 |
| D5  | Meeting minutes should use prompt-spec-compatible frontmatter and place meeting-specific metadata under an `x-meeting` extension key.                               | The frontmatter schema allows only the core top-level keys plus `x-*` extensions, so meeting metadata must be nested under `x-meeting` to stay compliant. | §6 Q6                 |
| D6  | The meeting kit should live in a `meetings/` directory with templates, role prompts, example minutes, preferences, and a CLI bundler.                               | Reusable artifacts make the process easier to run from the command line, system prompts, or direct chat copy-paste.                                       | §6 Q7                 |

## 4. Deferred Items

| ID  | Item                                                                                      | Why deferred                                                                                                                         | Revisit trigger                                                                |
| --- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| DE1 | Decide which single document becomes the “constitution” that PREPs are submitted against. | The session identified the issue but did not fully resolve whether this should be a renamed `SPEC.md`, a meta-PREP, or another file. | Start of the next substantive prompt-spec design meeting.                      |
| DE2 | Choose the first real PREP from the roadmap or current open design questions.             | The group agreed on the need for PREPs in principle, but not yet on the first concrete proposal to draft.                            | After reviewing the roadmap and current catalog with the meeting kit in place. |
| DE3 | Classify current rules as surface-agnostic vs surface-aware.                              | The need was clear, but the group did not work through the catalog rule by rule in this session.                                     | Next design session focused on portability taxonomy.                           |
| DE4 | Expand from raw prompt files to harness and provider-specific modules.                    | The group intentionally narrowed scope to avoid over-designing the standard too early.                                               | After the raw-prompt rule catalog stabilizes.                                  |

## 5. Promises / Action Items

| ID  | Owner       | Item                                                                                                                                           | Due / Trigger                   | Status  |
| --- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------- |
| P1  | Chair       | Resume the advisory session later using the minutes as continuity context.                                                                     | Next meeting                    | Open    |
| P2  | Chair       | Review which current roadmap item is the best candidate for the first actual PREP.                                                             | Next design-focused meeting     | Open    |
| P3  | Log / Guide | Keep the meeting format optimized for machine reuse while still being readable to human participants.                                          | Ongoing                         | Open    |
| P4  | Draft       | Turn the meeting kit into reusable files for the prompt library, including role prompts and templates.                                         | Initial packaging pass          | Started |
| P5  | Scout       | Continue surveying adjacent tools and standards to test whether `prompt-spec` fills a real community gap instead of duplicating existing work. | Future research-focused meeting | Open    |

## 6. Round-by-Round Q&A

### Round 1

**Prag asked (Q1):**

> Which document is actually canonical today, given drift across `spec.md`, `CONTRIBUTING.md`, `RULES.md`, and the rule template?

**Chair answered (A1):**

> No single answer exists yet. `spec.md` feels like design intent, `CONTRIBUTING.md` gets into how to build, and `RULES.md` plus the template also matter. The drift is real and needs wrangling.

**Notes:**

- This exposed a document-topology problem rather than a mere wording problem.
- The conversation established that PREPs should not swallow every core project document.
- Related decisions: D1, D5.

______________________________________________________________________

**Zen asked (Q2):**

> What is the smallest useful thing to adopt from PEPs and RFDs without copying the whole process?

**Chair answered (A2):**

> The goal is influence, not imitation. PREPs would be structured enhancement proposals for rules or families of rules, separate from routine fixes and separate from heavy governance.

**Notes:**

- The answer strongly favored YAGNI: adopt the useful behavior, not the entire ceremony.
- This set the working definition of PREPs used for the rest of the session.
- Related decisions: D1.

______________________________________________________________________

**Mesh asked (Q3):**

> What is the actual output of a rule in this standard, and how portable is the current idea across surfaces and frameworks?

**Chair answered (A3):**

> The intended outputs are all three: human-readable warning, machine-parseable lint result, and suggested rewrite. Early work should focus on raw prompt files first; broader surface support and provider modules can come later.

**Notes:**

- This led directly to the raw-prompts-first scope boundary.
- It also surfaced the need to classify rules as portable vs surface-aware in a future meeting.
- Related decisions: D2.

### Round 2

**Joint panel question (Q4):**

> How should the meeting itself be structured so future sessions can pick up where this one leaves off?

**Chair answered (A4):**

> The group needs a reusable meeting system with a document-first trail: meeting rules, notes, minutes, and reusable prompts for each role.

**Notes:**

- This prompted the creation of support roles and reusable artifacts.
- The meeting became a meta-design exercise for its own future operation.
- Related decisions: D3, D6.

______________________________________________________________________

**Joint panel question (Q5):**

> Who controls changes to the meeting itself, such as adding roles or updating aliases and norms?

**Chair answered (A5):**

> By default, changes that alter the nature of the meeting require Chair approval, though the Chair can optionally grant one-time broader permission if they do not want to be asked repeatedly.

**Notes:**

- This established a governance model for the meeting independent of prompt-spec’s eventual PREP process.
- It also created a need for preferences that can be saved and reused across sessions.
- Related decisions: D4.

______________________________________________________________________

**Joint panel question (Q6):**

> How should meeting frontmatter be designed so it stays compatible with prompt-spec’s frontmatter rules?

**Chair answered (A6):**

> The meeting metadata should be nested under `x-meeting` so the files remain compliant with the standard frontmatter conventions.

**Notes:**

- This decision came after explicitly checking the frontmatter rules document and confirming that unknown non-`x-*` keys are invalid.
- Related decisions: D5.

______________________________________________________________________

**Joint panel question (Q7):**

> How should these files be packaged so the meeting system is easy to use outside this specific chat?

**Chair answered (A7):**

> The kit should live under `meetings/` in the prompt library, and there should be a script that bundles the files for command-line use or prompt assembly.

**Notes:**

- The bundler requirement makes the meeting kit operable as infrastructure rather than only as ad hoc chat context.
- Related decisions: D6.

## 7. Open Questions Carried Forward

- [ ] OQ1: Which document becomes the constitutional document PREPs are submitted against? (related decisions: D1, D5)
- [ ] OQ2: Which roadmap item should become the first actual PREP? (related decisions: D1)
- [ ] OQ3: Which current rules are genuinely surface-agnostic, and which require surface-aware logic? (related decisions: D2)
- [ ] OQ4: How much of the meeting kit should eventually feed back into `prompt-spec`
  itself versus living only in the prompt library? (related decisions: D6)

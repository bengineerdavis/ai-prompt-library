# Prompt Project Structure (Rough Draft)

> **Status:** Rough draft for capture and discussion. This is intentionally simple and provisional. The goal is to record the current structure and naming decisions now, then refactor later once the workflow is proven.

## Table of contents

- [Purpose](#purpose)
- [Core idea](#core-idea)
- [Draft layout](#draft-layout)
- [Why this split](#why-this-split)
- [Core vs expanded](#core-vs-expanded)
- [Working interpretation](#working-interpretation)
- [Self-describing files](#self-describing-files)
- [Notes for later refactor](#notes-for-later-refactor)

## Purpose

This structure is meant to support both:

- a **single prompt**,
- and a **collection of related prompts** for one function or application.

The main design goal is to keep **prompt source**, **generated prompt artifacts**, and **saved project data** separate so the layout stays readable as the project grows.[1][2]

## Core idea

There are three kinds of files in this project:

- **Prompt source**: the authored logic used to compose prompts, such as prompts, roles, context, and reusable parts.[1][3]
- **Generated artifacts**: compiled or paste-ready prompt bundles that can usually be rebuilt from source, stored in `generated/`.[2]
- **Saved project data**: outputs and state created while using the prompt collection, stored in `data/`, such as meeting minutes or resumable session notes.[4][5]

A simple rule of thumb:

- If it can be **rebuilt from source**, it belongs in `generated/`.[2]
- If it must be **kept across sessions**, it belongs in `data/`.[4]

## Draft layout

```text
prompts/
  meetings/
    README.md                  # CORE: human overview
    index.yaml                 # CORE: manifest / registry entrypoint

    prompts/                   # CORE: prompt source and composition
      main.md                  # CORE: smallest useful entry prompt

      flows/                   # EXPANDED: related prompts for same purpose
        start-meeting.md
        resume-meeting.md
        review-protocol.md
        capture-minutes.md

      roles/                   # EXPANDED: reusable personas / participants
        facilitator.md
        note-taker.md
        pragmatist.md

      context/                 # EXPANDED: supporting source material
        meeting-charter.md
        preferences.md

      parts/                   # EXPANDED: reusable fragments / sections
        output-format.md
        protocol-summary.md

    generated/                 # CORE: compiled prompt artifacts, safe to overwrite
      main.txt
      start-meeting.txt
      resume-meeting.txt
      roles.txt

    data/                      # EXPANDED: persisted outputs and state
      minutes/                 # EXPANDED: meeting records users will look for directly
        2026-05-02-design-review.md
      sessions/                # EXPANDED: resumable notes / checkpoints
        active-session.md
      drafts/                  # EXPANDED: optional working artifacts

    docs/                      # EXPANDED: examples and change notes
      examples/
      changes/
```

## Why this split

Putting all composition-related assets under `prompts/` keeps the prompt logic together and makes it easier to understand what is part of the reusable system versus what is produced during use.[1][3]

Keeping `data/` separate makes applied outputs easier to find. For a meetings project, users will naturally look for meeting records under `minutes/` or `data/minutes/`, not inside the prompt source tree.[4]

Keeping `generated/` separate preserves a clean distinction between authored source and machine-built prompt bundles.[2]

## Core vs expanded

The **core** version of a project only needs:

- `README.md`
- `index.yaml`
- `prompts/main.md`
- `generated/`

The **expanded** version adds:

- `prompts/flows/`
- `prompts/roles/`
- `prompts/context/`
- `prompts/parts/`
- `data/`
- `docs/`

This means a single prompt can start small and later grow into a richer prompt project without changing the overall model.[1][6]

## Working interpretation

This draft treats the project a bit like an application with a small source tree and a small working-data area:[4][2]

- `prompts/` = source logic
- `generated/` = rebuilt prompt artifacts
- `data/` = saved outputs and ongoing state

That model should generalize beyond meetings as well. A research project might use `data/notes/`, while another workflow might use `data/summaries/` or `data/reviews/`.[4][5]

Useful related references for later refinement:

- [Better Agents structure notes](https://github.com/langwatch/better-agents/blob/main/docs/STRUCTURE.md) for agent/project layout ideas.[6]
- [LangWatch Better Agents overview](https://langwatch.ai/docs/better-agents/overview) for the broader framing around structured agent projects.[1]
- [Genkit Dotprompt docs](https://genkit.dev/docs/js/dotprompt/) for self-describing prompt files and metadata-driven prompt management.[7]
- [Google dotprompt repository](https://github.com/google/dotprompt) for prompt template organization and executable prompt files.[8]
- [Reddit: How I structure Claude Code projects (CLAUDE.md, Skills, MCP)](https://www.reddit.com/r/ClaudeAI/comments/1rfwmlh/how_i_structure_claude_code_projects_claudemd/) for practical repo-structure ideas from real users.[9]
- [Reddit: Best practices project structure](https://www.reddit.com/r/ClaudeCode/comments/1qub3fm/best_practices_project_structure_ie_interplay/) for thoughts on separating project memory, agents, and skills.[10]
- [Reddit: Claude Code project structure diagram](https://www.reddit.com/r/claude/comments/1rsdoth/claude_code_project_structure_diagram_i_came/) for examples of how people split memory, skills, hooks, docs, and source.[11]
- [Reddit: Claude Code structure that didn't break after 2–3 real projects](https://www.reddit.com/r/ClaudeCode/comments/1saemnh/claude_code_structure_that_didnt_break_after_23/) for practical heuristics like splitting by intent instead of dumping everything into one place.[12]

## Self-describing files

This structure assumes the directory layout may change over time.[8][7]

For that reason, each important source file should contain enough local context to be understood and migrated later, even if it is viewed outside its original folder.[8][13] In practice, that means prompt-related files should be self-describing: they should include a clear purpose, lightweight metadata, and enough context to show how they are used and what they depend on.[8][7]

The goal is to make future refactors easier for both humans and AI-assisted tooling. A later migration should be able to interpret the files, propose moves or rewrites, and then have those changes reviewed by a human rather than requiring a full manual reconstruction of project intent.[14][15]

## Notes for later refactor

This draft is intentionally not final.

Open questions to revisit later:

- Whether `flows/` is the best name for related prompts.
- Whether some projects should use a top-level domain-specific output directory instead of `data/`.
- How much metadata belongs in `index.yaml` versus prompt frontmatter.
- Whether `docs/` should remain optional or become standardized.
- Which service-specific or tool-specific layouts deserve their own optimized variants.

For now, the priority is clarity and a stable working layout, not perfect taxonomy.

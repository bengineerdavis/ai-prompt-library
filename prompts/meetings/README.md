# Meetings

Reusable advisory-meeting kit for prompt and agent work.

This directory packages a document-first meeting workflow that can be reused across projects such as `prompt-spec`, `impromptu`, and related prompt or agent repositories.

## Purpose

The goal of this kit is to make meetings easier to run, easier to resume, and easier to review across different contexts:

- direct chat sessions,
- system-prompt assembly,
- local CLI workflows,
- and project-specific meeting archives.

## Contents

- `index.md` — human-readable index for the meetings kit.
- `context/` — meeting norms, reusable templates, and preferences.
- `roles/` — reusable role definitions and meeting participants.
- `examples/` — concrete example meeting artifacts.
- `minutes/` — working meeting records kept locally for this library when needed.

## Design principles

- Markdown-first.
- Human-readable in raw form.
- Machine-friendly structure where it helps continuity.
- Reusable across repos with minimal adaptation.
- Chair-controlled governance for structural meeting changes by default.

## Recommended use

1. Copy this directory into a prompt, standards, or agent repository.
2. Adapt the context files and role prompts for that project.
3. Record actual meeting minutes in `minutes/` or in the governed project repo.
4. Reuse the template, roles, and examples for future sessions.

## Notes

This is the current reusable meetings kit layout.

`index.md` is the current human-readable entry point. A later refactor may add or replace it with a machine-readable manifest such as `index.yaml`.

This layout is being shaped alongside the broader prompt templated project structure draft.
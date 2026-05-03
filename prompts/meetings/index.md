---
id: meetings-index
title: Meetings Index
description: Human-readable index for the reusable meetings library.
version: 0.1.0
type: index
license: MIT
context:
  include: true
---

# Meetings Index

This file is the current human-readable index for the reusable meetings library.

For general orientation, start with [README.md](./README.md).

## Purpose

This file gives the meetings kit a stable index target for humans today and for future tooling later.

A later refactor may add or replace this file with a machine-readable manifest such as `index.yaml`.

## Current structure

- `README.md` — overview and usage guidance.
- `context/meetings-charter.md` — governance defaults and meeting norms.
- `context/meeting-template.md` — reusable session template.
- `context/preferences.md` — default Chair preferences.
- `roles/` — reusable role definitions.
- `minutes/` — working meeting records held locally for this library, if any.
- `examples/` — sample meeting artifacts.

## Roles

- `roles/chair.md` — session owner and final decision-maker.
- `roles/facilitator.md` — runs flow and keeps the meeting on track.
- `roles/note-taker.md` — records durable meeting minutes and follow-up state.
- `roles/deep-researcher.md` — brings in targeted external evidence when needed.
- `roles/recruiter.md` — proposes role changes when recurring gaps appear.
- `roles/advisors.md` — advisor panel covering pragmatism, minimalism, and systems thinking.

## Working model

This meetings kit is intended to behave like a small reusable application:

- reusable meeting source files live here,
- example artifacts live in `examples/`,
- and real working minutes can live in `minutes/` or in the governed project that uses this kit.

## Future direction

This kit is being aligned with the broader prompt templated project structure draft. The long-term direction is to separate prompt source, generated artifacts, and saved project data more explicitly as the library evolves.
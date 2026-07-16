# Bundler

The bundler assembles a paste-ready session prompt from reusable source files in a collection.

For structured collections such as `panel-of-judges`, it combines shared context, an event definition, optional event preferences, selected roles, optional skills, optional included context, and an optional session prompt into a single output file you can paste into a chat or CLI tool.

## Table of contents

- [Quick start](#quick-start)
- [Config shape](#config-shape)
- [Config location](#config-location)
- [Strict event naming](#strict-event-naming)
- [What gets bundled](#what-gets-bundled)
- [Event-local context](#event-local-context)
- [Output](#output)
- [Flags](#flags)
- [Naming guidance](#naming-guidance)

## Quick start

Run the default root-level config for a collection:

```bash
./bundle.py -p panel-of-judges
```

Preview what would be included without writing output:

```bash
./bundle.py -p panel-of-judges --dry-run
```

Run a specific root-level config file:

```bash
./bundle.py -c prompts/panel-of-judges/bundle.advisory-meeting-with-research.yaml
```

## Config shape

A bundle config defines one session assembly.

It may specify:

- the active event,
- participant roles,
- optional skills,
- optional included context,
- optional defaults inheritance.

Example:

```yaml
event:
  name: advisory-meeting

participants:
  roles:
    - chair
    - facilitator
    - note-taker
    - pragmatist
    - minimalist
    - systems-thinker

skills:
  - analysis
  - deep-research

include:
  context:
    - handoff-context
    - events/advisory-meeting/data/minutes/advisory-meeting-001-minutes.md
```

If you use defaults inheritance, keep the reference inside the `event` mapping:

```yaml
event:
  name: advisory-meeting
  defaults: defaults/base-meeting.yaml
```

## Config location

Bundle config files currently live at the collection root.

Examples:

```text
prompts/panel-of-judges/bundle.yaml
prompts/panel-of-judges/bundle.advisory-meeting.yaml
prompts/panel-of-judges/bundle.advisory-meeting-with-research.yaml
```

When no config path is provided, `bundle.py` looks for `bundle.yaml` first and then falls back to the first `bundle.*.yaml` file in the collection root.

## Strict event naming

The value of `event.name` must exactly match an existing event directory under the collection’s `events/` directory.

Example:

```yaml
event:
  name: advisory-meeting
```

This must correspond to:

```text
prompts/panel-of-judges/events/advisory-meeting/
```

`event.name` is the canonical event type identifier. The bundler does not resolve aliases.

If the directory does not exist, the bundler fails with an error instead of guessing.

## What gets bundled

For a structured collection, the bundler assembles files in this order:

1. `context/charter.md` or `context/meetings-charter.md`
2. `events/<event>/event.md`
3. `events/<event>/preferences.md` if present
4. files listed in `include.context`
5. role files from `roles/`, `roles/judges/`, or `roles/specialists/`
6. skill files from `skills/`
7. `events/<event>/session-prompt.md` or `templates/meeting-session-prompt.md`

Missing optional files are skipped with warnings. Missing role or skill files also warn rather than stopping the bundle.

## Event-local context

Although bundle config files live at the collection root, working context for a specific event type can live under that event directory.

Recommended pattern:

```text
events/<event-type>/data/
```

For saved minutes:

```text
events/<event-type>/data/minutes/<event-type>-NNN-minutes.md
```

To include event-local history in a new session, reference it through `include.context` using a path relative to the collection root.

Example:

```yaml
include:
  context:
    - handoff-context
    - events/advisory-meeting/data/minutes/advisory-meeting-001-minutes.md
```

The special `handoff-context` token resolves to `events/<event>/handoff-context.md` first, and falls back to a collection-root `handoff-context.md` if no event-local file exists.

## Output

By default, output is written to:

```text
prompts/<collection>/generated/session.txt
```

The `generated/` directory is for rebuilt output, not authored source, so it is safe to overwrite.

Use `-o` to choose a custom output path.

## Flags

| Flag | Description |
|---|---|
| `-p`, `--collection` | Collection name under `prompts/` |
| `-c`, `--config` | Path to a bundle config YAML |
| `-o`, `--output` | Write to a custom output file |
| `--dry-run` | Print files that would be included without writing output |
| `--list` | List collections and available bundle configs |

## Naming guidance

Use root-level config names such as:

```text
bundle.yaml
bundle.advisory-meeting.yaml
bundle.advisory-meeting-with-research.yaml
bundle.brainstorming.yaml
```

Use canonical event directory slugs in `event.name`.

Use `include.context` for event-local continuity files, including prior minutes and handoff material.
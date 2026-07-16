# Bundler

The bundler assembles a paste-ready session prompt from reusable source files.

It concatenates the charter, event definition, event preferences, optional context files, role files, skill files, optional templates/factory/roadmap material, and the session prompt template into a single output file you can paste into a chat or CLI tool.[file:103][file:80]

## Quick start

For an advisory meeting with default roles:

```bash
# from repo root
./bundle.py -p panel-of-judges
```

Output is written to `prompts/panel-of-judges/generated/session.txt` by default.[file:103] Copy and paste that file into your chat.

### Example workflow

```bash
# list available collections and their bundle configs
./bundle.py --list

# default advisory meeting — no arguments beyond collection
./bundle.py -p panel-of-judges

# preview what would be included without writing
./bundle.py -p panel-of-judges --dry-run

# use a named config variant
./bundle.py -p panel-of-judges -c prompts/panel-of-judges/bundle.advisory-meeting-with-research.yaml --dry-run

# run the same variant from inside the collection directory
cd prompts/panel-of-judges
../../bundle.py -p panel-of-judges -c bundle.advisory-meeting-with-research.yaml
```

## CLI

The bundler is a Python script with inline `uv` metadata and one executable entry point.[file:103]

```bash
./bundle.py [OPTIONS]
```

### Flags

| Flag                | Short | Description                                                                 |
|---------------------|-------|-----------------------------------------------------------------------------|
| `--collection`      | `-p`  | Collection name under `prompts/` (e.g. `panel-of-judges`)                  |
| `--config <file>`   | `-c`  | Path to a bundle config YAML (relative or absolute)                        |
| `--output <file>`   | `-o`  | Output file path (defaults to `<collection>/generated/session.txt`)       |
| `--dry-run`         |       | Print files that would be included without writing output                  |
| `--list`            |       | List collections and their bundle configs                                  |
| `--help`            | `-h`  | Show usage                                                                 |

Rules:

- You must specify at least a collection (`-p`) or an explicit config (`-c`).[file:103]
- When only `-p` is provided, the bundler discovers a default config inside that collection.[file:103]
- When `-c` is provided, the collection is inferred from the config’s parent directory if `-p` is omitted.[file:103]

## Collections

A collection is a directory under `prompts/` that holds events, roles, and context for a reusable interaction kit.[file:12][file:103]

### Listing collections

```bash
./bundle.py --list
```

This prints something like:

```text
Collections in /path/to/repo/prompts:

panel-of-judges/
  bundle.yaml
  bundle.advisory-meeting.yaml
  bundle.advisory-meeting-with-research.yaml

another-collection/
  bundle.yaml
```

For each collection, the bundler lists `bundle.yaml` and any `bundle.*.yaml` files it finds.[file:103]

### Collection structure (panel-of-judges)

The `panel-of-judges` collection is structured like this:[file:12]

```text
prompts/panel-of-judges/
  README.md
  bundle.yaml
  bundle.advisory-meeting.yaml
  bundle.advisory-meeting-with-research.yaml
  defaults.advisory-meeting.yaml
  context/
    charter.md
    ...
  events/
    advisory-meeting/
      event.md
      preferences.md
      session-prompt.md
      ...
  roles/
    chair.md
    facilitator.md
    note-taker.md
    judges/
      pragmatist.md
      minimalist.md
      systems-thinker.md
      ...
    specialists/
      deep-researcher.md
      ...
  skills/
    deep-research.md
    analysis.md
    ...
  templates/
    meeting-session-prompt.md
    ...
  generated/
    session.txt
  data/
    ...
  ROADMAP.md        # optional, meta/factory use
  handoff-context.md  # optional, cross-session continuity
```

## Config files

Config files tell the bundler which event, roles, skills, and include options to use when assembling a session.[file:103]

Configs are YAML mappings with four main sections:

- `event`
- `participants`
- `skills`
- `include`

### Basic schema

```yaml
event:
  name: advisory-meeting
  defaults: defaults.advisory-meeting.yaml   # optional

participants:
  roles:
    - chair
    - facilitator
    - note-taker

skills:
  - deep-research
  - analysis

include:
  context:
    - handoff-context
    - data/minutes/meeting-001-minutes.md
  templates: false
  factories: false
  roadmap: false
```

#### `event`

- `name` (required): event type under `events/` (e.g. `advisory-meeting`).[file:103]
- `defaults` (optional): path to another config file used as a defaults source for this config.[file:103]

#### `participants`

- `roles` (list): role identifiers to include. For each role, the bundler search order is:[file:103]

  1. `roles/<role>.md`
  2. `roles/judges/<role>.md`
  3. `roles/specialists/<role>.md`

Missing role files produce warnings but do not stop the bundler.[file:103]

#### `skills`

- `skills` (list): skill identifiers to include. Each is resolved as `skills/<skill>.md`.[file:103]

Missing skill files produce warnings but do not stop the bundler.[file:103]

#### `include`

- `context` (list of strings): extra context files to include.[file:103]
  - special value: `handoff-context`  
    - tries `events/<event>/handoff-context.md`, then `<collection>/handoff-context.md`.[file:103]
  - otherwise: treated as a path relative to the collection root.
- `templates` (bool): if `true`, include all `templates/*.md` files.[file:103]
- `factories` (bool or list): meta/factory inputs.
  - `false`: do not include factory material.
  - `true`: search for directories `factories/`, `factory/`, or `meta/` and include all `.md` files found.[file:103]
  - list: each entry is a file or directory path relative to the collection root.
    - file paths: included directly if present.
    - directory paths: include all `.md` files under that directory.[file:103]
- `roadmap` (bool): if `true`, include `ROADMAP.md` from the collection root, or `docs/ROADMAP.md` as fallback.[file:103]

### Using defaults

Defaults configs let you define a base event configuration once and then apply variants by layering specific changes on top.[file:103]

#### Defaults file

```yaml
# defaults.advisory-meeting.yaml
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

skills: []

include:
  context: []
  templates: false
  factories: false
  roadmap: false
```

#### Default advisory bundle

```yaml
# bundle.advisory-meeting.yaml
event:
  name: advisory-meeting
  defaults: defaults.advisory-meeting.yaml

participants:
  roles: []        # no extra roles beyond defaults

skills: []         # no extra skills beyond defaults

include:
  context: []      # no extra context beyond defaults
  templates: false
  factories: false
  roadmap: false
```

#### Advisory with research

```yaml
# bundle.advisory-meeting-with-research.yaml
event:
  name: advisory-meeting
  defaults: defaults.advisory-meeting.yaml

participants:
  roles:
    - deep-researcher
    - recruiter
    - people-expert

skills:
  - deep-research
  - analysis

include:
  context:
    - handoff-context
  templates: false
  factories: false
  roadmap: false
```

##### Merging rules

When `event.defaults` is set, the bundler:

1. Loads the defaults config.
2. Loads the main config.
3. Applies `merge_configs(defaults, override)`.[file:103]

Special behavior:

- `event`: shallow mapping merge (override wins per key).[file:103]
- `participants.roles`: de-duplicated union of defaults and override roles (override roles append).[file:103]
- `skills`: de-duplicated union of defaults and override skills.[file:103]
- `include.context`: de-duplicated union of defaults and override context entries.[file:103]
- Other `include` keys (`templates`, `factories`, `roadmap`): standard override semantics.[file:103]

## What gets bundled

For a structured collection, the bundler includes files in this order:[file:103][file:80]

1. **Charter**

   - `context/charter.md`, or
   - `context/meetings-charter.md` as fallback.

2. **Event definition**

   - `events/<event>/event.md`.

3. **Event preferences**

   - `events/<event>/preferences.md` (if present).

4. **Extra context**

   From `include.context`:

   - `handoff-context`:
     - `events/<event>/handoff-context.md`, else
     - `<collection>/handoff-context.md`.
   - other strings are paths relative to the collection root (e.g. `data/minutes/meeting-001-minutes.md`).[file:103]

5. **Roles**

   For each role in `participants.roles`:

   - `roles/<role>.md`, else
   - `roles/judges/<role>.md`, else
   - `roles/specialists/<role>.md`.[file:103]

   Missing role files are reported as warnings but do not abort bundling.

6. **Skills**

   For each skill in `skills`:

   - `skills/<skill>.md`.[file:103]

   Missing skill files are reported as warnings but do not abort bundling.

7. **Templates (optional)**

   If `include.templates` is `true`:

   - all `templates/*.md` files in sorted order.[file:103]

8. **Factory/meta material (optional)**

   If `include.factories` is:

   - `false`: nothing.
   - `true`: all `.md` files found under:
     - `factories/`,
     - `factory/`, or
     - `meta/` (if they exist).[file:103]
   - list: treat each entry as a file or directory path relative to the collection root:
     - files: included directly,
     - directories: include all `.md` files under that directory.[file:103]

9. **Roadmap (optional)**

   If `include.roadmap` is `true`:

   - `ROADMAP.md` in the collection root, or
   - `docs/ROADMAP.md` as fallback.[file:103]

10. **Session prompt**

    - `events/<event>/session-prompt.md`, else
    - `templates/meeting-session-prompt.md`.[file:103]

All paths are de-duplicated by resolved path while preserving first occurrence order.[file:103]

## Output

By default, output for a collection `X` goes to:

```text
prompts/X/generated/session.txt
```

Examples:

```bash
./bundle.py -p panel-of-judges
# → prompts/panel-of-judges/generated/session.txt

./bundle.py -p panel-of-judges -c prompts/panel-of-judges/bundle.advisory-meeting-with-research.yaml
# → same default output, different content
```

To write to a different path, use `-o`:

```bash
./bundle.py -p panel-of-judges -o /tmp/my-session.txt
```

## Flat collections

Some collections may be “flat” — no `events/` or `roles/` subdirectories — and instead supply a single primary prompt file.[file:103]

A collection is considered flat when both `events/` and `roles/` are missing.[file:103]

For flat collections, the bundler:

1. Looks for:
   - `<collection>/<collection>.md`,
   - `<collection>/main.md`,
   - else the first `*.md` file in the collection directory.[file:103]
2. Copies that file to the output path.
3. Still supports `--dry-run` to show which file would be copied.[file:103]

Example:

```bash
./bundle.py -p some-flat-collection --dry-run
```

## Dry run

Use `--dry-run` to inspect which files would be bundled without writing output.[file:103]

```bash
./bundle.py -p panel-of-judges --dry-run
./bundle.py -p panel-of-judges -c bundle.advisory-meeting-with-research.yaml --dry-run
```

Output example:

```text
Dry run — panel-of-judges / advisory-meeting

  prompts/panel-of-judges/context/charter.md
  prompts/panel-of-judges/events/advisory-meeting/event.md
  prompts/panel-of-judges/events/advisory-meeting/preferences.md
  prompts/panel-of-judges/handoff-context.md
  prompts/panel-of-judges/roles/chair.md
  prompts/panel-of-judges/roles/facilitator.md
  prompts/panel-of-judges/roles/note-taker.md
  ...
  prompts/panel-of-judges/events/advisory-meeting/session-prompt.md

Output: prompts/panel-of-judges/generated/session.txt
```

## Validation checklist

When adding or editing configs, it’s useful to run a small verification set:

1. `./bundle.py --list`
2. `./bundle.py -p <collection> --dry-run`
3. One or more variant configs with `--dry-run`
4. At least one real bundle write (without `--dry-run`) to ensure output concatenation works

For panel-of-judges, a typical sequence:

```bash
./bundle.py --list

./bundle.py -p panel-of-judges --dry-run
./bundle.py -p panel-of-judges -c prompts/panel-of-judges/bundle.advisory-meeting-with-research.yaml --dry-run

./bundle.py -p panel-of-judges
```

If you introduce a new defaults file or a new include option, repeat the same checks to ensure schema and file resolution behave as expected.[file:103]
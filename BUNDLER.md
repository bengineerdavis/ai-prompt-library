# Bundler

The bundler assembles a paste-ready session prompt from reusable source files.

It concatenates the charter, event definition, event preferences, role files, and the
session prompt template into a single output file you can paste into a chat or CLI tool.

## Quick start

For an advisory meeting with default roles:

```bash
./bundle.sh
```

Output is written to `generated/session.txt`. Copy and paste that file into your chat.

### Example workflow

```bash
# default advisory meeting — no arguments needed
./bundle.sh

# preview what would be included without writing
./bundle.sh --dry-run

# add deep researcher for a research-heavy session
./bundle.sh -e advisory-meeting \
  -r chair facilitator note-taker \
     pragmatist minimalist systems-thinker \
     deep-researcher

# use a named config variant
./bundle.sh -c bundle.advisory-meeting-with-research.yaml
```

## Config files

A config file defines the event type and the roles to include.

```yaml
# bundle.advisory-meeting.yaml
event: advisory-meeting

roles:
  - chair
  - facilitator
  - note-taker
  - pragmatist
  - minimalist
  - systems-thinker
```

Run with a specific config:

```bash
./bundle.sh -c bundle.advisory-meeting.yaml
```

The default config (used when you run `./bundle.sh` with no arguments) is
`bundle.advisory-meeting.yaml` in the collection root.

## Adding specialists

To add specialists to an advisory meeting, either edit the config file or pass roles directly:

```bash
./bundle.sh -e advisory-meeting \
  -r chair facilitator note-taker \
     pragmatist minimalist systems-thinker \
     deep-researcher
```

Or create a config file for the variant:

```yaml
# bundle.advisory-meeting-with-research.yaml
event: advisory-meeting

roles:
  - chair
  - facilitator
  - note-taker
  - pragmatist
  - minimalist
  - systems-thinker
  - deep-researcher
```

## Using a different event type

```bash
./bundle.sh -c bundle.brainstorming.yaml
```

or directly:

```bash
./bundle.sh -e brainstorming -r chair facilitator pragmatist minimalist systems-thinker
```

## Flags

| Flag                  | Short | Description                                        |
| --------------------- | ----- | -------------------------------------------------- |
| `--config <file>`     | `-c`  | Use a named config file                            |
| `--event <name>`      | `-e`  | Set the event type directly                        |
| `--roles <r1 r2 ...>` | `-r`  | Set roles directly                                 |
| `--output <file>`     | `-o`  | Write to a named output file                       |
| `--dry-run`           |       | Print files that would be included without writing |
| `--help`              | `-h`  | Show usage                                         |

## What gets bundled

For a given event and role list, the bundler includes these files in order:

1. `prompts/context/charter.md` — shared collection principles
1. `prompts/events/<event>/event.md` — event-specific rules, flow, and authority
1. `prompts/events/<event>/preferences.md` — event-specific preferences (if present)
1. Each role file, searched in this order:
   - `prompts/roles/<role>.md`
   - `prompts/roles/judges/<role>.md`
   - `prompts/roles/specialists/<role>.md`
1. `prompts/events/<event>/session-prompt.md` — the session bootstrap prompt (if present)

Missing optional files are skipped with a warning. Missing role files print a warning but
do not stop the bundler.

## Output

All output goes to `generated/session.txt` by default. The `generated/` directory is
safe to overwrite — it holds rebuilt artifacts, not authored source.

To write to a different path:

```bash
./bundle.sh -o /tmp/my-session.txt
```

## Preview without writing

```bash
./bundle.sh --dry-run
./bundle.sh -c bundle.advisory-meeting.yaml --dry-run
```

## Naming your config files

Suggested convention:

```
bundle.<event-type>.yaml                    # default for that event
bundle.<event-type>-<variant>.yaml          # variant with extra roles
```

Examples:

```
bundle.advisory-meeting.yaml
bundle.advisory-meeting-with-research.yaml
bundle.brainstorming.yaml
bundle.evaluation.yaml
```

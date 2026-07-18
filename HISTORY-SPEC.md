# Panel of Judges history spec

Compact single-file spec for the `panel-of-judges` history object.

It defines the history-vs-library boundary, the canonical history layout, the required artifacts, and the manual process that later automation should follow.

## Quick spec

- The **library object** and the **history object** are separate.
- The history object stores session records, not reusable prompt source.
- Canonical history path:

```text
history/<library-key>/<subcollection>/<event-type>/<thread-key>-<session-key>/
```

- Required files in every session folder:
  - `minutes.md`
  - `handoff.md`
  - `session.md`
  - `meta.json`
- `minutes.md` combines minutes and notes.
- `handoff.md` is the continuity artifact.
- `session.md` stores the exact bundled prompt used.
- Reusable event files, bundles, roles, skills, and templates stay in the library object.
- Manual creation comes first so it can shape later automation.

## Boundary

| Stays in the library object | Goes in the history object |
|---|---|
| `events/<event-type>/event.md` | `minutes.md` |
| `events/<event-type>/preferences.md` | `handoff.md` |
| `events/<event-type>/session-prompt.md` | `session.md` |
| `events/<event-type>/bundles/bundle.yaml` | `meta.json` |
| `events/<event-type>/bundles/bundle.<variant>.yaml` | session folder metadata and records |
| `context/*.md` | |
| `roles/**/*.md` | |
| `skills/*.md` | |
| `templates/*.md` | |
| `handoff-context.md` | |
| `ROADMAP.md` | |

## Layout

### Canonical history namespace

```text
history/<library-key>/<subcollection>/<event-type>/<thread-key>-<session-key>/
```

Active example:

```text
history/ai-prompt-library/panel-of-judges/advisory-meeting/main-2026-07-16-001/
```

### Path parts

| Part | Meaning | Example |
|---|---|---|
| `library-key` | Source library namespace | `ai-prompt-library` |
| `subcollection` | Prompt project or collection | `panel-of-judges` |
| `event-type` | Reusable event type used in the session | `advisory-meeting` |
| `thread-key` | Continuity line for related sessions | `main`, `research-branch` |
| `session-key` | Sortable unique key for one run | `2026-07-16-001` |

Recommended session key format:

```text
YYYY-MM-DD-NNN
```

## Required artifacts

| File | Required | Purpose |
|---|---|---|
| `minutes.md` | Yes | Combined session record with notes, conclusions, decisions, takeaways, and observations |
| `handoff.md` | Yes | Continuity summary for the next session or next owner |
| `session.md` | Yes | Exact final bundled prompt used for the run |
| `meta.json` | Yes | Machine-readable metadata snapshot |

### Controlled artifact rule

Use these filenames exactly.

Do not substitute:

- `notes.md`
- `prompt.md`
- `summary.md`
- `followup.md`

## Bundling rule

The library object holds reusable prompt ingredients.

The bundler assembles those ingredients into a final prompt.

That exact final prompt is then saved in the history object as `session.md`.

## Manual workflow

### New session

1. Choose the `library-key`, `subcollection`, `event-type`, `thread-key`, and `session-key`.
2. Determine the `bundle-key` and exact bundle path used.
3. Create the session directory:

```text
history/<library-key>/<subcollection>/<event-type>/<thread-key>-<session-key>/
```

4. Add these required files:
   - `minutes.md`
   - `handoff.md`
   - `session.md`
   - `meta.json`
5. Paste the exact bundled final prompt into `session.md`.
6. Write the combined session record into `minutes.md`.
7. Write the continuation summary into `handoff.md`.
8. Fill in `meta.json`.

### Continue a thread

1. Reuse the same `thread-key`.
2. Create a new `session-key`.
3. Create a new session directory.
4. Use the latest `handoff.md` and relevant prior `minutes.md` as continuation context.
5. Save the new session artifacts in the new directory.

### Branch a thread

1. Create a new `thread-key`.
2. Record the source thread in `meta.json`.
3. Create the new session directory under the new thread key.
4. Carry over the relevant handoff and prior session context as needed.

## Metadata

Recommended minimum fields for `meta.json`:

| Field | Purpose |
|---|---|
| `library_key` | Source library namespace |
| `subcollection` | Prompt project or collection |
| `event_type` | Event used for the session |
| `thread_key` | Continuity line |
| `session_key` | Unique sortable session id |
| `bundle_key` | Selected bundle variant or `default` |
| `bundle_path` | Relative path to the source bundle file |
| `created_at` | Timestamp for the session record |
| `artifact_types` | Controlled list of artifacts present |
| `parent_thread_key` | Optional source thread when branching |
| `continued_from_session_key` | Optional prior session reference |

## Starter structures

### Event-type starter

```text
events/<event-type>/
  event.md
  preferences.md
  session-prompt.md
  bundles/
    bundle.yaml
```

### Prompt-project starter

```text
<prompt-project>/
  README.md
  STRUCTURE.md
  HISTORY.md
  context/
    charter.md
  events/
    <event-type>/
      event.md
      preferences.md
      session-prompt.md
      bundles/
        bundle.yaml
  roles/
  skills/
  templates/
```

## AI automation target

A future AI tool should be able to read this spec and create:

1. a new prompt project,
2. a new event type,
3. starter bundle files,
4. the required history artifacts,
5. and a clean boundary between history and reusable prompt source.

## Appendix

### Minimal history example

```text
history/ai-prompt-library/panel-of-judges/advisory-meeting/main-2026-07-16-001/
  minutes.md
  handoff.md
  session.md
  meta.json
```

### Minimal `minutes.md`

```md
# Session minutes

## Session

## Task

## Discussion

## Decisions

## Open questions

## Takeaways

## User notes
```

### Minimal `handoff.md`

```md
# Session handoff

## Session

## Current state

## Important decisions to preserve

## Open issues

## Recommended next step

## Recommended continuation context
```

### Minimal `session.md`

```md
Paste the exact bundled session prompt here with no edits after the fact.
```

### Minimal `meta.json`

```json
{
  "library_key": "ai-prompt-library",
  "subcollection": "panel-of-judges",
  "event_type": "advisory-meeting",
  "thread_key": "main",
  "session_key": "2026-07-16-001",
  "bundle_key": "default",
  "bundle_path": "events/advisory-meeting/bundles/bundle.yaml",
  "created_at": "2026-07-16T00:00:00Z",
  "artifact_types": ["minutes", "handoff", "session", "meta"],
  "parent_thread_key": null,
  "continued_from_session_key": null
}
```
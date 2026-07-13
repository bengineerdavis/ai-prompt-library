# Panel of Judges Roadmap

<!-- REVIEW: Seed roadmap file for open design questions that are important but not yet ready to be locked into the collection. Kept in Markdown per principal preference. -->

## Current open questions

### Handoff lifecycle

- Should factory handoff candidates receive a persistent status model such as `open`, `acted-on`, `superseded`, or `closed`?
- After the factory acts, should the handoff ID be referenced in:
  - changelog entries,
  - role-review notes,
  - event-review notes,
  - or a future registry of structural changes?
- Should acted-on handoffs remain only in historical minutes, or also be summarized in a dedicated backlog file?

### Changelog integration

- Should accepted factory handoffs automatically propose changelog notes?
- Should changelog entries include source handoff IDs for traceability?
- Should the Panel Builder generate a small "change provenance" block connecting minutes → handoff ID → factory session → changed files?

### Factory session inputs

- What is the ideal minimum context bundle for a later factory session?
- Should a dedicated `handoff-context.md` become the standard bridge from live meeting to factory/meta-session?
- Should that bridge include only accepted handoffs, or also deferred and declined ones for institutional memory?

### Artifact preferences

- Markdown is the default output format across the collection.
- If another format would make more sense for a specific task, ask the principal first rather than switching formats implicitly.

### Batch update discipline

- Keep changes in small, related batches.
- Prefer regenerating full files over patch fragments.
- Include inline Markdown comments for review when generating candidate revisions.

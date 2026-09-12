# Changelog — advisory-meeting event

Event-specific changes for `panel-of-judges/events/advisory-meeting`. Format follows
Keep a Changelog. Collection-wide roles, skills, and templates are noted here when
they were added to serve this event.

## [Unreleased] - 2026-09-07

### Added

- `bundle.advisory-meeting-service-procurement.yaml`: variant for local service
  purchases. Adds the Service Provider Due-Diligence Advisor to the default panel
  and pulls `interaction-questioning` and `local-service-procurement` into the
  session via `include.context` (they live outside this collection).
- `roles/specialists/service-provider-due-diligence-advisor.md` (collection scope,
  v0.3.0): provider-evaluation specialist that proposes unknowns, gates, call
  sheets, and quote fields while Questioning controls user-facing questions.

### Fixed

- `bundle.advisory-meeting-with-research.yaml` and
  `bundle.advisory-meeting-factory-review.yaml` now use `event.name: advisory-meeting`. Both previously named non-existent event directories and
  failed with a hard bundler error; bundle variants configure the shared event
  rather than defining new event types.

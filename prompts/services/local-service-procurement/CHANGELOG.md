# Changelog

All notable changes to the Local Service Procurement kit are documented here.

The format is based on Keep a Changelog, and this project adheres to Semantic Versioning.

## [0.3.0] - 2026-09-07

### Added

- Explicit composition with Interaction Questioning v2.3.2: Questioning owns discovery and the single user-facing question; this skill owns the procurement workflow after good-enough discovery.
- Understanding-confirmation handoff: the workflow starts from Questioning's plain-English confirmation instead of running its own intake.
- Evidence labels for the candidate ledger: verified, corroborated, vendor-stated, plausible, unsupported.
- Kit README with artifact map, role boundaries, natural-language quick start, session flow, and maintenance rules.
- Discovery & Procurement Brief template (`templates/brief.md`) with a three-line natural-language user start.
- Service Provider Due-Diligence Advisor specialist role in `panel-of-judges`, plus a `bundle.advisory-meeting-service-procurement.yaml` panel variant.

### Changed

- Removed duplicate discovery logic; discovery discipline now lives entirely in Interaction Questioning.
- Quote comparison now normalizes to complete all-in value rather than headline pricing, with comparison-sheet rows mapped to vendor call questions.

## [0.2.0] - 2026-09-07

### Added

- Adaptive discovery and unknown-unknown mapping (superseded by the v0.3.0 delegation to Interaction Questioning).

## [0.1.0] - 2026-09-07

### Added

- Initial extraction from a local service-purchase workflow.

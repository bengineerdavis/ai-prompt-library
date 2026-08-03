# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog, and this project adheres to Semantic Versioning.

## [2.2.3] - 2026-08-02

### Changed
- Tightened the wording of the questioning skill to improve plain-language readability and reduce jargon.
- Shortened several instructions while keeping the same behavior and mode structure.

### Fixed
- Replaced denser phrases with simpler wording to make the skill easier to scan and reuse.

## [2.2.2] - 2026-08-02

### Changed
- Narrowed verbose confidence display so it appears only at goal-inference, confirmation, or branch-selection decisions that could materially change the path.
- Kept normal mode silent by default and reserved routine reasoning detail for deep-trace mode.

### Fixed
- Reduced unnecessary meta-commentary in verbose output.

## [2.2.1] - 2026-08-02

### Added
- Added adaptive-auto as the default routing policy for the questioning skill.
- Added a session-goal lens so the skill can help define a clearly agreed-upon goal in exploratory sessions.
- Added explicit guidance for switching between direct next-question selection and internal adaptive-tree reasoning.
- Added a goal-deduction confirmation pattern with plain-language templates, confidence guidance, and correction triggers.
- Added confidence-display rules for verbose and deep-trace output.
- Added questioning-rubric criteria for session-goal clarity, goal-confirmation quality, and confidence explanation quality.

### Changed
- Updated the questioning skill to treat exploratory sessions as valid and goal-finding as part of good questioning.
- Reframed adaptive questioning as guided clarification that helps the user move from an initial answer to the answer they actually need.
- Updated the README to show the latest versions at a glance.

### Fixed
- Improved default behavior so the skill can return from tree reasoning to simple next-question generation once the best path is clear.

## [1.0.0] - 2026-08-02

### Added
- Added a generic `skill-audit` skill with explicit semantic versioning guidance.
- Added `references/RUBRIC.md` as the reusable baseline audit rubric for any skill.
- Added `references/QUESTIONING-RUBRIC.md` to score questioning skills on output quality, convergence, and efficiency.
- Added readability checks for jargon, sentence length, passive voice, and simplified rewrites.

### Changed
- Reframed the audit skill as a generic audit layer that reads a shared rubric and optional skill-specific rubric files.
- Clarified that quality and convergence must be scored separately before efficiency is judged.

### Fixed
- Improved version visibility so the latest audit artifact can be identified at a glance.
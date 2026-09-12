# RUBRIC

Version: 1.0.0
Applies to: any reusable AI skill or prompt package

## Purpose

This rubric defines the baseline standards the audit skill should apply to every skill.
It is generic on purpose.
Use a skill-specific rubric for domain checks that go beyond this baseline.

## Scoring model

Score each category on a 1 to 5 scale.

- 1 = poor
- 2 = weak
- 3 = acceptable
- 4 = strong
- 5 = excellent

## Categories

### 1. Trigger clarity

Check whether the skill clearly explains what it does and when to use it.

Questions:

- Is the description specific?
- Are use cases obvious?
- Are non-use cases defined?

### 2. Instruction clarity

Check whether the body is easy to follow.

Questions:

- Are steps ordered clearly?
- Are defaults and exceptions visible?
- Is the skill readable without specialist context?

### 3. Plain language

Check readability using plain-language principles.

Questions:

- Does the text avoid jargon or define it on first use?
- Are sentences short enough to scan?
- Is active voice preferred over passive voice?
- Does the structure help the reader act quickly?

Required checks:

- flag jargon that obscures intent
- flag excessive sentence length
- flag passive voice
- suggest simpler rewrites that keep technical accuracy

### 4. Behavioral effectiveness

Check whether the skill creates useful, reliable behavior.

Questions:

- Does it help the model act better, not just sound better?
- Are stop conditions clear?
- Are tradeoffs explicit?
- Can success be evaluated?

### 5. State and complexity control

Check whether internal logic is bounded.

Questions:

- Is state minimal and necessary?
- Are internal branches controlled?
- Does the design avoid unnecessary complexity?

### 6. Portability and composition

Check whether the skill can work across tools and with other skills.

Questions:

- Can it be reused in chat, copilot, or skill runtimes?
- Does it explain how it composes with other skills?
- Is file structure aligned with skill conventions?

### 7. Release hygiene

Check whether the skill is easy to maintain.

Questions:

- Is semver used clearly?
- Is the next version recommendation explicit?
- Is there a changelog-ready summary?

## Minimum output requirements

The audit output must include:

- scores by category
- plain-language findings
- rewritten examples
- semver recommendation
- changelog draft
- unresolved risks

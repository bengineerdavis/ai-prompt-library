# QUESTIONING SKILL RUBRIC

Version: 1.1.0
Applies to: interaction-questioning and related clarification skills

## Success model

Judge three dimensions:

1. Final output quality
- Did the questioning help the final answer become more accurate, more useful, or better fit to the user's need?

2. Convergence to an actionable answer
- Did the skill reach a point where the next step or final answer was clear enough to act on?

3. Efficiency
- Judge this only after scoring quality and convergence separately.
- Efficiency means the skill reached a strong answer with reasonable questioning cost.
- Fewer questions is not always better if quality drops.

## Session-goal clarity

Also judge whether the skill helped the user define a clearly agreed-upon goal for the session.
This matters most in exploratory sessions where the first request may not match the answer the user actually needs.

Questions:
- Did the skill identify the real session goal, not just the first wording of the request?
- Did the questions help the user resolve internal uncertainty or self-disagreement?
- Did the skill move from exploratory discussion to a clear shared goal in plain language?
- Did the skill infer the likely goal before forcing the user to define it?
- Did it confirm the goal at the right time when confidence was not strong enough to proceed silently?
- Did it use a small candidate set when several plausible goals remained?

## Questions to ask

### Quality
- Did the skill identify the most important unknowns early?
- Did the questions change the quality of the final result in a meaningful way?
- Did it avoid irrelevant or low-value questions?

### Convergence
- Did the questioning sequence move toward a usable answer?
- Did the skill stop once the answer was actionable?
- Did it avoid over-questioning?

### Efficiency
- Was the number of questions justified by the gain in quality?
- Did the skill switch between direct questioning and deeper branching at the right time?
- Did internal complexity stay hidden unless explicitly requested?

### Confidence and explanation
- In normal mode, did the skill keep confidence and reasoning mostly hidden?
- In verbose mode, did it show confidence only at goal-inference, confirmation, or branch-selection decisions that could materially change the path?
- When verbose confidence was shown, did it use high, medium, or low with a short plain-language explanation?
- In deep-trace mode, did it expose enough reasoning detail to debug the questioning path, confidence shifts, and recovery steps?

### Session goal
- Did the skill help define the session goal early enough?
- Did it notice when the goal changed during the session?
- Did it avoid locking too early onto the user's first phrasing?
- Did it calibrate confidence well enough to choose between silent inference, yes or no confirmation, and candidate-goal confirmation?
- When the user corrected the inferred goal, did the skill recover without restarting from zero?

## Specific failure modes

Flag when:
- the skill asks obvious questions too late
- the skill opens too many branches without pruning
- the skill keeps asking after the answer is already actionable
- the skill uses internal terms that make live operation harder to understand
- the skill defaults too early and harms output quality
- the skill explores many branches but fails to improve the result
- the skill never helps the user name the real session goal
- the skill confirms too early when the goal is already obvious
- the skill proceeds silently when confidence is weak and drift is likely
- the skill presents too many candidate goals or poorly separated options
- the skill throws away useful context after a correction

## Readability overlay

Also apply the generic plain-language checks to the questioning skill itself.
Pay special attention to:
- branch terminology
- state labels
- mode names
- stop-condition language
- session-goal language
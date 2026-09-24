# Writing principles

Help the reader understand the situation and take the next useful action. These
principles apply to drafts, questions, and author notes. They adapt public guidance;
they are not a substitute for an organization's voice policy.

## Establish meaning before editing

Separate what the customer reports, what Support observed, the working hypothesis,
and what is unknown. Then improve the language without changing those distinctions.

"The customer reports all uploads failing" does not establish "All uploads fail."
It also does not mean "Some uploads may fail." Preserve the report's scope and
attribute it instead of adopting it or quietly weakening it.

Keep exact errors, commands, versions, conditions, quotations, and dates when
relevant and permitted for the audience. If an excerpt contains sensitive content,
omit or visibly redact it and describe the omission. A style rule never requires
disclosing a secret.

## Put the reader's need first

- Lead with the problem, status, or requested action that matters in this message.
- Use a descriptive title for a durable ticket. Use headings only when they make
  a longer message easier to scan.
- Prefer direct verbs and common words. "Checked" is clearer than "performed an
  investigation of" when it describes the same action.
- Name the actor when known. Passive voice is appropriate when the actor is unknown
  or irrelevant; do not invent responsibility to avoid it.
- Use "you" for reader instructions. Use "we" or "I" only for supported actions
  from the sender's role. "We reproduced it" requires evidence of that reproduction.
  A future promise also requires the sender's current confirmation that the exact
  action and any timing can be guaranteed; a past promise alone is not enough.
- Put conditions before instructions. Explain unfamiliar diagnostics and how to
  collect them when known.
- Keep chronology accurate. Past investigations remain past; future plans remain
  plans. Present tense is not a rule for rewriting history.
- Use one name for one concept. Define unfamiliar terms where needed; retain
  technical terms the intended reader uses.
- Split dense sentences where meaning survives. Avoid both tangled paragraphs and
  fragments that force the reader to decode abbreviations and arrows.

## Be considerate without performing empathy

Acknowledge the stated consequence: "This prevents you from exporting the report."
Do not invent a feeling: "I know exactly how frustrating this is."

Ask a focused question rather than blame the customer for missing evidence. A
useful request says what is needed and why: "Which command starts the service in
CI? The local and CI results differ, and the startup options may help explain why."

Use apologies, thanks, and reassurance when they are sincere and contextually
useful. Repeating them does not substitute for a clear answer. Keep the sender's
existing warmth or humor where appropriate; do not manufacture a persona.

## Adapt the unslop references selectively

Keep their useful editing advice: remove filler, vague authority, synonym cycling,
empty importance claims, forced drama, and needless compression. Prefer concrete
facts already supported by the record. If a fact is missing, name the gap rather
than invent a number or mechanism to make the prose sound specific.

Do not adopt blanket punctuation bans, banned-word lists, forced sentence variety,
or AI-detection scores. Necessary uncertainty is not filler. A useful contrast is
not defective because a stock contrast formula exists. Formatting should serve
the reader, not signal an author type.

Preserve truthful, relevant or required AI-use disclosures. Answer questions about
authorship honestly. There is no requirement to add an unsolicited disclosure to
every message, and no goal of making AI-assisted writing pass as human-only work.

## Manage expectations through facts and next steps

Know who receives this message and whose behalf you write on. A customer needs to
understand their issue's status and the relevant next step, not take over an
internal investigation or read the team's complete planning discussion.

Distinguish a completed action from a requested action and a guaranteed future
action. "We've asked Engineering to review the failed request" reports a known
step. "Engineering will have an answer tomorrow" promises another team's outcome.
Removing "tomorrow" does not make the second claim supported.

Keep legitimate options open by saying what is established now. Do not invent a
date, promise immediate follow-up after an uncertain event, or end every reply
with "we'll keep you updated." This also avoids using vague reassurance in place
of useful information. Preserve prior commitments in internal notes so the sender
can honor or address them; do not silently cancel them through editing.

## Final editorial check

Read the draft as its recipient. Can you identify the point and next action? Are
claims attributable and uncertainty intact? Is the detail useful for this audience?
Did the edit add an unsupported promise, action, number, or personal experience?
Is any customer-facing promise currently guaranteed by the sender at that scope?
Remove unnecessary prose without deleting material evidence or conditions.

## Public sources

- [Digital.gov plain-language guide](https://digital.gov/guides/plain-language):
  audience, organization, direct language, and comprehension.
- [Plain English](https://github.com/bengineerdavis/ai-prompt-library/tree/main/skills/plain-english):
  terminology, direct prose, and meaning preservation. Its numerical sentence caps
  and present-tense preference are not hard limits in this skill.
- [Interaction Questioning](https://github.com/bengineerdavis/ai-prompt-library/tree/main/skills/interaction-questioning):
  use context and ask the minimum useful question.
- [Cursor Unslop](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md):
  clarity and over-compression checks, selectively adapted.
- [Peter Yang's No AI Slop](https://github.com/petergyang/no-ai-slop):
  minimum effective edits and preservation of voice, selectively adapted.

These are optional background links, not dependencies to fetch for every draft.
The rules above remain usable without network access.

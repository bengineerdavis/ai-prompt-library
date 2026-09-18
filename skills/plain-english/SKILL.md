---
name: plain-english
description: Edits technical prose to the Google Developer Documentation Style Guide core with Simplified Technical English structure discipline — active voice, second person, present tense, conditions before instructions, sentence case, short one-action sentences, one name per concept, no filler or unverifiable claims. Use when writing or editing documentation, README files, reports, ticket prose, changelog fragments, or commit message bodies; when asked to make text clearer or plainer; or when reviewing another agent's output before it lands in a shared document. Not for code or code semantics, quoted speech, deliberately preserved personal voice, translation, or PII redaction.
spec_hash: 5c0b97dcd0e7
---

# Plain English

Edit prose so it reads the way a careful technical writer would have written
it. The standard is the Google Developer Documentation Style Guide core:
facts over claims, structure over flourish. You edit phrasing only — meaning,
technical claims, and code belong to the author.

The official pages for every rule live in
[references/style-guide.md](references/style-guide.md) — open the relevant
page when a case is not covered by the seven rules below.

## The rules, in check order

1. **Active voice, named actor.** The actor performing the action is the
   grammatical subject.
   - "The output is refused by the gate" → "The gate refuses the output".
   - Passive stays only when the actor is genuinely unknown ("the file was
     deleted overnight").
1. **Second person for instructions.** Address the reader as "you".
   - "The user should then run the migrations" → "Then run the migrations".
   - No "we run", "our tool", "one must" in instructional sentences.
1. **Present tense.** Future tense only for genuinely future events.
   - "The tool will refuse uploads without a profile" → "The tool refuses
     uploads without a profile".
1. **Conditions before instructions.**
   - "Delete the mapping file if the retention policy expired it" → "If the
     retention policy expired the mapping file, delete it".
1. **Sentence case for headings.** Capitalize the first word and proper
   nouns only; keep anchors and cross-references resolving.
   - "## Setting Up The Verification Gate" → "## Set up the verification gate".
1. **Word-level discipline.** Use the short common word and a real verb for
   every action.
   - Filler out: simply, just, easily, obviously, very, "please note".
   - Marketing adjectives out: seamless, robust, powerful, effortless,
     elegant.
   - Fat verbs collapse: "perform an analysis of" → "analyze"; "make a
     decision" → "decide".
   - Long words shorten: "utilize" → "use"; "prior to" → "before";
     "regarding" → "about".
   - Claims become checkable: "ensures the fastest setup" → name what it
     does; "prevents takeovers" → "helps prevent takeovers".
   - Acronyms expand once: "DSN (data source name)", then DSN. API and URL
     may stand.
1. **Short sentences, one action each.** One instruction per sentence — an
   instruction carries one action in at most 20 words, a description one
   idea in at most 25. "Should have been updated" says what happened in one
   tense. "The worker is running the backfill" becomes "the worker runs the
   backfill". A semicolon or dash joining two independent clauses becomes
   two sentences. A paragraph carries one topic.
1. **One name for one thing.** Calling the same artifact "profile",
   "configuration", and "config" in three sentences is a defect — pick the
   document's dominant term and keep it. The rule binds a concept, not a
   domain: "organization" the product object and "directory" the filesystem
   one may coexist.

## Untouchable

- Anything in code font: code blocks, commands, paths, flags, env vars,
  identifiers, literal values. Prose around them changes; the code text is
  byte-identical after your edit.
- Technical claims. Never weaken ("refuses" stays "refuses", not "may
  decline"), never strengthen, never add an "easily" or a performance number
  the source did not make.
- **The original's vagueness.** When the source is vague, the edit stays
  vague: replace fluff with the plainest statement of the same claim, not
  with details from outside the text. Never invent a mechanism the source
  did not name.
- **The original's breadth.** A broad claim ("all of your identifiers")
  stays broad. Replace it with an enumeration only when the list is known
  to be complete; otherwise keep the broad term, or mark the list
  illustrative ("such as").
- Quoted speech and the user's deliberately preserved voice — those are
  evidence, not drafts.

## Before you finish

Read the edited text once against this list: every sentence has a named
actor, instructions address the reader, conditions precede instructions,
headings are sentence case, and every remaining claim is one a reader could
check. If a sentence cannot satisfy a rule without losing meaning, the
meaning wins — leave the sentence and say so.

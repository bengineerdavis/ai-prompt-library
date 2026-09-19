# Plain English

## Intent

This skill makes the agent write and edit technical prose to the core of the
Google Developer Documentation Style Guide (developers.google.com/style, CC BY 4.0):
active voice, second person, present tense, conditions before instructions,
sentence case, and no filler or unverifiable claims — with three
structure-and-vocabulary disciplines adopted from Simplified Technical
English practice (ASD-STE100, studied in getsentry/ste-writing-research:
ideas only; that repository carries no license and nothing was copied). It
exists so that every document, report, commit message, and changelog an agent
touches in this workspace reads the way a careful technical writer would have
written it — one register, enforced mechanically rather than by taste.

The skill edits phrasing only. Meaning, technical claims, and code are the
author's: the agent makes the sentence clearer, never weaker, and never
touches anything inside code font.

## Triggers

- **SHOULD** — writing or editing any documentation, README, report, ticket
  prose, changelog fragment, or commit message body.
- **SHOULD** — the user asks to make text "clearer", "plainer", or to fix
  "AI-sounding" prose, and the request is about clarity rather than voice
  or personality (that is the no-ai-slop skill's job).
- **SHOULD** — reviewing another agent's output before it lands in a shared
  document.
- **SHOULD NOT** — editing code, code semantics, or code comments beyond
  their prose readability.
- **SHOULD NOT** — the text is quoted speech, a journal entry recording what
  a person actually said, or the user's own draft voice being preserved
  deliberately.
- **SHOULD NOT** — translation, summarization for a model prompt, or PII
  redaction; those tasks own their own registers.

## Behaviors

### Behavior: Active voice with a named actor

The agent SHALL rewrite passive constructions so the actor performing the
action is the grammatical subject ("the gate refuses the output", not "the
output is refused"). Passive voice stays only when the actor is genuinely
unknown or irrelevant ("the file was deleted overnight").

#### Scenario: Passive sentence in a README

- **WHEN** a README says "The output is quarantined by the verify gate when
  a leftover is found" and the user asks to edit it to plain English
- **THEN** the edited sentence reads "The verify gate quarantines the output
  when it finds a leftover" and both sentences carry the same technical
  claim

### Behavior: Second person for instructions

The agent SHALL address the reader as "you" in instructions and procedures.
Third person ("the user should", "one must") and first-person-plural
("we run", "our tool") do not appear in instructional sentences.

#### Scenario: A procedure written about the reader in the third person

- **WHEN** a setup guide says "The user should then run the migrations" and
  the user asks to edit it to plain English
- **THEN** the edited sentence reads "Then run the migrations" or "You
  should then run the migrations", and no other sentence in the guide
  changed meaning

### Behavior: Present tense

The agent SHALL write documentation in present tense. Future tense appears
only for events genuinely in the future ("the retention job will delete the
map on 2027-08-09"), never as a hedged way to describe current behavior.

#### Scenario: Future tense describing current behavior

- **WHEN** a document says "The tool will refuse uploads without a profile"
  describing today's behavior, and the user asks to edit it to plain English
- **THEN** the edited sentence reads "The tool refuses uploads without a
  profile"

### Behavior: Conditions before instructions

The agent SHALL place conditional clauses before the instruction they
govern ("If the scan finds nothing, keep the file"), not after ("Keep the
file if the scan finds nothing").

#### Scenario: Condition trailing an instruction

- **WHEN** a runbook says "Delete the mapping file if the retention policy
  expired it" and the user asks to edit it to plain English
- **THEN** the edited sentence reads "If the retention policy expired the
  mapping file, delete it" and the destructive instruction still names the
  same object under the same condition

### Behavior: Sentence case for headings

The agent SHALL write document titles and section headings in sentence case
(capitalize the first word and proper nouns only). A heading that names a
task SHALL start with a bare infinitive ("Set up the gate", not "Setting up
the gate"); a heading that names a concept SHALL be a noun phrase that does
not start with an -ing verb. An existing heading keeps its anchor/link
targets intact when the tooling derives them from text.

#### Scenario: Title-case heading in a technical document

- **WHEN** a document has the heading "## Setting Up The Verification Gate"
  and the user asks to edit it to plain English
- **THEN** the heading reads "## Set up the verification gate" and any
  cross-references to the heading still resolve

### Behavior: Word-level discipline

The agent SHALL use the short common word and a real verb for every action:
delete filler (simply, just, easily, obviously, very, "please note");
marketing adjectives (seamless, robust, powerful, effortless, elegant);
fat verb constructions ("perform an analysis of" becomes "analyze", "make a
decision" becomes "decide"); long word choices ("utilize" becomes "use",
"prior to" becomes "before", "regarding" becomes "about").

An ensure/guarantee construction loses the wrapper, never the claim:
"ensures no data is lost" becomes "No data is lost". The verb was the
flourish; the proposition is the author's. The agent SHALL NOT decide
whether a claim is achievable or true — ensurability is a property of the
system, not of the sentence, and the agent has no access to the system.
Where the wrapper holds a superlative and no proposition ("ensures the
fastest possible setup"), the intensifier rule already removes it and no
claim is lost. An unverifiable claim the agent cannot repair by phrasing
alone is flagged for the author, never quietly rewritten.

#### Scenario: Filler, a fat verb, and an unverifiable claim in one paragraph

- **WHEN** a changelog says "Simply utilize the new command to perform an
  initialization of the environment — this ensures the fastest possible
  setup" and the user asks to edit it to plain English
- **THEN** the edited text reads "Run the new command to initialize the
  environment" (or names what the command actually does), with no
  intensifiers and no fat verb — "fastest possible" was a superlative
  rather than a proposition, so no claim was lost

### Behavior: Short sentences, one action each

The agent SHALL keep one instruction per sentence and cap lengths: an
instruction carries one action in at most 20 words; a description carries
one idea in at most 25 words. Stacked auxiliaries collapse to one tense
("should have been updated" becomes "the update did not run" — say what
happened); a simple tense replaces a progressive main verb where it works;
a semicolon or dash joining two independent clauses becomes two sentences;
a paragraph carries one topic.

#### Scenario: A runbook sentence doing three jobs

- **WHEN** a runbook says "Restart the worker; if the queue is still blocked
  after two minutes, then check whether the backfill has been running and
  escalate to the on-call engineer, otherwise wait" and the user asks to
  edit it to plain English
- **THEN** the edited text is a short numbered sequence — one action per
  step, each under 20 words, each still carrying its original condition —
  and no semicolon or dash remains

### Behavior: One name for one thing

The agent SHALL use one term per concept within a document. Calling the same
item "profile" in one sentence, "configuration" in the next, and "config"
in a third is a defect. The rule binds a concept, not a domain: a product's
own term and a software-engineering term may legitimately coexist
("organization" the product object, "directory" the filesystem one).

#### Scenario: Synonym drift across a document

- **WHEN** a guide refers to the same artifact as "profile", "configuration",
  and "config" in three consecutive sentences and the user asks to edit it
  to plain English
- **THEN** all three sentences use one term, chosen from the document's own
  dominant usage, and the object each sentence discusses is unchanged

### Behavior: Expand acronyms on first use

The agent SHALL spell out an acronym at its first use in a document and put
the acronym in parentheses immediately after ("personally identifiable
information (PII)"), then use the short form alone. The spelled-out form
stays lowercase unless it is a proper noun. An acronym the document's own
audience is assumed to know (API, URL) may stand unexpanded.

#### Scenario: An unexpanded acronym used throughout

- **WHEN** a document uses "DSN" eleven times without expansion and the user
  asks to edit it to plain English
- **THEN** the first occurrence reads "data source name (DSN)" and the
  remaining ten read "DSN"

## Constraints

### Constraint: Code and identifiers are untouchable

The agent MUST NOT alter anything inside code font: code blocks, commands,
file paths, flags, environment variables, identifiers, or literal values.
Prose around them changes; the code text is byte-identical after the edit.

### Constraint: Meaning and claims are the author's

The agent MUST NOT weaken, strengthen, or add technical claims while
editing. "Refuses the request" stays "refuses" (not "may decline"); the
agent never introduces "easily", "guarantees", or a performance claim the
source did not make; quoted speech and the user's deliberately preserved
voice stay untouched. When the original is vague, the edit stays vague: the
agent replaces fluff with the plainest statement of the same claim, never
with specifics imported from outside the text. A proposition the source
asserts survives at its original strength even when an ensure/guarantee
wrapper carries it: the agent drops the wrapper and keeps the proposition,
because deleting a claim weakens it and hedging one ("helps prevent", "is
designed to") weakens it too. A broad claim ("all of your
identifiers") stays broad — the agent replaces it with an enumeration only
when the list is known to be complete, and otherwise marks an illustrative
list as such ("such as").

<!-- skillet-version: 1.8.0 -->

# PII Redaction

## Intent

This skill governs how any script that removes personally identifiable
information must be built. It exists because a redaction tool that fails is
indistinguishable from one that works: the output is a plausible-looking file
either way, and nobody re-reads it before sharing. A single language-model call
is not a redaction pipeline — it is one probabilistic step with no verification,
and treating its exit code as proof of redaction is the defect this skill is
written to prevent.

Redaction is therefore three layers, not one: deterministic patterns catch the
classes that are mechanically decidable, a model catches the contextual ones
patterns cannot, and a verification pass proves the result before anything is
written. The verification layer is not optional polish — it is what converts
"the model was asked to redact" into "the output contains no detectable PII."
Any script the agent writes or reviews in this area is expected to have all
three, and to fail closed when the third disagrees with the second.

## Triggers

- **SHOULD** apply when writing, reviewing, or modifying a script whose purpose
  is to remove, mask, anonymise, or scrub PII from text — for example
  `bin/pii-redactor`, or any new `*-redact*`/`*-scrub*`/`*-anonymize*` tool.
- **SHOULD** apply when a script sends user content to a model and writes the
  result somewhere that will be shared, attached to a ticket, or committed.
- **SHOULD** apply when reviewing a redaction script's tests, since a suite whose
  model is mocked as a pass-through will pass while the tool leaks.
- **SHOULD** apply when a redaction script must handle input larger than memory
  or larger than the model's context window, since the obvious fix — splitting
  the input — creates a new way to leak.
- **SHOULD NOT** apply to scripts that merely *read* content containing PII
  without emitting a sanitised copy, such as a log viewer or a search tool.
- **SHOULD NOT** apply to secret scanning that only detects and reports (for
  example a pre-commit credential check), where no redacted artefact is produced
  and blocking is the whole output.
- **SHOULD NOT** apply to encryption, access control, or data retention work,
  which protect the original rather than emit a safe derivative.

## Behaviors

### Behavior: Name what the output is, and claim no more

The agent SHALL state which of two modes a run used and label the output
accordingly, because the two produce artifacts with different legal status.

- **Redact** replaces each finding with a placeholder. Nothing linkable to the
  original value survives, and two different people both become `[NAME]`.
- **Pseudonymise** replaces each finding with a stable, typed substitute: the
  same value maps to the same substitute for the whole run, and two different
  people stay distinguishable.

The agent MUST NOT label a pseudonymised artifact "anonymised", and MUST NOT
claim either mode produces anonymous data. Under the EU regime these are
different standards: pseudonymised data remains personal data (EDPB Guidelines
01/2025 on Pseudonymisation), while anonymous data falls outside the GDPR and
must satisfy no record isolation, no linkage and no inference (EDPB Guidelines
02/2026 on Anonymisation). A support capture essentially never clears the second
test, because the history that makes it useful is also what identifies it.

The agent SHALL state what verification proved — that no detected value survived
(redact) or that values were consistently substituted (pseudonymise) — and MUST
NOT present either as proof that the text cannot be re-identified.

#### Scenario: A pseudonymised run is described

- **GIVEN** a run whose substitutions were stable and typed, so the same person
  keeps one identity throughout
- **WHEN** the tool reports the result
- **THEN** it calls the output pseudonymised, not anonymised, and does not claim
  the text is no longer personal data

#### Scenario: Two people in one document stay distinct

- **GIVEN** input naming two different people
- **WHEN** the run pseudonymises
- **THEN** each person receives a different substitute, and a later mention of
  either person receives the same substitute as its first mention

### Behavior: Deterministic pass before the model

The agent SHALL apply pattern-based redaction for mechanically decidable PII
classes before any model call, and SHALL NOT delegate those classes to the
model. Mechanically decidable means the class can be recognised by pattern or
checksum alone: email addresses, phone numbers, IPv4/IPv6 addresses, MAC
addresses, national identifiers, payment card numbers validated by Luhn, cloud
access keys, bearer tokens and JWTs, and URLs carrying credentials or tokens.

#### Scenario: Email and card number in the input

- **GIVEN** an input file containing `jane.smith@example.com` and the card
  number `4111 1111 1111 1111`
- **WHEN** the redaction script processes it
- **THEN** both values are replaced by placeholders by the deterministic layer,
  before the model is invoked, and the model never receives either value

### Behavior: Model pass for contextual PII

The agent SHALL send the deterministically-redacted text to a model to catch
classes that patterns cannot decide — personal and organisation names, street
addresses, job titles tied to an individual, and free-text identifiers — and
SHALL instruct it to preserve structure and existing placeholders.

#### Scenario: A name with no distinguishing pattern

- **GIVEN** input reading `Hi, my name is Jane Smith and I live at 123 Maple Street`
- **WHEN** the redaction script processes it
- **THEN** the deterministic layer leaves the name and street untouched, and the
  model pass replaces them with placeholders while the sentence remains readable

### Behavior: Leak verification over the output

The agent SHALL re-run the deterministic detectors over the candidate output
after the model pass, and SHALL treat any high-confidence match as a failed
redaction rather than a warning.

#### Scenario: The model returns text still containing an email

- **GIVEN** a model that echoes its input unchanged
- **WHEN** input containing `jane.smith@example.com` is processed
- **THEN** verification detects the address in the candidate output and the run
  fails

### Behavior: Unchanged and refusal-shaped output are failures

The agent SHALL fail the run when the model returns the text it was sent
byte-for-byte **while contextual PII remains in that text**, and when the output
is refusal-shaped — a short response declining the task rather than a redacted
copy of the input.

The qualifier is load-bearing. "The document contained PII" is the wrong test:
the deterministic layer has already removed the decidable classes by the time
the model sees the text, so a document whose only PII was an email address
legitimately comes back untouched, and failing there rejects correct runs. The
sound test is whether anything the model is responsible for — a name, an
address — is still present in what it was handed.

#### Scenario: Pass-through model leaves a name untouched

- **GIVEN** `bin/pii-redactor -i in.md -o out.md` where `llm` is a script that
  runs `cat`
- **WHEN** `in.md` contains `Contact Jane Smith at jane.smith@example.com`
- **THEN** the run exits non-zero, and `out.md` is not created

#### Scenario: Nothing left for the model to do

- **GIVEN** the same pass-through `llm`
- **WHEN** the input's only PII is an email address, which the deterministic
  layer has already replaced
- **THEN** the run succeeds and the output carries the placeholder, because an
  unchanged response was the correct answer

#### Scenario: Model declines the request

- **GIVEN** a model that replies `I'm sorry, I can't help with that.`
- **WHEN** input of several hundred words is processed
- **THEN** the run fails rather than writing the refusal as the redacted output

### Behavior: Fail closed on the output path

The agent SHALL write the destination file only after verification passes,
staging to a temporary location first, and SHALL remove the staging file on any
failure so no partially redacted artefact is left where clean output is expected.

#### Scenario: Verification fails after a pre-existing output file exists

- **GIVEN** `out.md` already holds a previously verified redaction
- **WHEN** a new run fails verification
- **THEN** `out.md` still holds its previous content, and no staging file remains
  in the directory

### Behavior: No PII persisted outside the output

The agent SHALL disable model prompt logging, keep the original text out of
caches and world-readable temporary files, and SHALL NOT echo unredacted input
into logs, progress output, or error messages.

#### Scenario: Error message for a failed verification

- **GIVEN** verification fails because an email address survived
- **WHEN** the script reports the failure
- **THEN** the message names the class and count that leaked, not the address
  itself, and the model call was made with prompt logging disabled

### Behavior: Bounded memory and bounded model context

The agent SHALL process input without holding the whole document in memory and
without sending more than one chunk budget to the model in a single call. Both
bounds are required: a run that fits in memory but overflows the model's context
fails just as hard, and a run that fits the context but exhausts memory cannot
finish at all.

An input that fits inside one chunk budget SHALL take the single-call path —
one model call over the whole document, verified as a whole. The streaming path
applies only to input that does not fit.

#### Scenario: Input far larger than memory

- **GIVEN** an input file substantially larger than available memory
- **WHEN** the redaction script processes it
- **THEN** the run completes with memory bounded by the chunk budget and carry
  window rather than by the input's size

#### Scenario: Input that fits in one call is unchanged

- **GIVEN** an input smaller than the chunk budget, and an input file that
  produced a given output before chunking existed
- **WHEN** the current script processes it
- **THEN** the output is byte-identical to the pre-chunking output, because the
  single-call path was not altered

### Behavior: Atoms are never split

The agent SHALL decompose input into atoms and SHALL NOT split an atom across
chunks. An atom is one line of text, one top-level value in JSON or NDJSON, one
document in YAML, or one table in TOML. Where a container is larger than the
budget, the agent SHALL descend into its members rather than cutting through
them, and SHALL NOT split a scalar value.

An atom larger than the whole budget SHALL fail the run, naming the atom's
location and size.

#### Scenario: A single line larger than the budget

- **GIVEN** a text file containing one line longer than the chunk budget
- **WHEN** the redaction script processes it
- **THEN** the run fails and names the line and its size, rather than splitting
  the line mid-token

#### Scenario: A JSON array of records larger than the budget

- **GIVEN** a JSON file whose top-level array is larger than the budget, holding
  entries that each fit
- **WHEN** the redaction script processes it
- **THEN** each entry becomes its own atom, container syntax is emitted verbatim,
  and the reassembled output parses as JSON

### Behavior: Chunk boundaries are proven safe

The agent SHALL read a carry window of input before each chunk so a detector can
recognise a match spanning the boundary between two atoms, and SHALL NOT emit any
byte of a chunk until the bytes that could extend a match have been examined.

Where a detector match touches either edge of the examined window, the window was
too small: the agent SHALL extend the carry and rescan, and SHALL fail the run
past a bounded number of extensions rather than emit on an unproven boundary.

#### Scenario: A match spanning two adjacent lines

- **GIVEN** a detector pattern that can match across a newline, and input where
  the match is split between two lines at a chunk boundary
- **WHEN** the redaction script processes it
- **THEN** the match is detected and redacted, not passed through because neither
  chunk contained it whole

#### Scenario: A match a fixed window cannot contain

- **GIVEN** a detector whose match can extend arbitrarily far
- **WHEN** the match reaches the edge of the carry window
- **THEN** the agent extends the carry and rescans, and fails the run rather than
  emitting output whose boundary was never proven safe

### Behavior: Structure is preserved where the format permits

The agent SHALL handle structured input structurally where a parser for the format
is available and streaming-compatible, and SHALL NOT claim structural handling
where it is not.

For JSON and NDJSON the output SHALL be re-parsed after the final rescan, and a
failure to parse SHALL fail the run. For YAML the agent SHALL split only on
document separators and SHALL report that structure within a document is not
parse-verified. Binary input SHALL be refused.

#### Scenario: A model rewrites JSON into something unparsable

- **GIVEN** a JSON input processed through the streaming path
- **WHEN** the model's output no longer parses as JSON
- **THEN** the run fails and the destination file is not created

#### Scenario: Binary input supplied as text

- **GIVEN** an input file whose leading bytes are not text
- **WHEN** the redaction script processes it
- **THEN** the run refuses with a message naming the file, rather than decoding it
  as text and reporting a clean verification that only means nothing matched

### Behavior: Streaming never weakens verification

The agent SHALL verify each chunk before its output reaches the staged artifact,
and SHALL rescan the completed artifact before releasing it. A chunk that fails
verification SHALL contribute nothing, so a run that stops partway leaves no
partially redacted file at the destination.

#### Scenario: The final chunk leaks

- **GIVEN** a streaming run where an early chunk passes and a later chunk's output
  still contains a name the model was given
- **WHEN** the run fails on that chunk
- **THEN** the destination file is absent or still holds its previous content, and
  no staging file remains

### Behavior: Cross-chunk recognition through a run-scoped ledger

The agent SHALL keep a run-scoped, in-memory record of values the model has
identified as PII and SHALL apply it deterministically to later chunks, so a form
appearing alone in a later chunk is still recognised after its fuller form has
scrolled out of view. The ledger SHALL NOT be written to disk and SHALL NOT
outlive the run.

Where the ledger is bounded it SHALL report that older entries were dropped and
that recognition may degrade, rather than degrading silently.

#### Scenario: A surname alone in a later chunk

- **GIVEN** a document whose first chunk contains `Jane Smith`, and whose later
  chunk mentions only `Smith`
- **WHEN** the streaming run processes the later chunk
- **THEN** `Smith` is redacted from the ledger, and the ledger does not appear in
  any file the run writes

### Behavior: Concurrency is an implementation detail

The agent SHALL produce byte-identical output regardless of how much concurrency
the run uses. Concurrency MAY accelerate the deterministic pass, which is pure
CPU work over independent atoms, and MAY accelerate the model pass where doing so
does not compromise cross-chunk recognition.

Concurrency SHALL be opt-in, SHALL default to serial, and SHALL NOT change what
verification proves. Where parallel model calls would order chunks differently
from the document, the agent SHALL preserve document order in the assembled
output, and SHALL NOT let parallel execution weaken the run-scoped ledger.

The agent SHALL NOT require a free-threaded interpreter. Concurrency SHALL work on
whatever interpreter runs the tool.

#### Scenario: Same input, more workers, same output

- **GIVEN** an input processed with concurrency disabled and again with eight
  workers
- **WHEN** both runs complete
- **THEN** the two outputs are byte-identical and report the same match counts

#### Scenario: Workers do not reorder the document

- **GIVEN** a streaming run where chunks finish in a different order from their
  position in the input
- **WHEN** the output is assembled
- **THEN** chunks appear in document order, not completion order

### Behavior: Refuse rather than degrade

The agent SHALL refuse a run it cannot complete safely, and SHALL name the reason,
the location, and the escape hatch. Refusal is the correct outcome for an atom
larger than the budget, a chunk count beyond the configured cap, and input that
cannot be decomposed into atoms.

#### Scenario: Chunk count beyond the cap

- **GIVEN** an input that would require more chunks than the configured maximum
- **WHEN** the redaction script processes it
- **THEN** the run refuses without calling the model, names the chunk count and the
  cap, and names the option that raises the budget

## Constraints

### Constraint: Never emit unverified output

The agent MUST NOT write, print, or return redacted content that has not passed
the verification layer, and MUST NOT offer a flag that skips verification while
still producing output. Convenience here defeats the only guarantee the tool
makes.

### Constraint: Never report success on an unproven redaction

The agent MUST NOT exit zero when verification failed, was skipped, or could not
run. A missing model, a missing detector, or an unreadable output must be a
failure, never a silent pass.

### Constraint: Never trust the model for decidable classes

The agent MUST NOT remove or weaken the deterministic layer on the grounds that
the model already handles those classes, and MUST NOT reduce it to a subset of
patterns because a model is "good enough" at the rest.

### Constraint: Never claim the output is anonymous

The agent MUST NOT describe the output as anonymous, and MUST NOT imply that
passing verification shows the text cannot be re-identified.

Verification proves the narrower, decidable thing: no value the detectors know
about survived, and in pseudonymise mode the substitutions were consistent. It
does not test inference. An output can pass every detector and still identify
its subject through a combination of retained details — an escalation history, a
region, a timeline — and no pattern matches those. Independent measurement puts
re-identification risk at roughly 42% for the best tool in class even on
explicitly written identifiers, and implicit details barely move from baseline.
Stating the limit is not a disclaimer; it is the difference between a true claim
and a false one.

### Constraint: Never let a mocked model imply the tool works

The agent MUST NOT write tests that assert only on exit status or file
non-emptiness while stubbing the model as a pass-through, since that combination
is green precisely when the tool leaks. Tests asserting redaction MUST assert on
absence of the input's PII in the output.

### Constraint: Never let a chunk boundary become a redaction boundary

The agent MUST NOT emit bytes whose surrounding context has not been examined for
detector matches, and MUST NOT trade boundary safety for throughput. A chunk
boundary that a match can straddle is a leak, and it is a leak that verification
over either chunk alone cannot detect — which makes it the most dangerous defect
in this area.

### Constraint: Never persist input that the run is removing

The agent MUST NOT write unredacted input to disk in order to make it seekable,
and MUST NOT spool a pipe to a temporary file. A file deleted on every exit path
is still a file that exists during the run, and "we delete it after" is the
assurance this skill exists to replace.

### Constraint: Never report a chunked run as a whole run

The agent MUST NOT describe a streamed result as if the whole document had been
seen by one model call. Verification, refusal, and progress reporting SHALL state
which path the run took, so a reader cannot mistake a per-chunk guarantee for a
whole-document one.

<!-- skillet-version: 1.7.0 -->

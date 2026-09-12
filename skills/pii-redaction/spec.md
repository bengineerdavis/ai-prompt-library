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
- **SHOULD NOT** apply to scripts that merely *read* content containing PII
  without emitting a sanitised copy, such as a log viewer or a search tool.
- **SHOULD NOT** apply to secret scanning that only detects and reports (for
  example a pre-commit credential check), where no redacted artefact is produced
  and blocking is the whole output.
- **SHOULD NOT** apply to encryption, access control, or data retention work,
  which protect the original rather than emit a safe derivative.

## Behaviors

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

### Constraint: Never let a mocked model imply the tool works

The agent MUST NOT write tests that assert only on exit status or file
non-emptiness while stubbing the model as a pass-through, since that combination
is green precisely when the tool leaks. Tests asserting redaction MUST assert on
absence of the input's PII in the output.

<!-- skillet-version: 1.7.0 -->

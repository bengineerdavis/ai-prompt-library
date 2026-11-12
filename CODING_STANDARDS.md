# Coding standards

What the reviewing agent enforces that no automated check can. Mechanical rules
live in `.alint.yml`, `.pre-commit-config.yaml`, and the skills themselves —
duplicating them here would create a second source of truth that drifts.

Read this when reviewing a change, not when writing one.

## Skill specs are contracts, not prose

A spec's scenarios are the test surface. When reviewing a spec change, check that
every `SHALL` has a scenario that could fail, and that no scenario asserts
something the behaviour does not promise. A behaviour with no failing scenario is
a wish.

## Preserve the reason, not just the rule

Constraints exist because something went wrong. When a change relaxes one — adding
an escape hatch, softening a `MUST NOT` — the diff must carry the argument for why
the failure it guards against can no longer happen. Deleting the reason and
keeping the rule makes the next reviewer unable to tell a considered exemption
from an oversight.

## Changelogs are written for users

An entry names what a user of the prompt or skill can now do, not which file moved.
"Streaming redaction handles input larger than memory" earns its line; "updated
spec.md" does not. Git log already records file movement.

## Vocabulary comes from the glossary

`GLOSSARY.md` holds the settled terms. A change that introduces a new term for an
existing concept — a second name for an atom, a synonym for staged output — is a
finding even when the code is correct, because the next reader has to discover the
two names are one thing.

## Fixtures are synthesized

Never copy real customer data, ticket content, or credentials into a test fixture,
an example, or documentation. Compose a realistic one instead. A scrubbed copy of
real data still carries provenance you cannot see, and rewriting it changes
nothing about where it came from.

---
id: APL-1
title: 'Add streaming path to pii-redactor: atoms, chunk plan, chunk-bytes and max-chunks
  flags'
status: To Do
created_date: 2026-11-10 21:50
labels:
- pii
- streaming
updated_date: 2026-11-12 03:39
documentation:
- DOC-1
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Why: the script reads the whole file into memory (read_input -> Path.read_bytes()) and sends it to the model in one call (run_llm -> subprocess.run with the whole text on stdin), so a large input either exhausts memory or overflows the model's context. Chunking is the open piece in raise's TASK-3 and the reason this refactor exists.

Ship: a streaming path used only above the chunk budget, decomposed into atoms that are never split, with the chunk plan printed to stderr before any model call.

Design locked in /to-spec: atoms are one line of text, one top-level JSON value, one YAML document, one TOML table. Containers are descended into rather than cut, and container syntax emitted verbatim. An atom larger than the budget refuses the run. Input under the budget keeps the existing single-call path byte-for-byte.

Chezmoi counterpart of APL-2 (spec) and APL-3 (verification). Code lives at home/bin/executable_pii-redactor; tests at tests/pii_redactor.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Input under the chunk budget takes the existing single-call path and produces byte-identical output; the 1180-line existing suite passes unchanged
- [ ] #2 Input above the budget completes with memory bounded by the budget and carry window, not by input size
- [ ] #3 Atoms are never split; a single oversized atom fails naming its location and size
- [ ] #4 A large JSON array or object is descended into, reassembles byte-exactly, and the result parses
- [ ] #5 --chunk-bytes, --max-chunks and --plan exist; --plan prints the plan and exits without calling the model
- [ ] #6 A run needing more chunks than the cap refuses before any model call, naming the count, the cap and the option that raises the budget
- [ ] #7 --concurrency N exists and defaults to serial; output is byte-identical at any worker count, with identical match counts
- [ ] #8 Chunks are assembled in document order, not completion order
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:IMPLEMENTATION_NOTES:BEGIN -->
Concurrency (2026-11-10, author-approved): --concurrency N joins --chunk-bytes and --max-chunks on the CLI surface. Layer 1 parallelises across atoms (pure CPU, no ordering constraint); model calls stay serial by default because the run-scoped ledger makes chunk N+1 depend on chunk N's findings. Document order must be preserved in the assembled output regardless of completion order, and output must be byte-identical at any worker count. Do NOT require a free-threaded interpreter.
<!-- SECTION:IMPLEMENTATION_NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->

<!-- SECTION:FINAL_SUMMARY:END -->

## Definition of Done
<!-- DOD:BEGIN -->
<!-- DOD:END -->

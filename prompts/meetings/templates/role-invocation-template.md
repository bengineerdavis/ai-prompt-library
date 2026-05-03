---
id: template-role-invocation
title: Role Invocation Template
description: Reusable template for invoking a specific advisory role in chat or CLI contexts.
version: 0.1.0
type: documentation
license: MIT
context:
  include: true
x-template:
  category: prompt-template
  reusable: true
---

# Role Invocation Template

## Inputs

- Role:
- Topic:
- Goal:
- Constraints:
- Context:
- Desired output:

## Prompt

Adopt the following role:

[ROLE CONTENT OR ROLE SUMMARY]

Task context:

- Topic: [TOPIC]
- Goal: [GOAL]
- Constraints: [CONSTRAINTS]
- Context: [CONTEXT]

Instructions:

1. Stay within the role’s purpose and boundaries.
2. Make trade-offs explicit.
3. Avoid pretending to have authority the role does not have.
4. Produce the requested output in a reusable, structured form.

Desired output:

[DESIRED OUTPUT]
---
id: template-meeting-session-prompt
title: Meeting Session Prompt Template
description: Reusable bootstrap prompt for starting or resuming an advisory meeting session.
version: 0.1.0
type: documentation
license: MIT
context:
  include: true
x-template:
  category: prompt-template
  reusable: true
---

# Meeting Session Prompt Template

Use this template to start or resume an advisory meeting in a chat or CLI tool.

## Inputs

- Meeting goal:
- Relevant project:
- Roles to activate:
- Current preferences:
- Prior minutes or context:
- Specific question for this session:

## Prompt

You are participating in a document-first advisory session.

Use the following meeting context:

- Goal: [MEETING GOAL]
- Project: [PROJECT]
- Active roles: [ROLES]
- Chair preferences: [PREFERENCES]
- Prior context: [PRIOR MINUTES OR SUMMARY]

Instructions:

1. Respect the active role definitions supplied separately.
2. Use an interview-style format when advisors ask questions.
3. Allow one substantive question per advisor per round unless explicitly changed.
4. Keep outputs human-readable but structured enough for note capture.
5. Surface decisions, deferred items, promises, and open questions clearly.
6. If research is needed, separate facts from implications and track sources.

Current task:

[CURRENT SESSION QUESTION OR GOAL]

Output expectations:

- Start with the active advisor or facilitator turn.
- Make role attribution explicit.
- Keep the conversation resumable.
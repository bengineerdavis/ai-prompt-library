# Sentry Support Tutor v1 — README

> A co-pilot, failure-review partner, and structured study guide for a Senior Support Engineer accelerating mastery of Sentry.io.  
> Part of the **Seed Factory System** (v4.1+). Requires: `seed-profile.md`, `seed-orchestrator-v3.2-hybrid.md`, `factories-registry.jsonl`.

---

## 📦 What's in This Package

```
sentry-support-tutor/
├── README-sentry-support-tutor.md          ← You are here
├── sentry-support-tutor-v1.md              ← Main factory prompt (paste into LLM)
└── data/
    └── factories-registry.jsonl            ← Updated registry with this factory registered
```

**Total size**: ~20 KB  
**Setup time**: 2 minutes  
**Dependencies**: seed-profile + orchestrator (from `seed-system/` root)

---

## 🎯 What This Factory Does

Three modes, one factory — triggered by a simple phrase:

| Mode | Trigger Phrase | What Happens |
|------|---------------|--------------|
| 🔍 **Co-Pilot** | `"co-pilot mode"` or `"I'm working a ticket"` | Real-time ticket guidance; enforces question-first rule before any answer |
| 🔁 **Failure Review** | `"failure review"` or `"let's review [ticket]"` | Structured debrief with rubric scoring and pattern tagging |
| 📚 **Study Session** | `"study session"` or `"let's study [topic]"` | Concept → application → check question flow |

**The core discipline this factory enforces:**
```
❌ Old loop:  ticket → research → conclude → respond (exhausted, wrong)
✅ New loop:  ticket → identify what's missing → ask ONE question → research with context
```

---

## 🚀 Quick Start

### Step 1 — Set up Seed root (if not already done)
```
Ensure these are in your seed-system/ root:
  ✓ seed-profile.md
  ✓ seed-orchestrator-v3.2-hybrid.md
  ✓ factories-registry.jsonl  ← use the one from data/ here (includes this factory)
  ✓ seed-prompting-strategies.jsonl
```

### Step 2 — Start a session (Perplexity or any LLM)
```
Paste 1: factories-registry.jsonl
Paste 2: seed-orchestrator-v3.2-hybrid.md
Paste 3: seed-profile.md
Type:    "Goal: Help me work a Sentry support ticket"
```

Orchestrator will match `sentry-support-tutor` at ≥85% confidence and prompt you to load it.

### Step 3 — Paste the factory
```
Paste: sentry-support-tutor-v1.md
```

### Step 4 — Pick your mode
```
"co-pilot mode" + paste ticket text
"failure review" + describe a past ticket
"study session — week 1"
```

---

## 📋 12-Week Study Plan (Embedded in Factory)

### Phase 1 — Foundation (Weeks 1–4)
| Week | Topic | Focus |
|------|-------|-------|
| 1 | Sentry data model: Events, Issues, Projects, DSN | How Sentry thinks about data |
| 2 | SDK fundamentals: init, breadcrumbs, contexts, tags | What customers misconfigure |
| 3 | Error Monitoring: stack traces, grouping, fingerprinting | Core product — most ticket volume |
| 4 | Tracing & Performance: spans, transactions, sample rates | Second most common ticket type |

### Phase 2 — Support Craft (Weeks 5–8)
| Week | Topic |
|------|-------|
| 5 | The clarifying question framework |
| 6 | Reproduction methodology: bug vs. config issue |
| 7 | Escalation judgment: push vs. pass vs. close |
| 8 | Response writing: confident, clear, non-over-committing |

### Phase 3 — Edge Cases & Mastery (Weeks 9–12)
| Week | Topic |
|------|-------|
| 9 | Session Replay & User Feedback |
| 10 | Source Maps & Release Tracking |
| 11 | Crons, Alerts, and Notification rules |
| 12 | Multi-project orgs, SDK version conflicts, AI agent context |

---

## 🔁 Failure Review Rubric

Every ticket debrief scores on 4 dimensions:

```
1. Did we understand the actual problem before responding? [yes/no/partial]
2. What was the first question we should have asked?
3. What type of gap? [product | sdk | investigation | response]
4. What's the 1-sentence rule to carry forward?
```

Pattern tags are logged per review (e.g., `premature_conclusion`, `missing_version_info`).  
After 3+ occurrences of the same tag → factory reinforces the countermeasure automatically.

---

## 🔍 Co-Pilot Mode — Output Format

When you paste a ticket and say "co-pilot mode", you get:

```
🔍 MISSING INFO:
- [list of unknowns from ticket]

❓ FIRST QUESTION TO ASK:
"[exact question to send to customer]"

🗺️ INVESTIGATION PATH (once answered):
- [step 1]
- [step 2]

Confidence in current direction: [~X%]
```

**Rule**: The factory will never output an answer or direction before it outputs a clarifying question.

---

## 📊 Factory Metadata

```json
{
  "name": "sentry-support-tutor",
  "version": "1.0",
  "type": "factory",
  "parent": "technical-tutor-for-self-learning",
  "avg_score": 8.80,
  "strategies": ["Decomposition", "Chain-of-Thought", "Meta-Prompting", "Few-Shot", "Self-Critique"],
  "tasks": ["co_pilot", "failure_review", "study_session", "pattern_tracking", "question_discipline"],
  "created": "2026-03-21"
}
```

Orchestrator match keywords: `sentry`, `support`, `tutor`, `copilot`, `triage`, `tickets`, `SDK`, `failure-review`, `breadcrumbs`, `DSN`, `tracing`, `escalation`

---

## 🗂️ Recommended Directory Layout

```
~/Documents/seed-system/
├── seed-profile.md
├── seed-orchestrator-v3.2-hybrid.md
├── seed-optimizer.md
├── seed-prompting-strategies.jsonl
├── factories-registry.jsonl          ← master registry (keep updated)
│
├── factories/
│   ├── sentry-support-tutor/
│   │   ├── README-sentry-support-tutor.md    ← this file
│   │   ├── sentry-support-tutor-v1.md
│   │   └── data/
│   │       └── factories-registry.jsonl      ← registry snapshot at time of creation
│   │
│   ├── technical-tutor-for-self-learning/    ← parent meta-factory
│   ├── strategy-builder/
│   ├── shopping-builder/
│   └── interview-prep/
│
└── logs/
    └── execution-log.jsonl                   ← tail module appends here
```

---

## 🔧 Adding to Registry (if not already present)

```bash
# Append registry entry
echo '{"name":"sentry-support-tutor","version":"1.0","type":"factory","description":"Co-pilot, failure review, and study guide factory for a Senior Support Engineer accelerating Sentry.io mastery.","parent":"technical-tutor-for-self-learning","enabled":true,"tasks":["co_pilot","failure_review","study_session","pattern_tracking","question_discipline"],"keywords":["sentry","support","tutor","copilot","study","triage","tickets","SDK","failure-review","breadcrumbs","DSN","tracing","issues","events","escalation"],"rubric":{"clarity":0.2,"feasibility":0.25,"goal_alignment":0.25,"risk_awareness":0.2,"context_awareness":0.1},"strategies":["Decomposition","Chain-of-Thought","Meta-Prompting","Few-Shot","Self-Critique"],"recent_scores":[8.8],"avg_score":8.80,"last_updated":"2026-03-21"}' >> factories-registry.jsonl

# Verify
jq 'select(.name == "sentry-support-tutor")' factories-registry.jsonl
```

---

## 🧪 Test Queries (Orchestrator Match ≥85%)

```
"co-pilot mode — customer says Sentry isn't capturing errors"
"failure review on a ticket I closed yesterday"
"study session week 1 — Sentry data model"
"help me triage this SDK initialization ticket"
"I'm stuck on a breadcrumbs issue, co-pilot"
```

---

## 📞 Troubleshooting

| Problem | Fix |
|---------|-----|
| Orchestrator matches wrong factory | Add more Sentry-specific keywords to query |
| Factory skips the clarifying question | Remind it: "question-first rule is non-negotiable" |
| Study plan feels too fast | Tell the factory: "slow down, I need more depth on week N" |
| Pattern tags not tracking | Paste prior session summary into `continuity_baseline` field |

---

## 🔗 Related Files

| File | Location | Purpose |
|------|----------|---------|
| `technical-tutor-for-self-learning-v1.md` | `factories/technical-tutor-for-self-learning/` | Parent meta-factory — generates tutors like this one |
| `seed-profile.md` | root | Global tone and behavior norms |
| `seed-prompting-strategies.jsonl` | root | Strategy registry referenced in Phase 0 |
| `factories-registry.jsonl` | root | Master registry — must include this factory's entry |

---

**Version**: 1.0 · **Created**: 2026-03-21 · **Status**: Production-Ready ✓  
**Parent**: `technical-tutor-for-self-learning` · **Orchestrator**: v3.2+

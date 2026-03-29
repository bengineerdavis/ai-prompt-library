# Technical Tutor for Self-Learning v1 — README

> A meta-factory that generates and deploys domain-specific technical tutors for any software, hardware, developer tool, or foundational concept.  
> Part of the **Seed Factory System** (v4.1+). Requires: `seed-profile.md`, `seed-orchestrator-v3.2-hybrid.md`, `factories-registry.jsonl`.

---

## 📦 What's in This Package

```
technical-tutor-for-self-learning/
├── README-technical-tutor-for-self-learning.md   ← You are here
├── technical-tutor-for-self-learning-v1.md        ← Main meta-factory prompt
└── data/
    └── factories-registry.jsonl                   ← Updated registry with this factory registered

Generated child factories (examples):
factories/
├── sentry-support-tutor/                          ← Generated from this meta-factory
├── kubernetes-tutor/                              ← Future example
└── rust-tutor/                                    ← Future example
```

**Total size**: ~18 KB  
**Setup time**: 2 minutes  
**Type**: `meta-factory` — generates other factories  
**Dependencies**: seed-profile + orchestrator + factory-template-v1.1

---

## 🎯 What This Meta-Factory Does

Unlike regular factories that solve a specific domain problem, this one **builds the factories that do**. Given any technical domain and a learner profile, it:

1. **Profiles the learner** — role, skill level, failure modes, available time
2. **Architects a study plan** — 3 phases × 4 weeks, scoped to job-critical topics first
3. **Generates a tutor factory** — a complete `.md` file following `factory-template-v1.1`
4. **Deploys immediately** — starts tutoring in the same session without extra setup

Every tutor it generates follows the same 3-mode pattern:

| Mode | Trigger | Purpose |
|------|---------|---------|
| 🔍 **Co-Pilot** | `"co-pilot mode"` | Job-task support; question-first discipline |
| 🔁 **Failure Review** | `"failure review"` | Debrief past work with rubric + pattern tagging |
| 📚 **Study Session** | `"study session"` | Structured concept → application → check question |

---

## 🆚 How It Differs from `factory-builder-v1`

| | `factory-builder-v1` | `technical-tutor-for-self-learning-v1` |
|--|---|---|
| **Purpose** | General-purpose factory generator | Tutor-specific factory generator |
| **Pedagogy** | Neutral — any factory type | Opinionated — always Co-Pilot + Failure Review + Study Session |
| **Learner profiling** | Not included | Built-in 3-round intake |
| **Study plan** | Not included | Always generated, scoped to available time |
| **Failure mode mapping** | Not included | Maps failure modes → countermeasures automatically |
| **Domain types** | Any | Technical/software/hardware only |

Use `factory-builder-v1` when you want a general factory.  
Use this when you want a **tutor** for a technical domain.

---

## 🚀 Quick Start

### Step 1 — Set up Seed root (if not already done)
```
Ensure these are in your seed-system/ root:
  ✓ seed-profile.md
  ✓ seed-orchestrator-v3.2-hybrid.md
  ✓ factories-registry.jsonl  ← use the one from data/ here
  ✓ seed-prompting-strategies.jsonl
  ✓ factory-template-v1.1.md
```

### Step 2 — Start a session
```
Paste 1: factories-registry.jsonl
Paste 2: seed-orchestrator-v3.2-hybrid.md
Paste 3: seed-profile.md
Type:    "Goal: I need a tutor to help me learn [domain]"
```

Orchestrator will match this factory at ≥85% confidence for any query mentioning:  
`tutor`, `self-learning`, `accelerate`, `mastery`, `study plan`, `mentor`, `new role`, `learning`

### Step 3 — Paste the meta-factory
```
Paste: technical-tutor-for-self-learning-v1.md
```

### Step 4 — Answer intake questions (≤3 rounds, ≤4 questions each)
The factory will ask about your domain, role, skill level, failure modes, and available time.  
Then it generates a tutor and can start working immediately.

### Step 5 — Save the generated tutor
Copy the generated `.md` output → save as `factories/{domain-slug}-tutor/`

---

## 🏗️ Domain Types Supported

| Domain Type | Examples | Tutor Focus |
|-------------|---------|-------------|
| `saas_platform` | Sentry.io, Datadog, Salesforce | Product model, API/SDK behavior, common user errors |
| `developer_tool` | Kubernetes, Docker, Terraform, Git | CLI/config/integration, failure modes, version quirks |
| `programming_language` | Rust, Go, TypeScript, Python | Syntax, runtime behavior, type system, idioms |
| `hardware` | Networking gear, embedded systems, GPUs | Physical layer, specs, compatibility, failure signatures |
| `foundational_concept` | TCP/IP, OS internals, databases | Mental models, analogies, misconceptions |
| `framework` | React, FastAPI, Rails, LangChain | Conventions, lifecycle, integration patterns |

---

## 🧠 Failure Mode → Countermeasure Mapping

The factory automatically detects your failure mode and wires the appropriate countermeasure into the generated tutor:

| Failure Mode | What It Looks Like | Countermeasure |
|---|---|---|
| `jumps_to_conclusions` | Answers before understanding | Question-first rule in Co-Pilot; Meta-Prompting SLA check |
| `paralysis_by_analysis` | Can't decide when to act | Time-box steps; explicit "good enough to proceed" threshold |
| `skips_fundamentals` | Uses things without understanding them | Phase 1 lock — must pass quiz gate before Phase 2 |
| `cognitive_overload` | Overwhelmed by learning + doing simultaneously | Separate "learn concept" and "solve task" into distinct steps |
| `imposter_syndrome` | Undermines own correct instincts | Probability language; normalize uncertainty explicitly |

---

## ⏱️ Study Plan Scoping (by Available Time)

| Weekly Hours | Study Plan Shape |
|---|---|
| < 2 hrs | Survival mode: Phase 1 only, top 3 job-critical topics |
| 2–4 hrs | Full Phase 1 + 2; Phase 3 as stretch. ~1 topic/week |
| 4–7 hrs | Full 3-phase plan + optional deep-dives. ~1.5 topics/week |
| 7+ hrs | Accelerated: compress to 8 weeks, add simulated tasks |

---

## 📊 Factory Metadata

```json
{
  "name": "technical-tutor-for-self-learning",
  "version": "1.0",
  "type": "meta-factory",
  "parent": "strategy-builder",
  "generates": "{domain-slug}-tutor-v1.md",
  "avg_score": 8.70,
  "strategies": [
    "Decomposition", "Chain-of-Thought", "Meta-Prompting",
    "Few-Shot", "Self-Critique", "Constraint-Based-Reasoning"
  ],
  "tasks": ["factory_generation", "tutor_deployment", "study_plan_design", "learner_profiling"],
  "created": "2026-03-21"
}
```

Orchestrator match keywords: `tutor`, `self-learning`, `technical`, `study`, `co-pilot`, `failure-review`, `mastery`, `accelerator`, `mentor`, `learning`

---

## 🗂️ Recommended Directory Layout

```
~/Documents/seed-system/
├── seed-profile.md
├── seed-orchestrator-v3.2-hybrid.md
├── seed-optimizer.md
├── seed-prompting-strategies.jsonl
├── factory-template-v1.1.md
├── factories-registry.jsonl                    ← master registry
│
├── factories/
│   ├── technical-tutor-for-self-learning/      ← this package
│   │   ├── README-technical-tutor-for-self-learning.md
│   │   ├── technical-tutor-for-self-learning-v1.md
│   │   └── data/
│   │       └── factories-registry.jsonl
│   │
│   ├── sentry-support-tutor/                   ← child generated by this factory
│   │   ├── README-sentry-support-tutor.md
│   │   ├── sentry-support-tutor-v1.md
│   │   └── data/
│   │       └── factories-registry.jsonl
│   │
│   ├── factory-builder-v1/                     ← sibling (general factory generator)
│   ├── strategy-builder/
│   ├── shopping-builder/
│   └── interview-prep/
│
└── logs/
    └── execution-log.jsonl
```

---

## 🔧 Adding to Registry (if not already present)

```bash
# Append registry entry
echo '{"name":"technical-tutor-for-self-learning","version":"1.0","type":"meta-factory","description":"Meta-factory that generates and deploys domain-specific technical tutors for any software, hardware, or foundational technical topic. All generated tutors follow Co-Pilot + Failure Review + Study Session pattern.","parent":"strategy-builder","enabled":true,"tasks":["factory_generation","tutor_deployment","study_plan_design","learner_profiling"],"keywords":["tutor","self-learning","technical","study","co-pilot","failure-review","mastery","accelerator","mentor","learning"],"rubric":{"domain_coverage":0.25,"job_relevance":0.25,"pedagogical_soundness":0.25,"cognitive_load_management":0.15,"constraint_fit":0.1},"strategies":["Decomposition","Chain-of-Thought","Meta-Prompting","Few-Shot","Self-Critique","Constraint-Based-Reasoning"],"generates":"{domain-slug}-tutor-v1.md","recent_scores":[8.7],"avg_score":8.70,"last_updated":"2026-03-21"}' >> factories-registry.jsonl

# Verify
jq 'select(.name == "technical-tutor-for-self-learning")' factories-registry.jsonl
```

---

## 🧪 Test Queries (Orchestrator Match ≥85%)

```
"I need a tutor to help me learn Kubernetes for my new DevOps role"
"Create a study plan for learning Rust — I'm a Python dev with 3 months to ramp"
"Help me master TCP/IP fundamentals, I keep getting lost on network tickets"
"I'm a new SRE and I'm struggling with Terraform — can you be my mentor?"
"Generate a tutor for learning React, I know Vue but need to switch"
```

---

## 🔄 Generating a New Tutor — Example Flow

```
You: "I need a tutor for learning Kubernetes for my new Platform Engineering role"

Factory Phase 0 (intake):
  Q1: How long have you been in this role? What's your K8s skill level (1–5)?
  Q2: What does a "bad day" with K8s look like for you?
  Q3: How many hours/week can you study?

You answer → Factory runs Phase 1:
  - Domain type: developer_tool
  - Failure mode detected: cognitive_overload
  - Countermeasure: separate learn-from-operate steps
  - Study plan compressed to 2–4 hrs/week shape

Factory Phase 2 output:
  ✓ Generates kubernetes-tutor-v1.md (full factory file)
  ✓ Prints registry entry to append
  ✓ Asks: "Deploy now or save and paste later?"
  → "Deploy now" → Tutor starts immediately
```

---

## 📞 Troubleshooting

| Problem | Fix |
|---------|-----|
| Orchestrator matches `factory-builder` instead | Add "tutor" or "study plan" to your query |
| Intake questions don't stop | Say "enough questions, generate the tutor" |
| Generated tutor is too generic | Re-run with more specific job context in Phase 0 |
| Study plan doesn't fit your time | Tell it: "compress to X hours/week" |
| Generated factory file is missing sections | Remind it: "follow factory-template-v1.1 structure" |

---

## 🔗 Related Files

| File | Location | Purpose |
|------|----------|---------|
| `factory-builder-v1.md` | `factories/factory-builder-v1/` | General factory generator (sibling) |
| `factory-template-v1.1.md` | root | Canonical structure all generated factories must follow |
| `sentry-support-tutor-v1.md` | `factories/sentry-support-tutor/` | Example child tutor generated by this factory |
| `seed-prompting-strategies.jsonl` | root | Strategy registry; `Constraint-Based-Reasoning` is key here |

---

**Version**: 1.0 · **Created**: 2026-03-21 · **Status**: Production-Ready ✓  
**Type**: `meta-factory` · **Parent**: `strategy-builder` · **Orchestrator**: v3.2+  
**Refactored from**: `sentry-support-tutor-v1` (domain-specific → generalized)

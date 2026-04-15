# Technical Tutor for Self-Learning v1

A meta-factory that generates and deploys domain-specific technical tutors for any
software, hardware, developer tool, or foundational concept.

Part of the Seed Factory System (v4.1+).
Dependencies: `seed-profile.md`, `seed-orchestrator-v3.2-hybrid.md`, `factories-registry.jsonl`, `factory-template-v1.1.md`

______________________________________________________________________

## What This Meta-Factory Does

Unlike regular factories that solve a specific domain problem, this one builds the
factories that do. Given any technical domain and a learner profile, it:

1. **Profiles the learner** — role, skill level, failure modes, available time
1. **Architects a study plan** — 3 phases × 4 weeks, scoped to job-critical topics first
1. **Generates a tutor factory** — a complete `.md` file following `factory-template-v1.1`
1. **Deploys immediately** — starts tutoring in the same session without extra setup

Every tutor it generates follows the same 3-mode pattern:

| Mode               | Trigger            | Purpose                                           |
| ------------------ | ------------------ | ------------------------------------------------- |
| **Co-Pilot**       | `"co-pilot mode"`  | Job-task support; question-first discipline       |
| **Failure Review** | `"failure review"` | Debrief past work with rubric + pattern tagging   |
| **Study Session**  | `"study session"`  | Structured concept → application → check question |

______________________________________________________________________

## How It Differs from `factory-builder-v1`

|                          | `factory-builder-v1`              | `technical-tutor-for-self-learning-v1`                         |
| ------------------------ | --------------------------------- | -------------------------------------------------------------- |
| **Purpose**              | General-purpose factory generator | Tutor-specific factory generator                               |
| **Pedagogy**             | Neutral — any factory type        | Opinionated — always Co-Pilot + Failure Review + Study Session |
| **Learner profiling**    | Not included                      | Built-in 3-round intake                                        |
| **Study plan**           | Not included                      | Always generated, scoped to available time                     |
| **Failure mode mapping** | Not included                      | Maps failure modes → countermeasures automatically             |
| **Domain types**         | Any                               | Technical/software/hardware only                               |

Use `factory-builder-v1` when you want a general factory.
Use this when you want a tutor for a technical domain.

______________________________________________________________________

## Quick Start

1. Confirm these files are in your seed root:

   - `seed-profile.md`
   - `seed-orchestrator-v3.2-hybrid.md`
   - `factories-registry.jsonl`
   - `seed-prompting-strategies.jsonl`
   - `factory-template-v1.1.md`

1. Start a session:

   ```
   Paste 1: factories-registry.jsonl
   Paste 2: seed-orchestrator-v3.2-hybrid.md
   Paste 3: seed-profile.md
   Type:    "Goal: I need a tutor to help me learn [domain]"
   ```

   The orchestrator will match this factory at ≥85% confidence for any query
   mentioning: `tutor`, `self-learning`, `accelerate`, `mastery`, `study plan`, `mentor`, `learning`

1. Paste `technical-tutor-for-self-learning-v1.md`.

1. Answer the intake questions (≤3 rounds, ≤4 questions each), then save the
   generated `.md` output to `factories/{domain-slug}-tutor/`.

For registry setup and directory layout, see `docs/setup.md` in the seed root.

______________________________________________________________________

## Supported Domain Types

| Domain Type            | Examples                                | Tutor Focus                                              |
| ---------------------- | --------------------------------------- | -------------------------------------------------------- |
| `saas_platform`        | Sentry.io, Datadog, Salesforce          | Product model, API/SDK behavior, common user errors      |
| `developer_tool`       | Kubernetes, Docker, Terraform, Git      | CLI/config/integration, failure modes, version quirks    |
| `programming_language` | Rust, Go, TypeScript, Python            | Syntax, runtime behavior, type system, idioms            |
| `hardware`             | Networking gear, embedded systems, GPUs | Physical layer, specs, compatibility, failure signatures |
| `foundational_concept` | TCP/IP, OS internals, databases         | Mental models, analogies, misconceptions                 |
| `framework`            | React, FastAPI, Rails, LangChain        | Conventions, lifecycle, integration patterns             |

______________________________________________________________________

## Failure Mode → Countermeasure Mapping

The factory detects your failure mode and wires the appropriate countermeasure into
the generated tutor:

| Failure Mode            | What It Looks Like                             | Countermeasure                                                |
| ----------------------- | ---------------------------------------------- | ------------------------------------------------------------- |
| `jumps_to_conclusions`  | Answers before understanding                   | Question-first rule in Co-Pilot; Meta-Prompting SLA check     |
| `paralysis_by_analysis` | Can't decide when to act                       | Time-box steps; explicit "good enough to proceed" threshold   |
| `skips_fundamentals`    | Uses things without understanding them         | Phase 1 lock — must pass quiz gate before Phase 2             |
| `cognitive_overload`    | Overwhelmed by learning + doing simultaneously | Separate "learn concept" and "solve task" into distinct steps |
| `imposter_syndrome`     | Undermines own correct instincts               | Probability language; normalize uncertainty explicitly        |

______________________________________________________________________

## Study Plan Scoping

| Weekly Hours | Study Plan Shape                                           |
| ------------ | ---------------------------------------------------------- |
| < 2 hrs      | Survival mode: Phase 1 only, top 3 job-critical topics     |
| 2–4 hrs      | Full Phase 1 + 2; Phase 3 as stretch (~1 topic/week)       |
| 4–7 hrs      | Full 3-phase plan + optional deep-dives (~1.5 topics/week) |
| 7+ hrs       | Accelerated: compress to 8 weeks, add simulated tasks      |

______________________________________________________________________

## Example Generation Flow

```
You: "I need a tutor for learning Kubernetes for my new Platform Engineering role"

Phase 0 (intake):
  Q1: How long have you been in this role? What's your K8s skill level (1–5)?
  Q2: What does a "bad day" with K8s look like for you?
  Q3: How many hours/week can you study?

Phase 1 (analysis):
  - Domain type: developer_tool
  - Failure mode detected: cognitive_overload
  - Countermeasure: separate learn-from-operate steps
  - Study plan: 2–4 hrs/week shape

Phase 2 (output):
  ✓ Generates kubernetes-tutor-v1.md (full factory file)
  ✓ Prints registry entry to append
  ✓ Asks: "Deploy now or save and paste later?"
```

______________________________________________________________________

## Troubleshooting

| Problem                                        | Fix                                                 |
| ---------------------------------------------- | --------------------------------------------------- |
| Orchestrator matches `factory-builder` instead | Add "tutor" or "study plan" to your query           |
| Intake questions don't stop                    | Say "enough questions, generate the tutor"          |
| Generated tutor is too generic                 | Re-run with more specific job context in Phase 0    |
| Study plan doesn't fit your time               | Tell it: "compress to X hours/week"                 |
| Generated factory is missing sections          | Remind it: "follow factory-template-v1.1 structure" |

______________________________________________________________________

## Related Files

| File                              | Purpose                                                     |
| --------------------------------- | ----------------------------------------------------------- |
| `factory-builder-v1.md`           | General factory generator (sibling)                         |
| `factory-template-v1.1.md`        | Canonical structure all generated factories must follow     |
| `sentry-support-tutor-v1.md`      | Example child tutor generated by this factory               |
| `seed-prompting-strategies.jsonl` | Strategy registry; `Constraint-Based-Reasoning` is key here |

______________________________________________________________________

**Version**: 1.0 · **Created**: 2026-03-21 · **Type**: `meta-factory` · **Parent**: `strategy-builder` · **Orchestrator**: v3.2+

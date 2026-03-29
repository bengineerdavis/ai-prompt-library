#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from textwrap import dedent

DEFAULT_FACTORY_FILE = "factories-registry-v3.3.jsonl"
DEFAULT_STRATEGY_FILE = "seed-prompting-strategies-v3.3.jsonl"

PASTE2 = dedent("""\
SEED SYSTEM BOOTSTRAP — PASTE 2 of 3: SEED PROFILE + ORCHESTRATOR
Paste after registry. Do not respond yet. Acknowledge with "Orchestrator loaded ✓"

--- seed-profile-v3 ---
You are a meta-system designer, expert senior AI & prompt engineer, and technical coach for a senior IC or technical practitioner.

TONE & EPISTEMIC NORMS:
- Use probability language: "[~75% confidence]", "likely", "uncertain"
- Be epistemically honest: always include caveats and "where this might be wrong"
- Prioritize scannability: short sections, bullets, optional tables
- Respect time constraints: design outputs for the time available
- Treat user as a senior IC unless told otherwise
- Avoid walls of text; prioritize actionable outputs
- Technical depth over business buzzwords

EVALUATION CRITERIA (all outputs scored on):
1. Clarity  2. Conciseness  3. Completeness
4. Goal Alignment  5. Context Awareness  6. Expected Output

GLOBAL SWITCHES:
- interaction_mode: "interactive"
- feedback_mode: "on"
--- END SEED PROFILE ---

--- orchestrator-v3.3 ---
You are the Seed Orchestrator v3.3. When I give you a goal, you:

PHASE 1 — MATCH: Compute 4-signal match against the loaded registry.
  Signal 1: Keyword match (40%) — overlap between query tokens and factory keywords
  Signal 2: Semantic match (30%) — intent alignment between query and factory purpose
  Signal 3: Task coverage (20%) — % of inferred required tasks the factory covers
  Signal 4: Recency/performance (10%) — factory avg_score / 10

  Thresholds:
  ≥90% → AUTO-RUN (state confidence, proceed)
  85–89% → ASK "Run [factory]?" (default yes)
  75–84% → Show top 3, ask user to pick
  <75% → Suggest creating a new factory with factory-builder-v1

  Show all 4 signals transparently every time.

PHASE 2 — TASK EXPANSION: If match ≥75%, check if query implies tasks not in factory's task list. If new tasks detected, ask: "Add [task] to [factory]? [Y/n]"

PHASE 3 — EXECUTE: Tell me which factory .md to paste, or if fully manual, run the factory phases inline.

PHASE 4 — TAIL MODULE: After execution, ask me to rate 1–5 on Clarity / Relevance / Confidence. Log result. Suggest next step.

STRATEGY SELECTION (Phase 0 of any factory):
- Default: use strategies listed in the factory's registry entry
- Meta-factories + multi-model available: prepend Model-Council-Generate → Model-Council-Judge
- Meta-factories + single model (manual mode): prepend Mixture-of-Roles
- Always show selected strategies before executing Phase 1

COUNCIL STRATEGIES:
- Model-Council-Generate: run Phase 1 prompt on 2-3 models independently, collect candidates
- Model-Council-Judge: send candidates to 2-3 judge models with rubric, aggregate scores, flag std_dev > 1.5 as uncertain
- Mixture-of-Roles (single-model fallback): run same prompt 3x as Skeptic / Domain Expert / Pragmatist, then synthesize

Acknowledge with: "Seed Orchestrator v3.3 ready. State your goal."
--- END ORCHESTRATOR ---
""")

def read_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            s = line.strip()
            if not s:
                continue
            try:
                rows.append(json.loads(s))
            except json.JSONDecodeError as e:
                raise SystemExit(f"Invalid JSONL in {path} line {n}: {e}")
    return rows

def to_jsonl_text(rows):
    return "\\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in rows)

def render_registry_paste(factory_rows):
    return dedent(f"""\
    SEED SYSTEM BOOTSTRAP — PASTE 1 of 3: REGISTRY
    Paste this first. Do not respond yet. Acknowledge with "Registry loaded ✓"

    --- {DEFAULT_FACTORY_FILE} ---
    {to_jsonl_text(factory_rows)}
    --- END REGISTRY ---
    """)

def render_strategy_summary(strategy_rows):
    core = []
    council = []
    for s in strategy_rows:
        line = f"- {s['name']} ({s['effectiveness']}, {s['computational_cost']}"
        if s.get("requires_multiple_runs"):
            line += ", requires_multiple_runs"
        line += f"): {s['implementation']}. Best for: {', '.join(s['best_for'])}."
        if "council" in s.get("tags", []):
            council.append(line)
        else:
            core.append(line)

    core_text = "\\n".join(core)
    council_text = "\\n".join(council)

    return dedent(f"""\
    SEED SYSTEM BOOTSTRAP — PASTE 3 of 3: STRATEGY REGISTRY
    Paste last. Respond with "Strategy registry loaded ✓ — all 3 components active. State your goal."

    --- {DEFAULT_STRATEGY_FILE} ---
    CORE STRATEGIES:
    {core_text}

    COUNCIL STRATEGIES:
    {council_text}
    --- END STRATEGIES ---
    """)

def write_quickstart(outdir: Path):
    text = dedent("""\
    # Quick Start

    1. Paste `PASTE-1-registry.md`
    2. Paste `PASTE-2-orchestrator.md`
    3. Paste `PASTE-3-strategies.md`
    4. Then send:

    Goal: [your goal here]

    Example goals:
    - Goal: I want to study Sentry tracing and breadcrumbs for my support role
    - Goal: Create a 6-week DevOps learning roadmap
    - Goal: Help me prep for a staff engineer behavioral interview
    - Goal: Build a new factory for Kubernetes troubleshooting
    - Goal: Best mechanical keyboard to buy under $150
    """)
    (outdir / "BOOTSTRAP-QUICKSTART.md").write_text(text, encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description="Build Seed bootstrap paste files from JSONL registries.")
    parser.add_argument("--dir", default=".", help="Directory containing the JSONL registry files")
    parser.add_argument("--output", default="bootstrap-out", help="Output directory")
    parser.add_argument("--validate", action="store_true", help="Only validate JSONL files")
    args = parser.parse_args()

    root = Path(args.dir).expanduser().resolve()
    outdir = Path(args.output).expanduser().resolve()

    factory_path = root / DEFAULT_FACTORY_FILE
    strategy_path = root / DEFAULT_STRATEGY_FILE

    if not factory_path.exists():
        raise SystemExit(f"Missing file: {factory_path}")
    if not strategy_path.exists():
        raise SystemExit(f"Missing file: {strategy_path}")

    factory_rows = read_jsonl(factory_path)
    strategy_rows = read_jsonl(strategy_path)

    if args.validate:
        print(f"Validated: {factory_path}")
        print(f"Validated: {strategy_path}")
        print(f"Factories: {len(factory_rows)}")
        print(f"Strategies: {len(strategy_rows)}")
        return

    outdir.mkdir(parents=True, exist_ok=True)

    (outdir / "PASTE-1-registry.md").write_text(render_registry_paste(factory_rows), encoding="utf-8")
    (outdir / "PASTE-2-orchestrator.md").write_text(PASTE2, encoding="utf-8")
    (outdir / "PASTE-3-strategies.md").write_text(render_strategy_summary(strategy_rows), encoding="utf-8")
    write_quickstart(outdir)

    print(f"Wrote: {outdir / 'PASTE-1-registry.md'}")
    print(f"Wrote: {outdir / 'PASTE-2-orchestrator.md'}")
    print(f"Wrote: {outdir / 'PASTE-3-strategies.md'}")
    print(f"Wrote: {outdir / 'BOOTSTRAP-QUICKSTART.md'}")

if __name__ == "__main__":
    main()
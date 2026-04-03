#!/usr/bin/env python3
"""Build Seed bootstrap paste files from the live repo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from textwrap import dedent

REGISTRIES_SUBDIR = "registries"
FACTORY_REGISTRY  = "factories-registry-v3.3.jsonl"
STRATEGY_REGISTRY = "seed-prompting-strategies-v1.1.jsonl"
PROFILE_PATH      = "seed/profile/profile.md"
ORCHESTRATOR_PATH = "seed/orchestrator/orchestrator.md"

QUICKSTART = dedent("""\
    # Bootstrap Quickstart

    1. Paste `PASTE-1-registry.md`
    2. Paste `PASTE-2-orchestrator.md`
    3. Paste `PASTE-3-strategies.md`
    4. Then send your goal:

        Goal: [your goal here]

    Example goals:
    - Goal: I want to study Sentry tracing and breadcrumbs for my support role
    - Goal: Create a 6-week DevOps learning roadmap
    - Goal: Help me prep for a staff engineer behavioral interview
    - Goal: Build a new factory for Kubernetes troubleshooting
    - Goal: Best mechanical keyboard to buy under $150

    For full usage instructions see QUICKSTART.md in the repo root.
    For registry setup and factory registration see docs/setup.md.
""")


# ---------------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------------

def read_jsonl(path: Path) -> list[dict]:
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as e:
            raise SystemExit(f"Invalid JSONL {path}:{n}: {e}")
    return rows


def to_jsonl(rows: list[dict]) -> str:
    return "\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in rows)


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------

def render_paste1(factory_rows: list[dict]) -> str:
    return (
        "SEED SYSTEM BOOTSTRAP — PASTE 1 of 3: REGISTRY\n"
        'Paste this first. Do not respond yet. Acknowledge with "Registry loaded ✓"\n\n'
        f"--- {FACTORY_REGISTRY} ---\n"
        f"{to_jsonl(factory_rows)}\n"
        "--- END REGISTRY ---\n"
    )


def render_paste2(profile: str, orchestrator: str) -> str:
    return (
        "SEED SYSTEM BOOTSTRAP — PASTE 2 of 3: SEED PROFILE + ORCHESTRATOR\n"
        'Paste after registry. Do not respond yet. Acknowledge with "Orchestrator loaded ✓"\n\n'
        f"--- {PROFILE_PATH} ---\n{profile}\n--- END SEED PROFILE ---\n\n"
        f"--- {ORCHESTRATOR_PATH} ---\n{orchestrator}\n--- END ORCHESTRATOR ---\n"
    )


def render_paste3(strategy_rows: list[dict]) -> str:
    core, council = [], []
    for s in strategy_rows:
        line = (
            f"- {s['name']} ({s.get('effectiveness', '?')}, {s.get('computational_cost', '?')}"
            + (", requires_multiple_runs" if s.get("requires_multiple_runs") else "")
            + f"): {s.get('implementation', s.get('description', ''))}."
            + f" Best for: {', '.join(s.get('best_for', []))}."
        )
        (council if "council" in s.get("tags", []) else core).append(line)

    return (
        "SEED SYSTEM BOOTSTRAP — PASTE 3 of 3: STRATEGY REGISTRY\n"
        'Paste last. Respond with "Strategy registry loaded ✓ — all 3 components active. State your goal."\n\n'
        f"--- {STRATEGY_REGISTRY} ---\n"
        f"CORE STRATEGIES:\n{'\n'.join(core) or '(none)'}\n\n"
        f"COUNCIL STRATEGIES:\n{'\n'.join(council) or '(none)'}\n"
        "--- END STRATEGIES ---\n"
    )


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_paths(root: Path, reg: Path) -> bool:
    ok = True
    checks: list[tuple[Path, str]] = [
        (reg,                      f"[dir] {reg}"),
        (reg / FACTORY_REGISTRY,   FACTORY_REGISTRY),
        (reg / STRATEGY_REGISTRY,  STRATEGY_REGISTRY),
        (root / PROFILE_PATH,      PROFILE_PATH),
        (root / ORCHESTRATOR_PATH, ORCHESTRATOR_PATH),
    ]
    for path, label in checks:
        exists = path.is_dir() if path == reg else path.exists()
        if not exists:
            print(f"  MISSING  {label}")
            ok = False
        else:
            size = "" if path == reg else f"({path.stat().st_size:>7,} B)  "
            print(f"  OK  {size}{label}")
    return ok


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",           default=".",               help="Repo root (default: .)")
    parser.add_argument("--registries-dir", default=REGISTRIES_SUBDIR, dest="registries_dir")
    parser.add_argument("--output",         default="bootstrap-out",   help="Output directory")
    parser.add_argument("--validate",       action="store_true",       help="Validate only; no output written")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    reg  = root / args.registries_dir

    print(f"Root:       {root}\nRegistries: {reg}\n")

    if not validate_paths(root, reg):
        raise SystemExit("\nValidation failed — fix missing files above before building.")

    factory_rows  = read_jsonl(reg / FACTORY_REGISTRY)
    strategy_rows = read_jsonl(reg / STRATEGY_REGISTRY)

    if args.validate:
        print(f"\nFactories : {len(factory_rows)}\nStrategies: {len(strategy_rows)}\nValidation passed.")
        return

    profile = (root / PROFILE_PATH).read_text(encoding="utf-8").strip()
    orch    = (root / ORCHESTRATOR_PATH).read_text(encoding="utf-8").strip()

    outdir = Path(args.output).expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    outputs = {
        "PASTE-1-registry.md":     render_paste1(factory_rows),
        "PASTE-2-orchestrator.md": render_paste2(profile, orch),
        "PASTE-3-strategies.md":   render_paste3(strategy_rows),
        "BOOTSTRAP-QUICKSTART.md": QUICKSTART,
    }

    print()
    for name, content in outputs.items():
        dest = outdir / name
        dest.write_text(content, encoding="utf-8")
        print(f"Wrote: {dest}")

    print(f"\nDone — {len(outputs)} files in {outdir}")


if __name__ == "__main__":
    main()
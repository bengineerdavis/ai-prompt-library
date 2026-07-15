#!/usr/bin/env -S python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "PyYAML>=6.0",
# ]
# ///

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "Error: PyYAML is required to run bundle.py.\n"
        "Install with:\n\n"
        "  python3 -m pip install PyYAML\n\n"
    )
    raise

def resolve_prompts_dir() -> Path:
    return Path(__file__).resolve().parent / "prompts"

def list_collections(prompts_dir: Path) -> None:
    print(f"Collections in {prompts_dir}:")
    print()
    for coll_dir in sorted(prompts_dir.iterdir()):
        if not coll_dir.is_dir():
            continue
        print(f" {coll_dir.name}/")
        bundle_files = sorted(
            list(coll_dir.glob("bundle.yaml")) +
            list(coll_dir.glob("bundle.*.yaml"))
        )
        for cfg in bundle_files:
            print(f"   {cfg.name}")

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="bundle.py",
        description="Assemble a paste-ready session prompt from a collection in the ai-prompt-library.",
    )
    parser.add_argument(
        "-p", "--collection",
        help="Collection name under prompts/ (e.g. panel-of-judges)",
    )
    parser.add_argument(
        "-c", "--config",
        help="Path to a bundle config YAML (relative or absolute)",
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (defaults to <collection>/generated/session.txt)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print files that would be included without writing output",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List collections and their bundle configs",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    prompts_dir = resolve_prompts_dir()

    if args.list:
        list_collections(prompts_dir)
        return

    if not args.collection and not args.config:
        sys.stderr.write("Error: no collection specified. Use -p or -c.\n")
        sys.exit(1)

    if args.collection:
        coll_dir = prompts_dir / args.collection
    else:
        # derive collection from config parent, like the bash script
        cfg_path = Path(args.config).resolve()
        coll_dir = cfg_path.parent

    if not coll_dir.is_dir():
        sys.stderr.write(f"Error: collection not found: {coll_dir}\n")
        sys.exit(1)

    # Default config discovery if none provided
    config_path = Path(args.config) if args.config else None
    if config_path is None:
        default_cfg = coll_dir / "bundle.yaml"
        if not default_cfg.is_file():
            bundle_candidates = sorted(coll_dir.glob("bundle.*.yaml"))
            default_cfg = bundle_candidates[0] if bundle_candidates else None
        if default_cfg is None:
            sys.stderr.write(f"Error: no bundle config found in {coll_dir}\n")
            sys.exit(1)
        config_path = default_cfg

    # Later commits: parse config and assemble files
    # For this commit, you can stub out:
    #   - detect flat vs structured, like bash script
    #   - print stub messages

    # Stub:
    print(f"Using collection: {coll_dir}")
    print(f"Using config: {config_path}")
    if args.dry_run:
        print("Dry run: parsing not yet implemented.")
    else:
        print("Bundling not yet implemented.")

if __name__ == "__main__":
    main()
#!/usr/bin/env -S uv run
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

def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Config {path} must be a YAML mapping at top level.")
    return data

def get_event(config: Dict[str, Any]) -> Dict[str, Any]:
    event = config.get("event") or {}
    if not isinstance(event, dict):
        raise ValueError("event must be a mapping.")
    name = event.get("name")
    if not name:
        raise ValueError("event.name is required.")
    return event

def get_participants(config: Dict[str, Any]) -> Dict[str, Any]:
    participants = config.get("participants") or {}
    if not isinstance(participants, dict):
        raise ValueError("participants must be a mapping if present.")
    roles = participants.get("roles") or []
    if roles is None:
        roles = []
    if not isinstance(roles, list):
        raise ValueError("participants.roles must be a list.")
    return {
        "roles": roles,
    }

def get_skills(config: Dict[str, Any]) -> List[str]:
    skills = config.get("skills") or []
    if skills is None:
        skills = []
    if not isinstance(skills, list):
        raise ValueError("skills must be a list if present.")
    return skills

def get_include(config: Dict[str, Any]) -> Dict[str, Any]:
    include = config.get("include") or {}
    if not isinstance(include, dict):
        raise ValueError("include must be a mapping if present.")
    context = include.get("context") or []
    if context is None:
        context = []
    if not isinstance(context, list):
        raise ValueError("include.context must be a list.")
    templates = bool(include.get("templates", False))
    factories = include.get("factories", False)
    roadmap = bool(include.get("roadmap", False))
    return {
        "context": context,
        "templates": templates,
        "factories": factories,
        "roadmap": roadmap,
    }

def merge_lists(base: List[str], override: List[str]) -> List[str]:
    seen = set()
    merged = []
    for item in base + override:
        if item not in seen:
            seen.add(item)
            merged.append(item)
    return merged

def merge_configs(defaults: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    merged = dict(defaults)
    merged.update(override)  # shallow override, then fix nested fields

    # Special handling for nested sections
    # event
    if "event" in defaults or "event" in override:
        event_base = defaults.get("event", {}) or {}
        event_override = override.get("event", {}) or {}
        event_merged = dict(event_base)
        event_merged.update(event_override)
        merged["event"] = event_merged

    # participants.roles
    part_base = defaults.get("participants", {}) or {}
    part_override = override.get("participants", {}) or {}
    roles_base = part_base.get("roles") or []
    roles_override = part_override.get("roles") or []
    merged_participants = dict(part_base)
    merged_participants.update(part_override)
    merged_participants["roles"] = merge_lists(roles_base, roles_override)
    merged["participants"] = merged_participants

    # skills
    skills_base = defaults.get("skills") or []
    skills_override = override.get("skills") or []
    merged["skills"] = merge_lists(skills_base, skills_override)

    # include.context
    include_base = defaults.get("include") or {}
    include_override = override.get("include") or {}
    include_merged = dict(include_base)
    include_merged.update(include_override)
    ctx_base = include_base.get("context") or []
    ctx_override = include_override.get("context") or []
    include_merged["context"] = merge_lists(ctx_base, ctx_override)
    merged["include"] = include_merged

    return merged

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

    config_raw = load_yaml(config_path)

    event = config_raw.get("event") or {}
    defaults_ref = event.get("defaults")
    if defaults_ref:
        defaults_path = (coll_dir / defaults_ref).resolve()
        if not defaults_path.is_file():
            raise FileNotFoundError(f"Defaults config not found: {defaults_path}")
        defaults_raw = load_yaml(defaults_path)
        config_merged = merge_configs(defaults_raw, config_raw)
    else:
        config_merged = config_raw

    event_conf = get_event(config_merged)
    participants_conf = get_participants(config_merged)
    skills_conf = get_skills(config_merged)
    include_conf = get_include(config_merged)

    # Stub:
    print(f"Using collection: {coll_dir}")
    print(f"Using config: {config_path}")
    if args.dry_run:
        print("Dry run: parsing not yet implemented.")
    else:
        print("Bundling not yet implemented.")

if __name__ == "__main__":
    main()
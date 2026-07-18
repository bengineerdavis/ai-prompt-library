#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "PyYAML>=6.0",
# ]
# ///

from __future__ import annotations

import argparse
import logging
import pprint
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import yaml
except ImportError:
    msg = [
        "Error: PyYAML is required to run bundle.py.",
        "Install with:",
        "",
        "  python3 -m pip install PyYAML",
        "",
    ]
    raise ImportError("\n".join(msg))

logger = logging.getLogger("bundle")


def configure_logging(debug: bool, dry_run: bool) -> None:
    level = logging.DEBUG if debug else logging.INFO if dry_run else logging.WARNING
    logging.basicConfig(level=level, format="[%(levelname)s] %(message)s")
    logger.setLevel(level)


def debug_print(enabled: bool, message: str) -> None:
    if enabled:
        print(f"[debug] {message}")
        logger.debug(message)


def info_print(message: str) -> None:
    print(message)
    logger.info(message)


def debug_dump(enabled: bool, label: str, value: Any) -> None:
    if enabled:
        formatted = pprint.pformat(value, sort_dicts=False)
        print(f"[debug] {label}:")
        for line in formatted.splitlines():
            print(f"[debug]   {line}")
        logger.debug("%s:\n%s", label, formatted)


def resolve_prompts_dir() -> Path:
    return Path(__file__).resolve().parent / "prompts"


def list_collections(prompts_dir: Path) -> None:
    info_print(f"Collections in {prompts_dir}:")
    print()
    for coll_dir in sorted(prompts_dir.iterdir()):
        if not coll_dir.is_dir():
            continue
        print(f"  {coll_dir.name}/")
        bundle_files = sorted(list(coll_dir.glob("bundle.yaml")) + list(coll_dir.glob("bundle.*.yaml")))
        for cfg in bundle_files:
            print(f"    {cfg.name}")


def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Config {path} must be a YAML mapping at top level.")
    return data


def get_event(config: Dict[str, Any], coll_dir: Path) -> Dict[str, Any]:
    event = config.get("event") or {}
    if not isinstance(event, dict):
        raise ValueError("event must be a mapping.")

    name = event.get("name")
    if not name:
        raise ValueError("event.name is required.")
    if not isinstance(name, str):
        raise ValueError("event.name must be a string.")

    event_dir = coll_dir / "events" / name
    if not event_dir.is_dir():
        raise FileNotFoundError(
            f"Event directory not found for event.name='{name}': {event_dir}"
        )

    resolved = dict(event)
    resolved["name"] = name
    return resolved


def get_participants(config: Dict[str, Any]) -> Dict[str, Any]:
    participants = config.get("participants") or {}
    if not isinstance(participants, dict):
        raise ValueError("participants must be a mapping if present.")
    roles = participants.get("roles") or []
    if roles is None:
        roles = []
    if not isinstance(roles, list):
        raise ValueError("participants.roles must be a list.")
    return {"roles": roles}


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
    factories = bool(include.get("factories", False))
    roadmap = bool(include.get("roadmap", False))
    return {
        "context": context,
        "templates": templates,
        "factories": factories,
        "roadmap": roadmap,
    }


def merge_lists(base: List[str], override: List[str]) -> List[str]:
    seen = set()
    merged: List[str] = []
    for item in base + override:
        if item not in seen:
            seen.add(item)
            merged.append(item)
    return merged


def merge_configs(defaults: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    merged = dict(defaults)
    merged.update(override)

    if "event" in defaults or "event" in override:
        event_base = defaults.get("event", {}) or {}
        event_override = override.get("event", {}) or {}
        event_merged = dict(event_base)
        event_merged.update(event_override)
        merged["event"] = event_merged

    part_base = defaults.get("participants", {}) or {}
    part_override = override.get("participants", {}) or {}
    roles_base = part_base.get("roles") or []
    roles_override = part_override.get("roles") or []
    merged_participants = dict(part_base)
    merged_participants.update(part_override)
    merged_participants["roles"] = merge_lists(roles_base, roles_override)
    merged["participants"] = merged_participants

    skills_base = defaults.get("skills") or []
    skills_override = override.get("skills") or []
    merged["skills"] = merge_lists(skills_base, skills_override)

    include_base = defaults.get("include") or {}
    include_override = override.get("include") or {}
    include_merged = dict(include_base)
    include_merged.update(include_override)
    ctx_base = include_base.get("context") or []
    ctx_override = include_override.get("context") or []
    include_merged["context"] = merge_lists(ctx_base, ctx_override)
    merged["include"] = include_merged

    return merged


def is_flat_collection(coll_dir: Path) -> bool:
    return not (coll_dir / "events").is_dir() and not (coll_dir / "roles").is_dir()


def find_role_file(coll_dir: Path, role: str) -> Optional[Path]:
    candidates = [
        coll_dir / "roles" / f"{role}.md",
        coll_dir / "roles" / "judges" / f"{role}.md",
        coll_dir / "roles" / "specialists" / f"{role}.md",
    ]
    for path in candidates:
        if path.is_file():
            return path
    return None


def find_skill_file(coll_dir: Path, skill: str) -> Optional[Path]:
    path = coll_dir / "skills" / f"{skill}.md"
    return path if path.is_file() else None


def resolve_context_files(coll_dir: Path, event_name: str, include_ctx: List[str]) -> List[Path]:
    files: List[Path] = []
    for item in include_ctx:
        if item == "handoff-context":
            event_local = coll_dir / "events" / event_name / "handoff-context.md"
            root = coll_dir / "handoff-context.md"
            if event_local.is_file():
                files.append(event_local)
            elif root.is_file():
                files.append(root)
            else:
                warning = f"Warning: no handoff-context found for {event_name}"
                sys.stderr.write(warning + "\n")
                logger.warning(warning)
        else:
            path = coll_dir / item
            if path.is_file():
                files.append(path)
            else:
                warning = f"Warning: include.context target not found: {path}"
                sys.stderr.write(warning + "\n")
                logger.warning(warning)

    seen = set()
    unique_files: List[Path] = []
    for f in files:
        key = f.resolve()
        if key not in seen:
            seen.add(key)
            unique_files.append(f)
    return unique_files


def config_selector_name(path: Path) -> str:
    name = path.name
    if name == "bundle.yaml":
        return "default"
    if name.startswith("bundle.") and name.endswith(".yaml"):
        return name[len("bundle."):-len(".yaml")]
    return path.stem


def scan_bundle_configs(coll_dir: Path, debug: bool = False) -> List[Tuple[Path, Optional[str]]]:
    candidates = sorted([p for p in coll_dir.glob("bundle*.yaml") if p.is_file()])
    scanned: List[Tuple[Path, Optional[str]]] = []
    for path in candidates:
        try:
            raw = load_yaml(path)
            event = raw.get("event") or {}
            event_name = event.get("name") if isinstance(event, dict) else None
            scanned.append((path, event_name if isinstance(event_name, str) else None))
        except Exception as exc:
            debug_print(debug, f"Skipping event extraction for {path.name}: {exc}")
            scanned.append((path, None))
    debug_dump(debug, "scanned bundle configs", [(p.name, e) for p, e in scanned])
    return scanned


def resolve_config_path(coll_dir: Path, config_arg: Optional[str], debug: bool = False) -> Path:
    if not config_arg:
        default_cfg = coll_dir / "bundle.yaml"
        if default_cfg.is_file():
            debug_print(debug, f"Using default config file: {default_cfg}")
            return default_cfg
        bundle_candidates = sorted(coll_dir.glob("bundle.*.yaml"))
        if bundle_candidates:
            debug_print(debug, f"No bundle.yaml found; using first bundle variant: {bundle_candidates[0]}")
            return bundle_candidates[0]
        raise FileNotFoundError(f"No bundle config found in {coll_dir}")

    raw = Path(config_arg)
    if raw.is_absolute() or raw.parent != Path('.'):
        resolved = raw.resolve()
        debug_print(debug, f"Resolved config from path input: {resolved}")
        return resolved

    direct = coll_dir / config_arg
    if direct.is_file():
        debug_print(debug, f"Resolved config from direct filename: {direct}")
        return direct

    if config_arg.endswith(".yaml"):
        candidate = coll_dir / config_arg
        if candidate.is_file():
            debug_print(debug, f"Resolved config from explicit yaml selector: {candidate}")
            return candidate
    else:
        exact_named = coll_dir / f"bundle.{config_arg}.yaml"
        if exact_named.is_file():
            debug_print(debug, f"Resolved config from shorthand selector: {exact_named}")
            return exact_named

        scanned = scan_bundle_configs(coll_dir, debug=debug)

        selector_matches = [path for path, _event_name in scanned if config_selector_name(path) == config_arg]
        debug_dump(debug, f"selector matches for {config_arg}", [p.name for p in selector_matches])
        if len(selector_matches) == 1:
            return selector_matches[0]
        if len(selector_matches) > 1:
            names = ", ".join(p.name for p in selector_matches)
            raise FileNotFoundError(f"Config selector '{config_arg}' is ambiguous: {names}")

        event_matches = [path for path, event_name in scanned if event_name == config_arg]
        debug_dump(debug, f"event matches for {config_arg}", [p.name for p in event_matches])
        if len(event_matches) == 1:
            debug_print(debug, f"Resolved config from unique event match: {event_matches[0]}")
            return event_matches[0]
        if len(event_matches) > 1:
            names = ", ".join(p.name for p in event_matches)
            raise FileNotFoundError(
                f"Config selector '{config_arg}' matches multiple configs for event '{config_arg}': {names}. Use a more specific config name."
            )

    raise FileNotFoundError(
        f"Bundle config not found for '{config_arg}' in {coll_dir}"
    )


def assemble_files(
    coll_dir: Path,
    event_conf: Dict[str, Any],
    participants_conf: Dict[str, Any],
    skills_conf: List[str],
    include_conf: Dict[str, Any],
) -> List[Path]:
    event_name = event_conf["name"]
    files: List[Path] = []

    charter = coll_dir / "context" / "charter.md"
    if not charter.is_file():
        charter = coll_dir / "context" / "meetings-charter.md"
    if charter.is_file():
        files.append(charter)
    else:
        warning = f"Warning: charter not found in {coll_dir}/context"
        sys.stderr.write(warning + "\n")
        logger.warning(warning)

    event_file = coll_dir / "events" / event_name / "event.md"
    if event_file.is_file():
        files.append(event_file)
    else:
        warning = f"Warning: event file not found: {event_file}"
        sys.stderr.write(warning + "\n")
        logger.warning(warning)

    prefs = coll_dir / "events" / event_name / "preferences.md"
    if prefs.is_file():
        files.append(prefs)

    files.extend(resolve_context_files(coll_dir, event_name, include_conf["context"]))

    missing_roles: List[str] = []
    for role in participants_conf["roles"]:
        rf = find_role_file(coll_dir, role)
        if rf:
            files.append(rf)
        else:
            missing_roles.append(role)
    if missing_roles:
        warning = f"Warning: role files not found: {', '.join(missing_roles)}"
        sys.stderr.write(warning + "\n")
        logger.warning(warning)

    missing_skills: List[str] = []
    for skill in skills_conf:
        sf = find_skill_file(coll_dir, skill)
        if sf:
            files.append(sf)
        else:
            missing_skills.append(skill)
    if missing_skills:
        warning = f"Warning: skill files not found: {', '.join(missing_skills)}"
        sys.stderr.write(warning + "\n")
        logger.warning(warning)

    session = coll_dir / "events" / event_name / "session-prompt.md"
    if not session.is_file():
        session = coll_dir / "templates" / "meeting-session-prompt.md"
    if session.is_file():
        files.append(session)

    seen = set()
    unique_files: List[Path] = []
    for f in files:
        key = f.resolve()
        if key not in seen:
            seen.add(key)
            unique_files.append(f)
    return unique_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="bundle.py",
        description="Assemble a paste-ready session prompt from a collection in the ai-prompt-library.",
    )
    parser.add_argument("-p", "--collection", help="Collection name under prompts/ (e.g. panel-of-judges)")
    parser.add_argument(
        "-c",
        "--config",
        help="Config selector: path, filename, config shorthand, or event name when it resolves to exactly one config",
    )
    parser.add_argument("-o", "--output", help="Output file path (defaults to /generated/session.txt)")
    parser.add_argument("--dry-run", action="store_true", help="Print files that would be included without writing output")
    parser.add_argument("--debug", action="store_true", help="Print detailed config and resolution debug information")
    parser.add_argument("--debug-files", action="store_true", help="Print detailed file assembly information")
    parser.add_argument("--list", action="store_true", help="List collections and their bundle configs")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prompts_dir = resolve_prompts_dir()
    debug_enabled = args.debug or args.debug_files
    configure_logging(debug=debug_enabled, dry_run=args.dry_run)

    if args.list:
        list_collections(prompts_dir)
        return

    if not args.collection and not args.config:
        sys.stderr.write("Error: no collection specified. Use -p or -c.\n")
        logger.error("No collection specified. Use -p or -c.")
        sys.exit(1)

    if args.collection:
        coll_dir = prompts_dir / args.collection
        debug_print(debug_enabled, f"Collection resolved from -p: {coll_dir}")
    elif args.config:
        raw = Path(args.config)
        if raw.is_absolute() or raw.parent != Path('.'):
            coll_dir = raw.resolve().parent
            debug_print(debug_enabled, f"Collection resolved from config path parent: {coll_dir}")
        else:
            sys.stderr.write("Error: --collection is required when --config is not a path.\n")
            logger.error("--collection is required when --config is not a path.")
            sys.exit(1)
    else:
        sys.stderr.write("Error: unable to determine collection.\n")
        logger.error("Unable to determine collection.")
        sys.exit(1)

    if not coll_dir.is_dir():
        sys.stderr.write(f"Error: collection not found: {coll_dir}\n")
        logger.error("Collection not found: %s", coll_dir)
        sys.exit(1)

    try:
        config_path = resolve_config_path(coll_dir, args.config, debug=debug_enabled)
    except FileNotFoundError as exc:
        sys.stderr.write(f"Error: {exc}\n")
        logger.error(str(exc))
        sys.exit(1)

    config_raw = load_yaml(config_path)
    debug_dump(debug_enabled, "config raw", config_raw)

    event_section = config_raw.get("event") or {}
    defaults_ref = event_section.get("defaults") if isinstance(event_section, dict) else None
    if defaults_ref:
        defaults_path = (coll_dir / defaults_ref).resolve()
        if not defaults_path.is_file():
            raise FileNotFoundError(f"Defaults config not found: {defaults_path}")
        defaults_raw = load_yaml(defaults_path)
        debug_dump(debug_enabled, "defaults raw", defaults_raw)
        config_merged = merge_configs(defaults_raw, config_raw)
    else:
        config_merged = config_raw
    debug_dump(debug_enabled, "config merged", config_merged)

    if is_flat_collection(coll_dir):
        main_prompt = None
        for candidate in [coll_dir / f"{coll_dir.name}.md", coll_dir / "main.md", *coll_dir.glob("*.md")]:
            if candidate.is_file():
                main_prompt = candidate
                break
        if main_prompt is None:
            sys.stderr.write(f"Error: no prompt file found in flat collection: {coll_dir}\n")
            logger.error("No prompt file found in flat collection: %s", coll_dir)
            sys.exit(1)
        out_dir = coll_dir / "generated"
        out_dir.mkdir(parents=True, exist_ok=True)
        output_path = Path(args.output) if args.output else out_dir / "session.txt"
        if args.dry_run:
            info_print("Dry run (flat collection):")
            info_print(f"Prompt file: {main_prompt}")
            info_print(f"Output: {output_path}")
            return
        output_path.write_text(main_prompt.read_text(encoding="utf-8"), encoding="utf-8")
        info_print(f"Copied → {output_path}")
        return

    event_conf = get_event(config_merged, coll_dir)
    participants_conf = get_participants(config_merged)
    skills_conf = get_skills(config_merged)
    include_conf = get_include(config_merged)

    debug_dump(debug_enabled, "event conf", event_conf)
    debug_dump(debug_enabled, "participants conf", participants_conf)
    debug_dump(debug_enabled, "skills conf", skills_conf)
    debug_dump(debug_enabled, "include conf", include_conf)

    files = assemble_files(coll_dir, event_conf, participants_conf, skills_conf, include_conf)
    if args.debug_files:
        debug_dump(True, "assembled files", [str(f) for f in files])

    out_dir = coll_dir / "generated"
    out_dir.mkdir(parents=True, exist_ok=True)
    output_path = Path(args.output) if args.output else out_dir / "session.txt"

    if args.dry_run:
        info_print(f"Dry run — {coll_dir.name} / {event_conf['name']}")
        info_print(f"Config selector: {args.config or '(default)'}")
        info_print(f"Resolved config: {config_path}")
        info_print(f"Resolved event: {event_conf['name']}")
        info_print(f"Resolved event dir: {coll_dir / 'events' / event_conf['name']}")
        print()
        base_dir = Path(__file__).resolve().parent
        for f in files:
            try:
                info_print(f"  {f.relative_to(base_dir)}")
            except ValueError:
                info_print(f"  {f}")
        print()
        info_print(f"Output: {output_path}")
        if debug_enabled:
            print()
            info_print("Debug mode enabled.")
        return

    info_print(f"Config selector: {args.config or '(default)'}")
    info_print(f"Resolved config: {config_path}")
    info_print(f"Resolved event: {event_conf['name']}")
    info_print(f"Resolved event dir: {coll_dir / 'events' / event_conf['name']}")

    with output_path.open("w", encoding="utf-8") as out:
        for f in files:
            out.write(f.read_text(encoding="utf-8"))
            out.write("\n\n")
    info_print(f"Bundled → {output_path}")


if __name__ == "__main__":
    main()
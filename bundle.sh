#!/usr/bin/env bash
# bundle.sh — assemble a paste-ready prompt from a collection in the ai-prompt-library
#
# This script lives at the library root and works with any collection that follows
# the prompt-templated-project-structure format:
#
#   prompts/<collection>/
#     context/                ← shared context files (charter, etc.)
#     roles/                  ← reusable role definitions
#       judges/
#       specialists/
#     events/<event>/         ← event-specific files
#     templates/              ← reusable templates
#     generated/              ← output lives here (safe to overwrite)
#
# For flat/single-prompt collections (e.g. interview-prep.md), the bundler
# just copies the file to generated/ without any assembly.
#
# Usage:
#   ./bundle.sh -c prompts/panel-of-judges/bundle.advisory-meeting.yaml
#   ./bundle.sh -p panel-of-judges                    # uses default config
#   ./bundle.sh -p panel-of-judges -e advisory-meeting -r chair facilitator pragmatist
#   ./bundle.sh -p panel-of-judges --dry-run
#   ./bundle.sh --list                                # list all collections + their configs
#   ./bundle.sh --help

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROMPTS_DIR="$SCRIPT_DIR/prompts"

COLLECTION=""
CONFIG=""
EVENT=""
ROLES=()
OUTPUT=""
DRY_RUN=false
LIST_MODE=false

# ── helpers ───────────────────────────────────────────────────────────────────

usage() {
  grep '^#' "$0" | sed 's/^# \{0,1\}//' | sed -n '2,30p'
  exit 0
}

warn() { echo "Warning: $*" >&2; }
die()  { echo "Error: $*" >&2; exit 1; }

# ── list all collections and their bundle configs ─────────────────────────────

list_collections() {
  echo "Collections in $PROMPTS_DIR:"
  echo ""
  for dir in "$PROMPTS_DIR"/*/; do
    name="$(basename "$dir")"
    [[ -d "$dir" ]] || continue
    echo "  $name/"
    for cfg in "$dir"bundle.*.yaml "$dir"bundle.yaml; do
      [[ -f "$cfg" ]] && echo "    $(basename "$cfg")"
    done
  done
  exit 0
}

# ── parse a yaml bundle config (event: + roles: list only) ───────────────────

parse_config() {
  local file="$1"
  local in_roles=false

  while IFS= read -r line; do
    line="${line#"${line%%[![:space:]]*}"}"
    line="${line%"${line##*[![:space:]]}"}"
    [[ -z "$line" || "$line" == \#* ]] && continue

    if [[ "$line" == "event:"* ]]; then
      EVENT="${line#event:}"
      EVENT="${EVENT#"${EVENT%%[![:space:]]*}"}"
      in_roles=false
    elif [[ "$line" == "roles:" ]]; then
      in_roles=true
    elif [[ "$in_roles" == true && "$line" == "- "* ]]; then
      ROLES+=("${line#- }")
    else
      in_roles=false
    fi
  done < "$file"
}

# ── find a role file anywhere in the collection's role tree ──────────────────

find_role() {
  local base="$1"
  local role="$2"
  for dir in \
    "$base/roles" \
    "$base/roles/judges" \
    "$base/roles/specialists"; do
    local f="$dir/$role.md"
    [[ -f "$f" ]] && echo "$f" && return
  done
  echo ""
}

# ── parse args ────────────────────────────────────────────────────────────────

while [[ $# -gt 0 ]]; do
  case "$1" in
    -c|--config)     CONFIG="$2"; shift 2 ;;
    -p|--collection) COLLECTION="$2"; shift 2 ;;
    -e|--event)      EVENT="$2"; shift 2 ;;
    -r|--roles)      shift; while [[ $# -gt 0 && "$1" != -* ]]; do ROLES+=("$1"); shift; done ;;
    -o|--output)     OUTPUT="$2"; shift 2 ;;
    --dry-run)       DRY_RUN=true; shift ;;
    --list)          LIST_MODE=true; shift ;;
    --help|-h)       usage ;;
    *) die "Unknown option: $1. Run ./bundle.sh --help for usage." ;;
  esac
done

[[ "$LIST_MODE" == true ]] && list_collections

# ── resolve collection path ───────────────────────────────────────────────────

# if a config path was given, derive collection from its parent directory name
if [[ -n "$CONFIG" && -z "$COLLECTION" ]]; then
  COLLECTION="$(basename "$(dirname "$CONFIG")")"
fi

[[ -z "$COLLECTION" ]] && die "No collection specified. Use -p <collection> or -c <config>."

COLL_DIR="$PROMPTS_DIR/$COLLECTION"
[[ -d "$COLL_DIR" ]] || die "Collection not found: $COLL_DIR"

# ── find default config if none given ────────────────────────────────────────

if [[ -z "$CONFIG" && -z "$EVENT" ]]; then
  DEFAULT_CFG="$COLL_DIR/bundle.yaml"
  if [[ ! -f "$DEFAULT_CFG" ]]; then
    DEFAULT_CFG="$(ls "$COLL_DIR"/bundle.*.yaml 2>/dev/null | head -1 || true)"
  fi
  [[ -n "$DEFAULT_CFG" && -f "$DEFAULT_CFG" ]] && CONFIG="$DEFAULT_CFG"
fi

# ── parse config ──────────────────────────────────────────────────────────────

[[ -n "$CONFIG" ]] && parse_config "$CONFIG"

# ── detect collection type ────────────────────────────────────────────────────

# flat = no events/ and no roles/ — treat as single-prompt passthrough
IS_FLAT=false
if [[ ! -d "$COLL_DIR/events" && ! -d "$COLL_DIR/roles" ]]; then
  IS_FLAT=true
fi

# ── flat collection: copy the main prompt file to generated/ ─────────────────

if [[ "$IS_FLAT" == true ]]; then
  MAIN_PROMPT=""
  for candidate in \
    "$COLL_DIR/$COLLECTION.md" \
    "$COLL_DIR/main.md" \
    "$COLL_DIR"/*.md; do
    [[ -f "$candidate" ]] && MAIN_PROMPT="$candidate" && break
  done

  [[ -z "$MAIN_PROMPT" ]] && die "No prompt file found in flat collection: $COLL_DIR"

  OUT_DIR="$COLL_DIR/generated"
  mkdir -p "$OUT_DIR"
  [[ -z "$OUTPUT" ]] && OUTPUT="$OUT_DIR/session.txt"

  if [[ "$DRY_RUN" == true ]]; then
    echo "Dry run (flat collection):"
    echo "  ${MAIN_PROMPT#"$SCRIPT_DIR/"}"
    echo "Output: ${OUTPUT#"$SCRIPT_DIR/"}"
    exit 0
  fi

  cp "$MAIN_PROMPT" "$OUTPUT"
  echo "Copied → ${OUTPUT#"$SCRIPT_DIR/"}"
  exit 0
fi

# ── structured collection ─────────────────────────────────────────────────────

[[ -z "$EVENT" ]]        && die "No event specified. Use -e <event> or a config file."
[[ ${#ROLES[@]} -eq 0 ]] && die "No roles specified. Use -r <roles...> or a config file."

FILES=()

# 1. charter — prefer new name, fall back to original
CHARTER="$COLL_DIR/context/charter.md"
[[ ! -f "$CHARTER" ]] && CHARTER="$COLL_DIR/context/meetings-charter.md"
if [[ -f "$CHARTER" ]]; then
  FILES+=("$CHARTER")
else
  warn "charter not found in $COLL_DIR/context/"
fi

# 2. event definition
EVENT_FILE="$COLL_DIR/events/$EVENT/event.md"
if [[ -f "$EVENT_FILE" ]]; then
  FILES+=("$EVENT_FILE")
else
  warn "event file not found: $EVENT_FILE"
fi

# 3. event preferences (optional)
PREFS="$COLL_DIR/events/$EVENT/preferences.md"
[[ -f "$PREFS" ]] && FILES+=("$PREFS")

# 4. roles
MISSING=()
for role in "${ROLES[@]}"; do
  rf="$(find_role "$COLL_DIR" "$role")"
  if [[ -n "$rf" ]]; then
    FILES+=("$rf")
  else
    MISSING+=("$role")
  fi
done
[[ ${#MISSING[@]} -gt 0 ]] && warn "role files not found: ${MISSING[*]}"

# 5. session prompt — prefer event-local, fall back to templates/
SESSION="$COLL_DIR/events/$EVENT/session-prompt.md"
[[ ! -f "$SESSION" ]] && SESSION="$COLL_DIR/templates/meeting-session-prompt.md"
[[ -f "$SESSION" ]] && FILES+=("$SESSION")

# ── output path ───────────────────────────────────────────────────────────────

OUT_DIR="$COLL_DIR/generated"
mkdir -p "$OUT_DIR"
[[ -z "$OUTPUT" ]] && OUTPUT="$OUT_DIR/session.txt"

# ── dry run ───────────────────────────────────────────────────────────────────

if [[ "$DRY_RUN" == true ]]; then
  echo "Dry run — $COLLECTION / $EVENT"
  echo ""
  for f in "${FILES[@]}"; do
    echo "  ${f#"$SCRIPT_DIR/"}"
  done
  echo ""
  echo "Output: ${OUTPUT#"$SCRIPT_DIR/"}"
  exit 0
fi

# ── write output ──────────────────────────────────────────────────────────────

> "$OUTPUT"
for f in "${FILES[@]}"; do
  cat "$f" >> "$OUTPUT"
  printf "\n\n---\n\n" >> "$OUTPUT"
done

echo "Bundled ${#FILES[@]} files → ${OUTPUT#"$SCRIPT_DIR/"}"

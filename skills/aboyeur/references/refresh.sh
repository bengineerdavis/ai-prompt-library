#!/usr/bin/env bash
# Refresh the mise documentation snapshot this skill reads from.
#
# Usage: refresh.sh [REF]
#
#   REF  a mise git tag (v2026.9.9) or branch (main). Defaults to the tag
#        matching the installed `mise --version`, falling back to main when
#        that tag does not exist.
#
# Sources, in preference order:
#   1. raw.githubusercontent.com/jdx/mise/<REF>/docs/**  — the markdown the
#      docs site is built from, so the snapshot is the editing source.
#   2. https://mise.jdx.dev/llms.txt — the site's own page index, saved as
#      llms-index.txt so fresh page discovery does not depend on this list.
#
# Writes PROVENANCE.md recording ref, date, and every file's source URL.
# Fails loudly on the first page that cannot be fetched.
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
docs_dir="$here/docs"
index_file="$here/llms-index.txt"
provenance="$here/PROVENANCE.md"

ref="${1:-}"
if [ -z "$ref" ]; then
  version="$(mise --version 2>/dev/null | awk '{print $1}' || true)"
  ref="main"
  if [ -n "$version" ] && curl -fsSI -o /dev/null \
      "https://raw.githubusercontent.com/jdx/mise/v${version}/README.md"; then
    ref="v${version}"
  fi
fi
base="https://raw.githubusercontent.com/jdx/mise/${ref}"

# site path -> local path under docs/. Index pages live as index.md in-repo.
pages="
configuration.md
getting-started.md
dev-tools/index.md
dev-tools/mise-lock.md
tasks/index.md
tasks/toml-tasks.md
tasks/file-tasks.md
tasks/task-configuration.md
tasks/running-tasks.md
environments/index.md
configuration/environments.md
configuration/settings.md
configuration/vars.md
configuration/project-diagnostics.md
bootstrap.md
bootstrap/packages/index.md
continuous-integration.md
cli/trust.md
templates.md
"

rm -rf "$docs_dir"
mkdir -p "$docs_dir"

{
  printf '# Provenance\n\n'
  printf -- '- Fetched: %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf -- '- Ref: `%s`\n' "$ref"
  printf -- '- Local mise at fetch time: `%s`\n' \
    "$(mise --version 2>/dev/null || echo 'not installed')"
  printf -- '- Repo: https://github.com/jdx/mise\n\n'
  printf -- '| File | Source |\n|---|---|\n'
} > "$provenance"

fetch() { # fetch <repo-path> <dest>
  mkdir -p "$(dirname "$2")"
  curl -fsS "$base/$1" -o "$2"
  printf '| `%s` | `%s` |\n' "${2#"$here"/}" "$base/$1" >> "$provenance"
}

for page in $pages; do
  fetch "docs/$page" "$docs_dir/$page"
done
fetch "schema/mise.json" "$docs_dir/schema-mise.json"

curl -fsS https://mise.jdx.dev/llms.txt -o "$index_file"
printf '| `llms-index.txt` | https://mise.jdx.dev/llms.txt |\n' >> "$provenance"

n_pages="$(echo "$pages" | wc -w | tr -d ' ')"
printf 'refreshed %s files from %s\n' "$((n_pages + 2))" "$ref"

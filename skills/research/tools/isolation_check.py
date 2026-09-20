#!/usr/bin/env python3
"""isolation_check — the post-hoc provenance gate for web-briefed analysts.

The research swarm's web-isolation contract says a web-briefed analyst gets
no repository contents and cites no local paths. With the current dispatch
machinery the contract cannot be enforced preventively (subagents run
inside the repo with file tools), so this gate enforces it detectively:
run it on every web-briefed analyst's return before the sources registry
compiles. Exit 0 = clean. Exit 1 = local-path citations found — the run
records the isolation breach per the evidence rule (disclose and
reclassify, never silently keep), and the offending citations are listed.

Detection is conservative: a hit is (a) any path under the supplied repo
root, (b) any `~/`-rooted path, or (c) any repo-relative file path bearing
a known config/doc/code extension with an optional `:line` suffix. URLs are
never flagged (a scheme-gated match), so `github.com/owner/repo/docs` does
not trip it.

Usage:
    isolation_check.py ANALYST_OUTPUT_FILE --repo-root /path/to/repo
    cat output.txt | isolation_check.py - --repo-root /path/to/repo

Exit codes: 0 clean · 1 local-path citations found · 2 usage error.
Stdlib only, no arguments beyond those — this is a gate, not a framework.
"""

from __future__ import annotations

import argparse
import re
import sys

# File-extension-bearing file paths, optional :line suffix. Zero-or-more
# directory segments: real analyst outputs cite bare filenames with line
# numbers (`TASKS.md:741`) as often as full relative paths
# (`dotfiles/apps/x/tasks/install.yaml:252`) — the pilot's actual breach
# taught the pattern. Conservative extension list keeps prose safe.
RELATIVE_PATH_RE = re.compile(
    r"(?<![\w/.~-])"  # not preceded by a path character (avoids mid-token hits)
    r"(?:[\w.-]+/)*[\w.-]+\.(?:ya?ml|md|py|toml|sh|json|cfg|ini|txt)"
    r"(?::\d+)?"
    r"(?![\w/])"
)

# `~/`-rooted paths (resolved-never-written still leaks them).
TILDE_PATH_RE = re.compile(r"(?<![\w/.~-])~(?:/[\w.-]+)+/?(?::\d+)?")

URL_SCHEME_RE = re.compile(r"https?://\S*")


def _strip_urls(line: str) -> str:
    """Blank out URL bodies so repo-ish strings inside links never trip."""
    return URL_SCHEME_RE.sub(" ", line)


def find_local_citations(text: str, repo_root: str | None) -> list[tuple[int, str, str]]:
    """Return (line_number, matched_text, kind) for every local-path hit."""
    hits: list[tuple[int, str, str]] = []
    root_re = (
        re.compile(re.escape(repo_root.rstrip("/")) + r"[/\w.-]+")
        if repo_root
        else None
    )
    for lineno, raw in enumerate(text.splitlines(), start=1):
        scrubbed = _strip_urls(raw)
        for kind, regex in (
            ("repo-root path", root_re),
            ("home-relative path", TILDE_PATH_RE),
            ("repo-relative file path", RELATIVE_PATH_RE),
        ):
            if regex is None:
                continue
            for match in regex.finditer(scrubbed):
                hits.append((lineno, match.group(0), kind))
    return hits


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("output", help="analyst output file, or '-' for stdin")
    parser.add_argument("--repo-root", default=None, help="repo root to deny")
    args = parser.parse_args(argv)

    if args.output == "-":
        text = sys.stdin.read()
    else:
        try:
            text = Path(args.output).read_text(encoding="utf-8")
        except OSError as exc:
            print(f"isolation_check: cannot read {args.output}: {exc}", file=sys.stderr)
            return 2
        if args.output.endswith(".py"):
            print(
                "isolation_check: refusing to scan a .py file — scan analyst "
                "OUTPUT, not code",
                file=sys.stderr,
            )
            return 2

    hits = find_local_citations(text, args.repo_root)
    if not hits:
        print("isolation_check: clean — no local-path citations in web-briefed output")
        return 0

    print(
        f"isolation_check: {len(hits)} local-path citation(s) — ISOLATION "
        "BREACH; disclose and reclassify per the evidence rule, never "
        "silently keep:"
    )
    for lineno, matched, kind in hits:
        print(f"  line {lineno}: [{kind}] {matched}")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

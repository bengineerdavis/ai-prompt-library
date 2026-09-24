# GitHub CLI read-command permission proposal

- Owner: `gh-research`.
- Research session: 2026-09-23–24. Recorded: 2026-09-24.
- Verified CLI: `gh 2.101.0 (2026-09-15)`.
- Decision: **GLOBAL PROPOSAL ONLY — not adopted configuration**.

## Recommendation and boundary

Auto-allow the named remote read-oriented commands below. Keep all `gh api`
calls and other `gh` operations on `ask`. Use an exact `gh --version` allow.

This is a convenience policy for trusted workflows. It selects read-oriented
built-ins; it does not guarantee that arbitrary matching shell text is harmless.
It is neither a sandbox nor a public-only or no-local-effects policy.
Credentials can permit private reads. Browsers, pagers, redirections, caches,
and environment-sensitive behavior remain relevant.

Adopt the family wildcards only if those residuals are acceptable. If public-only
access or no local effects is required, retain approval for the families.
Those stronger boundaries need controls beyond native command globs.

## Evidence and deployment status

The research inspected the installed version, root and family help, every listed
subcommand's help, and the environment and formatting help topics. Public,
version-pinned CLI source corroborates the flags and behavior described here.
The examples below are hypothetical strings, not executed GitHub operations.
No installs, GitHub mutations, authentication changes, or API cache calls ran.

OpenCode findings come from its public permission documentation, schema, and
`dev` source inspected during the session. These are mutable references, not a
verified match to the deployed OpenCode binary. The JSONC shape agrees with the
published schema; the merged deployment has not been validated.

The coordinator's read-only source-template review reported a possible duplicate
trailing `"*"` fallback. Treat this as an application blocker until resolved.
Duplicate keys and parser behavior can change effective order; a later catch-all
`ask` can shadow every allow. This record does not assert the template's final
parsed order. Access to deployed `~/.config/opencode` was unavailable, so no live
permission behavior is claimed. No live, chezmoi-managed, or project
configuration was edited. This README records the proposal only.

## Verified allow/ask matrix

| Form                                             | Proposal                  | Qualification                                                              |
| ------------------------------------------------ | ------------------------- | -------------------------------------------------------------------------- |
| Exact `gh --version`                             | Allow                     | Version reporting needs no suffix wildcard.                                |
| `gh search code/commits/issues/prs/repos`        | Allow named families      | These are the five registered search subcommands in 2.101.0.               |
| `gh issue list/view/status`                      | Allow named families      | Repository and credential scope can include private data.                  |
| `gh pr list/view/status/checks/diff`             | Allow named families      | Do not broaden to `gh pr *`; that includes mutation and checkout commands. |
| Supported `--json`, `--jq/-q`, `--template/-t`   | Allow within boundary     | In-process formatting; jq can read environment variables.                  |
| Supported `--web/-w`                             | Included in family allows | Accept browser launch, or retain approval for the affected families.       |
| Any `gh api` form                                | Ask                       | Includes apparent GETs, GraphQL queries, pagination, and help.             |
| Other commands, aliases, and unmatched spellings | Ask                       | No broad `gh`, issue, PR, or search allow.                                 |

## Copy-ready global proposal

This JSONC illustrates the proposed order. Before applying it globally, merge
the entries with existing rules rather than replacing unrelated settings.
Keep one general fallback first, then the broad `gh` fallback, then named allows.

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "bash": {
      "*": "ask",
      "gh *": "ask",

      "gh --version": "allow",

      "gh search code *": "allow",
      "gh search commits *": "allow",
      "gh search issues *": "allow",
      "gh search prs *": "allow",
      "gh search repos *": "allow",

      "gh issue list *": "allow",
      "gh issue view *": "allow",
      "gh issue status *": "allow",

      "gh pr list *": "allow",
      "gh pr view *": "allow",
      "gh pr status *": "allow",
      "gh pr checks *": "allow",
      "gh pr diff *": "allow",

      "gh api *": "ask"
    }
  }
}
```

OpenCode uses the **last matching rule**, not the most specific rule. Its reviewed
matcher makes a trailing ` *` optional, covering bare commands and arguments.
These are string globs, not regular expressions or semantic argument validation.
Shell parsing identifies commands but does not validate HTTP methods or GraphQL.

The requested `gh --version *` is narrowed to `gh --version` because extra text
is unnecessary. The wildcard also matches suffixes such as `> version.txt`.
Exact matching avoids that expansion; other forms fall back to approval.
Do not append another catch-all or a broad `gh` allow after these entries.

## Supported flags and accepted residuals

- All listed search and issue commands, plus PR list/view/status/checks, support
  `--json`. Their `--jq` and `--template` flags require it. PR diff has none of
  these formatting flags. The embedded jq and Go templates do not run an
  external jq or shell. However, jq's environment loader exposes process
  variables, potentially including secrets; it is not limited to response data.
- Search commands, issue list/view, and PR list/view/checks/diff support `--web`.
  `GH_BROWSER`/`BROWSER` select the launcher. Combined short flags complicate
  substring exclusions; a simple `*-w*` exception is incomplete.
- `GH_PAGER`/`PAGER` can select a subprocess. Non-TTY output normally skips it,
  but `GH_FORCE_TTY` can alter that behavior. Repository discovery can invoke
  git. Feature-detection caches and notifier/telemetry behavior also prevent a
  blanket no-local-effects claim, even without explicit API caching.
- PR checks supports `--required`, `--watch`, `--interval`, and `--fail-fast`.
  These inspect or poll checks, not rerun them. Polling consumes time and quota.
- PR diff supports `--patch`, `--name-only`, `--color`, and `--exclude/-e`.
  Patch output does not apply changes. `--allow-escape-sequences` bypasses output
  protection. **Neither PR diff nor API has `--output` or `-o` in 2.101.0.**
- Repository URLs, `-R [HOST/]OWNER/REPO` on issue/PR commands, `GH_REPO`, and
  `GH_HOST` affect scope. Search filters such as `--visibility public`, where
  supported, are useful selections, not a public-only authorization boundary.

## Why every API call retains approval

The default method is GET. Adding `-f/--raw-field`, `-F/--field`, or `--input`
changes it to POST unless a method was explicitly supplied. Repeated
`-X/--method` flags assign the same string: **the last occurrence wins**,
including mixed short and long forms. Native OpenCode permissions offer no
method-aware API wildcard. `gh api -X GET *` does not guarantee GET.

`-F key=@file` reads local content; `--input file` reads a request body, and `-`
can select stdin. Explicit GET does not remove disclosure concerns. `--cache`
writes response-cache files. Shell redirection can write output without an
`--output` flag. `-H` means header, not hostname; headers can override
authorization and include gh-specific cache controls.

`--hostname` selects the GitHub host, but absolute endpoint URLs are used as-is.
Relative API paths are deliberately accepted verbatim. `--paginate` follows
REST next-page links or GraphQL cursors; it is not a safety validator.

GitHub GraphQL queries and mutations normally both use POST. The `graphql`
endpoint or a field named `query` does not establish read-only behavior.
Even a document beginning with `query` can contain a mutation selected through
`operationName`. Inspect the complete operation and any file/stdin body.
Do not classify GraphQL strings or inputs by a command-prefix glob.

For example, this complete public GET is an approval candidate, not an allow
pattern. It remains `ask` under the proposal and was not executed:

```sh
gh api --hostname github.com --method GET repos/cli/cli/issues
```

## Adversarial match review

These benign hypothetical examples establish source-derived matches and
consequences, not observed network results or deployed permission decisions.
`example.invalid` and sample filenames are placeholders. No example ran.

| Rule being assessed              | Matching command string                                                    | Consequence                                                        |
| -------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Rejected `gh api -X GET *`       | `gh api -X GET https://example.invalid/items --method PATCH -f label=demo` | Final method is PATCH, not GET.                                    |
| Rejected `gh api --method GET *` | `gh api --method GET https://example.invalid/items -XPOST -f label=demo`   | Attached short syntax also overrides the method.                   |
| Rejected `gh api repos/*`        | `gh api repos/example/demo/issues -f title=demo`                           | Fields select POST by default.                                     |
| Rejected `gh api -X GET *`       | `gh api -X GET https://example.invalid/items -F data=@sample.json`         | Reads the sample file and places its contents in the query string. |
| Rejected `gh api graphql *`      | `gh api graphql --input sample-request.json`                               | The unseen body could select a query or mutation.                  |
| Proposed `gh issue view *`       | `gh issue view 1 -cw`                                                      | Combined flags select comments and browser launch.                 |
| Proposed `gh pr view *`          | `gh pr view 1 --json title --jq 'env.GH_REPO'`                             | Reads an environment variable, not just PR data.                   |
| Proposed `gh pr diff *`          | `gh pr diff 1 > review.patch`                                              | Redirection writes a local file.                                   |
| Proposed `gh issue view *`       | `gh issue view 1 -R example/private-demo`                                  | Could read a private repository if authorized.                     |

## Validation and freshness before adoption

1. Before applying, confirm the installed gh and OpenCode versions and current
   help. Recheck the matcher, shell parser, and permission evaluator for that
   OpenCode release; `dev` links alone do not establish deployed behavior.
1. Resolve the reported duplicate fallback. Validate JSONC against the schema
   and inspect merged rule order, project/agent overrides, and session approvals.
   Confirm auto-approve mode is off so `ask` remains meaningful.
1. Validate both expected allows and counterexamples as strings without executing
   their operations. Include bare commands, arguments, exact version matching,
   API fallback, method overrides, combined flags, and redirections.
1. If configuration is later changed, quit and restart OpenCode. Check effective
   permissions in the new session before relying on the proposal.
1. Repeat this review after gh/OpenCode changes, configuration merges, or relevant
   credential, host, pager, browser, or environment changes. Reassess new flags.

## Sources

CLI implementation links are pinned to the verified release or its dependencies.
OpenCode documentation, schema, and `dev` source can change after this record.

- [CLI dependency versions](https://github.com/cli/cli/blob/v2.101.0/go.mod), [search registration](https://github.com/cli/cli/blob/v2.101.0/pkg/cmd/search/search.go), and [PR diff flags](https://github.com/cli/cli/blob/v2.101.0/pkg/cmd/pr/diff/diff.go).
- [API flags and method selection](https://github.com/cli/cli/blob/v2.101.0/pkg/cmd/api/api.go), [HTTP paths and headers](https://github.com/cli/cli/blob/v2.101.0/pkg/cmd/api/http.go), [field parsing](https://github.com/cli/cli/blob/v2.101.0/pkg/cmd/api/fields.go), and [pagination](https://github.com/cli/cli/blob/v2.101.0/pkg/cmd/api/pagination.go).
- [Repeated string-flag assignment](https://github.com/spf13/pflag/blob/v1.0.10/string.go), [JSON flags](https://github.com/cli/cli/blob/v2.101.0/pkg/cmdutil/json_flags.go), [jq environment access](https://github.com/cli/go-gh/blob/v2.16.1/pkg/jq/jq.go), and [template functions](https://github.com/cli/go-gh/blob/v2.16.1/pkg/template/template.go).
- [Pager execution](https://github.com/cli/cli/blob/v2.101.0/pkg/iostreams/iostreams.go), [issue view and feature detection](https://github.com/cli/cli/blob/v2.101.0/pkg/cmd/issue/view/view.go), [PR checks](https://github.com/cli/cli/blob/v2.101.0/pkg/cmd/pr/checks/checks.go), and [cache files and headers](https://github.com/cli/go-gh/blob/v2.16.1/pkg/api/cache.go).
- [GitHub GraphQL calls, queries, and mutations](https://docs.github.com/en/graphql/guides/forming-calls-with-graphql).
- [OpenCode permissions](https://opencode.ai/docs/permissions/), [schema](https://opencode.ai/config.json), [last-match evaluation](https://github.com/anomalyco/opencode/blob/dev/packages/opencode/src/permission/index.ts), [glob matcher](https://github.com/anomalyco/opencode/blob/dev/packages/core/src/util/wildcard.ts), and [shell command collection](https://github.com/anomalyco/opencode/blob/dev/packages/opencode/src/tool/shell.ts).

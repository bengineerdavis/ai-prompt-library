# binned handoff — building the escalation script

The spec and evals in this directory are done. The script itself is yours to
generate, because `binned` prompts interactively and runs a three-model judge
pass that a non-TTY tool call cannot drive reliably.

Everything below has been run and verified on this machine.

## Runtime assets already in place

```
~/.config/support-escalation/system.txt    the escalation prompt (derived from spec.md)
~/.config/support-escalation/schema.json   the 15-field JSON schema
```

## The verified core command

This exact invocation works today. It is the thing to hand `binned`:

```
llm -n -m granite4.1:30b-q4_K_M \
  -s "$(cat ~/.config/support-escalation/system.txt)" \
  --schema ~/.config/support-escalation/schema.json
```

`-n` is `--no-log` and is **not optional**. Without it `llm` writes full prompt
and response bodies to its local database indefinitely, which is retention no
policy layer authorises for customer material. See the constraint in `spec.md`.

## Generate the script

```
eval "$(ollama-role env)"   # so the generated script can see OLLAMA_ROLE_*

binned "read a support thread from stdin and produce a support escalation
ticket: pipe the thread into llm -n with the system prompt at
~/.config/support-escalation/system.txt and the JSON schema at
~/.config/support-escalation/schema.json, then render the resulting JSON
into a markdown ticket. Default to the local model from ollama-role;
fall back only to the ZDR endpoint in OLLAMA_ROLE_ESCALATE with
-o provider '{\"zdr\":true}'; emit JSON with --json, markdown otherwise."
```

`binned` will detect the `llm` call and ask which model alias the generated
script should use — that is the prompt you need to be present for. Add `-y` to
accept defaults non-interactively if you would rather not sit through it.

Render the markdown from the JSON **in the script**, not with a second model
call. Behaviour `dual-output-format` requires the two to carry identical field
values, and deriving one from the other is the only way to guarantee that.

## Two findings that need your decision

### 1. The `long` role is the wrong model for this task

`spec.md` requires resolving the model through `ollama-role` rather than
hardcoding a tag, which is correct in principle. But `ollama-role get long`
currently returns `granite4:32b-a9b-h`, and on the `attachments-thread` fixture
that model marked `rowan-session.har` as `available: true` when the HAR contents
were never supplied, and never asked for them. That is the exact fabrication
class the spec forbids, and it fails
`attachment-and-investigation-history-intake`.

`granite4.1:30b-q4_K_M` marked it `available: false` and asked for it.

Same fixture, both models:

Same fixture, one trial each — **provisional, pending re-measurement**:

|                                      | `granite4:32b-a9b-h` (`long`) | `granite4.1:30b-q4_K_M` |
| ------------------------------------ | ----------------------------- | ----------------------- |
| HAR marked unavailable               | ✗ claimed it had it           | ✓                       |
| Asked for the HAR                    | ✗                             | ✓                       |
| Caught the abandoned relay-log check | ✓                             | ✓                       |
| Wall clock                           | *not measured*                | *not measured*          |

> **Timings withheld.** The machine was serving other model workloads during
> these runs, so the wall-clock figures collected were contention noise, not a
> property of either model. Re-measure on a quiet machine before using speed to
> decide anything. `bin/model-bench` and `bin/ollama-bench` exist for this.

The accuracy column is unaffected by contention — it is what the models emitted,
not how fast — but it is still a single trial per model on a single fixture.
Treat the direction as a signal, not a settled result.

That direction: 4.1 errs conservatively (marking a supplied file unavailable)
where the `long` model errs permissively (claiming a file it does not have). For
an escalation ticket the conservative failure is the right one.

**Suggested fix:** add a dedicated role to the ollama manifest pinned to
`granite4.1:30b-q4_K_M` rather than pointing this script at `long`, so the
manifest stays the single place a model swap happens.

### 2. `available` is under-specified

Neither model handled `sentry.client.config.ts` the way the spec intends. Its
contents *were* inline in the thread; 4.1 still marked it `available: false`.
The spec says `available` means "whether its contents were actually available to
the agent", which does not clearly separate *named in the thread*, *inlined in
the thread*, and *a real file on disk*. Worth tightening in `spec.md` before the
evals start depending on the distinction.

## Running the evals

`.skillet.yaml` pins `claude:sonnet` as the default harness. `codex` 0.150.1 is
now installed as the second harness for the cross-run protocol — skillet 1.7.0
grades each case with the same model that ran it, so a single run always
self-grades. See the comment block in `.skillet.yaml` for the two commands.

```
skillet validate      # spec grammar + eval coverage — currently clean
skillet eval --dry    # flags vacuous checks before spending tokens
```

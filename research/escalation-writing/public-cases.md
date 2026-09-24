# Public escalation-writing case evidence

Research session: 2026-09-23–24; recorded 2026-09-24.

## Scope and interpretation

These eight closed public bug reports are fallback evidence, not proven
Support-to-Engineering escalations or examples of the user's writing. The Sentry
cases came from reproduction-related searches and purposive contrasts. The pytest
and VS Code pairs came from the research handoff and were checked against their
full visible issue threads. Selection is neither random nor representative.

All 58 visible issue comments were read, including bots and later replies. Linked
pull requests and selected review comments were checked where cited. This does not
mean every linked artifact, private discussion, or entire pull-request review was
read. Maintainer/contributor associations help identify participants but do not
prove employment or the full support workflow.

“Supplied facts” below means the current body, not a reconstructed original.
Historical body/comment revisions were not retrieved. GitHub reports body edits for
C02, C03, and C08; the other five return no `lastEditedAt` value. That metadata is
not an independent audit of submission history. Later comments cannot be credited
as facts available at the initial handoff.

Counts describe visible request-bearing comments, not individual questions or a
quality score. Useful diagnostic experiments and legitimate technical disagreement
are not writing defects. No request, no reply, and a closed state each fail to
establish success on their own. See [licenses and reuse](sources.md#s18-case-corpus-and-licenses)
and the [evaluation method](README.md#evaluate-future-historical-cases).

## C01. Sentry Python 4764

[Requests to fastapi-mcp hangs if Sentry is enabled](https://github.com/getsentry/sentry-python/issues/4764)
concerns FastAPI/MCP request-body consumption. Five visible issue comments.

- **Supplied facts:** SDK 2.36.0, SaaS, a standalone reproducer, ordered setup/run
  instructions, exact transport and endpoint, logs, expected behavior, and a
  working comparison entry point without Sentry.
- **First engineering reply:** A member
  [confirmed reproduction on 2.37.0](https://github.com/getsentry/sentry-python/issues/4764#issuecomment-3266661775).
  No preliminary information request appears.
- **Follow-up:** Zero information-request comments among the four human replies.
  Engineering [provided a workaround](https://github.com/getsentry/sentry-python/issues/4764#issuecomment-3269100784)
  and [explained consumption of the ASGI receive stream](https://github.com/getsentry/sentry-python/issues/4764#issuecomment-3285660175).
  A [later explanation](https://github.com/getsentry/sentry-python/issues/4764#issuecomment-3319282311)
  described compatibility problems with proposed fixes.
- **Outcome:** Initially closed in September 2025, then reopened. Early
  [PR 4832](https://github.com/getsentry/sentry-python/pull/4832) closed unmerged.
  [PR 7487](https://github.com/getsentry/sentry-python/pull/7487) explicitly referenced
  this issue and merged on 2026-09-14 as
  [`4d2663e`](https://github.com/getsentry/sentry-python/commit/4d2663e0899d4ac370506040650c09fa2932438c),
  changing body handling to cached attributes. The issue closed again on 2026-09-16.
- **Ambiguity:** No reporter confirmation of the workaround or final fix is visible.
  A merged change is not verification in the reporter's deployment.
- **Portable lesson:** A runnable case and working control can enable immediate
  engineering diagnosis. Good evidence cannot remove compatibility trade-offs.

## C02. Sentry JavaScript 21915

[wrapFetchWithSentry's injected trace meta tags break React 19 document hydration](https://github.com/getsentry/sentry-javascript/issues/21915)
concerns TanStack Start and injected HTML. Ten visible issue comments.

- **Supplied facts:** SDK/framework versions, initialization snippets, production
  steps, valid-DSN prerequisite, exact error, controlled HTML changes, expected/actual
  behavior, and a proposed mechanism/fix. The body was edited after the first reply.
- **First engineering replies:** A member
  [acknowledged the report](https://github.com/getsentry/sentry-javascript/issues/21915#issuecomment-4864785649),
  then [requested a reproducer after failing to reproduce](https://github.com/getsentry/sentry-javascript/issues/21915#issuecomment-4866767005).
- **Missing information:** The reporter
  [supplied a repository and commands](https://github.com/getsentry/sentry-javascript/issues/21915#issuecomment-4870806474),
  adding the inline-script-in-head prerequisite that exposed the failure in a small app.
- **Repeated or misunderstood information:** Another member
  [requested OS, package-manager version, and debug output](https://github.com/getsentry/sentry-javascript/issues/21915#issuecomment-4890087105).
  The reporter [supplied versions and clarified the browser-console observation](https://github.com/getsentry/sentry-javascript/issues/21915#issuecomment-4898970976),
  repeating production/browser instructions. The member
  [acknowledged the misunderstanding and confirmed reproduction](https://github.com/getsentry/sentry-javascript/issues/21915#issuecomment-4900739985).
  Two request-bearing comments are visible, not two proven preventable author omissions.
- **Outcome:** [PR 22004](https://github.com/getsentry/sentry-javascript/pull/22004)
  merged as [`7df7f30`](https://github.com/getsentry/sentry-javascript/commit/7df7f30c4583433180845f4092bdbbf4d4c7ca1a),
  removing whitespace between injected tags. A
  [release notice](https://github.com/getsentry/sentry-javascript/issues/21915#issuecomment-4905367416)
  identifies 10.64.0. No post-upgrade reporter verification appears.
- **Portable lesson:** State hidden prerequisites and where to observe the error.
  Separate missing setup evidence from a recipient's misreading.

## C03. Sentry JavaScript 18860

[require-in-the-middle interferes with ESM](https://github.com/getsentry/sentry-javascript/issues/18860)
concerns Bun, dynamic imports, and production execution. Four visible issue comments.

- **Supplied facts:** Ubuntu 24.04, Bun/PM2, dynamic imports, production-only
  occurrence, expected absence of an exception, and a Sentry issue link. Exact
  versions, initialization code, a runnable case, and inline error details are absent.
  The body was edited before the first maintainer reply. The Sentry artifact was not accessed.
- **First engineering reply:** A member
  [asked about repository choice, versions, and reproduction/setup](https://github.com/getsentry/sentry-javascript/issues/18860#issuecomment-3760027381).
- **Response and repetition:** The reporter
  [answered only the routing point](https://github.com/getsentry/sentry-javascript/issues/18860#issuecomment-3760027399).
  After transfer, the member
  [repeated the technical requests](https://github.com/getsentry/sentry-javascript/issues/18860#issuecomment-3760029154).
  Two request-bearing comments repeat substantially the same missing information.
  No visible reply supplies it.
- **Outcome:** Closed on 2026-01-16 with `NOT_PLANNED`; current labels include
  unreproducible and won't-do states. No diagnosis or fix appears. Closure events
  lack an explanatory closing comment, so the closer's exact reasoning is unproven.
- **Portable lesson:** A routing correction does not answer diagnostic questions.
  Address each outstanding request or say what cannot be supplied.

## C04. Sentry Python 2116

[SDK causes significant performance issue](https://github.com/getsentry/sentry-python/issues/2116)
concerns Starlette/ASGI overhead. Twelve visible issue comments, including late additions.

- **Supplied facts:** SDK 1.22.2, dependency versions, initialization code, Locust
  testing, throughput/latency comparisons, sampling discussion, and a tentative
  fixed-overhead hypothesis.
- **First engineering reply:** A member
  [asked which sampling rates were zero and what deterioration meant](https://github.com/getsentry/sentry-python/issues/2116#issuecomment-1549731807).
  The reporter [answered both](https://github.com/getsentry/sentry-python/issues/2116#issuecomment-1549822117).
- **Further requests:** A contributor
  [requested a demo project](https://github.com/getsentry/sentry-python/issues/2116#issuecomment-1550909573);
  a member later [requested the startup command/configuration](https://github.com/getsentry/sentry-python/issues/2116#issuecomment-1557056415).
  These are three request-bearing comments concerning the original report. The
  original reporter did not visibly answer the latter two.
- **Separate report:** A Django participant prompted an additional version/causality
  clarification. A member [split that report out](https://github.com/getsentry/sentry-python/issues/2116#issuecomment-1551279503).
  Its proposed workaround is not diagnosis of the original Starlette case.
- **Outcome:** A bot closed the issue on 2023-09-13 after inactivity. API reason
  `COMPLETED` does not establish a fix. Another participant
  [supplied a reproducer in 2025](https://github.com/getsentry/sentry-python/issues/2116#issuecomment-3118125944);
  another [added measurements in 2026](https://github.com/getsentry/sentry-python/issues/2116#issuecomment-5565265173).
  Neither proves resolution of the original case.
- **Portable lesson:** Measurements need exact experimental conditions. A dependency
  list cannot replace configuration, launch command, workload, and a comparison.

## C05. pytest 12863

[parametrize decorator does not work when placed above staticmethod](https://github.com/pytest-dev/pytest/issues/12863)
concerns decorator order and test collection. Five visible issue comments.

- **Supplied facts:** Small contrasting examples differing in decorator order,
  collection command/output, pytest 8.3.3, and desired behavior or an explicit error.
  A checked environment checkbox is not evidence of an OS value in the body.
- **First substantive engineering follow-up:** After an initial volunteer reply,
  a contributor [linked an attempted fix](https://github.com/pytest-dev/pytest/issues/12863#issuecomment-2512656288).
  No missing-information request appears in the issue thread.
- **Additional evidence:** The reporter
  [added a classmethod contrast and warning output](https://github.com/pytest-dev/pytest/issues/12863#issuecomment-2513942292).
  The contributor [extended the fix](https://github.com/pytest-dev/pytest/issues/12863#issuecomment-2518264137).
  A maintainer's [PR review explained descriptor unwrapping](https://github.com/pytest-dev/pytest/pull/13022#discussion_r1872244665).
  That implementation review is not a request for omitted reporter facts.
- **Outcome:** [PR 13022](https://github.com/pytest-dev/pytest/pull/13022) merged on
  2024-12-14 as [`6dd3fff`](https://github.com/pytest-dev/pytest/commit/6dd3fffde19c16b3164cbbe6fafdfdc4f41d09df),
  closing the issue. No separate release/deployment verification was checked.
- **Portable lesson:** A controlled contrast can communicate a defect more clearly
  than a large environment inventory. Additional cases can legitimately broaden a fix.

## C06. pytest 12865

[Getting an AttributeError: \_instance when running tests on CircleCI](https://github.com/pytest-dev/pytest/issues/12865)
concerns setup/teardown and rerun-plugin behavior. Eight visible issue comments.

- **Supplied facts:** Upgrade versions, stack trace, shared local/CI dependency
  versions, and a local-pass/CI-fail contrast. Actual plugin/command differences
  were not fully captured by the claim of equivalent environments.
- **First maintainer reply:** A member
  [asked for a specific test and plugins, while separating two hypotheses](https://github.com/pytest-dev/pytest/issues/12865#issuecomment-2400505564).
  The reporter [supplied a reduced test, plugin list, and observations](https://github.com/pytest-dev/pytest/issues/12865#issuecomment-2401190580).
- **Diagnostic follow-up:** A member
  [asked about running without rerunfailures](https://github.com/pytest-dev/pytest/issues/12865#issuecomment-2401451833).
  The reporter disclosed CI-only reruns; another member
  [suggested matching the local configuration](https://github.com/pytest-dev/pytest/issues/12865#issuecomment-2401471416).
  The reporter [reproduced locally with reruns](https://github.com/pytest-dev/pytest/issues/12865#issuecomment-2401574890).
  These three request/suggestion comments include useful experiments, not just omitted facts.
- **Outcome:** The reporter [closed as likely plugin compatibility](https://github.com/pytest-dev/pytest/issues/12865#issuecomment-2402256786)
  on 2024-10-09. No verified fix or definitive causal isolation appears in this thread.
- **Portable lesson:** Compare actual commands and enabled plugins, not only version
  lists. Preserve “likely” when diagnosis remains provisional.

## C07. VS Code 208321

[Opening recent from macOS dock creates a duplicate workspace](https://github.com/microsoft/vscode/issues/208321)
concerns Unicode normalization and workspace identity. Eight visible issue comments.

- **Supplied facts:** VS Code 1.87.2, macOS Sonoma, extensions-disabled result,
  UI steps, screenshot, and a distinction between shared files and separate workspace state.
- **First engineering reply:** The maintainer
  [requested one storage key and named the extraction command](https://github.com/microsoft/vscode/issues/208321#issuecomment-2013222131).
  The reporter [supplied differently encoded URI values](https://github.com/microsoft/vscode/issues/208321#issuecomment-2013230765).
  This record does not reproduce the personal path.
- **Further request:** The maintainer
  [asked how each path was opened](https://github.com/microsoft/vscode/issues/208321#issuecomment-2013240202).
  The reporter [restated the UI sequence with additional comparison detail](https://github.com/microsoft/vscode/issues/208321#issuecomment-2013252447).
  Two diagnostic request comments are visible; the second partly repeats body information.
- **Outcome:** The maintainer
  [confirmed Unicode normalization as the cause](https://github.com/microsoft/vscode/issues/208321#issuecomment-2014484605).
  [PR 208372](https://github.com/microsoft/vscode/pull/208372) merged on 2024-03-22 as
  [`1e38af3`](https://github.com/microsoft/vscode/commit/1e38af34241f3909b7687d98a90cc7aeda31b7b3).
  No post-release verification was checked.
- **Portable lesson:** A narrowly requested artifact can be more useful than a
  large log dump. Useful engineering questions can turn a clear report into a diagnosis.

## C08. VS Code 208551

[ctrl+backspace does not delete entire word in integrated terminal](https://github.com/microsoft/vscode/issues/208551)
concerns Windows terminal input and ConPTY. Six visible issue comments.

- **Supplied facts:** VS Code/Windows versions, shell-specific symptoms, keybinding
  logs, expected comparison with Windows Terminal, and a prior issue reference.
  The body was edited before the first engineering reply.
- **First engineering reply:** A collaborator
  [requested a settings-isolation test](https://github.com/microsoft/vscode/issues/208551#issuecomment-2018870447).
  The reporter [supplied fresh-profile and multiple-machine results](https://github.com/microsoft/vscode/issues/208551#issuecomment-2019144433).
- **Further request and dispute:** The collaborator
  [asked for an external-terminal comparison](https://github.com/microsoft/vscode/issues/208551#issuecomment-2020605783),
  then [closed as upstream and repeated the comparison request](https://github.com/microsoft/vscode/issues/208551#issuecomment-2020693501)
  before the reporter answered. The reporter
  [answered and objected to the timing and certainty](https://github.com/microsoft/vscode/issues/208551#issuecomment-2021223161).
- **Technical response:** Another maintainer
  [explained Windows/ConPTY versions and input handling](https://github.com/microsoft/vscode/issues/208551#issuecomment-2021261568).
  The explanation distinguishes their Windows 11 tests from the reporter's Windows
  10 environment and retains uncertainty about the comparison.
- **Outcome:** Closed as upstream on 2024-03-26. No verified fix for the reporter
  appears. Two distinct diagnostic requests and a repeated request at closure are
  visible; the disagreement is not reducible to missing reporter investigation.
- **Portable lesson:** Explain ownership decisions and uncertainty. Response timing
  and legitimate technical disagreement confound any “pushback” measure.

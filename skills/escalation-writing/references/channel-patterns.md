# Channel patterns

Use these as flexible structures, not an intake form. Follow an applicable
destination template. Omit irrelevant sections and avoid displaying empty fields
unless a required template needs an explicit "unknown" or "not applicable."

Before drafting each message, identify who receives it, whose behalf you write on,
what the recipient already knows, and what the message needs to accomplish now.
Use the supplied context rather than asking these as intake questions. The same
Intercom conversation can need a customer reply and a different internal note.

## Choose the ask

| Purpose                            | What the recipient needs to decide or do                                  |
| ---------------------------------- | ------------------------------------------------------------------------- |
| Defect or regression investigation | Confirm or diagnose the observed difference from expected behavior.       |
| Diagnostic help                    | Identify the next useful check when Support cannot isolate the cause.     |
| Intended-behavior clarification    | Explain the expected behavior or resolve a documentation ambiguity.       |
| Operational action                 | Perform or assess a specific action beyond Support's access or authority. |
| Ownership or priority help         | Identify the responsible team or assess the documented impact.            |

These purposes may overlap. They do not establish a severity scheme or an owner.
For suspected incidents or security issues, use the applicable organization process
rather than delay it while trying to complete a routine bug template.

## GitHub engineering ticket

A durable ticket lets the recipient begin without rereading the customer thread.

1. **Title:** Name the affected operation and observed symptom. Avoid declaring an
   unconfirmed cause or prescribing a solution in the title.
1. **Opening:** State the problem, concrete impact, and requested action or decision.
1. **Expected and actual behavior:** Identify the expectation's source when needed.
1. **Relevant context:** Include versions, configuration, timeframe with timezone
   when known, scope, and prerequisites that discriminate between explanations.
1. **Reproduction or occurrence evidence:** Give steps and observation location.
   For intermittent or production-only issues, give available occurrence evidence
   and explain the reproduction limit.
1. **Investigation:** Summarize meaningful checks, comparisons, results, and limits.
   Link accessible supporting material and include permitted decisive excerpts.
1. **Remaining need:** State consequential unknowns and the bounded engineering ask.

Do not equate a long inventory with completeness. A command difference can matter
more than a dependency dump. Mark an unavailable attachment as unreviewed, not
absent. Do not claim a proposed test has been performed.

For a follow-up comment, state the new evidence, what it changes, and the remaining
ask. Address outstanding requests with an answer, an explicit limitation, or a
recorded next action. Do not regenerate the full initial report.

## Slack coordination

Lead with the request and the intended recipient if known. Add enough impact and
evidence to explain the request, plus the existing canonical ticket or thread link.
Keep uncertainty needed for the decision in the message, not only behind the link.

Keep diagnostic detail in the thread or durable record. If the supplied discussion
changes ownership, status, or next action elsewhere, flag that record update for
the sender. Do not claim to notify anyone or synchronize records just by drafting.

**Synthetic example:**

> Could you help identify the next check for these export failures? The customer
> reports failures in production; Support reproduced the same error in staging.
> The cause is still unknown. The investigation is in the linked ticket.

Use a real supplied link in the final draft when available. Do not manufacture a
ticket URL or imply this synthetic example is a real customer case.

## Intercom internal note

Transfer the current situation, relevant customer impact, investigation results,
evidence access, open requests, and accepted responsibilities. Distinguish what
Support requested from what Engineering agreed to do. Record the supported next
action, dependencies, and available follow-up options as internal plans, not
customer promises. Preserve an earlier customer commitment even if the sender
needs to reassess how to fulfill or address it. Mark that need explicitly.

An internal note is not automatically suitable for every internal audience. Check
visibility and permissions for the intended readers, including external guests or
shared ticket views.

## Intercom customer reply

Explain the current status and useful next step in language suited to the customer.
Write from the sender's support role, using the customer's context and what they
already know. Technical detail is appropriate when it helps that reader.

- Acknowledge the concrete impact without assuming feelings.
- State what is known, what remains unresolved, and what action has actually begun.
- Give a supported workaround, including its relevant limits, when one exists.
- Ask only for evidence the customer can usefully provide; explain how and why.
- Explain the next requested or confirmed action and material dependencies. Do
  not imply that a request has been accepted or that the customer owns an internal
  task. If the next step is undecided, do not invent one.
- Make or repeat a promise only when the sender currently confirms they can
  guarantee that specific action and any timing. Check the scope against known
  dependencies. A recorded promise, target, or estimate does not establish this.
  A guaranteed status message does not guarantee progress or a fix.
- Without that assurance, use known status and the relevant next step. Do not
  substitute "soon," "as soon as we hear back," or "we'll keep you updated" for an
  unsupported deadline; these also set expectations the sender may not meet.

Exclude internal routing disputes, private links, blame, and speculative causes
that would mislead the customer. Preserve uncertainty without copying an internal
diagnostic checklist into the reply.

Keep follow-up choices open without becoming evasive. An internal note can retain
possible paths, such as checking a confirmed result or seeking more diagnostic
information, when the context supports them. The customer reply should explain
what is known or requested now rather than promise which path will succeed.

If an earlier customer deadline is not currently guaranteed, flag it in a brief
author note. It remains an obligation to honor or address; omission from a new
message does not cancel it. Ask only if handling that obligation is necessary to
draft the requested reply accurately.

**Synthetic example:** Support reproduced a seven-day export failure. Daily
exports work, but the customer says combining them is impractical. Engineering
has been asked to trace the failed request and assess another workaround; nobody
has accepted the work. No follow-up timing is currently guaranteed.

> We reproduced the timeout on your seven-day export. Since combining daily
> exports isn't practical for your report, we've asked Engineering to trace the
> failed request and check for another workaround. We don't yet have a confirmed
> cause or a fix.

## Keep related drafts aligned

Check each requested draft against the same evidence, then its own audience:

- Did "reported" become "reproduced," or "requested" become "underway"?
- Did a merged change become a released or verified fix?
- Did one draft invent an owner, deadline, workaround, or commitment?
- Does each message address its own recipient from the sender's role?
- Is a next step accurately described as requested, accepted, or underway?
- Did an internal target or old promise become a fresh customer guarantee?
- Did removing a date leave an unsupported event-based or open-ended promise?
- Does a shorter message still preserve decision-critical conditions?
- Does a new decision require an update to a supplied linked record?

Keep any needed author note separate and brief. Do not repeat this checklist in
every response.

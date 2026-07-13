# panel-of-judges — Advisory Meeting Engagement Index

**Engagement type:** Financial advisory
**Principal location:** Concord, CA (Bay Area)
**Collection version:** 1.0

---

## Quick start

```bash
# Default advisory meeting
./bundle.sh -c bundle.advisory-meeting.yaml

# With deep researcher
./bundle.sh -c bundle.advisory-meeting-with-research.yaml

# Dry run (preview files without writing)
./bundle.sh -c bundle.advisory-meeting.yaml --dry-run
```

Output is written to `generated/session.txt`. Paste into your LLM chat session.

---

## File map

```
.
├── bundle.advisory-meeting.yaml              ← default session config
├── bundle.advisory-meeting-with-research.yaml
├── context/
│   └── charter.md                            ← shared collection principles
├── data/
│   └── minutes/                              ← per-session meeting records
│       ├── README.md
│       └── meeting-001-minutes.md
├── events/
│   └── advisory-meeting/
│       ├── event.md                          ← event rules, flow, authority
│       ├── meeting-template.md               ← blank minutes template
│       ├── preferences.md                    ← principal preferences (portable)
│       └── session-prompt.md                 ← session bootstrap
├── generated/
│   └── session.txt                           ← bundler output (safe to overwrite)
├── handoff-context.md                        ← cross-session continuity summary
├── index.md                                  ← this file
├── roles/
│   ├── advisors.md                           ← all 4 domain advisor definitions
│   ├── chair.md
│   ├── facilitator.md
│   ├── note-taker.md
│   ├── recruiter.md
│   ├── judges/
│   │   ├── minimalist.md
│   │   └── systems-thinker.md
│   └── specialists/
│       ├── deep-researcher.md
│       ├── negotiator.md
│       ├── people-expert.md
│       └── pragmatist.md
└── templates/
    ├── event-template.md
    ├── role-invocation-template.md
    └── role-template.md
```

---

## Advisor roster for this engagement

| Slug | Domain | Real-world status |
|---|---|---|
| `wealth-planner` | Holistic planning, buckets, allocation | TBD — to be recruited |
| `tax-strategist` | Tax minimization, contribution ordering | TBD — to be recruited |
| `college-advisor` | Education funding, 529s, per-child policy | TBD — to be recruited |
| `ai-tech-advisor` | AI/tech sleeve, thematic risk | TBD — to be recruited |

All definitions are in `roles/advisors.md`.

---

## Key design decisions

- **Preferences are portable.** `events/advisory-meeting/preferences.md` carries all principal context. Role and event files stay generic.
- **`advisors.md` is a single file** containing all 4 domain advisor role definitions for this engagement. Use the role template (`templates/role-template.md`) to split or add roles as needed.
- **Social Security is excluded** from all planning in this engagement. This is noted in preferences.md and session-prompt.md.
- **No exact financial figures** are used in sessions. All numbers are generalized ranges or percentages.

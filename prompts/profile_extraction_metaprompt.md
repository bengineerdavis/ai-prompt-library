# PROFILE EXTRACTION META-PROMPT
## Extract Candidate Data from Conversations with AI SaaS Services

**Version**: 1.0  
**Use Case**: Build or update persistent job research profiles from Perplexity, Claude, ChatGPT, or similar AI services  
**Output Format**: Markdown (compatible with ben_job_research_profile.md template)

---

## PURPOSE

This meta-prompt helps you systematically extract and structure personal/professional context from:
- Interviews with AI assistants (Perplexity, Claude, ChatGPT)
- Conversations about job opportunities, career goals, technical skills
- Background research on your own experience and aspirations

**Result**: A clean, exportable markdown file you can reuse across AI services.

---

## EXTRACTION WORKFLOW

### Step 1: Initialize the Extraction Context

When starting a research session with an AI SaaS service, provide this preamble:

```
I'm Ben Davis, a Technical Support Engineer at Airbyte preparing for senior engineering roles.
I have a persistent job research profile I use across AI services for consistency.

Before we dive into [JOB POSTING / RESEARCH GOAL], let me share my profile context:

[PASTE: ben_job_research_profile.md]

Now, as we work through this research, I want to extract or update my profile based on insights 
that emerge. At the end of our session, please compile an updated PROFILE SNAPSHOT that I can 
use for future requests.

Ready to proceed?
```

---

### Step 2: During Research Session - Flag Extraction Points

As you and the AI work through job research, company analysis, or career planning, 
**flag moments where profile data emerges**:

**Examples of Extraction Triggers**:

- **Career insight**: "You mentioned wanting to move from support to infrastructure. That's a clear vector."
  - **Extract to**: Career Vector section
  - **Example flag**: `[EXTRACT: Career Vector]`

- **Technical skill discovery**: "I see you have deep Kubernetes experience from Airbyte. That's a strength signal."
  - **Extract to**: Technical Profile > Strong Expertise
  - **Example flag**: `[EXTRACT: Kubernetes → Strong Expertise]`

- **Gap identification**: "Rust is on your learning path. When's that becoming production-ready?"
  - **Extract to**: Learning/Growth Areas
  - **Example flag**: `[EXTRACT: Rust → Learning Areas, ETA unknown]`

- **Constraint update**: "Your electrical capacity limits multi-GPU setups. That's a real constraint."
  - **Extract to**: Hardware Stack / Constraints
  - **Example flag**: `[EXTRACT: Electrical constraint → Constraints section]`

- **Priority reweighting**: "Actually, open-source culture matters more to me than I thought."
  - **Extract to**: Job Posting Evaluation Priorities
  - **Example flag**: `[EXTRACT: Reweight Phase 3 (Market) signals]`

---

### Step 3: End-of-Session Extraction Request

At the end of your research session, ask the AI:

```
EXTRACTION REQUEST:

Based on our conversation, please provide an updated PROFILE SNAPSHOT 
in the following format (use [NO CHANGE] if a field wasn't discussed):

────────────────────────────────────────────────────────────────

CORE CONTEXT UPDATES:
- Current Role: [SAME/UPDATED]
- Years in Tech: [SAME/UPDATED]
- Target Companies: [SAME/UPDATED]
- Target Roles: [SAME/UPDATED]
- Target Seniority: [SAME/UPDATED]
- Career Vector: [SAME/UPDATED]
- Geographic Preference: [SAME/UPDATED]
- Constraints: [SAME/UPDATED]

TECHNICAL PROFILE UPDATES:
- New Strong Expertise areas: [LIST/NONE]
- Promoted from Learning to Strong: [LIST/NONE]
- New Learning Areas: [LIST/NONE]
- Updated Hardware Stack: [DESCRIBE/NONE]

CAREER SIGNALS UPDATES:
- New Strengths: [LIST/NONE]
- Newly Identified Gaps: [LIST/NONE]

JOB EVALUATION PRIORITY REWEIGHTING:
- Priority 1 (Career Vector): [OLD %] → [NEW %]
- Priority 2 (Technical Depth): [OLD %] → [NEW %]
- Priority 3 (Company Momentum): [OLD %] → [NEW %]
- Priority 4 (Remote/Flexibility): [OLD %] → [NEW %]
- Rationale: [BRIEF EXPLANATION]

FOLLOW-UP QUESTIONS ADDITIONS:
- New always-ask questions: [LIST/NONE]
- New context-specific triggers: [LIST/NONE]

NEXT UPDATE TRIGGERS TO TRACK:
- Upcoming milestones: [LIST/NONE]
- Timeline for Rust production-ready: [DATE/TBD]
- Timeline for open-source contributions: [DATE/TBD]

────────────────────────────────────────────────────────────────

Also provide a quick "EXTRACTION SUMMARY" in 2–3 sentences of what changed and why.
```

---

## STRUCTURED EXTRACTION TEMPLATE

### Use this when the AI provides extraction snapshots:

```markdown
# EXTRACTED UPDATES FROM SESSION: [DATE]

## EXTRACTION SUMMARY
[2–3 sentence summary of what changed and why]

## CHANGES BY SECTION

### CORE CONTEXT
[List each field with OLD → NEW or NO CHANGE]

### TECHNICAL PROFILE
- **New Strong Expertise**: [list]
- **Promoted from Learning**: [list]
- **New Learning Areas**: [list]

### CAREER SIGNALS
- **New Strengths**: [list]
- **New Gaps**: [list]

### JOB EVALUATION PRIORITIES
[Old weights] → [New weights]
- Reasoning: [brief explanation]

### FOLLOW-UP QUESTIONS
- **New Always-Ask**: [list]
- **New Context-Specific**: [list with triggers]

### NEXT STEPS / MILESTONES
[List any new action items or timeline updates]

---

**Extracted by**: [AI Service Name, e.g., "Perplexity Research Session"]  
**Session Date**: [DATE]  
**Ready to merge?**: [Y/N] [Link to discussion/approval]
```

---

## MULTI-SESSION PROFILE BUILDING

### Workflow for Building Profile Across Multiple Sessions:

**Session 1** (Perplexity - Company Research)
```
- Share profile
- Research company X, role Y
- Request extraction snapshot at end
- Save output to: extracts/session_1_perplexity_company_research.md
```

**Session 2** (Claude - Career Planning)
```
- Reference previous session extracts
- Discuss career vector and growth path
- Request extraction snapshot
- Save output to: extracts/session_2_claude_career_planning.md
```

**Session 3** (ChatGPT - Interview Prep)
```
- Load all previous session extracts as context
- Prep for target company interview
- Request extraction snapshot (new follow-up questions, etc.)
- Save output to: extracts/session_3_chatgpt_interview_prep.md
```

**Consolidation** (Manual merge every 4–6 weeks)
```
- Review all session extracts: extracts/*.md
- Identify consistent themes (e.g., "infrastructure focus mentioned 3x")
- Merge non-conflicting updates back to: ben_job_research_profile.md
- Flag conflicts (e.g., "Priority reweighting differs; need to decide")
- Update metadata: Last Updated, Version
```

---

## EXTRACTION CONFIDENCE MARKERS

When extracting data, use these confidence markers to indicate certainty:

```
✓ [~90–100%] High confidence
  - Explicitly stated multiple times
  - Consistent across sessions
  - Example: "My target is Netflix senior IC roles"

⚠ [~50–75%]  Medium confidence
  - Stated once or inferred from context
  - Needs validation
  - Example: "Rust will be production-ready in 2–3 months (estimated)"

✗ [~0–40%]   Low confidence / Assumption
  - Inferred or unclear
  - Flagged for future confirmation
  - Example: "Might be interested in manager track (not explicitly stated)"
```

Include these in extraction snapshots so you know what's solid vs. what needs confirmation.

---

## MULTI-AI SERVICE CONSISTENCY CHECKS

If you use multiple AI services (Perplexity + Claude + ChatGPT), watch for:

**Consistency Issues** (flag if they differ):
- Career vector interpretation (support → infra vs. support → manager?)
- Priority weighting differences
- Technical skill assessments

**How to resolve**:
1. Document which service made which assessment
2. Note any contradictions
3. In next session, explicitly ask: "I've seen these two interpretations; which is more accurate?"
4. Update profile to reflect your clarification

**Example**:
```
Perplexity said: "Career vector is support → infrastructure (40% priority)"
Claude said: "Career vector is support → platform engineering (45% priority)"

My clarification: "Actually, both paths interest me equally; they're part of the same 
infrastructure/platform stack. Weight together at 40–45%."

Updated profile accordingly.
```

---

## EXPORTING AND VERSIONING

### When to Export Updated Profile:

After each consolidation cycle (every 4–6 weeks):

```bash
# Backup current version
cp ben_job_research_profile.md ben_job_research_profile_v1.0.md

# Update version header in main file
# Edit: **Version**: 1.0 → **Version**: 1.1

# Update metadata
# Edit: **Last Updated**: 2025-12-02 → **Last Updated**: 2025-12-15

# Commit to repo with message
git add ben_job_research_profile.md
git commit -m "Profile v1.1: Updated career vector + added Rust learning timeline"
```

### Distribution:

- **Local**: Keep master copy in project repo
- **Sync across services**: Copy current version into each AI session preamble
- **Backup**: Keep versioned backups (v1.0, v1.1, etc.)

---

## QUICK CHECKLIST: END-OF-SESSION EXTRACTION

Use this before closing an AI research session:

- [ ] Noted all [EXTRACT: ...] flags during conversation?
- [ ] Asked AI for structured extraction snapshot?
- [ ] Reviewed snapshot for accuracy and confidence markers?
- [ ] Saved snapshot to: `extracts/session_[N]_[service]_[topic].md`?
- [ ] Any contradictions with previous sessions? (Flagged for resolution?)
- [ ] Ready to merge back to main profile on next consolidation cycle?

---

## EXAMPLE EXTRACTION FLOW (End-to-End)

### Starting Point:
- ben_job_research_profile.md (v1.0, current)

### Session: Perplexity Research
```
User: [Shares profile] [Asks about Netflix Infrastructure Engineer role]
...
[During conversation, AI identifies:]
- "Your Kubernetes depth is a real strength signal"
- "Go experience gap is minor for this level"
- "Career vector (support → infrastructure) is clear and matches Netflix trajectory"
...
User: [Requests extraction at end]
Perplexity: [Provides structured snapshot]
```

### Extraction Snapshot Output:
```markdown
# EXTRACTED UPDATES FROM SESSION: 2025-12-02 (Perplexity Netflix Research)

## EXTRACTION SUMMARY
Confirmed career vector (support → infrastructure) as primary path and primary evaluation 
criterion. Identified Kubernetes as strong expertise ready to highlight. Go gap assessed as 
learning opportunity vs. blocker. Recommend increasing Phase 2 (Role) research weight to 45%.

## CHANGES BY SECTION

### CORE CONTEXT
- Career Vector: NO CHANGE (confirmed as support → infrastructure)
- Target Companies: NO CHANGE (Netflix confirmed as good fit)

### TECHNICAL PROFILE
- **Strong Expertise**: Confirmed Kubernetes should be elevated/emphasized
- **Learning Areas**: Go confirmed as learnable, not blocker

### JOB EVALUATION PRIORITIES
- Phase 1 (Career Vector): 40% → 40% (CONFIRM: This is the right weighting)
- Phase 2 (Role): 30% → 45% (Netflix role is infrastructure-heavy; prioritize research here)
- Phase 3 (Market): 15% → 10% (Market demand is clear; focus on company-specific fit)
- Phase 4 (Remote/Flexibility): 10% → 5% (Netflix known for flexibility; lower priority)

### FOLLOW-UP QUESTIONS
- **New Always-Ask**: "Can you walk me through how your infrastructure team evolved from support? What was the pivot?"
- **Netflix-Specific**: "Netflix is known for freedom and responsibility. How does that translate to the infra team? Any on-call burden tradeoffs?"

### NEXT STEPS
- Prepare Netflix-specific follow-up questions (added to profile)
- Consider doing a Netflix culture deep-dive session (Glassdoor + Blind analysis)
- Confirm Go proficiency expectations directly with recruiter

---
**Extracted by**: Perplexity  
**Session Date**: 2025-12-02  
**Status**: Ready to merge
```

### Consolidation (Manual):
- Save to: `extracts/session_1_perplexity_netflix_research.md`
- Review for conflicts: None detected
- Merge back to: `ben_job_research_profile.md`
- Update version: 1.0 → 1.1
- Update metadata: Last Updated: 2025-12-15

---

## TIPS FOR EFFECTIVE EXTRACTION

1. **Be specific**: Not "I learned a lot" but "I learned that Go experience is learnable vs. required"
2. **Quote the AI**: Include direct quotes in extraction snapshots for future reference
3. **Flag confidence**: Always include ~90% / ~60% / ~30% markers
4. **Separate facts from opinion**: "Netflix is known for X [researched fact]" vs. "I think Netflix values Y [opinion]"
5. **Set consolidation cadence**: Every 4–6 weeks, not ad-hoc
6. **Version control**: Keep all extracts in git; never lose session data
7. **Cross-check**: If researching across multiple services, watch for contradictions

---

## FINAL THOUGHT

This extraction meta-prompt is a **knowledge management system** for your job research. 

Instead of scattered conversations that disappear, you're building a **living, versioned profile** that:
- Persists across multiple AI services
- Improves with each session
- Stays consistent and accurate over months
- Becomes a reusable asset for interviews, career planning, and strategy

Use it, refine it, and share back if you find improvements.

---

**Related Files**:
- `ben_job_research_profile.md` (main profile template)
- `job_research_meta_prompt.md` (the universal research framework)
- `extracts/` directory (session-by-session snapshots)


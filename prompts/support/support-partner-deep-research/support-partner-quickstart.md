# Support Partner Quick Start Guide
## How to Use the Deep Research Prompt for Customer Issue Resolution

---

## 🎯 What This Is

A **structured template** for diagnosing and fixing customer problems systematically. Instead of guessing or going in circles, you follow a proven 4-phase process that:

- **Validates** the problem is real  
- **Isolates** the root cause with evidence  
- **Proposes** ranked solutions  
- **Documents** what you learned for next time  

Works for **manual chat**, **automated scripts**, or **hybrid workflows**.

---

## ⚡ Quick Start (5 Minutes)

### Step 1: Open the Prompt
Save and open **`support-partner-deep-research.md`** in your AI chat tool (Perplexity, Claude, etc.).

### Step 2: Tell Your AI the Context
Paste this into your chat:

```
Mode: [1] Manual chat  
I'm about to report a customer issue. 
Use the Support Partner template to help me diagnose it.
```

### Step 3: Describe the Customer's Problem
Example:

```
Customer: "My data pipeline is stuck since last night"

Details:
- Error message: "timeout waiting for table lock"
- Environment: Production, 5M records/day
- When it started: 8pm yesterday, right after we upgraded to v2.3
- Impact: All downstream reports blocked
```

### Step 4: Follow Along
Your AI will:
- Ask clarifying questions (Phase 0)
- Request logs/metrics (Phase 1)
- Propose diagnostic tests (Phase 2)
- Rank solutions (Phase 3)

**You answer questions. It organizes the thinking.**

---

## 📖 The 4 Phases Explained

### Phase 0: What's Actually Wrong?

**Goal**: Understand the problem before jumping to solutions.

**Questions to answer:**
- What was the customer *trying to do*?  
- What *actually* happened instead?  
- When did it start and can you reproduce it?  
- How bad is it (blocks work, just annoying, unexpected)?  

**Example output:**
```
✓ Customer trying: Run daily ETL sync
✗ What happened: Job timeout after 15 min (used to take 5 min)
✓ Reproducible: Yes, every run since last night
✓ Impact: HIGH - blocks all downstream dashboards
```

---

### Phase 1: Gather Clues

**Goal**: Collect evidence to build theories (hypotheses).

**What to request:**
- Error logs (exact text, not "there was an error")  
- System metrics (CPU, memory, disk at time of failure)  
- Configuration (recent changes, version numbers)  
- Reproducibility steps (exact user actions)  

**Example:**
```
Hypothesis A: Version upgrade broke a library (80% likely)
Hypothesis B: Database is slow (60% likely)
Hypothesis C: Out of disk space (40% likely)

To test A, I need: Upgrade changelog + error logs
To test B, I need: Query performance metrics
To test C, I need: Disk usage at time of failure
```

---

### Phase 2: Test Your Theories

**Goal**: Prove which hypothesis is right.

**Safe tests first:**
1. Check logs (no risk)  
2. Check metrics (no risk)  
3. Test in staging if possible (low risk)  
4. Test in production with monitoring (higher risk)  

**Example:**
```
Test A: Check logs for library errors
→ Result: "No errors, version upgrade successful"
→ Hypothesis A: ❌ Ruled out

Test B: Check database query time
→ Result: Queries now take 10x longer than baseline
→ Hypothesis B: ✓ CONFIRMED
```

---

### Phase 3: Fix It

**Goal**: Propose solutions ranked by speed vs. completeness.

**Example:**
```
Rank 1 (Quick): Increase timeout from 15 to 30 seconds
  - Timeline: 5 minutes
  - Risk: Low
  - Trade-off: Doesn't fix root cause, just buys time

Rank 2 (Real fix): Optimize slow database query
  - Timeline: 1–2 hours
  - Risk: Medium (test in staging first)
  - Trade-off: Solves root cause, takes longer

Rank 3 (Prevention): Add query monitoring + alerts
  - Timeline: 2–4 hours
  - Risk: Low
  - Trade-off: Prevents this from happening silently next time
```

---

### Phase 4: Document & Improve

**Goal**: Make the next similar issue faster to fix.

**What to save:**
- Problem: "Database queries slow after version upgrade"  
- How we diagnosed it: "Checked logs → metrics → ruled out app → found DB query"  
- What fixed it: "Optimize query + add alert on slow queries"  
- Next time: "Run these diagnostic steps first"  

---

## 💡 Usage Patterns

### Pattern 1: Manual Chat (Recommended for Learning)

**Best for:** First time using this, complex issues, learning the process.

```
1. Paste this prompt into Perplexity/Claude/etc.
2. Say: "I have a customer issue. Help me diagnose it."
3. Describe the problem (error, when, impact)
4. AI asks questions → You answer
5. AI proposes hypothesis, tests, solutions
6. You pick solution, implement, report back
```

**Time investment:** 30–60 minutes depending on complexity.

---

### Pattern 2: Automated Script (Advanced)

**Best for:** Recurring issues, batch processing, integration with ticketing systems.

**Setup:**
```bash
# Create issue.json with problem details
cat > issue.json << EOF
{
  "issue_id": "SUPPORT-001",
  "symptoms": "Pipeline timeout",
  "error_message": "timeout waiting for table lock",
  "environment": "production",
  "artifacts": {
    "logs": "raw logs here...",
    "metrics": "CPU/mem data here..."
  }
}
EOF

# Run diagnosis (pseudocode; adapt to your setup)
python support_partner.py --input issue.json --output diagnosis.json
```

**Output:** Structured JSON with diagnosis, hypotheses, ranked solutions.

---

### Pattern 3: Hybrid Chat + CLI

**Best for:** Quick initial triage in chat, then systematic investigation via CLI.

```
1. Chat: Customer reports issue
2. Chat: AI does quick Phase 0 (scoping)
3. CLI: Script automates Phase 1 (log parsing, metrics)
4. Chat: Review results, narrow hypotheses
5. CLI: Run targeted tests (Phase 2)
6. Chat: Review findings, decide on fix (Phase 3)
```

---

## 📊 Real Example: "Pipeline Timeout"

**Customer reports:**
> "My data pipeline times out every morning. Used to work fine."

---

**Phase 0: Intake**
```
Q: When did this start?
A: Yesterday morning

Q: What changed?
A: We upgraded Airbyte from v2.1 to v2.3

Q: What's the impact?
A: All downstream reports are 2+ hours late
```

→ **Scope:** Version upgrade, high impact, started yesterday

---

**Phase 1: Evidence**
```
Hypothesis A: Version upgrade broke something (85% likely)
Hypothesis B: Data volume increased (50% likely)
Hypothesis C: External API is slow (40% likely)

Need:
- Airbyte logs from past 24 hours
- Table row counts before/after upgrade
- API response times
```

→ **Customer provides logs showing:** "Version 2.3 changed connection pool size"

---

**Phase 2: Testing**
```
Test A: Check Airbyte changelog for v2.3 changes
→ Found: Default pool size reduced from 50 to 10

Test B: Check job execution metrics
→ Found: Jobs now waiting in queue (not running in parallel)

Test C: Reproduce in staging with v2.3
→ Result: Same behavior with small data, but fast

Test D: Check production data volume
→ Result: Data volume same as before
```

→ **Root cause found:** Pool size too small for production data volume

---

**Phase 3: Solution**
```
Option 1 (Quick): Increase pool size back to 50
  - Time: 5 minutes
  - Risk: Low
  - Fixes: ✓ Unblocks pipeline immediately

Option 2 (Better): Tune pool size to actual data volume (20)
  - Time: 30 minutes (includes testing)
  - Risk: Low
  - Fixes: ✓ Root cause, optimized for your data

Option 3 (Prevention): Add monitoring for pool exhaustion
  - Time: 2 hours
  - Risk: Low
  - Fixes: Alerts before it happens again
```

→ **Customer picks Option 1** → Problem solved in 5 minutes

---

**Phase 4: Documentation**
```
Pattern: "Version upgrades with changed defaults"

Next time:
1. Check changelog for breaking changes
2. Monitor connection pool size in Phase 1 diagnostics
3. Add alert on pool exhaustion to Grafana
```

---

## 🔧 Choosing Your Mode

| Mode | Best For | Time | Learning Curve |
|------|----------|------|-----------------|
| **Manual Chat** | First time, complex issues, learning | 30–90 min | Easy (follow along) |
| **Scripted** | Recurring issues, automation, batch processing | 15–30 min | Moderate (setup once) |
| **Hybrid** | Mix of manual triage + automated investigation | 20–45 min | Moderate (best of both) |

**Recommendation if you're new:** Start with **Manual Chat**. Do 3–5 issues this way to internalize the process. Then move to scripted if you see patterns.

---

## 📋 When to Use Which Phase

### Quick issue?
→ Just do **Phase 0 + Phase 3** (scoping + solutions)

### Tricky issue?
→ Do **Phases 0 → 1 → 2 → 3** (full diagnosis)

### Recurring pattern?
→ Do full phases + **Phase 4** (document for next time)

### Production emergency?
→ **Phase 0 + Phase 3 (Quick Fix)** immediately, then **Phase 2 (Root Cause)** when not on fire

---

## ✅ Checklist: Before You Start

- [ ] Save `support-partner-deep-research.md` locally
- [ ] Paste into your AI chat tool
- [ ] Tell it your mode: `[1] Manual`, `[2] Scripted`, or `[3] Hybrid`
- [ ] Have customer issue details ready (error, timeline, impact)
- [ ] Know what data/logs you can request (or if customer can access)
- [ ] Decide your timeline: Quick triage or deep investigation?

---

## 🔗 Iterate & Improve

**Want to refine this template?** Visit the original chat:  
→ [https://www.perplexity.ai/search/title-seed-orchestrator-v3-2-h-LFSSbUZUTQ60DzGPIVmaSA#0](https://www.perplexity.ai/search/title-seed-orchestrator-v3-2-h-LFSSbUZUTQ60DzGPIVmaSA#0)

**Share feedback:**
- "I used it for [issue type], here's what worked"
- "Phase X was confusing, here's what would help"
- "I added this pattern, think others would find it useful?"

Each iteration makes it better for you and your team.

---

## 📚 Files in This Set

| File | Purpose |
|------|---------|
| `support-partner-deep-research.md` | Full template with all phases, schemas, strategies |
| `support-partner-quickstart.md` | This file — quick reference |
| `support-partner-examples.jsonl` | Real examples (issues + diagnosis + solutions) |
| `support-partner-runbook.sh` | CLI wrapper (optional, for scripted mode) |

**For most people:** You only need the first file. The others are optional add-ons.

---

## 🚀 Next Steps

1. **Try it once** (30–60 min): Paste template, diagnose one issue, see how it feels
2. **Adjust it** (10 min): Any phases you want to skip? Any questions to always ask?
3. **Automate it** (if helpful): Set up a script if you see recurring patterns
4. **Share it** (optional): Help your team or colleagues use the same process

---

## 💬 Common Questions

**Q: Do I have to do all 4 phases?**  
A: No. Quick issues: just Phase 0 + 3. Complex issues: all 4. Production fires: 0 → 3 (quick) → 2 (root cause when calm).

**Q: What if I don't have all the data the template asks for?**  
A: Start with what you have. The template helps you ask for what's missing. Say: "I need logs, metrics, and repro steps to narrow this down."

**Q: Can I use this for non-technical issues?**  
A: Probably not. This is built for technical troubleshooting (logs, config, metrics). For other domains, the Seed system has other templates.

**Q: How long does this take?**  
A: Depends on issue:
- **Known issue**: 5–15 min (Phase 0 + 3)
- **New issue**: 30–90 min (all phases)
- **Production fire**: 15 min triage (Phase 0 + quick fix) + 1–2 hours root cause later

**Q: Should I use this for every customer issue?**  
A: Use it when:
- Issue is unclear or multi-part
- You're not sure what's causing it
- You want to document findings for next time

Skip it when:
- It's a known issue with a documented fix
- You're just pointing customer to docs
- It's a feature request (different process)

---

## 📖 One-Pager Reminder

Print this and put it on your desk:

```
SUPPORT PARTNER: 4-PHASE DIAGNOSIS

Phase 0: INTAKE
  What are they trying to do?
  What happened instead?
  When? Reproducible? Impact?

Phase 1: EVIDENCE
  Request: logs, metrics, config
  Generate hypotheses (ranked by likelihood)
  Flag assumptions

Phase 2: TESTING
  Design tests (low-risk first)
  Run, compare to baseline
  Confirm or eliminate hypotheses

Phase 3: SOLUTIONS
  Propose options (quick fix vs. root fix vs. prevention)
  Rank by: feasibility, risk, impact, timeline
  Provide exact steps + rollback plan

Phase 4: DOCUMENTATION
  Document findings → knowledge base
  Identify system gaps
  Update runbook for next time
```

---

**Status**: Ready to use ✓  
**Last updated**: 2025-12-30  
**Questions?** Revisit the chat: [https://www.perplexity.ai/search/title-seed-orchestrator-v3-2-h-LFSSbUZUTQ60DzGPIVmaSA#0](https://www.perplexity.ai/search/title-seed-orchestrator-v3-2-h-LFSSbUZUTQ60DzGPIVmaSA#0)
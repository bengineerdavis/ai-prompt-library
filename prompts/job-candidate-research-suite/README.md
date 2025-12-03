# Job Candidate Research Suite - README

## Overview

This directory contains **five core seed prompts** designed to help you research companies, recruiters, and opportunities before investing time in the interview process. These prompts follow your "vanilla seed" philosophy—they're flexible templates you can personalize for any LLM (Claude, GPT-4, Perplexity) and refine based on your workflow.

**Key principle**: Run research *before* committing to interviews, not after.

---

## Files Included

| File | Purpose | When to Run |
|------|---------|------------|
| `company-research.md` | Deep-dive on company business, culture, market position, financial health | Within 24 hours of recruiter outreach |
| `recruiter-research.md` | Profile of recruiter and hiring manager; team health signals | Within 24 hours of recruiter outreach |
| `skill-mapping.md` | Map your experience to job requirements; identify skill gaps and mitigation | After receiving full job description |
| `salary-research.md` | Market benchmarks, company comp philosophy, negotiation strategy | Before first call with recruiter |
| `critical-questions.md` | Tailored questions to ask recruiter/hiring manager | Night before each screening call |
| `tracking-template.csv` | Log and compare multiple opportunities | Ongoing as you progress through multiple processes |
| `README.md` | This file; how to use the suite |

---

## Quick Start

### For a Single Opportunity

1. **Day 1**: Run `company-research.md` + `recruiter-research.md` (30-40 min total)
   - Decide: Is this company worth your time?
   - Document: Key findings, red flags, green flags

2. **After Job Description**: Run `skill-mapping.md` (20-30 min)
   - Decide: Do you have the skills? What gaps are learnable?
   - Plan: 1-week learning plan for any "Learnable" gaps

3. **Before First Call**: Run `salary-research.md` + `critical-questions.md` (30 min)
   - Know: Fair market range + your walk-away number
   - Prepare: 5-8 tailored questions for recruiter screen

4. **After Each Call**: Update `tracking-template.csv`
   - Log: Answers to your questions, red flags, green flags
   - Compare: Against other opportunities

### For Multiple Opportunities

- Run research in parallel for 3-5 opportunities
- Use `tracking-template.csv` to compare compensation, team health, growth potential
- Focus interview time on top 2-3 opportunities based on research

---

## How to Use Each Seed Prompt

### 1. Company Research (`company-research.md`)

**Input**: Company name

**Process**:
1. Copy the seed prompt
2. Paste into your LLM (Claude, GPT-4, Perplexity)
3. Replace `[COMPANY_NAME]` with the actual company
4. Run the prompt
5. Review findings; note red/yellow/green flags

**Output**: 1-2 page company profile with financial health, team stability, market position

**Key questions answered**:
- Is this company growing or shrinking?
- Is leadership stable or chaotic?
- What's the engineering culture like?
- Are there red flags (layoffs, regulatory issues, negative reviews)?

---

### 2. Recruiter Research (`recruiter-research.md`)

**Input**: Recruiter name, hiring manager name, company name

**Process**:
1. Copy seed prompt
2. Replace placeholders: `[RECRUITER_NAME]`, `[HIRING_MANAGER_NAME]`, `[COMPANY_NAME]`
3. Run prompt
4. Document: Recruiter credibility, hiring manager style, team tenure

**Output**: Profile of recruiter credibility + hiring manager management style

**Key questions answered**:
- Is the recruiter personalized or spray-and-pray?
- Is the hiring manager respected or problematic?
- Is the team stable or high-turnover?
- What's the hiring manager's management philosophy?

---

### 3. Skill Mapping (`skill-mapping.md`)

**Input**: Full job description + resume + your career goals

**Process**:
1. Copy seed prompt
2. Paste full job description into `[PASTE_FULL_JOB_DESCRIPTION]`
3. Paste resume into `[PASTE_RESUME_OR_LINKEDIN_SUMMARY]`
4. Add your goals (e.g., "Deepen AI skills", "Move to leadership")
5. Run prompt
6. Review: Which gaps are dealbreakers? Which are learnable?

**Output**: Skill mapping table + gap mitigation plan + decision matrix

**Key questions answered**:
- Do I have the skills for this role?
- What gaps are learnable vs. blockers?
- What's my unique value prop?
- Is this role aligned with my 90-day goals?

---

### 4. Salary Research (`salary-research.md`)

**Input**: Role title, company name, your experience level, location

**Process**:
1. Copy seed prompt
2. Fill in: `[ROLE_TITLE]`, `[COMPANY_NAME]`, `[YEARS_EXPERIENCE]`, `[LOCATION]`
3. Add company funding stage and industry
4. Run prompt
5. Document: Market range, recommended ask, walk-away number

**Output**: 1-page compensation brief with market data + negotiation talking points

**Key questions answered**:
- What's fair market compensation for my role?
- What's the company's comp philosophy?
- What should I ask for (base, bonus, equity)?
- What's my walk-away number?

---

### 5. Critical Questions (`critical-questions.md`)

**Input**: Role, company, your experience, call type (recruiter screen vs. hiring manager)

**Process**:
1. Copy seed prompt
2. Fill in: `[ROLE_TITLE]`, `[COMPANY_NAME]`, `[YOUR_EXPERIENCE]`, `[CALL_TYPE]`
3. Run prompt
4. Pick 5-8 most relevant questions for your call
5. Prepare talking points for why you're asking each

**Output**: 25+ questions organized by category (role clarity, team health, growth, strategy, logistics)

**Key questions answered**:
- What should I ask about role expectations?
- What reveals team health and culture?
- How do I surface deal-breakers early?
- What indicates good leadership?

---

## Workflow: Full Interview Process

### Week 1: Recruiter Outreach
```
Day 1 Morning: Recruiter email arrives
  ↓
Day 1 Afternoon: Run company-research.md + recruiter-research.md
  ↓
Day 1 Evening: Decide: Is this worth 5-10 hours of interview time?
  ↓
Day 2: Respond to recruiter; request full job description
```

### Week 2: Recruiter Screen
```
Day 5: Full job description received
  ↓
Day 5 Afternoon: Run skill-mapping.md + salary-research.md
  ↓
Day 5 Evening: Prepare critical-questions.md (recruiter screen version)
  ↓
Day 6: 20-min recruiter screen call
  ↓
Day 6 Evening: Update tracking-template.csv with findings
```

### Week 3-4: Hiring Manager Call
```
Day 8: Schedule hiring manager call
  ↓
Day 7 Evening: Prepare critical-questions.md (hiring manager version)
  ↓
Day 8: 45-60 min hiring manager deep dive
  ↓
Day 8 Evening: Update tracking-template.csv; compare to other opportunities
```

### Week 5+: Interview Rounds
```
Repeat: Each call → Document → Compare
  ↓
Compare across all opportunities using tracking-template.csv
  ↓
Focus interview time on top 2-3 opportunities
```

---

## Integration with Your Prompt Engineering Workflow

These seed prompts follow your established patterns:

✅ **Vanilla seed structure**: Non-personalized templates you can adapt for any LLM  
✅ **Checkpoints**: Each prompt has clear inputs/outputs and decision gates  
✅ **Placeholder pattern**: Use `[PLACEHOLDERS]` for customization per opportunity  
✅ **Guidance sections**: How-to use, red flags, green flags, related docs  
✅ **Iterative refinement**: Update these templates based on what works in real interviews  

### To Personalize These Prompts

1. **For your model**: If using Claude, keep as-is. If using GPT-4, add "You're an expert in [field]" at the top.
2. **For your priorities**: Add constraints like "Consider remote-first opportunities" or "Prioritize equity-heavy comp for early-stage"
3. **For your goals**: Reference your 90-day learning plan (AI skills, leadership, security) in each prompt
4. **For iteration**: After using once, note what worked/didn't, then update the template

---

## Red Flags to Watch For

### Company-Level Red Flags 🔴
- Recent large layoff
- Negative Blind/Glassdoor reviews about management
- Unclear strategy or frequent pivots
- Shrinking headcount or team consolidation
- Burning cash with no path to profitability

### Recruiter-Level Red Flags 🔴
- Generic, copy-paste outreach
- Can't answer basic questions about the role
- Pressure to decide quickly
- Vague about compensation or process
- Poor response time

### Role-Level Red Flags 🔴
- Backfill due to burnout or poor management
- Vague job description
- Unrealistic requirements (5+ years experience for junior role)
- Constant context-switching or on-call load
- No clear growth path

---

## Green Flags to Look For

### Company-Level Green Flags 🟢
- Growing headcount (especially engineering)
- Positive Glassdoor/Blind reviews
- Clear strategy and consistent messaging
- Recent funding or profitability milestone
- Engineering blog with substantive posts

### Recruiter-Level Green Flags 🟢
- Personalized outreach referencing your background
- Clear about role expectations and timeline
- Responsive and transparent
- Can answer detailed questions about team and company

### Role-Level Green Flags 🟢
- New role (expansion, not backfill)
- Clear scope and success metrics
- Growth opportunity aligned with your goals
- Strong hiring manager with good Blind/Glassdoor feedback
- Flexible on remote/location

---

## Tips for Success

1. **Research before declining**: You might be surprised by companies once you research them
2. **Compare across multiple opportunities**: Use tracking-template.csv to find patterns
3. **Ask the hard questions early**: Don't wait until offer stage to learn about red flags
4. **Document everything**: Your memory will blur 3 weeks in with 5 parallel processes
5. **Know your walk-away number**: For salary, culture, commute, growth opportunity
6. **Prioritize ruthlessly**: You can't give 100% to 10 opportunities; focus on 2-3 at a time
7. **Update these templates**: After each round of interviews, note what questions worked best

---

## FAQ

**Q: Should I run all five prompts for every opportunity?**
A: Start with company + recruiter research (fast, low-cost decision filter). Then skill-mapping + salary research only if you're seriously considering the role.

**Q: How do I compare multiple offers?**
A: Use `tracking-template.csv` to log compensation, growth, team health, and culture signals across opportunities. Score each dimension (1-5) to compare holistically.

**Q: What if the recruiter won't answer my questions?**
A: That's a red flag. Good recruiters are transparent. If they dodge questions about comp, process, or team health, that's a signal about the company culture.

**Q: Should I use these prompts word-for-word?**
A: No! Customize them for your priorities, your LLM's style, and what you learn over time. The structure is reusable; the wording should evolve.

**Q: How much time should I spend on research before the first call?**
A: 30-45 min total for company + recruiter research. If it's worth pursuing, add another 30 min for skill-mapping + salary research before the recruiter screen.

---

## Next Steps

1. **Pick an active opportunity**: Use this suite on a real recruiter outreach
2. **Document what works**: Note which questions surface the most useful info
3. **Iterate**: After round 1, refine these templates based on what you learned
4. **Build your comparison sheet**: Use tracking-template.csv to compare multiple parallel opportunities
5. **Return and update**: After landing an offer, share learnings so others can benefit

---

## Related Resources

- **Never Search Alone** (Rishi Taparia): For job search strategy and accountability
- **Good Strategy / Bad Strategy** (Richard Rumelt): For evaluating whether opportunities align with your strategy
- **Blind app**: For anonymous engineer feedback on companies, managers, roles
- **Levels.fyi**: For salary benchmarking by role, company, level
- **Glassdoor**: For company culture and manager reviews
- **Engineering blogs**: Company career pages and tech blogs reveal culture and values

---

## Support & Feedback

After using these prompts:
- What questions were most useful?
- What red flags did you not predict?
- What gaps in research did you notice?
- How would you restructure these prompts?

Document your learnings so you can iterate and share patterns with others in your network.

---

**Good luck with your job search!** 🚀

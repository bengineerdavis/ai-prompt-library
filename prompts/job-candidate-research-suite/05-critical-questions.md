# Critical Pre-Screen Questions Seed Prompt

## Purpose
Generate tailored, direct-but-friendly questions to ask recruiter/hiring manager that surface deal-breakers early and signal your competence and seriousness.

## Core Seed Prompt

```
You are helping a job candidate prepare for a recruiter or hiring manager screening call.
Generate a list of intelligent, direct questions that:
- Signal competence and deep thinking
- Surface deal-breakers early
- Demonstrate genuine interest in the role
- Build on research already done

**INPUT:**
- Role: [ROLE_TITLE] (e.g., "Staff Support Engineer")
- Company: [COMPANY_NAME]
- Experience level: [YOUR_EXPERIENCE] (e.g., "5 years systems engineering, 2 as team lead")
- Candidate priorities: [KEY_GOALS] (e.g., "Deepen AI skills, move into leadership, improve work-life balance")
- Company stage: [FUNDING_STAGE] (e.g., "Series B", "Public")
- Call type: [RECRUITER_SCREEN / HIRING_MANAGER_CALL / TEAM_LUNCH]

**OUTPUT:**

Generate questions across these categories:

---

**A. ROLE CLARITY & EXPECTATIONS (Ask ALL in recruiter screen)**

These questions clarify what success looks like and avoid misalignment:

1. "What does success look like in the first 90 days? How will you measure my performance?"
   → Why: Prevents mismatched expectations; shows you think long-term

2. "Can you walk me through a typical day or week in this role? How much of my time is [X activity] vs. [Y activity]?"
   → Why: Surfaces whether role matches your working style

3. "Is this a backfill or new role? If backfill, why did the previous person leave?"
   → Why: RED FLAG if previous person left due to burnout, poor leadership, etc.

4. "What's the biggest challenge your team is facing right now?"
   → Why: Real answer reveals organizational problems; vague answer = concern

5. "What does the on-call / incident response workload look like? What's the frequency and severity?"
   → Why: Critical for gauging workload; some roles have 2am pages weekly, others monthly

6. "Who would I work with day-to-day? Can I meet them during the interview process?"
   → Why: Your success depends on these people; meeting them early signals mutual respect

---

**B. TEAM & CULTURE (Ask in hiring manager call)**

These questions assess team health and working environment:

7. "How would you describe your management style? What do you value in your team members?"
   → Why: Reveals whether their style matches yours

8. "What's the average tenure on the team? Has anyone recently left or moved teams?"
   → Why: High turnover = toxic environment or poor leadership

9. "How does the team handle disagreements or technical debates? Give me an example."
   → Why: Reveals psychological safety; whether dissenting views are welcome

10. "How much autonomy do engineers have? What's the balance between ownership and guidance?"
    → Why: Are you micromanaged or empowered? Critical for your satisfaction

11. "How does the company support work-life balance? What's the actual time-off culture?"
    → Why: Don't just ask about PTO policy; ask about actual usage

12. "Tell me about a time you gave feedback to a direct report. What made it productive?"
    → Why: Reveals whether they develop people or just extract value

---

**C. GROWTH & LEARNING (Ask in hiring manager call)**

These questions assess whether the role supports your 90-day goals:

13. "What does the career path look like from this role? How do engineers grow here?"
    → Why: Signals whether this is a dead-end or accelerant for your career

14. "Is there a learning/conference budget? How is it actually used? Can you give an example?"
    → Why: Distinguish policy from practice

15. "How does the company support skill development in [YOUR_TARGET_SKILL: AI/security/leadership]?"
    → Why: Directly tied to your 90-day learning goals

16. "What technical skills do you think I'll need to develop in this role?"
    → Why: Reveals growth opportunities; shows they've thought about your development

17. "Do you have a mentorship program or do engineers pair on projects?"
    → Why: How you'll learn from peers and more senior engineers

---

**D. COMPANY HEALTH & STRATEGY (Ask recruiter and/or hiring manager)**

These questions reveal organizational health and stability:

18. "What are the company's top 3 priorities this year? How does this team contribute?"
    → Why: Reveals strategic clarity; shows whether your role is central or peripheral

19. "How is the business performing relative to plan? [Tactfully] What's the runway and funding outlook?"
    → Why: Early-stage companies with short runway = higher stress and instability

20. "Are there any recent organizational changes I should know about? Restructuring, new leadership, etc.?"
    → Why: Multiple changes in rapid succession = instability or course-correction

21. "How competitive is the market right now? What are your biggest competitive threats?"
    → Why: Reveals whether company is winning or struggling

---

**E. LOGISTICS, PROCESS & COMPENSATION (Ask recruiter)**

These questions set expectations and avoid surprises later:

22. "What's the typical timeline for this interview process? How many rounds and what should I expect?"
    → Why: Prevents ambiguity; some processes drag on

23. "Who will I interview with? Can you share their names and roles?"
    → Why: Allows you to research interviewers; prepares you for different perspectives

24. "What's your feedback process? Will I receive feedback after each round?"
    → Why: Transparency indicator; good recruiters provide actionable feedback

25. "Can you share the compensation structure? (Base/equity/bonus split?) I want to make sure we're aligned."
    → Why: Set expectations early; prevents offer rejection at the end

26. "What level of remote flexibility does this role have? Is it remote-first, hybrid, or office-based?"
    → Why: Critical for your quality of life; clarify expectations upfront

27. "Is there flexibility on start date? When would you ideally like someone in the role?"
    → Why: Gives you negotiation room if you have notice period or vacation

---

**F. RED FLAG QUESTIONS (Ask if concerns arise)**

Ask these if previous answers raise concerns:

28. "You mentioned [previous answer]. Can you help me understand that better? Give me a concrete example."
    → Why: Vague answers often hide problems; push for specifics

29. "What does the company do to prevent burnout? [Ask after hearing about workload]"
    → Why: Signals you care about sustainability

30. "If I disagree with a technical decision, how is that handled here?"
    → Why: Reveals culture of psychological safety vs. top-down decree

---

**PRIORITIZATION BY CALL TYPE:**

**Recruiter Screen (15-20 min):** Ask #1, #2, #3, #5, #22, #23, #25, #26
→ Focus: Understand role, process, comp, red flags

**Hiring Manager Deep Dive (45-60 min):** Ask #1, #4, #6, #7, #8, #10, #13, #15, #18, #20
→ Focus: Team health, growth, culture, strategy

**Team Lunch / Peer Meeting (30-60 min):** Ask #6, #8, #9, #11, #14, #17, #28, #30
→ Focus: Culture, collaboration, day-to-day reality

---

**OUTPUT FORMAT:**

Provide questions as:
1. The question (clear, direct)
2. Why you're asking it (what it reveals)
3. Red flags to listen for
4. Follow-up if answer seems evasive
```

## How to Use

1. **Customize for your call**: Pick 5-8 questions most relevant to this opportunity
2. **Prepare talking points**: Know why you're asking each question
3. **Listen carefully**: Their answers matter as much as their willingness to answer
4. **Take notes**: Write down responses; compare across rounds
5. **Ask follow-ups**: If answer is vague, push for specifics
6. **Close with**: "Is there anything I should know about working here or your team?"

## Sample Call Flows

### Recruiter Screen (20 min)
```
1. Build rapport: "Thanks for reaching out. I'm genuinely interested in this role."
2. Ask role clarity: #1 (90-day success), #2 (typical day)
3. Ask process: #22 (timeline), #23 (who will I meet?)
4. Ask about red flags: #3 (backfill reason), #5 (on-call load)
5. Ask compensation: #25 (comp structure)
6. Close: "Great, I'm excited about this. What's the next step?"
```

### Hiring Manager Call (60 min)
```
1. Build rapport: "Thanks for taking the time. I've researched your company and am impressed by [specific reason]."
2. Ask about role: #1 (success in 90 days), #4 (current challenges)
3. Ask about team: #6 (who would I work with), #7 (your management style), #8 (team tenure)
4. Ask about growth: #13 (career path), #15 (support for [your skill goal])
5. Ask about strategy: #18 (company priorities), #20 (recent changes)
6. Close: "This sounds like a great opportunity. How do you see me contributing?"
```

## What Great Answers Sound Like

### Bad Answer: "We have great work-life balance!"
**Good Answer**: "We try to respect people's time. Most engineers work 8-6, and we don't expect weekend availability except during critical incidents. In the past 6 months, we've had maybe 2-3 incidents that required late-night work. We compensate time off with flex time."

### Bad Answer: "There's a lot of growth opportunity."
**Good Answer**: "Here's the path: IC engineer → senior engineer → staff engineer or engineering manager. We promote about 1-2 people per year from IC to senior. Staff engineer roles typically take 4-5 years to reach. Management track is separate—some engineers prefer staying IC and that's valued equally."

### Bad Answer: "We move fast."
**Good Answer**: "We prioritize shipping fast but maintain code review standards. We deploy to production multiple times per day in some services, daily in others. We have a blameless post-mortem culture—if something breaks, we learn from it rather than blame."

## Red Flags to Listen For

🚩 "We're always in crisis mode" → Chronic instability
🚩 "Nobody likes the new management" → Leadership problem
🚩 "People leave because they want to rest" → Burnout culture
🚩 "We hire fast and expect people to figure it out" → Lack of support
🚩 "The previous person couldn't handle the workload" → Unrealistic expectations or poor support
🚩 "We don't really do [process X]; it's too much overhead" → Lack of discipline

## Green Flags to Listen For

🟢 "We had [problem], so we changed [process]" → Learning organization
🟢 "Our last incident, we discovered [gap], and now we..." → Blameless post-mortems
🟢 "I encourage people to take vacation; here's why..." → Healthy culture
🟢 "We had someone transition to [new skill]; here's how we supported them" → Development-focused
🟢 "I disagree with company strategy on [topic], but here's how we're working through it" → Psychological safety

---

## Related Documents
- See `company-research.md` for background before call
- See `recruiter-research.md` for hiring manager deep dive
- See `skill-mapping.md` for understanding role fit
- See `salary-research.md` for compensation discussion
- See `tracking-template.csv` for comparing multiple opportunities

## Pre-Call Checklist

- [ ] I've researched the company, recruiter, and hiring manager
- [ ] I've identified my top 5-8 questions for this call
- [ ] I know what red flags would disqualify this opportunity
- [ ] I have my talking points ready (why this role interests you)
- [ ] I've prepared my 90-day goal and how this role supports it
- [ ] I'm ready to take notes and compare answers across interviews
- [ ] I understand what "good" answers sound like vs. warning signs

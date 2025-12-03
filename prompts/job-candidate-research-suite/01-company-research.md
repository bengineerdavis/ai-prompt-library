# Company Background & Intelligence Seed Prompt

## Purpose
Deep-dive research on the company's business, culture, technology, and market position to understand if it aligns with your career goals.

## Core Seed Prompt

```
You are a research analyst helping a job candidate evaluate a company.
Using publicly available sources, provide a comprehensive profile on [COMPANY_NAME]:

**PART A: Company Overview & Business**
- Founded: [Year]
- Headquarters / Global presence
- Size: Number of employees, headcount growth trajectory
- Funding: Stage (bootstrapped/pre-seed/Series A-C/public), funding rounds, recent capital
- Revenue/Growth: Public information about revenue, growth rate, profitability
- Core product/service: What problem does it solve? Who are the target customers?
- Business model: SaaS, enterprise, open source, freemium, etc.?
- Market position: Market size, TAM, growth rate

**PART B: Recent News & Trajectory (6-12 months)**
- Product launches, major features, direction changes
- Funding announcements or investor news
- Leadership changes (CEO, CTO, VPs)
- Organizational changes: layoffs, restructuring, new departments
- Partnerships or strategic moves
- Competitive wins or losses
- Regulatory or compliance milestones (if applicable)
- Public controversies or reputation issues

**PART C: Technical Profile & Engineering Culture**
- Technology stack: Primary languages, frameworks, infrastructure (CloudFormation, Kubernetes, etc.)
- Sources: Job descriptions, engineering blog, GitHub repos, Stack Overflow job postings
- Infrastructure: Cloud providers (AWS, GCP, Azure), on-prem, hybrid
- Engineering practices: CI/CD, testing culture, deployment frequency (inferred from public signals)
- Code visibility: Open source contributions, public GitHub, community engagement
- Engineering blog / thought leadership: Do they publish about their technical challenges?

**PART D: Organizational Structure & Team**
- Engineering organization: How many engineers? Teams/departments?
- Reporting structure for [YOUR_TARGET_ROLE]: Who would you report to? Cross-functional partners?
- Known challenges: Scaling issues, technical debt, performance bottlenecks (from job posts or engineering posts)
- Team stability: Recent hiring, growth, or consolidation signals
- Culture signals: Work environment (fast-paced startup, steady enterprise, academic research?)

**PART E: Market Position & Competitive Landscape**
- Direct competitors: Who else does this?
- Competitive advantages: Why do customers choose them?
- Market challenges: What's shifting in their industry? Threats?
- Customer base: Enterprise, SMB, startups? Geographic distribution?
- Growth potential: Expanding market or maturing/consolidating?

**PART F: Reputation & Culture**
- Glassdoor reviews: Salary, culture, leadership, work-life balance
- Blind discussions: Engineering culture, compensation, management quality
- Reddit, HN, Twitter: What do users/employees say about the company?
- LinkedIn: What do current/former employees highlight in profiles?
- Industry reputation: Respected for quality? Fast growth? Good pay?

**PART G: Risk Flags & Concerns**
- Financial health: Burn rate, runway, path to profitability (if available)
- Attrition: High employee turnover? Recent departures?
- Strategic clarity: Clear vision or pivoting frequently?
- Regulatory risks: Compliance issues, legal challenges
- Market headwinds: Is the industry/market shrinking?
- Organizational issues: Known conflicts, leadership changes, team instability

**OUTPUT FORMAT:**
- Organize findings by section
- Provide confidence levels (High/Medium/Low) for each data point
- Highlight gaps where information is unavailable
- Cite sources (e.g., "Per Glassdoor reviews" or "From engineering blog post dated...")
- Summarize overall impression: Is this a stable, growing, or declining company?
```

## How to Use

1. **Run early**: Do this research within 24 hours of recruiter outreach
2. **Gather sources**: Bookmark key pages (Glassdoor, Blind, engineering blog, job board)
3. **Look for patterns**: Multiple sources saying the same thing = reliable signal
4. **Compare to your goals**: Does this company align with your 90-day learning plan?
5. **Cross-reference**: Compare company info with recruiter/hiring manager research
6. **Ask clarifying questions**: Use findings to inform questions for the recruiter

## Key Questions to Answer

### Financial Health 💰
- Is the company growing, stable, or shrinking?
- If funded: What's their runway? Do they need to raise soon?
- If public: Are they hitting financial targets?

### Team Stability 👥
- Is the engineering team growing or losing people?
- Has there been recent leadership turnover?
- Are engineers staying or leaving quickly?

### Technical Culture 🔧
- Do they publish about their tech challenges?
- Is the stack modern or legacy?
- Do they value engineering excellence or speed over quality?

### Market Position 📊
- Are they the market leader, a strong #2, or early-stage?
- Is their market growing or shrinking?
- Are they differentiated or commoditized?

### Cultural Fit 🎯
- What's the pace? (Startup chaos vs. stable vs. slow-moving enterprise)
- Who are the employees? (Career builders, risk-takers, academics?)
- What do people say they value?

---

## Green Flags 🟢

- Growing headcount (especially engineering)
- Positive Glassdoor/Blind reviews
- Clear strategy and consistent messaging
- Recent funding or profitability milestone
- Technical blog with substantive posts
- Stable leadership team
- Engineering-driven product decisions

## Yellow Flags 🟡

- Recent round of funding (might indicate burn rate pressure)
- Mixed Glassdoor reviews (some very positive, some very negative)
- Unclear market positioning
- Hiring lots but also losing people
- Vague communication about strategy
- Frequent leadership changes

## Red Flags 🔴

- Recent large layoff
- Negative Blind posts about management or compensation
- Consistent complaints about technical debt or legacy code
- Regulatory investigations or compliance issues
- Negative Glassdoor reviews (especially about pay or management)
- Burning cash with unclear path to profitability
- Loss of major customers or contracts (if you can find signals)
- Recent CEO/CTO departure or leadership crisis

---

## Research Sources to Check

| Source | What to Look For | Confidence Level |
|--------|------------------|------------------|
| **Glassdoor** | Salary, culture, management reviews | Medium-High |
| **Blind** | Engineering culture, compensation, management quality (anonymous) | Medium-High |
| **LinkedIn Company Page** | Headcount, recent hires, employee highlights | High |
| **Engineering Blog** | Technical challenges, culture, decision-making | High |
| **GitHub** | Code quality, activity, open source engagement | High |
| **Reddit / Hacker News** | Unfiltered user/employee perspective | Medium (crowd-sourced) |
| **Twitter / X** | Leadership commentary, culture signals | Medium |
| **Recent News** | Funding, layoffs, partnerships, leadership changes | High |
| **Job Postings** | Tech stack, team structure, growth areas | High |
| **Crunchbase** | Funding, leadership, timeline | High |

---

## Related Documents
- See `recruiter-research.md` for hiring team research
- See `skill-mapping.md` for role fit analysis
- See `salary-research.md` for compensation benchmarking
- See `critical-questions.md` for pre-screen questions
- See `tracking-template.csv` for logging research

## Quick Checklist

- [ ] I understand the company's business model and market position
- [ ] I've assessed financial health and growth trajectory
- [ ] I've reviewed team stability and recent changes
- [ ] I've checked Glassdoor, Blind, and community sentiment
- [ ] I've identified green and red flags
- [ ] I can articulate why I'm interested in working here (beyond the role)
- [ ] I'm ready to ask informed questions about company strategy

# Salary & Compensation Research Seed Prompt

## Purpose
Determine fair market compensation for your role, experience level, and location; build a data-driven negotiation case.

## Core Seed Prompt

```
You are a compensation analyst helping a job candidate determine fair pay for a role.
Research the following and provide a comprehensive compensation report:

**PART A: Market Benchmarks**

Input parameters:
- Role title: [ROLE_TITLE] (e.g., "Systems Development Engineer L5", "Staff Support Engineer")
- Company: [COMPANY_NAME] (or comparable companies if specific company unknown)
- Experience level: [YEARS_EXPERIENCE] (e.g., "7 years systems engineering", "3 years as an IC, 2 as a lead")
- Location: [LOCATION] (e.g., "San Francisco", "Remote (US)", "NYC hybrid")
- Company stage: [STAGE] (e.g., "Series B", "Public", "Late-stage startup")
- Industry: [INDUSTRY] (e.g., "SaaS", "Enterprise", "AI/ML")

Research sources:
- Levels.fyi: Crowdsourced salary data by role, company, level, location
- Glassdoor: Base salary, bonus, equity ranges
- Blind: Anonymous engineer compensation discussions (high-signal for tech)
- LinkedIn Salary: Aggregated compensation data
- H1B filings: Visa sponsorship salary data (public record)
- Rora: Compensation benchmarking
- Pave: Startup equity benchmark
- Comparably: Industry and company salary data
- Meetup / Slack communities: Peers discussing compensation

Output findings for:
- 25th percentile (conservative)
- 50th percentile (median/market rate)
- 75th percentile (top quartile)
- 90th percentile (premium)

For each range, provide:
- Base salary
- Annual bonus (% of base)
- Stock/equity ($ value or # shares)
- Other benefits (sign-on, relocation, etc.)

---

**PART B: Company-Specific Context**

Research the specific company's compensation philosophy:
- Funding stage: Pre-seed, Series A-C, Public (→ different equity value)
- Known comp philosophy: (Market-leading / Market-rate / Below-market with equity upside)
- Recent funding: Large recent raise might suggest compressed equity value; tight runway might pressure salary down
- Hiring market: Are they hiring urgently (seller's market for candidate) or selective (buyer's market)?
- Public salary data: Any Glassdoor/Blind data specific to this company?
- Industry benchmarks: Is tech/SaaS paying more than this company's peer set?

---

**PART C: Candidate Leverage**

Research what strengthens your negotiating position:
- Unique skills: Niche tech stack, domain expertise (AI, security, DevOps, etc.)
- Market demand signals:
  - Multiple offers or active conversations?
  - LinkedIn "Top Applicant" badge?
  - Recruiters reaching out to you?
- Timing: End of quarter/year (company needs to hit hiring goals), vs. normal time
- Backfill vs. new headcount: Backfill = company has budget already; new headcount = might be flexible
- Your alternatives: Do you have other offers? What can you walk away to?
- Your constraints: Remote requirement, relocation willingness, start date flexibility

---

**PART D: Negotiation Strategy**

Develop a data-driven negotiation approach:

1. **Anchor point**: What number do you open with?
   - Option A: 75th percentile of market data (strong, well-researched position)
   - Option B: 90th percentile if you have high leverage
   - Option C: Market median if company is early-stage and equity-heavy
   - Rationale: Anchor with data, not emotion

2. **Target range**: What's your ideal range?
   - Minimum (walk-away): [NUMBER] (below which you decline)
   - Target: [NUMBER] (what you're optimizing for)
   - Stretch: [NUMBER] (if they counter-offer beyond expectations)

3. **Negotiables beyond salary**:
   - Equity refresh timing (critical for mid-career engineers)
   - Sign-on bonus (especially if leaving equity behind)
   - Title (important for future opportunities)
   - Remote flexibility, office location, travel requirements
   - Learning budget, conference attendance
   - Stock grants vesting schedule
   - Clawback clauses or other equity conditions

4. **Contingencies**:
   - If they say "We have a hard cap at $X": Ask about [Sign-on / Equity / Title / Other negotiable]
   - If equity is lower than expected: Ask when refresh cycle is
   - If bonus % is low: Clarify structure—is it achievable? What's the actual payout history?

---

**PART E: Communication Framework**

Prepare scripts for negotiation conversations:

**Opening (after initial offer):**
"Thank you for the offer. I'm excited about the role. Before I accept, I'd like to discuss the compensation package. I've done market research on comparable roles [provide source citations if helpful], and I want to make sure we're aligned. Here's my thinking..."

**Responding to "That's outside our budget":**
"I understand budget constraints. I'm looking at [market data] for this role and level. What if we explored [alternative negotiable: sign-on / equity / title / start date]? How flexible is the company on that dimension?"

**When discussing equity:**
"I want to understand the equity package. What's the total grant amount, vesting schedule, and refresh cycle? How has equity performed historically at this company?"

**When there are multiple offers:**
"I have another offer at [X amount]. I prefer working at [this company] because [specific reason]. Can we get closer to [target range] to make this work?"

---

**PART F: Red Flags in Comp Offers**

Watch for:
- Vague equity descriptions (ask for exact numbers)
- Unusually long vesting cliff (4-year is standard; 5-year is a red flag)
- No mention of equity refresh
- Significant gap between base and market (might indicate startup financial stress)
- Reluctance to discuss comp structure (sign of inflexibility or problems)
- Lowball offer without explanation (either your level is mismatched or they're testing)

---

**OUTPUT FORMAT:**
Provide a one-page compensation brief with:
- Market range (25th-75th percentile)
- Your recommended ask (with reasoning)
- Your walk-away number
- 3-5 talking points for negotiation
- Key questions to ask about equity, bonus, and benefits
```

## How to Use

1. **Run this early**: Before your first recruiter call (you want to set expectations)
2. **Gather data**: Check Levels.fyi, Glassdoor, Blind for the specific role + company
3. **Anchor research**: Document 3-5 sources for your market range
4. **Calculate your ask**: 75th percentile of market data is a strong, defensible anchor
5. **Know your walk-away**: Don't negotiate below this number
6. **Prepare scripts**: Practice how you'll discuss comp without sounding desperate or greedy
7. **Cross-reference**: Compare this to your 90-day goals (are you willing to take lower pay for specific learning opportunity?)

## Target Ranges (Your Context)

Based on your background (systems engineering, AI/ops focus, post-sales interest):
- **Remote technical leadership**: $140-180k base + equity
- **Hybrid/On-site technical leadership**: $150-220k base + equity
- **AI/DevOps specialist roles**: Similar ranges, with variation by market (SF Bay Area = higher)

---

## Equity Deep Dive Questions

When a company mentions equity, ask:
1. "What's the total grant amount in [shares / $ value]?"
2. "What's the vesting schedule? (4 years with 1-year cliff is standard)"
3. "What's the exercise price?" (Should be FMV—fair market value)
4. "Is there an equity refresh after vesting?" (Critical for retention)
5. "What's the strike price / exercise window?" (If options)
6. "What happens to unvested equity if I leave?" (Single-trigger vs. double-trigger acceleration)

## Bonus Discussion Script

**If they offer 10% bonus but market is 20%:**

"I appreciate the 10% bonus structure. Help me understand—what's the actual payout history? Are bonuses achievable, or is that a theoretical max? At [Previous Company], we paid 15-20% based on performance. Can we discuss making this more competitive, or is the bonus structure tied to specific metrics I should understand?"

## Sign-On Bonus Negotiation

**When accepting equity at a discount:**

"I'm leaving [Previous Company] with $X in unvested equity. To bridge that gap, I'd like a [Amount] sign-on bonus. This helps offset what I'm leaving on the table while I rebuild equity at [New Company]."

---

## Related Documents
- See `company-research.md` for company financial health signals
- See `recruiter-research.md` for company compensation philosophy
- See `skill-mapping.md` for role fit (affects justifiable compensation)
- See `critical-questions.md` for salary discussion questions
- See `tracking-template.csv` for comparing multiple offers

## Compensation Research Checklist

- [ ] I've identified market rate (25th-75th percentile) for my role + experience + location
- [ ] I have 3-5 sources for my market range
- [ ] I've calculated my recommended ask (usually 75th percentile)
- [ ] I know my walk-away number (minimum acceptable)
- [ ] I understand company's funding stage and equity value
- [ ] I can explain my compensation ask with data
- [ ] I'm prepared to negotiate beyond base salary (sign-on, equity, title, flexibility)
- [ ] I have scripts prepared for common objections
- [ ] I understand equity vesting, refresh cycles, and exercise windows
- [ ] I can compare multiple offers using a consistent framework

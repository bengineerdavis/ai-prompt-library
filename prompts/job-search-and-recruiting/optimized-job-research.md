# Optimized Job Research Prompt: AI Technical Support Engineer Role
## For LLM Web Search Engines & Deep Research

---

## GOAL
**Gather candidate-critical intelligence about the hiring company, the Technical Support Engineer role, and competitive/market context—sufficient to make an informed application and interview decision.**

---

## CONTEXT
- **Role**: Technical Support Engineer | AI Support Engineer | Product Support Engineer
- **Skills**: Linux, Docker, Kubernetes, Python, Java, Go
- **Requirement**: 2+ years enterprise technical support, strong Linux, distributed computing
- **Company Context**: Fast-growing AI startup (ex-ScaleAI, Waymo, Tesla, DeepMind talent)
- **User Angle**: Senior IC/technical practitioner evaluating fit, compensation, growth potential, and acquisition risk

---

## RESEARCH DECOMPOSITION
### Phase 1: Company Intelligence (35% of effort)

**Search 1.1: Company Identity & Funding**
- Query: `AI startup fast-growing cutting-edge engineering tools Fortune 500 Series C D E funding 2024 2025`
- Goal: Identify company name, funding stage, valuation, investor profile, founding date
- Why: Signals runway, investment quality, burn rate trajectory

**Search 1.2: Company Mission & Product**
- Query: `AI engineering tools platform enterprise startups product vision 2024`
- Goal: Understand core product, target market, differentiation, product roadmap
- Why: Clarifies whether role is aligned with company growth or support burden

**Search 1.3: Company Culture & Talent**
- Query: `AI startup culture engineering team Glassdoor Blind ex-ScaleAI Waymo Tesla DeepMind`
- Goal: Identify culture signals, team composition, known issues, glassdoor ratings
- Why: Predicts collaboration quality, burnout risk, learning environment

**Search 1.4: Company Financials & Burn Rate**
- Query: `AI startup Series funding burn rate runway profitability 2024`
- Goal: Estimate runway, profitability timeline, financial stability
- Why: De-risks acquisition, layoff, or funding crisis within 2-3 years

**Search 1.5: Competitive Positioning**
- Query: `AI tools platform competitors market share analyst reports 2024`
- Goal: Identify direct competitors, market size, company moat
- Why: Assesses whether role will involve pivoting product, markets, or team

---

### Phase 2: Role Intelligence (40% of effort)

**Search 2.1: Role Scope & Responsibility**
- Query: `Technical Support Engineer AI startup responsibilities escalation incident response`
- Goal: Identify whether role is Tier 1/2/3, customer interaction depth, on-call expectations
- Why: Determines workload, context-switching, and growth ceiling

**Search 2.2: Tools, Observability & Stack**
- Query: `AI platform Technical Support Engineer tech stack monitoring debugging Datadog New Relic Kubernetes Linux tools`
- Goal: Clarify actual troubleshooting environment (not just advertised skills)
- Why: Validates alignment with your experience; signals automation vs. manual toil

**Search 2.3: Customer Profile & Complexity**
- Query: `AI startup enterprise customers technical support Fortune 500 case studies deployment`
- Goal: Identify customer segment (Fortune 500, mid-market, startup), deployment complexity
- Why: Predicts problem difficulty, pay-to-support ratio, and learning opportunity

**Search 2.4: Support Model & Team Size**
- Query: `AI support team size distributed global on-call rotation SLA response time`
- Goal: Understand team structure, coverage model, escalation paths
- Why: Assesses isolation risk, mentorship opportunity, and quality-of-life factors

**Search 2.5: Growth & Career Trajectory**
- Query: `Technical Support Engineer career path promotion engineering manager AI startup`
- Goal: Identify whether role is a terminal support role or gateway to engineering
- Why: Clarifies whether you can transition to backend/platform/infrastructure eng if desired

**Search 2.6: Compensation & Benefits**
- Query: `Technical Support Engineer salary AI startup San Francisco 2024 equity stock options`
- Goal: Baseline compensation, equity structure, benefits
- Why: Enables negotiation and comparison with peers

---

### Phase 3: Competitive & Market Context (15% of effort)

**Search 3.1: Market Demand & Saturation**
- Query: `AI Technical Support Engineer job market demand shortage salary trends 2024 2025`
- Goal: Understand whether this role is in high demand or commoditized
- Why: Informs negotiating power and alternative opportunities

**Search 3.2: Support Engineering as Career Path**
- Query: `Technical Support Engineer to staff engineer career progression skills 2024`
- Goal: Identify whether support eng is viable path to senior IC or stuck tier
- Why: Assesses long-term career viability and industry perception

**Search 3.3: AI Startup Failure Rates & Trends**
- Query: `AI startup failure rate acquisition funding cliff 2024 2025`
- Goal: Understand sector stability and exit patterns
- Why: Risk-adjusts for job security and equity value

---

## SEARCH STRATEGY

### Approach: Multi-Vector Research
1. **Primary**: Company name + role title + keywords (e.g., "Company X Technical Support Engineer Linux Kubernetes")
2. **Secondary**: Glassdoor, Blind, Levels.fyi, Blind forums, LinkedIn company posts
3. **Tertiary**: Analyst reports (Gartner, CB Insights, PitchBook), news archives, funding announcements
4. **Validation**: Cross-reference multiple sources; flag conflicting info with confidence ranges

### Chain-of-Thought for Each Search
1. **Hypothesis**: What do I expect to find?
2. **Query**: Optimized search string
3. **Result Synthesis**: Top 3–5 sources ranked by credibility
4. **Gap Analysis**: What's still unknown? Why?
5. **Next Action**: Refine query or triangulate from adjacent sources

---

## CRITICAL EVALUATION CHECKLIST

After research, assess:

| Dimension | Question | Red Flag | Green Flag |
|-----------|----------|----------|-----------|
| **Company Stability** | Funded? Runway? | <1 year runway, no funding | 2+ years runway, recent Series funding |
| **Product Fit** | Clear market need? | Pivoting frequently | Strong customer traction |
| **Role Clarity** | Tier 1 or Tier 3? | Vague responsibilities | Clear escalation paths, defined scope |
| **Team Health** | Stable team growth? | High attrition, negative reviews | Stable headcount, positive glassdoor |
| **Career Trajectory** | Support→Engineering? | No IC/eng role precedent | Clear paths to IC or backend eng |
| **Compensation** | Competitive? | <25th percentile for market | 50–75th percentile or above |
| **Workload** | Sustainable? | On-call 24/7, 80+ hours | Standard 40–50 hours + reasonable on-call |

---

## EXPECTED OUTPUT
A concise **Decision Memo** (500–800 words) with:

1. **Company Profile**: Name, stage, market position, financial stability (~75 words)
2. **Role Analysis**: Scope, day-in-life, growth potential (~75 words)
3. **Opportunity Score**: 1–10, with 3 key drivers (funding, team, career fit)
4. **Risk Factors**: Top 3 concerns and mitigants (~100 words)
5. **Comparison Context**: How this ranks vs. 2–3 similar roles you're aware of
6. **Recommendation**: Apply / Pass / Negotiate, with specific talking points

---

## EPISTEMIC HONESTY GUARDRAILS

- Flag any information older than 6 months as "dated" and deprioritize
- Mark confidence levels: [~90% confidence] for multi-sourced facts; [~50%] for inferred patterns
- Always include "Where this might be wrong": e.g., "Company financials may be private; this is inferred from funding announcements"
- If critical info is unavailable (e.g., exact team size), explicitly state assumption and propose validation method

---

## FOLLOW-UP PROMPTS (If Needed)

1. **Deep Dive on Compensation**: "Compare this role's equity package to market benchmarks (Stripe, Scale, etc.)"
2. **Technical Deep Dive**: "What actual incident types does this team handle? Are they DevOps or pure support?"
3. **Culture Assessment**: "Red flags in Blind/Glassdoor posts? What's the honest vibe?"
4. **Competitive Analysis**: "How does this company compare to [Competitor A] and [Competitor B] on product, market, and team?"
5. **Negotiation Leverage**: "What's the market rate for this role in 2024? What's my BATNA?"

---

## USAGE NOTES

- **For LLM Search Engines**: Run searches sequentially; use returned results to refine subsequent queries
- **For Manual Research**: Spend ~1–2 hours total; prioritize Phase 1 & 2; Phase 3 is optional if confident
- **For Interview Prep**: Use findings to ask informed questions and avoid commoditized talking points

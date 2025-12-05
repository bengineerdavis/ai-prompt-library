# Meta-Prompt: Job Research & Intelligence Gathering
## Universal Adaptive Framework for Any Job Description
### Auto-Extracts Variables | Validates Role/Company | Optional Resume Matching

<!-- 
https://www.perplexity.ai/search/use-the-seed-prompts-and-its-a-4x8xKgXxTcSM96eOflD_Aw?preview=1


---

## PURPOSE
Transform any job posting into a structured research plan by:
1. **Checking for resume** to enable personalized matching (optional)
2. **Validating** that the role and company actually exist
3. **Auto-extracting** 9 key variables from the posting
4. **Analyzing match quality** (if resume provided)
5. **Identifying follow-up questions** (informed by resume + research)
6. **Running structured research** based on confirmed variables

---

## EXECUTION FLOW

### Step 0: Resume Check (Adaptive Branch)

**Input**: Paste your job posting OR provide company name + role title.

**System will ask**:
```
❓ RESUME AVAILABILITY

To help you best, I can either:
a) Use your resume to assess match quality + generate targeted questions
b) Run generic job research without personal matching

Do you have a resume attached or want to upload one?
   [UPLOAD RESUME] [SKIP - GENERIC RESEARCH] [BRIEF BIO]

Why this helps (if provided):
- Compare your skills to posted requirements
- Identify gaps and strengths
- Generate personalized follow-up questions
- Assess fit (strong / medium / stretch)
```

**If resume provided**, parse for:
- Current/recent role and seniority level
- Technical skills (languages, tools, frameworks)
- Years in relevant domains (e.g., "X years in support", "Y years in infrastructure")
- Company backgrounds (startups vs. enterprises, known companies)
- Career trajectory signals (support→engineering path visible? management experience?)

**If no resume provided**, skip to Step 1 (generic research continues normally)

---

-->

### Step 1: Role & Company Validation Search

**Before extracting details**, run validation searches:

**Search V1: Company + Role Existence Check**
- **Query**: `{company_name_from_posting} {role_title_from_posting} careers hiring 2024 2025`
- **Goal**: Confirm company exists, role is real, recent posting date
- **Signals to validate**:
  - ✓ Company appears in Google results, LinkedIn, Crunchbase
  - ✓ Role appears on company careers page or LinkedIn jobs
  - ✓ Recent posting (within last 30 days ideal, 90 days acceptable)
  - ⚠ Old posting (3+ months) → May be inactive or recycled
  - ✗ No results → Company or role may not exist OR posting may be confidential

**Search V2: Company Name Discovery (if unknown)**
- **Query**: `{COMPANY_SIGNALS} {COMPANY_INDUSTRY} startup company 2024`
- **Goal**: Discover actual company name from pedigree signals
- **Example**: "ex-Waymo AI startup fast-growing 2024" → Identify company

**Search V3: Role Type Validation**
- **Query**: `{ROLE_TITLE} {COMPANY_INDUSTRY} job market exists 2024`
- **Goal**: Confirm this role type is real/common OR assess if it's specialized/niche
- **Example**: "Staff Infrastructure Engineer AI/ML" → Real role? Common or rare?

**Display validation results**:
```
═══════════════════════════════════════════════════════════════
VALIDATION RESULTS
═══════════════════════════════════════════════════════════════

✓ COMPANY EXISTS
  Found: [Company name, LinkedIn profile, founding year, recent funding]
  Confidence: [~95%] Company is real and actively hiring

✓ ROLE EXISTS
  Found: [Posted on company careers page, LinkedIn, other job boards]
  Confidence: [~90%] Role is recent (posted 15 days ago)

✓ ROLE TYPE IS REAL
  Found: [X other companies hiring for similar role]
  Market demand: [High / Medium / Low]
  Confidence: [~85%] This is a real/marketable role type

═══════════════════════════════════════════════════════════════
```

---

### Step 2: Variable Extraction & Resume Analysis (Adaptive)

**If resume was provided:**

Display resume analysis against posting:

```
═══════════════════════════════════════════════════════════════
RESUME ANALYSIS vs. JOB POSTING
═══════════════════════════════════════════════════════════════

YOUR BACKGROUND
├─ Current: Technical Support Engineer at Airbyte
├─ Years in support: 4 years
├─ Years in startups: 5 years
└─ Location: [From resume]

JOB REQUIREMENT
├─ Role: Technical Support Engineer
├─ Years required: 2+ years
└─ Industry: AI/ML startups

═══════════════════════════════════════════════════════════════
MATCH ASSESSMENT
═══════════════════════════════════════════════════════════════

Overall Match: STRONG FIT [~85% confident]
├─ Role alignment: ✓ Exact match (Support Eng → Support Eng)
├─ Experience level: ✓ Exceeds requirement (4 years > 2+ required)
├─ Technical skills:
│  ├─ Required [8/9 match]: Linux ✓, Docker ✓, Kubernetes ✓, 
│  │                         Python ✓, Java ✓, Go ✗
│  └─ Nice-to-have [5/6]: Distributed systems ✓, ...
├─ Industry background: ✓ AI/ML startup experience (Airbyte)
├─ Company size match: ✓ Similar startup stage
└─ Growth trajectory: ⚠ Support role; IC path unclear from resume

═══════════════════════════════════════════════════════════════
GAPS & QUESTIONS
═══════════════════════════════════════════════════════════════

Minor gaps:
├─ Go experience: You don't have it; 1 of 9 required languages
├─ Unknown: Your Python depth (junior vs. fluent?)
└─ Unknown: Your on-call experience and scope

═══════════════════════════════════════════════════════════════
```

**Now extract variables** (same for both resume and no-resume flows):

## INLINE CONFIDENCE LEGEND
**Show this at top of extraction summary output:**

```
═══════════════════════════════════════════════════════════════
CONFIDENCE LEGEND (Quick Reference)
═══════════════════════════════════════════════════════════════
✓ [~90–100%] Explicit: Stated directly in posting → [KEEP]
⚠ [~50–75%]  Inferred: Deduced from context → [REVIEW / EDIT]
✗ [~0–40%]   Missing: Not found in posting → [PROVIDE]
═══════════════════════════════════════════════════════════════
```

---

## EXTRACTION VARIABLES (9 Total)

### Variables to Extract (with confidence markers)

| # | Variable | Extracted Value | Confidence | Status | Action |
|---|----------|-----------------|------------|--------|--------|
| 1 | `{COMPANY_NAME}` | [auto-extracted or "unknown"] | [~XX%] | ✓ / ⚠ / ✗ | [Keep / Edit / Provide] |
| 2 | `{COMPANY_INDUSTRY}` | [auto-extracted] | [~XX%] | ✓ / ⚠ / ✗ | [Keep / Edit / Provide] |
| 3 | `{ROLE_TITLE}` | [auto-extracted] | [~XX%] | ✓ / ⚠ / ✗ | [Keep / Edit / Provide] |
| 4 | `{KEY_SKILLS}` | [auto-extracted] | [~XX%] | ✓ / ⚠ / ✗ | [Keep / Edit / Provide] |
| 5 | `{EXPERIENCE_REQUIRED}` | [auto-extracted] | [~XX%] | ✓ / ⚠ / ✗ | [Keep / Edit / Provide] |
| 6 | `{COMPANY_STAGE}` | [auto-extracted or inferred] | [~XX%] | ✓ / ⚠ / ✗ | [Keep / Edit / Provide] |
| 7 | `{COMPANY_SIGNALS}` | [auto-extracted] | [~XX%] | ✓ / ⚠ / ✗ | [Keep / Edit / Provide] |
| 8 | `{HIRING_PATTERN}` | [auto-extracted or "unclear"] | [~XX%] | ✓ / ⚠ / ✗ | [Keep / Edit / Provide] |
| 9 | `{YOUR_ROLE}` | [user context] | [~XX%] | ✓ / ⚠ / ✗ | [Keep / Edit / Provide] |

---

## EXTRACTION PHASE: WHAT TO LOOK FOR

### 1. `{COMPANY_NAME}` 
**Search the posting for**:
- Explicit company name (often in header or "About us")
- Company website or email domain
- Descriptions like "fastest-growing AI company" paired with any identifying signals
- Recruitment partner name (may indicate who to ask)

**If not found**: Mark as "unknown" → will use `{COMPANY_SIGNALS}` as fallback for discovery searches

**Extraction Example**: 
```
Posting: "Software Recruitment Solutions is partnered with one of the fastest-growing AI companies..."
Extraction: {COMPANY_NAME} = "unknown" [~10%], but inferred to be fast-growing AI startup
```

---

### 2. `{COMPANY_INDUSTRY}`
**Search the posting for**:
- Explicit industry language (e.g., "healthcare", "fintech", "AI/ML", "DevOps")
- Product description (e.g., "SaaS platform for X")
- Problem space (e.g., "solving data integration challenges")
- Customer profile hints (e.g., "Fortune 500 enterprises")

**Extraction Example**:
```
Posting: "fastest-growing AI companies building cutting-edge engineering tools"
Extraction: {COMPANY_INDUSTRY} = "AI/ML" [~90%]
Secondary: ["SaaS", "Enterprise Software"]
```

---

### 3. `{ROLE_TITLE}`
**Search the posting for**:
- Role title in header (e.g., "Senior Backend Engineer")
- Alternative titles listed (e.g., "Technical Support Engineer | AI Support Engineer | Product Support Engineer")
- Seniority level (Junior, Mid, Senior, Staff, Lead, Principal)
- Functional category (Engineer, Product Manager, Sales, Support, etc.)

**Extraction Example**:
```
Posting: "AI Support Engineer | Technical Support Engineer | Product Support Engineer"
Extraction: {ROLE_TITLE} = "Technical Support Engineer (Support tier)" [~95%]
Alternatives: ["AI Support Engineer", "Product Support Engineer"]
```

---

### 4. `{KEY_SKILLS}`
**Search the posting for**:
- "Required skills:" section
- "Must have:" bullets
- Programming languages, tools, frameworks
- Technologies (Kubernetes, Docker, PostgreSQL, Python, Go, Java, etc.)
- Soft skills or domain expertise

**Extraction Example**:
```
Posting: "Strong Linux Knowledge of distributed computing, containerization, and orchestration 
technologies (e.g. Docker, Kubernetes) Experience with programming languages such as Python, Java, or Go"
Extraction: {KEY_SKILLS} = "Linux, Docker, Kubernetes, Python, Java, Go" [~98%]
```

---

### 5. `{EXPERIENCE_REQUIRED}`
**Search the posting for**:
- "X+ years of experience"
- "Must have worked in [domain]"
- "Required background"
- "Minimum qualifications"

**Extraction Example**:
```
Posting: "2+ years in a technical role supporting enterprise-level customers"
Extraction: {EXPERIENCE_REQUIRED} = "2+ years enterprise technical support" [~95%]
```

---

### 6. `{COMPANY_STAGE}`
**Search the posting for (explicit)**:
- "Series A / B / C / D" funding stage
- "Pre-revenue", "Bootstrapped", "Public"
- "Early-stage startup", "Mature company"

**Infer from (signals)**:
- Headcount hints ("we're 50 people" → likely Series A–B)
- Funding mentions ("raised $50M" → likely Series C–D)
- Customer profile ("Fortune 500 clients" → likely Series C+)
- Hiring volume ("we're hiring 20+ roles" → growth stage)

**Extraction Example**:
```
Posting: "fastest-growing AI startups"
Direct statement: None found [~0%]
Inferred signals: "ex-ScaleAI, Waymo, Tesla, DeepMind" (senior talent) 
  + "Fortune 500 enterprises" (traction)
  + "world-class team" (fundraising appeal)
  → Inferred {COMPANY_STAGE} = "Series B–C" [~60%]
```

---

### 7. `{COMPANY_SIGNALS}`
**Search the posting for**:
- Team pedigree: "ex-Google", "ex-Meta", "ex-Uber", etc.
- Founding info: "founded 2022", "founded by X"
- Funding mentions: "backed by Y investors"
- Awards or recognition
- Culture hints: "remote-friendly", "collaborative", "fast-paced"
- Product mentions: "used by Fortune 500", "millions of users"
- Bootstrapped signals: "bootstrapped", "profitability", "sustainable"

**Extraction Example**:
```
Posting: "world-class team (ex ScaleAI, Waymo, Tesla, DeepMind and more) solving some 
of the most complex issues within AI"
Extraction: {COMPANY_SIGNALS} = "ex-ScaleAI, Waymo, Tesla, DeepMind talent; 
AI-focused; enterprise problem-solving" [~95%]
```

---

### 8. `{HIRING_PATTERN}`
**Search the posting for**:
- Hiring volume: "we're hiring 5+ roles" (volume) vs. "rare opportunity" (selective)
- Frequency of posting: Is this a recurring posting?
- Role description depth: Highly detailed (selective, high bar) vs. generic (volume hiring)
- Recruitment method: Direct LinkedIn (selective) vs. agency recruiting (often volume)

**Extraction Example**:
```
Posting tone: "rare opportunity to join", specific team context, agency recruiting
Inferred {HIRING_PATTERN} = "selective but via recruiter" [~70%]
```

---

### 9. `{YOUR_ROLE}` (Context about You)
**User provides** (now informed by resume analysis if available):
- Current role (e.g., "Technical Support Engineer at Airbyte")
- Career stage (e.g., "Senior IC evaluating IC vs. manager path")
- Goals (e.g., "target Netflix/Oxide roles")
- Constraints (e.g., "remote-only", "visa sponsorship needed")
- Match quality vs. this role (from resume comparison above, if resume provided)

**Extraction**: Informed by resume analysis (if available); affects which Phase 2/3 searches matter most

---

## CONFIRMATION PHASE

After extraction, display (same for both flows):

```
═══════════════════════════════════════════════════════════════
CONFIDENCE LEGEND (Quick Reference)
═══════════════════════════════════════════════════════════════
✓ [~90–100%] Explicit: Stated directly in posting → [KEEP]
⚠ [~50–75%]  Inferred: Deduced from context → [REVIEW / EDIT]
✗ [~0–40%]   Missing: Not found in posting → [PROVIDE]
═══════════════════════════════════════════════════════════════

EXTRACTION SUMMARY & CONFIRMATION
═══════════════════════════════════════════════════════════════

✓ HIGH CONFIDENCE [~85–100%] (Keep as-is)
├─ {ROLE_TITLE}: Technical Support Engineer [~95%]
├─ {KEY_SKILLS}: Linux, Docker, Kubernetes, Python, Java, Go [~98%]
└─ {EXPERIENCE_REQUIRED}: 2+ years enterprise support [~95%]

⚠ MEDIUM CONFIDENCE [~50–75%] (Review & confirm or edit)
├─ {COMPANY_INDUSTRY}: AI/ML [~90%]
├─ {COMPANY_STAGE}: Series B–C [~60%] [?] ← CLICK TO EDIT
└─ {COMPANY_SIGNALS}: ex-ScaleAI, Waymo talent [~85%] [?] ← CLICK TO EDIT

✗ MISSING OR UNKNOWN [~0–40%] (Please provide)
├─ {COMPANY_NAME}: unknown [~10%] 
│  → Needed for Phase 1 searches (company-specific queries)
│  → Fallback: Using {COMPANY_SIGNALS} for discovery
│  → ACTION: Provide company name if known, or confirm "discover via signals"
│
├─ {HIRING_PATTERN}: Unclear [~30%]
│  → Could not infer from posting tone
│  → ACTION: Is hiring selective or high-volume?
│
└─ {YOUR_ROLE}: [From resume if provided, otherwise user input needed]

═══════════════════════════════════════════════════════════════
NEXT STEPS
═══════════════════════════════════════════════════════════════

1. REVIEW: Scan the confidence levels above
2. EDIT: Click [?] to edit any medium-confidence or questionable extractions
3. CONFIRM: Provide missing values or confirm "use fallback/discovery mode"
4. PROCEED: Once confirmed, I'll run targeted research + identify key follow-up questions

═══════════════════════════════════════════════════════════════
```

---

## INTERACTIVE CONFIRMATION WORKFLOW

Once variables are extracted, show this interactive checklist:

```
╔════════════════════════════════════════════════════════════╗
║  CONFIRM VARIABLES BEFORE RESEARCH (9 Total)             ║
╚════════════════════════════════════════════════════════════╝

1. □ {COMPANY_NAME}
   Currently: unknown [~10%]
   Recommendation: [EDIT] [CONFIRM "DISCOVERY MODE"]
  
2. □ {COMPANY_INDUSTRY}
   Currently: AI/ML [~90%]
   Recommendation: [KEEP] [EDIT]
  
3. □ {ROLE_TITLE}
   Currently: Technical Support Engineer [~95%]
   Recommendation: [KEEP] [EDIT]
  
4. □ {KEY_SKILLS}
   Currently: Linux, Docker, Kubernetes, Python, Java, Go [~98%]
   Recommendation: [KEEP] [EDIT]
  
5. □ {EXPERIENCE_REQUIRED}
   Currently: 2+ years enterprise support [~95%]
   Recommendation: [KEEP] [EDIT]
  
6. □ {COMPANY_STAGE}
   Currently: Series B–C (inferred) [~60%]
   Recommendation: [KEEP] [EDIT/CONFIRM]
  
7. □ {COMPANY_SIGNALS}
   Currently: ex-ScaleAI, Waymo, Tesla, DeepMind [~85%]
   Recommendation: [KEEP] [EDIT]
  
8. □ {HIRING_PATTERN}
   Currently: Selective, via recruiter [~70%]
   Recommendation: [KEEP] [EDIT]
  
9. ✓ {YOUR_ROLE}
   Currently: [From resume analysis if provided, or user input]
   Status: [READY]

[PROCEED TO RESEARCH & GENERATE KEY QUESTIONS]
```

---

## EDIT WORKFLOW

When user clicks [EDIT] on a field:

```
⚠ EDITING: {COMPANY_STAGE}

Current: "Series B–C (inferred)" [~60%]
Confidence: Inferred from team seniority + customer profile, not explicit

Options:
a) Keep as "Series B–C" [~60%]
b) Change to: [INPUT TEXT]
c) Mark as "unknown, will discover" [~0%]

Provide new value or select option: _________________

[CONFIRM EDIT] [CANCEL]
```

---

## FINALIZATION PROMPT

Once all variables confirmed:

```
═══════════════════════════════════════════════════════════════
RESEARCH PARAMETERS CONFIRMED (9 Variables)
═══════════════════════════════════════════════════════════════

1. ✓ COMPANY_NAME: unknown → using discovery mode
2. ✓ COMPANY_INDUSTRY: AI/ML
3. ✓ ROLE_TITLE: Technical Support Engineer
4. ✓ KEY_SKILLS: Linux, Docker, Kubernetes, Python, Java, Go
5. ✓ EXPERIENCE_REQUIRED: 2+ years enterprise support
6. ✓ COMPANY_STAGE: Series B–C (inferred)
7. ✓ COMPANY_SIGNALS: ex-ScaleAI, Waymo, Tesla, DeepMind talent
8. ✓ HIRING_PATTERN: Selective, via recruiter
9. ✓ YOUR_ROLE: Senior IC targeting Netflix-like roles

═══════════════════════════════════════════════════════════════
RESEARCH PLAN
═══════════════════════════════════════════════════════════════

Given your context:
- Fast-growing AI startup, Series B–C stage
- Technical Support Engineer role, 2+ years required
- [IF RESUME PROVIDED: You're a STRONG FIT (85%); will highlight gaps + growth path]
- [IF NO RESUME: Generic assessment mode]

I will prioritize:
1. Phase 1 (Company): Funding, financial health, product-market fit [35%]
2. Phase 2 (Role): IC/manager track clarity, team health, compensation [40%]
3. Phase 3 (Market): AI support eng career viability, market demand [15%]
4. Follow-ups: Culture deep-dive (Blind posts), manager quality [10%]

Ready to begin? [START RESEARCH] [ADJUST PRIORITIES] [CANCEL]
```

---

## ADAPTIVE OUTPUT: FOLLOW-UP QUESTIONS

**If resume was provided**, generate targeted follow-up questions based on gaps + research:

```
═══════════════════════════════════════════════════════════════
KEY FOLLOW-UP QUESTIONS FOR YOUR INTERVIEW
═══════════════════════════════════════════════════════════════
Based on: Resume analysis [STRONG FIT] + Research findings + Gap identification

TIER 1 (Ask early / in initial call)
├─ Career trajectory: "I see you have 4 years of support experience. 
│  What's the path from this role to backend/IC roles at your company?"
│
├─ Go experience gap: "I have strong Python experience but limited Go. 
│  How critical is Go proficiency for day-1, vs. something I'd learn on the job?"
│
└─ On-call expectations: "From your posting, I'm inferring this involves on-call support. 
   What does the typical rotation look like? How many incidents per week?"

TIER 2 (Dig deeper if you like the role)
├─ Team health: "Walk me through the team structure. How stable is the support team? 
│  Any recent hires or departures?"
│
├─ Learning culture: "Your team has ex-Waymo and ex-ScaleAI talent. 
   How hands-on is mentorship? What's an example of someone growing in this role?"
│
└─ Compensation & equity: "What's the equity structure? Any signing bonus or flexibility?"

TIER 3 (Before final yes/no)
├─ Company momentum: "Your Series B–C stage signals growth. What's your hiring roadmap for 2025?"
│
├─ Manager quality: [Research findings will suggest]: "I found positive/neutral/mixed 
   reviews on Blind. Can you walk me through your management philosophy?"
│
└─ Risk factors: "Any near-term changes to the support team or company direction I should know about?"

═══════════════════════════════════════════════════════════════
```

**If no resume was provided**, generate generic follow-up suggestions:

```
═══════════════════════════════════════════════════════════════
SUGGESTED FOLLOW-UP QUESTIONS
═══════════════════════════════════════════════════════════════
[No resume analyzed; generic suggestions based on role + company research]

TIER 1 (Role clarity)
├─ What does day-1 look like? What incidents/problems will I handle?
├─ What's the on-call rotation and incident volume?
└─ Who would I report to? Can I speak with them?

TIER 2 (Team & culture)
├─ How's the team structured? Team size and recent changes?
├─ How do you support learning and growth for people in this role?
└─ What's the compensation structure (base + equity)?

TIER 3 (Company)
├─ [From research] What's your hiring roadmap?
├─ [From research] Any risks I should be aware of?
└─ What would success look like in the first 3–6 months?

═══════════════════════════════════════════════════════════════
```

---

## FULL RESEARCH DECOMPOSITION

### Phase 1: Company Intelligence (35% of effort)

**Search 1.1: Company Identity & Funding**
- **Query (with variables)**: `{COMPANY_SIGNALS} {COMPANY_INDUSTRY} startup funding Series 2024 2025`
- **Goal**: Identify company name, funding stage, valuation, investor profile
- **Confidence**: High when using confirmed `{COMPANY_SIGNALS}` + `{COMPANY_STAGE}`

**Search 1.2: Company Mission & Product**
- **Query**: `[discovered company name] product vision market {COMPANY_INDUSTRY}`
- **Goal**: Understand product, target market, differentiation

*[Continues with Phase 1–3 as before, using confirmed variables...]*

---

## EPISTEMIC HONESTY & EXTRACTION CAVEATS

**Where extraction might be wrong**:
- **Recruiting agencies** (like "Software Recruitment Solutions") may obscure actual company names intentionally
- **Generic role titles** ("Technical Support Engineer") could mask wide scope variations
- **Inferred company stage** from signals alone is often 60–70% confident; actual stage may differ significantly
- **Missing company name** requires discovery mode; searches may surface false positives
- **Resume analysis** (if provided): Limited by what's documented on resume; hidden skills or recent work not included won't show up

**Guardrail**: Always note confidence levels; if a variable is <50% confident, flag it for user confirmation before running research

---

## SUMMARY

This universal adaptive meta-prompt:
1. ✅ **Checks for resume** and branches to personalized or generic flow
2. ✅ **Validates** that role and company actually exist before deep analysis
3. ✅ **Requests resume** (optional) to assess match quality and identify gaps
4. ✅ **Analyzes resume** against posting requirements (if provided): skills %, experience level, industry fit
5. ✅ **Auto-extracts** 9 key variables from any job posting
6. ✅ **Confidence-marks** each extraction (high/medium/low)
7. ✅ **Includes inline legend** at top of output for quick reference
8. ✅ **Flags missing** values with specific prompts
9. ✅ **Generates targeted follow-up questions** (personalized if resume provided; generic if not)
10. ✅ **Prioritizes research** based on confirmed variables and your background
11. ✅ **Maintains epistemic honesty** about extraction limitations and assumptions
12. ✅ **Works for anyone** (personal use with resume, or generic use without)

**Result**: Single unified prompt that adapts to whether you provide a resume—providing personalized candidate assessment when possible, generic research when not.

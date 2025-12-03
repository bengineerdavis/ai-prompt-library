# Skill & Experience Mapping Seed Prompt

## Purpose
Map your unique experience to job requirements, identify critical skill gaps, and develop a mitigation strategy for each gap before the interview.

## Core Seed Prompt

```
You are a career coach helping a job candidate assess fit for a specific role.

Given the following inputs:

**INPUT A: Job Description**
[PASTE_FULL_JOB_DESCRIPTION]

**INPUT B: Candidate Resume/LinkedIn Summary**
[PASTE_RESUME_OR_LINKEDIN_SUMMARY]

**INPUT C: Candidate Goals & Priorities**
[OPTIONAL: e.g., "I want to deepen AI skills", "I'm transitioning from support to leadership"]

TASK:
Analyze and provide the following:

---

**1. REQUIREMENT MAPPING**

Extract all explicit and implicit requirements from the job description:
- Must-have technical skills (e.g., Python, Kubernetes, leadership)
- Nice-to-have skills (e.g., specific certifications, frameworks)
- Implicit expectations (e.g., "move fast" = startup chaos tolerance; "cross-functional" = communication skills)
- Experience level signals (e.g., "5+ years" suggests architectural thinking, not just coding)

For each requirement, map the candidate's experience:
- **Strong Match (90%+)**: Direct, recent experience in this exact area
- **Partial Match (60-89%)**: Related experience that transfers well
- **Learnable (30-59%)**: Candidate understands foundations, can upskill quickly
- **Gap (0-29%)**: No clear background; requires significant learning or narrative framing

Create a table with columns: Requirement | Candidate's Experience | Match Level | Evidence

---

**2. STRENGTH POSITIONING**

Identify 3-5 unique strengths the candidate brings that aren't common in the market:
- For each strength, provide:
  a) What the strength is (e.g., "scaled support at 200% YoY growth")
  b) Why it's rare (e.g., "most candidates haven't managed teams through that pace")
  c) How to frame it in the interview (e.g., "You've managed crises while maintaining team morale")
  d) Relevance to this specific role (e.g., "This role needs someone who can prioritize under pressure")

---

**3. GAP MITIGATION STRATEGY**

For each identified gap (Learnable or Gap level), provide:

a) **Severity Assessment:**
   - Blocker: Critical to success; must address before interview
   - Learnable: Can address with 1-2 weeks of focused effort
   - Narrative-able: Can frame existing experience as transferable

b) **Mitigation Tactic:**
   - Take a weekend course and deploy a small project
   - Read key blog posts or documentation and summarize findings
   - Leverage similar past experience to show learning ability
   - Ask hiring manager during interview: "I haven't used X in production, but I've built Y. How does this role use X?"

c) **Narrative Framing:**
   - "I haven't worked with [Tool], but here's how my [Related Experience] transfers:"
   - "I'm actively learning [Skill] through [Course/Project]. Here's what I've built so far:"
   - "This role is exactly why I want to deepen [Skill]—I've struggled with it, and I'm committed to mastering it."

---

**4. RED FLAGS & MISALIGNMENT**

Identify and assess potential mismatches:
- Is this a growth opportunity or a mismatch? (e.g., IC role for someone seeking leadership)
- What would you need to see to be confident this is a fit?
- Are there any role characteristics that concern you?
- Is the company/role aligned with your 90-day goals?

---

**5. DECISION MATRIX**

Provide a summary recommendation:

| Dimension | Score (1-5) | Rationale |
|-----------|-------------|-----------|
| Technical Fit | [1-5] | % of skills match |
| Growth Opportunity | [1-5] | Chance to deepen target skills |
| Team/Culture Fit | [1-5] | Based on hiring manager + team research |
| Compensation Alignment | [1-5] | Based on market research |
| **Overall Recommendation** | **[1-5]** | **Pursue / Pursue with Caution / Pass** |

---

**OUTPUT STRUCTURE:**

Provide findings in a clear, scannable format:
- Use tables for mapping
- Use bullet points for narratives and tactics
- Highlight gaps that are dealbreakers vs. learnable
- Suggest concrete next steps (e.g., "Take Terraform course before round 2")
```

## How to Use

1. **Gather inputs**: Full job description, updated resume, LinkedIn profile
2. **Run this prompt** after receiving the role details
3. **Focus on gaps**: For each "Learnable" gap, create a 1-week learning plan
4. **Practice narratives**: Rehearse gap-mitigation stories with a peer or coach
5. **Update as you learn**: After each interview round, refine your understanding of which skills matter most
6. **Cross-reference**: Compare this analysis to recruiter feedback

## Example: Filling Gaps

### Gap: "Terraform experience required, you have none"

**Severity**: Learnable (Infrastructure-as-Code concepts transfer from other tools)

**Mitigation Tactic**:
- Spend 4 hours Friday learning Terraform basics (HashiCorp tutorials)
- Deploy a small AWS infrastructure (e.g., EC2 + S3 bucket) using Terraform on Saturday
- Document the experience: "Why I chose Terraform for this" + learnings
- Push code to GitHub

**Narrative Framing**:
"I haven't used Terraform in production, but I've managed CloudFormation templates at [Previous Company]. I understand the Infrastructure-as-Code principles—state files, modules, dependency graphs. Over the weekend, I deployed a small AWS infrastructure using Terraform to get comfortable with the syntax. Here's what I learned..."

**Why this works**:
- Shows initiative and learning ability
- Proves you can pick up tools quickly
- Demonstrates understanding of the *why* (IaC principles), not just the *what* (Terraform syntax)
- Hiring managers respect candidates who invest time upfront

---

## Key Narratives to Prepare

### "I haven't used [Tool], but..."

Template:
```
"I haven't used [Tool] in production, but I have [Related Experience].
Here's how the concepts transfer:
- [Concept 1]: I did this with [Tool A]
- [Concept 2]: I've built this pattern multiple times

I'm actively learning [Tool] by [Specific Action].
Here's what I've built/learned so far: [Artifact or insight]."
```

### "This is exactly why I'm interested in this role"

Template:
```
"I've realized in my last role that [Gap/Weakness/Challenge].
This role is a perfect opportunity to deepen [Skill] because [Reason].
I've already started by [Action taken].
Here's my 90-day learning plan: [Outline]."
```

### "My background might look different, but here's why I'm a fit"

Template:
```
"My experience in [Previous Domain] might not look like [Expected Path], but here's why it's valuable:
- I've learned [Transferable Skill 1]
- I've solved [Similar Problem] in [Different Context]
- I bring [Unique Perspective] that most candidates don't have

Here's how that applies to this role: [Specific examples]."
```

---

## Related Documents
- See `recruiter-research.md` for hiring manager research
- See `salary-research.md` for compensation benchmarking
- See `critical-questions.md` for pre-screen call preparation
- See `company-research.md` for company background
- See `tracking-template.csv` for logging research across multiple opportunities

## Quick Checklist Before Your First Interview

- [ ] I've identified all skill gaps and their severity
- [ ] I've created a 1-week mitigation plan for each "Learnable" gap
- [ ] I've practiced 3-5 gap narratives with a peer
- [ ] I've identified my 3-5 unique strengths and how to position them
- [ ] I understand why this role aligns with my 90-day learning goals
- [ ] I'm ready to discuss gaps confidently, not defensively

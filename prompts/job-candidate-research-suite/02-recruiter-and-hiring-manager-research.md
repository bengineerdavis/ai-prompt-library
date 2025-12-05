# Recruiter & Hiring Manager Research Seed Prompt

## Purpose

Understand who is reaching out, their credibility, track record, and the broader hiring context (team health, stability, hiring manager style).

## Core Seed Prompt

You are helping a senior technical candidate evaluate a recruiter and hiring team for a potential role.
Using public information, research the following and provide a structured profile:

## PART A: Recruiter Profile

- **Name:** [RECRUITER_NAME]
- **Current company:** [COMPANY_NAME]
- **LinkedIn:** background, tenure at current company, previous roles, typical functions/levels they recruit for
- **Track record (confidence level):** evidence of successful placements or long‑term relationships (e.g., repeat roles with same hiring managers, recommendations, tenure in prior recruiting roles)
- **Reputation signals:** Any public feedback on this recruiter (Glassdoor comments, Blind mentions, Reddit threads, or other community forums). Note whether data is sparse.
- **Specialization:** Do they appear focused on technical roles, senior/lead talent, or a mix?
- **Outreach quality (subjective assessment):** Based on the initial message, does it appear personalized and grounded in the candidate's background, or generic / template‑driven?
- **Communication style (if any data):** Responsiveness, clarity about process, and ability to answer basic questions about role, team, and compensation.

*For each bullet in Part A, include a confidence level: High / Medium / Low.*

## PART B: Hiring Manager / Team Lead Profile

- **Name:** [HIRING_MANAGER_NAME] (if unknown, state that clearly and look for likely manager from job post and team structure)
- **LinkedIn:** career trajectory, seniority progression, time at each company, and time managing teams
- **Leadership signals:** Any posts, talks, podcasts, blog posts, endorsements, or conference appearances that reveal their views on management, engineering culture, or mentoring
- **Technical depth (where applicable):** GitHub activity, publications, patents, conference talks, or technical blog posts that indicate hands‑on experience or strong technical literacy
- **Management reputation:**
  - Any Glassdoor reviews that mention this person by name or title
  - Any Blind or Reddit posts referencing their team, organization, or leadership style
  - Any visible patterns of people leaving or being promoted under their org
- **Culture indicators:** What they seem to value in their team (based on LinkedIn posts, recommendations they've written, interviews, or public commentary).

*For each bullet in Part B, include a confidence level: High / Medium / Low, and highlight where you're inferring vs. citing explicit evidence.*

## PART C: Team Context

- **Team identity:** Likely team name/org (e.g., "Customer Support," "Platform Engineering," "Post‑Sales / Solutions") and where it sits in the org chart
- **Team size and structure (estimate):** number of peers in similar roles, reporting lines, and cross‑functional partners (e.g., product, infra, sales engineering)
- **Recent hires:** Evidence of growth (new joiners on LinkedIn in the past 6–12 months) and their profiles/seniority
- **Turnover signals:** People who have left the team/org in the past 12–24 months, including whether they moved sideways internally or left the company entirely
- **Growth trajectory:** Whether job postings and LinkedIn suggest the team is expanding (multiple open roles, new levels) or consolidating (backfills only, fewer roles)
- **Cross‑references:** Any mentions of this team or manager in company blog posts, changelogs, incident writeups, open‑source contributions, or conference talks.

*Again, attach confidence levels to each item and explicitly note when public data is missing or too sparse to draw conclusions.*

## PART D: Hiring Process Signals

- **Typical timeline:** Any public or crowdsourced information on interview length (e.g., candidate posts, Glassdoor interview reviews, Reddit threads). If not available, state that.
- **Process structure:** Known stages (recruiter screen, hiring manager, panel, take‑home, etc.) and whether this seems consistent across similar roles at the company.
- **Feedback quality:** Any signals about how they handle rejections and feedback (brief or detailed, timely or slow).
- **Transparency:** Evidence that they communicate clearly about expectations, leveling, compensation bands, and remote vs. in‑office requirements.
- **Red flags:**
  - Vague or shifting role descriptions
  - Conflicting information between job post, recruiter message, and employee profiles
  - Signs of chaotic hiring (repeated job reposts, multiple failed searches, or many short‑tenured team members).

Provide a short **"Risk & Signal Summary"** at the end, explicitly listing:

- Green flags
- Yellow flags
- Red flags

## OUTPUT FORMAT & STYLE

- Organize the answer into the four parts above (A–D) plus the final Risk & Signal Summary.
- For every concrete data point, include a confidence level (High/Medium/Low).
- Call out "Data sparse / no reliable signal" where information cannot be found.
- Clearly separate facts (what is visible) from interpretation (what it likely means for a senior technical candidate).

Finally, suggest 5–7 follow‑up questions for the candidate to ask the recruiter directly, tailored to:

- Clarifying team health and turnover
- Understanding the hiring manager's style and expectations
- Confirming the realism of the role's scope, seniority, and growth path.



## Related Documents
- See `skill-mapping.md` for role fit analysis
- See `salary-research.md` for compensation benchmarking
- See `critical-questions.md` for pre-screen call preparation
- See `tracking-template.csv` for logging research across multiple opportunities

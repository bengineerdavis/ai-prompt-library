# Content Optimizer - Usage Guide

A metaprompt for optimizing personal content (blog posts, social media, website copy) while preserving your authentic voice and technical depth.

## What is This?

Content Optimizer is a metaprompt based on the Seed framework that acts as your personal editor. It helps you improve readability and engagement without turning your writing into corporate speak or stripping away technical substance.

**Core principles:**
- Preserve your authentic voice
- Prioritize scannability without dumbing down
- Make minimal edits necessary
- Always explain changes and get approval

## Who is This For?

Technical practitioners (senior ICs, engineers, researchers) who:
- Share insights on LinkedIn, personal blogs, or social media
- Want to improve readability without losing technical depth
- Value authenticity over polish
- Want to attract builders and collaborators, not just engagement

## Quick Start

### Option 1: Use with ChatGPT, Claude, or Perplexity

1. Copy the entire `content-optimizer.md` file
2. Paste it into a new chat session
3. (Optional) Set configuration parameters:
   ```
   research_mode: deep
   strategy_check: true
   timing_check: true
   source_approval: true
   ```
4. Share your content with context:
   ```
   Platform: LinkedIn
   Goal: Find collaborators interested in prompt engineering
   Audience: Technical practitioners
   Concern: Post feels too long and buries the lede
   
   Links I have: [list any references]
   Previous posts on this topic: [paste or summarize if relevant]
   
   [Your content here]
   ```
5. Review the source analysis file (if claims need validation)
6. Approve sources and address counterpoints
7. Review the proposed edits
8. Accept, modify, or reject changes
9. Provide feedback so the system learns your preferences

### Option 2: Use with Local LLM (Ollama, LM Studio)

Same process as above, but paste the metaprompt into your local LLM interface.

**Recommended models:**
- qwen2.5:14b or larger
- llama3.1:8b or larger
- mistral:7b or larger

**Note:** Deep research mode requires web search capability. If your local LLM doesn't have web access, stick with `research_mode: light` and provide your own sources.

## How It Works

The Content Optimizer follows a multi-step process:

**Step 0: Capture Context** - Understands your platform, goal, audience, and concerns

**Step 0.5: Research & Strategy Context** - Gathers links, sets research mode, checks strategy alignment, considers timing

**Step 0.6: Source Validation & Approval** - Validates factual claims, presents sources with confidence scoring, waits for your approval

**Step 1: Analyze Structure** - Scores content on clarity, scannability, voice, alignment, engagement

**Step 2: Identify Issues** - Flags specific problems with examples

**Step 3: Propose Minimal Edits** - Shows before/after with rationale

**Step 4: Restructure if Needed** - Suggests major changes only when necessary (>75% confidence)

**Step 5: Optional Enhancements** - Suggests improvements (but doesn't force them)

**Step 6: Feedback Loop** - Learns your preferences over time

### Key Features

**Source Validation:**
- Generates separate `source-analysis-[topic].md` file
- Validates all factual claims before optimization
- Provides confidence scores (high/medium/low) with explicit reasoning
- Identifies meaningful counterpoints using 6-criteria framework
- Waits for your approval before incorporating sources

**Research Modes:**
- **Light** (default): Reminds about missing links, suggests research for unsupported claims
- **Deep**: Actively searches web for supporting evidence + counterpoints, provides summaries

**Strategy Integration:**
- Checks consistency with previous content
- Suggests follow-ups when natural extensions are spotted
- Considers timing (explicit deadlines + implicit time-sensitivity)
- Helps content fit into broader narrative

## Source Validation Deep Dive

One of the most important features is the source validation system, which ensures your content is factually accurate and well-supported.

### How It Works

**1. Claim Identification**
The optimizer scans your content for claims that need validation:
- Factual statements without attribution
- Statistics or data points
- Technical claims that could be disputed
- References to tools, papers, or people
- Time-sensitive information

**2. Research & Analysis**
For each claim, the optimizer (in deep research mode):
- Searches for supporting evidence
- Finds meaningful counterpoints (using 6-criteria framework)
- Evaluates source quality and confidence
- Provides 2-3 sentence summaries of each source

**3. Separate Analysis File**
Instead of cluttering the conversation, the optimizer generates:

```
source-analysis-[topic-slug].md
```

This file contains:
- All claims organized by topic
- Supporting sources with confidence scores
- Meaningful counterpoints with explicit criteria
- Recommendations for how to address gaps
- Checklist for your approval

**4. Confidence Scoring**
Every source gets a confidence rating with explicit reasoning:

**High confidence:**
- Peer-reviewed research
- Official documentation
- Recent data from credible sources
- Domain expert consensus

**Medium confidence:**
- Reputable blog posts
- Case studies with multiple examples
- Recent articles from established publications
- Expert opinions (single source)

**Low confidence:**
- Anecdotal evidence
- Dated information (>3 years for fast-moving fields)
- Non-expert opinions
- Unverified claims

**The reasoning is always shown so you can make informed decisions.**

### Meaningful Counterpoint Framework

Not all counterpoints are worth including. The optimizer uses these 6 criteria:

1. **Challenges core claims** - Disputes your main argument, not peripheral details
2. **Credible source** - From domain experts, peer-reviewed research, established practitioners
3. **Substantive evidence** - Provides data/reasoning, not just opinion
4. **Relevant to audience** - Matters to the practitioners/builders you're trying to reach
5. **Not easily dismissed** - Requires thoughtful response, not obvious rebuttal
6. **Recent/current** - Reflects current thinking (especially important for fast-moving fields)

**A counterpoint is "meaningful" if it meets ≥3 criteria.**

### Why This Matters

**For your credibility:**
- Practitioners can spot unsupported claims
- Including counterpoints shows intellectual honesty
- Proper sources build trust with your audience

**For your time:**
- Separate file means easier review
- Confidence scores help prioritize which sources to read
- Summaries let you evaluate relevance before clicking

**For your content:**
- Stronger arguments when you address counterpoints
- Better positioning in your field
- More likely to start substantive discussions

### Example: Source Analysis File

```markdown
# Source Analysis for: Recursive Introspection Post

## Claim 1: "Recursive introspection dramatically improves prompt quality"

**Supporting Sources:**

1. **Meta-Prompting Framework (Stanford, 2024)**
   - Link: [URL]
   - Type: Peer-reviewed paper
   - Summary: Controlled study with 100 participants showing 40% improvement 
     in prompt quality when using recursive self-improvement techniques.
     Measured across 5 task categories.
   - Supports claim: Yes (directly validates)
   - Confidence: **High**
   - Confidence reasoning: Peer-reviewed, recent (2024), controlled methodology, 
     large sample size, measured outcomes

**Meaningful Counterpoints:**

1. **Diminishing Returns in Iterative Prompting (arXiv, 2024)**
   - Link: [URL]
   - Summary: Study showing benefits plateau after 3 iterations, with 
     negligible gains beyond that point. Tested across multiple models.
   - Challenge: Suggests "dramatically" may overstate sustained benefits
   - Meaningful criteria met:
     ✓ Challenges core claim (1) - questions magnitude of improvement
     ✓ Credible source (2) - arXiv preprint from research team
     ✓ Substantive evidence (3) - empirical testing across models
     ✓ Recent/current (6) - 2024 publication
   - Confidence: **High**
   - How to address: Soften "dramatically" to "significantly" and add note 
     about 3-iteration sweet spot

**Recommendation:** Use both sources. The counterpoint actually strengthens 
your argument by showing you're aware of limitations.
```

## Example Session

**Your input:**
```
research_mode: deep
Platform: LinkedIn
Goal: Share a useful AI technique and get feedback from practitioners
Concern: Post feels too cynical at the start, not sure if claims are well-supported

[Your draft post]
```

**Step 0-0.5: Context & Research Setup**
- Platform: LinkedIn
- Research mode: deep
- Goal confirmed: Share technique + get practitioner feedback
- Timing: No urgency, evergreen content
- Links provided: [1 blog post on recursive introspection]

**Step 0.6: Source Validation**

Generated file: `source-analysis-recursive-introspection.md`

```markdown
# Source Analysis for: Recursive Introspection Post

## Claims Requiring Validation

### Claim 1: "Recursive introspection dramatically improves prompt quality"

**Supporting Sources:**
1. **Meta-Prompting Framework (Stanford, 2024)**
   - Confidence: High (peer-reviewed, recent methodology)
   - Summary: Study showing 40% improvement in prompt quality...
   
2. **Practitioner Case Studies (Anthropic Blog)**
   - Confidence: Medium (anecdotal but multiple examples)
   - Summary: 5 case studies from production use...

**Meaningful Counterpoints:**
1. **Diminishing Returns Study (arXiv, 2024)**
   - Challenge: Shows benefits plateau after 3 iterations
   - Criteria met: Credible (4), Substantive (3), Recent (6)
   - How to address: Add nuance about iteration limits

**Recommendation:** Soften "dramatically" to "significantly" and add note about 3-iteration sweet spot
```

**Your approval:** "Use sources 1 & 2, address counterpoint by adding nuance about iteration limits"

**Step 1-3: Analysis & Edits**
- Structural analysis with scores
- Specific issues flagged with quotes
- Minimal edits with explanations (including source integration)
- Restructured opening (earnest vs cynical)

**Step 4-5: Optional Enhancements**
- Suggested follow-up: "You could write a follow-up on when NOT to use recursive prompting"
- You: "Good idea, let's queue that"

**Step 6: Feedback Loop**
- What worked: Deep research found great counterpoint that strengthened argument
- What didn't: Initial analysis was too aggressive on tone
- Logged preference: "Author wants earnest but not corporate, technical depth with caveats"

**Result:**
- Improved content with validated sources
- Natural integration of counterpoint (adds credibility)
- Still sounds like you
- Clear follow-up idea captured

## Configuration Parameters

You can set these at the start of each session (or eventually in a config file):

### Research Mode
- `research_mode: "light"` **(default)** - Reminds about missing links, suggests research for unsupported claims
- `research_mode: "deep"` - Actively searches web for supporting + counter evidence, provides summaries

### Strategy Check
- `strategy_check: true` **(default)** - Asks about previous posts, suggests follow-ups
- `strategy_check: false` - Skip strategy alignment, focus only on current content

### Timing Check
- `timing_check: true` **(default)** - Asks about timeline + flags time-sensitive content
- `timing_check: false` - Assumes evergreen content, no timing considerations

### Source Approval
- `source_approval: true` **(default)** - Presents sources and waits for approval before using
- `source_approval: false` - Incorporates sources automatically (not recommended)

### Follow-up Suggestions
- `suggest_followups: "auto"` **(default)** - Suggests when natural extensions spotted
- `suggest_followups: "always"` - Always suggests follow-up topics
- `suggest_followups: "never"` - Skip follow-up suggestions

### Example Usage

**Minimal (use defaults):**
```
Platform: LinkedIn
Goal: Share a technique and get feedback
[Your content]
```

**Explicit configuration:**
```
research_mode: deep
strategy_check: true
timing_check: true
source_approval: true

Platform: LinkedIn
Goal: Share a technique and get feedback
Links: [list your links]
Previous posts: [summarize if relevant]

[Your content]
```

## Platform-Specific Tips

### LinkedIn
- **Best for:** Sharing resources, starting discussions, finding collaborators
- **Structure:** Front-load value → Details → Call-to-action
- **Tone:** Earnest and helpful (cynicism underperforms)
- **Format:** Use line breaks and bold headers for mobile readability

### Blog Posts
- **Best for:** Deep dives, tutorials, long-form thinking
- **Structure:** Clear sections with headers, examples, code snippets
- **Tone:** Technical depth is welcome
- **Format:** SEO-friendly headers, scannable but comprehensive

### Twitter Threads
- **Best for:** Quick insights, connecting ideas, starting conversations
- **Structure:** Hook → Context → Insight → Close
- **Tone:** Conversational, one clear idea per tweet
- **Format:** Links in final tweet, visual breaks between concepts

### Personal Website
- **Best for:** Portfolio, professional presence, showcasing work
- **Structure:** Clean sections, clear hierarchy
- **Tone:** Show personality + expertise
- **Format:** Assume readers are evaluating you

## Customization

The metaprompt learns your preferences over time. After each session, it logs:
- **Tone preferences** (e.g., "Author prefers directness over softening language")
- **Structural patterns** (e.g., "Always use headers for posts >200 words")
- **Platform quirks** (e.g., "LinkedIn posts work better with explicit CTAs")
- **Voice markers** (e.g., "Author uses technical specificity as a trust signal")
- **Source preferences** (e.g., "Prefers peer-reviewed sources over blog posts", "Always include counterpoints when available")
- **Research depth** (e.g., "Usually needs deep research for technical claims, light research for opinion pieces")

You can also manually edit the "Version History & Learning" section in `content-optimizer.md` to capture persistent preferences.

## Real Example

This metaprompt was created by optimizing a LinkedIn post about AI discourse. Here's what changed:

**Original concern:** "Post feels too long, buries the lede, opening is too cynical"

**What the optimizer did:**
1. Proposed earnest opening vs. cynical (explained why)
2. Split dense paragraphs into scannable chunks
3. Added bold headers for structure
4. Fixed grammar/typos
5. Added call-to-action for engagement
6. Preserved all technical content and voice

**Result:** Same ideas, better readability, more aligned with goal of finding collaborators.

## Best Practices

### Do:
- Provide context upfront (platform, goal, audience)
- Be specific about concerns ("too long" vs "buries lede in paragraph 3")
- Review all changes before accepting
- Give feedback so the system learns
- Use it iteratively (draft → optimize → rewrite → optimize again)

### Don't:
- Expect it to write content from scratch (it's an optimizer, not a generator)
- Accept all edits blindly (you're the author, it's the editor)
- Skip the context step (garbage in, garbage out)
- Forget to update the learning section with persistent preferences

## Troubleshooting

**Problem:** Edits feel too corporate/sanitized
**Solution:** In feedback, say "This loses my voice—be more conservative with tone changes"

**Problem:** Not catching grammar/clarity issues
**Solution:** Explicitly ask "Focus on grammar and clarity this round, skip structural changes"

**Problem:** Suggesting too many changes
**Solution:** Add to context "Only flag high-impact issues, ignore minor style preferences"

**Problem:** Not understanding technical content
**Solution:** Add brief context about domain/terminology in your initial message

## Integration with Seed System

This metaprompt is a "Factory Pattern" within the larger Seed framework. If you're using the full Seed system:

1. The Seed Orchestrator can call Content Optimizer as a child pattern
2. The Seed Optimizer can propose improvements to Content Optimizer itself
3. Preference tracking integrates with your broader Seed preferences

If you're not using Seed, this works standalone—no dependencies required.

## Version History

**v2.0** (Current - Enhanced Research & Strategy)
- Added configurable parameters (research_mode, strategy_check, timing_check, source_approval, suggest_followups)
- Added Step 0.5: Research & Strategy Context for broader content planning
- Added Step 0.6: Source Validation & Approval with separate analysis markdown file
- Added explicit "meaningful counterpoint" criteria (6-point framework)
- Added confidence scoring with reasoning for all sources (high/medium/low)
- Added follow-up suggestion logic (spots natural extensions, asks before elaborating)
- Added timing considerations (explicit + implicit time-sensitivity)
- Improved: Factual accuracy validation now happens before optimization
- Improved: Source approval is separate stage with dedicated file for easier review

**v1.0** (Initial release)
- Based on LinkedIn post optimization session
- Supports LinkedIn, blog posts, Twitter threads, personal website
- Includes voice preservation, minimal edits, feedback loops
- Learned preferences: earnest > cynical, scannability + substance, preserve technical depth

## Future Enhancements

Potential improvements based on usage:
- **Config file**: Create `content-optimizer-config.json` for persistent parameter defaults (research_mode, strategy_check, etc.)
- **Platform-specific scoring weights**: Different criteria emphasis for LinkedIn vs blog posts
- **Voice marker library**: Common phrases, style patterns automatically detected
- **A/B testing suggestions**: Try 2-3 openings, evaluate which works best
- **Integration with analytics**: Track what performs well on each platform
- **Multi-format optimization**: Write once, optimize for each platform simultaneously
- **Source library**: Build database of high-quality sources for common topics
- **Automated follow-up tracking**: Queue suggested follow-up posts with context

## Contributing

Have ideas for improvements? Patterns that work well for your workflow? Open an issue or submit a PR.

Keep in mind:
- The core metaprompt should remain generic
- Platform-specific guidance can be expanded
- Learning/preference tracking should be flexible

## License

MIT

---

## Questions?

- **How is this different from Grammarly/Hemingway?** Those tools focus on grammar and readability metrics. This preserves voice and technical depth while improving structure.
- **Can I use this with AI tools other than ChatGPT?** Yes—works with any LLM that accepts long context (Claude, Perplexity, local models)
- **Will this make my writing sound like everyone else's?** No—the core principle is voice preservation. It structures your ideas better without changing your language.
- **Do I need the full Seed system?** No—this works standalone. Seed integration is optional.

---

**Ready to use it?** Copy `content-optimizer.md` and paste it into your LLM of choice with your content.

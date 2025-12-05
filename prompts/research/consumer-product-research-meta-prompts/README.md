# Product Research Universal Shopper v1.6 - README & Usage

## 🎯 One Prompt Does Everything

- **Product Research**: "mechanical keyboards under $150"
- **Upgrades**: "new PC vs 2024 research"  
- **Shopping Strategy**: "best time to buy GPUs 2025"
- **Use Cases**: "fitness tracker use cases BJJ"
- **Rollback**: "keyboards {model:perplexity,v1.4}"

## 🚀 Quick Start

### 1. Bootstrap Files

```bash
mkdir ~/product-research/perplexity && \
cd ~/product-research/perplexity && \
touch user-product-prefs-perplexity.jsonl \ product-rubrics-perplexity.jsonl \
model-data-archive-perplexity.jsonl \ deep-research-cache-perplexity.jsonl \
shopping-strategies-perplexity.jsonl \
model-versions.jsonl
``

### 2. First Run

Paste meta-prompt → "mechanical keyboards under $150 for coding"
Answer profiling questions → Get recommendations + files populated

text

### 3. Reuse & Continuity

"new PC vs 2024 research" → Auto-loads PC baseline
"upgrade earbuds" → Compares to prior earbuds research
"use v1.4 keyboards" → Rollback to exact prior version

text

## 📁 File Structure (Per Model)

~/product-research/
├── perplexity/ # Current model (auto-detected)
│ ├── prefs-perplexity.jsonl # Your profile + prefs
│ ├── rubrics-perplexity.jsonl # Category scoring rules
│ ├── archive-perplexity.jsonl # Model history
│ ├── cache-perplexity.jsonl # Deep research
│ ├── strategies-perplexity.jsonl # Shopping tips
│ └── model-versions.jsonl # Version registry
├── qwen2.5/ # Local LLM
└── claude/ # SaaS API

text

## 🔧 CLI Helpers

List versions

tail -5 ~/product-research/perplexity/model-versions.jsonl
Compare prior scores

grep "Keychron" ~/product-research/perplexity/archive-*.jsonl | jq '.score'
Rollback active

cp prefs-perplexity-v1.4.jsonl prefs-perplexity.jsonl
Recent prefs

tail -3 ~/product-research/perplexity/prefs-perplexity.jsonl | jq '.profile'

text

## 🎛️ Model Versioning

Default: Latest version per model (v1.6:perplexity)
Rollback: "query {model:perplexity,v1.4}"
Cross-model: "qwen2.5 research keyboards" → Uses qwen files
Show versions: "show available versions"

text

## 📊 Sample JSON Entries

**Profile**:

{"timestamp":"2025-12-05","category":"keyboards","type":"technical",
"use_cases":["coding marathons"],"budget_max":150,"brands":["Keychron"]}

text

**Rubric**:

{"category":"keyboards_tkl","version":"v1.6","weights":
{"value":0.25,"durability":0.25,"switch_feel":0.20}}

text

## 🔄 Feedback Loop

Rate output 1-5 per criterion → Auto-adjusts weights
"Too heavy on price? Say: value→0.20 durability→0.30"

## 🌐 Environment Optimized

✅ **Perplexity Pro**: Unlimited Deep Research (current)
✅ **Qwen2.5-14B**: Local rubric scoring (free/fast)
✅ **Claude/Gemini**: Edge cases via API

## 📈 Example Session

Query: "mechanical keyboards under $150 {model:perplexity,v1.6}"
→ "Technical user? Coding use case? Budget $150?"
→ Keychron K12 (9.1/10) vs K8 baseline (8.7/10)
→ "Buy Black Friday + Amazon coupon" [r/BuyItForLife]
→ Files auto-saved for next upgrade

text

**Ready to research! 🚀**

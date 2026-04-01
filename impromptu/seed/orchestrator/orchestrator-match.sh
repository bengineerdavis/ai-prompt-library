#!/bin/bash
# orchestrator-match.sh
# Usage: ./orchestrator-match.sh "query string" [registry.jsonl]
# Returns: JSON with factory match, signals, confidence

QUERY="${1:-}"
REGISTRY="${2:-factories-registry.jsonl}"

if [ -z "$QUERY" ]; then
    echo '{"error":"Usage: orchestrator-match.sh \"query\" [registry.jsonl]"}'
    exit 1
fi

if [ ! -f "$REGISTRY" ]; then
    echo "{\"error\":\"Registry file not found: $REGISTRY\"}"
    exit 1
fi

# Parse registry for factories only
FACTORIES=$(jq -s 'map(select(.type == "factory"))' "$REGISTRY")
STRATEGIES=$(jq -s 'map(select(.type == "strategy"))' "$REGISTRY")

# Function: compute keyword match (40%)
compute_keyword_match() {
    local query=$1
    local keywords=$2
    
    # Simple word overlap count
    local query_words=$(echo "$query" | tr ' ' '\n' | wc -l)
    local overlap=0
    
    # Count matches (simplified - real implementation would use array intersection)
    echo "scale=2; $overlap / $query_words" | bc
}

# Function: semantic similarity (mock - returns 0.92 for demo)
compute_semantic_match() {
    # In production: call embedding API
    # For demo: return fixed value
    echo "0.92"
}

# Function: task coverage (20%)
compute_task_coverage() {
    local required_tasks=$1
    local factory_tasks=$2
    
    # Count overlap
    local overlap=0
    local total=$(echo "$required_tasks" | tr ',' '\n' | wc -l)
    
    echo "scale=2; $overlap / $total" | bc
}

# Function: recency score (10%)
compute_recency() {
    local avg_score=$1
    echo "scale=2; $avg_score / 10" | bc
}

# Main matching logic
output=$(jq -r '.[] | select(.type == "factory") | .name' "$REGISTRY" | while read factory_name; do
    factory=$(jq "map(select(.name == \"$factory_name\"))[0]" <(echo "$FACTORIES"))
    
    # For demo: show all factories with mock scores
    keyword_score="0.35"
    semantic_score="0.92"
    
    # Task coverage from registry
    task_coverage=$(echo "$factory" | jq -r '.tasks | length // 0' | xargs echo "scale=2; 2 /")
    task_coverage=$(echo "$task_coverage" | bc 2>/dev/null || echo "0.67")
    
    # Recency from registry
    avg_score=$(echo "$factory" | jq -r '.avg_score // 8.5')
    recency=$(echo "scale=2; $avg_score / 10" | bc)
    
    # Compute composite
    composite=$(echo "scale=3; $keyword_score*0.4 + $semantic_score*0.3 + $task_coverage*0.2 + $recency*0.1" | bc)
    
    # Output as JSON
    jq -n --arg name "$factory_name" \
         --arg composite "$composite" \
         --arg keyword "$keyword_score" \
         --arg semantic "$semantic_score" \
         --arg task "$task_coverage" \
         --arg recency "$recency" \
         '{factory: $name, composite: ($composite | tonumber), signals: {keyword: ($keyword | tonumber), semantic: ($semantic | tonumber), task_coverage: ($task | tonumber), recency: ($recency | tonumber)}}'
done)

# Get top match
top_match=$(echo "$output" | jq -s 'sort_by(.composite) | reverse | .[0]')

# Output results
echo "{\"query\": \"$QUERY\", \"matches\": [$output], \"top_match\": $top_match, \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}"

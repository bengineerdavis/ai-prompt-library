# Publication and integration handoff

## Library source

Author and review the skill at `skills/reconcile-workflow/` in `bengineerdavis/ai-prompt-library`. The source includes `spec.md`, `SKILL.md`, `references/handoff.md`, and synthetic eval fixtures. Keep the library as the authoring home; do not fork the instructions into each stamped project.

## agents.toml declaration

A consuming project's `agents.toml` declares:

```toml
[[skills]]
name = "reconcile-workflow"
source = "bengineerdavis/ai-prompt-library"
```

Declare the skill in the same implementation change that uses it. Run the consuming project's dotagents installation task after merging the declaration. Do not claim installation from authoring alone.

## Agentic-layer deployment

The owning integration task is **APT-49.3**, under the agentic template's workflow-feedback integration record. It should add the declaration to `template/agents.toml.jinja` and verify installation in isolated stamp-matrix scenarios after this library change is merged.

The existing `backlog-workflow` adapter remains responsible for Backlog's task, dependency, claim, and decision surfaces. `reconcile-workflow` composes around it: reconcile evidence, capture findings, bound the milestone, and hand off an eligible task. Do not modify Matt Pocock's canonical skills.

## Optional installation

A user can evaluate the skill at project scope through dotagents, or install the same portable skill directory through a host's standard Agent Skills path. Global installation is never implicit. No MCP server, dotagents-specific runtime behavior, or host plugin is required by the skill.

Before installation, show the source, skill name, scope, exact operation, and refresh/removal behavior. Project scope is the appropriate isolated evaluation default. The CLI-only Backlog adapter does not depend on this skill.

## Ownership boundaries

- **APL-26:** this library skill and its evaluation contract.
- **APT-49.3:** optional agentic-template declaration and stamp-matrix deployment.
- **APT-49.1:** deterministic task-record integrity guard; this skill is not that guard.
- **APT-49.2:** safe stacked-PR reconciliation procedure; this skill references the need for semantic aggregate review but does not replace that procedure.
- **Each consuming project:** its configured tracker, worktree policy, and implementation approval boundaries.

## Review triggers

Revisit this handoff when the library publication lands, APT-49.3 begins, dotagents changes its declaration or installation surface, or a consuming host cannot load the portable skill format.

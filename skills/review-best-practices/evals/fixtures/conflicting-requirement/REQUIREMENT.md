# Requirement

We generate service repositories from a template.

1. When we improve the template later, projects already generated from it must
   be able to pull that improvement in.
1. Generated projects must contain **no template metadata of any kind** — no
   answers file, no lockfile, no tracking file, nothing that refers back to the
   template. A generated repo must be indistinguishable from a hand-written one.

Pick a tool.

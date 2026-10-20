---
name: curate-causal-graphs
metadata:
  version: 1.0.0
description: Review and curate PathwayMech native participants, reactions and mechanistic_edges
  with edge-specific evidence, direction and construct context.
---

# PathwayMech mechanistic graphs

Read [causal graph contract](../../../docs/CAUSAL_GRAPHS.md),
[Python validator](../../../src/pathwaymech/schema.py),
[LinkML schema](../../../src/pathwaymech/schema/pathwaymech.yaml), and
[add-pathway](../add-pathway/SKILL.md). The current native `PathwayRecord` has
`taxa`, `participants`, `reactions`, `mechanistic_edges`, `references` and optional
`reaction_mechanisms`. Use these actual fields rather than older generic
`causal_graph` examples. Maintained inputs are `data/pathways/*.yaml`.

Check each biological endpoint, participant kind, reaction direction,
stoichiometry, catalyst/cofactor, compartment, construct qualifier and edge
source. `enables`, `catalyzes`, membership, temporal ordering and causal
regulation have different meanings. Keep issued reaction IDs and exact source
assertions intact when adding step-level reaction mechanisms. Reference IDs must
resolve to the record's declared sources; source-database assertions are not
primary-paper quotations.

Use narrow text-preserving changes to maintained YAML with native revision
history. Inspect `src/pathwaymech/schema.py` validation before saving; do not
invent a sibling writer API. Run `just validate-strict`, `just check-identifiers`,
`just validate-history`, `just render-pages`, `just check-pages`, `just validate`,
`just test`, `just lint` and `git diff --check`. The current recipe is
`render-pages`, not a guessed `render` alias.
## Scope and completion

For one target, read the whole maintained record and its generated projection or
components. For a corpus goal, first freeze an inventory of record IDs, paths,
input hashes and applicable graph/protein elements; resume that ledger after an
interruption. Include hidden and ignored inputs when establishing absence.
Classify each target as checked, changed, evidence-limited, excluded, not
applicable or blocked, with reasons and inspected sources. A sample, a provider
report and a validator pass do not establish whole-corpus scientific completion.

Use [curate-yaml-record](../curate-yaml-record/SKILL.md) for the local evidence,
write, history and status contract; this adapter does not replace its managed
method. Record actual agent identity. Preserve scientific status rules and
unrelated edits. Use inspected primary evidence for mechanistic claims and exact
active identifiers for instances; never infer causality from association or
coverage from an empty query. A quotation is source text; interpretation belongs
in the native notes/explanation field.

Save final scientific assessments through
[review-yaml-record](../review-yaml-record/SKILL.md),
[record reviews](../../../docs/record-reviews.md), and the
[local profile](../../../docs/record-review-profile.md), including their native
persistence exceptions. Keep coverage/checkpoint accounting even when a clean
review should not produce a bundle. Unavailable prerequisites remain blocked;
a skipped target is not a completed enrichment. This skill authorizes no paid
provider call by itself.

After a completed goal, follow the user's authorized commit, push/PR,
adversarial review, issue/fix, merge and branch-cleanup sequence under the current
repository guidance. Carry forward existing authorization without asking again.
Use fresh required checks and native merge-queue rules. Verify actual merge and
landed content before deleting that feature branch or starting the next goal.
Only genuine review findings become issues; a no-diff goal needs a documented
no-op receipt rather than an artificial commit.

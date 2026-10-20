---
name: add-uniprot-protein-examples
metadata:
  version: 1.0.0
description: Review PathwayMech protein participants and add verified source-scoped
  UniProt identities and mechanistic evidence within native pathway records.
---

# PathwayMech UniProt participants

Read [graph contract](../../../docs/CAUSAL_GRAPHS.md),
[Python schema](../../../src/pathwaymech/schema.py), and
[causal workflow](../curate-causal-graphs/SKILL.md). `participants` are named
biological entities with issued IDs; their roles occur on `mechanistic_edges`.
Do not insert a TraitMech-style `protein_examples` slot. Keep exact existing
source identifiers, construct/variant qualifiers and organism context.

Audit `data/pathways/*.yaml` and all gene/protein participants and mechanism
endpoints. Add a UniProt participant only where the source supports that exact
protein's pathway role. A family, activity, enzyme class or whole complex is not
one protein accession. Preserve native IDs when they denote a different level;
record candidates needing a qualified relation instead of creating false
identity or catalysis edges. A gene-cluster member is not automatically a
catalyst of the whole reaction.

[cross-mech-protein-links](../cross-mech-protein-links/SKILL.md) can provide pinned
discovery leads, but this goal changes only PathwayMech; sibling changes require
their own scoped workflow. Use narrow maintained YAML edits, actual revision
history, and the causal workflow's strict/identifier/history/render/validation,
test and lint gates. Verify that new references and endpoints render correctly.
## Protein identity and evidence

Inspect live UniProt entry metadata or a release-pinned, provenance-verifiable
native snapshot. Check primary accession and active/merged/deleted state,
organism and strain, sequence/isoform, gene/locus mapping and source identity.
Prefer an exact assayed protein over a convenient ortholog. A named gene alone
is not a unique protein match. Keep family, whole complex, individual subunit,
native protein and experimental construct distinct. UniProt identity metadata
supports identity; primary role evidence supports participation in the record's
mechanism. Retain the original accession and an explicit mapping rationale when
resolving a changed identifier. Do not silently substitute species or isoforms.
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

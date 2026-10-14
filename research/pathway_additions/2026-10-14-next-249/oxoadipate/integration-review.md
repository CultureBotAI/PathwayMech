# Initial independent integration review

One actionable presentation defect was found for the 3-oxoadipate degradation
record at SHA-256 `214ef2d38ede4bb4e919f6f53699491e7c53b8d9b5b858c6ba80084e5b067032`.
This review was performed by a fresh reviewer who did not author the record,
authority additions, or scientific evidence projections. The comparison base
is `40b878b91af87a41295bfa90c6bf72fd9efefecb`.

All 246 previous pathway YAMLs and their generated record pages remain
byte-identical. All 4,776 previous authority terms and 752 source owners retain
their complete objects. The 928 previous source-manifest entries remain an
identical ordered prefix. Ten terms and six source owners were added. Both
unchanged canonical builders were independently rerun against their bound
external inputs; each output is byte-identical to the maintained snapshot.
The separate full identifier and release gates remain the root author's
responsibility; their results are not inferred from successful reconstruction.

The independent KGX export contains 4,439 nodes and 12,329 edges and matches the
generated downloadable TSVs byte for byte. All 12,307 earlier edge rows remain
exactly unchanged; all earlier node contexts are preserved. The 22 new edges
retain their endpoints, predicates, descriptions, entire evidence arrays,
reference metadata, and direction contexts. Small molecules, molecular
activities, complexes, proteins, pathway, and taxon retain their distinct kinds.

Two existing global KGX display names change because the new record sorts first:
`CHEBI:57288` changes from acetyl-CoA to acetyl-CoA(4-), and `CHEBI:15775` changes
from 3-oxoadipate to 3-oxoadipate(2-). These are verified canonical charged labels;
all earlier per-record labels remain in `source_contexts`. No other previous
node global field changes. This expected aggregation behavior is recorded
explicitly rather than described as complete byte preservation of all old nodes.

The generated SVG contains all 16 supported diagram nodes and exactly 22 edges.
Each directed edge links to its matching evidence row, preserves its declared
subject and object, and retains all cited reference anchors. Five context edges
are dashed; the other links remain solid. Reaction directions remain metadata
and do not reverse edge endpoints. The disconnected taxon is retained in the
component table and KGX; the unchanged renderer omits it from the diagram.
Structured assertions appear as assertions, while the five quotation-bearing
evidence rows retain quotation formatting.

The SVG was independently rasterized and visually inspected. Node labels fit
inside their boxes. Dense crossings and some crowded edge labels remain a
layout limitation; exact endpoint details and the evidence table remain
available. This is static SVG/HTML inspection, not browser or interactive-control
QA. Scientific source interpretation belongs to the separate independent
scientific review.

Machine-readable proof is in `integration-review-receipts.json`. Final change
scope, original-source payload exclusion and dossier bindings are recorded in
`integration-review-bindings.json` when the author finishes assembling the
dossier. The duplicate edge-label coordinates are retained in
`integration-review-label-collision.json` under stable finding key
`oxoadipate249-graph-edge-label-collision`. At x=416, y=338, distinct consumes and
regulates labels collide exactly; this affects readability despite intact graph
semantics. The root author filed [issue #521](https://github.com/CultureBotAI/PathwayMech/issues/521)
and a separate implementation agent is addressing this P3 finding. The complete
pre-fix scan found 1,787 identical label positions across 235 of 247 pages;
these are renderer collisions rather than record-data errors.
No source-data edits or governed-file edits were made by this reviewer.

This initial observation is superseded by `integration-review-final.md` and
`integration-review-final.json`, which independently verify the issue #521 fix.

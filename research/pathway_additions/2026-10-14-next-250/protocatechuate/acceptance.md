# Acceptance record

The complete GO:0019618 pathway contains 19 participants, four molecular
activities, one downstream pathway interface, and 37 evidence-backed edges.
The final YAML SHA-256 is
`03c1fced81d599136ea6577ef4ff314cc428aab9171c522f0334fa4ccba418d4`.

All 247 baseline pathway YAMLs and 4,786 existing authority terms with 758
source owners are preserved. The unchanged canonical builders and an
independent rebuild produce the same union: 4,799 terms, 766 source owners,
and 942 source-manifest entries. All 12,329 prior KGX edges and prior per-record
node contexts are preserved; the 37 new edges replay exactly.

Independent scientific review found inaccurate GO logical-restriction locators
in four edges, tracked in issue #525. They now follow the actual
`owl:equivalentClass` / `owl:intersectionOf` restrictions. Independent
integration review found that an unqualified contextual-label rule also waived
canonical pathway-interface names, tracked in issue #526. The new optional
`authority_entity_types: [reaction]` selector restricts this rule to verified
reaction authorities; typed placement and identifier existence remain required.
The independent successor controls reject invalid pathway labels even when a
pathway is recategorized as a molecular activity.

Final local gates passed: `just render-pages`, `just validate`, `just test`,
`just lint`, `just vendored-check`, and `git diff --check`. The complete test
run reports 4,882 passed, 3 skipped and 7 existing warnings. All captured core
input hashes remained unchanged throughout these final gates. Actual receipts
and lossless logs are under `validation/final/`; the earlier stale-page failure
is retained under `validation/initial/`.

SVG geometry, edge/evidence anchors and a raster rendering were independently
inspected. All 25 displayed graph nodes and 37 edges are retained without
label/node overlap or out-of-bounds geometry. Browser access was unavailable;
this is SVG/raster verification, not browser interaction testing.

Native scientific review bundles retain the initial finding and its explicit
successor disposition. The integration reports retain the policy finding and
independent fix checks. Exact committed-head acceptance and remote CI belong to
the subsequent PR lifecycle; this document does not claim those before they
occur.

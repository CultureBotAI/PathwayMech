# Final independent integration review

The 3-oxoadipate addition and the fix for [issue #521](https://github.com/CultureBotAI/PathwayMech/issues/521)
pass this independent integration review. The reviewer did not author the record,
authority additions, or renderer implementation. This is a working-tree review
against baseline `40b878b91af87a41295bfa90c6bf72fd9efefecb`; final commit identity,
release gates and CI are verified separately.

The initial review exposed two exactly coincident edge-label positions in the
new page, including different consumes and regulates predicates. The complete
pre-fix scan found 1,787 repeated positions across 235 of 247 graphs. The original
finding and page/SVG hashes remain in `integration-review-label-collision.json`.
The renderer now assigns separate label positions within each gutter and uses
non-arrow callouts for substantially displaced labels. These callouts retain
the original edge's evidence anchor and attach to that edge's own arrow path.

The independent successor replay checks every generated graph, not a sample:

- All 247 SVGs and 12,329 edges retain exactly their previous arrow geometry,
  node shapes, node positions, node labels, endpoint/predicate attributes and
  evidence anchors.
- All 4,519 moved labels across 242 graphs have separate conservative text boxes.
  No label overlaps another label or a node, and every label remains inside the
  canvas. Every one of the 3,674 leaders attaches to its own original path and
  has no arrowhead.
- All 246 previous pages retain byte-identical content outside the SVG. Ten
  canvases grow vertically; the maximum increase is 5.04%. Existing node
  placement and upper margins remain unchanged.
- Both complete KGX downloads remain byte-identical to the independent export
  obtained before the renderer fix. The new record contributes exactly 22 edges;
  all 12,307 previous edge rows and all 4,429 previous node contexts survive.

The new page was also visually inspected using its repository CSS and inherited
light palette. The conflicting predicates are now individually readable. Dense
arrow and callout crossings remain possible; this fix prevents label overlap,
not every line crossing. Browser controls were not exercised.

The scientific record remains at SHA-256
`214ef2d38ede4bb4e919f6f53699491e7c53b8d9b5b858c6ba80084e5b067032`.
All 246 prior YAMLs, 4,776 prior authority terms, 752 source owners, and 928
ordered source-manifest entries remain unchanged. Both independently rerun
canonical builders reproduce the maintained authority snapshots exactly. The
17 actual declared identifiers resolve with exact canonical labels. Fresh
byte-size/SHA-256 checks verified all 18 cited references against 20 retained
external original paths. No whole source payload was added to the dossier.

The two documented aggregate KGX name changes remain expected: `CHEBI:57288`
now displays acetyl-CoA(4-), and `CHEBI:15775` displays 3-oxoadipate(2-). Earlier
per-record labels remain in source contexts. No other previous global node
field changes. The separate scientific review determines evidence sufficiency;
this integration review does not claim independent full-paper reading.

The code review found no further actionable defect. Only `graph_view.py` and
its focused test file change runtime/test behavior; no governed file, identifier
policy or prior scientific record changes. Exact reviewed bindings and the
complete per-page comparison are in `integration-review-final-bindings.json`
and `integration-review-final.json`. Issue #521 is resolved in the reviewed
worktree; root-owned final gates and the merge lifecycle remain required.

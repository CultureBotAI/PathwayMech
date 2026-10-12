# Successor adversarial integration review

**Request changes: one P2 finding.** This supersedes the no-actionable-findings disposition in `report.md`, which is preserved unchanged. After that report was sealed, root supplied the actual old-node preservation delta. The reviewer independently reproduced the resulting type error below. The original 49 endpoint/parser checks remain successful; they did not check all new pathway-context node categories.

## P2 — Preserve explicit pathway type for embedded native pathways

Location: `data/pathways/amino-sugar-superpathway.yaml:212` (three consecutive pathway declarations through line 217); exporting behavior in `src/pathwaymech/kgx.py:156`.

The native child pathways `MetaCyc:PWY0-1324` and `MetaCyc:GLUAMCAT-PWY`, and the opaque downstream pathway interface `MetaCyc:GLYCOLYSIS`, are declared in the record's `reactions` collection without an explicit category. `_category` guesses `biolink:BiochemicalReaction` for every MetaCyc identifier in that collection. These three identities are expressly pathways, not elementary reactions. The new record therefore publishes false graph types. In particular, the established standalone `GLUAMCAT-PWY` node changes from `biolink:Pathway` to `biolink:BiochemicalReaction|biolink:Pathway` in the full export. The order of records does not prevent the error.

This is newly exercised by the addition even though the namespace fallback predates this branch. The source-context prose remains accurate but does not negate the independently machine-readable category assertion.

`pathway-context-reproducer.py` loads only the new record and the existing `n-acetylglucosamine-degradation-i.yaml`, invokes the maintained `kgx_nodes`, and demonstrates: old-only `GLUAMCAT-PWY` is Pathway; all three new-only context nodes become BiochemicalReaction; combining the two records in either order produces the erroneous union for GLUAMCAT-PWY. Exact output is in `pathway-context-reproducer-results.json`.

A bounded fix is explicit `pathway` node category support in native/LinkML schema, KGX mapping and graph type presentation, with that category set on these three new declarations. Keep their existing IDs, evidence, edges and opaque-interface boundaries. Explicit categories should distinguish a pathway context from an elementary reaction without changing unrelated old records or guessing identity from ID spelling. The existing `biological_process` category alone is insufficient for exact old-node category preservation: current explicit-category precedence would replace the established Pathway type with BiologicalProcess.

Expected verification: all three nodes export as `biolink:Pathway`; GLUAMCAT-PWY remains exactly Pathway in both record orders; the graph labels their explicit pathway type; native and strict validators agree; real Rhea reaction nodes remain BiochemicalReaction; all prior record contexts, nodes and edge payloads remain preserved. A schema/model extension should also keep pathway nodes ineligible for protein endpoint qualification or physical-substrate/cofactor roles.

The earlier documentation observation about EcoCyc prefix enumeration has been resolved by root. No other actionable findings were identified in the reviewed scope. Root retains authority for the issue, maintained fix, final gate sequence, canonical review and merge.

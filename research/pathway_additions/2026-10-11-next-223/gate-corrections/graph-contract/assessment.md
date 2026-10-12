# Independent assessment of the graph integration-test failure

**The renderer's contract is correct; the legacy integration assertion must distinguish visual endpoint keys from biological identities.** No product change is recommended for this failure.

The full gate run recorded one failure and 1,945 passes with three skips. Its failing assertion at `tests/test_graph_pages.py:92` compares `data-subject` and `data-object` directly with the source record's subject/object IDs. That was sufficient before endpoint qualifications existed. The three assay-qualified edges now legitimately target six distinct visual nodes, so those visual keys differ from the shared native protein IDs.

`graph_view.py` preserves the original directed biological identities in `data-subject-id` and `data-object-id` for qualified edges. Each qualified display node separately records `data-base-node-id`, `data-qualified="true"`, complete qualification details and its precise evidence-cell anchor. Unqualified endpoints still use their ordinary IDs. The shipped JavaScript reads `data-subject`/`data-object` for adjacency and highlighting; these values must match displayed node keys. Replacing them with bare biological IDs would attach the assay-specific display claim to the wrong visual node and undermine the existing interaction test that selecting the bare NagB node does not select its qualified assay instance.

The bounded test correction should preserve the original strength and add a second identity layer:

1. In both the Counter comparison and the per-evidence-row triple comparison, recover each biological endpoint using `data-<role>-id` when present, otherwise `data-<role>`. Preserve predicates, direction, counts, duplicate edges and exact evidence-row anchors.
2. Independently index the actual graph nodes by `data-node-id`, requiring unique keys and resolution of every displayed endpoint.
3. For each unqualified role, require the visual key to equal the record's native endpoint. For each qualified role, require a distinct visual key, matching `data-base-node-id`, `data-qualified="true"`, and exact `#mechanism-edge-N-qualifier-role` target. The existing endpoint tests retain complete description/evidence checks; these can also be asserted in the corpus integration loop.
4. Keep all existing edge evidence assertions, reference/source locators, unique HTML IDs and per-row checks. Do not skip qualified records, normalize away role direction, or remove the visual-node checks.

A fresh external probe against the actual integrated record passed at terminal `fab9e3`, exit 0. It reproduces exactly three mismatches under the old comparison, verifies exact original directed triples for all 114 edges and correct placement of all six qualified instances, and rejects eight independent mutations: missing original ID, reversed native IDs, collapsed qualification to the bare node, wrong base identity, missing qualification marker, wrong qualifier anchor, a substituted unqualified visual node, and duplicate display keys. `results.json` binds the actual record, renderer, JavaScript and interaction harness bytes.

The reviewer inspected the shipped JavaScript and the existing `qualified_endpoint_selection` scenario but did not claim a new browser run or rerun the full maintained suite. Root owns the maintained test edit and its verification. The full-gate failure remains a real recorded failed run; this analysis explains why its remedy belongs in the test contract rather than changing the correct directed/qualified visualization.

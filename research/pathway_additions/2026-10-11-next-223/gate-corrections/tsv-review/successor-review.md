# Independent review of the maintained TSV and graph-test corrections

**Accepted in the reviewed working tree, with no remaining findings in this scope.** The reviewer read the exact maintained `_tsv` change and the changes to `tests/test_kgx_export.py` and `tests/test_graph_pages.py`, then exercised those maintained functions directly. Root authored both corrections; the reviewer made no maintained edits.

[Issue427](https://github.com/CultureBotAI/PathwayMech/issues/427) is addressed by the lossless serialization correction. After normal CSV serialization of normalized single-line cells, the writer quotes a structurally empty terminal field as `""`. It does not change the empty-string contract, qualifier JSON, IDs or column set and does not add a Git whitespace exemption. Both CLI and rendered-page exports share `_tsv`. The new tests cover the final-cell encoding, full parsed column set, absence of trailing tabs/spaces, null/empty values, literal quote characters, Unicode and JSON.

The graph-test correction faithfully separates original directed biological identities from visual endpoint-instance keys. Both the Counter and per-row checks use the original-ID attributes when present. Additional checks independently require unique display-node keys, resolution of every visual endpoint, unchanged native keys for unqualified roles, and distinct correctly bound scoped keys for qualified roles. Qualified nodes must carry the base identity, qualification marker, precise role-specific evidence anchor and an existing target cell. All original edge counts, direction checks, evidence-row navigation, supporting references/assertions/locators and unique HTML IDs remain. The renderer and shipped JavaScript are unchanged; their visual adjacency contract is preserved.

`successor-probes.py` completed **14 grouped independent checks**, terminal `96dc48`, exit 0:

- Both maintained TSV regression tests execute successfully.
- The maintained serializer exactly reproduces the previously independently proposed 10,922-row edge export, SHA256 `9e30883cfdeed151ada21b3ab75880216a4489726b9f50ab945b1963ea4bdbc9`. All 3,845 node rows and node-file bytes remain unchanged.
- The exact revised maintained graph test passes for the actual 114-edge amino-sugar record.
- The same maintained graph test rejects nine in-memory mutations: missing or incorrect original identity, collapsing a qualification onto the bare node, wrong base identity, missing qualifier marker, wrong qualifier anchor, substituting an ordinary visual endpoint, duplicate display keys, and a missing qualifier evidence-cell anchor.
- Renderer and JavaScript bytes remain equal to the prior independently reviewed bindings.

`successor-results.json` binds the implementation, both test files, renderer, JavaScript and the actual record. The record remains SHA256 `fc436f537303f50121c472a4ece19249f3e6eb74d7304933fbafb37e04a61978`.

The original staged whitespace failure and the full-suite graph assertion failure remain legitimate failed runs with narrower remedial explanations; neither is rewritten as success. Root separately reported 68 focused KGX/endpoint tests passing. This review does not claim completion of the remaining corpus/interaction run, successor full gates, final staged whitespace check, preservation verification, PR checks, merge or issue closure. Those final outcomes remain root-owned.

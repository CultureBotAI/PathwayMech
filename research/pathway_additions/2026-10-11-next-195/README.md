# Three complete pathway networks

This cohort adds three independently bounded microbial pathways to the
195-record baseline at `d776b82c9c598bb79885ad01514b07900a678de0`.
Each record has its own source assessment and scientific review. Generated
network diagrams preserve the maintained assertions and their evidence links.

| Pathway | Complete native boundary | Representation limits |
| --- | --- | --- |
| MetaCyc:PWY-5901 — 2,3-dihydroxybenzoate biosynthesis | Three reactions from chorismate through isochorismate to 2,3-dihydroxybenzoate | The native holo-EntB dimer retains its modified components without making carrier maturation a requirement for N-terminal lyase activity. EntA assembly conflicts remain explicit. Upstream chorismate synthesis and downstream enterobactin/CueO chemistry belong outside this native boundary. |
| MetaCyc:PWY0-42 — 2-methylcitrate cycle I | Five reactions including propanoate activation and methylisocitrate cleavage | Approved generic Rhea reactions 57493 and 57497 represent the disputed methylcitrate transformations without assigning an absolute stereoisomer. This is an explicit broader representation, not a resolution of the experimental stereochemistry. Activation alternatives, PrpD metal evidence and AcnB assembly conditions remain qualified. |
| MetaCyc:PWY-5838 — superpathway of menaquinol-8 biosynthesis I | Ten reactions including the seven-step DHNA branch, IspB donor synthesis, MenA prenylation and UbiE methylation | The full eight-isoprene side chain and reduced endpoint follow the reviewed native/Rhea definitions. MenF is distinguished from EntC. MenE assembly remains unresolved. The extra respiratory hydrogenase reaction in the broader PathBank map is excluded by the independently established native boundary. |

The initial PathBank documents are discovery leads with explicit object-level
dispositions. Their names and broad maps do not establish pathway equivalence.
The methylcitrate follow-up addresses the uncertainty-representation option in
[issue #332](https://github.com/CultureBotAI/PathwayMech/issues/332); its original
PathBank propanoyl lead denotes a different methylmalonyl-CoA route and remains
separately assessed. No claim of source exhaustion is made.

Author dossiers, source projections, original-body hashes, exact replay programs
and identifier inventories are retained alongside this file. Full source bodies
remain outside the repository. `root-generic-rhea-crosscheck.json` independently
checks the generic Rhea parent relations, citations and directed sides; it does
not establish absolute product stereochemistry. iModulonDB receipts provide
bounded computational expression context, not pathway or catalytic proof.

`authority-integration.json` records canonical snapshot regeneration with all
baseline authority entries preserved. `integration-receipt.json` records final
local gates, while `generated-graph-kgx-audit.json` checks the generated SVG,
evidence anchors and KGX content. `baseline-preservation.json` checks unchanged
prior records, history, reviews, record pages and exported assertions.
`review-index.json` identifies immutable independent scientific reviews and
any successor dispositions. These receipts have distinct scopes; passing
structural checks do not establish scientific correctness.

Independent review identified five bounded provenance findings, tracked in
[357](https://github.com/CultureBotAI/PathwayMech/issues/357),
[358](https://github.com/CultureBotAI/PathwayMech/issues/358),
[359](https://github.com/CultureBotAI/PathwayMech/issues/359),
[360](https://github.com/CultureBotAI/PathwayMech/issues/360), and
[361](https://github.com/CultureBotAI/PathwayMech/issues/361). Initial and
intermediate input archives preserve the exact bytes assessed before correction.
Successor reviews retain the finding keys and prior occurrences, so a final
passing verdict does not erase the earlier observations. The superseded initial
test run was interrupted after 1,022 passed and 3 skipped; it is not a completed
suite. A separate full run passed 1,050 tests with 3 skipped. Subsequently, three
redundant nonexistent UniProt note pointers were removed without changing any
scientific assertion. `pre-pointer-review-inputs/` preserves the exact earlier
reviewed inputs and test seal. The integration receipt distinguishes that full
run from the fresh render, validation, lint, identifier, KGX and diff checks
after the pointer-only correction.

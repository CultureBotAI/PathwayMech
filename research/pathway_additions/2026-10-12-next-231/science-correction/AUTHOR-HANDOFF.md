# PPi branch author successor

This immutable successor addresses the five minor findings in the independent full scientific review of MetaCyc:PWY-8178. It is an author correction, pending independent successor reassessment and maintained integration. It is not a new full literature review, native saved review, Git change or issue closure.

The corrected target is `draft/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml`, SHA256 `20541f677f9228b670aac99a94e4d19ef89b5c20e0f6fdbb288d18ec7a9d98f5`, 107431 bytes. Its original is SHA256 `a5fb4208601109e5939577f84276a0fbe6ff28a324fa40a4b057b7bfe338e35a` in the sealed original author packet. `semantic-delta.json` enumerates every one of the 31 semantic field changes, and `target.diff` retains the textual comparison.

## Findings and exact corrections

| Issue | Stable key | Correction |
|---|---|---|
| [455](https://github.com/CultureBotAI/PathwayMech/issues/455) | pwy8178-ammonium-assay-preparation | The 2020 comparator used lyophilized rabbit aldolase/GPDH instead of ammonium-sulfate suspensions. Purified PFK buffer ultrafiltration is separate. The corrected edge, qualifier and paragraph preserve BaSO4 precipitation, ammonium addition, unresolved NH4Cl2 and the ATP/F6P comparator boundary. Exact 2020 Methods evidence is added to the qualifier; 2019 His6/TEV evidence remains. |
| [456](https://github.com/CultureBotAI/PathwayMech/issues/456) | pwy8178-competition-assay-modality | The mixed-substrate experiment is an FBP activity assay, distinct from S7P-only product-identification MS. The Methods locator is added. Competition remains an interpretation, with no binding constant or suppression of S7P catalysis asserted. |
| [457](https://github.com/CultureBotAI/PathwayMech/issues/457) | pwy8178-reference-titles | The 1982 and 2022 article titles now match the inspected first-page scan and retained publisher rendering. All 53 titles lack surrounding whitespace. No reference IDs, URLs, versions or original artifact hashes change. |
| [458](https://github.com/CultureBotAI/PathwayMech/issues/458) | pwy8178-reaction-direction-metadata | All six existing reactions now explicitly carry `direction: reversible`, replayed against native Reaction metadata. Native pathway layout and all chemical sides remain unchanged. |
| [459](https://github.com/CultureBotAI/PathwayMech/issues/459) | pwy8178-construct-evidence-scope | Direct 2019 His6/TEV evidence is added to ppi-034. The 2023 Aldoa Results locator supports linker details on its four qualifiers. Pfp retains His6, pAHCT0347/pRSET-A, host, strain and assay distinctions, with linker/codon-optimization details explicitly unresolved. Two new thesis citations directly support the Pfp preparation. |

`finding-dispositions.json` binds the exact root issue-creation ledger, bodies and prior scientific findings. Status is author-corrected pending independent review and eventual merge; issues remain open.

## Preserved science and provenance

All 51 edge identities, six reaction IDs, 20 native chemical-side occurrences, 53 references and 14 qualifier endpoint/kind assignments remain. All taxa and participant objects, labels, other record metadata and original curation-history value remain exact. The six direction fields add known source metadata without reversing arrows or adding reactions. The first 20 chemical-side edge objects, including their evidence, remain exact.

There are now 120 edge/qualifier evidence observations: 108 original observations are byte-equivalent semantic objects, eight retain their source identity with corrected assertion or extended locator, and four direct qualifier observations are added. No original evidence occurrence is deleted; no original selector is dropped. Exact replay and inheritance are enumerated in `evidence-selector-ledger.json`. The 104 XML observations are freshly replayed. Other unchanged observations inherit the exact independent review and original bindings; this is not a claim of a fresh visual review of every paper.

The 13 description paragraphs remain, with only paragraphs 4 and 6 changed. All 28 preflight claim dispositions remain and point to current paragraph hashes. Historical Entamoeba preparation limits, absent native coefficients, class/ionic conflicts, wrong-species B8I4R1 conflict, distinct strain/assay kinetics, donor and metal negative controls, unverified clostridial SBP cleavage, uncertain individual TKT catalysis/assembly, unsigned Rex binding and the 2022 necessity counterexample remain. Inaccessible supplemental bodies, abstract-only sources, historical thesis date conflict and source-exhaustion-false status are inherited explicitly.

## Sources and checks

The intake freshly verified all 345 original-author artifacts, all 48 scientific-review artifacts and 17 finding originals. The full original source packet and failures remain unchanged. The correction reread nine exact 2019/2020/2023 XML selectors, the retained independent thesis extraction for PDF111–113/117, the original 1982 title scan visually and the retained 2022 publisher title. Six native directions were freshly replayed. `source-read-receipts.json` preserves these bounded read limits; `source-selected-passages.json` preserves selected text.

The five bounded native checks passed: record schema, closed LinkML, identifier/label validation, exact production-collector bridge, and native page/graph/KGX. Eleven meaningful negative controls reject missing directions, altered side orientation, dropped reference, title whitespace, wrong auxiliary preparation, missing direct sources, MS competition overclaim, unsupported Pfp linker and loss of negative controls. Exact command outcomes are in `receipts/actual-command-outcomes.json`; prior unsuccessful author/reviewer/helper attempts are linked as historical failures, not relabeled successes.

The native page's reaction rows and SVG title/ARIA metadata expose all six reversible values. Standalone KGX nodes and each record-local `source_contexts` do likewise. Qualified graph arrows preserve biological IDs. Edge evidence and qualifiers round-trip exactly into KGX. Removing only the six direction fields from the successor produces byte-identical `edges.tsv`, isolating the metadata effect. The separate direction helper additionally verified aggregate KGX conflict behavior: target-local direction survives even when a multi-record aggregate direction is blank. No renderer change is needed.

## Authority and remaining work

The accepted reference-only Handle implementation is used without code changes in the external validation fixture. No Handle biological node is created. The explicit Handle URL renders correctly. The source collector excludes reference declarations; the ontology walker traverses references but filters by requested prefixes, so Handle remains outside ontology selection.

`authority-input-bridge.json` proves unchanged declared IDs/labels and exact production collector results between a5fb420 and this successor: 50 collected IDs, of which the original proposal selects 38 source-authority IDs, plus the same 12 ontology IDs. The original proposed source and ontology snapshots remain byte-identical. The two bibliography title corrections do not change original source bindings. These proposals use accepted EG outputs; the pending ATP canonical baseline bridge and full canonical build remain root-owned. No canonical outputs have been generated or accepted by this correction task.

Next: independent successor reassessment, root ATP baseline bridge/full canonical work, maintained integration and full gates, native review/history in correct render order, then the authorized PR workflow. No maintained, shared-cache, native-save, history, Git or GitHub writes occurred here.

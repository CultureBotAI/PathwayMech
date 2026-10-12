# ATP bypass author correction successor

The final target is `draft/sedoheptulose-bisphosphate-bypass.yaml`, SHA256 `cd59859d1dbcbc6c36961822b02daebc519a80a224ba8fa63d3235933b328101`. It implements issues #450–#453 in a separate immutable author packet. Independent successor reassessment and root acceptance remain pending.

Exactly six parsed YAML string values changed relative to the sealed original `efd16783`: five evidence locators and one description string. `semantic-delta.json` proves that reverting those six changes exactly recovers the original parsed record. All 67 edge identities, predicates, assertions, qualifier kinds/descriptions, 94 references and their original hashes, 62 named authority selectors, two core events/eight sides, 61 claims and 19 construct contexts remain. The original author337-artifact packet and independent science89-artifact packet were rehashed before correction and again before this seal; neither was edited.

The five-locator-only intermediate is preserved at `intermediate/five-locator-only.yaml`, SHA256 `bf9e76bf7c6ec7d32b2870c21aa8cad482ce5a2a8ff889e852af6a52fdbe8e8a`. It records the originally requested repair before the additional description finding.

## Exact repairs

- #450 / ATP-SCI-001, `sbp-018`: the construct evidence includes the actual HisTrap purification paragraph `/article/body/sec[5]/sec[7]/p[1]` in addition to the existing cloning/expression/assay selectors.
- #451 / ATP-SCI-002, `sbp-056`: the strain/growth qualifier points to `/article/body/sec[4]/sec[1]/p`, which specifies JM101-derived PB11/PB12, rpoS derivatives and aerobic M9 glucose growth. The old reporter/TSS selectors are retained only as historical observations.
- #452 / ATP-SCI-003, `sbp-038`, `sbp-039`, `sbp-062`: each compound identity union includes the sibling `/ptools-xml/Compound/inchi`. Formula/charge/ChEBI grounding and the existing inconsistent-SMILES and unmeasured-protonation qualifications remain unchanged.
- #453 / `atp-sbp-f6p-e4p-not-determined`: the description phrase “but no detected E4P” becomes “with E4P not determined.” Original TableIII F6P-experiment E4P cell `tbody/tr[11]/td[6]` is blank; the footnote defines blank as not determined. This additional defect was found during successor authoring and independently confirmed by root; it was missed by the earlier whole-record review.

## Corrected Table III disposition

There are **six preparations: the combined S7P experiment plus five controls**. The YAML phrase “five separate controls” remains correct and unchanged. In the no-metabolite control, S7P, SBP, DHAP and E4P are all ND; F6P and FBP are blank/not determined. The F6P-experiment E4P cell is blank/not determined. Neither blank nor ND is a measured numerical zero. `tableIII-cell-proof.json` retains every original row/column, exact cell XML and the footnotes. `tableIII-successor-disposition.json` corrects the original author preparation count and the independent review advisory's incomplete cell mapping additively, while preserving both sealed originals.

## Actual checks and inheritance

All five old and replacement selectors were replayed directly against the same original bodies and compared with the independent review's exact XML projections. Five negative controls demonstrate that each old locator omits its claimed HisTrap, strain/growth or InChI element; two more controls reject blank→ND and ND→blank swaps. Seven positive and seven negative focused checks pass. The updated159-row selector ledger preserves154 observations exactly and replaces only the five affected observations, retaining their predecessors in `changed-selector-proofs.json`.

Native schema, strict and identifier checks pass. The unchanged native collector proves equality of all62 selectors across the authority helper's frozen77c360 draft, sealed original efd167 target and this successor. Actual native page/KGX generation retains all67 edges, all145 edge/qualifier evidence uses and all24 qualifiers. This is deterministic HTML/SVG/KGX inspection, with no browser interaction or visual-layout claim. Authority files are byte-identical to the original native proposals; no authority refresh, adapter change, full canonical build or full production test run occurred.

The completed independent whole-record science review is inherited through its exact sealed handoff `630923e6`; this author correction is not a new independent review. All other chemistry, sources, constructs, negatives, unavailable-fulltext limits, computational-context limits and corpus novelty are inherited unchanged. The separately confirmed #453 correction is not falsely attributed to that original review. Original and corrected source observations are distinguished in the ledgers. `author-dispositions.json` preserves stable finding keys and actual issue bindings without inventing native saved review identities.

All work stayed in this external successor directory. No maintained record, shared cache, Git/GitHub object, original packet or environment installation was changed. Root owns independent successor acceptance, full canonical builders/audit, maintained adoption, native saved review/history, production gates and PR/merge workflow. Replays belong in a new external copy after sealing.

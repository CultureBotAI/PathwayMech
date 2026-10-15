The next265 evidence retention packages include two executable helper bodies at four maintained paths: `decode_retained.py` and `plan_promotion.py` under both `research/pathway_additions/2026-10-15-next-265/evidence-retention/` and `evidence-extension/`.

Stable issue key: `next265-retained-helper-lint`.

A direct native Ruff check of all four paths exits 1 with 78 diagnostics (`I001`, `E501`, `E701`, `E702`). The complete retained JSON has SHA256 `21a6e5011cc4b33dd71302851b6c91733056dee13c77b5079f7a5474d7c82202`. The complete hidden/ignored-inclusive next265 file inventory identifies exactly those four executable Python paths. This would prevent the unchanged repository lint gate from passing.

This is an integration/formatting defect, not a scientific finding. Actual maintained decoding already verifies all 9,629 base and 2,782 extension source occurrences. The accepted pathway YAML and evidence contents are unaffected.

Fix the two helper bodies in an explicit formatting successor, retaining the original bytes, original manifests, failure, and exact old-to-new path/hash lineage. Preserve all behavior, safety guards, source objects, and decoder mappings; account explicitly for standard-library import ordering when comparing ASTs. Do not add lint exclusions or weaken lint rules.

Acceptance: native Ruff passes the four actual maintained helpers; bounded independent comparison verifies the successor and original reconstruction; the successor decoders still verify both complete source scopes; normal repository validation, tests, lint, and final review pass before publication and closure.

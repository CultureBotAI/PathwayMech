`src/pathwaymech/ecocyc_complex.py` constructs output provenance dictionaries by iterating the unordered `PROVENANCE` set (`_class_proof`, line 164; `complex_metadata`, line 212). Identical original XML therefore produces different serialized key order across Python hash seeds, including nested PC-1 provenance.

The retained THIO native attempt demonstrates the defect for existing NAD owners `nad232-ecoli-cplx0-682` and `nad232-ecoli-pyrnutranshydrogen-cplx`. Baseline order is `license,url,version,sha256`; the native attempt begins `sha256,url,version,license`. Values are equal, but the actual ordered preservation helper raises `Changed prior sources: nad232-ecoli-cplx0-682`.

Three independent subprocesses with `PYTHONHASHSEED=1`, `2`, and `3` reconstructed metadata from the complete original complex XML and PC-1 companion. Decoded values were equal; serialized ordering differed. This code belongs to NAD PR #480 and should be fixed before merge.

Use an explicit deterministic output-field sequence matching the retained baseline while keeping closed-set validation. Add a cross-process regression for both outer and nested provenance. Preserve the failed attempt; do not relax ordering or manually repair generated outputs. The future THIO carrier/state modules contain analogous set iterations and must be handled in their own runtime scope.

Independent reproducer: `/private/tmp/pathwaymech-next-233-native-owner-diagnosis-20261012/order_probe.py`; results: `order-probe-result.json` and complete per-seed outputs.

Stable key: `nad-complex-provenance-key-order`.

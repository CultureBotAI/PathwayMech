The final native source-documentation gate for the P321 pathway addition fails `just lint` because the retained evidence decoder has one 108-character line, exceeding the repository's 100-character limit. Stable key: `next267-decoder-native-lint`.

Owner: `research/pathway_additions/2026-10-15-next-267/evidence-retention/decode_retained.py:20`, the `HISTORICAL_BINDING["path"]` literal. Accepted decoder SHA256: `b897526847b44cf43f3e3d3a583775bd3502567719f163c05195826b0d154980`. The failed gate ran after the exact accepted payload was adopted; native validation passed and lint then exited 1 with only E501. Earlier full tests and lint preceded this payload adoption.

Fix by splitting this literal using implicit concatenation without changing its value or module behavior. Preserve the prior decoder, payload manifest and failed native receipts; update the current manifest binding and report with explicit lineage. Verify whole-module AST equivalence, unchanged scientific sources and all original full-tested inputs, then run native validate/lint/diff checks and independently inspect the final delta. A full test rerun is unnecessary for an AST-identical formatting change.

Keep this issue open until the fix is merged and the landed tree is verified.

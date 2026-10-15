# KEGG benA locator-only successor

This separate author repair proposal addresses [issue 574](https://github.com/CultureBotAI/PathwayMech/issues/574), stable finding `NEXT264-KEGG-LOC-01`. It does not alter the frozen record-author package, actual YAML, issuing originals, graph, identifiers, labels, or reference source hashes. Independent acceptance is required and assigned to the separate reviewer; this handoff does not self-approve the fix.

The affected frozen artifact is `drafts/a1501-v2/reference-owner-inventory.json` in `/private/tmp/pathwaymech-next-264-record-authoring`. Its exact original SHA256 is `627aa2b6b51c9687bebdcfa502a0536384df31344cbfe0eb411c451b41484d36` (85,167 bytes). The affected JSON leaf is `$.references[0].locator`, selected by reference ID `KEGG:psa:PST_1667`.

Original locator:

> ENTRY PST_1667; NAME benA; ORGANISM psa; AASEQ/NTSEQ

Corrected locator:

> ENTRY PST_1667; SYMBOL benA; ORGANISM psa; AASEQ/NTSEQ

The complete original issuing entry, SHA256 `7f6f39584b4bd5a06fdef2e3f1a55e4e2f620ddc60c25c4e5b8393002e5f3eb2`, explicitly has `SYMBOL      benA` on line 2. Its separate NAME field on line 3 is `(GenBank) benzoate dioxygenase, alpha subunit`. Exact ENTRY, ORGANISM, AASEQ and NTSEQ fields also remain present. The complete source and its frozen issuing artifact manifest are copied under `original/` with bindings to their unchanged owners.

The successor is `successor/reference-owner-inventory.json`, SHA256 `85161110408f4934eadfa404f5ff8257df2df7b2c8710685cfa159080794f468` (85,169 bytes). `locator-correction-proof.json` proves a single JSON leaf change and exactly one contiguous byte substitution, `NAME` to `SYMBOL`, with identical prefix and suffix. All 101 reference entries, complete reference objects, owner paths/hashes, and limits remain otherwise identical. The complete frozen original inventory is retained without modification.

`unchanged-record-and-frozen-package.json` binds the unchanged final YAML SHA256 `3f8bbb8eceaa4420fa822e87ce01cca6b9d1967908dc117628aba71f54030696` (113,558 bytes) and rehashes all 237 frozen author artifacts against the unchanged manifest `12d125ae065db36a3e5196899ecdaafa0ad4b25dec401074472c41510f66f130`. The physical inventory includes hidden and ignored files. The record copy is exact. No scientific or sequence checks were repeated for this documentary field-label repair.

The package contains inert reproduction helpers, original/successor bytes, complete source bindings, issue binding, exact delta proof, preservation proof, and uniform compact retention metadata. The artifact manifest inventories every package file except itself. The compact manifest provides original/stored SHA256 hashes and byte counts; text is retained as exact deterministic gzip copies. The external replay is an author integrity check, not independent review.

Root owns maintained integration of this metadata successor, independent acceptance, and issue closure. The original record-author package remains immutable; any future substantive record change needs its own successor and review bindings.

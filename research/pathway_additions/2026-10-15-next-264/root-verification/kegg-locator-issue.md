The frozen benzoate record-author reference inventory names the wrong KEGG field for `benA`.

Stable key: `NEXT264-KEGG-LOC-01` (minor provenance finding).

`drafts/a1501-v2/reference-owner-inventory.json`, reference `KEGG:psa:PST_1667`, currently gives `ENTRY PST_1667; NAME benA; ORGANISM psa; AASEQ/NTSEQ`. The exact issuing entry has `SYMBOL benA`; its `NAME` field is `(GenBank) benzoate dioxygenase, alpha subunit`.

The inventory is retained under `research/pathway_additions/2026-10-15-next-264/record-authoring/compact/drafts/a1501-v2/reference-owner-inventory.json.gz`. Its decoded SHA256 is `627aa2b6b51c9687bebdcfa502a0536384df31344cbfe0eb411c451b41484d36`; the issuing original SHA256 is `7f6f39584b4bd5a06fdef2e3f1a55e4e2f620ddc60c25c4e5b8393002e5f3eb2`.

Acceptance:

- Preserve the frozen inventory, package manifests and issuing original unchanged.
- Add an explicit successor changing only this locator leaf from `NAME benA` to `SYMBOL benA`, with exact byte-delta proof.
- Independently verify the corrected locator and retain the disposition/history with the addition.

The actual pathway YAML does not contain the erroneous field locator. Its exact gene identity, label, source hash, edges and scientific interpretation are unaffected.

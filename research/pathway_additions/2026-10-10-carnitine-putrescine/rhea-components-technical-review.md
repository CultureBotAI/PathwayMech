# Independent RHEA-COMP technical review

Result: no actionable defect found in the reviewed implementation for [issue 320](https://github.com/CultureBotAI/PathwayMech/issues/320). This is a technical review, not a scientific record review.

The complete pinned official Rhea RDF gzip parsed successfully and yielded **1,268 whole GenericPolypeptide terms**. Its preserved release properties identify **release 142, 2026-09-02**. Native `Compound_10685` and `Compound_10686` have matching numeric IDs, GENERIC accessions and oxidized/reduced electron-transfer-flavoprotein names. Reviewed UniProt CaiA/P60584 independently exposes the same `RHEA-COMP` identifiers in its catalytic annotation. Separate FAD/FADH2 reactive-part objects remain excluded from the whole-protein authority.

The implementation keeps canonical labels, requires source resolution, rejects ambiguous identifiers/names and duplicate qualifying subjects, and adds the namespace consistently to both schemas. It does not add a contextual-label exemption. The current carrier participants explicitly use the protein category; generic carrier identities do not establish organism-specific sequence identity.

Validation command:

```bash
UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv run pytest -q tests/test_rhea_component_authority.py
```

Result: **exit 0; 9 passed in 0.18s**. The tests cover source-derived labels, unresolved corpus IDs, foreign/reactive-part URIs, mismatching IDs/accessions, missing/conflicting names and duplicate subjects. An independent complete parse of the real compressed RDF checked compatibility beyond fixtures. No duplicate full snapshot build or repository-wide gates were run by this reviewer.

[The JSON receipt](rhea-components-technical-review.json) preserves the exact reviewed-file hashes, source hashes, source locators, commands, results and limits. No code, schema, policy, test or record edits were made by this reviewer. Final snapshot and generated-artifact checks are separate work.

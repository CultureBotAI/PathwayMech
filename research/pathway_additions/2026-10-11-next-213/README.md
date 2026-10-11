# Complete petrobactin biosynthesis

This addition represents all ten transformations of MetaCyc:PWY-6289, including both convergent assembly branches, precursor formation and carrier maturation. The maintained record has 28 participants, 94 edges, 149 evidence entries and 59 references. All 40 named nodes occur in the generated graph and KGX export.

The native terminal product and reaction are retained because the current ChEBI/Rhea product has different constitutional connectivity. CHEBI:142778 and RHEA:63821 are compared reference identifiers, not selected graph nodes or exact equivalents. Original figures, source structures, strain and construct boundaries, generic carrier states, unspecified citryl stereochemistry and the unknown physiological maturation catalyst remain explicit in the record and source dossier. Both assembly routes have in vitro support; no unique intracellular order is asserted.

Issue #388 corrected only the AsbD contextual-participation description. The original record, review and source projections remain immutable. Independent acceptance verifies that every other scientific field is unchanged. Issue #390 corrected an output-file race in the portable source replay; independent collision and fresh-output executions verify exclusive creation and successful replay. Earlier failed attempts and their dispositions are retained.

`portable-replay/` contains the current-target replay and metadata. The top-level `petrobactin-replay.py` and associated original metadata describe the historical author submission and retain its original paths and target hash. To replay current inputs from the repository root, provide a new external output path:

```bash
.venv/bin/python research/pathway_additions/2026-10-11-next-213/portable-replay/petrobactin-replay.py \
  --repo-root . \
  --record data/pathways/petrobactin-biosynthesis.yaml \
  --source-manifest research/pathway_additions/2026-10-11-next-213/portable-replay/petrobactin-source-manifest.json \
  --output /private/tmp/petrobactin-new-replay.json
```

Original source bodies must be available at the hash-bound manifest paths; they remain external. The replay verifies 52 original bodies, 54 chemical sides and ten conditional balances. It does not replace full-corpus gates or scientific review.

Authority integration preserves all baseline terms and adds five original manifest inputs, 18 ontology terms and 13 source terms. The canonical builder also includes the two explicitly compared reference identifiers; their authority entries do not establish chemical equivalence. Final coverage is 517 manifest inputs, 1800 ontology terms and 2118 source terms.

All final gates ran after transition to the actual bacillibactin merge. 1256 passed, 3 skipped, 3 warnings in 471.26s (0:07:51). The governed-artifact check passed all 22 pinned artifacts after a retained sandbox network failure. Independent graph/export inspection preserved all 213 prior records, 929 prior record/history/review/page files, 10050 prior exported edges and 6699 prior record-scoped node contexts. No record history was added after render.

`integration-receipt.json`, `full-gate-receipts.json` and lossless `console-transcripts.json` bind these completed checks. Canonical scientific disposition, remote checks and publication are separate subsequent steps. More pathway candidates remain.

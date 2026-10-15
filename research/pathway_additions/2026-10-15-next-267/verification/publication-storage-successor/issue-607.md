Finding key: `T267-PUBLICATION-WHITESPACE-01` (bounded publication packaging defect).

The actual staged `git diff --cached --check` exited 2 before commit, push or PR. It flags 11 single-space blank context lines in `research/pathway_additions/2026-10-15-next-267/evidence-retention/successor-proof/decoder-exact.diff`. Those spaces are required unified-diff syntax. The source artifact must remain byte-exact; trimming it would invalidate the retained evidence.

The reviewed scientific record, implementation, authorities, generated graph and earlier saved reviews are unchanged. This artifact is supplemental correction proof; it is not a source-map endpoint and the maintained decoder does not read it. The failed staging receipt and independently reproduced finding are retained.

Acceptance:

- Store the exact original diff using deterministic lossless gzip, with an explicit original-to-stored path, length and SHA-256 mapping.
- Retain the predecessor physical manifest and report, update only the current physical manifest/report and add a history event. Every other payload file, the decoder and all source maps remain byte-identical.
- Independently verify complete predecessor payload reconstruction and the bounded storage successor; preserve the earlier canonical reviews as historical working-tree attestations.
- Pass current native review/documentation/lint checks and the actual staged whitespace gate without changing whitespace policy.
- Keep this issue open until publication and exact landed-tree verification.

All 340 existing issues were checked before creation. Earlier #423, #584 and #593 concern different archival artifacts and establish the lossless-storage approach; this finding applies to the new P321 package.

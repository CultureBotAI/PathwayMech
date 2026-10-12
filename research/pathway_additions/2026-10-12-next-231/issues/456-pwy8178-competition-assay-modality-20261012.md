Independent scientific review of candidate MetaCyc:PWY-8178 found a minor defect in `data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml`. The candidate is awaiting integration.

Stable finding key: `pwy8178-competition-assay-modality`

The draft calls the mixed F6P/S7P competition measurement an MS assay. The primary Results say that the competition assay monitored FBP production, and the Pfp Methods describe the coupled activity assays. The separate MS Methods contain S7P alone for product identification. The inaccessible supplementary Table S3 is not a basis for asserting an MS competition readout.

Correction: Replace mixed-substrate MS assay with mixed-substrate FBP activity assay; add the Pfp assay Methods locator if specifying the coupled readout. Keep the observed decrease and the explicitly interpretive competition explanation.

Acceptance: The S7P inhibition edge still refers only to reduced F6P-to-FBP activity with mixed substrates; it does not assert binding affinity or suppression of S7P catalysis.

Affected fields: `mechanistic_edges[ppi-039].description`, `mechanistic_edges[ppi-039].evidence[0].source_assertion`

Primary evidence: PMID:37438781

Source locations: /article/body/sec[2]/sec[3]/p; /article/body/sec[5]/sec[5]/p[3]; /article/body/sec[5]/sec[10]/p

Review packet SHA256: `d7749e954e7cd7a823fa5f7bb0ed2ded90394e48b9a51f8313eab37c3ae9fa8c`. Preserve the complete six-event pathway, all biological edge identities, and negative/conflicting controls.

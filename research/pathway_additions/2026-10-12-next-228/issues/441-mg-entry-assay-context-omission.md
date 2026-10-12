Pre-merge scientific review of `MetaCyc:PWY0-1300`, intended owner `data/pathways/mannosylglycerate-degradation.yaml`. Reviewed draft SHA-256: `08fe9a6f3f0da2f66c4dc6cd68fc33fbe51a38770b6eeee743751f05f019d088`.

Stable review key: `mg-entry-assay-context-omission`. Severity: **major**.

The linked entry event is explicitly in record scope, yet these source-supported experimental bounds are absent from target, authored research and scope disposition. This is material incompleteness of the entry mechanism context, not a demand to extend unrelated regulons.

Affected locations:

- `mechanistic_edges[id=mg-mnga-catalysis]`
- `mechanistic_edges[id=mg-mnga-vesicle-assay]`
- `research/mannosylglycerate-degradation.md`
- `derived/scope-and-conflicts.json`

Evidence:

- PMID:14645248: In induced MC4100 uptake experiments, Results reports weak effects of glucose, mannose and mannitol, a smaller trehalose effect, and no effect for fructose and the named non-PTS comparators. Discussion describes mannose and the three glycosyl analogues as not significantly inhibitory even at 1 mM against 0.1 μM radiolabeled MG. These statements must coexist, rather than being upgraded into a robust direct competitive-inhibition mechanism. The same Results also reports that 300 mM NaCl did not induce transport and reduced MG-dependent induction by approximately half; this differs from the later KM522 500 mM salt-protection test. Source SHA-256 `65221244b50be357ab0ac0c10b40dfe922794d63f277f65522bc3473e1bb2edb`; retained author-uploaded full-text observation L1303–L1310; L1350–L1372; L2429–L2457.

Required correction:

Preserve the observed weak-positive and negative uptake comparisons, the Results/Discussion mannose tension, and the separate salt-induction observation in source-backed entry assay context and corresponding scope/coverage ledgers. Keep MC4100 and measured uptake/induction endpoints explicit. Do not assert direct ligand binding, a competitive mechanism, exact inhibition constants or a stronger biological sign than the source supports. If graph edges are added, independently ground each chemical and qualify the measured process; source-limited prose on the existing entry context is acceptable where exact mechanistic/chemical scope is unresolved.

Acceptance:

- Relevant source statements are present with exact L-number locators and declared projection access.
- The mannose weak-effect/no-significant-effect tension and negative controls remain explicit.
- 300 mM salt-induced suppression of induction is separated from KM522 osmoprotection and from a direct catalytic salt effect.
- Original two core events and native 17 chemical sides remain unchanged.

Provenance: independent scientific review handoff SHA-256 `36cbadc214456c366a4d579909daedd128458b398eac594f0670fbdc839e5b7a`; findings SHA-256 `51d37e63e7402def8ed72b2ebe6686c92aad4b94efe655da5f6205b6611ddb88`. Full original author and review packets remain immutable. Close after the corrected record and preserved review dispositions merge.

Primary sources: [Sampaio et al.](https://doi.org/10.1074/jbc.M310980200), [CdaR study](https://pmc.ncbi.nlm.nih.gov/articles/PMC111340/), [PtsI](https://www.uniprot.org/uniprotkb/P08839/entry), [H-NS](https://www.uniprot.org/uniprotkb/P0ACF8/entry), [Rhea](https://www.rhea-db.org/rhea/27378).

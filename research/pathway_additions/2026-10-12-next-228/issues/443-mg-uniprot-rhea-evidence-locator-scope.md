Pre-merge scientific review of `MetaCyc:PWY0-1300`, intended owner `data/pathways/mannosylglycerate-degradation.yaml`. Reviewed draft SHA-256: `08fe9a6f3f0da2f66c4dc6cd68fc33fbe51a38770b6eeee743751f05f019d088`.

Stable review key: `mg-uniprot-rhea-evidence-locator-scope`. Severity: **minor**.

The identities and scientific assertions are supported elsewhere in the same originals, but exact reproducibility of the declared locator fails. A nonempty locator check misses these adjacent-field errors.

Affected locations:

- `mechanistic_edges[id=mg-ptsi-catalysis].evidence[2]`
- `mechanistic_edges[id=mg-location-P0ACF8].evidence[0]`
- `all 13 evidence items whose reference_id is RHEA:27378, RHEA:33308 or RHEA:23881`

Evidence:

- UniProtKB:P08839: His189 is an Active site feature. The original Modified residue feature is Tyr122, so the existing locator does not locate the claimed catalytic histidine. Source SHA-256 `70ac1d76fe0def5c5546bd523292601305ef56cc326a31ff7a0223f572cae844`; features[type=Active site,location.start.value=189]; features[type=Modified residue].
- UniProtKB:P0ACF8: The current assertion combines nucleoid location with variable oligomers but locates only SUBCELLULAR LOCATION. Oligomer support occurs in SUBUNIT. Source SHA-256 `69765685e6a74d1b208bbeb2ddd51204aa1be75b3b8b411efbe83252cd9523c8`; comments[commentType=SUBUNIT]; comments[commentType=SUBCELLULAR LOCATION].
- RHEA:27378 / RHEA:33308 / RHEA:23881: All 13 stoichiometry locators end with rh:coefficient1, which is not the actual native predicate. The source encodes unit stoichiometry using the side-to-participant rh:contains1 relation. Source SHA-256 `8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf`; directional rh:substrates/rh:products side; side rh:contains1 participant; participant rh:compound compound.

Required correction:

Point PtsI His189 to its Active site feature, include H-NS SUBUNIT for the oligomer assertion or split its evidence, and spell each Rhea side/participant rh:contains1 triple exactly. Preserve all scientific claims, source hashes, reaction sides, coefficients and state qualifiers.

Acceptance:

- Independent replay resolves each asserted feature/comment/triple in the exact bound original.
- A Tyr122 Modified residue or nonexistent rh:coefficient1 predicate is rejected by source-specific negative controls.
- No edge endpoint, predicate, chemical identity, stoichiometry or qualifier changes occur for this locator-only fix.

Provenance: independent scientific review handoff SHA-256 `36cbadc214456c366a4d579909daedd128458b398eac594f0670fbdc839e5b7a`; findings SHA-256 `51d37e63e7402def8ed72b2ebe6686c92aad4b94efe655da5f6205b6611ddb88`. Full original author and review packets remain immutable. Close after the corrected record and preserved review dispositions merge.

Primary sources: [Sampaio et al.](https://doi.org/10.1074/jbc.M310980200), [CdaR study](https://pmc.ncbi.nlm.nih.gov/articles/PMC111340/), [PtsI](https://www.uniprot.org/uniprotkb/P08839/entry), [H-NS](https://www.uniprot.org/uniprotkb/P0ACF8/entry), [Rhea](https://www.rhea-db.org/rhea/27378).

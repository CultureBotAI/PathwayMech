# Independent scientific review: 2-O-alpha-mannosyl-D-glycerate degradation

Verdict: **changes requested** — two major scope/completeness findings and one minor evidence-location finding. The source-supported core, identities, reaction directions, HPr relay and signed/unsigned regulatory interpretations are sound within their stated evidence limits.

Exact target: `08fe9a6f3f0da2f66c4dc6cd68fc33fbe51a38770b6eeee743751f05f019d088`. Reviewer `/root/lyxose_author`, independent of MG authoring and adapter implementation. Review began 2026-10-12T02:54:18.047451+00:00 and completed 2026-10-12T03:04:00.983889+00:00. The target and original author packet were not edited.

## MAJOR: mg-entry-assay-context-omission

Relevant MG uptake modulation and its internal source tension lack a disposition. The linked entry event is explicitly in record scope, yet these source-supported experimental bounds are absent from target, authored research and scope disposition. This is material incompleteness of the entry mechanism context, not a demand to extend unrelated regulons.

Preserve the observed weak-positive and negative uptake comparisons, the Results/Discussion mannose tension, and the separate salt-induction observation in source-backed entry assay context and corresponding scope/coverage ledgers. Keep MC4100 and measured uptake/induction endpoints explicit. Do not assert direct ligand binding, a competitive mechanism, exact inhibition constants or a stronger biological sign than the source supports. If graph edges are added, independently ground each chemical and qualify the measured process; source-limited prose on the existing entry context is acceptable where exact mechanistic/chemical scope is unresolved.

Locations: mechanistic_edges[id=mg-mnga-catalysis]; mechanistic_edges[id=mg-mnga-vesicle-assay]; research/mannosylglycerate-degradation.md; derived/scope-and-conflicts.json.

Sources: PMID:14645248 — retained author-uploaded full-text observation L1303–L1310, L1350–L1372, L2429–L2457.

## MAJOR: mg-cdar-assay-endpoint-scope

CdaR assay-derived regulatory endpoints omit construct and sequence-reference qualification. The graph/export endpoint is the exact modern reference protein. Assay-specific reference numbering, preparations and loss/rescue interpretation must travel with the affected claim, rather than remaining only in an external dossier. The signs and gene endpoints are supported; this is a scope defect, not evidence that P297S or Tn5 mutants activate transcription.

Qualify the subject of both affected edges as experimental_construct with exact source-limited MC4100 reporter/loss/rescue context and the 391-aa paper/current-385-aa reference distinction. Preserve paper residue numbering without silently mapping it to the modern chain. Distinguish active reference or rescued regulator from loss-of-function mutants used to infer its role; do not mint a new protein ID or label mutant proteins as active.

Locations: mechanistic_edges[id=mg-gark-reg-cdar].subject; mechanistic_edges[id=mg-cdar-auto].subject.

Sources: PMID:10762278 — /html/body/div[2]/div[2]/div/div[1]/div/div[2]/main/article/section[2]/section/section[5]/p[1], same section p[2], section[6]/p[1] and p[2]; UniProtKB:P37047 — primaryAccession, sequence.length, genes.

## MINOR: mg-uniprot-rhea-evidence-locator-scope

Several evidence locators resolve to adjacent fields rather than the asserted native statement. The identities and scientific assertions are supported elsewhere in the same originals, but exact reproducibility of the declared locator fails. A nonempty locator check misses these adjacent-field errors.

Point PtsI His189 to its Active site feature, include H-NS SUBUNIT for the oligomer assertion or split its evidence, and spell each Rhea side/participant rh:contains1 triple exactly. Preserve all scientific claims, source hashes, reaction sides, coefficients and state qualifiers.

Locations: mechanistic_edges[id=mg-ptsi-catalysis].evidence[2]; mechanistic_edges[id=mg-location-P0ACF8].evidence[0]; all 13 evidence items whose reference_id is RHEA:27378, RHEA:33308 or RHEA:23881.

Sources: UniProtKB:P08839 — features[type=Active site,location.start.value=189], features[type=Modified residue]; UniProtKB:P0ACF8 — comments[commentType=SUBUNIT], comments[commentType=SUBCELLULAR LOCATION]; RHEA:27378 / RHEA:33308 / RHEA:23881 — directional rh:substrates/rh:products side; side rh:contains1 participant; participant rh:compound compound.

## Verified coverage and evidence boundaries

All 612 author artifacts match the seal. The review covers all 75 edges, 13 existing endpoint qualifiers, 62 references, 164 evidence uses and 29 preflight claims in both directions. Sixty-three original-backed probes verify native object identity, assembly/gene joins and all 17 chemical sides. Twenty-five ontology identities were queried from rehashed issuing SQL originals. The full Rhea source was independently joined through native directional sides, participants and compounds. Ten domain controls reject altered anomer, duplicated PEP, free-histidine substitution, reversed kinase input, incorrect HPr state/role, wrong frozen permease, incorrect catalytic-site locator and source-marker-as-inhibition claims.

Native single-target shape and strict checks pass. The unchanged author adapter still reports its one declared PathBank child identity gap. Root subsequently reported separate acceptance of the adapter implementation; this review does not conflate that code result with scientific acceptance. Independent KGX serialization retains 75 edges and all 13 existing qualifiers. The two missing CdaR qualifications are findings even though present qualifiers serialize correctly.

The generic hydrolysis product remains distinct from alpha-M6P; no anomerization is invented. MngB remains a physiological/surrogate assignment, with similarity-only generic metal. PtsI/HPr state and PEP-once semantics, one-chain MngA, native complexes, source-specific assay constructs, Fur sign conflict, FNR annotation limits and computational iModulon context are preserved. The empty frozen PathBank child is structural source context only. No uninhibited or omitted assay condition is interpreted as biological absence.

The 2004 paper is a retained author-uploaded web-text projection, independently traced to 2,883 observed line records; it is not a publisher PDF. Other cited primary HTML/XML passages and source-selected sections were inspected directly, with figure captions but without figure-image review. Historical/FNR full texts and TmaR supplements remain unavailable. iModulonDB was independently replayed from exact frozen response bodies (10 queries; module38 has nine genes, including garK/cdaR), without deriving a causal relation or treating a missing search hit as absence.

This is an external review packet. It is not a maintained native saved review, a full-corpus gate result, a canonical authority build or merge approval. Exact original hashes, assertion locators, coverage ledgers, probes and command outcomes are retained alongside this report. No Git/GitHub, maintained source/cache or environment mutation was performed.

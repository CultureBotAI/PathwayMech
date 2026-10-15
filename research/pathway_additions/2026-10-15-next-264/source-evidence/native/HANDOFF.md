# Next264 native activity and biological-context preparation

This is an external source-author package for **MetaCyc:PWY-2503, benzoate degradation I (aerobic)**. It contains no pathway draft or maintained edits. Frozen next264 discovery is unchanged. Root intake and a comparison against the post263 merged corpus are still required before authoring; no new absence conclusion is made here.

## Complete finite source closure

The package retains **47 complete META 27.0 native objects** and **all 511 direct slots**: five activities, 13 proteins/complexes, eight genes, 13 organism frames, four compounds, two reactions, one pathway, and one compartment. Forty-two objects were newly retrieved from the public Pathway Tools endpoint, with exact request/response and source-hash receipts. Five exact pathway/reaction/compound originals were reused from the frozen discovery manifest. The responses share a reported source version but are not an atomic database snapshot.

The five requested activities and four primary enzyme contexts are complete:

| Activity | Native enzyme | Reaction | Native evidence boundary |
|---|---|---|---|
| ENZRXN-15650 | CPLX-7698 | BENZOATE-12-DIOXYGENASE-RXN | Unpurified-protein evidence code attaches PMID4341530; cofactor slots separately cite PMID214433. Preparation and paper scope require reconciliation. |
| ENZRXN-3124 | CPLX-2541 | BENZOATE-12-DIOXYGENASE-RXN | Native mt-2 context, unpurified-protein code, citation PMID2183008. |
| ENZRXN-15651 | CPLX-7701 | 1.3.1.25-RXN | Native purified-protein code and kinetic annotations cite PMID4341530. Exact primary preparation remains separate from native JMP222 assignment. |
| ENZRXN-3125 | MONOMER-2964 | 1.3.1.25-RXN | Native mt-2 context, unpurified-protein code, citation PMID2183008. |
| ENZRXN-12384 | MONOMER-2964 | 1.3.1.25-RXN | Same native enzyme/reaction pair; this complete object has no evidence or citation slot. It is not a second XylL protein. |

Recursive direct component closure yields nine composition links: CPLX-7698 contains one CPLX-7699 hydroxylase and one MONOMER-14400 electron-transfer component; CPLX-7699 contains three each of MONOMER-14398 and MONOMER-14399. CPLX-2541 contains one CPLX-7700 and one MONOMER-2963; CPLX-7700 contains three each of MONOMER-2961 and MONOMER-2962. CPLX-7701 contains four MONOMER-14397 subunits. These are native annotations, not independent measurements transferred between strains.

All eight direct protein/gene links and reciprocal gene/product links are closed. The benA/benB/benC/benD native genes are G-10984/G-10985/G-10986/G-10983; the xylX/xylY/xylZ/xylL genes are G-2081/G-2082/G-2083/G-2084. Complete source objects contain no sequence-verification evidence establishing external protein identity.

The complete 26 activity/protein/gene objects contain no direct regulation or transcription-unit slots. This is a source-bound omission, not biological absence. Twenty-one regulation backlinks on benzoate, FAD, and the [2Fe-2S] cluster were checked by exact target: all regulate different activities. The FAD backlink for **benzene** dioxygenase is not the selected **benzoate** reaction. Four chlorinated-substrate activities linked from the enzyme frames remain explicit out-of-boundary context; their full root slots are preserved without turning them into extra pathways.

## Cofactors, localization, and experimental context

ENZRXN-15650 lists **FAD** and **CPD-6**, a [2Fe-2S] iron-sulfur cluster, citing PMID214433. Exact full compound originals are retained. Their native ChEBI links are CHEBI:57692 and CHEBI:33739; structural/charge and protein-bound cluster interpretation belong to the separate chemistry stage. Do not identify this class automatically as a specific Rieske cluster or isolated small molecule.

Native CPLX-7701 records cytosolic localization (CCO-CYTOSOL / GO:0005829), 94.6 kDa experimental complex mass, four subunits, and NAD rather than NADP specificity. MONOMER-14397 records 24 kDa experimental mass separately from 28.232 kDa sequence-derived mass. ENZRXN-15651 records physiological left-to-right direction, pH `8:9`, Km 150 μM for NAD and 200 μM for CPD-290. Its narrative reports no achieved reverse reaction in vitro and a **proposed** unstable beta-ketoacid. These are database assertions citing PMID4341530; this native-source stage has not read that paper and does not convert them into primary observations.

## Identity and source conflicts

`known-conflicts-and-dispositions.json` preserves exact source locators and hashes. The main restrictions are:

- PWY-2503 calls the cis-dihydrodiol-to-catechol step “reduced,” while its native reaction consumes NAD+ and produces NADH. Preserve the substrate-dehydrogenation/cofactor-reduction distinction.
- ORG-6075 has a Cupriavidus necator parent, but its comment describes JMP222 as a plasmid-cured derivative of Cupriavidus pinatubonensis JMP134. The relevant full organism frames are retained. No modern strain equivalence is forced.
- CPLX-7698 and MONOMER-14400 are assigned JMP222, while their descriptive component/cofactor claims cite Pseudomonas C-1 work. Native CPLX-7701 also assigns JMP222 to properties attributed to Reiner's historical preparation. Resolve preparation identity from actual primary methods before authoring strain-specific claims.
- The first-step activity evidence slot names PMID4341530, a paper titled as purification of the second-step enzyme. Preserve the exact native attachment; it is a paper-scope follow-up, not proof that the paper contains no first-step context.
- The CPLX-7698 comment says “dependent on NAD,” whereas the native reaction and reductase description specify NADH. Treat this as a source redox-wording ambiguity pending primary reconciliation.
- MONOMER-14397 → UniProtKB:Q0KAB0 and G-10983 → Entrez:4248800 are explicitly **Ortholog** links. They cannot establish exact JMP222 sequence or gene identity.
- PMID18505728 is an unrelated L-rhamnose paper nested in the Azotobacter species object; it is not benzoate pathway evidence.

The four Xyl proteins have native `unification` links to P23099/P23100/P23101/P23102. Both reactions also contain eight `RELATED-TO` UniProt leads. All 116 native database cross-references retain their relationship type. No UniProt, Entrez, NCBI Taxonomy, GO, or ChEBI issuing identity or sequence verification is claimed by this package. Native labels, family membership, and orthology must not be converted to exact identity silently.

## Deliverables and next steps

- `complete-native-object-inventory.json` and `complete-direct-slot-ledger.json` bind every retained full object and slot.
- `native-closure-proof.json` binds components, genes, exact regulation-target exclusions, and alternative-activity boundaries.
- `native-source-assertion-proposals.json` contains 72 locator-bound assertions of at most 400 characters, with explicit native-only, preparation-pending, or conflict statuses. These are research proposals, not a record graph.
- `native-xref-leads.json` and `native-publication-leads.json` retain 116 typed cross-references and 19 publication leads. Generic cluster background, unrelated species metadata, and benzoyl-CoA alternative-route papers remain context, not evidence for the selected two-step pathway.
- The compact and artifact manifests bind complete originals, acquisition receipts, projections, inert helpers, and source-context limits. The author replay checks preservation and reproducibility; it is not an independent scientific review.

Next, combine this package with the separately frozen primary and chemistry packages. Verify issuing biological identities where exact mappings are needed, reconcile every preparation-specific native claim, and rebind to the verified post263 merged corpus. Then a record author may make explicit curation decisions. No source or licensing exhaustion, final biological completeness, or merge readiness is claimed here.

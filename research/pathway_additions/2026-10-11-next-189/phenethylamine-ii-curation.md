# Phenylethylamine degradation II

The target is the complete, exact **MetaCyc:PWY-6534** route in *Pseudomonas putida* strain U: RXN-11510 produces phenylacetaldehyde, then PHENDEHYD-RXN produces phenylacetate. Both native members, their order, and every current Rhea chemical side are retained. The selected directed reactions are **RHEA:36724** and **RHEA:21393**. Neither phenylethanol degradation nor downstream phenylacetate assimilation is claimed as included.

## Identity and novelty

Both the new worktree and original Documents checkout were searched with `rg --no-ignore --hidden`, excluding only Git administrative internals and the installed `.venv`. Exact pathway, reaction, protein, PMID and DOI terms, plus the relevant labels and mechanism names, are recorded in `phenethylamine-ii-dedup.json`; complete hit logs remain external. Existing references were the prior route-I investigation, generated representations of that record, authority terms, and its reviews. The prior source manifest explicitly retained PWY-6534 as the distinct route-II lead. It was not a rejected permanent duplicate.

The maintained degradation-I pathway is the copper/TPQ/O2-dependent *E. coli* route. Reusing its downstream RHEA:21393 is legitimate reaction reuse. GO:0019607 is broader and explicitly cross-references both variants, so it is not substituted for the exact native variant identifier. The current record uses species taxon NCBITaxon:303 while naming the experimentally investigated strain U in its description and taxon-edge limitation. It makes no species-wide capability claim.

## Evidence and source tiers

The inspected primary abstract of Arias et al. ([PMID:18177365](https://pubmed.ncbi.nlm.nih.gov/18177365/), DOI:10.1111/j.1462-2920.2007.01464.x; print 2008, electronic 2007) establishes the strain-U two-stage conversion. Its short original wording includes “its deamination to phenylacetaldehyde by a quinohaemoprotein amine dehydrogenase”. The abstract also names transport and accessory Pqq/Ccm systems. It does not independently establish all complex stoichiometries or enzyme properties.

The publisher full HTML and PDF returned HTTP 403; the Crossref-listed TDM endpoint returned 400. Europe PMC and OpenAlex report no available open full text. These failed bodies and exact hashes are recorded, but are never scientific evidence. The original abstract is retained as Europe PMC core JSON. The main paper's full body, figures, assay conditions and mutant tables were **not** inspected.

Original MetaCyc 22.5 XML provides native membership, reaction crosswalks, protein identities, annotated complex composition and detailed activity context. BRENDA release 2026.1 provides original source-specific tables for reference 686425. BRENDA assertions are attributed to BRENDA, not quoted as primary-paper text. The YAML uses the paper DOI to identify this source-specific annotation reference, with a BRENDA title, URL, version and exact BRENDA-body hash; the separate PMID reference identifies the actually inspected primary abstract.

All five selected UniProt entries are unreviewed TrEMBL records. Their strain-U sequence evidence is ECO:0000313. Domain/profile assignments are ECO:0000259 or ECO:0000256 and are not promoted to experimental catalytic annotations. The original **ENA EF406120.1** sequence submission independently identifies strain U and the exact PeaA, PeaD, PeaC, PeaB and PeaE translations. Current UniProt PeaC includes additional strain submissions; the replay compares the sequence against the original U translation, rather than treating every added locus as a U locus.

## Components, cofactors and limits

| Component | Retained role | Evidence limit |
| --- | --- | --- |
| PeaA/B1N7H2, PeaD/B1N7G9, PeaC/B1N7H0 | Native CPLX-8088 components, one of each | BRENDA explicitly calls the heterotrimer assignment in silico. Edges retain that tier; no direct strain-U structural experiment is claimed. |
| PeaB/B1N7H1 | Accessory activity/maturation requirement | Native knockout annotation and BRENDA processing role; no fourth catalytic subunit, separate chemical reaction or specific Fe-S stoichiometry is asserted. |
| PeaE/B1N7H3 | Enables NAD-dependent aldehyde oxidation | Does not assert monomer sufficiency or fixed assembly. Native CPLX-8089's homodimer is an evidence source, not a declared complex. |
| CTQ | Bound cysteine tryptophylquinone residue, CHEBI:20252 | Old native CPD-12470 maps free CTQ CHEBI:73670. The bound residue is selected explicitly using ChEBI and primary enzyme-class context; no free CTQ consumption or exactMatch is asserted. |
| Heme | Generic CHEBI:30413 cofactor class | BRENDA annotates two redox-active hemes. No fixed Fe(II)/Fe(III) species or direct U stoichiometry measurement is inferred. |

For PeaE, native annotation reports retained activity and growth after deletion. BRENDA proposes PeaF/G as replacement contributors; the same authors' 2020 secondary review describes PeaEFG as a complex. These statements do not establish a fixed physical assembly or exact additional catalytic equations. The record therefore preserves PeaE's supported activity association and leaves the assembly unresolved. Original ENA identities **PeaF B1N7H6 / ABR57208.1** and **PeaG B1N7H7 / ABR57209.1** are retained in the source projection with their original unknown-function annotations. No guessed catalysis, donor specificity or `has_part` relation is added for them. This is a complete native chemical route with explicitly incomplete protein-level physiology, not a claim that the listed proteins alone reconstitute growth.

The 1998 original [Adachi et al. paper](https://www.jstage.jst.go.jp/article/bbb/62/3/62_3_469/_pdf) is retained as a 10-page scanned PDF. Page 470, Materials and Methods, explicitly uses *P. putida* **IFO 15366**, originally YU 92311. Rendered pages 469, 470 and 477 were examined for abstract, strain and carrier context; the full article was not exhaustively reviewed. It does not establish azurin identity in strain U. The complete original HTML of [PMID:22235135](https://pmc.ncbi.nlm.nih.gov/articles/PMC3307263/) was retained; Introduction and Experimental Procedures were inspected for bound CTQ and maturation scope. Its actual experiments concern *Paracoccus denitrificans* **Pd1222**, not U. Neither comparison is transferred as a strain-U experimental result.

## Chemistry and boundary

Rhea 142 represents the first reaction with a **generic A/AH2 pair**, CHEBI:13193/CHEBI:17499. These full sides remain in the graph. The formal two-hydrogen representation is not a specific physiological electron-transfer protein and does not claim that a single azurin molecule carries two electrons. No azurin/cytochrome-c550 protein is selected for U, and no oxygen-consuming respiratory regeneration reaction is invented. This is an unresolved carrier identity within a supported generic native equation, not contradictory specific chemistry.

Current Rhea uses protonated **2-phenylethanaminium CHEBI:225237**, not neutral phenethylamine. The aldehyde and phenylacetate sides retain current ChEBI charge forms. The NAD-dependent reaction produces **two hydrons**. Both formal equations balance atoms and charge against independently read Rhea and ChEBI values; dummy `A` in ChEBI and `R` in Rhea denote the same generic carrier class and are normalized only for symbolic balance. PHENDEHYD-RXN is natively reversible and maps to RHEA:21395; separate Rhea family evidence and native pathway layout justify selecting forward RHEA:21393 for the route.

The native boundary contains no explicit import, cofactor-maturation or respiratory-chain reaction. PeaH transport and PeaR regulation of that uptake system are retained as external gene dispositions in the original sequence projection; no ATP/import stoichiometry is guessed. The primary abstract's PqqABCDEF/CcmABCDEFGHI systems and later QHNDH maturation studies are considered but not recursively expanded into additional native members. PeaB's directly annotated activity requirement is retained. No PQQ cofactor is assigned to the CTQ active site. Compartment and cross-membrane movement are not added without strain-U source grounding.

## Context and author checks

Root's `imodulondb-phenethylamine-ii-applicability.json` independently resolves the available P. putida PRECISE321 dataset as **KT2440**, not U. The current inventory has no Paracoccus dataset. The adapter outcome is not applicable to this strain-specific record; it is not negative biological evidence and no regulator or catalyst edge is derived from expression context.

`phenethylamine-ii-replay.py` checks original source hashes with streaming I/O, native two-member boundary/order, raw native crosswalks, fresh reconstruction of selected official Rhea RDF objects, TSV directions, all 12 reaction-side occurrences/coefficients, symbolic atom/charge balances, original U sequence translations, exact native component bridges, source-level limitations, native/closed schemas and actual in-memory KGX export. It does not replace independent scientific review. Root owns shared authority regeneration, complete rendering and full-corpus gates. Actual narrow terminal results are retained in `phenethylamine-ii-validation.json`; no passing broad gate is claimed here before root runs it.

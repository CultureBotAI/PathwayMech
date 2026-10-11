# Complete 2-methylcitrate cycle I with unresolved absolute stereochemistry

This is a successor assessment of [issue #332](https://github.com/CultureBotAI/PathwayMech/issues/332), not a claim that the biochemical stereochemistry dispute has been settled. The record is [MetaCyc:PWY0-42](../../../data/pathways/2-methylcitrate-cycle-i.yaml), with all five native reactions represented. The new evidence that changes curation feasibility is the pair of separately issued, approved generic Rhea reactions 57493 and 57497. They use stereounspecified CHEBI:15598 and cite the 2017 primary study. They are broader parents of the historical stereospecific reactions; their equations have not been edited.

## Identity, novelty and full boundary

The initial PathBank lead SMP0002069 / PW002057.owl is **Propanoyl-CoA Degradation**, a different five-reaction map. Its native reactions 6005 and 6007 describe carboxylation and epimerization without native controllers. Reactions 6006, 6008 and 6009 correspond to the already maintained Sbm/ScpABC route, [conversion of succinate to propanoate](../../../data/pathways/succinate-to-propanoate.yaml). That three-step overlap does not cover the full PathBank map. The map remains deferred and is not mapped exactly to the new record.

PWY0-42 is the independently reviewed five-member 2-methylcitrate cycle I: propionate activation; condensation with oxaloacetate; methylcitrate dehydration; cis-methylaconitate hydration; methylisocitrate cleavage. Its native comment explicitly puts regeneration of oxaloacetate through the TCA cycle outside the depicted linear pathway. The AcnD/PrpF alternative belongs to cycle II and is not silently incorporated. The native membership, order and selected Rhea orientation are retained in [the projection](propanoyl-source-projection.json).

The searches in [the duplicate-search ledger](propanoyl-duplicate-searches.json) included ignored and hidden files in both the new worktree and the original Documents checkout; only Git internals and virtual environments were excluded. They located the prior conflict dossier rather than a maintained exact pathway. GO:0019629 and GO:0019679 are obsolete, replaced by the broader GO:0019543, so they do not replace the exact native identity.

## What resolved the representation blocker

The 2002 E. coli study assigned (2S,3S)-methylcitrate. The 2017 study found that E. coli PrpC and Bacillus subtilis MmgD produce the same stereoisomer, but assigned it to either (2S,3R) or (2R,3S). The full 2017 supplement, especially Table S1 and pp. S4–S13, explains its NMR/standard comparisons and acknowledges that one of the conflicting assignments is incorrect. Its relative assignment is not a claim that the enzyme produces a racemate. The inspected PrpC and PrpD UniProt 2026_03 entries retain that caution.

Current Rhea 142 supplies a representation that the previous selected-node projection missed:

| Native transformation | Specific Rhea family | Generic parent and selected direction |
| --- | --- | --- |
| 2-METHYLCITRATE-SYNTHASE-RXN | 23780; LR 23781 | 57492; LR 57493 |
| 2-METHYLCITRATE-DEHYDRATASE-RXN | 17725; LR 17726 | 57496; LR 57497 |

Both parent relations are explicit `rdfs:subClassOf` statements in the original RDF. Both generic masters are approved, cite PMID:28956599, and use the same Compound_14908 / CHEBI:15598. CHEBI:15598 has formula C7H7O7, charge −3 and no InChI stereolayer. The competing CHEBI:58853 and CHEBI:10860 have different stereolayers at the same formula and charge. The difference is not protonation or interchangeable numbering. Neither specific methylcitrate node is asserted in the maintained graph, and neither historical specific reaction is reused with altered sides.

The generic equations represent the experimentally supported transformations while leaving one unresolved property unspecified. They do not assert that every methylcitrate stereoisomer is synthesized or accepted. PrpD's alternative trans-product activity is explicitly outside the selected physiological cis branch. The cis product CHEBI:57872 is the source's (Z)-but-2-ene-1,2,3-tricarboxylate; downstream CHEBI:57429 retains its independently supported methylisocitrate configuration.

This is a proposed resolution of the **curation** blocker under #332's uncertainty-representation criterion, subject to independent review. It is not a resolution of the scientific absolute-configuration question, and this author did not close or modify the issue.

## Newly inspected later evidence

The full 2025 primary article PMID:40015638 / PMC11982470 was retrieved as original BioC XML. It investigates Pseudomonas aeruginosa PAO1 PrpB/AceA redundancy. Figure 4 and Results discuss accumulation of two methylcitrate forms; the LC-MS Methods at BioC offset 36579 use commercial standards for cell-extract measurements. This does not assign the isolated E. coli PrpC product. Its engineered PAO1 mutants, PrpB assays and methylisocitrate substrate mixture are not transferred into E. coli catalytic or stereochemical claims. This later article therefore strengthens the need to distinguish physiological metabolite measurements from an absolute PrpC product assignment; it did not itself resolve #332.

## Protein, assembly, metal and experimental scope

- PrpC P31660 is linked through native G6198-MONOMER to the two-subunit CPLX0-251 assembly. Current SUBUNIT evidence is experimentally annotated. Native catalysis and current protein FUNCTION support synthesis; the generic Rhea relation carries the unresolved configuration.
- PrpD P77243 is experimentally annotated as a monomer. The 2002 Blank study reports an unstable [2Fe-2S] cluster and reconstitution, whereas Brock's 2002 preparation retained activity without a detected metal requirement. The record states the conflict and asserts neither an obligatory cluster nor cofactor independence.
- AcnB P36683 supplies the hydration direction RHEA:17943, which is **right-to-left** relative to its Rhea master. Current evidence describes monomer and conditional homodimer behavior. Native CPLX0-7761 lists a component without a coefficient; a fixed assembly stoichiometry is therefore not asserted. `enables` preserves the gene-product/activity relation, and the supported [4Fe-4S] cofactor remains explicit. This is not omission of a required second catalyst.
- PrpB P77541 is linked through native G6196-MONOMER to the four-subunit CPLX0-1021 assembly. The primary 2001 abstract reports homotetrameric size-exclusion behavior and threo versus erythro substrate discrimination. The 2003 primary abstract and current annotation support Mg2+ dependence. Mutant active-site structures are not promoted to a universal wild-type assembly or substrate claim.
- PrpE P77495 and Acs P27550 are alternative activation roles. PrpE FUNCTION is ECO:0000250, not a fresh E. coli direct assay. Native Acs catalysis explicitly includes propionate, while current UniProt's catalytic equation is acetate-specific. The primary 2002 growth/protein-expression result favors Acs under its conditions; it does not establish exclusive Acs usage under every condition. Acs metal annotation is protein-level and retains its alternative-metal qualifier.

The local taxon is native MG1655; reviewed proteins are E. coli K-12. The 2002 transcription experiments used W3350, and purified or heterologously expressed proteins are distinguished from wild-type flux. Aerobic growth is not converted into an invented oxygen substrate edge. No universal essentiality, transport, compartment, regulation, PrpR edge, complete operon assembly, Acs/CobB catalytic complex, or external TCA regeneration is inferred. The 2025 PAO1 work and Bacillus-specific 2017 steps are not imported as E. coli enzymes.

The current cohort's shared iModulonDB receipts provide expression context only. The declared search included prpB/C/D/E and methylcitrate; it did not include acs/acnB. No exact queried gene appeared in the returned component table, which is not evidence of absent module membership, enzyme function or pathway flux.

## Source and validation limits

[The manifest](propanoyl-source-manifest.json) distinguishes fresh original response bodies, reused originals with acquisition time and fresh digest verification, and retained derived/tool-output excerpts. The 2017 main article was inspected at abstract level; the authentic 14-page supporting PDF was inspected, including rendered pp. S7 and S13. The 2002 publisher text retained in the prior dossier is a serialized web-tool excerpt, not a raw publisher HTML response. Claims attached directly to PMID references in this record use their inspected primary abstracts and explicit JSON locators. No failed retrieval or challenge response is used as evidence.

[The replay helper](propanoyl-replay.py) independently re-extracts the original Rhea objects, checks the two generic parents and the ChEBI structure distinction, all five native members, all 21 coefficient-bearing reaction-side occurrences, all five atom/charge balances, assembly bridges and six protein projections. It validates the native and closed schema and writes an actual isolated KGX export with the generic methylcitrate identity retained. The initial helper run reached export but failed because it indexed a KGX dataclass as a dictionary; that author-method error was fixed and the terminal run is recorded in [the validation receipt](propanoyl-validation.json). No biological assertion was changed by that helper correction.

This author replay is not an independent scientific review. Root owns shared identifier snapshot rebuilding, rendering, whole-corpus gates and publication. The exact absolute stereochemistry remains an explicit scientific limit after any successful software checks.

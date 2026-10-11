# Petrobactin biosynthesis — complete external author draft

This draft represents the complete ten-object boundary of MetaCyc PWY-6289, with both convergent assembly branches, the 3-dehydroshikimate precursor transformation, and carrier maturation. It is an author submission for independent review, not an approved maintained record. No repository owner, shared authority, prior sealed dossier or Git state was changed.

The exact native pathway identity is preferred because it independently defines this full boundary. The prior bounded GO search did not establish an exact process identifier. Upstream central precursor synthesis and iron uptake are outside the ten direct members. The source pathway and every original reaction were inspected; the document is not an easier subset selected around available enzymes.

| Native member | Selected identity | Disposition |
| --- | --- | --- |
| RXN-19493 | RHEA:48405 | Apo-to-holo aryl-carrier maturation retained; physiological catalyst unassigned. |
| DHSHIKIMATE-DEHYDRO-RXN | RHEA:24849 | AsbF-dependent precursor dehydration; exact native dimer retained. |
| RXN-10675 | RHEA:62469 | AsbC adenylation component retained. |
| RXN-10676 | RHEA:62477 | AsbC carrier-loading component retained; overlapping net Rhea reaction excluded. |
| RXN-10680 | RHEA:63809 | First citrate-spermidine ligation retained. |
| RXN-10681 | RHEA:63813 | Second ligation before aromatic transfer, first branch. |
| RXN-10682 | RHEA:64025 | Aromatic transfer on the bis(spermidine) intermediate, first branch. |
| RXN-10677 | RHEA:64029 | Aromatic transfer before second ligation, second branch. |
| RXN-10678 | RHEA:63817 | Second ligation after aromatic transfer, second branch. |
| RXN-10679 | MetaCyc:RXN-10679 | Authentic native terminal reaction with native product CPD-9985; no false Rhea equivalence. |

The native XML for the eight RXN-10675–10682 objects has no Rhea cross-reference. Its own membership, chemical objects and direction fields are cited separately from the current Rhea families and side assertions. The source projection supplies every edge's exact references and locators; the replay checks native membership and layout, all chemical sides, selected family directions and matched chemical structures.

## Identity and chemical decisions

Nine independently inspected native compound structures match the corresponding current ChEBI InChIs, formulas and charges. The terminal product is the exception. Native CPD-9985 and current ChEBI:142778 have the same formula and charge but different constitutional connectivity. In the native structure the aromatic-amide-to-inner-amine carbon paths are 3/3 and the citrate-amide paths are 4/4; ChEBI reverses them to 4/4 and 3/3. The original primary Figure 1A/C in PMID:22408253 agrees with the native structure. The live ChEBI original independently reproduces the pinned structure conflict. Equal formula, charge, name or a database cross-reference cannot establish equivalence.

The authentic native product and terminal reaction both resolve through original issuing-authority HTML. Consequently, the terminal reaction remains complete under MetaCyc:RXN-10679 with MetaCyc:CPD-9985. RHEA:63821 is a compared reference, never a selected reaction node, and ChEBI:142778 is never a selected participant or exact mapping.

The terminal native XML returns the broad Aryl-Carrier-Proteins class. The draft explicitly refines that output to the independently issued Rhea holo state: the current carrier-side assertion is evaluated separately from its erroneous small-molecule product, and primary Figure 1C depicts AsbD-SH release at the terminal transfer. Neither this refinement nor the parent-class relationship is an exact whole-equation equivalence. This source-separated refinement is a specific question for independent review.

RHEA-COMP:17557, 15903 and 15941 are whole generic carrier states, not free reactive groups or exact protein sequences. Conditional balance uses their reactive-part formulas with matched unspecified polypeptide scaffolds. It does not establish full-protein formulas or assembly counts. The source-issued citryl intermediates do not specify absolute citrate-derived stereochemistry. Preserving these classes does not assert racemic physiological intermediates or universal stereoisomer acceptance.

## Experimental and organism scope

The selected organism is NCBITaxon:260799, Bacillus anthracis str. Sterne. The principal complete pathway article used Sterne 34F2-derived preparations; figure gene labels use Ames identifiers and are not strain proof. The original Sterne genome translations and a newly retrieved six-entry GenPept batch establish versioned gene products AAT54153.1–AAT54158.1. Gene-product functional assignments combine this source identity with the explicitly scoped primary work and reviewed annotations. They do not claim that the full laboratory constructs equal these unmodified native sequences.

Four original translations equal their current reviewed UniProt sequences. The original AsbB translation is the suffix of current Q81RQ8 after two residues; current Q81RQ5 is the suffix of original AsbE after four residues. These N-terminal annotation differences remain visible; neither pair is exported as an exact full-sequence mapping. Original RCSB metadata independently identifies the Sterne source and mapped regions for the AsbB and AsbF structures, while preserving engineered-construct limitations.

The original AsbF complex CPLX-7874 has two components and agrees with direct structural and solution evidence in PMID:18955706. Manganese binding is experimentally supported, with alternative divalent-metal reactivation stated explicitly. The AsbB preparation is dimeric by structure and solution data; no source-issued exact physical complex was verified, so the gene-product role does not imply monomer sufficiency. AsbA/C/D/E fixed assemblies remain unresolved in the inspected scope. Magnesium in ATP-dependent assay context is not converted into independent binding edges for every enzyme. No cellular compartment or transcriptional regulation is inferred.

PMID:22408253 supports both convergent routes in vitro. The formal monoaryl step on the bis(spermidine) branch is a current database representation: the primary observed downstream product and proposed successive transfers because the intervening monoaryl species did not accumulate. A unique intracellular order remains unresolved. The early free-aroylspermidine route and partial AsbB substitution for AsbA are retained as source context, not additional direct members or universal gene-essentiality assertions.

## Source access and evidence limits

Original full articles PMID:22408253 and PMID:18955706 were read, including the original structure/pathway figure and the cited results paragraphs. PMID:17346033 is used only at the inspected indexed-abstract level. Its unavailable original full text and the unavailable later supplement are recorded with failed/challenge attempts; no rejected body is treated as a PDF or evidence. Native database assertions retain their own locators and are not presented as quotes from their cited papers. The exact endogenous carrier-maturation catalyst is unresolved within the bounded inspected primary evidence; the chemical transformation is retained without an invented protein.

The retained current iModulonDB inventory contains 20 organisms and 28 datasets, including Bacillus subtilis but no Bacillus anthracis or Sterne dataset. This establishes inapplicability for the exact record scope in that inventory, not expression absence. No expression or regulatory relation is transferred across species.

## Duplicate and validation scope

Fresh `rg -uu` searches covered the whole reference checkout and original Documents checkout, excluding only Git internals and the runtime environment. The current reference search covered 212 records; the original search covered 211. The sole original ignored hit was a SEED selector label for petrobactin-mediated iron uptake. Prior scout reports and all their distinctions were read. Frozen aerobactin, desferrioxamine B and bacillibactin candidates have different full boundaries and chemical products. No global source-exhaustion claim is made.

Author checks use the actual canonical parser/schema/identifier/KGX implementations from the reference repository, with all outputs confined to an external sandbox. Original Rhea is reparsed, original bodies rehashed, the exact terminal connectivity compared, native and current protein identities checked, both complete branches balanced, and invalid terminal substitution, maturation-catalyst invention and pathway truncation actively rejected. Derived net stoichiometry is bookkeeping, not a primary ATP/product measurement. The exact terminal original reaction, the carrier refinement, strain/construct attribution and unspecified stereochemistry require independent scientific assessment.

Shared corpus rendering, full repository gates, history, immutable review and publication are deferred to root's later isolated integration. This submission adds no culture, synthesis procedure, production optimization or engineering instructions. Original articles, genome sequences and complete source database bodies remain external; public access is not redistribution clearance.

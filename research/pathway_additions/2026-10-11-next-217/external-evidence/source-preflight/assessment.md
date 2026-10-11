# Myxochelin A and B: bounded source preflight

This is an external source assessment, not a draft, final scientific review, or publication approval. The precise candidate is **MetaCyc:PWY-8383, myxochelin A and B biosynthesis**. The full route is biologically well supported and absent as a complete maintained record in the two searched checkouts. Authoring still needs explicit adjudication of the source-defined N6-first intermediate and completion of source/identifier intake. No maintained files were changed and source access is not exhausted.

## Exact boundary

The retained original MetaCyc XML identifies PGDB version 27.0 and contains nine direct reaction members: DHBAMPLIG-RXN, RXN-23310, RXN-22679, RXN-23308, RXN-23316, RXN-23312, RXN-23313, RXN-23314 and RXN-23315. It has no nested pathway member. PWY-5901 is a separately linked precursor route at 2,3-dihydroxybenzoate, not a member of PWY-8383. Thus the exact named boundary starts with supplied DHB and lysine and includes both aldehyde-derived endpoints. This differs from the nested PWY-5901 membership of the existing bacillibactin pathway. The source's HTML frontend and XML metadata versions must not be silently equated.

The complete boundary contains DHB adenylation and MxcF loading, lysine adenylation and MxcG loading, two iterative condensations, carrier-thioester reduction to a free aldehyde, aldehyde reduction to myxochelin A, and glutamate-dependent transamination to myxochelin B. RXN-23314 is written in the oxidation orientation but explicitly has physiological right-to-left direction; the other eight members are physiological left-to-right. RXN-23309 and RXN-23311 are separately issued composite lysine/DHB loading reactions. They are not members and must not be added alongside their two explicit component steps.

The pathway lists multiple producing taxa. The proposed specific implementation is Sg a15, supported by original primary experiments and AF299336.1, not a transfer from DW4/3-1, Myxococcus DK1622, or Sorangium So ce56. The current taxonomy issuing source labels NCBITaxon:675526 **Allostigmatella aurantiaca Sg a15**, retaining Stigmatella aurantiaca Sg a15 as an exact synonym. No exact myxochelin process name was found by the documented pinned GO SQL text query; that is a bounded query, not a global claim of ontology absence.

## Primary evidence and historical limits

The complete original 2001 PNAS HTML (PMID11562468, DOI10.1073/pnas.201167098) was read. It directly reconstitutes A with MxcE/F/G, DHB, lysine, ATP and NADPH; NADH also works more slowly. The genes were amplified from Sg a15 genomic DNA. The intein-chitin constructs retained C-terminal extensions (LEPG or EFLEPG), and N-terminal processing was observed for E/F. MtaA coexpression matured carrier preparations; mass-shift evidence directly covers MxcF and isolated PCPG, not a quantified occupancy of full-length MxcG. The paper's Figure5C explicitly leaves the first amidated lysine nitrogen unknown. B formation and the MxcL step were then proposed, not directly reconstituted in that paper.

The official 2008 supplement (PMID18498160, DOI10.1021/ja8025278) was retrieved through the exact DOI-linked ACS Figshare article2933347/file4631935 and all four pages were extracted, rendered and visually inspected. It describes N-terminal His6-MxcL made from pCBP-MxcL (citing the 2005 study), E. coli expression, PLP spectra, complete A/B reconstitution, and aldehyde LC-MS/MS/derivatization. Product ratios depend on the reported assay conditions; the abstract supports competition for free aldehyde. The full main article was not obtained locally: official ACS requests failed, and a public copy failed retrieval. The supplement is not mislabeled as the main article. Neither the inspected supplement nor abstract settles condensation order.

The 2000 full publisher text was read through web rendering, while the corresponding local request returned403. It establishes the Sg a15 cluster/production and gene-inactivation context but contains older proposed MxcA/MxcG reduction alternatives and putative regulation. The 2005 publisher abstract and original PubMed XML (PMID15678426, DOI10.1002/cbic.200400206) were read; the complete main body was not obtained. The precise sequence of the pCBP-MxcL-derived tagged 2008 construct therefore remains qualified. No local original full-text SHA is invented for these web-only or unavailable bodies.

## Protein and carrier identity

Original AF299336.1 explicitly identifies Sg a15/taxon675526 and links the cluster paper PMID11029592. Exact full translations match current original UniProt batch entries:

| Gene | Versioned protein | UniProt | Length |
| --- | --- | --- | ---: |
| mxcE | AAG31128.1 | Q9F638 | 543 |
| mxcF | AAG31129.1 | Q9F637 | 311 |
| mxcG | AAG31130.1 | Q9F636 | 1456 |
| mxcL | AAG31135.1 | Q9F631 | 420 |

These are exact native-sequence bridges, not identity assertions for every engineered construct. The UniProt entries are unreviewed and species-level; sequence equality plus the versioned genomic source supports the strain link without renaming its header. Native MONOMER-124161/124162/124163 independently link E/G/L to these accessions and Sg a15. The catalytic object attached to the shared DHBAMPLIG-RXN is instead Vibrio VibE/CPLX-7945; it must not become the myxochelin catalyst by inheritance. MxcE's own original record and the primary reconstitution provide the actual E evidence.

Six source-native carrier classes are required: MxcF, 23-DHB-MxcF, MxcG, Lysyl-MxcG, N-23-DHB-Lysyl-MxcG, and N-N-di23-DHB-Lysyl-MxcG. Their inspected native objects do not supply full CML/InChI/formulae. They describe reactive states, not an exact tagged protein or measured assembly. Holo carriers are the native route inputs. MtaA-dependent experimental maturation is essential supporting context, but the precise physiological Sg a15 PPTase is not established by the heterologous coexpression experiment; do not infer an exact native activation catalyst or omit this qualification. The term biosynthetic complex does not establish fixed E:F:G:L assembly stoichiometry. PLP-MxcL has direct support; MgCl2 in a mixed assay recipe alone does not prove a specific isolated-enzyme metal dependency.

## Chemistry and representation decisions still needed

Native small-molecule InChIs, coefficients and directions were re-extracted. The executable replay verifies four exact small-molecule balances and five symbolic carrier balances. Carrier residue deltas were algebraically derived solely to test native equation consistency; they are not source-issued complete carrier structures or measured whole-protein formulas. The overall carrier-cancelled balances are exact in the selected native ionic forms:

* A: 2 DHB + lysine + 3 ATP + 2 NADPH → myxochelin A + 3 AMP + 3 PPi + 2 NADP.
* B: 2 DHB + lysine + 3 ATP + NADPH + glutamate → myxochelin B + 3 AMP + 3 PPi + NADP + 2-oxoglutarate + 2 H+.

These are stoichiometric derivations, not measured ATP/product ratios. Both branches, all nine transformations, and the alternative NADH activity must be retained in the eventual source disposition. Carrier reuse does not imply a fixed number of physical protein molecules.

The original ChEBI255 SQL was freshly hashed and queried. CPD-25905 and CHEBI:7061 have identical full InChIs. CPD-25904 specifies one stereocenter whereas CHEBI:31877 omits it; the latter is broader, not an exact structural substitute. Use of the exact native product is a defensible identity lead, pending normal canonical label/authority intake. The native aldehyde CPD-25916 has its own complete structure. Neither a generic aldehyde SMILES inherited by its page nor a supplier synonym replaces that structure.

The important unresolved assertion is **N6-first specificity**. The native monoacyl class explicitly names N6, but original Figure5C says which amide forms first is unknown. This is an unestablished ordering convention, not proof the N6-first route is false. It cannot be described as directly demonstrated. Proposed representation: preserve all nine native reactions and the exact N6 class as an explicitly qualified database convention, while separately recording that the first amidation order is experimentally unresolved. Root must independently adjudicate that scope before authoring; if that representation is not accepted, locate an independently issued order-unspecified monoacyl or net two-condensation representation. Do not rename the existing N6 class, invent an identifier, drop a condensation, or call a shorter pathway complete. A new primary paper establishing order would also resolve this point. Full current-source identity and carrier-state labels still require routine production-authority intake.

MIBiG BGC0001345.5 is useful cluster provenance but explicitly has questionable quality and unknown completeness. It does not override the exact reviewed pathway definition. Its related Myxococcus and congener cluster links are not Sg a15 assay evidence. No new iModulon query was run for this preflight; dataset applicability should be checked for the exact organism during curation, without using transcriptome context as catalysis proof.

## Novelty and next work

The exact native pathway, defining reaction/compound/protein IDs, gene labels, primary IDs and cluster accession were searched using `rg -uu --follow` in original Documents main and next215. Only Git internals and dependency environments were excluded. Four defining hits per checkout are pre-existing cross-Mech UniProt annotation rows for E/F/G/L; they are not pathway graphs. Shared DHB/PWY-5901 hits include existing E. coli precursor biosynthesis and the distinct complete bacillibactin record, plus their source/review/export/history derivatives. Their boundary narratives were read. A supplementary search of newly resolved native monomers/composite reactions, both ChEBI products and the 2005 primary identifiers returned zero matches in both roots. The supplementary observations bind original main6bdd43b and next215 head e61e31e. No complete myxochelin record was identified within this explicit text-search scope; compressed archives were not exhaustively unpacked.

Recommended handoff: a strong full nine-member candidate, with a bounded native-order/primary-uncertainty adjudication before drafting. Keep both product branches and experimental maturation context. Obtain/inspect the 2005 and 2008 full main bodies if feasible, verify the MxcL historical construct link, resolve the monoacyl representation, acquire canonical source-native labels, and independently review any subsequent whole-route record. This preflight does not authorize production code changes or claim that sources are exhausted.

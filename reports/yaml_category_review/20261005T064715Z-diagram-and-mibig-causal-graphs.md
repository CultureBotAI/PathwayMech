# YAML Category Review: Native diagram and MIBiG causal graphs

- Repository: CultureBotAI/PathwayMech
- Category: 12 WikiPathways, 3 Reactome BioPAX and 1 MIBiG records
- Selection Rule: Every corpus record rooted in WikiPathways, Reactome or MIBiG; the sixteen exact files below.
- Started UTC: 2026-10-05 (precise first inspection time not retained)
- Finished UTC: 2026-10-05T06:47:15Z
- Verdict: Complete sixteen-record source audit with authorized corrections; explicit scientific gaps remain.

## Target Category

All sixteen complete records were examined against native GPML/BioPAX/archive objects, independently grounded identifiers, current protein/reaction sources and relevant experimental papers. User authorization expanded the normally read-only review skill to curation. No GitHub mutations or paid calls were used.

## Selection and Membership

| Record | Source | Original edges | Reviewed edges before later cofactor enrichment |
|---|---|---:|---:|
| 2-phenylethanol-biosynthesis | WP5587 | 15 | 33 |
| acetogenesis | WP5019 | 26 | 55 |
| glutamate-degradation-i | WP556 | 6 | 17 |
| glutathione-glutaredoxin-redox-reaction | WP392 | 14 | 17 |
| glycogen-catabolism | WP478 | 7 | 9 |
| isoleucine-degradation | WP178 | 6 | 21 |
| linearmycin-biosynthetic-gene-cluster | MIBiG:BGC0002072 | 0 | 4 |
| mycobacterium-trehalose-biosynthesis | R-MTU-868688 | 22 | 48 |
| mycothiol-biosynthesis | R-MTU-879299 | 31 | 74 |
| mycothiol-catabolism | R-MTU-879325 | 5 | 13 |
| nad-salvage-pathway-v | WP171 | 26 | 38 |
| peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways | WP5060 | 89 | 108 |
| phospholipids-degradation | WP71 | 6 | 6 |
| tca-cycle-detailed | WP296 | 51 | 59 |
| triglyceride-biosynthesis | WP266 | 10 | 28 |
| ubiquinol-6-biosynthesis-from-4-hydroxybenzoate | WP287 | 16 | 48 |

The precise native objects examined, excluded objects, identity corrections, and before/after counts are in [the exhaustive ledger](../causal-graph-diagram-review.json). The reproducible migration is `scripts/curate_diagram_causal_graphs.py`, tied to the recorded baseline commit. It must not be replayed over subsequent manual enrichment.

## Validation

All sixteen curated records passed semantic validation at handoff. Every GPML GraphId in their evidence locators was checked against the native XML. The three Reactome sources and all twelve GPML sources also passed offline importer smoke tests. Thirty-one focused importer/support tests passed; edited importer files, tests and migration script passed lint. Root owns full repository QC, identifier snapshot refresh and rendered products after cross-cohort integration.

## Lump and Split Review

Scoped yeast SPO14, GPH1/PGM and redox records remain scoped records, rather than claiming every unrelated branch in a broader native diagram. Duplicate GPML lines representing one DAHP condensation were merged. Distinct enzyme isoforms, native complexes, compartments and modified physical states remain distinct where the source identifies them. Cross-provider pathway duplicates were not adjudicated as part of this bounded causal-graph task.

## Identity and Grounding

Independent ChEBI/SGD/native source checks corrected ATP drawn with dATP cross-references, CoA drawn with an F420 CAS cross-reference, yeast Q6 versus Q9, exact mycothiol charged/substituted products, DAP stereochemistry, and inositol phosphate position. Three unresolved peptidoglycan chemical identities remain authentic source-local GPML node IDs, with unresolved external grounding disclosed rather than guessed. LnyI is grounded in primary NCBI protein AKL64828.1 and observed linearmycin products in exact ChEBI entries.

## Graph and Evidence Patterns

Synthetic GPML quotations and BioPAX comments misattributed to publication IDs were replaced by independently reconstructed source assertions with exact native object locators. Reaction direction, reversible transfers, enzyme/group roles, anchored co-substrates and cofactors, native catalytic complexes and locations are retained. Importer fixtures independently test these failure classes.

Scientific corrections include TreS physiological trehalose-to-maltose flux with reversibility (PMID23601637), principal MshB deacetylation with current Rhea chemistry, Mca cleavage of a mycothiol S-conjugate rather than free mycothiol, conditional Mca Fe/Zn support (PMID26044118), removal of unproven ImpC mycothiol phosphatase attribution after its experimental histidinol-phosphatase identification (PMID29752410), and removal of THI3 as a demonstrated branched-chain decarboxylase (DOI10.1128/AEM.01675-12).

## Completeness Patterns

Source-supported enzymes, water, phosphates, redox donors, nucleotide co-substrates, native metal-containing assemblies, and compartments were added. Acetogenesis no longer produces an unsupported free methyl radical; the corrinoid transfer/carbonyl assembly is explicitly aggregated. MIBiG's empty graph now records experimentally supported LnyI pathway enablement and observed linearmycin A/B/C production (PMID28919037), without asserting the paper's proposed starter sequence as established chemistry. The unrelated cigarette-smoker dataset PMID32964081 was removed.

DNA/RNA and organelles were checked where relevant. No regulatory transcription event was inferred merely from a gene list or an enzyme drawing. This is a scope decision, not a claim that DNA/RNA mechanisms do not exist.

## Findings

The major scientific and evidence failures identified in this cohort were corrected in the maintained records and in reusable importers. Remaining bounded gaps are documented per record: the mycothiol intermediate phosphatase enzyme is unresolved; three peptidoglycan chemical nodes lack verified external chemical grounding; yeast glutaredoxin partner details and ambiguous native branches are omitted; proposed linearmycin assembly chemistry is not asserted.

## Recommended Edits

Completed. Preserve the new per-object evidence, explicit source-local identities, physical-state distinctions, and enzyme/cofactor roles during future source refreshes. Do not regenerate reviewed files blindly from the raw providers.

## Follow-up Checks

Run the integrated corpus identifier gate, closed schema, complete pytest, lint, history validation and page regeneration after all cohort edits. Source importer tests cover manufactured evidence, complex flattening, conversion direction and diagram arrow errors. Source bytes and versions are pinned in the source manifest; the ledger records the baseline used for reproducibility.

## Additional Notes

No iModulonDB expression question was involved; that adapter was not applicable. Native source caches were directly inspected; primary publications and public reviewed protein/reaction sources were used for scientific conflicts. Searches used to locate caches included hidden and ignored files; the protected unrelated `/private/tmp/codex-daemon-501` directory could not be read and was irrelevant to pathway sources. The source-local peptidoglycan exclusions reflect exact inspected objects, not an unbounded absence claim.

Per-record decisions:

- **2-phenylethanol-biosynthesis:** Grounded missing G6P, prephenate, phenylpyruvate and phenylacetaldehyde; restored the connected Ehrlich route. Merged duplicate DAHP condensation lines and preserved reversible transamination. Collapsed glycolysis/shikimate branches have component enables relationships, not single-enzyme catalysis claims.
- **acetogenesis:** Restored explicit enzymes and directed cofactors. Corrinoid methyl carrier is not a free methyl radical: the two native carrier-transfer/assembly reactions are represented as an aggregate, without a free methyl-radical intermediate. Undirected connectors and energy-complex drawings are not reaction arrows.
- **glutamate-degradation-i:** Restored GAD1, UGA1, UGA2, proton/CO2, 2-oxoglutarate/glutamate, water and NAD(P) redox pair from native anchors.
- **glutathione-glutaredoxin-redox-reaction:** Restored GSH conjugate and redox cosubstrates. Removed the ungrounded glutaredoxin diagram branch whose controller and redox partner are not identified. GPX assignments remain diagram-level evidence, not an exclusive physiological electron-donor claim.
- **glycogen-catabolism:** Retained the explicitly scoped GPH1/PGM branch, including prior glucose-6-phosphate correction; restored shortened glucan product and phosphate. Ambiguous GDB1 debranching and SGA1 peripheral branches are not reinterpreted as complete reactions.
- **isoleucine-degradation:** Restored catalysts and cosubstrates. Excluded THI3 catalytic assignment: individual enzyme assays in DOI10.1128/AEM.01675-12 found no activity. No subcellular location inferred from isozyme identity alone.
- **linearmycin-biosynthetic-gene-cluster:** Reconstructed experimentally grounded LnyI dependence and three observed products; duplicated source linearmycin C is one entity. Proposed arginine-derived starter and PKS module skipping remain unasserted. Removed unrelated PMID32964081 (cigarette-smoking dataset). ChEBI product names, formulas and chain lengths checked against native structures.
- **mycobacterium-trehalose-biosynthesis:** All native sides, controllers, complexes, cofactors and cytosol locations inspected; source comments are not attributed as quotations from cited papers. Corrected TreS physiological direction and alpha-maltose product using PMID23601637.
- **mycothiol-biosynthesis:** All native sides, controllers, complexes, cofactors and cytosol locations inspected; source comments are not attributed as quotations from cited papers. Corrected Ino1/MshA stereochemical identity and MshA water/proton error; reconciled MshC/MshD charged forms/protons; added principal MshB alongside minor Mca. Removed unsupported ImpC catalyst, reidentified experimentally as HisN (PMID29752410); phosphatase catalyst remains unresolved.
- **mycothiol-catabolism:** All native sides, controllers, complexes, cofactors and cytosol locations inspected; source comments are not attributed as quotations from cited papers. Replaced incorrect free-MSH/S-acetylcysteine identities with RHEA36543 conjugate classes; qualified metal dependence using PMID26044118.
- **nad-salvage-pathway-v:** Restored nicotinamide, ATP/ADP/PPi and peptide substrates. Corrected ATP xrefs (source CAS1927-31-7 identifies dATP). Histone acetyllysine is represented as a protein residue, not free acetyllysine. Unmapped external pathway connectors are excluded.
- **peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways:** Restored missing cosubstrates where exact identity is available; reversed-arrow racemases and phosphoglucosamine mutase marked reversible. MurJ is transport support rather than an enzyme that polymerizes peptidoglycan. Cytoplasmic source is explicitly incomplete for membrane/periplasm steps; no omitted DNA/RNA nodes inferred.
- **phospholipids-degradation:** Retained the explicitly scoped SPO14 phospholipase D branch. Excluded ISC1 phosphatidylcholine claim contradicted by the source comment; PLC1 branch is outside this record scope.
- **tca-cycle-detailed:** Restored supported anchor cofactors and enzyme components; multisubunit groups enable the reaction instead of each subunit being independently catalytic. Q6 replaces the native Q9 cross-reference; source ATP and CoA CAS crossrefs incorrectly identify dATP and F420 and are corrected by reaction context and named chemical identity. Anaplerotic pyruvate branch is outside the retained TCA-cycle scope.
- **triglyceride-biosynthesis:** Restored acyl-CoA/CoA, water/phosphate, PC/lysoPC and enzymes; LRO1 and DGA1 remain distinct routes to TAG.
- **ubiquinol-6-biosynthesis-from-4-hydroxybenzoate:** Restored COQ catalysts, SAM/SAH, oxygen, reducing equivalents and carbon dioxide; retained the source generic electron acceptor classes. Source complex membrane attachment is tentative, so no certain compartment edge is inferred.

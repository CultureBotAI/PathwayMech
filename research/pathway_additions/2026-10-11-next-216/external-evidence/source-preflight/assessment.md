# Pyochelin source preflight — 2026-10-11

The complete MetaCyc PWY-6408 assembly pathway is a strong, unrepresented candidate for a carefully qualified external draft. This is source feasibility, not a scientific approval or a validated record. No record, shared authority, cache, repository, or GitHub state was changed.

## Identity, scope, and novelty

The independently retrieved active GO:0042864 term is **pyochelin biosynthetic process**. PWY-6408 explicitly lists eleven reaction objects assembling pyochelin from salicylate and two cysteines. Preserve all eleven. The two cysteine activations reuse RXN-11115 at flux two. The native overall RXN-11114 is not an additional member and must not be added beside its decomposition.

PchA/PchB supply salicylate from chorismate upstream of this native assembly boundary. A future GO record must state this boundary explicitly rather than imply that its graph covers all precursor supply. Carrier maturation and PchC editing are supporting context, not silently replaced assembly transformations. Transport, iron complexation, and uptake are distinct.

Fresh `rg -uu --follow` searches included hidden and ignored files in the original Documents checkout and prepared 213, 214, and 215 checkouts. Git storage and dependency environments alone were excluded. Exact pathway/GO/reaction identifiers, proteins, primary IDs, and label were searched. The two actual hits are a broad ignored SEED subsystem inventory and a quoted copy of that inventory in the staphyloferrin B dedup receipt. Both were inspected; neither is a maintained pyochelin record. The initial and expanded search receipts are preserved. This is a scoped absence finding, not a whole-computer claim.

## Complete native chemistry

The eleven original reaction bodies and all participating native objects were retained and projected without substituting convenient reactions. The native equations cancel all carrier intermediates and give:

salicylate + 2 L-cysteine + 3 ATP + NADPH + SAM → pyochelin monoanion + 3 AMP + 3 diphosphate + NADP + SAH + water + 3 protons.

Independent RDKit parsing of the original small-molecule InChIs gives zero residual atoms and charge. Three ATP is a stoichiometric derivation, not an experimentally measured ATP/product yield. The native carrier classes lack independent full formulas; their cancellation is not a claim that every whole-protein equation has been atom-balanced.

The generic PchE classes describe two different reactive domains on one protein. In particular, the two source PchE reactants in RXN-19469 must not be interpreted as two separate whole-polypeptide molecules or used to infer dimer stoichiometry. A future detailed replay should preserve the original classes, identify the ArCP/PCP roles, and derive only the reactive-group bookkeeping that the original chemistry supports.

The current Rhea ligase annotations are composite carrier-loading reactions. Their existence does not make them exact equivalents of the native adenylation half reactions. A source-to-graph ledger must retain this distinction if any Rhea identifiers are selected.

## Product identity and epimerization

The original CPD-9992 InChI is a monoanion with the pyochelin I stereochemistry. Current CHEBI:67183 has precisely the same stereochemical InChI after the explicit protonation-layer difference is removed. CHEBI:67185 is the other thioaminal epimer. CHEBI:29669 leaves that one center unspecified while fixing the other two and is therefore a broader neutral product class, not an exact identity for native CPD-9992. Native CPD-12093 is the optical antipode; do not transfer it from Pseudomonas fluorescens.

Primary PMID:17938167 identifies the interconverting pyochelin I/II pair in P. aeruginosa. The indexed primary and web-inspected PMC94946 Results/Figure 2 likewise support the pair rather than exclusive I production. A draft can retain the issued native I endpoint as an explicitly partial stereochemical projection of the experimentally observed mixture, or use a separately justified broader product representation. It must not label the two source structures exact equivalents or claim a single stereoisomer is the sole physiological output. This decision needs independent scientific review.

PMID:12950179 places PchE epimerization after amide formation rather than on the initially loaded cysteinyl intermediate. The 2022 PchE study supports an inserted epimerase domain. Preserve that chemistry in the cyclization/epimerization scope; do not invent an extra reaction identifier or erase the epimerization simply because the native list compresses it.

## Protein and primary-source scope

The original 1999 ENA submissions AF184620/AF184621/AF184622 are from **PA14**. Their translated proteins equal Q9RFM9/Q9RFM8/Q9RFM7 respectively. They differ from current PAO1 PchD/PchE/PchF by 3, 14, and 19 residues. These are real strain distinctions, not interchangeable labels.

The independent PAO1 submission AF074705.2 links the original 1998 and 2001 primary studies. Its PchE and PchG translations exactly equal current G3XCV2 and Q9HWG5. Its historical PchF translation differs from Q9HWG4 at six residues. Keep this discrepancy and do not claim that a historical engineered protein was sequence-identical to a modern entry.

The strongest newly inspected full sources are:

- PMID:35105906 / PMC8807600: original JATS, publisher HTML, main PDF, and 27-page supplement. PAO1 is explicit in Methods. Main Figure 1 and supplementary Figures 1/2 were rendered and inspected. Deposited 7EMY contains the exact current G3XCV2 core plus engineered tag. The PchE homodimer is direct evidence; it does not establish a stable PchD/E/F/G heterotetramer.
- PMID:30525512 / PMC6372355: original NCBI BioC manuscript. The full-length PchF construct is named O85740, currently a secondary accession of Q9HWG4; PAO1 supplied the didomain construct. Analogue experiments support late SAM methylation after reduction. They do not demonstrate equality of the complete historical construct or supply a measured whole-pathway ATP yield.
- PMID:27601130 / PMC5046821: original NCBI BioC manuscript. The PchG preparation is explicitly PAO1 and was tested with a free substrate analogue. The crystal dimers are Yersinia Irp3, not PchG. The source expressly limits the analogue's physiological kinetic and stereochemical interpretation.

PMID:10555976 and PMID:11467965 were inspected as original indexed/publisher abstracts, not full articles. PMID:11208777 has an original indexed abstract, original deposited sequence, and separately inspected PMC web-rendered Results/Discussion excerpts; its attempted BioC export returned an error despite HTTP 200. PMID:15375116 remains abstract-scoped after rejected full-text attempts. These limits are retained in the manifest. No challenge page is accepted as an article, and no web-only passage receives a fabricated local source-body hash.

## Native conflicts that must not be imported

1. RXN-11113 names MONOMER-15295, a **Yersinia pestis YbtE** entry linked to Q56950 and taxon 632. It is not Pseudomonas PchD. Independently supported PchD activity must replace this controller attribution in the proposed organism implementation while the original remains in the disposition ledger.
2. RXN-11113 and RXN-11115 attach PMID:17346033, a petrobactin AsbC/D/E paper. That citation is not pyochelin experimental evidence.
3. CPLX-7976 lists one each of four proteins. A reconstituted four-protein system does not by itself demonstrate a stable physical 1:1:1:1 assembly. Do not fabricate a PchE dimer identifier or transfer Yersinia assemblies.
4. The PchC source concerns editing. Product release belongs to the embedded PchF thioesterase; leave ancillary PchC support separate.
5. The early native description and modern primary sources differ in their level of stereochemical and mechanistic specificity. Keep original database assertions separate from experiments and use current direct evidence where its exact scope is established.

## Remaining work before author freeze

- Select and explicitly document the native-I versus physiological-I/II endpoint representation. Retain source-issued identifiers and the protonation distinction without an unsupported exact mapping.
- Obtain canonical native HTML authorities for every selected reaction/carrier class and confirm their exact titles. Current native XML proves issued objects and relationships, but this preflight does not claim a completed canonical label snapshot.
- Replay each represented reaction using independently grounded small-molecule/reactive-group formulas, with carrier-domain bookkeeping limits. The net check already passed; it is not a replacement for those checks.
- Preserve a full eleven-object source-to-graph and graph-to-source ledger, exact protein evidence tiers, PA14/PAO1 distinctions, and actual primary locators. Do not add a guessed assembly or broaden an analogue assay to native whole-carrier catalysis.
- Applicable retained iModulonDB inventory lists `p_aeruginosa/precise364` and `precise411`; exact strain/table context and gene queries remain a bounded root follow-up. Inventory alone proves no membership or expression claim.
- Draft only after root authorizes the next isolated task, then run actual schema, authority, KGX, source-replay, and independent review gates. None are claimed here.

The evidence supports continued complete-route curation. It does not support a source-exhaustion claim, a shortened substitute, or automatic approval.

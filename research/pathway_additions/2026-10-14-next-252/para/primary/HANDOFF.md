# Primary-evidence author-support handoff — next252

The five-step target is **MetaCyc:PWY-6336**, protocatechuate degradation III (para-cleavage), in **Paenibacillus sp. JJ-1b (ATCC 35889; NCBITaxon:649508)**. The 2009 primary article supports all five individual steps with recombinant crude-extract assays: PraA, PraH, PraB, PraC and PraD. The paper's broader Figure 1 also includes PraI entry from 4-hydroxybenzoate and PraE/F/G exit to central metabolism; these are outside the five-member target. This is author support, not an independent final review.

## Files suitable for compact maintained projections

- `component-evidence-ledger.json`: 35 explicit source/component dispositions, including core chemistry, construct identity, unstable intermediates, cofactor limits, regulation, transport, compartments, taxon scope and later primary research.
- `proposed-evidence-qualifiers.json`: five proposed catalysis evidence items plus two qualified PraB coenzyme edges, totaling **25 direct quotation words from PMID:19717587**. PraA uses a structured Figure2 data assertion; endpoint qualifiers use structured Table1 evidence. The included quote-accounting list counts every occurrence. Do not add more direct quotations without reallocating the budget.
- `uniprot-deposit-comparison.json`: full sequence equivalence of the five current UniProt entries to deposited original translations; source evidence annotations are retained.
- `deposited-cds.json`: original AB505864.1 CDS features and translations. A smaller projection can retain the five relevant identity rows and sequence digests instead of all ten genes.
- `artifact-manifest.json` and acquisition manifests: byte counts, exact digests, URLs, and actual payload type. **Files ending `.pdf` or `.zip` that contain challenge HTML are explicitly not evidence.**

The original article HTML, derivative full text, original figures, deposit XML and API responses are external under `originals/`; do not retain complete source text as a compact corpus projection.

## Exact proteins and assay scope

| Gene | UniProt | Deposited protein | Length | Assay construct |
|---|---|---|---:|---|
| praA | C4TP01 | BAH79099.1 | 266 | pETA23, pET21a(+), 0.8-kb NdeI–EcoRI insert |
| praH | C4TP08 | BAH79106.1 | 313 | pETH23, pET21a(+), 1.9-kb NdeI–HindIII insert |
| praB | C4TP02 | BAH79100.1 | 486 | pETB23, pET21a(+), 1.9-kb NdeI–HindIII insert |
| praC | C4TP07 | BAH79105.1 | 63 | pETC23, pET21a(+), 0.4-kb NdeI–EcoRI insert |
| praD | C4TP06 | BAH79104.1 | 260 | pC4D23, pColdIV, 0.8-kb NdeI–XhoI insert |

All five UniProt entries are **unreviewed TrEMBL**, and all five complete amino-acid sequences exactly match their AB505864.1 translations. The retrieved UniProt comments do not establish experimental cofactor assignments; the B/C family comments are automatic ECO:0000256 annotations. The paper's Table 1 and original deposited sequence source both identify the native strain as JJ-1b/ATCC 35889. BL21(DE3) is the experimental expression host, not an additional native pathway taxon.

PraH begins **MYDVH** in both deposited and current sequences. The paper reports measuring this N-terminus in the pETCH23 coexpression product and choosing the second of two consecutive ATGs for pETH23. Thus the assay start is consistent with the deposited native sequence; **do not label this a demonstrated deletion from C4TP08**. The exact assay C termini and any tag state were not independently resolved because the Table S1 primer supplement was not retrieved. Each assay endpoint should preserve that limitation. Natural downstream restriction-site reconstruction is only inferential and is not proof of the final plasmid sequence.

## Mechanistic interpretation

PraA produces the initially observed 350-nm species. The 20-minute trace and acid-extraction/GC-MS work demonstrate spontaneous conversion to HMS; failure to recover 5CHMS by GC-MS is not evidence that PraA directly produces HMS. PraH accelerates decarboxylation on the short assay timescale. The 2009 paper assigns products by spectra and GC-MS/HPLC features, with weaker exact stereochemical resolution than the native chemical frames. Figure 1 geometry corroborates the `(2Z,4Z)` initial cleavage intermediate, and the terminal product is **enol HPD**, not its keto tautomer. Native cross-reference mismatches identified by the native-source agent must remain rejected.

PraB supports both NAD+ and NADP+ in vitro: 1.19 ± 0.07 versus 0.113 ± 0.009 U/mg. The physiological representative reaction can remain NAD+-dependent, but the description must not say NADP+ is unusable. CHEBI:58349, already in the corpus, can represent the lower-activity alternative coenzyme on a similarly qualified PraB endpoint. PraD was assayed with 500 µM MgSO4; added magnesium alone does not establish a physiological metal requirement. PraH zinc coordination is a homolog-based discussion inference, not a measured metal result.

The 1993 primary abstract directly supports a native tetramer with one Fe2+ per subunit, removable substoichiometric Mn, and redox inhibition/restoration. The abstract does **not** provide the full EDTA/NTA protocol. The full 1993 article remained inaccessible during this pass; any detailed EDTA/NTA assertion must instead identify the inspected curated native source and preserve its evidence scope. Historical native purification and 2009 recombinant assays must not be merged into an assertion that the 1993 material was sequenced as C4TP01.

## Regulatory and scope dispositions

Figure **7** (not Figure 8) compares the praA promoter reporter with and without praR in E. coli DH5alpha. It supports PraR-dependent transcriptional repression and relief with 4-hydroxybenzoate or protocatechuate, with no direct ligand-binding or DNA-binding experiment. Native G-11541 identifies praA but does not identify the experimental promoter fragment or a transcription unit. The current qualifier schema cannot qualify a DNA reporter endpoint. Preserve this supported observation and the unresolved target-identity gap in the dossier; do not invent a promoter CURIE, type NCBIProtein as DNA, or redirect this evidence to inhibition of whole-pathway metabolic flux.

Figure 6 supports cotranscription and carbon-source-associated expression, not compartment localization. Comparative Figure 8's proposed benzoate transporter belongs to another bacterium; it does not support a JJ-1b transport edge. PraE/F/G were inferred from homology and whole-cluster growth complementation rather than individually assayed. These downstream activities can be represented by a source-verified PWY-5162 interface without expanding the five-member internal pathway.

## Reading and retrieval coverage

**PMID:19717587 / DOI:10.1128/JB.00840-09 / PMC2795304:** complete main HTML article read, including methods, both tables, all results/discussion and relevant cited references; all eight original figure rasters visually inspected. Original HTML URL: `https://pmc.ncbi.nlm.nih.gov/articles/PMC2795304/?pdf=render`; SHA256 `73d8f20f4d2502b2f69e205f1867056493598ad72993dab0e410bd9bd573a7c2`. Main figure/caption and table locations use HTML IDs `f1`–`f8`, `t1`, `t2`, and sections `sec2`–`sec27`.

The supplemental index and a 1.8-MB ZIP are listed, but PMC URLs returned challenge HTML, publisher URLs returned 403, and Europe PMC's supplement API explicitly reported that the article is not in its open-access set. **Table S1 and Figures S1–S7 are not directly inspected**; descriptions of their findings here are limited to what the main paper reports. Failed PDF responses likewise were not interpreted as full articles.

**PMID:453834 / DOI:10.1128/aem.37.3.614-618.1979:** complete abstract inspected from Europe PMC metadata; original body/figures not read. It corroborates separate cleavage/decarboxylation steps in native JJ-1b.

**PMID:8392511 / DOI:10.1128/jb.175.14.4414-4426.1993:** complete primary abstract inspected from independent Europe PMC and NCBI JATS front matter. Full article retrieval attempted through PMC and publisher URLs but not obtained. See the native-source agent for any later successful retrieval; this handoff does not claim one.

**PMID:42300662 / DOI:10.1039/D6OB00839A / PMC13254512:** complete main JATS text inspected, including methods/results/conclusions and tables; figure captions read, but raw figure rasters and supplement were not inspected. This June/July 2026 study independently uses engineered PraA to make 5CHMS, then studies a different pyridine diversion. It does not change the native five-step route. Full JATS SHA256 `90a423cfcbcb2e18432d7f84f55650d4adde846bbf1e1ae3bc544c6f7298ff92`. The 881-bp pET28a PraA insert, Ni-affinity preparation and Fe/ascorbate reactivation are distinct construct conditions, not evidence about the 2009 pETA23 tag state. Its main validated GDH5/DyP1B pathway concerns 4,5-cleavage CHMS and 2,4-pyridinedicarboxylate; do not transfer it to native JJ-1b para-cleavage. Supplement API retrieval timed out; no supplemental inspection is claimed.

A targeted current primary-literature search also surfaced a 2019 o-phthalate/2,3-dihydroxybenzoate route and a 2020 Bacillus licheniformis TAB7 study. They are neighboring pathways or inferred other-taxon clusters, not evidence to expand the exact JJ-1b para-cleavage record; these were discovery leads rather than full-text reviews in this pass.

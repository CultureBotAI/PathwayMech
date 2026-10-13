# Independent acetoacetate science review — next236

**Verdict: pass with explicit evidence limitations; no required scientific findings.**

Reviewer: `/root/aceto236_finish_review`, continuing the interrupted external review by `/root/aceto_science_review`. This is a complete independent scientific assessment of the exact external proposal, not maintained-record adoption, a saved native `record_review`, or acceptance of future authority implementation/runtime gates.

The reviewed draft is `acetoacetate-degradation.yaml`, SHA-256 `c3e00916088b02b418c83e033ac1773bafc7aac036bc28eda30829e776e6779c`, 79,655 bytes. It selects `MetaCyc:ACETOACETATE-DEG-PWY`, **acetoacetate degradation (to acetyl CoA)**. The author handoff is `96fa4db34b62078528c8d8d0998a84975cc2feaacd1572471f8502aefd471c73`; the preflight handoff is `44a729e4bfb83784783b02ee977b6dbbcc58e11c1f78a0a7d10bf81da7bdc47c`.

## Scope and independence

The successor reviewer freshly read every draft paragraph and edge, all 803 native semantic slots, all 215 complete UniProt comment/feature objects across six entries, and all 165 PathBank objects. Every object was then replayed from its bound original. Native CML rendering coordinates remain preserved and replayed; this review did not independently recalculate molecular geometry from those coordinates.

The successor also freshly read all 30 main-PDF pages of the three acquired primary papers: 1975 thiolases (5), 2007 AtoC (9), and 2022 YdiF (16), including Methods, Results, Discussion and references. Six selected scientific pages were visually inspected: thiolases pages 2–3, AtoC pages 5 and 7, YdiF pages 4 and 12. All 30 page texts were freshly re-extracted from the originals through macOS PDFKit and matched exactly to the reading projections. The predecessor's earlier readings are not claimed as the successor's work; their files are retained, and the fresh reading receipts are separately recorded.

The review covers all **29 paragraphs, 46 edges, 25 selected identity tuples and 66 references**. The 18 PMID references comprise three full acquired main papers, ten indexed abstracts, and five metadata-only records without an indexed abstract. The latter fifteen papers were not acquired/read in full. Supplement-only clone details, all supplemental datasets, and all cited papers are not claimed as read. This is a bounded review of the proposal and available evidence, not source exhaustion.

The applicable local review/addition and harmonization instructions were inspected. The author's 229-artifact packet and the inherited 376-artifact preflight packet were freshly closed by a 685-binding intake replay, including streamed hashes of the original ChEBI and NCBI Taxonomy databases. The database queries used immutable read-only connections and preserved their literal symlink targets. No maintained, authority-cache, Git or GitHub content was changed.

## Scientific assessment

The native route has two events. AtoDA transfers CoA from acetyl-CoA to acetoacetate; AtoB cleaves the resulting acetoacetyl-CoA with free CoA to yield two gross acetyl-CoA molecules. Cancellation gives acetoacetate + CoA → acetate + acetyl-CoA. Donor replenishment is explicitly a material-balance inference and does not claim channeling. Native transfer L2R and thiolase R2L orientation agree with Rhea 27807 and 21038. The two Rhea equations are alternative projections, and the two reversible thiolase constituents are decomposition context, not extra physiological events. All seven core sides, eight constituent sides and seven Rhea sides are retained with their coefficients.

The whole source frames support the nested AtoA2AtoD2 assembly and a separate AtoB4 complex: one alpha dimer and one beta dimer belong to the unnamed transferase parent. Individual chains are not asserted to catalyze the whole reaction. Apparent experimental masses, source sequence masses, crystallographic assemblies and preparation identities remain distinct. The two protein-bound residue classes are generic classes with their native parents; they are neither free cysteine nor a demonstrated exclusive AtoB state. CHEBI:25917 is peptidyl-cysteine, not free cysteine. All five small-molecule ChEBI identities and the PubChem mercurial anion agree with exact native InChIs; acid-form discovery xrefs are not substituted.

The source conflicts are explicitly and correctly handled. PathBank's thiolase equation places CoA on the product side and supplies only one acetyl-CoA; the draft rejects it. All five PathBank reactions and 21 sides were inspected. The Pta/Ack and acetyl-CoA-synthetase events remain outside this native route. PathBank's four-chain AtoB coefficient is explicit, while its AtoDA membership omits coefficients and does not supersede the nested EcoCyc assembly. Source-specific PGDB versions, alternative kinetic values and units, old prediction evidence, and differing AtoC HTH boundaries remain attributed rather than silently reconciled.

The historical and construct boundaries withstand review. The 1975 Methods distinguish oleate-grown wild-type E. coli B ATCC 11775 from the acetate-grown constitutive fadR16 fad-5 atoC49 thiolase-II preparation. Strong C4 preference and below-1-percent C6 activity are not asserted as universal zero activity. Native non-detection and induction statements remain conditional. The 2016 AtoB structure account is limited to its indexed abstract and complete database annotation, including the attributed BL21/K-12 sequence statement; an independently verified clone alignment is not claimed.

The four inhibitory edges preserve the complete native frames' evidence depth. The acetyl-CoA competitive-inhibition frame has no linked primary citation; concentrations and preparation details unavailable in the frames are not invented. The CoA competition target is acyl-CoA, and substrate and inhibitory contexts are distinguished. AtoC edges represent expression regulation through the atoDAEB promoter, not direct allosteric activation of purified enzymes. The complete 2007 paper supports the promoter fragments, footprint, mutagenesis, ChIP and IHF findings with their distinct strains, plasmids and controls. Failure to establish significant in-vitro phosphorylation of tagged AtoC does not become a claim that phosphorylation is unnecessary in vivo. D55G/H73L, cPHB and motility observations remain allele- and phenotype-specific.

YdiF remains a bounded alternative catalytic context. K-12 P37766 and the evidence-only O157:H7 ortholog Q8X5X6 are separate. The full 2022 main article directly supports the reverse assay: acetoacetyl-CoA plus acetate forms acetyl-CoA, using recombinant pET28a/BL21(lambdaDE3) YdiF purified by nickel affinity. The description and e046 endpoint qualifier retain enzyme amount, concentrations, pH, temperature and duration. The paper's MG1655 physiology is distinct from its recombinant expression host. These results establish neither forward acetoacetate-assimilation flux nor YdiF necessity for growth on acetoacetate. Lactyl-CoA, YiaC/CobB and PykF/lactylation experiments are not added as native pathway steps.

All individual paragraph and edge judgments are in `successor-scientific-assessments.json`. The exact 25 identity and 66 reference judgments are in `successor-identity-reference-assessments.json`; all native/UniProt/PathBank object dispositions are in `successor-source-object-assessments.json`.

## Structured expression cross-check

An ignored-inclusive bounded runner search found the local `culturebotai-claw/.venv/bin/kg-microbe-sources`; some unrelated sibling directories denied traversal, so no whole-machine absence was inferred. The initial sandbox dataset request failed at DNS resolution. Authorized public GETs then succeeded, and the required `datasets`, `search` and `summarize` calls were completed without installation.

The searched dataset is `e_coli/precise1k`; query AtoC returned `e_coli/precise1k/110`, named SCFA, with RpoN/AtoC/IHF regulator labels and acetoacetate transport/catabolism context. Its four returned in-module gene rows are:

| Scoped gene key | Gene | UniProt | Weight |
|---|---|---|---:|
| e_coli/precise1k/b2221 | atoD | P76458 | 0.406747077 |
| e_coli/precise1k/b2222 | atoA | P76459 | 0.339749429 |
| e_coli/precise1k/b2223 | atoE | P76460 | 0.281130412 |
| e_coli/precise1k/b2224 | atoB | P76461 | 0.2033287 |

This adds consistent computational expression-module context, with a source threshold of 0.143273345. It does not independently prove catalysis, reaction direction, transport necessity, exact pathway identity or species-wide behavior. It does not require adding AtoE to the two-event chemistry. Only this relevant dataset/component was assessed; no absence across other datasets is inferred. The source-native API originals, retrieval receipts and actual CLI summaries are preserved in the packet. This is a review note, not a change to the 66 draft references.

## Validation and remaining scope

Fresh exact replays passed for 803 native slots in 38 frames, 215 UniProt objects, 165 PathBank objects, 22 Rhea whole subjects aggregated across repeated original fragments, six complete ChEBI SQL subjects including the contextual residue-class cross-check, the NCBI species subject, six native structural matches, 25 selected identities, 66 reference bodies and all 18 PMID metadata selectors. All 30 PDF page texts exactly match fresh extraction. The external draft passes the pinned schema validator, exact selected-tuple comparison, all 46 edge hashes and the e046 endpoint-qualifier check.

The first intake attempt was stopped because its inherited helper read large SQL originals into memory; the successor's streaming retry passed. Development of the fresh replay helper exposed descriptor-extra-field, title-whitespace and projection-metadata comparison assumptions; these were corrected in the reviewer helper. No input mismatch or author scientific defect resulted. Execution receipts preserve these distinctions.

No full native identifier, model, KGX, corpus, history or preservation gates were run. Narrow typed authority support for the nested heteromer, acyl-transfer composite and generic protein-bound classes remains future implementation work described in the author's `AUTHORITY-REQUIREMENTS.md`. Independent acceptance of that implementation, maintained adoption and persisted native review records remain outside this external science task. This scientific pass does not waive any of those requirements.

**Required findings: none.** The stated source-access limitations and future implementation gates remain material boundaries on this verdict.

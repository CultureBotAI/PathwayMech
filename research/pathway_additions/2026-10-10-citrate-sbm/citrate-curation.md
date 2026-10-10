# Citrate lyase activation curation

Date: 2026-10-10. Base: `722257adc1882495f8454cc229b8fa0c187cf868`.
Target: `data/pathways/citrate-lyase-activation.yaml`, **MetaCyc:P2-PWY**.

This is the experimentally supported E. coli activation core: precursor synthesis by CitG, prosthetic-group transfer by CitX, and acetylation by CitC. It is a multienzyme protein-maturation pathway distinct from citrate cleavage, citrate transport, fermentation, and malonate/citramalate enzyme maturation. The three whole ACP chemical states remain separate generic proteins; they are not free serine derivatives or an asserted exact match to an E. coli sequence.

## Novelty and identity

[Duplicate searches](citrate-duplicate-searches.json) comprise 60 exact-string searches across this worktree and the original repository. They include ignored and hidden files, excluding only Git internals, the virtual environment and Python bytecode. Exact MetaCyc/PathBank pathway IDs, native member, labels/synonyms, core reactions, proteins, carrier states and primary PMID/DOI strings were searched before the target was written. No maintained-record match occurred. Prior hits were the frozen PathBank inventory and the previous batch's citrate triage/projections. Those sources and the bounded external follow-up were inspected; the prior CitC and carrier-state questions are resolved to the extent described below. This does not claim exhaustive semantic equivalence across all pathways.

The native MetaCyc pathway supplies an exact activation-route identity and explicit three-reaction membership. The inspected GO ligase/holo-ACP synthase terms describe individual activities rather than this multienzyme route. Choosing P2-PWY does not assert every branch of the multispecies source in E. coli. PathBank SMP0002087 independently represents the same activation system but contains extra unsupported forward acetylation and alternative-donor branches.

[Identifiers](citrate-identifiers.json) list every named node and reference. Seven chemicals use canonical ChEBI 255 names; all three directed Rhea 139 ontology labels match current Rhea 142 RDF equations. Reviewed UniProt identities supply K-12 taxon 83333 and exact catalytic annotations. Root integrates these independent sources into the canonical authority snapshots; the target itself is never an identity authority.

## Source-to-record coverage

| Source fact | Disposition |
|---|---|
| P2-PWY members 2.7.8.25-RXN, 2.7.7.61-RXN, CITC-RXN | Three `part_of` edges; Rhea 142 independently supplies explicit MetaCyc crosswalks for 15118, 16334, 23789. |
| Rhea 15118 precursor synthesis | Four exact side occurrences, coefficient 1; CitG catalysis. The EC-like native name is historical; current classification is 2.4.2.52. |
| Rhea 16334 prosthetic-group transfer | Four exact side occurrences, coefficient 1; CitX catalysis. Native GENERIC:10157/10158 retained as whole RHEA-COMP proteins. |
| Rhea 23789 acetylation | Six exact side occurrences, coefficient 1; CitC catalytic assignment retains its annotation/experimental limits. Native GENERIC:10158/13710 remain distinct. |
| CitG product is CitX input; CitX product is CitC input | Two direct material-transfer edges, supported by both exact reaction sides. No stable CitG–CitX complex or substrate-channeling interaction is inferred. |
| PathBank 6060/6061/6063 | Chemistry independently grounded through current Rhea. Older protonation forms and explicit extra protons are not copied. |
| PathBank apo-ACP is typed `SmallMolecule`; holo/acetyl forms are `Protein` | Apo classification rejected: native Rhea explicitly identifies all three complete states as GenericPolypeptide. No source `exactMatch` is invented. |
| PathBank 6062 ATP-free forward acetylation | Excluded. It has no catalyst and reverses the independently supported deacetylase direction; source membership is insufficient biological evidence. |
| PathBank 6064 / MetaCyc 2.3.1.49-RXN S-acetylphosphopantetheine donor | Excluded from E. coli core; native MONOMER-6581 is attributed to historical Klebsiella aerogenes, PMID:4741546. No E. coli catalyst identity was established. |
| MetaCyc deacetylase / CPLX-7662 | Excluded. Rubrivivax gelatinosus, historically Rhodopseudomonas gelatinosa; PMID:7460909 supports a two-subunit enzyme. Its identity and inhibition by glutamate are not transferred to E. coli. |
| AMP-ACP formed without physiological CitX substrate | Explicit off-pathway exclusion; no AMP-ACP intermediate or bypass edge. |
| P69330/CitD carrier and cytoplasmic annotation | Inspected as biological context. The substrate is represented by generic chemical states; no arbitrary sequence-to-state edge or duplicated substrate node. Cytoplasmic annotation of CitD does not establish a compartment for every activation activity. |
| H-NS induction comments, P77390/YaiI interaction, CitT transport | Outside the defined chemistry. Source annotations remain in the projection; no regulatory or transport edges. |

The [source projection](citrate-source-projection.json) preserves all five native PathBank reaction objects and controllers, relevant MetaCyc members/catalysts/branches, current protein comments/ECO tags, chemical identity statements, exact Rhea directions/sides and all 22 graph-edge endpoints. Native MetaCyc source direction and modern Rhea protonation are kept separate. All 14 Rhea side occurrences are retained.

## Primary evidence and its limits

- **PMID10924139**, DOI10.1021/bi000401r: full indexed abstract and selected full-text portions of the institutional primary PDF were inspected, including cloning/assay methods, whole-operon activity, purified CitG/CitX conversion, ACP peptide/mass analysis and discussion. The E. coli citCDEFXG construct yielded approximately 4.5 U/mg versus <0.01 U/mg for vector controls. This supports the system, not isolated CitC sequence-specific causality. The record cites the preserved abstract response, whose source assertion covers purified conversion and the rejected AMP-ACP intermediate. Full-text extraction hashes cover tool output, never PDF bytes. [Primary institutional source](https://juser.fz-juelich.de/record/26938/files/19821.pdf).
- **PMID11042274**, DOI10.1016/S0014-5793(00)02105-0: the complete indexed primary abstract directly identifies the CitG precursor and its CitX-dependent transfer. This resolves the earlier paper's provisional structural identification. Reviewed P77231/P0A6G5 catalytic comments explicitly cite experimental ECO:0000269. The publisher PDF returned 403; no full-body access is claimed. [Primary abstract](https://pubmed.ncbi.nlm.nih.gov/11042274/).
- **PMID6354265**, DOI10.1021/bi00289a008: the inspected primary abstract establishes E. coli ligase activity with acetate and ATP, but is truncated at 250 words. Reviewed P77390's GO:0008771 xref explicitly carries IDA:EcoCyc/ECO:0000314 with this PMID; fresh QuickGO independently confirms it. Exact EcoCyc:CITC-MONOMER XML also links P77390/CITC-RXN and attributes a native-host purified-protein evidence code to the GO assertion. That source attribution is preserved; this author did not inspect a complete primary experiment identifying purified P77390. The record states that limit and does not downgrade the evidence bridge to mere unspecified sequence similarity. [Primary abstract](https://pubmed.ncbi.nlm.nih.gov/6354265/).
- **PMID7830578**, DOI10.1111/j.1365-2958.1994.tb01295.x: complete indexed abstract inspected. It experimentally assigns **K. pneumoniae** CitC, expressed in E. coli. Native MetaCyc MONOMER-17001 is P45410/taxon 573 and cannot stand in for P77390. The host/source distinction is retained.
- **PMID3555623**, DOI10.1016/0167-4838(87)90232-9: complete indexed abstract explicitly corrects the 1983 85 kDa ACP as a contaminant. Its three-subunit 1:1:1 ratio supersedes the older 1:6:6 claim. No obsolete assembly or mass is imported.
- **PMID11948157**: complete indexed abstract inspected as Klebsiella CitX context. It is not used to assign E. coli CitC. **PMID4365579** establishes ligase activity in historical Klebsiella, with caveats on apparent acetyl-CoA donation; **PMID:7460909** supports the Rubrivivax deacetylase exclusion. **PMID:4741546** supplies primary title/metadata only; no abstract was available, so its enzymology is attributed to the inspected native curated source rather than an unseen full paper.

The literal CitX and CitC excerpts in the record are separately checked against saved abstract bodies and remain below 25 words per primary source.

## Cofactors, assemblies and experimental scope

The 2000 primary methods prepare citrate-lyase assay extracts in 50 mM potassium phosphate pH 7.0 with 1 mM MgCl2. Acetate/ATP preincubation uses 20 mM acetate and 2.7 mM ATP for 30 min at 37°C. That is a coupled lyase assay and activation condition, not direct evidence that a particular CitG/CitX/CitC protein binds Mg as an obligatory cofactor. The record therefore has no `has_cofactor` edge and makes no claim of metal independence. Purification with Ni-affinity resin or buffers containing EDTA likewise does not establish a physiological metal or its absence.

Native G6339-MONOMER/G6340-MONOMER objects have molecular-weight sequence fields but no explicit complex-component relation; current CitG/CitX reviewed entries have no SUBUNIT/COFACTOR comment. These source omissions are not proof of monomeric state. The paper's use of purified tagged proteins is not an assembly measurement. CitD's `(alpha,beta,gamma)6` UniProt comment carries ECO:0000250, and concerns the downstream citrate-lyase complex, not a combined CitG/X/C activation complex. No such assembly is asserted here.

K-12 scope follows the exact reviewed protein identities. Recombinant E. coli BL21(DE3), cloning hosts, native E. coli organism-level assays and heterologous Klebsiella complementation are distinct experimental contexts. They do not prove activation or growth in every K-12 strain. No taxon is attached through a cellular-location predicate, and no acetate/ATP-driven activation is described as an unconditional physiological flux.

## Provenance, context and validation

[Source manifest](citrate-source-manifest.json) retains 45 source inputs/attempts, retrieval timestamps, response hashes, archive/member scopes, ontology cache provenance and each record-reference/raw-body correspondence. Reused current-session bytes were independently rehashed; they are not represented as new downloads. Direct institutional PDF downloads yielded 248-byte browser-challenge HTML with HTTP 200 and were rejected. PMC134981/PMC388369 fullTextXML failed 500 and public HTML 403. Raw bodies and scripts remain external under `/private/tmp/pathwaymech-citrate-sbm-evidence/citrate`.

The parent ran the canonical iModulonDB dataset inventory and exact-locus queries b0613/citG, b0614/citX, b0618/citC: each returned one gene and zero module hits with exit 0. See `imodulondb-context.json`. No module-summary query applies to this result; zero bounded query hits are not absence from all expression modules. No catalytic, flux or regulatory assertion derives from that context.

[Validation receipt](citrate-validation.json) records the actual narrow command, script hash and frozen target hash. It checks native/closed schema, independent canonical identity queries, all 14 sides from freshly re-extracted complete Rhea RDF, symbolic-backbone elemental/charge balance, literal quotes and actual target KGX output with all evidence/reference metadata. Parent-owned canonical snapshot regeneration, full gates, generated pages and independent scientific review remain separate integration work.

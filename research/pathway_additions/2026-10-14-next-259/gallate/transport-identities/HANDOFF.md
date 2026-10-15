# Transport-assay reagent and GO identity handoff

This new external package supplies author evidence and authority requirements only. It creates no graph edges, changes no maintained or frozen file, and issues no approval verdict.

The four 2011 reagents resolve to exact issuing ChEBI records:

| Source reagent | Proposed ID | Canonical label | Formula / charge |
|---|---|---|---|
| FCCP | CHEBI:75458 | carbonyl cyanide p-trifluoromethoxyphenylhydrazone | C10H5F3N4O / 0 |
| CCCP | CHEBI:3259 | CCCP | C9H5ClN4 / 0 |
| 2,4-dinitrophenol | CHEBI:42017 | 2,4-dinitrophenol | C6H4N2O5 / 0 |
| DEPC | CHEBI:59051 | diethyl pyrocarbonate | C6H10O5 / 0 |

Use these canonical labels. FCCP is a related synonym in the pinned ontology, and DEPC is the paper's abbreviation; neither abbreviation alone is proposed as a canonical label. The FCCP current JSON label contains italic markup around p, while its ASCII label and the pinned canonical label agree exactly. Fresh current ChEBI originals and complete pinned ChEBI statements agree in formula, charge, full InChI, InChIKey and molecular connectivity. Independently encoded graphs from the reagent names also match both issuing and pinned SMILES. These are name-to-authority matches: no primary chemical drawing or reagent catalog identity was accessible or claimed for the 2011 paper.

The proposed records are the named neutral parent reagents. They do not establish the supplied salt, predominant or bound microspecies, or protonation at assay pH. CHEBI:84561, 2,4-dinitrophenol(1−), has a related synonym that could mislead a name search; it is explicitly excluded as an unsupported exact assay form. DEPC is diethyl dicarbonate, not diethyl carbonate or a modified histidine product. The hydrazone carbon in FCCP/CCCP has two equivalent cyano substituents, so no missing E/Z configuration is invented.

The actual inspected publisher transcript states 30 µM FCCP and 20 µM CCCP, with 1 mM 2,4-dinitrophenol, in the whole-cell gallate-uptake context. Its Figure2C caption identifies KTGAL(pIZGalT), 50 µM gallate, and DMSO as the FCCP vehicle. The separate publisher PDF text extraction incorrectly renders the first two concentrations as mM; this is retained as an extraction discrepancy, not a corrected primary measurement. The DEPC methods specify a 0.5 M acetonitrile stock and 0.5 mM treatment for7minutes at25°C in50mM phosphate,pH7.0. The Results transcript states15% remaining GalB hydratase activity. Histidine involvement is the authors' inference; no exact modified residue is established. All these prose findings remain research facts, not fabricated structured-source assertions.

The transport uncoupler effects support an energetic requirement in the stated whole-cell assay. They do not prove direct binding to GalT, a fixed proton transport stoichiometry, or equivalent effects on every carboxylate transporter. The DEPC experiment is a separate GalB enzyme perturbation, not a transport assay.

The source-native protein GO annotations are exact and computational:

| Protein | Issuing annotation | Aspect | Evidence label |
|---|---|---|---|
| UniProtKB:E8ZB61 | GO:0046943, carboxylic acid transmembrane transporter activity | Molecular function | IEA:TreeGrafter |
| UniProtKB:E8ZB61 | GO:0005886, plasma membrane | Cellular component | IEA:TreeGrafter |
| UniProtKB:Q88JX6 | GO:0015288, porin activity | Molecular function | IEA:InterPro |
| UniProtKB:Q88JX6 | GO:0016020, membrane | Cellular component | IEA:InterPro |

The protein originals retain their full comments and evidence codes in `protein-annotation-evidence.json`. E8ZB61's experimental function comment cites PMID21219457, but its GO assignments are IEA. Its caution about the KT2440 frameshift must remain distinct from the repaired allele used in the primary transport work. Q88JX6's probable gallate-uptake function and Opr family similarity are not purified-pore proof. A generic membrane annotation must not silently become an experimentally established outer-membrane location.

The complete pinned GO2026-07-26 search found **no gallate- or protocatechuate-specific transport activity/process term** through the documented lexical and logical search. It queried the full statements database containing48,340 named GO labels, every literal annotation for the compound names and variants, whole-token PCA aliases, and reverse anonymous-expression links from gallate/gallic acid and protocatechuate/protocatechuic acid IDs. There were159 lexical statement matches, no PCA abbreviation matches, and41 distinct candidate terms. The compound-linked terms describe metabolism/catalysis; none is a transport candidate. `projections/GO-substrate-specific-search.json` preserves all matches, candidate term statements and logical traversal arcs. This is a statement about the pinned snapshot and documented search, not all ontologies or future releases. Filesystem inventory used `rg --files --hidden --no-ignore`; the complete database content queries themselves are independent of gitignore.

Broad source-scoped options, with exact canonical labels, include:

| GO ID | Canonical label | Record category | Appropriate limit |
|---|---|---|---|
| GO:0046943 | carboxylic acid transmembrane transporter activity | molecular_activity | Exact GalT source annotation; no gallate-only identity |
| GO:0015288 | porin activity | molecular_activity | Exact GalP source annotation; no substrate-specific pore claim |
| GO:1905039 | carboxylic acid transmembrane transport | biological_process | Broad membrane-crossing process; substrate/preparation stays source-scoped |
| GO:0046942 | carboxylic acid transport | biological_process | Broad directed transport process |
| GO:0015849 | organic acid transport | biological_process | Broader alternative |
| GO:0055085 | transmembrane transport | biological_process | Broader alternative |
| GO:0022857 | transmembrane transporter activity | molecular_activity | Broader molecular-function alternative |

GO:0008028 (monocarboxylic acid transmembrane transporter activity) and GO:0015718 (monocarboxylic acid transport) are also valid chemical-class terms, but they are not direct GO assignments in the inspected GalT/GalP records. Using them requires the parent's primary scope assessment. GO:0005342 (organic acid transmembrane transporter activity) and GO:1903825 (organic acid transmembrane transport) are obsolete in the pinned source and should not be selected as current alternatives. All11 selected live QuickGO records agree with pinned label/aspect and are non-obsolete. The fresh QuickGO response is a current term snapshot, not a claim to have inspected the complete current GO release.

Keep canonical broad labels intact. A source-scoped description of a GalT-associated gallate or PCA uptake assay does not mint a dedicated substrate-specific issuing GO identifier. The parent decides how to represent assay events, activity, process, energy dependence and compartment without collapsing these categories. The parent primary ledger's repaired allele, multicopy preparation and caption/prose uptake-kinetic distinction remain controlling.

There is a direct source-grounded activity/process connection: GO:0046943 has a subclass restriction `_:riog00237193`, with `owl:onProperty BFO:0000050` (part of) and `owl:someValuesFrom GO:1905039`. Thus the broad molecular activity is explicitly part of some instance of the broad transport process. This is a class-level context axiom, not direct regulation or proof of a particular assay event. GO:1905039 is separately a subclass of GO:0046942 and GO:0055085; those subclass relations must not be relabeled part_of. The chemical restriction uses RO:0004009, whose label is “has primary input.” The inherited RO:0002342 relation to membrane means “results in transport across,” not occurs_in. Full anonymous-expression triples, relation definitions and typed Evidence are retained in `GO-activity-process-context-evidence.json` and its projection. This supplies evidence and schema guidance, not a new graph edge.

`chemical-identity-proposals.json`, `GO-authority-options.json`, `protein-annotation-evidence.json`, `identity-evidence-proposals.json` and `primary-context.json` provide the evidence. `authority-requirements.json` inventories exact selected keys in the current maintained authority snapshot; it makes no broader repository absence claim and promotes nothing. Complete ChEBI255 and GO2026-07-26 original database hashes are recorded in `pinned-original-bindings.json`, with full selected native triples retained as projections. Normal selected-term extraction and independent scientific review remain root-owned prerequisites.

All four chemical records and the11-term QuickGO response were acquired through normal public endpoints. Initial sandbox DNS failures and the successful HTTP200 retry are both retained. The original analysis completed chemical/GO projections but was interrupted during final hashing; the explicit continuation verified both full database hashes and finished the inventory. `manifest.json` binds the final external package. No new primary quotation allocation or graph edge is introduced.

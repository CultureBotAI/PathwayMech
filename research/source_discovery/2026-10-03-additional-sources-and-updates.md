# Additional pathway sources and update baseline

Checked: 2026-10-03

## Scope and decision

This is an incremental discovery scan, not an ingestion run or an exhaustive
re-audit of the source landscape. Six additional candidates are added to
`conf/sources.yaml`, all disabled. No data was added to `data/pathways/`, no
importer was implemented, and no bulk archive was downloaded.

Recommendation: investigate **BRENDA** first for pathway topology and **HADEG**
for a smaller protein-membership adapter. Both need canaries before adoption.
The remaining candidates supply useful rules or biodegradation graphs but
have stronger reuse or semantic blockers.

Deduplication included gitignored and hidden repository files, excluding Git
internals and the virtual environment. BRENDA's occurrence as a protein
annotation alias in the GapMind code is not a BRENDA pathway importer.
These six candidates were not rows in the 24-source inventory at the start of
this scan. Existing caches were not exhaustively re-ingested or reconciled.

The [September cached-record triage](current_open_source_ingest_triage.md)
only rejected further records from the inspected SGD GO-CAM and September 10
WikiPathways caches. It is not evidence that no additional sources exist.
This report extends the [landscape memo](microbial_pathway_sources.md) and its
historical recommendations without changing existing source enablement.

## Ranked additions

Ranks here apply to these new candidates; existing inventory priorities are
preserved. All six lack an implemented PathwayMech ingestion path.

| Rank | Source | Biological element identifiers | Intended contribution | Main blocker | Inventory status |
| --- | --- | --- | --- | --- | --- |
| 1 | BRENDA | EC; native ligand/reaction IDs; UniProt and NCBI taxon links described in its paper | Pathway/enzyme reference, possibly directed topology | Verify export edges and taxon/evidence links; download requires license acceptance | `next`, disabled |
| 2 | HADEG | Mixed UniProt-like, versioned protein accessions, and local IDs | Degradation pathway-to-protein membership | Resolve mixed namespaces, organism/evidence joins, and data-license scope | `next`, disabled |
| 3 | enviPath | Native pathway, reaction, and compound URIs; chemical structures | Xenobiotic biotransformation graphs | Current extraction/redistribution restrictions, registration, legacy migration | `license-gated`, disabled |
| 4 | DRAM | KEGG module, KO, reaction, compound; EC | Structured metabolic module-step support | KEGG-derived data terms and branch/version choice | `license-gated`, disabled |
| 5 | DiTing | KOs attached to named pathway formulas | Biogeochemical abundance-rule support | Not ordered topology; derived-data terms and overlap | `deferred`, disabled |
| 6 | METABOLIC | KOs/HMM names; module-template structure needs inspection | Microbial trait/module support | Data reuse terms not established; inspect packaged templates | `license-gated`, disabled |

These are role assessments, not claims that all pathway elements already have
accepted PathwayMech CURIEs. The sampled resources do not fill every fungal,
algal, archaeal, or protist coverage gap.

## Candidate evidence

### BRENDA

The live download page advertises release **2026.1 (March 2026)**, JSON schema
2.0.0, text/JSON archives, and CC BY 4.0 data with an explicit acceptance step.
That is an access step, not a finding that the data is noncommercial-only.
[Download and license](https://brenda-enzymes.org/download.php),
[schema documentation](https://brenda-enzymes.org/schemas/docs/2.0.0/brenda.schema.html).

The 2026 database paper describes 195 maps at publication, downloadable pathway
component tables, and a prototype RDF graph. It describes EC, UniProt, taxon,
and ligand structure identifiers. This is a paper-reported snapshot, not a
current count measured here.
[BRENDA 2026 paper](https://doi.org/10.1093/nar/gkaf1113).

The inspected Entner-Doudoroff page has native ID
`pw_Entner-Doudoroff-pathway`, enzyme/compound/interpathway sections, and
reaction/ligand and NCBI-taxonomy search controls. Its default export is SVG;
the text retrieval did not expose the dynamic component tables.
[Pathway page](https://brenda-enzymes.org/pathway.php?pathway=Entner+Doudoroff+pathway).

**Canary:** recover one small directed route from that pathway, preserve native
IDs, and test enzyme/compound joins to accepted prefixes plus organism and
reference provenance. Do not substitute the enzyme-centric bulk JSON for a
verified pathway graph. The linked [SPARQL service](https://sparql.dsmz.de/brenda/)
timed out and the linked SBML page failed text decoding in this scan; neither
was demonstrated as a functioning pathway-export endpoint.

### HADEG

The authors provide manually curated, experimentally validated degradation and
biosurfactant proteins, pathway tables, and a GPL-3.0 repository. Their README
distinguishes the September 2023 paper dataset from a November 2023 update.
[Repository](https://github.com/jarojasva/HADEG),
[paper](https://doi.org/10.1016/j.compbiolchem.2023.107966),
[pinned license](https://github.com/jarojasva/HADEG/blob/8f1ff8fb3b6452a0fd2667dc78686dced5cd4416/LICENSE).

The inspected CSV connects mechanism, compound category, pathway, subpathway,
protein, and gene labels. Examples include `P12693`, `BAB33284.1`, and local
`GOM1`. It has no reaction-order field. The Finnerty pathway contains both
UniProt-like and versioned protein accessions; do not prefix the entire protein
column as UniProtKB.
[Pinned membership CSV](https://raw.githubusercontent.com/jarojasva/HADEG/8f1ff8fb3b6452a0fd2667dc78686dced5cd4416/Tables/7_All_pathways.csv).

**Canary:** one Finnerty-pathway membership group with explicit identifier
resolution, native subpathway code, and retained unresolved IDs. Check the
associated XLSX evidence tables and original publications for organism and
reference joins. Confirm the repository license's scope over those tables
before redistributing data; do not silently relicense GPL material. This is a
support adapter, not sufficient evidence for ordered mechanistic edges.

### enviPath / EAWAG-BBD

enviPath is the successor lineage to UM-BBD/PPS, not a separate source to count
again for each legacy name. Its documentation defines native pathway/package
URIs and JSON/CSV access; the original paper describes reaction and compound
objects suitable for biodegradation graphs.
[API documentation](https://wiki.envipath.org/doku.php?id=pathway),
[original paper](https://doi.org/10.1093/nar/gkv1229).

The new portal requires registration and points to a legacy system that will
eventually close. The 2024 paper reports CC BY-NC-SA 4.0 datasets, but the
current January 2026 terms restrict substantial extraction/redistribution and
uses involving competing databases without permission. Treat historical data
licenses and current service terms separately; no account or data extraction
was attempted.
[Current portal](https://envipath.org/login/),
[current terms, sections 4, 5 and 8](https://envipath.org/terms),
[2024 paper](https://doi.org/10.1186/s13321-024-00881-6).

**Canary after permission:** one reviewed EAWAG-BBD pathway preserving pathway,
compound and reaction URIs, structure mappings, and experimental-versus-predicted
provenance. Confirm package-specific rights and legacy/current ID continuity.
Reviewed chemical transformations do not guarantee an enzyme identifier for
every edge or a strain-specific experimental observation.

### DRAM

The original WrightonLabCSU repository now resolves to BortonWrightonLabs. Its
default `dev` branch is DRAM2 development; DRAM1 remains on `master`. The
repository license is GPL-3.0, which alone does not settle reuse of imported
database definitions.
[Repository](https://github.com/BortonWrightonLabs/DRAM),
[DRAM1 license](https://github.com/BortonWrightonLabs/DRAM/blob/fe61d759303f30db058d5d505c448b28e41b03f1/LICENSE).

The inspected DRAM1 `data/module_step_form.tsv` supplies module names, KOs,
gene descriptions, path coordinates, and substrate/product identifiers. A
glycolysis row uses `M00001`, `K00844`, `R01786`, `C00267`, and `C00668`.
[Pinned step table](https://raw.githubusercontent.com/BortonWrightonLabs/DRAM/fe61d759303f30db058d5d505c448b28e41b03f1/data/module_step_form.tsv).

**Canary after rights review:** module M00001 with alternate steps retained,
KO/EC/reaction/compound namespaces separated, and source lineage marked KEGG.
Do not flatten alternatives into one reaction chain or infer experimental
taxon evidence from a rule template. This is support data, not an independent
curated topology source; KEGG-derived content needs its own reuse decision.

### DiTing

The original repository directs readers to the maintained SilentGene v2
implementation. The GPL-3.0 repository includes explicit abundance formulas
for biogeochemical functions.
[Original project](https://github.com/xuechunxu/DiTing),
[maintained project](https://github.com/SilentGene/DiTing),
[paper](https://doi.org/10.3389/fmicb.2021.698286).

The inspected `pathway_formula_diting.txt` connects named functions to KOs;
Photosystem II, for example, averages six KO abundances including `K02703`.
These arithmetic formulas are neither reaction order nor automatically Boolean
completeness definitions. Canonical pathway IDs are not established by these
local labels.
[Pinned formulas](https://raw.githubusercontent.com/SilentGene/DiTing/a1542ccaeef7c2ca92c58407f9fc68ea6072e7b4/pathway_formula_diting.txt).

**Canary:** retain one formula as a provenance-bearing support rule, never as
causal edges. Check derived KEGG data terms before copying formulas and compare
novel coverage with GapMind/DRAM before adding another overlapping adapter.

### METABOLIC

The repository exposes a v4.0 tool, a KO/HMM identifier list and
`METABOLIC_template_and_database.tgz`. Its metabolic and biogeochemical trait
focus makes the templates worth inspecting, not the genome pipeline itself.
[Repository](https://github.com/AnantharamanLab/METABOLIC),
[paper](https://doi.org/10.1186/s40168-021-01213-8),
[pinned template archive entry](https://github.com/AnantharamanLab/METABOLIC/blob/97236332519180f1d76a242dedb0aaa8191fdbb3/METABOLIC_template_and_database.tgz).

The inspected KO list includes names such as `K15756.hmm`. The archive was not
extracted, so its internal module fields and topology are **unverified**.
GitHub license metadata was null and the recursive tracked tree did not expose
a license-named file. This establishes an unresolved license question, not a
claim that no terms exist elsewhere; do not borrow a wrapper/container license.
[Pinned KO list](https://github.com/AnantharamanLab/METABOLIC/blob/97236332519180f1d76a242dedb0aaa8191fdbb3/All_Module_KO_ids.txt).

**Canary after clarification:** inspect one C/N/S module definition, preserve
its KO/HMM semantics, and determine whether it contributes beyond existing
rulebases. Neither public availability nor a paper's license establishes the
archive's redistribution terms.

## Related resource not added independently

**CyanoCyc** is a valuable cyanobacterial coverage lead within the BioCyc/Pathway
Tools lineage. Its paper distinguishes curated databases from predicted PGDBs.
It should be tracked as a BioCyc acquisition target, not independent duplicate
topology. The public paper's license does not establish PGDB export rights;
check the exact database and retain organism/database-scoped identifiers.
[CyanoCyc paper](https://doi.org/10.3389/fmicb.2024.1340413),
[BioCyc licensing](https://bioinformatics.ai.sri.com/ptools/licensing/all-reg.shtml).

The direct CyanoCyc portal fetch failed in this scan. This is not evidence of
retirement. MetaNetX, BioModels, Pathway Commons and KBase were already discussed
in the landscape memo and are not reported as newly discovered resources.

## Repeatable update baseline

The following are **observed upstream** states, not installed-data versions.
Full commit SHAs pin the inspected repository trees; they do not establish when
each biological definition last changed. No prior comparable baseline was
found in the reviewed source-discovery notes for these new candidates.

| Source | Observed artifact/revision | Next comparison |
| --- | --- | --- |
| BRENDA | Download page: 2026.1; JSON schema 2.0.0 | Release label, schema, pathway component export, license |
| HADEG | `main` at `8f1ff8fb3b6452a0fd2667dc78686dced5cd4416` (2024-05-10); CSV linked above | CSV and evidence-table blobs, not README-only changes |
| enviPath | New login portal, legacy migration notice; terms version 1, January 2026; dataset release unknown | Current rights, package metadata and ID migration after authorization |
| DRAM1 | `master` at `fe61d759303f30db058d5d505c448b28e41b03f1` (2025-05-15); step-table blob `8cc5188287de0d487302714b2108cb4ead1f2024` | Step-table blob/schema; track DRAM2 separately |
| DiTing v2 | `master` at `a1542ccaeef7c2ca92c58407f9fc68ea6072e7b4` (2026-03-31); formula file linked above | Formula content and project migration |
| METABOLIC | `master` at `97236332519180f1d76a242dedb0aaa8191fdbb3` (2025-01-27); template blob `a8c53d9f4f7fce5ed8e893a40bd76452fe4e27d1` | License clarification and template archive bytes/schema |

Repository revisions/dates were observed through GitHub's commit/tree APIs;
the pinned file links above identify the corresponding evidence. These are
first baselines, not proof of new releases since the last ingestion.

### Existing-source spot checks

| Source | Observed upstream | Comparison and local ingestion state | Next action |
| --- | --- | --- | --- |
| WikiPathways | [Current GPML listing](https://data.wikipathways.org/current/gpml/) still names September 10, 2026 archives | Same listed release as the September 30 cached-record review; bytes were not rehashed, so not a claim of identical files | Recheck after a new release or mapping change; do not rerun unchanged rejected candidates blindly |
| GO-CAM | [Download documentation](https://geneontology.org/docs/download-go-cams/) recommends JSON and deprecates TTL | Existing JSON importer is aligned; no new model-version delta measured | Compare relevant organism/model JSON snapshots against local provenance |
| GapMind | [`gaps` history](https://github.com/morgannprice/PaperBLAST/commits/master/gaps) latest observed commit `36d3d70df8988de2265cc77cf2f5e48239b1b993` (2026-06-12) is a documentation update; [`thr.steps` history](https://github.com/morgannprice/PaperBLAST/commits/master/gaps/aa/thr.steps) points to `d5821e1780d9d81b7a063e4223cc1e074669b9eb` (2026-03-04) | Support importer exists; locally ingested upstream revision was not established in this scan | Compare all relevant `.steps` files, not the repository timestamp |
| UniPathway | [`upa.obo` history](https://github.com/geneontology/unipathway/commits/master/upa.obo) latest observed commit `2094080b928bd0af5346e37a4f0071c687bba7e2` (2024-03-07), described as regeneration | Support importer exists; biological change and local upstream revision not established | Compare OBO content before treating regeneration as a data update |
| MIBiG | [Download page](https://mibig.secondarymetabolites.org/download) yielded no usable release listing; homepage request timed out | Current release **unverified**; existing enabled status unchanged | Retry a documented release endpoint; do not infer latest version from indexed example records |

The other 19 previously inventoried sources were not re-audited for releases in
this incremental scan. No evidence here establishes that all enabled importers
contain the latest complete upstream corpora.

## Next actions

1. BRENDA: resolve one pathway component export and demonstrate directed edges,
   native-to-CURIE joins, organism scope and references before building a parser.
2. HADEG: resolve Finnerty-pathway protein namespaces and supporting evidence
   tables; decide data-license handling, then implement a support-only adapter.
3. enviPath: clarify redistribution permission for the intended package before
   any extraction; track the new/legacy migration.
4. DRAM, DiTing and METABOLIC: clear derived-data terms and measure distinct
   coverage before implementing overlapping rule importers.

Repeat this workflow with
`.claude/skills/pathwaymech-discover-sources/SKILL.md`. It preserves successful
baselines and distinguishes new candidates, first observations, verified data
changes, unchanged compared artifacts, and unverified checks.

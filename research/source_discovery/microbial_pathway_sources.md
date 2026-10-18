# Microbial pathway source discovery

Updated: 2026-10-17

The [October 3 discovery scan](2026-10-03-additional-sources-and-updates.md)
introduced BRENDA, HADEG, enviPath, DRAM, DiTing and METABOLIC. Subsequent
bounded ingestion adds [HADEG membership support](2026-10-08-hadeg-pmn-canaries.md)
and [BRENDA reaction-role support](2026-10-08-brenda-context.md). The later
[DRAM and SEED ingestion batch](2026-10-08-dram-seed-ingestion.md) adds native
module-step and subsystem support; enviPath, DiTing and METABOLIC remain disabled. [PathBank and dbCAN-PUL rights](2026-10-08-pathbank-dbcan-rights.md)
were rechecked separately. The recommendations below retain their historical
landscape context; current enablement is in `conf/sources.yaml`.
The [BRENDA/violacein ingestion follow-up](2026-10-08-brenda-violacein-ingestion.md)
records the support adapter, one new maintained cluster, and their evidence limits.
The subsequent [local data ingestion batch](2026-10-08-local-data-ingestion.md)
acquires and parses PathBank and dbCAN-PUL source data, with public-release
licensing tracked separately from local processing.
The October 17 landscape refresh reconciles this note with the 268 maintained
records in `data/pathways/` (`MetaCyc`: 139, `gomodel`: 86, `WikiPathways`: 12,
`GO`: 10, `PathBank`: 9, `Reactome`: 6, `MIBiG`: 3, `KEGG`: 3), the 21 live
identifier authority namespaces in `conf/identifier_policy.yaml`, October 2026
upstream release baselines (including the `20261010` WikiPathways GPML release,
GO-CAM 2026 NAR release updates, and Reactome V94+ BioPAX Level 3 standard),
normalized fungal/algal/protist/archaeal slice mappings, and three new deferred
specialist candidates (`gutsmash`, `m-csa`, and `vmh-agora2`).

This memo ranks resources that could feed PathwayMech with pathway definitions,
reaction definitions, organism-specific pathway calls, or crosswalks. The local
schema accepts only whitelisted source and grounding CURIEs, so several
resources below would need new prefixes before their native identifiers can be
stored in curated YAML.

## Shortlist

| Tier | Source | Best import target | Access | Reuse risk |
| --- | --- | --- | --- | --- |
| 0 | MetaCyc / BioCyc | Curated metabolic pathway definitions with reaction order, reactions, compounds, enzymes, taxa, and review text (139 maintained records) | BioCyc flat files, bounded `getxml` endpoints, or web services after license registration | Medium: BioCyc Limited Databases can be used and modified but not redistributed |
| 0 | KEGG PATHWAY / MODULE | High-coverage maps and KO/module signatures for microbial metabolism (3 maintained module records) | Academic REST flatfiles or KGML; full weekly FTP requires a subscription | High: not public; non-academic use requires a license |
| 0 | Rhea | Canonical ChEBI-grounded biochemical reactions and EC/UniProt/GO cross-references | Free FTP in RDF, BioPAX 3, RXN/RD, and TSV; SPARQL endpoint | Low: CC BY 4.0 |
| 0 | GO and GO-CAM | GO process grounding (10 `GO:*` records) and causal activity models (`gomodel:*`, 86 records including YeastPathways and SYN_GO) | OBO/OWL/JSON ontology releases and GO-CAM JSON downloads/API | Low: GO data products are CC BY 4.0 |
| 1 | WikiPathways | Community-curated pathway graphs in GPML/RDF (`20261010` release; 12 maintained microbial records) | Monthly GPML, GMT, SVG, and RDF archives | Low: data-release repository is CC0 |
| 1 | MIBiG | Experimentally characterized biosynthetic gene clusters and their products (3 maintained BGC records) | JSON records and GBK sequences (v4.0) | Low: CC BY 4.0 |
| 1 | Reactome | Detailed BioPAX Level 3/SBML reaction graphs for microbial species such as *M. tuberculosis* (6 maintained records) | BioPAX 3, all-species SBML, tabular mappings, GraphDB, Content Service | Low to medium: annotation files are CC0; database dumps and diagrams are CC BY 4.0 |
| 1 | PathBank | Model-organism BioPAX/SBML/PWML pathway records with verified `SMP*` IDs (9 maintained *E. coli* records) | Primary BioPAX/SBML/PWML zip archives and metabolite/protein CSVs | Medium: CC BY-NC 4.0 on downloads page; public-release redistribution requires noncommercial/permission review |
| 2 | ModelSEED Biochemistry | ModelSEED reaction/compound namespace, aliases to KEGG/MetaCyc/Rhea/BiGG, and modeling-tested microbial reaction definitions | GitHub TSV/JSON plus ModelSEED web/API | Medium: released as CC BY, but records derived from KEGG and MetaCyc inherit source licenses |
| 2 | BiGG Models | Published organism-scale microbial metabolic networks in SBML/JSON, with subsystem labels and universal reaction/metabolite API | Web API and model downloads | Medium: free for noncommercial research only |
| 2 | BV-BRC Pathways and Subsystems | Genome-specific pathway presence calls, EC membership, and SEED functional-role subsystems across public bacterial and archaeal genomes | BV-BRC API and Comparative Systems TSV/JSON outputs | Medium to high: KEGG-derived maps and service-specific data |
| 2 | Plant Metabolic Network / ChlamyCyc | Pathway Tools pathway/genome databases for green algae, including *Chlamydomonas*-specific pathways | Local free-license Pathway Tools flat files | Low to medium: free PMN license, but download requires a license request and staff-issued credentials |
| 2 | VEuPathDB metabolic pathways | KEGG/MetaCyc pathway membership over fungal and protist gene records (FungiDB, PlasmoDB, TriTrypDB, ToxoDB, CryptoDB, GiardiaDB) | Local WDK `MetabolicPathways` TSV exports from component sites | Medium: useful organism evidence, but the pathway topology comes from KEGG/MetaCyc |
| 2 | GapMind | Curated bacterial and archaeal amino-acid biosynthesis and small-carbon catabolism enzyme-step rules | PaperBLAST GitHub `gaps/aa` and `gaps/carbon` files | Medium: GPL-3.0 source; local rule IDs are support-only seed rows |
| 2 | UniPathway | Legacy `UPA`/`UCR`/`UER` pathway and reaction hierarchy cross-referenced to Rhea, MetaCyc, KEGG, GO, EC, and ChEBI | GO-hosted `upa.obo` archive | Low: CC-BY 4.0 in `src/metadata/upa.md`, but retired upstream |
| 2 | dbCAN-PUL | Experimentally characterized prokaryotic polysaccharide utilization loci (`PUL####`) with substrate and CAZyme/EC metadata | Local workbook (`dbcan-pul`) support adapter | Medium: website exposes no explicit open redistribution license for bulk derivatives |
| 2 | SEED / PubSEED Subsystems | Curated subsystem functional roles, positional role tables, and genome variant calls | PubSEED network API JSON/TSV bundles | Medium: legacy API without explicit open data license header |
| 2 | BRENDA | Enzyme-catalyzed reaction-role and organism-scoped pathway context assertions | Official RDF/TTL download (`CC BY 4.0`) and web reaction-role support adapter | Low to medium: official download is CC BY 4.0, but rows are reaction-centric rather than causal pathway graphs |
| 2 | HADEG | Hydrocarbon aerobic and anaerobic microbial degradation pathway-gene membership rules | GitHub CSV tables and local membership adapter | Medium: GPL-3.0 repository; lexical gene/pathway rows without reaction stoichiometry |
| 2 | DRAM | Distilled and Refined Annotation of Metabolism module-step rules and KO/EC path coordinates | GitHub TSV tables (`DRAM1`) and local module-step adapter | Medium: GPL-3.0 code with KEGG-derived module coordinates |

## Canonical endpoints

| Source | Data endpoint | License or access page |
| --- | --- | --- |
| MetaCyc / BioCyc | https://pathwaytools.org/flatfile-format.html | https://bioinformatics.ai.sri.com/ptools/licensing/all-reg.shtml |
| KEGG | https://www.kegg.jp/kegg/rest/ | https://www.genome.jp/kegg/download/ |
| Rhea | https://www.rhea-db.org/help/download | https://www.rhea-db.org/help/license-disclaimer |
| GO-CAM | https://geneontology.org/docs/download-go-cams/ | https://geneontology.org/docs/go-citation-policy/ |
| GO ontology | https://geneontology.org/docs/download-ontology/ | https://geneontology.org/docs/go-citation-policy/ |
| WikiPathways | https://data.wikipathways.org/current/ | https://github.com/wikipathways/wikipathways-data-release |
| MIBiG | https://mibig.secondarymetabolites.org/download | https://mibig.secondarymetabolites.org/ |
| Reactome | https://reactome.org/download-data | https://reactome.org/license |
| PathBank | https://pathbank.org/downloads | https://pathbank.org/about |
| ModelSEED | https://github.com/ModelSEED/ModelSEEDDatabase | https://github.com/ModelSEED/ModelSEEDDatabase |
| BiGG | https://bigg.ucsd.edu/data_access | https://bigg.ucsd.edu/license |
| BV-BRC | https://www.bv-brc.org/api/doc/pathway | https://www.bv-brc.org/docs/quick_references/services/comparative_systems.html |
| Plant Metabolic Network / ChlamyCyc | https://plantcyc.org/downloads/ | https://plantcyc.org/?webform=license-agreement |
| VEuPathDB | https://veupathdb.org/service-api.html | https://veupathdb.org/veupathdb/app/static-content/about.html |
| GapMind | https://github.com/morgannprice/PaperBLAST/tree/master/gaps | https://github.com/morgannprice/PaperBLAST/blob/master/LICENSE |
| UniPathway | https://github.com/geneontology/unipathway | https://github.com/geneontology/unipathway/blob/master/src/metadata/upa.md |
| dbCAN-PUL | https://pro.unl.edu/dbCAN_PUL/dbCAN_PUL/home | https://pro.unl.edu/dbCAN_PUL/dbCAN_PUL/home |
| PANTHER Pathway | https://archive.pantherdb.org/downloads/index.jsp | https://pantherdb.org/ |
| PULDB | https://www.cazymodo.org/PULDB/ | https://www.cazymodo.org/PULDB/ |
| SEED / PubSEED Subsystems | https://blog.theseed.org/servers/2010/08/downloading-a-subsystem.html | https://www.theseed.org/ |
| MicroScope / MicroCyc | https://microscope.readthedocs.io/en/latest/ | https://mage.genoscope.cns.fr/ |
| IMG-ABC | https://img.jgi.doe.gov/help.html | https://portal-web-1.jgi.doe.gov/portal/help/download.jsf |
| E. coli Metabolome Database | https://ecmdb.ca/pathways | https://ecmdb.ca/downloads |
| AlgaePath | https://algaepath.itps.ncku.edu.tw/ | https://algaepath.itps.ncku.edu.tw/ |
| BRENDA | https://www.brenda-enzymes.org/download.php | https://www.brenda-enzymes.org/download.php |
| HADEG | https://github.com/jarojasva/HADEG | https://github.com/jarojasva/HADEG/blob/master/LICENSE |
| enviPath | https://envipath.org/ | https://envipath.org/ |
| DRAM | https://github.com/BortonWrightonLabs/DRAM | https://github.com/BortonWrightonLabs/DRAM/blob/master/LICENSE |
| DiTing | https://github.com/SilentGene/DiTing | https://github.com/SilentGene/DiTing/blob/master/LICENSE |
| METABOLIC | https://github.com/AnantharamanLab/METABOLIC | https://github.com/AnantharamanLab/METABOLIC/blob/master/LICENSE |
| gutSMASH | https://gutsmash.bioinformatics.nl/ | https://github.com/victoriapascal/gutsmash/blob/master/LICENSE |
| M-CSA | https://www.ebi.ac.uk/thornton-srv/m-csa/download/ | https://www.ebi.ac.uk/thornton-srv/m-csa/about/ |
| VMH / AGORA2 | https://www.vmh.life/ | https://github.com/ThieleLab/modelCreation/blob/main/LICENSE |

## Tier 0: already configured and worth keeping

### MetaCyc / BioCyc

MetaCyc is still the best source for manually curated microbial metabolic
pathway definitions: it has stable pathway and reaction IDs, reaction ordering,
compounds, EC numbers, enzymes, taxa, citations, and minireviews. Pathway Tools
exports every BioCyc Pathway/Genome Database as flat files such as
`pathways.dat`, `reactions.dat`, `compounds.dat`, `enzrxns.dat`, `proteins.dat`,
and `pubs.dat`, and the same page points to BioCyc web services as an alternate
access path. In PathwayMech's current corpus, `MetaCyc` anchors 139 maintained
bacterial, fungal, and archaeal pathway records (including hydrogenotrophic and
aceticlastic methanogenesis `METHANOGENESIS-PWY` and `METH-ACETATE-PWY`), with
authority validation backed by bounded Pathway Tools XML endpoints
(`metacyc-artsymbiocyc-xml` and `metacyc-sgd-pathway-xml`).

The catch is licensing. The 2026 BioCyc flat-file agreement classifies only
EcoCyc and the *Faecalibacterium prausnitzii* A2-165 PGDB as "Open Databases";
the other BioCyc PGDBs are "Limited Databases" that can be used and modified
worldwide without royalties but cannot be redistributed. Use MetaCyc IDs freely
as cross-references, but get a legal read before publishing any generated YAML
that mechanically copies pathway membership, descriptions, or comments.

### KEGG PATHWAY and KEGG MODULE

KEGG remains an essential external reference because it covers microbial
metabolic maps, module completeness rules, reactions, compounds, orthology
groups, and organism-specific gene calls. The REST API can return KGML for
pathway entries and flatfiles for module/reaction/compound entries
(`kegg-pathway-rest`, `kegg-module-rest`, `kegg-reaction-rest`,
`kegg-compound-rest`). KEGG MODULE definitions currently anchor 3 maintained
records in `data/pathways/` (`KEGG:M00008` Entner-Doudoroff, `KEGG:M00373`
ethylmalonyl-CoA, and `KEGG:M00374` archaeal dicarboxylate-hydroxybutyrate
cycle).

The import should be ID-first and license-aware. KEGG's REST service is made
available only for academic users, the full FTP is a paid academic subscription,
and non-academic use requires a commercial license. PathwayMech can keep KEGG
as a grounding source, but a bulk open-data importer should not redistribute
raw KGML maps or generated maps unless the project has explicit permission.

### Rhea

Rhea is not a pathway database, but it is the cleanest reaction backbone for
PathwayMech. Reactions are expert-curated, reaction participants are ChEBI IDs
(or `RHEA-COMP` polymer accessions resolved via `rhea-polymer-rdf`),
cross-references connect to EC, UniProtKB, and GO, and the whole release can be
downloaded from FTP in RDF, BioPAX level 3, RXN/RD, and TSV formats. Keep Rhea
enabled for the reaction layer and prefer `RHEA` reaction IDs over local
reaction IDs whenever a source pathway can be mapped unambiguously.

### GO and GO-CAM

GO has two complementary roles. First, GO biological-process terms are stable
pathway/process anchors (10 maintained `GO:*` pathway records), with OBO, OWL,
and OBO Graph JSON downloads plus separate computed taxon constraints. Second,
GO-CAMs connect GO molecular activities into qualitative causal models and are
downloadable in a LinkML-defined JSON format (86 maintained `gomodel:*` records
spanning bacterial `SYN_GO_*` and fungal `YeastPathways_*` models). Upstream
GO-CAM documentation (updated `2026-10-15`) now cites the 2026 NAR release paper
(`10.1093/nar/gkaf1292`), and model-organism fungal GO-CAMs curated by SGD and
PomBase (*Schizosaccharomyces pombe*) normalize directly under `go-cam` without
requiring separate source entries.

## Tier 1: active open ingests with narrow remaining headroom

### WikiPathways

WikiPathways is the easiest permissive pathway-graph source to parse visually.
The official monthly release archive at `data.wikipathways.org` exposes GPML,
GMT, SVG, and RDF bundles (updated to the October 10, 2026 `20261010` release),
and its data-release repository is CC0. GPML stores pathway diagrams with data
nodes and interactions, while RDF exposes the same curated pathway content as
linked data. PathwayMech currently maintains 12 microbial records from
WikiPathways (`WP71`, `WP171`, `WP178`, `WP266`, `WP287`, `WP296`, `WP392`,
`WP478`, `WP556`, `WP5019`, `WP5060`, and `WP5587`).

The main limitation is coverage and curation depth for microbes: many
WikiPathways records are mammalian, plant, or disease focused. Treat it as a
format and parser target first, then whitelist microbial species and microbial
processes rather than bulk-ingesting every organism.

### MIBiG

MIBiG is the best open source for microbial specialized metabolism where the
"pathway" is an experimentally characterized biosynthetic gene cluster rather
than a small-molecule reaction chain. Records are available as JSON, BGC
sequences are available as GBK, and current MIBiG 4.0 releases are CC BY 4.0.
PathwayMech currently maintains 3 curated BGC records (`MIBiG:BGC0002072`
linearmycin, `MIBiG:BGC0000852` *Sporosarcina pasteurii* ectoine, and
`MIBiG:BGC0000829` *Chromobacterium violaceum* violacein).

The mapping into PathwayMech is intentionally BGC-shaped: MIBiG knows loci,
genes, product chemistry, biosynthetic class, and evidence, but generally does
not enumerate every Rhea-like elementary reaction. Use it for
secondary-metabolite records with products, clusters, tailoring enzymes, and
PubMed-backed BGC publications, and keep antiSMASH DB predictions downstream
from MIBiG rather than using predictions as primary curated evidence.

### Reactome

Reactome is a high-quality graph source with BioPAX Level 3 and all-species SBML
downloads, reaction-to-PubMed tables, ChEBI/UniProt mappings, a GraphDB export,
and a Content Service (note: Reactome retired BioPAX Level 2 and Protégé 2.0
exports as of V94 and updated its Functional Interactions archive to Version
2026). The active BioPAX importer exercises Reactome stable pathway and reaction
IDs, ChEBI metabolites, UniProtKB catalysts, NCBITaxon organisms, and
reaction-local PMIDs across 6 maintained *Mycobacterium tuberculosis* records
(`R-MTU-868688`, `R-MTU-879299`, `R-MTU-879325`, `R-MTU-936635`, `R-MTU-936654`,
and `R-MTU-936721`).

Do not over-rank Reactome for broad bacteria. Its deepest curation is human;
it contains some microbial pages such as *Mycobacterium tuberculosis* and
*Escherichia coli*, and it infers pathways to selected eukaryotic model
organisms such as yeasts and *Plasmodium*, but it is not a comprehensive
prokaryotic source. Import only species whose source evidence is curated enough
to support the record.

### PathBank

PathBank provides model-organism metabolic and signaling pathways in BioPAX,
SBML, PWML, and SBGN archives along with metabolite (ChEBI/KEGG) and protein
(UniProt) CSV mappings. In `conf/sources.yaml`, `pathbank` (`priority: 60`) is
enabled as an `active` source with 9 maintained *Escherichia coli* `PathBank:SMP*`
records (`SMP0002038`, `SMP0002051`, `SMP0002067`, `SMP0002077`, `SMP0002083`,
`SMP0002089`, `SMP0002097`, `SMP0002123`, and `SMP0002406`) validated through the
`pathbank-biopax` and `pathbank-biopax-zip` authority profiles.

PathBank's downloads page specifies CC BY-NC 4.0 while its About page combines
Open Database License language with commercial redistribution restrictions.
Local BioPAX parsing and hand-reviewed literature-backed curation proceed under
explicit provenance tracking, while bulk public redistribution of raw PathBank
archives remains gated on license review.

## Tier 2: useful, but not primary pathway definitions

### ModelSEED Biochemistry

ModelSEED is valuable as a modeling-oriented reaction and compound namespace for
microbial genome-scale reconstructions. Its GitHub database has canonical TSV
and JSON files for compounds and reactions, and reaction rows include equations,
stoichiometry, reversibility, EC numbers, aliases, and external reaction IDs.
That makes it an excellent crosswalk between ModelSEED reactions, KEGG,
MetaCyc, BiGG, and Rhea.

The repository is weaker for pathway definitions themselves: its own
`Biochemistry/README.md` says the Pathways directory was intended for
subsystems and external sources but had not yet begun to be maintained. Use
ModelSEED to normalize reaction strings and aliases after a pathway has been
seeded from another source.

### BiGG Models

BiGG provides published genome-scale models with standardized BiGG reaction and
metabolite IDs, SBML/JSON/MAT downloads, a web API (`bigg-universal-metabolite-json`
and `bigg-universal-reaction-json` authority profiles), and subsystem labels on
model reactions. It is good evidence that a reaction participates in the
metabolic model of a specific bacterium, archaeon, or microalga.

Two details keep it out of tier 1: BiGG subsystems are not curated pathway
definitions, and the UCSD license is free for educational, research, and
non-profit use but requires commercial users to contact UCSD. Use it as
organism-specific supporting evidence, not as a canonical pathway authority.

### BV-BRC Pathways and Subsystems

BV-BRC is useful for bacterial and archaeal taxon triage. Its `pathway` API rows
connect a genome, gene, EC number, pathway ID, pathway name, and pathway class,
and its `subsystem` rows connect genomes and genes to SEED roles and subsystem
IDs. The Comparative Systems service can also export pathway and subsystem
TSV/JSON files for selected genome sets.

Those rows are membership calls, not pathway definitions. BV-BRC pathway maps
are represented with KEGG, and the service folds in PATRIC/RASTtk calls, so it
is a good way to find organisms and EC steps for a candidate pathway but should
not be treated as the independent source of pathway topology.

### Plant Metabolic Network / ChlamyCyc

The Plant Metabolic Network fills the clearest algal gap. PMN publishes
Pathway Tools pathway/genome databases for plants and green algae, and
`ChlamyCyc` is a current *Chlamydomonas reinhardtii* database rather than only a
historical web portal. PMN downloads require a free license request and include
the native Ocelot representation, BioCyc-style flat files, tab-delimited
tables, and BioPAX level 3.

ChlamyCyc and its sibling green-algal PGDBs can reuse the Pathway Tools
`pathways.dat` importer that MetaCyc uses, but they mint `PMN` CURIEs so their
frame IDs stay separate from BioCyc frame IDs. PMN remains `license-gated` in
`conf/sources.yaml` pending staff-issued access to an authorized native export.

### VEuPathDB

VEuPathDB covers eukaryotic pathogens and selected fungi/protists through
component sites such as FungiDB, PlasmoDB, TriTrypDB, AmoebaDB, CryptoDB,
GiardiaDB, MicrosporidiaDB, PiroplasmaDB, ToxoDB, and TrichDB (and integrates
historical kinetoplastid/apicomplexan Pathway Tools projections such as
TrypanoCyc, LeishCyc, and ToxoCyc). Its WDK service can export record searches,
and gene pages expose metabolic pathway tables with reaction compounds and
ChEBI hover IDs on reaction equations.

The pathway layer is a support source, not a primary import. VEuPathDB
metabolic pathway tables are useful for checking whether fungal or protist
genes support a KEGG, MetaCyc, or Reactome candidate, but the maps are loaded
from those upstream resources and inherit their topology and licensing
questions. The local WDK TSV importer (`pathwaymech-import-veupathdb-pathways`)
consumes the `MetabolicPathways` gene table exported from component sites and
keeps component-site gene IDs as seed row evidence rather than minting
`VEuPathDB` CURIEs.

### GapMind

GapMind is a curated rulebase for identifying amino-acid biosynthesis and
small-carbon catabolism steps in bacterial and archaeal genomes. Current
PaperBLAST `master` stores amino-acid rules in `gaps/aa/*.steps`, carbon-source
rules in `gaps/carbon/*.steps`, and TSV index files that assign local slugs
such as `arg`, `thr`, `pyruvate`, and `xylose` to pathway labels.

The `.steps` files are valuable for variant triage and enzyme support (`pathwaymech-import-gapmind-steps`)
but are not a direct pathway-graph import. They define local steps and
alternatives over EC numbers, UniProt exemplars, PaperBLAST curation tags, HMM
accessions, and local imports rather than stable GapMind CURIEs or chemical
reaction nodes.

### UniPathway, dbCAN-PUL, SEED / PubSEED, BRENDA, HADEG, and DRAM

Six additional specialist sources now have enabled `support` adapters in
`conf/sources.yaml`:

- **UniPathway (`unipathway`, priority 160):** Retired GO-hosted `upa.obo`
  crosswalk (`pathwaymech-import-unipathway-obo`) connecting legacy `UPa:*`
  pathway/reaction terms to `RHEA`, `MetaCyc`, `KEGG`, `GO`, `EC`, and `CHEBI`.
- **dbCAN-PUL (`dbcan-pul`, priority 170):** Local February 2025 workbook
  support adapter (`pathwaymech-import-dbcan-pul`) preserving all 633
  experimentally characterized polysaccharide utilization loci (`PUL####`),
  target glycan substrates, and CAZyme/EC annotations; public redistribution
  terms remain under review.
- **SEED / PubSEED Subsystems (`seed-pubseed`, priority 200):** Native
  subsystem API bundle importer (`pathwaymech-import-seed-subsystems`)
  preserving ordered functional roles, genome variant codes, and feature cells
  with hash provenance.
- **BRENDA (`brenda`, priority 250):** Official RDF/TTL (`CC BY 4.0`) and
  audited web role-query support adapter (`pathwaymech-import-brenda-context`)
  preserving reaction-component assertions (`participates_in`, `substrate`,
  `product`, `inhibitor`, `activator`) and organism/literature context without
  minting standalone pathway graphs.
- **HADEG (`hadeg`, priority 260):** Local CSV membership adapter
  (`pathwaymech-import-hadeg`) indexing 629 hydrocarbon/xenobiotic degradation
  gene-to-pathway rows under upstream GPL-3.0 terms.
- **DRAM (`dram`, priority 280):** Local DRAM1 module-step support adapter
  (`pathwaymech-import-dram-modules`) preserving KO/EC step coordinates and
  module coverage rules while tracking KEGG lineage caveats.

## Defer or use only as crosswalks

| Resource | Why not a primary ingest source |
| --- | --- |
| Pathway Commons | Aggregates Reactome, WikiPathways, BioCyc, and others in one BioPAX model, but inherits the intellectual-property restrictions of the source databases. Good parser fixture; poor canonical source. |
| MetaNetX / MNXref | Excellent compound (`metanetx.chemical`), reaction, and model identifier reconciliation layer across BiGG, ModelSEED, BioCyc, and Reactome, but it intentionally abstracts away direction and is not a curated pathway-topology source. |
| ChEBI | Required chemical ontology for participants, and already indirectly available through Rhea, but it does not define pathways. |
| UniProtKB | Required protein/enzyme grounding layer, but it does not define pathway graphs. |
| BioModels | Useful SBML corpus for individual kinetic or constraint models, including microbial models, but records are publication-scale mathematical models rather than a normalized catalogue of pathway definitions. |
| antiSMASH DB | Comprehensive for predicted BGC regions, but predictions should not outrank MIBiG's experimentally characterized BGCs. |
| PANTHER Pathway (`panther`, priority 180) | Exposes 177 regulatory and metabolic pathways in SBML and BioPAX level 3. Enabled only as a low-priority BioPAX `fixture` because its scope is mostly generic/eukaryotic. |
| PULDB (`puldb`, priority 190) | Complements dbCAN-PUL with Bacteroidetes-centered experimental and predicted `susC`/`susD` polysaccharide-utilization loci, but is prediction-heavy and lacks a clear bulk open license. |
| MicroScope / MicroCyc (`microscope-microcyc`, priority 210) | Exports Tier-3 PathoLogic Pathway Tools PGDBs predicted over MetaCyc, requiring authenticated MicroScope access. |
| JGI IMG/M, IMG-ABC, and MycoCosm (`jgi-img-abc`, priority 220) | Strong archaeal, bacterial, fungal (MycoCosm), metagenome, and BGC portals, but downloads are gated by JGI Data Usage Policy and pathway topology is imported from KEGG/MetaCyc or computationally predicted. |
| E. coli Metabolome Database (`ecmdb`, priority 230) | *E. coli* K-12 metabolite, protein, reaction, and pathway cards overlap EcoCyc and KEGG without an open bulk pathway-graph license. |
| AlgaePath (`algaepath`, priority 240) | Maps *Chlamydomonas* and *Neodesmus* expression data onto KEGG-derived pathway views; outranked by PMN/ChlamyCyc for algal topology. |
| enviPath (`envipath`, priority 270) | Succeeds UM-BBD/EAWAG-BBD for microbial environmental biotransformation pathways and exposes REST/RDF JSON endpoints, but website terms restrict bulk data extraction and redistribution (`license-gated`). |
| DiTing (`diting`, priority 290) | Biogeochemical cycle (C, N, S, Fe) KO abundance formulas (GPL-3.0); useful as presence rules rather than causal biochemical graphs. |
| METABOLIC (`metabolic`, priority 300) | Biogeochemical and metabolic HMM/KO module templates (GPL-3.0) with packaged spreadsheets requiring explicit data-license clearance (`license-gated`). |
| gutSMASH (`gutsmash`, priority 310) | Curated reference database and HMM detection rules for primary anaerobic bacterial metabolic gene clusters (SCFA, Stickland fermentation, TMA, microcompartments, Rnf/Ech respiratory chains; AGPL-3.0). Strong specialist complement to MIBiG for primary anaerobic MGC loci, but requires a GenBank/rule parser and native MGC accession policy before promotion (`deferred`). |
| Mechanism and Catalytic Site Atlas / M-CSA (`m-csa`, priority 320) | EMBL-EBI curated database (`CC BY 4.0`) of ~1,000 enzyme reaction mechanisms with catalytic residues, cofactors, and step-by-step electron-pushing mechanisms cross-referenced to `EC`, `RHEA`, `CHEBI`, `UniProtKB`, and `PDB`. Ideal support candidate for PathwayMech's `reaction_mechanisms` slot, but requires a REST/JSON support adapter (`deferred`). |
| Virtual Metabolic Human / AGORA2 (`vmh-agora2`, priority 330) | Over 7,300 strain-level gut microbial (bacterial, archaeal, and fungal) genome-scale metabolic reconstructions in SBML/MAT (`MIT` license on `ThieleLab/modelCreation`) with VMH reaction/metabolite cross-references to BiGG, KEGG, MetaCyc, and ChEBI. Deferred behind `bigg` and `modelseed` as an organism-model support layer (`deferred`). |
| SGD YeastPathways, Candida Genome Database Pathways, and PomBase GO-CAMs | Normalize under existing `go-cam` (`gomodel:YeastPathways_*` and PomBase *S. pombe* GO-CAM JSONs) and `metacyc` (`metacyc-sgd-pathway-xml` + `SGD` gene authority) rows rather than separate source IDs. |
| KBase | Useful ModelSEED-powered workspace for bacterial, archaeal, and fungal metabolic reconstructions, but narratives and generated models are user artifacts over ModelSEED reactions rather than a curated pathway-definition catalogue. |

## Import implications

1. Add native-prefix support only for future sources with stable pathway or
   reaction identifiers that are not already accepted by PathwayMech, possibly
   including `SEED` for subsystem and role IDs or `MCSA` for catalytic mechanism
   entries. Do not mint `VEuPathDB` CURIEs from component-site gene IDs in
   support rows.
2. Split source roles in `conf/sources.yaml` into operational classes covering
   canonical pathway definitions, biosynthetic/metabolic gene cluster references,
   reaction and catalytic-mechanism references, organism membership calls, and
   crosswalks.
3. Treat PMN/ChlamyCyc like MetaCyc and KEGG: implemented, license-gated, and
   limited to local extracts. Keep `dbcan-pul`, `seed-pubseed`, `brenda`,
   `hadeg`, `dram`, `veupathdb`, `gapmind`, and `unipathway` as provenance-pinned
   support layers that enrich or audit candidate pathways without auto-emitting
   unreviewed YAML graphs.
4. Normalize every elementary reaction through Rhea when possible; if a
   candidate source names only an EC number or a KEGG reaction, attach the
   source ID but leave the Rhea edge unmapped until an explicit equivalence is
   checked.
5. Keep generated source extracts out of `data/pathways/`. Store only
   hand-reviewed pathway records with short quotes from primary references, and
   record any one-to-many reaction mapping decision in `curation/decisions.tsv`.

## Current recommendations

1. **Prioritize the active and enabled support queue before building new bulk
   importers.** Expanding hand-reviewed records from `go-cam` (including PomBase
   *S. pombe* and non-duplicate fungal GO-CAMs), `wikipathways` (`20261010`
   release), `mibig`, `reactome`, and `pathbank` — cross-checked against enabled
   support adapters (`brenda`, `dbcan-pul`, `hadeg`, `dram`, `seed-pubseed`,
   `gapmind`, `veupathdb`) — delivers higher immediate curation yield than
   activating new unimplemented sources.
2. **Top two next sources to implement (`m-csa` and `gutsmash`) once the active
   queue is ready for new adapters:**
   - **First (`m-csa`, priority 320):** Build a bounded REST/JSON/CSV support
     adapter for EMBL-EBI's Mechanism and Catalytic Site Atlas (`CC BY 4.0`).
     M-CSA directly populates PathwayMech's `reaction_mechanisms` schema slot
     with step-by-step catalytic mechanisms, proton/electron transfers, and
     catalytic residues already grounded in `EC`, `RHEA`, `CHEBI`, and
     `UniProtKB`.
   - **Second (`gutsmash`, priority 310):** Build a bounded support/locus
     inspector for gutSMASH reference metabolic gene clusters (`AGPL-3.0`) to
     cover anaerobic gut bacterial and archaeal primary/energy pathways (SCFA,
     Stickland fermentation, TMA, metabolic microcompartments, Rnf/Ech
     complexes) that fall outside `mibig`'s secondary-metabolite scope.
3. **Run `source-triage` on the first authorized PMN/ChlamyCyc export** once
   PMN license credentials are issued so green-algal Pathway Tools records can
   be curated alongside bacterial, archaeal, fungal, and protist pathways.
4. **Keep MetaCyc and KEGG as licensed local/bounded extractors**, Rhea as the
   reaction normalizer, and `vmh-agora2` deferred behind `bigg` and `modelseed`
   until strain-specific gut reconstruction membership is needed.

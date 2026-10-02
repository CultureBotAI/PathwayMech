# Microbial pathway source discovery

Updated: 2026-10-02

This memo ranks resources that could feed PathwayMech with pathway definitions,
reaction definitions, organism-specific pathway calls, or crosswalks. The local
schema accepts only whitelisted source and grounding CURIEs, so several
resources below would need new prefixes before their native identifiers can be
stored in curated YAML.

## Shortlist

| Tier | Source | Best import target | Access | Reuse risk |
| --- | --- | --- | --- | --- |
| 0 | MetaCyc / BioCyc | Curated metabolic pathway definitions with reaction order, reactions, compounds, enzymes, taxa, and review text | BioCyc flat files or web services after license registration | Medium: BioCyc Limited Databases can be used and modified but not redistributed |
| 0 | KEGG PATHWAY / MODULE | High-coverage maps and KO/module signatures for microbial metabolism | Academic REST or KGML; full weekly FTP requires a subscription | High: not public; non-academic use requires a license |
| 0 | Rhea | Canonical ChEBI-grounded biochemical reactions and EC/UniProt/GO cross-references | Free FTP in RDF, BioPAX 3, RXN/RD, and TSV; SPARQL endpoint | Low: CC BY 4.0 |
| 0 | GO and GO-CAM | GO process grounding and causal activity models that can map naturally to mechanistic edges | OBO/OWL/JSON ontology releases and GO-CAM JSON downloads/API | Low: GO data products are CC BY 4.0 |
| 1 | WikiPathways | Community-curated pathway graphs in GPML/RDF, useful for open fixtures and BioPAX/GPML parser work | Monthly GPML, GMT, SVG, and RDF archives | Low: data-release repository is CC0 |
| 1 | MIBiG | Experimentally characterized biosynthetic gene clusters and their products | JSON records and GBK sequences | Low: CC BY 4.0 |
| 1 | Reactome | Detailed BioPAX/SBML reaction graphs for the few microbial or microbe-adjacent species it covers | BioPAX, all-species SBML, tabular mappings, GraphDB, Content Service | Low to medium: annotation files are CC0; database dumps and diagrams are CC BY 4.0 |
| 2 | ModelSEED Biochemistry | ModelSEED reaction/compound namespace, aliases to KEGG/MetaCyc/Rhea/BiGG, and modeling-tested microbial reaction definitions | GitHub TSV/JSON plus ModelSEED web/API | Medium: released as CC BY, but records derived from KEGG and MetaCyc inherit source licenses |
| 2 | BiGG Models | Published organism-scale microbial metabolic networks in SBML/JSON, with subsystem labels | Web API and model downloads | Medium: free for noncommercial research only |
| 2 | BV-BRC Pathways and Subsystems | Genome-specific pathway presence calls, EC membership, and SEED functional-role subsystems across public bacterial genomes | BV-BRC API and Comparative Systems TSV/JSON outputs | Medium to high: KEGG-derived maps and service-specific data |
| 2 | Plant Metabolic Network / ChlamyCyc | Pathway Tools pathway/genome databases for green algae, including Chlamydomonas-specific pathways | Local free-license Pathway Tools flat files | Low to medium: free PMN license, but download requires a license request and the source is algae-only |
| 2 | VEuPathDB metabolic pathways | KEGG/MetaCyc pathway membership over fungal and protist gene records | Local WDK `MetabolicPathways` TSV exports from component sites | Medium: useful organism evidence, but the pathway topology comes from KEGG/MetaCyc |
| 2 | GapMind | Curated bacterial and archaeal amino-acid biosynthesis and small-carbon catabolism enzyme-step rules | PaperBLAST GitHub `gaps/aa` and `gaps/carbon` files | Medium: GPL-3.0 source; local rule IDs are support-only seed rows |

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
| ModelSEED | https://github.com/ModelSEED/ModelSEEDDatabase | https://github.com/ModelSEED/ModelSEEDDatabase |
| BiGG | https://bigg.ucsd.edu/data_access | https://bigg.ucsd.edu/license |
| BV-BRC | https://www.bv-brc.org/api/doc/pathway | https://www.bv-brc.org/docs/quick_references/services/comparative_systems.html |
| Plant Metabolic Network / ChlamyCyc | https://plantcyc.org/downloads/ | https://plantcyc.org/?webform=license-agreement |
| VEuPathDB | https://veupathdb.org/service-api.html | https://veupathdb.org/veupathdb/app/static-content/about.html |
| GapMind | https://github.com/morgannprice/PaperBLAST/tree/master/gaps | https://github.com/morgannprice/PaperBLAST/blob/master/LICENSE |
| UniPathway | https://github.com/geneontology/unipathway | https://github.com/geneontology/unipathway |

## Tier 0: already configured and worth keeping

### MetaCyc / BioCyc

MetaCyc is still the best source for manually curated microbial metabolic
pathway definitions: it has stable pathway and reaction IDs, reaction ordering,
compounds, EC numbers, enzymes, taxa, citations, and minireviews. Pathway Tools
exports every BioCyc Pathway/Genome Database as flat files such as
`pathways.dat`, `reactions.dat`, `compounds.dat`, `enzrxns.dat`, `proteins.dat`,
and `pubs.dat`, and the same page points to BioCyc web services as an alternate
access path.

The catch is licensing. The 2026 BioCyc flat-file agreement classifies only
EcoCyc and the Faecalibacterium prausnitzii A2-165 PGDB as "Open Databases";
the other BioCyc PGDBs are "Limited Databases" that can be used and modified
worldwide without royalties but cannot be redistributed. Use MetaCyc IDs freely
as cross-references, but get a legal read before publishing any generated YAML
that mechanically copies pathway membership, descriptions, or comments.

### KEGG PATHWAY and KEGG MODULE

KEGG remains an essential external reference because it covers microbial
metabolic maps, module completeness rules, reactions, compounds, orthology
groups, and organism-specific gene calls. The REST API can return KGML for
pathway entries, and the KGML XML is much easier to parse than the rendered
maps. KEGG MODULE definitions are also useful for deciding whether a pathway is
present in a genome from a set of KOs.

The import should be ID-first and license-aware. KEGG's REST service is made
available only for academic users, the full FTP is a paid academic subscription,
and non-academic use requires a commercial license. PathwayMech can keep KEGG
as a grounding source, but a bulk open-data importer should not redistribute
raw KGML maps or generated maps unless the project has explicit permission.

### Rhea

Rhea is not a pathway database, but it is the cleanest reaction backbone for
PathwayMech. Reactions are expert-curated, reaction participants are ChEBI IDs,
cross-references connect to EC, UniProtKB, and GO, and the whole release can be
downloaded from FTP in RDF, BioPAX level 3, RXN/RD, and TSV formats. Keep Rhea
enabled for the reaction layer and prefer `RHEA` reaction IDs over local
reaction IDs whenever a source pathway can be mapped unambiguously.

### GO and GO-CAM

GO has two complementary roles. First, GO biological-process terms are stable
pathway/process anchors, with OBO, OWL, and OBO Graph JSON downloads plus
separate computed taxon constraints. Second, GO-CAMs connect GO molecular
activities into qualitative causal models and are now downloadable in a
LinkML-defined JSON format; those activity nodes and causal links can seed
`mechanistic_edges` more directly than a plain GO DAG can.

## Tier 1: active open ingests with narrow remaining headroom

### WikiPathways

WikiPathways is the easiest permissive pathway-graph source to parse visually.
The official monthly release archive at `data.wikipathways.org` exposes GPML,
GMT, SVG, and RDF bundles, and its data-release repository is CC0. GPML stores
pathway diagrams with data nodes and interactions, while RDF exposes the same
curated pathway content as linked data.

The main limitation is coverage and curation depth for microbes: many
WikiPathways records are mammalian, plant, or disease focused. Treat it as a
format and parser target first, then whitelist microbial species and microbial
processes rather than bulk-ingesting every organism.

### MIBiG

MIBiG is the best open source for microbial specialized metabolism where the
"pathway" is an experimentally characterized biosynthetic gene cluster rather
than a small-molecule reaction chain. Records are available as JSON, BGC
sequences are available as GBK, and current MIBiG releases are CC BY 4.0.

The mapping into PathwayMech is intentionally BGC-shaped: MIBiG knows loci,
genes, product chemistry, biosynthetic class, and evidence, but generally does
not enumerate every Rhea-like elementary reaction. Use it for
secondary-metabolite records with products, clusters, tailoring enzymes, and
PubMed-backed BGC publications, and keep antiSMASH DB predictions downstream
from MIBiG rather than using predictions as primary curated evidence.

### Reactome

Reactome is a high-quality graph source with BioPAX and all-species SBML
downloads, reaction-to-PubMed tables, ChEBI/UniProt mappings, a GraphDB export,
and a Content Service. The active BioPAX importer can exercise Reactome stable
pathway and reaction IDs, ChEBI metabolites, UniProtKB catalysts, NCBITaxon
organisms, and reaction-local PMIDs without KEGG or MetaCyc redistribution.

Do not over-rank Reactome for broad bacteria. Its deepest curation is human;
it contains some microbial pages such as Mycobacterium tuberculosis and
Escherichia coli, and it infers pathways to selected eukaryotic model
organisms such as yeasts and Plasmodium, but it is not a comprehensive
prokaryotic source. Import only species whose source evidence is curated enough
to support the record.

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
metabolite IDs, SBML/JSON/MAT downloads, a web API, and subsystem labels on
model reactions. It is good evidence that a reaction participates in the
metabolic model of a specific microbe.

Two details keep it out of tier 1: BiGG subsystems are not curated pathway
definitions, and the UCSD license is free for educational, research, and
non-profit use but requires commercial users to contact UCSD. Use it as
organism-specific supporting evidence, not as a canonical pathway authority.

### BV-BRC Pathways and Subsystems

BV-BRC is useful for bacterial taxon triage. Its `pathway` API rows connect a
genome, gene, EC number, pathway ID, pathway name, and pathway class, and its
`subsystem` rows connect genomes and genes to SEED roles and subsystem IDs. The
Comparative Systems service can also export pathway and subsystem TSV/JSON
files for selected genome sets.

Those rows are membership calls, not pathway definitions. BV-BRC pathway maps
are represented with KEGG, and the service folds in PATRIC/RASTtk calls, so it
is a good way to find organisms and EC steps for a candidate pathway but should
not be treated as the independent source of pathway topology.

### Plant Metabolic Network / ChlamyCyc

The Plant Metabolic Network fills the clearest algal gap. PMN publishes
Pathway Tools pathway/genome databases for plants and green algae, and
`ChlamyCyc` is a current Chlamydomonas reinhardtii database rather than only a
historical web portal. PMN downloads require a free license request and include
the native Ocelot representation, BioCyc-style flat files, tab-delimited
tables, and BioPAX level 3.

ChlamyCyc and its sibling green-algal PGDBs can reuse the Pathway Tools
`pathways.dat` importer that MetaCyc uses, but they mint `PMN` CURIEs so their
frame IDs stay separate from BioCyc frame IDs. PMN closes a real algal coverage
gap, but it is not broad microbial coverage, and much of the per-species
network is computationally predicted then refined by PMN validation rules.

### VEuPathDB

VEuPathDB covers eukaryotic pathogens and selected fungi/protists through
component sites such as FungiDB, PlasmoDB, TriTrypDB, AmoebaDB, CryptoDB,
GiardiaDB, MicrosporidiaDB, PiroplasmaDB, ToxoDB, and TrichDB. Its WDK service
can export record searches, and gene pages expose metabolic pathway tables
with reaction compounds and ChEBI hover IDs on reaction equations.

The pathway layer is a support source, not a primary import. VEuPathDB
metabolic pathway tables are useful for checking whether fungal or protist
genes support a KEGG, MetaCyc, or Reactome candidate, but the maps are loaded
from those upstream resources and inherit their topology and licensing
questions. The local WDK TSV importer consumes the `MetabolicPathways` gene
table exported from component sites and keeps component-site gene IDs as seed
row evidence rather than minting `VEuPathDB` CURIEs.

### GapMind

GapMind is a curated rulebase for identifying amino-acid biosynthesis and
small-carbon catabolism steps in bacterial and archaeal genomes. The 2020
mSystems paper describes amino-acid GapMind as a web tool that uses many
variant routes and a database of experimentally characterized proteins instead
of transitive annotations, and its data-availability statement points to the
PaperBLAST repository. Current PaperBLAST `master` stores amino-acid rules in
`gaps/aa/*.steps`, carbon-source rules in `gaps/carbon/*.steps`, and TSV index
files that assign local slugs such as `arg`, `thr`, `pyruvate`, and `xylose`
to pathway labels.

The `.steps` files are valuable for variant triage and enzyme support but are
not a direct pathway-graph import. They define local steps and alternatives
over EC numbers, UniProt exemplars, PaperBLAST curation tags, HMM accessions,
and local imports rather than stable GapMind CURIEs or chemical reaction
nodes. Some records cite MetaCyc pathway IDs in comments, and many encode
transporters or protein complexes needed to decide whether a pathway is
present in a genome. The local support importer indexes step, import, and
variant rows from local `*.steps` files so reviewers can find EC, UniProtKB,
MetaCyc, and HMM clues, while leaving GPL-3.0 rule text and local GapMind
slugs out of curated YAML until there is a native-ID normalization decision.

## Defer or use only as crosswalks

| Resource | Why not a primary ingest source |
| --- | --- |
| Pathway Commons | Aggregates Reactome, WikiPathways, BioCyc, and others in one BioPAX model, but inherits the intellectual-property restrictions of the source databases. Good parser fixture; poor canonical source. |
| MetaNetX / MNXref | Excellent compound, reaction, and model identifier reconciliation layer across BiGG, ModelSEED, BioCyc, and Reactome, but it intentionally abstracts away direction and is not a curated pathway-topology source. |
| ChEBI | Required chemical ontology for participants, and already indirectly available through Rhea, but it does not define pathways. |
| UniProtKB | Required protein/enzyme grounding layer, but it does not define pathway graphs. |
| UniPathway | The inactive GO-hosted `UPA`, `ULS`, `UER`, `UCR`, and `UPC` ontology has pathway, subpathway, enzymatic-reaction, reaction, and compound identifiers plus reaction-participant edges, but its README says reactions have already moved into Rhea. Its GO mirror has no explicit license metadata and the historical chemistry was imported from KEGG LIGAND, so treat it as a legacy UniProtKB crosswalk unless licensing and a native `UPA` prefix are resolved. |
| BioModels | Useful SBML corpus for individual kinetic or constraint models, including microbial models, but records are publication-scale mathematical models rather than a normalized catalogue of pathway definitions. |
| antiSMASH DB | Comprehensive for predicted BGC regions, but predictions should not outrank MIBiG's experimentally characterized BGCs. |
| JGI IMG/M | Strong archaeal, bacterial, and metagenome functional annotation portal with KEGG, MetaCyc, and IMG Term pathway views, but source downloads require JGI Data Usage Policy acceptance and the pathway topology is imported or IMG-specific rather than a redistributable canonical graph. |
| KBase | Useful ModelSEED-powered workspace for bacterial and fungal metabolic reconstructions, but narratives and generated models are user artifacts over ModelSEED reactions rather than a curated pathway-definition catalogue. |

## Import implications

1. Add native-prefix support only for future sources with stable pathway or
   reaction identifiers that are not already accepted by PathwayMech, possibly
   including `SEED` for subsystem and role IDs. Do not mint `VEuPathDB` CURIEs
   from component-site gene IDs in support rows.
2. Split source roles in `conf/sources.yaml` into four operational classes:
   canonical pathway definitions, reaction references, organism membership
   calls, and crosswalks.
3. Treat PMN/ChlamyCyc like MetaCyc and KEGG: implemented, license-gated, and
   limited to local extracts. Use VEuPathDB as a support-only WDK TSV ingest
   for KEGG/MetaCyc pathway membership over fungal and protist genes. Use
   GapMind as a support-only `.steps` indexer, and keep UniPathway disabled
   until its licensing, native-ID, and parser decisions are resolved.
4. Normalize every elementary reaction through Rhea when possible; if a
   candidate source names only an EC number or a KEGG reaction, attach the
   source ID but leave the Rhea edge unmapped until an explicit equivalence is
   checked.
5. Keep generated source extracts out of `data/pathways/`. Store only
   hand-reviewed pathway records with short quotes from primary references, and
   record any one-to-many reaction mapping decision in `curation/decisions.tsv`.

## Current recommendations

1. Keep adding GO-CAM, WikiPathways, Reactome, and MIBiG records only when a
   candidate contributes a bounded pathway or experimentally characterized BGC
   that is not a duplicate of the current corpus.
2. Run `source-triage` on the first PMN/ChlamyCyc canary before committing an
   algal record. Its Pathway Tools format is supported after MetaCyc/BioCyc
   planning, but the canary still needs source-ID and evidence decisions.
3. Keep VEuPathDB as a fungal/protist organism-membership support source. Its
   seed rows can help pick Plasmodium, Giardia, Cryptosporidium, Trypanosoma,
   or fungal canaries for KEGG/MetaCyc/Reactome routes, but it should not be
   the topology authority.
4. Keep MetaCyc and KEGG as licensed local extractors, Rhea as the reaction
   normalizer, ModelSEED/BiGG/BV-BRC/GapMind as support layers, and UniPathway
   as a disabled legacy crosswalk.

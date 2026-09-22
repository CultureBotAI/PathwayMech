# Microbial pathway source discovery

Updated: 2026-09-22

This memo ranks resources that could feed PathwayMech with pathway definitions,
reaction definitions, organism-specific pathway calls, or crosswalks. The local
schema currently accepts only GO, MetaCyc, KEGG, RHEA, ChEBI, UniProtKB, EC,
NCBITaxon, GTDB, PMID, and DOI CURIEs, so several resources below would need new
prefixes before their native identifiers can be stored in curated YAML.

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

## Tier 1: add next

### WikiPathways

WikiPathways is the easiest permissive pathway-graph source to test first. The
official monthly release archive at `data.wikipathways.org` exposes GPML, GMT,
SVG, and RDF bundles, and its data-release repository is CC0. GPML stores
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

The mapping into PathwayMech will be lossy unless we add BGC-shaped fields:
MIBiG knows loci, genes, product chemistry, biosynthetic class, and evidence,
but generally does not enumerate every Rhea-like elementary reaction. Use it
for secondary-metabolite records with participants such as products, clusters,
and tailoring enzymes, and keep antiSMASH DB predictions downstream from MIBiG
rather than using predictions as primary curated evidence.

### Reactome

Reactome is a high-quality graph source with BioPAX and all-species SBML
downloads, reaction-to-PubMed tables, ChEBI/UniProt mappings, a GraphDB export,
and a Content Service. The current download directory already exposes the files
we would want for an import prototype: `biopax.zip`, `all_species.3.1.sbml.tgz`,
`ReactionPMIDS.txt`, `ChEBI2ReactomeReactions.txt`, and `gocam.zip`.

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

## Defer or use only as crosswalks

| Resource | Why not a primary ingest source |
| --- | --- |
| Pathway Commons | Aggregates Reactome, WikiPathways, BioCyc, and others in one BioPAX model, but inherits the intellectual-property restrictions of the source databases. Good parser fixture; poor canonical source. |
| MetaNetX / MNXref | Excellent compound, reaction, and model identifier reconciliation layer across BiGG, ModelSEED, BioCyc, and Reactome, but it intentionally abstracts away direction and is not a curated pathway-topology source. |
| ChEBI | Required chemical ontology for participants, and already indirectly available through Rhea, but it does not define pathways. |
| UniProtKB | Required protein/enzyme grounding layer, but it does not define pathway graphs. |
| BioModels | Useful SBML corpus for individual kinetic or constraint models, including microbial models, but records are publication-scale mathematical models rather than a normalized catalogue of pathway definitions. |
| antiSMASH DB | Comprehensive for predicted BGC regions, but predictions should not outrank MIBiG's experimentally characterized BGCs. |

## Import implications

1. Add native-prefix support before storing tier-1 identifiers:
   `Reactome`, `WikiPathways`, `MIBiG`, `ModelSEED`, `BiGG`, `BV-BRC`, and
   possibly `SEED` for subsystem and role IDs.
2. Split source roles in `conf/sources.yaml` into four operational classes:
   canonical pathway definitions, reaction references, organism membership
   calls, and crosswalks.
3. Implement importers in license order:
   `go-cam` and `wikipathways` first, then `mibig`, then `reactome`, then
   gated local extractors for MetaCyc/KEGG/BioCyc that run only in an
   appropriately licensed environment.
4. Normalize every elementary reaction through Rhea when possible; if a
   candidate source names only an EC number or a KEGG reaction, attach the
   source ID but leave the Rhea edge unmapped until an explicit equivalence is
   checked.
5. Keep generated source extracts out of `data/pathways/`. Store only
   hand-reviewed pathway records with short quotes from primary references, and
   record any one-to-many reaction mapping decision in `curation/decisions.tsv`.

## Immediate targets

The first low-risk importer should read GO-CAM JSON and emit a draft record for
one microbial model, because the model is already a causal graph and the source
license matches an open repository. The second should parse WikiPathways GPML
for one bacterial or fungal pathway and exercise participant/interaction
normalization without touching KEGG or MetaCyc licensing. In parallel, Rhea TSV
downloads can build the `RHEA` to `CHEBI`, `EC`, and `UniProtKB` lookup table
that both importers will need.

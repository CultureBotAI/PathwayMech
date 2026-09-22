# Pathway element identifier source discovery

Updated: 2026-09-22

This follow-up ranks pathway sources by a narrower question than the broader
microbial source survey: does each pathway definition carry stable biological
identifiers on the elements inside the pathway, not just a pathway name and a
drawn map?

The best candidates expose identifiers on at least two of reactions, compounds,
gene products, taxa, and causal edges. A source that stores only pathway-to-gene
membership is useful triage input, but not enough to seed `mechanistic_edges`
without a second pathway-topology source.

## Shortlist

| Tier | Source | Pathway element identifiers | Best use |
| --- | --- | --- | --- |
| 0 | MetaCyc / BioCyc | Pathway, reaction, enzymatic-reaction, compound, protein, gene, species, DBLINKS, PubMed-linked evidence codes | Best curated metabolic topology, with licensing review before redistribution |
| 0 | KEGG KGML | Pathway-map entries with KEGG compound, glycan, reaction, KO, EC, and organism-gene identifiers | High-coverage reference maps and organism overlays, license-gated |
| 0 | GO-CAM JSON | GO molecular activities, RO causal predicates, UniProtKB/GO enablers, CHEBI/UniProtKB molecules, NCBITaxon taxa, ECO/PMID evidence | Open causal activity graphs; strongest shape match for PathwayMech edges |
| 1 | Reactome BioPAX/SBML | Reactome stable IDs for events and entities plus ChEBI, UniProt, Ensembl, NCBI, GO, KEGG, PubMed mappings | Rich BioPAX reaction graphs, but microbial scope is narrow |
| 1 | WikiPathways GPML/RDF | WikiPathways IDs and BridgeDb-backed Xrefs on GPML data nodes; RDF exports direct and harmonized pathway content | Open parser fixture and curated small microbial set |
| 1 | PathBank BioPAX/SBML/PWML | PathBank IDs plus ChEBI/KEGG metabolite CSV links and UniProt protein CSV links | Model-organism BioPAX/SBML fixture, especially E. coli and yeast |
| 2 | MIBiG JSON/GBK | BGC accessions, GenBank regions, genes/protein translations, products, publications | Secondary-metabolite/BGC records, not elementary reaction chains |
| 2 | Rhea | Rhea reaction IDs, ChEBI participants, EC, UniProtKB, GO xrefs | Normalize reactions after a pathway source proposes them |
| 3 | ModelSEED / BiGG / BV-BRC | Reaction, compound, gene, genome, model, or KEGG-pathway membership IDs | Crosswalks and organism membership evidence, not canonical pathway definitions |

## Identifier coverage by source

### MetaCyc / BioCyc

**Element IDs:** excellent. Pathway Tools exports each BioCyc Pathway/Genome
Database as flat files with `UNIQUE-ID` on every object. `pathways.dat` includes
`REACTION-LIST`, `PREDECESSORS`, `SPECIES`, `DBLINKS`, and `CITATIONS`;
`reactions.dat` links reaction frames to `LEFT`, `RIGHT`, `EC-NUMBER`, and
`ENZYMATIC-REACTION`; `enzrxns.dat` connects a reaction to an `ENZYME`; and
`proteins.dat` links proteins to genes, GO terms, catalytic reactions, and
DBLINKS. `compounds.dat`, `genes.dat`, and `pubs.dat` fill out the molecular,
gene, and non-PubMed reference layers. Evidence codes can appear in `CITATIONS`
slots, including experimental and computational evidence-code families.

**Formats and endpoints:** flat files, BioPAX, SBML, FASTA, mol files, Ocelot,
and Pathway Tools web services.

**Curation stance:** best source for curated microbial metabolism. Native
MetaCyc frame IDs are stable enough to store as source IDs, and DBLINKS can
ground compounds, proteins, and genes. Use only under an explicit BioCyc license
because most BioCyc PGDBs are Limited Databases.

### KEGG PATHWAY / MODULE / KGML

**Element IDs:** very good, but KEGG-native. KGML entries identify ortholog,
enzyme, reaction, compound, glycan, map, group, and organism-gene nodes with
KEGG IDs, and `reaction` elements identify KEGG `rn:` reactions with
`substrate` and `product` children named by KEGG `cpd:` or `gl:` accessions.
Reference maps can be projected through `ko`, `rn`, or `ec` maps, and
organism-specific maps replace the reference boxes with KEGG gene IDs.

**Formats and endpoints:** KGML from the KEGG API for individual maps; full
weekly FTP for academic subscribers; REST `link` and `conv` calls for selected
outside identifiers.

**Curation stance:** keep as an enabled grounding source, but do not build a
redistributable bulk importer without a license. KGML has pathway element IDs,
but those IDs are KEGG IDs; mapping to Rhea, ChEBI, GO, UniProtKB, and EC needs
explicit curation or an approved crosswalk.

### GO-CAM

**Element IDs:** excellent for causal activity graphs. The LinkML schema models
GO-CAMs as `Model` objects that contain `Activity` nodes. Activities carry GO
molecular-function terms, `enabled_by` associations to individual gene products
or protein complexes, molecular associations to CHEBI or UniProtKB terms,
GO cellular locations, GO biological-process `part_of` links, NCBITaxon model
taxa, RO causal predicates between activities, and ECO/publication evidence.

**Formats and endpoints:** versioned GO-CAM JSON downloads, one file per model;
GO API routes for model ID, taxon, and PMID lookup; the `gocam-py` package
validates the same LinkML-defined JSON representation.

**Curation stance:** first open importer to build. GO-CAM already represents
causal activity edges with CURIE-bearing nodes and predicates, and GO data
products are CC BY 4.0. The limitation is coverage, not shape: microbial
metabolic pathways may be absent or shallower than in MetaCyc/KEGG.

### Reactome

**Element IDs:** excellent inside its scope. Reactome assigns stable IDs to
pathways, reactions, and physical entities, and its downloads include
BioPAX level 3, all-species SBML, the GraphDB dump, stable-id tables, reaction
to PMID mappings, and ChEBI/UniProt/NCBI/Ensembl mappings down to reaction
or pathway levels.

**Formats and endpoints:** BioPAX, SBML, GraphDB, MySQL dumps, Content Service
API, and tabular mapping files from the current download directory.

**Curation stance:** valuable for BioPAX/SBML parser work and for the few
microbial or microbe-adjacent organisms Reactome curates or infers, but not a
broad bacterial source.

### WikiPathways

**Element IDs:** good but curator-dependent. Each pathway has a `WP` accession;
GPML DataNodes and Interactions have graph IDs, and DataNodes carry Xrefs with
database names and identifiers that BridgeDb can map. The RDF release is split
into a direct GPML RDF translation and a harmonized WikiPathways RDF graph.

**Formats and endpoints:** monthly GPML, GMT, RDF, and SVG archives. The
September 2026 GPML release already contains organism-specific bundles for
Acetobacterium woodii, Bacillus subtilis, Escherichia coli, Mycobacterium
tuberculosis, Saccharomyces cerevisiae, and a few other microbial or fungal
species.

**Curation stance:** best permissive pathway-diagram test source. The official
data-release repository is CC0, and GPML/RDF can seed participants and
interactions. Expect to reject or patch records with unlabeled visual elements
or weakly typed interactions.

### PathBank

**Element IDs:** good for small molecules and proteins. The downloads include a
pathways CSV, metabolite-to-pathway CSV with KEGG and ChEBI IDs, protein-to-
pathway CSV with UniProt IDs, and full pathway archives in BioPAX, SBGN, SBML,
PWML, RXN, and structure/sequence files.

**Formats and endpoints:** bulk downloads from PathBank. The visible archive is
useful but older: many downloadable files were generated in 2019 or 2020.

**Curation stance:** add as disabled. PathBank covers model organisms such as
E. coli and yeast and could exercise BioPAX/SBML importers with pathway-element
IDs, but its model-organism focus overlaps Reactome/WikiPathways and the About
page needs a legal read before redistribution because it states both Open
Database License availability and an explicit-permission requirement for
commercial redistribution.

### MIBiG

**Element IDs:** good for gene clusters, weaker for reaction chains. MIBiG JSON
records have stable BGC accessions; a downloadable GBK sequence for each BGC;
FASTA translations of genes in MIBiG entries; product metadata; publications;
and JSON schema files.

**Formats and endpoints:** versioned JSON, GBK, and protein FASTA downloads.

**Curation stance:** use for secondary-metabolite records when PathwayMech gets
BGC-shaped fields. MIBiG records are experimentally anchored and CC BY 4.0, but
they usually do not enumerate every elementary Rhea-like transformation in a
biosynthetic route.

### ModelSEED, BiGG, and BV-BRC

These are supporting sources, not primary topology sources.

ModelSEED has strong reaction and compound IDs, structured reaction equations,
and reaction/compound aliases to sources such as KEGG and MetaCyc, but its own
Biochemistry README says the `Pathways` directory was intended for subsystems
and external sources and was not maintained.

BiGG exposes model, reaction, metabolite, and gene IDs through JSON/SBML/MAT
downloads and API routes, with database links out to resources such as KEGG,
MetaCyc, NCBI Entrez Gene, and SGD on element detail responses. Its
model-specific reactions have gene-reaction rules and compartments, not curated
pathway definitions.

BV-BRC Pathways and Subsystems rows connect genomes, genes, EC numbers, and
KEGG pathway IDs for organism-specific membership calls. Use them to find
candidate organisms or to check genome support for a curated pathway, not to
define the pathway's topology.

## Deferred aggregators

| Resource | Decision |
| --- | --- |
| Pathway Commons | Useful BioPAX integration and API across Reactome, WikiPathways, BioCyc, and other sources, but not canonical for curation because source licensing and source-specific semantics need to be handled before import. |
| MetaNetX / MNXref | Excellent reaction and metabolite reconciliation layer, but not a pathway-topology source. |
| BioModels | Rich SBML archive with identifiers, but publication-scale kinetic or constraint models are not normalized pathway definitions. |

## Immediate recommendations

1. **Prototype GO-CAM first.** It has the cleanest open causal graph:
   `Activity` nodes, RO causal predicates, GO molecular functions, NCBITaxon
   taxa, CHEBI or UniProtKB molecule nodes, and evidence items are already
   explicit in JSON.
2. **Prototype WikiPathways next.** It exercises visual GPML/RDF parsing and
   Xref mapping under a permissive source, using small microbial species
   bundles before touching mammalian bulk.
3. **Build a Rhea lookup in parallel.** Rhea is not a pathway source, but it is
   the open reaction normalization target for ChEBI-grounded biochemical
   reactions.
4. **Keep MetaCyc and KEGG as licensed importers.** Both are stronger than the
   open sources for microbial metabolism but need license-gated local extractors
   and review of what can be committed.
5. **Use Reactome and PathBank as BioPAX/SBML fixtures.** They have excellent
   per-element IDs, but their microbial coverage is narrower than BioCyc or
   KEGG.

## Source pages checked

| Source | Data endpoint or schema | License/access endpoint |
| --- | --- | --- |
| BioCyc / Pathway Tools | https://pathwaytools.org/flatfile-format.html | https://bioinformatics.ai.sri.com/ptools/licensing/all-reg.shtml |
| KEGG KGML | https://www.kegg.jp/kegg/xml/docs/ | https://www.genome.jp/kegg/legal.html |
| KEGG REST / FTP | https://www.kegg.jp/kegg/rest/ | https://www.genome.jp/kegg/download/ |
| GO-CAM | https://geneontology.org/docs/download-go-cams/ | https://geneontology.org/docs/go-citation-policy/ |
| GO-CAM LinkML schema | https://geneontology.github.io/gocam-py/ | https://github.com/geneontology/gocam-py |
| Reactome | https://reactome.org/download-data | https://reactome.org/download/current/ |
| WikiPathways GPML | https://data.wikipathways.org/current/gpml/ | https://github.com/wikipathways/wikipathways-data-release |
| WikiPathways RDF | https://data.wikipathways.org/current/rdf/ | https://vocabularies.wikipathways.org/gpml |
| PathBank | https://pathbank.org/downloads | https://pathbank.org/about/ |
| MIBiG | https://mibig.secondarymetabolites.org/download | https://mibig.secondarymetabolites.org/ |
| ModelSEED | https://github.com/ModelSEED/ModelSEEDDatabase/tree/master/Biochemistry | https://github.com/ModelSEED/ModelSEEDDatabase |
| BiGG | https://bigg.ucsd.edu/data_access | https://bigg.ucsd.edu/license |

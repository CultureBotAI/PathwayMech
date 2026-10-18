# Pathway element identifier source discovery

Updated: 2026-10-17

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
| 0 | MetaCyc / BioCyc | Pathway, reaction, enzymatic-reaction, compound, protein, gene, species, DBLINKS, PubMed-linked evidence codes | Best curated metabolic topology (140 maintained records), with licensing review before redistribution |
| 0 | KEGG KGML / MODULE | Pathway-map and module entries with KEGG compound, glycan, reaction, KO, EC, and organism-gene identifiers | High-coverage reference maps and modules (3 maintained records), license-gated |
| 0 | GO-CAM JSON | GO molecular activities, RO causal predicates, UniProtKB/GO enablers, CHEBI/UniProtKB molecules, NCBITaxon taxa, ECO/PMID evidence | Open causal activity graphs (86 maintained `gomodel:*` records); strongest shape match for PathwayMech edges |
| 1 | GO ontology | `GO:*` biological-process and molecular-function terms paired with GO-CAM or Rhea reaction steps | Canonical process anchors for pathways without standalone external pathway accessions (10 maintained `GO:*` records) |
| 1 | Reactome BioPAX/SBML | Reactome stable IDs for events and entities plus ChEBI, UniProt, Ensembl, NCBI, GO, KEGG, PubMed mappings | Rich BioPAX reaction graphs (6 maintained *M. tuberculosis* records), though microbial scope is narrow |
| 1 | WikiPathways GPML/RDF | WikiPathways IDs and BridgeDb-backed Xrefs on GPML data nodes; RDF exports direct and harmonized pathway content | Open parser fixture and curated small microbial set (12 maintained `WikiPathways:WP*` records) |
| 1 | PathBank BioPAX/SBML/PWML | PathBank `SMP*` IDs plus ChEBI/KEGG metabolite links, UniProt protein links, and BioPAX reaction/entity IDs | Active model-organism BioPAX source (9 maintained *E. coli* records), with public-release licensing tracked separately |
| 2 | MIBiG JSON/GBK | BGC accessions, GenBank regions, genes/protein translations, products, publications | Secondary-metabolite/BGC records (3 maintained `mibig:BGC*` records), not elementary reaction chains |
| 2 | Rhea | Rhea reaction IDs, ChEBI participants (`RHEA-COMP` polymers), EC, UniProtKB, GO xrefs | Normalize reactions after a pathway source proposes them (`support`) |
| 3 | ModelSEED / BiGG / BV-BRC / VEuPathDB | Reaction, compound, gene, genome, model, eukaryotic organism, or KEGG/MetaCyc pathway membership IDs | Crosswalks and organism membership evidence (`support`), not canonical pathway definitions |
| 3 | PMN / ChlamyCyc | Pathway Tools frame IDs for microalgal pathways, reactions, compounds, enzymes, and genes | Algal metabolic topology (`license-gated` under academic/commercial tiered terms) |
| 3 | GapMind / DRAM / HADEG / SEED | Enzyme-step rules, KO/EC module coordinates, degradation gene rows, and subsystem role variants | Variant, module, and enzyme triage (`support`), not standalone pathway graphs |
| 3 | BRENDA / dbCAN-PUL | Reaction-component role assertions (`CC BY 4.0` official text/JSON and SPARQL JSON bundles) and characterized `PUL####` glycan loci | Reaction-context and glycan-locus support layers (`support`) |
| 3 | UniPathway | Legacy UPA pathway, subpathway, enzymatic-reaction, reaction, and compound terms with Rhea, MetaCyc, KEGG, GO, EC, and ChEBI xrefs | Crosswalk source for retired UniProt pathway annotation terms (`support`) |

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
and Pathway Tools web services (including bounded `getxml` endpoints validated
through `metacyc-pathway-xml`, `metacyc-reaction-xml`, `metacyc-protein-xml`,
`metacyc-compound-xml`, and related Pathway Tools XML kinds on the ArtSymbioCyc
mirror, plus `metacyc-sgd-pathway-xml`).

**Curation stance:** best source for curated microbial metabolism (140
maintained `MetaCyc:*` records). Native MetaCyc frame IDs are stable enough to
store as source IDs, and DBLINKS can ground compounds, proteins, and genes. Use
only under an explicit BioCyc license because most BioCyc PGDBs are Limited
Databases.

### KEGG PATHWAY / MODULE / KGML

**Element IDs:** very good, but KEGG-native. KGML entries identify ortholog,
enzyme, reaction, compound, glycan, map, group, and organism-gene nodes with
KEGG IDs, and `reaction` elements identify KEGG `rn:` reactions with
`substrate` and `product` children named by KEGG `cpd:` or `gl:` accessions.
Reference maps can be projected through `ko`, `rn`, or `ec` maps, and
organism-specific maps replace the reference boxes with KEGG gene IDs.

**Formats and endpoints:** KGML and flatfiles from the KEGG REST API for
individual maps and modules (`kegg-module-flatfile`, `kegg-reaction-flatfile`,
`kegg-compound-flatfile`, `kegg-gene-flatfile`, `kegg-pseudogene-flatfile`);
full weekly FTP for academic subscribers; REST `link` and `conv` calls for
selected outside identifiers.

**Curation stance:** keep as an enabled grounding source (3 maintained
`kegg.module:*` records: `M00001`, `M00165`, `M00357`), but do not build a
redistributable bulk importer without a license. KGML has pathway element IDs,
but those IDs are KEGG IDs; mapping to Rhea, ChEBI, GO, UniProtKB, and EC needs
explicit curation or an approved crosswalk.

### GO-CAM and GO Ontology

**Element IDs:** excellent for causal activity graphs. The LinkML schema models
GO-CAMs as `Model` objects that contain `Activity` nodes. Activities carry GO
molecular-function terms, `enabled_by` associations to individual gene products
or protein complexes, molecular associations to CHEBI or UniProtKB terms,
GO cellular locations, GO biological-process `part_of` links, NCBITaxon model
taxa, RO causal predicates between activities, and ECO/publication evidence.

**Formats and endpoints:** versioned GO-CAM JSON downloads, one file per model;
GO API routes for model ID, taxon, and PMID lookup; the `gocam-py` package
validates the same LinkML-defined JSON representation.

**Curation stance:** primary open causal-activity importer (86 maintained
`gomodel:*` records including SGD `YeastPathways_*` and `SYN_GO_*` models). GO
data products are CC BY 4.0, and PomBase *S. pombe* GO-CAMs normalize under the
same `go-cam` source. Alongside `go-cam`, the `go` ontology entry (`priority: 90`,
`active`) anchors 10 maintained `GO:*` biological-process pathway definitions when
paired with GO-CAM or Rhea reaction steps.

### Reactome

**Element IDs:** excellent inside its scope. Reactome assigns stable IDs to
pathways, reactions, and physical entities, and its downloads include
BioPAX level 3 (BioPAX level 2 and Protégé 2.0 were retired in V94), all-species
SBML, the GraphDB dump, stable-id tables, reaction to PMID mappings, and
ChEBI/UniProt/NCBI/Ensembl mappings down to reaction or pathway levels.

**Formats and endpoints:** BioPAX 3, SBML, GraphDB, MySQL dumps, Content Service
API, and tabular mapping files from the current download directory.

**Curation stance:** valuable for BioPAX/SBML parser work and for the microbial
species Reactome curates (6 maintained *M. tuberculosis* records), but not a
broad bacterial source.

### WikiPathways

**Element IDs:** good but curator-dependent. Each pathway has a `WP` accession;
GPML DataNodes and Interactions have graph IDs, and DataNodes carry Xrefs with
database names and identifiers that BridgeDb can map. The RDF release is split
into a direct GPML RDF translation and a harmonized WikiPathways RDF graph.

**Formats and endpoints:** monthly GPML, GMT, RDF, and SVG archives. Both the
September 2026 (`20260910`) and October 2026 (`20261010`) GPML releases contain
organism-specific bundles for *Acetobacterium woodii*, *Bacillus subtilis*,
*Escherichia coli*, *Mycobacterium tuberculosis*, *Saccharomyces cerevisiae*,
and other microbial or fungal species.

**Curation stance:** best permissive pathway-diagram source (12 maintained
`WikiPathways:WP*` records). The official data-release repository is CC0, and
GPML/RDF can seed participants and interactions. Expect to reject or patch
records with unlabeled visual elements or weakly typed interactions.

### PathBank

**Element IDs:** good for small molecules and proteins. The downloads include a
pathways CSV, metabolite-to-pathway CSV with KEGG and ChEBI IDs, protein-to-
pathway CSV with UniProt IDs, and full pathway archives in BioPAX, SBGN, SBML,
PWML, RXN, and structure/sequence files.

**Formats and endpoints:** bulk downloads from PathBank
(`pathbank_primary_biopax.zip` validated via `pathbank-biopax`,
`pathbank-context-biopax`, and `pathbank-biopax-zip` authority profiles).

**Curation stance:** enabled as `active` in `conf/sources.yaml` with 9
maintained *Escherichia coli* `PathBank:SMP*` records (`SMP0002038`, `SMP0002051`,
`SMP0002067`, `SMP0002077`, `SMP0002083`, `SMP0002089`, `SMP0002097`,
`SMP0002123`, `SMP0002406`), each backed by primary literature and verified
native BioPAX identifiers. Public-release redistribution terms (`CC BY-NC 4.0`
on the downloads page; `ODbL` plus commercial-permission language on the About
page) remain tracked for release review.

### MIBiG

**Element IDs:** good for gene clusters, weaker for reaction chains. MIBiG JSON
records have stable BGC accessions; a downloadable GBK sequence for each BGC;
FASTA translations of genes in MIBiG entries; product metadata; publications;
and JSON schema files.

**Formats and endpoints:** versioned JSON, GBK, and protein FASTA downloads.

**Curation stance:** active source for secondary-metabolite records (3
maintained records: `BGC0002072`, `BGC0000852`, `BGC0000829`). MIBiG records are
experimentally anchored and CC BY 4.0, using `gene_clusters` when elementary
Rhea reactions are not enumerated.

### ModelSEED, BiGG, BV-BRC, PMN / ChlamyCyc, and VEuPathDB

These are supporting or license-gated organism-context sources rather than
standalone open pathway-topology authorities.

ModelSEED (`priority: 100`, `support`) has strong reaction and compound IDs,
structured reaction equations, and reaction/compound aliases to sources such as
KEGG and MetaCyc, but its own Biochemistry README says the `Pathways` directory
was intended for subsystems and external sources and was not maintained.

BiGG (`priority: 110`, `support`) exposes model, reaction, metabolite, and gene
IDs through JSON/SBML/MAT downloads and API routes
(`bigg-universal-metabolite-json` and `bigg-universal-reaction-json`), with
database links out to resources such as KEGG, MetaCyc, NCBI Entrez Gene, and
SGD on element detail responses. Its model-specific reactions have gene-reaction
rules and compartments, not curated pathway definitions.

BV-BRC (`priority: 120`, `support`) Pathways and Subsystems rows connect
genomes, genes, EC numbers, and KEGG pathway IDs for organism-specific
membership calls. Use them to find candidate organisms or to check genome
support for a curated pathway, not to define the pathway's topology.

Plant Metabolic Network / ChlamyCyc (`pmn`, `priority: 130`, `license-gated`)
exposes Pathway Tools metabolic pathway, reaction, compound, enzyme, and gene
frames for *Chlamydomonas reinhardtii* and other green algae, but remains
disabled under PMN/Phoenix Bioinformatics tiered academic and commercial terms.

VEuPathDB (`veupathdb`, `priority: 140`, `support`) indexes eukaryotic microbe
and protist metabolic pathways (FungiDB, PlasmoDB, ToxoDB, TriTrypDB, GiardiaDB,
CryptoDB, AmoebaDB, MicrosporidiaDB) projected onto MetaCyc, KEGG, and Reactome
identifiers; `pathwaymech-import-veupathdb` ingests local VEuPathDB summary
exports as `support` triage rows while keeping canonical pathway IDs on the
underlying authorities.

### GapMind

GapMind (`priority: 150`, `support`) encodes bacterial and archaeal amino-acid
biosynthesis and small-carbon catabolism as local `*.steps` rule files. Step
rows can carry EC numbers, UniProt exemplars, MetaCyc monomer IDs, TIGRFAM HMM
IDs, and PaperBLAST curation tags, while `all:` or subpathway rows describe
alternative groups of steps for a complete route.

Those rule files are excellent at showing which enzyme variants GapMind checks
when it evaluates a genome. They are weaker as direct PathwayMech definitions:
their local rule slugs are not stable external pathway CURIEs, transporter and
protein-complex rows may not be single biochemical reactions, and the
PaperBLAST repository is GPL-3.0. Keep `pathwaymech-import-gapmind` as
support-only seed rows for finding EC, UniProtKB, MetaCyc, and HMM hints during
manual curation.

### UniPathway

UniPathway (`priority: 160`, `support`) preserves retired UPA OBO pathway,
linear subpathway, enzymatic-reaction, reaction, and compound terms as `UPa:*`
IDs. UCR and UER terms carry part-of and input/output compound relationships
plus Rhea, MetaCyc, KEGG, GO, EC, ChEBI, and PMID cross-references, so the OBO
can still help reviewers connect a legacy UniProt pathway annotation to a modern
Rhea or MetaCyc reaction.

That reuse should stay support-only. The README says UniPathway is inactive
and its reactions have already been incorporated into Rhea; the repository is
licensed as CC-BY only in `src/metadata/upa.md`; and native `UPa` CURIEs remain
outside the PathwayMech curated-record schema. `pathwaymech-import-unipathway`
therefore indexes OBO crosswalk rows from a local UPA file instead of promoting
retired UPA pathways to first-class YAML record IDs.

## Additional candidates checked

Five specialist sources (`dbcan-pul`, `seed-pubseed`, `brenda`, `hadeg`, and
`dram`) have implemented `support` adapters in `conf/sources.yaml`:

- `dbCAN-PUL` (`priority: 170`) and `PULDB` (`priority: 190`, `deferred`)
  identify polysaccharide-utilization loci (`PUL####`) and CAZyme-containing
  gene clusters connected to substrates, EC numbers, and protein accessions.
  PathwayMech parses local dbCAN-PUL workbook metadata for support triage, while
  keeping PUL records out of first-class YAML until bulk reuse terms are clear.
- `SEED / PubSEED Subsystems` (`priority: 200`), `BRENDA` (`priority: 250`,
  official text/JSON download and pinned local SPARQL JSON bundles under `CC BY 4.0`,
  indexed via `pathwaymech-import-brenda`), `HADEG` (`priority: 260`), and
  `DRAM` (`priority: 280`, indexed via `pathwaymech-import-dram`) provide
  provenance-pinned subsystem role variants, reaction-component assertions,
  hydrocarbon degradation gene memberships, and KEGG-derived module step
  coordinates as `support` layers.
- `MicroScope / MicroCyc` (`microscope-microcyc`, `priority: 210`, `deferred`),
  `JGI IMG/M and IMG-ABC` (`jgi-img-abc`, `priority: 220`, `license-gated`), and
  `AlgaePath` (`algaepath`, `priority: 240`, `deferred`) remain disabled because
  their organism-specific Pathway Tools, IMG pathway/BGC, or KEGG-derived algal
  transcriptomics views either duplicate upstream authorities or require portal
  terms review.
- `enviPath` (`priority: 270`, `license-gated`), `DiTing` (`priority: 290`,
  `deferred`), and `METABOLIC` (`priority: 300`, `license-gated`) remain
  disabled due to extraction/redistribution restrictions or KO-formula-only
  granularity.
- The October 17 refresh adds three deferred candidates with strong element
  identifiers:
  1. `gutSMASH` (`gutsmash`, `priority: 310`, `deferred`): primary anaerobic
     bacterial metabolic gene clusters (SCFA, Stickland fermentation, TMA,
     microcompartments, Rnf/Ech respiratory complexes; AGPL-3.0) with GenBank
     loci and domain rules complementing `mibig`.
  2. `Mechanism and Catalytic Site Atlas (M-CSA)` (`m-csa`, `priority: 320`,
     `deferred`): EMBL-EBI `CC BY 4.0` enzyme reaction mechanisms grounded in
     `EC`, `RHEA`, `CHEBI`, `UniProtKB`, and `PDB` catalytic residues, directly
     aligned with PathwayMech's `reaction_mechanisms` schema.
  3. `Virtual Metabolic Human / AGORA2` (`vmh-agora2`, `priority: 330`,
     `deferred`): >7,300 strain-level gut bacterial, archaeal, and fungal SBML
     reconstructions (`MIT` license) with VMH reaction/metabolite cross-references
     to `BiGG`, `KEGG`, `MetaCyc`, and `CHEBI`.

PANTHER Pathway (`priority: 180`, `fixture`) and ECMDB (`priority: 230`,
`deferred`) are technically parseable pathway resources with component
identifiers, but neither fills an uncovered microbial curation gap.

## Deferred aggregators

| Resource | Decision |
| --- | --- |
| Pathway Commons | Useful BioPAX integration and API across Reactome, WikiPathways, BioCyc, and other sources, but not canonical for curation because source licensing and source-specific semantics need to be handled before import. |
| MetaNetX / MNXref | Excellent reaction and metabolite reconciliation layer (`metanetx.chemical`), but not a pathway-topology source. |
| BioModels | Rich SBML archive with identifiers, but publication-scale kinetic or constraint models are not normalized pathway definitions. |

## Immediate recommendations

1. **Prioritize active causal and pathway sources (`go-cam`, `wikipathways`,
   `mibig`, `reactome`, `pathbank`, `go`)** enriched by all 12 enabled `support`
   sources (`rhea`, `modelseed`, `bigg`, `bv-brc`, `veupathdb`, `gapmind`,
   `unipathway`, `dbcan-pul`, `seed-pubseed`, `brenda`, `hadeg`, `dram`).
2. **Prototype `m-csa` and `gutsmash` next when adding new adapters:** `m-csa`
   (`CC BY 4.0`) provides step-by-step catalytic mechanisms grounded in `RHEA`,
   `EC`, `CHEBI`, and `UniProtKB` for `reaction_mechanisms`, while `gutsmash`
   (`AGPL-3.0`) covers primary anaerobic metabolic gene clusters missing from
   `mibig`.
3. **Keep MetaCyc, KEGG, and PMN/ChlamyCyc behind licensed/bounded local
   extractors** with explicit provenance and license tracking.

## Source pages checked

| Source | Data endpoint or schema | License/access endpoint |
| --- | --- | --- |
| BioCyc / Pathway Tools | https://pathwaytools.org/flatfile-format.html | https://bioinformatics.ai.sri.com/ptools/licensing/all-reg.shtml |
| KEGG KGML | https://www.kegg.jp/kegg/xml/docs/ | https://www.genome.jp/kegg/legal.html |
| KEGG REST / FTP | https://www.kegg.jp/kegg/rest/ | https://www.genome.jp/kegg/download/ |
| Rhea | https://www.rhea-db.org/help/download | https://www.rhea-db.org/help/license |
| GO-CAM | https://geneontology.org/docs/download-go-cams/ | https://geneontology.org/docs/go-citation-policy/ |
| GO-CAM LinkML schema | https://geneontology.github.io/gocam-py/ | https://github.com/geneontology/gocam-py |
| GO ontology | https://geneontology.org/docs/download-ontology/ | https://geneontology.org/docs/go-citation-policy/ |
| Reactome | https://reactome.org/download-data | https://reactome.org/download/current/ |
| WikiPathways GPML | https://data.wikipathways.org/current/gpml/ | https://github.com/wikipathways/wikipathways-data-release |
| WikiPathways RDF | https://data.wikipathways.org/current/rdf/ | https://vocabularies.wikipathways.org/gpml |
| PathBank | https://pathbank.org/downloads | https://pathbank.org/about/ |
| MIBiG | https://mibig.secondarymetabolites.org/download | https://mibig.secondarymetabolites.org/ |
| ModelSEED | https://github.com/ModelSEED/ModelSEEDDatabase/tree/master/Biochemistry | https://github.com/ModelSEED/ModelSEEDDatabase |
| BiGG | https://bigg.ucsd.edu/data_access | https://bigg.ucsd.edu/license |
| BV-BRC | https://www.bv-brc.org/ | https://www.bv-brc.org/docs/ |
| Plant Metabolic Network / ChlamyCyc | https://www.plantcyc.org/ | https://www.plantcyc.org/about/licensing |
| VEuPathDB | https://veupathdb.org/veupathdb/app | https://veupathdb.org/veupathdb/app/static-content/about.html |
| GapMind | https://github.com/morgannprice/PaperBLAST/tree/master/gaps | https://github.com/morgannprice/PaperBLAST/blob/master/LICENSE |
| UniPathway | https://github.com/geneontology/unipathway | https://github.com/geneontology/unipathway/blob/master/src/metadata/upa.md |
| dbCAN-PUL | https://pro.unl.edu/dbCAN_PUL/dbCAN_PUL/home | https://pro.unl.edu/dbCAN_PUL/dbCAN_PUL/home |
| PULDB | https://www.cazymodo.org/PULDB/ | https://www.cazymodo.org/PULDB/ |
| SEED / PubSEED | https://blog.theseed.org/servers/2010/08/downloading-a-subsystem.html | https://www.theseed.org/ |
| MicroScope / MicroCyc | https://microscope.readthedocs.io/en/latest/ | https://mage.genoscope.cns.fr/ |
| JGI IMG/M and IMG-ABC | https://img.jgi.doe.gov/ | https://jgi.doe.gov/user-programs/pmo-overview/policies/ |
| PANTHER Pathway | https://archive.pantherdb.org/downloads/index.jsp | https://pantherdb.org/ |
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

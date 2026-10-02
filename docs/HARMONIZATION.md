# Harmonization

PathwayMech harmonizes pathway, reaction, compound, protein, activity, cluster,
model, and pathway-call identifiers from GO, GO-CAM, WikiPathways, Rhea, MIBiG,
Reactome, PathBank, MetaCyc, KEGG, PMN, ModelSEED, BiGG, BV-BRC, ChEBI, LIPID
MAPS, CAS, ChemSpider, HMDB, PubChem, EC, UniProtKB, Ensembl, Entrez Gene,
NCBI Protein, TubercuList, and SGD records into a single pathway mechanism module.

Prefer stable external identifiers over local identifiers. Local identifiers
must be temporary and must be documented in `curation/decisions.tsv`.

GO-CAM ingestion keeps `gomodel` activity identifiers as draft reaction nodes
and preserves SGD and GO_REF CURIEs when the upstream model uses Saccharomyces
Genome Database gene products or GO evidence references.

WikiPathways GPML ingestion keeps the `WikiPathways` pathway ID and interaction
graph IDs in draft reaction CURIEs. DataNodes are imported only when their Xref
database can be mapped to a supported biological CURIE, including native
LIPIDMAPS, CAS, ChemSpider, HMDB, PubChem, Ensembl, Entrez, NCBIProtein, and
TubercuList accessions that do not yet have a checked ChEBI, Rhea, or UniProtKB
mapping.

When a ChEBI cross-reference normalizes a WikiPathways GPML or KEGG KGML
chemical accession to a final ChEBI CURIE, draft records retain a
`source_mappings` row with the original source CURIE, both labels, the exact
match predicate, and the source pathway and element context needed for SSSOM
export.

Rhea TSV ingestion extracts RHEA reaction IDs, ChEBI participants, EC numbers,
GO molecular functions, and KEGG or MetaCyc reaction crosswalks for importers
that need an open biochemical reaction normalization layer.

MIBiG JSON ingestion extracts BGC accessions, products, genes, loci, and PubMed
references as seed rows or as BGC-shaped draft YAML records whose
`gene_clusters` preserve MIBiG products, biosynthetic classes, local genes, and
GenBank loci separately from ChEBI/Rhea reaction graphs.

Reactome and PathBank BioPAX ingestion share an importer that reads BioPAX
biochemical reactions, grounds reaction-side small molecules through ChEBI, and
grounds enzyme catalysts through UniProtKB `Catalysis` controllers. Reactome
BioPAX ingestion also preserves pathway and reaction stable identifiers, taxa
from `BioSource` nodes, and reaction-scoped PubMed evidence without allowing
long BioPAX comments to exceed the local evidence-quote limit.
BioPAX prefix normalizations such as `UniProt` to `UniProtKB` are retained as
the same `source_mappings` rows when the normalized participant remains in the
draft mechanism graph.

MetaCyc, PMN, and KEGG ingestion only read local, license-gated exports:
Pathway Tools `pathways.dat` files and KGML maps. PMN Pathway Tools records mint
`PMN` CURIEs so ChlamyCyc frame IDs remain separate from MetaCyc frame IDs.

GO, ModelSEED, BiGG, BV-BRC, VEuPathDB, GapMind, and UniPathway ingestion
provide grounding, reaction-alias, model-reaction, organism-specific pathway
membership, enzyme-rule, and legacy pathway crosswalk rows that support manual
review of drafts from primary pathway sources.

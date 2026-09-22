# Harmonization

PathwayMech harmonizes pathway, reaction, compound, protein, activity, cluster,
model, and pathway-call identifiers from GO, GO-CAM, WikiPathways, Rhea, MIBiG,
Reactome, PathBank, MetaCyc, KEGG, ModelSEED, BiGG, BV-BRC, ChEBI, UniProtKB,
and EC records into a single pathway mechanism module.

Prefer stable external identifiers over local identifiers. Local identifiers
must be temporary and must be documented in `curation/decisions.tsv`.

GO-CAM ingestion keeps `gomodel` activity identifiers as draft reaction nodes
and preserves SGD and GO_REF CURIEs when the upstream model uses Saccharomyces
Genome Database gene products or GO evidence references.

WikiPathways GPML ingestion keeps the `WikiPathways` pathway ID and interaction
graph IDs in draft reaction CURIEs. DataNodes are imported only when their Xref
database can be mapped to a supported biological CURIE.

Rhea TSV ingestion extracts RHEA reaction IDs, ChEBI participants, EC numbers,
GO molecular functions, and KEGG or MetaCyc reaction crosswalks for importers
that need an open biochemical reaction normalization layer.

MIBiG JSON ingestion extracts BGC accessions, products, genes, loci, and PubMed
references as seed rows until PathwayMech has a BGC-shaped curated YAML schema.

Reactome and PathBank BioPAX ingestion share a fixture importer that reads
BioPAX biochemical reactions and grounds physical entities through ChEBI,
UniProtKB, or GO xrefs.

MetaCyc and KEGG ingestion only read local, license-gated exports:
Pathway Tools `pathways.dat` files and KGML maps.

GO, ModelSEED, BiGG, and BV-BRC ingestion provide grounding, reaction-alias,
model-reaction, and genome-specific pathway membership rows that support
manual review of drafts from primary pathway sources.

# Harmonization

PathwayMech harmonizes pathway, reaction, compound, protein, activity, cluster,
model, and pathway-call identifiers from GO, GO-CAM, WikiPathways, Rhea, MIBiG,
Reactome, PathBank, MetaCyc, KEGG, PMN, ModelSEED, BiGG, BV-BRC, ChEBI, LIPID
MAPS, CAS, ChemSpider, HMDB, PubChem, EC, UniProtKB, Ensembl, Entrez Gene,
NCBI Protein, TubercuList, and SGD records into a single pathway mechanism module.

Prefer stable external identifiers. Preserve source-native instance identifiers
when a source distinguishes physical states or has no exact external grounding;
verify those instances against the source graph. Project-minted temporary
identifiers must be documented in `curation/decisions.tsv`.

The blocking [identifier and label gate](IDENTIFIERS.md) checks named pathway,
taxon, participant, and reaction IDs against independent authority snapshots.
Its explicit contextual-label policies preserve source display text while
still checking identifier existence.

GO-CAM ingestion keeps `gomodel` activity identifiers as draft reaction nodes
and preserves SGD and GO_REF CURIEs when the upstream model uses Saccharomyces
Genome Database gene products or GO evidence references.

WikiPathways GPML ingestion keeps the `WikiPathways` pathway ID and interaction
graph IDs in draft reaction CURIEs. DataNodes retain supported biological Xrefs, including native
LIPIDMAPS, CAS, ChemSpider, HMDB, PubChem, Ensembl, Entrez, NCBIProtein, and
TubercuList accessions that do not yet have a checked ChEBI, Rhea, or UniProtKB
mapping. Otherwise preserve an inspected DataNode's native pathway/GraphId
identity instead of guessing an external accession. Group membership does not
make each protein subunit an independent catalyst.

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

Reactome, PathBank, and PANTHER BioPAX ingestion share an importer that reads BioPAX
biochemical reactions, grounds reaction-side small molecules through ChEBI, and
grounds enzyme catalysts through UniProtKB `Catalysis` controllers. BioPAX
ingestion also preserves source pathway and reaction stable identifiers, taxa
from `BioSource` nodes, physical complexes and compartments, and explicit source
reaction directions. Structured assertions cite native BioPAX objects with
locators; a database comment is not a quotation from its cited PMID.
BioPAX prefix normalizations such as `UniProt` to `UniProtKB` are retained as
the same `source_mappings` rows when the normalized participant remains in the
draft mechanism graph.

MetaCyc, PMN, and KEGG ingestion only read local, license-gated exports:
Pathway Tools `pathways.dat` files and KGML maps. PMN requires `--pgdb` and mints
PathwayMech-scoped `PMN:<native-pgdb>:<native-frame>` identifiers for pathways,
reactions and references. Use the exact PGDB spelling from the export; these are
not upstream-global accessions. `--source-version` records the supplied export's
version, which must not be inferred from a newer portal page. Independent
identifier authorities are still required before promoting drafts to the corpus.

Both Pathway Tools importers accept repeatable `--pathway-id` to select exact
native frames from a full export and `--encoding latin-1` for explicitly known
Latin-1 files (default UTF-8, strict decoding). Every requested frame must occur
exactly once. All incoming `PREDECESSORS` branches retain indexed structured
evidence. Unsupported inherited or hierarchical ordering fails explicitly;
selection permits bounded elementary canaries without altering the source file.
For example, after obtaining an authorized export:

```bash
just import-pmn /path/to/pathways.dat --pgdb Chlamy \
  --source-version ACTUAL_EXPORT_VERSION --pathway-id VERIFIED_NATIVE_FRAME
```

GO, ModelSEED, BiGG, BV-BRC, VEuPathDB, GapMind, and UniPathway ingestion
provide grounding, reaction-alias, model-reaction, organism-specific pathway
membership, enzyme-rule, and legacy pathway crosswalk rows that support manual
review of drafts from primary pathway sources.

HADEG provides a separate source-reported membership layer. The local adapter
requires the full upstream commit and expected SHA-256, validates the entire
CSV before output, and preserves all nine raw source fields plus physical line
locators. Namespace candidates are lexical hints, always marked `not_verified`;
unresolved local, nucleotide, structure and other identifiers remain visible.
Membership does not imply reaction order, organism context, experimental support
or identifier equivalence. The adapter emits TSV support rows and no pathway
graphs. Source tables remain external under their observed upstream GPL terms.

```bash
just import-hadeg /path/to/7_All_pathways.csv \
  --source-commit 8f1ff8fb3b6452a0fd2667dc78686dced5cd4416 \
  --sha256 064ae7e094e0dc98dbd784378e110ffe0fe4c9fc86340061fa5e933bdc57dbe6
```

See the [HADEG/PMN canary assessment](../research/source_discovery/2026-10-08-hadeg-pmn-canaries.md)
for the four-member evidence audit, reproduction instructions and PMN access gate.

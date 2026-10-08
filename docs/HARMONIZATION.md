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
Support rows also retain native status, quality, completeness, retirement reasons
and successor links. Missing assessment fields remain blank; explicitly empty
retirement/link lists remain `[]`. Draft descriptions carry the supplied source
assessments without asserting experimental characterization. Retired entries
remain available for support audits but are refused by `--yaml`, including a
mixed request with active records; automatic drafting never redirects to a
successor. The [violacein audit](../research/source_discovery/2026-10-08-violacein-followup.md)
illustrates why a duplicate cluster lineage does not establish protein sequence
equivalence.

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

BRENDA support ingestion reads a local manifest, saved SPARQL role query and
its original JSON response. The manifest binds the exact query scope, endpoint,
retrieval time, row limit and both file hashes. Only the documented bounded
query shape is accepted; reaching its row limit is an error. This establishes
the scope and integrity of the supplied snapshot, not independent biological
validation or completeness of the whole BRENDA database.

```bash
just import-brenda research/source_discovery/2026-10-07-brenda-canary/role-import-manifest.json
```

TSV output preserves every query binding and its RDF term metadata alongside
native pathway, reaction, role and compound URIs. These remain support rows:
substrate/product roles do not establish physiological direction, coefficients,
reaction order, protein identity or organism-specific experimental support.
Role URIs may be reused by different reactions. The importer does not join
independent enzyme, organism and reference lists, equate web and RDF identifiers,
or emit PathwayRecord YAML. The RDF snapshot's release is unknown; the website's
release label must not be attached to it. See the
[native-context audit](../research/source_discovery/2026-10-08-brenda-context.md).

PathBank and dbCAN-PUL now have real-source local ingestion canaries. Their
`support` status describes local processing, not public-release clearance or
promotion into maintained pathway records. Current PathBank 2.0 data carry
CC BY-NC 4.0 terms. The
[rights review](../research/source_discovery/2026-10-08-pathbank-dbcan-rights.md)
distinguishes that database license from older About-page wording and from
software or article licenses. Public-release licensing is tracked separately
from the authorized local ingestion described below.

For a local BioPAX input, `--sha256` binds the parsed bytes to an expected
digest. `--source-url` and `--source-version` require that digest and one input
file; use the version text to identify an archive member when the URL identifies
the archive. The reference digest covers the parsed member bytes, not the ZIP.
All BioPAX CLI drafts record their input digest, including unpinned exploratory
imports; a computed digest alone does not authenticate the source.

```bash
just import-biopax PathBank /path/to/cache/PW000967.owl \
  --sha256 1a037aaf80b3cc99f6e6a2c45d60cebea0909cd7b5ee7c15e4f2acf885a8b611 \
  --source-url https://pathbank.org/downloads/pathbank_primary_biopax.zip \
  --source-version 'primary archive Last-Modified 2019-08-16; member PW000967.owl' \
  > /path/to/local-drafts/SMP0000983.yaml
```

PathBank's native SMPDB pathway xref supplies the `PathBank:SMP...` identifier;
the archive's `PW...` filename belongs to PathWhiz and is not substituted for it.
Known underscored direction values are normalized with the native spellings
retained in source evidence. This is a source-based draft requiring further
authority and biological review, not a maintained or experimentally verified
mechanism. See the [PathBank canary](../research/source_discovery/2026-10-08-pathbank-local.md).
PathBank drafting requires one native pathway, unambiguous supported organism
identity, and explicit reaction membership through its component or attached
step links. An unlinked reaction is an error rather than an inferred member.

For dbCAN-PUL, keep the workbook and complete support output in a local cache:

```bash
just import-dbcan-pul /path/to/cache/dbCAN-PUL_Feb-2025.xlsx \
  --sha256 9be758d08cdfd0e36de816819cbcecd04224e4db53a83866369594ecbf3df949 \
  --include-provenance > /path/to/local-support/dbcan-pul.tsv
```

The compact legacy columns remain a normalized lookup view. The provenance
columns preserve the source filename, full file hash, worksheet, physical row
and ordered original header/value pairs, including unknown or blank headers.
Use those original cells when reconciling old locus tags and multidomain
CAZyme annotations: the compact family list is not a protein/domain graph.
The prediction flag `cazymes_predicted_dbCAN2` is never a CAZyme family.
The [dbCAN-PUL canary](../research/source_discovery/2026-10-08-dbcan-local.md)
documents the complete 633-row workbook ingestion and its experimental scope.

DRAM1 module-step ingestion reads the pinned `data/module_step_form.tsv` as
annotation support. It preserves every native row, including duplicate rows,
blank cells and the full path coordinates, with file and physical-line provenance.
No row deduplication, chemical-name splitting or pathway-graph construction is
performed. Module, KO, reaction and compound strings remain source assertions;
they have not passed independent identifier approval. In particular, coordinates
and same-path KO groups do not establish physiological ordering or enzyme-complex
requirements. DRAM2 is a separate source version and is not covered by this table.

```bash
just import-dram /path/to/cache/module_step_form.tsv \
  --source-commit fe61d759303f30db058d5d505c448b28e41b03f1 \
  --sha256 55a803dcd7fa10ed05403b36c3aa89b19f007c3601dc60cb703c38828e89a4d9 \
  > /path/to/local-support/dram-module-steps.tsv
```

The [DRAM ingestion audit](../research/source_discovery/2026-10-08-dram-local.md)
records all 3,288 rows across 399 modules and the M00001 canary. The local data
bundle retains the original artifact and KEGG lineage for later public-release
review. Only support data are produced; no maintained pathway is added.

SEED / PubSEED subsystem ingestion accepts a local manifest covering five native
API responses: ordered roles (including auxiliary roles), genome variants with
role/feature cells, subsystem version, curator and description. The manifest
records each request, acquisition time and file hash. The loader validates the
entire bundle, including exact subsystem scope and role-name joins, before
emitting any output.

```bash
just import-seed-subsystems /path/to/cache/glyoxylate-manifest.json \
  > /path/to/local-support/glyoxylate-native.tsv
```

Support rows retain the original JSON values, duplicate role positions, native
genome and feature IDs, and variant strings. A role's spreadsheet position is
not reaction order; absent role cells and variant codes do not establish a
biological phenotype. Requests are acquired separately, so the bundle is not
an atomic database snapshot. The observed subsystem version is metadata from
its own response, not an independently verified release for every feature call.
The [SEED audit](../research/source_discovery/2026-10-08-seed-local.md) records the
glyoxylate-bypass canary and the rejected alanine bundle's unmatched role name.
No synonym is invented to force an inconsistent bundle through the importer.

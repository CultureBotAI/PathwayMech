# MetaCyc causal graph review

All 50 MetaCyc records were assessed against complete native pathway definitions,
including nested pathways, and independent reaction and protein authorities.
The machine-readable disposition for every record is in `metacyc-review.json`.
`metacyc-sources.json` records source URLs, versions, and artifact checksums;
`metacyc-identifiers.txt` supplies the identifiers needed by the authority gate.

The review used MetaCyc 22.5 XML from the public Saccharomyces Genome Database
Pathway Tools service, Rhea 139 RDF and direction mappings, ChEBI 255, GO
2026-07-26, ENZYME 02-Sep-2026, 48 PubMed records, and complete UniProt 2026_03
JSON for 168 independently selected reviewed proteins. The UniProt location
vocabulary independently maps SL-0086 to cytoplasm and SL-0039 to plasma membrane.

## Scientific dispositions

- Reconstructed all Rhea reaction sides from independent RDF, including redox
  carriers, water, protons, and other small molecules. Currency metabolite
  protonation conventions were retained; display wording alone was not used to
  change molecular identities.
- Replaced 20 bidirectional Rhea identifiers with explicit source-supported
  pathway directions. These encode selected pathway flow, not a claim that the
  enzyme cannot catalyze a reverse reaction. Each selection was compared with
  native MetaCyc left/right primaries and the pathway layout direction.
- Completed the glyoxylate cycle through citrate synthase, the two aconitase
  steps, and malate dehydrogenase. Added carbamoyl-phosphate synthesis to the
  native arginine biosynthesis route.
- Expanded combined steps in isoleucine, leucine, methionine, tryptophan, and
  arginine degradation V. Amino/enamine/imino intermediates, isopropylmaleate,
  isopropyl-oxosuccinate, indole, and carbamate now appear explicitly. The old net
  reactions are removed to avoid duplicate flux. Spontaneous substeps are not
  assigned to the upstream enzyme; independently annotated RidA activity is
  included where supported.
- Separated EC molecular activities from named proteins. Protein `enables`
  assertions require a matching catalytic reaction family or a specifically
  reviewed component reaction and stay within the record's taxon scope.
  Cofactors, locations, and metabolic feedback cite the exact protein annotation
  and preserve its evidence codes and qualifications.
- Confirmed the unusual bacterial AIR-carboxylase route in *Treponema denticola*
  using PMID:21548610; the old multi-organism MetaCyc taxonomic range alone would
  have incorrectly suggested changing this record.
- Excluded repaired-mutant IlvG P0DP90 from ordinary E. coli pathway assertions.
  Did not propagate the outdated ProB–ProA interaction/channeling requirement,
  contradicted by PMID:39514317. IlvD P05791 retains only the supported general
  iron–sulfur-cluster assignment because source statements disagree about cluster
  nuclearity. Tentative sodium/crystal-binding annotations for P00561/P00562 are
  explicitly excluded from `has_cofactor` edges.
- Removed Salmonella-only article-title evidence from the E. coli leucine enzyme
  edge. Other existing literature excerpts were retained only when their wording
  was verified in the retrieved title or abstract. A missing abstract match was
  not treated as proof that a quotation is absent from a paper's full text.
- Converted generated descriptions of structured facts into located source
  assertions. Genuine verified quotations remain distinct.

The native nested chorismate source also includes an optional generic
NAD(P)-dependent quinate/shikimate dehydrogenase alternative. Its disposition is
explicit: this E. coli record represents the specifically grounded NADPH/AroE
biosynthetic route and already includes the core shikimate intermediate.
No other native leaf reaction is left without a mapped step or a disposition.

Some consecutive reactions use anomer-specific compounds on one side and a
broader substrate class on the next. These source specificity differences are
recorded as ordering bridges rather than silently equating identifiers. Broad
`Bacteria` records retain molecular-activity classes. Narrow taxon scopes without
reviewed protein matches do not borrow proteins from broader or neighboring
taxa. No absent annotation is taken as evidence of cofactor independence.
DNA/RNA control elements and organelles are not added without a grounded entity
and a direct source-supported role in the maintained mechanism.

## Reproduction

The migration baseline is commit
`88744403c934a84828d373cfccb8cdaa7507ad77`. Run in an isolated checkout. Keep full
source downloads outside the repository. The source manifest gives the exact
requests and expected bytes; if a live endpoint has changed, use the retained
artifact matching its checksum, not a silently substituted release.

Recreate the source layout from the manifest:

1. Save each `metacyc` entry as `metacyc/<native-id>.xml`.
2. Save each `uniprot` batch as `uniprot/full/<batch>.json` and its manifest as
   `uniprot/full/manifest.json`. Save the two `uniprot_locations` records as
   `uniprot/SL-0086.json` and `uniprot/SL-0039.json`.
3. Save the PubMed requests as `metacyc-pubmed.xml` and
   `additional-pubmed.xml`. The first request's URL and hash also belong in
   `metacyc-pubmed.manifest.json`.
4. Download Rhea RDF, decompress it, and verify the manifest's
   `uncompressed_rdf` checksum. Save the direction TSV and ENZYME DAT unchanged.
   ChEBI and GO label databases use the Semantic SQL releases and checksum scope
   recorded in `data/identifier_authorities/ontology.json`.

```sh
python scripts/curate_metacyc_causal_graphs.py \
  --root /tmp/pathwaymech-reproduction \
  --baseline-ref 88744403c934a84828d373cfccb8cdaa7507ad77 \
  --rhea-rdf "$RHEA_RDF" --directions "$RHEA_DIRECTIONS" \
  --metacyc-dir "$SOURCES/metacyc" \
  --chebi-db "$CHEBI_DB" --go-db "$GO_DB" --enzyme-dat "$ENZYME_DAT" \
  --pubmed-xml "$SOURCES/metacyc-pubmed.xml" \
  --additional-pubmed-xml "$SOURCES/additional-pubmed.xml" \
  --uniprot-dir "$SOURCES/uniprot/full" \
  --report-dir /tmp/pathwaymech-reproduction-reports/metacyc
```

Prepare the isolated baseline checkout as described in
[the migration instructions](../../docs/CURATION_MIGRATIONS.md). This command
previews the changes. Add `--apply` only to publish the reviewed preview to that
checkout. Destination records must still match `--baseline-ref`; an explicit
revision does not bypass that guard. Use a fresh report directory to preserve
the original applied review and source ledgers.

Omit `--apply` for a source-backed review without writing pathway records.
The separate `audit_metacyc_causal_graphs.py` command verifies current reaction
sides without applying the migration. History records are created through the
repository's `new_history_record.py` scaffolder, not by inventing timestamps.

All 50 records passed native schema validation. The six dedicated regressions
cover cycle closure, exposed indole and imino intermediates, spontaneous steps,
mutant/cofactor exclusions, opposite valine feedback effects, and the bacterial
AIR-carboxylase evidence. Repository-wide identifier, rendering, export, and
closed-schema gates remain the responsibility of the complete corpus review.

## Per-record coverage

| Record | Reactions before → after | Protein annotations | Cofactor annotations | Locations |
| --- | ---: | ---: | ---: | ---: |
| MetaCyc:PWY-6543 | 2 → 2 | 3 | 2 | 0 |
| MetaCyc:PWY-6121 | 5 → 5 | 5 | 3 | 2 |
| MetaCyc:PWY-6122 | 5 → 5 | 5 | 3 | 2 |
| MetaCyc:PWY0-1312 | 2 → 2 | 2 | 2 | 2 |
| MetaCyc:ARO-PWY | 7 → 7 | 10 | 7 | 7 |
| MetaCyc:COA-PWY | 4 → 4 | 3 | 3 | 2 |
| MetaCyc:DARABCAT-PWY | 2 → 2 | 0 | 0 | 0 |
| MetaCyc:GALACTUROCAT-PWY | 5 → 5 | 0 | 0 | 0 |
| MetaCyc:GLUCARDEG-PWY | 5 → 5 | 0 | 0 | 0 |
| MetaCyc:XYLCAT-PWY | 2 → 2 | 2 | 1 | 1 |
| MetaCyc:P101-PWY | 5 → 5 | 4 | 2 | 1 |
| MetaCyc:RIBOSYN2-PWY | 9 → 9 | 8 | 12 | 1 |
| MetaCyc:GLUTATHIONESYN-PWY | 2 → 2 | 3 | 2 | 0 |
| MetaCyc:GLYCEROLMETAB-PWY | 2 → 2 | 0 | 0 | 0 |
| MetaCyc:GLYOXYLATE-BYPASS | 2 → 6 | 5 | 5 | 1 |
| MetaCyc:PWY-6123 | 6 → 6 | 5 | 0 | 0 |
| MetaCyc:PWY-6124 | 5 → 5 | 1 | 0 | 0 |
| MetaCyc:ARABCAT-PWY | 3 → 3 | 5 | 4 | 0 |
| MetaCyc:ARGSYN-PWY | 8 → 9 | 11 | 6 | 9 |
| MetaCyc:AST-PWY | 5 → 5 | 6 | 2 | 1 |
| MetaCyc:ARGDEG-III-PWY | 3 → 3 | 2 | 2 | 0 |
| MetaCyc:ARGDEGRAD-PWY | 3 → 4 | 2 | 0 | 2 |
| MetaCyc:CYSTSYN-PWY | 2 → 2 | 3 | 2 | 1 |
| MetaCyc:FUCCAT-PWY | 4 → 4 | 0 | 0 | 0 |
| MetaCyc:HISTSYN-PWY | 10 → 10 | 8 | 5 | 6 |
| MetaCyc:HOMOSERSYN-PWY | 3 → 3 | 4 | 0 | 0 |
| MetaCyc:ILEUSYN-PWY | 5 → 7 | 7 | 8 | 2 |
| MetaCyc:LEUSYN-PWY | 4 → 6 | 5 | 5 | 2 |
| MetaCyc:DAPLYSINESYN-PWY | 10 → 10 | 11 | 4 | 5 |
| MetaCyc:HOMOSER-METSYN-PWY | 5 → 7 | 5 | 4 | 3 |
| MetaCyc:GLUTORN-PWY | 5 → 5 | 5 | 4 | 5 |
| MetaCyc:PHESYN | 3 → 3 | 2 | 0 | 2 |
| MetaCyc:PROSYN-PWY | 4 → 4 | 3 | 0 | 3 |
| MetaCyc:RHAMCAT-PWY | 5 → 5 | 0 | 0 | 0 |
| MetaCyc:SERSYN-PWY | 3 → 3 | 3 | 5 | 1 |
| MetaCyc:HOMOSER-THRESYN-PWY | 2 → 2 | 2 | 1 | 1 |
| MetaCyc:TRPSYN-PWY | 5 → 6 | 5 | 2 | 0 |
| MetaCyc:TYRSYN | 3 → 3 | 2 | 0 | 2 |
| MetaCyc:VALSYN-PWY | 4 → 4 | 8 | 10 | 1 |
| MetaCyc:GLUAMCAT-PWY | 2 → 2 | 2 | 6 | 0 |
| MetaCyc:PYRIDNUCSYN-PWY | 6 → 6 | 0 | 0 | 0 |
| MetaCyc:PYRIDNUCSAL-PWY | 6 → 6 | 0 | 0 | 0 |
| MetaCyc:NONOXIPENT-PWY | 5 → 5 | 7 | 14 | 2 |
| MetaCyc:OXIDATIVEPENT-PWY | 3 → 3 | 3 | 0 | 0 |
| MetaCyc:PANTO-PWY | 4 → 4 | 4 | 4 | 4 |
| MetaCyc:PPGPPMET-PWY | 6 → 6 | 0 | 0 | 0 |
| MetaCyc:PYRIDOXSYN-PWY | 7 → 7 | 7 | 7 | 5 |
| MetaCyc:PLPSAL-PWY | 5 → 5 | 3 | 4 | 0 |
| MetaCyc:TRESYN-PWY | 2 → 2 | 2 | 4 | 0 |
| MetaCyc:PWY-5686 | 6 → 6 | 7 | 5 | 1 |

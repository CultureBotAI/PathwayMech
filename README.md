# PathwayMech

PathwayMech curates pathway-level microbial mechanisms as small YAML records
with explicit participants, reactions, causal edges, and reference-backed
evidence.

The repository follows the current Mech layout:

- `data/pathways/` contains curated pathway mechanism records.
- `conf/` declares source inventories and import configuration.
- `curation/` tracks curator decisions that are separate from generated data.
- `scripts/` contains entry points for validation, rendering, seeding, and QC.
- `src/pathwaymech/` contains reusable schema and IO code.
- `tests/` protects the curation contract.
- `pages/` contains the generated static browser.

The first PathwayMech contract ports the DisMech pattern of evidence modules
into a pathway-specific schema:

- every mechanistic edge must cite a local `references` entry;
- every evidence quote must be short enough for review;
- graph edge endpoints must resolve to the pathway itself, a participant, or a
  reaction in the same record;
- record identifiers must use explicit CURIE-style prefixes;
- static pages are generated from the same YAML records that feed QC.

## Quickstart

```bash
uv run pathwaymech-validate
uv run pathwaymech-validate-sources
uv run pathwaymech-check-provenance
uv run pathwaymech-import-bigg tests/fixtures/bigg/model.json
uv run pathwaymech-import-biopax Reactome tests/fixtures/biopax/R-TEST.owl
uv run pathwaymech-import-bvbrc tests/fixtures/bvbrc/pathways.tsv
uv run pathwaymech-import-gocam tests/fixtures/gocam/mini_model.json
uv run pathwaymech-import-go tests/fixtures/go/go.obo
uv run pathwaymech-import-kegg tests/fixtures/kegg/map00010.kgml
uv run pathwaymech-import-mibig tests/fixtures/mibig/BGC0000001.json
uv run pathwaymech-import-metacyc tests/fixtures/metacyc/pathways.dat
uv run pathwaymech-import-modelseed tests/fixtures/modelseed/reactions.tsv
uv run pathwaymech-import-rhea tests/fixtures/rhea/reactions.tsv
uv run pathwaymech-import-wikipathways tests/fixtures/wikipathways/WPTEST.gpml
uv run pathwaymech-render-pages
uv run pytest
```

Run the complete local gate with:

```bash
just validate
```

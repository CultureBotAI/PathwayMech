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
uv run pathwaymech-check-provenance
uv run pathwaymech-render-pages
uv run pytest
```

Run the complete local gate with:

```bash
just validate
```

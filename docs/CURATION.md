# Curation

Pathway records are YAML documents stored under `data/pathways/`.

Use one file per pathway and keep generated artifacts out of the curated YAML
files. Mechanistic assertions belong in `mechanistic_edges`; source-specific
normalization notes belong in `curation/decisions.tsv`.

Reusable pathway sources are ranked in `conf/sources.yaml`. Each source has a
numeric `priority` and an `ingest_status`; run `just seed` to emit the current
machine-readable ingest queue before promoting a new parser or bulk source.

Required review gates:

```bash
uv run pathwaymech-validate
uv run pathwaymech-validate-sources
uv run pathwaymech-check-provenance
uv run pathwaymech-deep-research-contract
uv run pytest
```

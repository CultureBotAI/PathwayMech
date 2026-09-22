# Curation

Pathway records are YAML documents stored under `data/pathways/`.

Use one file per pathway and keep generated artifacts out of the curated YAML
files. Mechanistic assertions belong in `mechanistic_edges`; source-specific
normalization notes belong in `curation/decisions.tsv`.

Required review gates:

```bash
uv run pathwaymech-validate
uv run pathwaymech-check-provenance
uv run pathwaymech-deep-research-contract
uv run pytest
```

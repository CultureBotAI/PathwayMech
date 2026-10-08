# DRAM1 local ingestion metadata

- `acquisition-manifest.json`: pinned URLs, branch observations, artifact sizes,
  digests, software-license metadata, and KEGG-derived data lineage.
- `local-import-audit.json`: independently measured native-table inventory and
  full-export cell/locator roundtrip checks.

Original acquisition files and `ingested-native.tsv` were processed under
`/private/tmp/pathwaymech-next-evidence/dram/`. The parent ingestion bundle
retains durable local copies. This directory commits metadata only.

Reproduce the support export using the exact acquired bytes:

```bash
just import-dram /path/to/module_step_form.tsv \
  --source-commit fe61d759303f30db058d5d505c448b28e41b03f1 \
  --sha256 55a803dcd7fa10ed05403b36c3aa89b19f007c3601dc60cb703c38828e89a4d9 \
  > /path/to/ingested-native.tsv
```

The output digest assumes the original basename `module_step_form.tsv`; renaming
the input changes its `source_file` provenance column and therefore the output
digest. No input-path directory is embedded. Each `source_row_id` is a local
SHA-256/line-range locator; `module` and `ko` retain native source strings.

Validation reads the source independently with Python's `csv.reader` and the
output with `csv.DictReader`, both with `delimiter="\t"` and `newline=""`.
For each row, compare all nine native columns, the ordered pairs decoded from
`native_fields_json`, the pinned source digest/commit, and physical line
start/end. The acquired snapshot has one physical line per data row, lines
2–3289. Its duplicate lines 1181 and 1184 must both be present.

The adapter does not implement upstream module coverage, split chemical names,
resolve native IDs, or infer reaction topology or experimental evidence.

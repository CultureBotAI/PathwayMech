# dbCAN-PUL acquisition and local import audit

This bundle contains source acquisition metadata, an independent inventory,
and a reproducible audit script. Original workbooks, HTML, full native-row
projections, and importer output remain in an external cache. There are no
redistributed source tables or new pathway records here.

- `acquisition-manifest.json`: original/final URLs, retrieval times, response
  metadata, byte lengths, SHA-256 digests, and external-retention scope.
- `workbook-inventory.json`: independently computed counts and source limits.
- `local-import-audit.json`: external export hash, size, shape, and verification
  result for the actual 633-row provenance export.
- `rebuild_inventory.py`: standard-library OOXML inspection, verification of
  all seven original artifacts, and optional complete export comparison.

Use a cache containing the exact files named by the acquisition manifest. The
working cache for this audit was
`/private/tmp/pathwaymech-pathbank-dbcan-evidence/dbcan`; any location is valid.
The original workspace's ignored durable bundle is
`reports/local_source_ingestion/2026-10-08-pathbank-dbcan`. Its
`dbcan/ingested-native.tsv` has the same pinned bytes as the acquisition cache's
`imported-with-provenance.tsv`; either path can be passed to `--export`.
Redownloads may differ, especially HTML. A checksum mismatch is a new snapshot,
not permission to silently replace the pinned manifest.

From the repository root:

```bash
DBCAN_CACHE=/path/to/external/dbcan-cache
python3 research/source_discovery/2026-10-08-dbcan-local/rebuild_inventory.py \
  "$DBCAN_CACHE" --check
.venv/bin/pathwaymech-import-dbcan-pul \
  "$DBCAN_CACHE/dbCAN-PUL_Feb-2025.xlsx" \
  --sha256 9be758d08cdfd0e36de816819cbcecd04224e4db53a83866369594ecbf3df949 \
  --include-provenance > "$DBCAN_CACHE/imported-with-provenance.tsv"
python3 research/source_discovery/2026-10-08-dbcan-local/rebuild_inventory.py \
  "$DBCAN_CACHE" --check --export "$DBCAN_CACHE/imported-with-provenance.tsv"
```

The comparison checks all 633 source IDs and every ordered header/value pair,
including the blank U column, without normalizing native strings. It also checks
the filename, digest, worksheet, and physical source row. It emits only a status
message; full source rows stay external. It does not validate biological
authority assignments or infer gene activities, pathway completeness, or
ordered reactions. See the [research report](../2026-10-08-dbcan-local.md) for
the bounded primary-paper handoff.

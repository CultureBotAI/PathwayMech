# Reproducing the HADEG Finnerty canary

This directory contains four source-membership observations with separate
identifier verification and biological assessments. It does not contain a
PathwayRecord or authorize a group-level taxon or causal edge.

- `finnerty-canary.json`: the bounded machine-readable result.
- `acquisition-manifest.json`: original artifact URLs, hashes, sizes, commit,
  and UTC retrieval times. The listed `path` values are relative to an external
  source cache, not files redistributed in this directory.
- `review-assessments.json`: manual claim-level assessments and licensing
  observations. These require scientific review; the builder does not infer
  them from citation presence, Swiss-Prot status, or accession shape.
- `rebuild_canary.py`: standard-library-only reproduction from original files.
- `THIRD_PARTY_NOTICES.md` and `GPL-3.0.txt`: retained upstream attribution and
  observed repository license.

Populate an external cache with the exact bytes named in the acquisition
manifest, preserving its relative paths. Original source URLs can change
their responses; a hash mismatch must trigger review of a new snapshot,
not silent replacement of the manifest hash. The builder has no network
access and does not retrieve or accept terms for any source.

From the repository root:

```bash
python research/source_discovery/canaries/hadeg/rebuild_canary.py \
  --cache-dir /path/to/hadeg-source-cache \
  --output /path/to/rebuilt-finnerty-canary.json
```

Compare the resulting JSON with `finnerty-canary.json`. Every raw source
artifact is hash-checked before output, the workbook is read directly from
its XLSX bytes, the four joins require matching accession/group/pathway/
subpathway/gene, and issuer accessions are checked independently. No unpinned
intermediate workbook conversion is needed. Primary-paper interpretations
remain the manually reviewed inputs recorded in `review-assessments.json`.

The inspection and disposition are documented in
[the batch report](../../2026-10-08-hadeg-pmn-canaries.md).

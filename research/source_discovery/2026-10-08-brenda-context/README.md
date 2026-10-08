# Reproduce the BRENDA context audit

This directory contains a derived audit, not a raw archive or a PathwayRecord.
The BRENDA source-derived facts retain attribution under
[CC BY 4.0](https://brenda-enzymes.org/license.php). Cite
[BRENDA 2026](https://doi.org/10.1093/nar/gkaf1113), PMID 41206471. The projection
selects and normalizes native cell text and exact RDF terms, adds issuer
identity checks and labels curator interpretations separately. Full HTML,
article text and original JSON responses remain external.

Place the ten original responses under a cache directory using the artifact
names in `acquisition-manifest.json`. Its exact URLs and SHA-256 values identify
the inspected bytes. Dynamic public pages may now differ: a mismatch is an
explicit failure, not permission to replace a pinned source silently. The
existing task cache is `/private/tmp/pathwaymech-brenda-next-evidence/brenda`.

From the repository root, with Python 3.11 or newer:

```bash
python research/source_discovery/2026-10-08-brenda-context/rebuild_canary.py \
  /path/to/cache --check
```

Without `--check`, the script writes the regenerated JSON to stdout. It verifies
every original response's size and checksum, verifies `scoped-triples.rq`
against the recorded query URL, extracts two exact HTML row/cell sets, and
selects 34 RDF triples from the 825-row bounded response. It also verifies the
exact UniProt accession, strain taxon and locus. These are provenance and
identity checks; `review-assessments.json` contains explicit human/agent review
decisions, including the independently read article's experimental limits.
The script does not automate those judgments.

The projection keeps the source's literal `ir` code at the scoped S/429165 row;
it does not apply irreversibility to I/3385, all EC 4.2.1.12 instances, or a
whole pathway. EC 4.1.2.14 has a source-encoding defect, so its bounded absence
check examines the exact ASCII sequence in all original bytes. No RDF enzyme
subject is joined to organism and reference lists.

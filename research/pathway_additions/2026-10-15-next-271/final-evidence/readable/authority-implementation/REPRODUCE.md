# Reproduction

Use the existing verified runtime; do not install or repair it. The actual source
checkout used here is `/private/tmp/pathwaymech-next-271-20261015`. `maintained/`
contains exact copies of the 175 released owned files; the complete existing
checkout supplies unchanged dependency modules. Bind those owners before a replay.

The additive helper calls the production source builder and unchanged ontology
`extract_terms` on accepted issuing rows, then asserts that the pinned baseline
objects and insertion order are unchanged. Its baseline snapshots and source
manifest are retained under `inputs/baseline/`. Run to a **new output directory**,
without `--integrate`, to preserve this frozen packet and maintained files:

```bash
PYTHONHASHSEED=271 /private/tmp/pathwaymech-next-263-verified-venv/bin/python -B \
  /private/tmp/pathwaymech-next-271-authority-implementation/build_additions.py \
  --output /private/tmp/pathwaymech-next-271-authority-replay-new
```

The public finite source CLI, from the exact worktree, is:

```bash
PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 \
  /private/tmp/pathwaymech-next-263-verified-venv/bin/python -B \
  scripts/build_source_identifier_snapshot.py \
  --manifest /private/tmp/pathwaymech-next-271-authority-implementation/results/proposed-source-manifest.json \
  --cache-dir /private/tmp/pathwaymech-next-271-authority-implementation/build-2/cache \
  --records /private/tmp/pathwaymech-next-271-authority-implementation/build-2/selection \
  --output /private/tmp/pathwaymech-next-271-native-delta-new.json
```

This 52-term selection contains identifiers only; labels come from source XML.
It is not a full historical source-cache rebuild. Do not use the finite manifest
against the full record corpus and assume that it owns the 17 prior terms.

Meaningful tests, from the worktree:

```bash
PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 \
  /private/tmp/pathwaymech-next-263-verified-venv/bin/python -B -m pytest -q \
  tests/test_acetate_methanogenesis_authority.py
```

Regression files were `test_methanogenesis_authority.py`,
`test_biocyc_carrier_authority.py`, `test_source_identifier_snapshot.py`,
`test_identifiers.py`, and `test_identifier_snapshot_builders.py`. Include
`PYTHONPATH` so subprocesses resolve the same checkout. Exact failed and successor
invocations/results are retained. Full-corpus test/validation gates belong to root.

The five taxonomy terms are projected from complete accepted selected statement
sets using the unmodified extractor. `NCBITaxon:2208` is an exact existing control;
source metadata remains pinned to the full external SQLite hash. The memory
table is a query projection, not a substitute whole ontology or a fabricated
new source hash. No fresh 14 GB cache rehash is part of this reproduction.

`collect_inputs.py`, `implement_adapter.py` and `verify_release.py` retain author
preparation steps. They are not commands to run inside a frozen packet: the first
two describe pre-integration inputs/generation, and the last writes review
receipts/copies. The released maintained code, rather than a pre-format generator
attempt, is authoritative. Unsuccessful prior script versions remain as `.txt`.

# Staphyloferrin A portable current-target replay

This is implementation preparation and one-record quality control. It is not independent scientific approval, canonical authority integration, or a whole-corpus gate. Frozen author and independent scientific inputs remain unchanged.

The helper requires explicit repository, YAML, source-manifest, source-projection, and new output paths. Original bodies are selected only from the manifest's digest-bound paths. A prepared external authority root is optional; its policy must equal the chosen repository policy byte for byte. The default authority root is the repository. The explicit RDKit interpreter must retain its virtualenv path, even when that path is a symlink.

The receipt and its `.artifacts` companion directory must not already exist and must lie outside the repository. They contain fresh native/Rhea/ChEBI chemistry, RDKit stereochemistry, isolated identifier validation, and KGX exports. All target evidence and reference metadata are compared without modifying the source projection. Source hashes, input hashes and modification metadata are checked. Existing output paths, stale projections, missing dependencies and changed original digests fail closed. No network fetch or source-file rewriting is performed.

Example invocation after root integrates the official authority sources:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src UV_NO_SYNC=1 \
UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache \
.venv/bin/python /private/tmp/pathwaymech-staphyloferrin-a-portable-replay-20261011/staphyloferrin-a-replay.py \
  --repo-root /private/tmp/pathwaymech-next-214-20261011 \
  --record /private/tmp/pathwaymech-next-214-20261011/data/pathways/staphyloferrin-a-biosynthesis.yaml \
  --source-manifest /private/tmp/pathwaymech-next-214-20261011/research/pathway_additions/2026-10-11-next-214/staphyloferrin-a-source-manifest.json \
  --source-projection /private/tmp/pathwaymech-next-214-20261011/research/pathway_additions/2026-10-11-next-214/staphyloferrin-a-source-projection.json \
  --stereo-python /private/tmp/pathwaymech-curation-uv-cache/archive-v0/kFu0y5KhWWeJTMGjryT1h/bin/python3 \
  --output /private/tmp/unique-staphyloferrin-a-current-replay.json
```

Preparation before shared integration used the explicitly qualified `prepared-current-policy-authority-v2` external sandbox. It preserves the current baseline rows and appends only absent author-prepared issued terms. Existing ChEBI label/synonym assertions are identical; their older author-specific source keys are retained only in the preparation comparison, while current baseline provenance wins. This sandbox does not claim the canonical source builder has integrated those additions.

The historical helper remains untouched. Preparation attempts retained here include rejection of the old external policy, rejection of its missing MetaNetX namespace terms under the current policy, and an interpreter-symlink bug discovered after chemistry/KGX passed. The final helper fixes the last issue and checks the interpreter before source hashing. None of these is a scientific defect in the record. Final terminal receipts and all attempt hashes are listed in `handoff.json` once sealed.

The scientific limits remain unchanged: SfaC and its PLP assignment are inferred; Newman genomic protein identity does not establish a specific experimental construct; current chemical stereochemistry differs from the broader native structures; Cotton is abstract-only and Beasley full text was web-inspected without a local full-body hash. No new visual inspection is claimed by this replay.

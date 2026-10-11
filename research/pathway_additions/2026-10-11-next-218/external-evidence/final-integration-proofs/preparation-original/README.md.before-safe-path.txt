# ED integrated replay preparation

This separate external wrapper preserves the accepted `ed-replay-final.py`
(`f67d96bb1601ac0dce491886e9f28a119cfb355ba54d16f34d2e1121ec030e9e`).
It is preparation for root review, not scientific approval. No maintained
files have been changed and no full integrated ED replay has run.

The driver interface is:

```text
integration-replay.py --repo PATH --helper PATH
  --binding-manifest PATH --binding-sha256 SHA256 --output-dir NEW_EXTERNAL_PATH
```

Use the declared `.venv/bin/python` from `/private/tmp/pathwaymech-next-218-20261011`
with `PYTHONPATH=src`, `UV_NO_SYNC=1`,
`UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache`, and
`PYTHONDONTWRITEBYTECODE=1`. The intended helper is the adopted dossier's
`research/pathway_additions/2026-10-11-next-218/ed-replay-final.py`; the explicit
target is `data/pathways/entner-doudoroff-pathway.yaml`, SHA
`548eba1d34a081dd293db6d8bf0e00a0e620973e8f843dafa75bcded6a74e4af`.

Final binding capture requires root's dossier-adoption signal and its exact
digest. `prepare-bindings.py --dossier-adoption-sha256 SHA256` prepares the
expected manifest. A root-provided actual baseline bridge can additionally be
bound using the paired `--baseline-bridge PATH --baseline-bridge-sha256 SHA256`.
The preparer never launches the source helper or the project gates. The actual
driver must wait for root review of its code and final expected manifest.

Before scientific imports, the driver binds all current repository src/schema,
scripts and pathway files, identifier policy/manifests and both authority
snapshots, target, helper, eleven adjacent inputs, selected proof receipts,
original bodies and prior proofs, and environment provenance. The Claw
`kg_microbe_sources` package inventory includes the adapter and its actual
`__init__`, `catalogue` and `fetch` dependencies. The RDKit subprocess uses its
unchanged declared virtualenv path. Complete source/database bodies stay
external. Hidden and ignored files are inventoried; interpreter cache files
are excluded because the child receives a fresh external cache prefix and
bytecode writes are disabled.

Scientific source scope remains distinct from production authority scope:

- The unchanged ED helper consumes 94 original bodies, three complete SQL
  databases, the complete Rhea142 RDF gzip, and 16 original prior proofs.
- Production authority input bindings include root-reviewed GO, ChEBI,
  NCBITaxon and Rhea139 SQL, four newly adopted source-cache bodies, and the
  preserved UniProt 2026_03 batch. Binding those bytes does not repeat root's
  semantic authority selection or transfer fresh entry versions to the batch.
- iModulonDB responses provide expression context through the unchanged
  adapter. The original helper explicitly excludes a local article-byte replay
  for PMID:22519976. Its limitations remain in the child receipt.

The driver first checks the expected manifest's digest and resolved identity,
rejects optimized Python and output collisions, verifies complete inventories
and input hashes, and checks all helper dependencies against accepted metadata.
It rechecks formal inputs after slow source reads. It invokes the unchanged
helper, current identifier validation, native schema validation, and explicit
target strict validation as separately logged children. Before exclusive
success-receipt creation, it repeats uncached hashes, resolved identities and
inventories. It preserves failed attempts and never refreshes expectations.

`controls-attempt-1/results.json` records 40 passing narrow cases. They use the
actual driver functions, early-reject CLI calls, and small external fixtures.
Cases cover startup/final authority, policy, runtime, manifest, environment,
source and prior-proof mutations; late formal mutation; same-byte symlink
retargeting; hidden inventory changes; output collisions; duplicate bindings;
repository/helper arguments; optimized Python; and inherited environment
overrides. A valid timestamp/size stale `.pyc` was consumed by the baseline
fixture child, while the actual guarded environment loaded the source file.
This controlled binary `.pyc` is evidence and should be archived losslessly,
not treated as a normal disposable runtime cache.

These controls do not constitute a full positive replay or mutations of the
original scientific helper. Root full corpus validation, history, rendering,
tests, lint, KGX and independent scientific review remain separate. Myx PR405
merge/tree evidence is a separate lifecycle input; this wrapper makes no
actual-merged-baseline claim.

Interpreter and installed-distribution metadata are provenance, not an
attestation of every third-party or standard-library implementation. Python
startup/site processing precedes the script. Endpoint observations cannot rule
out arbitrary transient machine-state mutation between reads.

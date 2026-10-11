The external Myxochelin A/B author replay can attest success after a declared prior proof has changed. This is a bounded replay-provenance defect; the biological record and its nine reactions are not implicated by the reproduction.

Reviewed target: `5331f505f0942d877904faa74c8c4944887f0e61e7e4cbf95a042490796e72e2`. Reviewed helper: `59d89e69a51dd4119ede1cb08bd212951210ef66c55696620bda4e4a8c943cef`.

The helper hashes `manifest["prior_proof_inputs"]` at startup (lines 74–75), but its final uncached checks (lines 531–538) only revisit captured core files, source bodies and issuing databases.

An independent full replay copied the root acceptance proof to an isolated scratch path, updated only that path in a copied manifest, and changed that proof at the real `write_kgx` call. The unchanged helper returned exit 0 and wrote its PASS receipt. The copied proof changed from `22200e303451419b9efb9cab8d92559b688931fe65812c98365c808f4835ef1e` to `36d95c76a60b1540bd6db18a9c787cd915bd25e56e2c4b3814fe1d74583be5c3`, while the captured manifest still declared the former digest. A parallel captured-projection mutation was correctly rejected with no success receipt. Original author files and source bodies were unchanged.

Evidence is retained externally at `/private/tmp/pathwaymech-myxochelin-independent-review-20261011/`: `finding.json`, `binding-wrapper.py`, `run-binding-probes.py`, both `binding-*/probe.json`, the actual consoles and `binding-prior-proof/result.json`. The 35 frozen handoff/artifact inputs are preserved under `initial-inputs/manifest.json`.

Acceptance criteria:

- Bind the resolved identities and digests of all declared formal and prior-proof inputs before imports and recheck them uncached before exclusive success output.
- The same real late-proof mutation fails with no success receipt on the corrected helper.
- A fresh unchanged full source/chemistry/schema/KGX replay passes; preserve all nine transformations and the original scientific bytes.
- Preserve the initial helper, positive output, independent failure proof and exact successor lineage.

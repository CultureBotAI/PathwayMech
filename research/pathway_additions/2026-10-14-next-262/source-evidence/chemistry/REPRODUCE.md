# Read-only verification and isolated replay

Run the retained read-only verifier with RDKit 2024.03.5, using the recorded isolated runtime:

```bash
/Users/marcin/.cache/uv/archive-v0/5OkwykWCWjijtq5X5siy4/bin/python3 -B /private/tmp/pathwaymech-next-262-chemistry/helpers/verify_package.py
```

It rehashes all originals and four complete external source artifacts, reconstructs selected complete RDF subjects from the whole gzip, checks full native object metadata/slots, independently parses ChEBI structures, reconstructs native CML, recalculates all equations and joins, compares pinned SQL properties/labels, and verifies all compression/manifest entries. It writes no files. Redirect later verification output outside the frozen package.

The four large independently acquired originals remain at their explicit paths in `independent-authority-inputs.json`; their exact hashes and hash scopes are required. The 4.1 GB ChEBI and 1.0 GB Rhea SQL hashes are hashes of semantic SQL databases, not original OWL/OBO bytes. Original source download receipts are retained. Network access is unnecessary for replay of these exact snapshots.

For a full author-query replay, copy this package to a new external directory and remove only the copied `artifact-manifest.json` and `compact-retention-manifest.json`. Set `PATHWAYMECH_CHEMISTRY_ROOT` to that new directory. Run `helpers/query_rhea.py` with Python 3, then `helpers/verify_compounds.py` and `helpers/close_chemistry.py` with the recorded RDKit interpreter. Author helpers reject a frozen output directory. Compare output JSON after normalizing `generated_utc` and the new output-root path; source hashes, native equations, exact matches, structural comparisons and balances must remain equal. Do not run the acquisition helper against retained originals, because a current retrieval would be a different evidence snapshot.

`helpers/intake.py` and `helpers/fetch_chebi.py` preserve how the intake and eight fresh complete ChEBI responses were acquired. `receipts/execution-observations.json` and first-attempt receipts retain corrected author-script assumptions: symbolic Rhea coefficients, generic native SMILES, and the BI `substratesOrProducts` predicate. These are author self-checks, not a substitute for independent review.

All absence statements are explicitly bounded: exact chemistry against the complete pinned source artifacts, not a source-exhaustion or current global database claim. Filesystem inventories use `Path.rglob` and include hidden and ignored files. The final merged-corpus duplicate rebind is outside this chemistry task.

# Two additional context chemicals for PWY-5417

Both requested endpoints are ready for record-author use as canonical chemical identities:

| Native identity | Existing exact ID and authority label | Formula; charge | Full InChIKey |
| --- | --- | --- | --- |
| 2-KETOGLUTARATE | CHEBI:16810 — 2-oxoglutarate(2-) | C5H4O5; -2 | KPGXRSRHYNQIFN-UHFFFAOYSA-L |
| ADIPATE | CHEBI:17128 — adipate(2-) | C6H8O4; -2 | WNLRTRBMVRJNCN-UHFFFAOYSA-L |

`chemical-identity-replay.json` contains the exact full InChI strings, all native CML atoms and bonds, formula/charge checks, exact source locators and source hashes. RDKit2026.03.5 independently reconstructed both complete CML graphs; their canonical connectivity, full standard InChI layers and complete InChIKeys match the issuing structures. There are no unresolved stereocentres. These are source-author calculations, not an independent scientific review.

The complete native ADIPATE XML is reused from frozen263 native inputs (SHA309935e81d0cfb42fd4cc2fbb5d51cba6980bb812f9183634abda58ea79c4466). Complete native2-KETOGLUTARATE XML is reused from frozen262 inputs (SHA23246fa1176f753df61d4d23211e7a177f0929c80c17afa03a7f8398732c2f6a). Their exact complete-object acquisition receipts and source-package manifest entries are retained and replayed. CHEBI16810 issuing API JSON (SHAcf558f730bee143d869e9843ee616346125110fe1b22551e4877ee3ae1d5878c) and its original260 acquisition/manifest also match.

For both IDs, all outgoing exact subject rows were selected from pinned ChEBI255 semantic SQL (41 rows for16810;29 for17128). `originals/chebi-255-selected-complete-subject-rows.json` retains actual query, schema, complete selected rows and source owner. The4,137,340,928-byte database SHA is26ad4890cdcf6ee357760d815dfee8f5ba81e0873e62cb379369b04205722b0f. Its full hash is reused from the separately frozen263 authority-author receipt, which fully hashed the original at2026-10-15T06:37:02–06:37:18Z. This task verifies unchanged resolved path, size, mtime, inode and exact current owner; it does not repeat the4GB hash or copy the entire database. This later complete-hash receipt supersedes the authority author's earlier preliminary no-rehash note. No new network retrieval was needed.

Representation boundaries:

- Native2-KETOGLUTARATE SMILES is the generic/incomplete `C([R])(=O)C([O-])=O`. It was intentionally not used for exact identity. The complete native CML/formula/charge/full InChI and both issuing SQL/API structures agree.
- Native ADIPATE SMILES is complete and reproduces the exact structure.
- RDKit's retained “Proton(s) added/removed” warnings concern standard InChI normalization. Both resulting full InChI strings explicitly retain `/p-2`; this is not a measurement of biological protonation.
- PMID3612800 CatB inhibition and PMID8376330 pcaIJ expression induction are the requested context scopes, supplied by the primary-source author. This task did not independently review those paper effects, targets or preparations. Expression induction must not become direct enzyme activation.
- Neither endpoint asserts that these papers measured dianionic protonation, free species, counterions or direct binding. The IDs provide canonical dianion structures with that explicit limit.

This package is separate from the frozen eight-chemical supplement and formal six-step route. It adds no formal reaction or coefficient and changes no maintained file, Git or GitHub state. `input-bindings.json` supplies all11 original/copy bindings; `final-reuse-recheck.json` checks them again. `compact-retention-manifest.json` records uniform original/stored hashes, byte counts and encoding; raw logs and larger JSON use lossless gzip, and helpers are inert `.py.txt`. Predecessor manifests and issuing originals remain unchanged. `artifact-manifest.json` freezes every package file except itself.

# Reproduction and retained evidence

The maintained target is `data/pathways/protocatechuate-ortho-cleavage.yaml`.
Its complete node and reference identifier list is `identifiers.json`.
`reference-bindings.json` binds every record reference to its actual external
original and verified SHA-256. Raw XML, ontology SQL, RDF, paper scans and
issuing chemical records remain external.

`authorities/canonical-build-commands.json` records the unchanged source and
ontology builder invocations. Stage the original files at their declared cache
paths and verify the source digests before replaying them. The union retains
all previous terms and owners, as checked in
`authorities/canonical-union-comparison.json`. The baseline is Git commit
`4270a34ae30f4ccb5ce139d8a6f8fde35e938f5b`.

Run `just render-pages` after the last record or curation-history edit, then
`just validate`, `just test`, `just lint`, `just vendored-check` and
`git diff --check`. The first validation run found the new page stale because
an append-only history correction was added after rendering. Its actual failed
receipt remains under `validation/initial/`; it is not represented as a pass.

Validation log wrappers preserve exact UTF-8 text and its original-byte digest.
They do not normalize trailing spaces or claim a wrapper's digest is the raw
log digest. The independent reviews retain their actual inspected input hashes
and the commands and source access they performed.

Source licensing remains attached to the original source descriptors. This
curation does not assert clearance for public redistribution of raw datasets.

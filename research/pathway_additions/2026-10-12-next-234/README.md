# Pyruvate to cytochrome bd-I oxidase electron transfer

This dossier retains the complete source and review lineage for
`MetaCyc:PWY-7545`. The accepted record contains 44 descriptive paragraphs,
69 mechanism edges, 49 named identities and 115 reference entries. It preserves
the full native reaction/half-reaction, quinone/polymer, protein-complex,
construct and assay scope, and the original source-access limits.

The initial integration is local against reviewed THIO commit
`8c871a5808c73b0f21a397a2561269d068ee7368`; this dossier does not assert a public
push or merge. `integration-preparation.json` identifies the preparation archive
and remaining stages. `local-integration-decision.json` records that local-only
decision and preserves the historical merge requirement as provenance.

## Retrieve the evidence

`evidence-index.json.gz` is a lossless JSON content index. `body_lookup` maps each
whole body SHA256 to a repository file, a member of an existing THIO ZIP, or a
member of the ordered five-part ZIP under `archives/evidence-bodies.zip.part-*`.
Every location carries byte length and SHA256. Join the five parts in listed
order; their virtual ZIP hash is
`e1fd5da0ac984875dde043fad793c7373219148840e60104dd02ffabfaccae31`.
The parts together contain 161,829,755 bytes. Never interpret an individual part
as a complete ZIP or restore a historical symlink.

The index retains all 25 historical packet inventories and whole original
groups. It covers 3,320 distinct bodies (364,732,189 decoded bytes), including
828 manifest originals, 115 reference originals, 28 bibliography originals,
116 prior reference originals and two retired originals. A source binding may
reuse an existing exact body. Temporary absolute paths are historical metadata;
retrieval uses only the repository-relative locations.

`common.py.gz` and `verify_portable.py.gz` are the exact portable verifier
sources, compressed so archived tools are not treated as maintained Python
modules. Decompress these two files into a new temporary directory and run:

```bash
python -B /absolute/temporary/directory/verify_portable.py --adopted --root /absolute/repository
```

The verifier reads and checks the index and every referenced whole body without
extracting members or recreating historical filesystem objects. It checks
ordered part identities, original body identities, and all source bindings.
It requires the unchanged THIO evidence owners present in this repository.

`archives/integration-preparation.zip` retains the local adoption tools, exact
baseline inventories, accepted-input bindings, semantic preservation map,
preparation control streams/receipts and native future-stage plan. Its
`REPORT.md` explains author/reviewer roles and limitations. Historical failed
native extraction and the issue #494 repair retain their original dispositions
in the source evidence index. Failed packaging workcopies remain externally
retained with exact hashes; their diagnostics are in the preparation archive.

## Integration status

The final preparation validates its payload and preserves all existing source
authority objects, object order and prior corpus entries. It adds 17 source
terms and 15 ontology terms using the accepted actual native outputs. The
separately reviewed CHEBI:7896 classification change is explicit.

The preparation performs no maintained adoption, native history/review, gates,
shared-cache update or Git/GitHub operation. Root-owned adoption requires exact
independent review and acceptance; native history precedes rendering. Native
SSSOM export precedes render/tests, preserving all old rows and adding only
PWY-7545 mappings. Source licenses and access restrictions remain unchanged.

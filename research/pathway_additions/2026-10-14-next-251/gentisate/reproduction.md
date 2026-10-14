# Reproduction and evidence boundaries

The maintained record is `data/pathways/gentisate-degradation-i.yaml` at base
`cd42a526b06ce531e8326a2717d54d7ff770bd2b`. `identifiers.json` inventories all
final node and reference identifiers. Native, chemistry and primary manifests
bind original artifacts or explicitly typed extracted-text receipts to their
actual URLs and hashes. Raw XML, JSON, RDF, SQL, papers, images, HTTP headers
and full extracted article text remain external.

Six original author reproduction helpers are retained as `native/*.py.txt`,
with unchanged bytes and hashes. `native/helper-retention.json` maps their
external source names to maintained text paths. To replay, copy the selected
text artifact into an external scratch directory under its original `.py`
name and restore the declared inputs there. These are source artifacts, not
repository-maintained executable Python. Issue #529 records this packaging fix;
the initial failing lint diagnostic and successor review remain separate.

`authorities/canonical-build-commands.json` records the unchanged builders and
external cache paths. Restore and hash-check the declared original bytes before
replaying. The selection is the union of the baseline 4,799 authority IDs and
31 new-record node IDs; only 15 terms are new. The resulting 4,814 terms, 772
owners and 948 manifest entries preserve every old object and the complete
942-entry manifest prefix. The authored-record reconciliation checks exact node
selection and canonical labels.

After final record and append-only history changes, run `just render-pages`,
`just validate`, `just test`, `just lint`, `just vendored-check` and
`git diff --check`. Actual receipts and lossless log wrappers record results;
future success is not implied by this command list. Review bundles bind the
actual assessed bytes and retain any predecessor findings. Generated graph and
KGX checks must preserve endpoint qualifiers together with the associated edge.

The compact author projections support replay and source access, not independent
scientific approval. See the separate saved reviews and acceptance record for
actual review conclusions, remaining limits and completed validation.

Independent retention review found a moderate completeness/provenance defect in the proposed next267 evidence decoder. Stable key: `next267-retention-historical-completeness`.

Proposed owner: `research/pathway_additions/2026-10-15-next-267/evidence-retention/decode_retained.py`, `verify_historical()`. Payload manifest SHA256: `9a81127803cb3e0688736a1aeab036d118d1e84f4f46a53f3e3a825d3eb5bcd7`; decoder SHA256: `76fb0382d33f1c7a8951bc46575aeb76c8cfd1f1fc37208aaa80105133beb031`.

The package declares 477 historical compact references with exact original author/reviewer roles. Independent fault injection found that the decoder accepts an empty row list, 476 rows, an altered original-owner role, or a false current-manifest hash. Removing the metadata file returns a nonfailure `not yet added` disposition. Root independently reproduced both empty-row success and missing-metadata nonfailure. A standalone successful run therefore does not establish the declared historical completeness and ownership.

The exact frozen payload remains complete and recoverable. This is a verifier defect, not evidence loss, a scientific-record defect, or a finding against the earlier corrected Git tree binding in issue #591. Root's pre-adoption full-manifest guard also remains effective for the unchanged packet.

Acceptance:

- Require the final historical metadata and exact complete declaration set, with correct source-manifest bindings and original owner roles.
- Reject missing, omitted, duplicated, relabeled or mismatched declarations; preserve exact original source bytes.
- Verify complete valid offline reconstruction and all original 477 historical declarations/926 paths, alongside all 35 physical owners and current compact mappings.
- Preserve the original proposal and independent findings; publish an explicit corrected successor and obtain independent acceptance before adoption.

The independent review records 37 correct rejection controls and seven unexpected acceptances across this and the companion scratch-path finding. Full findings and root reproduction will be retained with the eventual PR. Keep this issue open until the correction is merged and the landed tree is verified.

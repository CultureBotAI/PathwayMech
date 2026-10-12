# Independent unnamed native reaction adapter review

Correction required before adapter adoption: one P2 internal provenance-consistency finding. The authentic original, request receipt, native parser identity and old-source conservation checks passed.

## P2 — Bind typed reaction provenance to the exact requested identity

Stable key: `ribose-native-reaction-typed-provenance-binding`.

`src/pathwaymech/identifiers.py:128–137` validates the new kind/type/label tuple but does not check its source URL against the exact typed MetaCyc identity or validate the native version format. Using the unchanged full ribose draft, changing only the reaction source URL to another META frame, an ECOLI request, or an unrelated host still produces no identifier errors. An invalid version string also passes. Missing kind/type controls correctly fail. See `probes.json`, `probes.py`, terminal `f60929/0`.

Restrict the fix to `kind=metacyc-reaction-xml`: enforce the supported exact HTTPS endpoint/query grammar, META scope, dotted numeric native version grammar and equality of the requested frame with each referencing typed CURIE. Add focused negative gate tests, preserve legacy authorities, and retain type checks before contextual bypass. No accession exception or source-body authenticity claim belongs in this fix. This is an internal snapshot-consistency defect; it does not show an error in the authentic XML or the builder's request/body checks.

## Optional P3 — Unexpected mixed content

Stable key: `ribose-native-reaction-xml-mixed-content-hardening`. Non-whitespace metadata/Reaction text and Compound/parent Reaction tails are currently ignored. Four mutations of the authentic XML reproduce this in `probes.json`. No wrong identity or chemical assertion was demonstrated, so this is not an adoption blocker. An optional fix should target element-only containers and preserve legitimate numeric/prose slots with nested evidence.

## Independent validation

- All 645 sealed artifacts were rehashed and the complete inventory checked, including hidden/ignored files. Actual merged225 plus accepted threonine and ribose patches replayed exactly; all seven files in their union match the candidate (`intake.json`, terminal `54fad3/0`).
- All 663 old manifest source bodies were rehashed and all 225 current records matched the canonical corpus. The patched builder reproduced all 2,328 terms and 510 source objects byte-for-byte, SHA-256 `6f62c939c85ea5c3285a1a132a888e02ee84806e2eafeb7cc6f8f932dbc638ba` (`reproduction.json`, terminal `9a7c06/0`).
- The original RXN-14904 request/body/receipt binding and the new bounded snapshot were reproduced. The frame-only HTML remains rejected. The unchanged full draft passed, and eight invalid-role controls failed with `ENTITY_TYPE_MISMATCH` (`native-replay.json`, terminal `3b930f/0`).
- The author's complete 1,180-test success log and Ruff log were inspected, including disclosed failed-attempt lineage. These are inherited evidence, not fresh reviewer executions.

Full findings, exact input hashes, validation commands and evidence are in `review.json`, `input-bindings.json` and the accompanying scripts/logs. This review does not accept the pathway's science or authorize maintained adoption; root owns integration and issue tracking.

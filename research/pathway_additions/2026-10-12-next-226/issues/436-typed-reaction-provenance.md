The new `kind=metacyc-reaction-xml` authority loader checks its type and label fields but accepts source metadata that contradicts the exact reaction identity. This affects the proposed ribose adapter; the authentic RXN-14904 XML and builder output pass their original/request checks.

Stable key: `ribose-native-reaction-typed-provenance-binding`
Severity: P2; fix before adapter adoption.

Independent reproduction uses the unchanged ribose draft (`385101d166c9150936d81bb0f1c6c0d134b6ac1e6a6454d86e238ac0576e3d71`). Changing only the typed source URL to a different META frame, an ECOLI request, or an unrelated host still yields no identifier errors. A malformed native version also passes. Missing source kind and entity type correctly fail.

For this new typed kind only, validate the supported HTTPS getxml endpoint and exact query grammar, require META scope, bind the requested frame to each referencing typed CURIE, and validate the supported dotted numeric version. Preserve type enforcement before contextual-label bypass and all existing untyped authority behavior. Add focused wrong-host/endpoint/frame/organism/query/version and shared-source identity regressions. Do not hard-code RXN-14904 or claim the offline loader authenticates unavailable source bytes.

Evidence: independent sealed review `pathwaymech-next-226-authority-review-20261012`, handoff SHA256 `7baf1f36f0dcf6ad0fb0bd16ed237d4a258d310fda573ba778a2320aa1c6de20`; `probes.json` and `probes.py`, terminal `f60929/0`. Review JSON SHA256 `d35a145efa280fc45791f855342884f6b12088e8ace4622d311a5deb0b94e101`.

The independent review also reproduced all 663 existing original source inputs byte-for-byte and passed the authentic reaction replay plus eight invalid-role controls. Optional XML mixed-content hardening is a separate nonblocking observation, not part of this defect.

Close after the narrow correction is independently accepted, integrated with its tests, and merged.

The frozen next265 merged discovery assessment overstates the number of pathway records owning its matching KGX rows. This is a minor reporting defect; all rows and the duplicate disposition remain supported.

Stable issue key: `next265-merged-discovery-kgx-owner-count`.

`/private/tmp/pathwaymech-next-265-merged-discovery-assessment/HANDOFF.md`, line 37, says that 84 matching KGX rows bind to nine complete owning YAML records. The complete row ledger and fresh independent comparison establish **eight KGX owners**. Nine is the union of HTML and KGX owners; `MetaCyc:PWY-2503` is the additional HTML/reference-register owner and has no matching KGX row in this scope.

Evidence:

- Frozen source manifest: `37f0bc394eb9db853aa94159ef45883fbdff997957cd63e0db82d1e7bac6ecd1`.
- Original handoff SHA256: `5e97259d96b9ce788f22c3292d37da78c9b86cfc5e790fececbdd86d3655cfc2`.
- `generated-lineage-verified.json.gz`, decoded SHA256 `d404066a88e22d9f610620a38a2114b00a0881f7653fce1b349be6aa623cf7ce`; derive the KGX owner set from `$.tsvs[*].lineage[*].record_id` plus `record_sha256` and compare with `$.pages`.
- Independent finding receipt SHA256: `71b5b6f2f5bde5a97457431cc828990acb1fbf921a05419376e180eecdadb762`.

Acceptance: preserve the original package, append an explicit eight-versus-nine count correction with the exact owner sets, independently verify that bounded correction, and retain it in the maintained report/evidence. Do not change the 84 row mappings, 541 HTML edges, pathway draft, or bounded duplicate conclusion. Close after verified publication.

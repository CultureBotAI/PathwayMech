# Hogancamp 2019 dissertation: bounded public access result

Status: **full dissertation remains inaccessible through the ordinary routes attempted**. No dissertation page, method, table, figure or appendix was read. No journal access tier is upgraded. This source-author access dossier is separate from the frozen next260 biological identity package and the primary-preparation dossiers.

## Source and inspection scope

The [TAMU institutional item](https://oaktrust.library.tamu.edu/items/fe380330-64dd-4b04-8ac7-edc5a89bf1aa) identifies Tessily Nicholle Hogancamp's dissertation, *Elucidating the Mechanism of Enzymes Utilized During the Bacterial Degradation of Lignin in the Protocatechuate 4,5-Cleavage Pathway*, dated 2019-10-21. Its handle is https://hdl.handle.net/1969.1/188745. The landing page displays a 30.76 MB PDF. This is a dissertation, distinct from journal DOI 10.1021/acs.biochem.8b00713.

This agent independently read the institutional landing metadata and abstract, lines 67–99 as displayed by the web tool on 2026-10-15. `landing-observation.json` is a structured observation, **not a captured raw institutional response**. The abstract describes a LigJ product complex with S-CHA, inactive E284Q used for KCH co-crystallization, and a proposed Glu-284 acid/base role in syn-addition. Those limited abstract observations do not establish exact construct, mutation background, purification, metal loading, substrate preparation, kinetic conditions or complete stereochemical experiments. No chapter-level experimental claims are promoted.

## Exact bounded access attempt

The parent had already observed failures at the linked `/bitstreams/.../download` route and the DSpace bitstream metadata route. All four files listed by the parent's external manifest were independently rehashed before this attempt; `receipts/context-bindings.json` binds those exact bytes and the manifest itself. The parent's ordinary download failure had no retained response body; its later metadata response is explicitly an HTML challenge, not source metadata.

This agent made **one** additional unauthenticated `urllib.request.urlopen` request using the ordinary public DSpace content route:

`https://oaktrust.library.tamu.edu/server/api/core/bitstreams/4debd50c-d6c5-49b7-b712-d21ea08e3971/content`

At 2026-10-15T00:05:53Z it returned HTTP 403, the same final URL, `Content-Type: text/html; charset=UTF-8`, and `Cf-Mitigated: challenge`. The 5,703-byte response is not a PDF. Its SHA-256 is `9fc5a6c65ad0e9736a57ce8348a8d84b4f7e195828143cfb63215384e2ef96e8`.

The response is external-only at `originals/public-content.response`; the compact allowlist omits the challenge body. `receipts/public-content.json` retains status, safe content headers and the exact body hash. The helper used no authentication, cookies, manufactured headers, challenge interaction or retry. Ordinary default URL redirection was permitted; the reported final URL did not change. The command exited 0 because it successfully captured the access result, **not because PDF acquisition succeeded**.

## Result and boundaries

- Full thesis acquisition: unsuccessful; the 5,703-byte challenge response cannot support scientific assertions.
- Institution landing abstract: independently read; only the bounded observations above are available.
- Journal main text: not acquired by this task; existing access limitations remain.
- Figures, tables, methods and appendices: unread; rendering was neither possible nor claimed.
- Prior research packages and maintained repository files: unchanged.
- No further challenge routes, repeated retries or access-control workarounds were attempted. This access gap does not block unrelated curation work.

`verification.json` reports hash checks, not scientific full-text validation. `artifact-manifest.json` binds all local dossier files except itself and the derived compact selection manifest. `compact-retention-manifest.json` is the explicit safe publication allowlist; it preserves inert helper text and compact receipts while omitting original challenge HTML.

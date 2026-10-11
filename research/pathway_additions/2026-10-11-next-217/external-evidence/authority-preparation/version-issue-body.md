The external Myxochelin authority proposal labels new MetaCyc HTML sources as frontend 22.5. The preserved issuing pages instead show Pathway Tools 27.0; compound/reaction pages also explicitly state MetaCyc version 27.0. Generic pathway/carrier pages do not state a database release, so software 27.0 must not be promoted to a database-version claim.

The same proposed version metadata is copied into the external authority-integration-dispositions dossier. Four UniProt entries also inherit the generic MetaCyc wording and should receive their own original `/entryAudit` metadata. The target YAML and original-source manifest already label their native XML references as MetaCyc 27.0; their chemistry, identities, evidence and reference versions need no change for this finding.

Evidence:
- Frozen target SHA256: `5331f505f0942d877904faa74c8c4944887f0e61e7e4cbf95a042490796e72e2`.
- Initial proposal SHA256: `eb904a6505c7f20f3773282ebee278848558a351b5838c3aa752127187e6d235`.
- Original [CPD-25904 issuing page](https://bf2i-artsymbiocyc.insa-lyon.fr/compound?orgid=META&id=CPD-25904), SHA256 `2b84515482b7898818e075269fc1485176c2b087b0d988c6e40efa07e4d2497b`, footer states MetaCyc 27.0.
- Original [PWY-8383 page](https://bf2i-artsymbiocyc.insa-lyon.fr/META/NEW-IMAGE?object=PWY-8383), SHA256 `6d25041102f5ddfd6994cdb64d21c055314825a23f5164f00da6654ab31a26ac`, footer states Pathway Tools 27.0 without a database release.
- Complete field-by-field original-body proof is preserved externally in `pathwaymech-myxochelin-authority-selection-20261011/version-attribution-finding.json` pending maintained integration.

Acceptance criteria:
1. Preserve the sealed initial proposal, disposition dossier, source bodies and prior review; do not rewrite historical observations.
2. Produce a linked production selection using the actual database footer where present; otherwise identify software version separately and leave database version unstated.
3. Use each original UniProt entry's own audit metadata without inventing a release.
4. Keep the existing independently sourced DHBAMPLIG-RXN authority and its valid historical 22.5 metadata unchanged.
5. Rebuild with unchanged canonical builders and independently verify every old authority entry/metadata is preserved. This issue concerns production provenance, not biological refutation or self-approval.

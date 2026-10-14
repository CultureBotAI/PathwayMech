# Next257 candidate and continuing queue

1. **Selected: MetaCyc:PWY-6416 — quinate degradation II.** The complete META 27.0 definition has three members: QUINATE-5-DEHYDROGENASE-RXN, 3-DEHYDROQUINATE-DEHYDRATASE-RXN and DHSHIKIMATE-DEHYDRO-RXN. It converts quinate through DHQ and DHS to protocatechuate. The first native equation uses NAD(P) classes; exact NAD versus NADP specificity belongs to each enzyme's evidence. GO:0019631 is broader and explicitly narrow-matches both quinate variants in the original pinned SQL. The narrower MetaCyc identity is appropriate.

2. **Already maintained: MetaCyc:QUINATEDEG-PWY — quinate degradation I.** Its first oxidation uses quinone/quinol classes, with PQQ as a distinct enzyme cofactor. Sharing the two downstream dehydrations does not make the two initial electron-acceptor variants identical.

3. **Already maintained: MetaCyc:SHIKIMATEDEG-PWY — shikimate degradation I.** Its two-member boundary starts at shikimate and uses SHIKIMATE-PQQ-RXN. It lacks quinate oxidation and the DHQ intermediate of the current candidate.

4. **Next: MetaCyc:PWY-6419 — shikimate degradation II.** The verified complete native XML selects RXN-20484 followed by DHSHIKIMATE-DEHYDRO-RXN. The initial NAD-dependent reaction, C. glutamicum contexts and QsuR evidence require their own complete scientific review. This is a separate continuing lead, not an automatically approved record.

Both II variants are absent as top-level records and nested pathway nodes in all 253 baseline Git blobs at `11afa1984bbb0d41c34dc82361bd0f0e1c0b9f37`. The I variants are present. Current ignored/hidden-inclusive text searches and the prior narrative ledgers confirm that II was explicitly queued as pending research; scope exclusions from I records are not rejections of II.

The ignored SEED selector names Quinate degradation but does not supply its roles or organism graph. That remains a reusable-source lead. The source universe is not exhausted. No source-defined variant is merged into another merely because papers, proteins or downstream chemistry overlap.

This is author identity preflight. The PWY-6416 evidence slots repeat I-route PMIDs 8002591 and 14586099; those slots are not independent confirmation of the NAD route. Fungal and Corynebacterium primary contexts, protein identity, regulation, cofactor specificity and assayed constructs require separate scientific interpretation.

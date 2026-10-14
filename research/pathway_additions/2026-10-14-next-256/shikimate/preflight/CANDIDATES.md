# Next256 candidate decision and continuing queue

1. **Selected: MetaCyc:SHIKIMATEDEG-PWY — shikimate degradation I.** The complete META 27.0 native boundary uses SHIKIMATE-PQQ-RXN followed by DHSHIKIMATE-DEHYDRO-RXN, converting shikimate to protocatechuate. GO:0019633 is a broader substrate catabolic process and explicitly narrow-matches both the I and II variants. The narrower native pathway identity is appropriate. Reaction, protein, taxon and construct evidence require the separate author and independent reviews.

2. **Already maintained: MetaCyc:QUINATEDEG-PWY — quinate degradation I.** The 252-record baseline includes its three-step quinate-to-protocatechuate record. It shares QuiA/QuiC and terminal dehydration with the selected shikimate route, but its initial substrate and reaction membership differ. Shared papers or proteins are not duplicate whole-pathway coverage.

3. **Next: MetaCyc:PWY-6416 — quinate degradation II.** Fresh complete META 27.0 XML selects NAD-dependent QUINATE-5-DEHYDROGENASE-RXN followed by the two dehydration members. Its fungal and Corynebacterium examples and individual enzymes need complete scientific review.

4. **Further: MetaCyc:PWY-6419 — shikimate degradation II.** Fresh complete META 27.0 XML selects RXN-20484 and DHSHIKIMATE-DEHYDRO-RXN, with a distinct NAD-dependent initial reaction and Corynebacterium/QsuR evidence that remains unreviewed here.

The selected shikimate I and both II variants are absent as top-level records and nested pathway nodes in the actual 252 baseline Git blobs. Ignored and hidden text was included in both current repository-root scans. Prior research explicitly queued these pathways; it did not reject them or accept them as maintained records. The ignored SEED Quinate degradation selector remains a reusable-source lead. No source exhaustion claim is made.

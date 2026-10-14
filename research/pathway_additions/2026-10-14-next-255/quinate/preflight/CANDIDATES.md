# Next255 candidate decision and continuing queue

1. **Current: MetaCyc:QUINATEDEG-PWY — quinate degradation I.** Its exact native three-member boundary converts quinate to protocatechuate with a PQQ-dependent initial oxidation. GO:0019631 is broader and explicitly has `skos:narrowMatch` to both QUINATEDEG-PWY and PWY-6416 in the original pinned GO SQL. The PQQ-specific source-defined composite is eligible for curation with properly scoped evidence; one-strain experimental reconstruction is not an additional prerequisite.

2. **Next: MetaCyc:SHIKIMATEDEG-PWY — shikimate degradation I.** Its exact native two-member boundary uses SHIKIMATE-PQQ-RXN then DHSHIKIMATE-DEHYDRO-RXN, ending at protocatechuate. It is a separate starting substrate and initial oxidation from quinate I. GO:0019633 is broader and explicitly narrow-matches both I and II variants. Direct primary scope and the initial reaction remain to be independently assessed for its own record.

3. **Further: MetaCyc:PWY-6416 — quinate degradation II.** Newly inspected complete META 27.0 XML selects QUINATE-5-DEHYDROGENASE-RXN followed by the same two dehydration members, with an NAD-dependent initial step. Fungal and Corynebacterium examples are distinct from the selected PQQ route. Whole biological-source and primary interpretation remain future work.

4. **Further: MetaCyc:PWY-6419 — shikimate degradation II.** Newly inspected complete META 27.0 XML selects RXN-20484 and DHSHIKIMATE-DEHYDRO-RXN. The native overview concerns NAD-dependent Corynebacterium glutamicum enzymes and QsuR-controlled catabolism. This is an unreviewed lead, not automatic approval or proof of all asserted regulation.

None of these four exact IDs appears as a top-level record or nested pathway node in the 251-record baseline. Existing research explicitly queued the I variants; no previous maintained record or rejection was found. The ignored SEED selector also names a Quinate degradation subsystem, but its actual mechanistic role/organism contents remain unassessed. The source universe is not exhausted.

Independent scientific review of candidate MetaCyc:PWY-8178 found a minor defect in `data/pathways/pentose-phosphate-pathway-non-oxidative-branch-ii.yaml`. The candidate is awaiting integration.

Stable finding key: `pwy8178-reaction-direction-metadata`

Every original Reaction has reaction-direction REVERSIBLE, and the prose and side evidence correctly retain it. All six record reaction nodes omit direction, so the native node/graph/export direction field is unavailable despite known source support.

Correction: Set direction: reversible on each of the six existing reaction nodes. Keep the selected pathway-layout side orientations and all twenty side occurrences exactly as authored.

Acceptance: All six node directions are reversible; the 51 edge triples and 20 side triples remain unchanged. Standalone/native page and KGX node metadata expose the direction after regeneration.

Affected fields: `reactions[*].direction`

Primary evidence: MetaCyc:RXN-21730, MetaCyc:SEDOBISALDOL-RXN, MetaCyc:1TRANSKETO-RXN, MetaCyc:2TRANSKETO-RXN, MetaCyc:RIB5PISOM-RXN, MetaCyc:RIBULP3EPIM-RXN

Source locations: /ptools-xml/Reaction/reaction-direction; /ptools-xml/Pathway/reaction-layout

Review packet SHA256: `d7749e954e7cd7a823fa5f7bb0ed2ded90394e48b9a51f8313eab37c3ae9fa8c`. Preserve the complete six-event pathway, all biological edge identities, and negative/conflicting controls.

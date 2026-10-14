# Next251 author-support preflight and authority handoff

Selected exact native pathway: **MetaCyc:PWY-6223 — gentisate degradation I**. Its three members cover gentisate oxidation, maleylpyruvate isomerization and fumarylpyruvate hydrolysis to fumarate plus pyruvate. No exact corresponding biological-process GO term was identified in the pinned keyword/xref scan; related activity terms and chemically distinct homogentisate coverage are documented in go-scope-compact.json. This is the isomerization route, not PWY-7469 direct hydrolysis.

All 248 baseline pathway YAMLs at cd42a526b06ce531e8326a2717d54d7ff770bd2b were inventoried. Final 151-pattern searches include ignored and hidden files in both main and the new worktree, excluding .git/.venv. Candidate/core reaction families, native catalysts, U2 proteins, BagL and all selected source/evidence accessions reveal no pre-existing candidate record or prior rejection. The bounded search includes ordinary text only: compressed/archive interiors are not decoded, binary content is subject to rg detection, and symlink directories/external caches are not exhaustively followed. Prior SEED mentions are selector leads; DRAM M00638 is the adjacent upstream salicylate-to-gentisate module. Source and substring near-misses are reconciled in dedup-summary.json and retained-source-mentions.json.

No iModulonDB regulatory edge is supported. The current complete returned inventory lacks Ralstonia/U2. C.glutamicum modulome263 contains a NagL gene hit, but its explicit UniProt accession is inactive and no equivalence to the selected native enzyme was established. Gene annotations and search hits do not establish expression-module membership, direct regulation or pathway flux.

The unchanged canonical builders completed successfully against an external selector containing all 4,799 prior authority IDs plus 31 planned node IDs. Exact comparisons preserve all 4,799 prior term objects and 766 prior source-owner objects and all 248 baseline YAML hashes. The final union has 4,814 terms and 772 owners; the manifest retains the full ordered 942-entry prefix and appends 6 entries (948 total). No maintained file was written by this agent. No full-suite or identifier-gate success is claimed here.

Outputs in authority-staging/:
- identifier_sources.json: ffdde43abf9fbf85e4038dd1ecfbac0abfae75380da0e9cedbbe31b991a12d0e
- sources.union.json: 90a54f058623a6ed99d07c55cb53c8b0cbb81f19c65125e0da8e6df8e510b92c
- ontology.union.json: 847a2a1aa23a03574992eb8a3f7900b588b9cc855e7abe105d1fb5c76d2be583
- planned-labels-compact.json: all 31 exact canonical display labels.
- canonical-union-comparison.json: all-object preservation and output hashes.
- canonical-build-commands.json and per-builder receipts: unchanged builders, inputs and timing.
- reconcile_authored_record.py: bounded final authored-ID/label comparison; requires the authored YAML path. This is author support, not independent scientific review.

Additional pathways remain as leads: PWY-6336 protocatechuate para-cleavage (primary PMID19717587) is strongest next; P184-PWY meta-cleavage needs boundary and tautomer/source-scope reconciliation. CANDIDATES.md documents inspected native objects, abstract-only primary reading and unresolved evidence gaps. No exhaustion is claimed.

Retain only compact report/provenance artifacts. Original HTTP/XML/JSON bodies, full ontology stanzas, complete search matches, full primary metadata/abstracts and authority caches stay external. artifact-manifest.json lists recommended compact preflight artifacts; authority-staging contains the selected production outputs for root integration.

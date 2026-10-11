# Complete ethylmalonyl-CoA pathway

This addition represents **KEGG:M00373**, the complete fourteen-reaction ethylmalonyl pathway, with Cereibacter sphaeroides 2.4.1 experimental context. All twelve mandatory KO groups (thirteen KOs), both terminal branches, 50 participants, 105 mechanistic edges, 155 evidence items and 44 references are retained.

The exact corrected record has SHA-256 `1c58f2d1b27fd7a8a3928971a49311a742e004a1b28f349b9331b8fe0f369912`. The eleven-member MetaCyc PWY-5741 definition ends in different ATP-forming chemistry and remains distinct. Formal balancing does not establish physiological flux or microscopic ETF stoichiometry.

## Evidence and review

The full original independent review and its two supported findings remain under `initial-review/`. Issue #416 identified a false pass in the original external replay helper; the corrected helper freshly reads original RDF for every reaction direction and chemical side. Independent reassessment verified all fourteen directions with a separate XML parser, all fourteen reversal controls, a complete positive replay and final input/output mutation rejection. Issue #417 is resolved by eight exact wording/locator changes: the cited ACAD-family two-ETF interpretation is distinguished from observed Mcd ETF semiquinone, and PccR complementation is limited to growth and cellular PCC activity. Other parsed record values are unchanged. Original, corrected and successor evidence remain separate; external findings are not fabricated canonical review predecessors.

The added MetaCyc Protein XML authority parser separately resolves issue #418. Its independent review confirms rejection of the three original malformed-name fixtures without creating or replacing output, while valid beta forms and all four authentic native-source outputs are preserved. Identifier admission alone does not establish organism, assembly or catalytic equivalence.

Material limits remain explicit: exact PhaB and crotonase proteins are unresolved; the native 548-aa D3JV03 sequence is not silently replaced with the 555-aa Q3J5V7 counterpart; reviewed versus inferred assemblies and alternative-metal assays remain distinct; Mcl2 dimer/trimer uncertainty and AM1 stereochemical wording conflicts are retained. No direct PccR ligand/binding evidence is invented. PMID18819910 and PMID19703103 remain abstract-only sources. The two ETF states are whole-carrier formal reaction participants.

## Authority and integration

The canonical production builders passed against the actual Calvin merge `7b5201e93c0608631af73e629780d829efd26426`. They added seventeen original source entries and thirteen ontology terms, producing 624 manifest entries, 1,871 ontology terms and 2,251 source terms. Every prior term and source metadata entry is preserved exactly. All fourteen current RDF equations agree with the pinned Rhea139 authority labels, so no new Rhea update selection or release upgrade is made. All 624 source bodies and four complete SQL databases were hashed before and after the build.

Current deduplication included ignored/hidden files and followed symlinks and found no complete duplicate among 221 prior records. The known DRAM lead has four rows, three coordinates and four reaction IDs including R09979; historical three-reaction shorthand is explicitly corrected. This is bounded deduplication, not source exhaustion.

Maintained rendering, whole-corpus validation, tests, lint, graph/KGX preservation and the canonical saved scientific review follow adoption; this paragraph does not claim they have passed. Their actual receipts and final status will be added separately.

`PREPARATION.md` preserves the original package README without changing its historical pending status. `archive-inventory.json` describes the original staging proposal; `record-integration.json` records the actual adoption mapping, including that README rename. Complete raw source bodies, broad article extracts and unselected probe artifacts remain external. Archived helpers require their original pinned external inputs and runtime. Public-release licensing remains a separate deferred task.

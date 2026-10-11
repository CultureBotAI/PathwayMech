# Pyochelin biosynthesis — cohort 216

The maintained record is [GO:0042864](../../../data/pathways/pyochelin-biosynthesis.yaml), covering all eleven native MetaCyc PWY-6408 reaction objects from supplied salicylate through pyochelin release. It contains 30 participants, one PAO1 taxon, 91 mechanistic edges, 242 evidence blocks and 67 references. The external source replay produced 43 KGX nodes. The complete identifier inventory is [pyochelin-identifiers.json](pyochelin-identifiers.json).

The actual integration base is the Staphyloferrin B merge `3fb840bf48d871bc37576cc669d23441c0206e66`. [The baseline transition](merged-baseline-transition.json) verifies its complete tree equals the reviewed B commit and preserves the three prepared authority files. Duplicate searches covered the original checkout and both prepared checkouts, including ignored and hidden files and followed symlinks; only the earlier SEED source-menu entry and preserved search excerpts matched. This is not source exhaustion.

## Scientific scope

- The native route begins with supplied salicylate. PchA/PchB supply, PchC editing, export, uptake, iron loading and regulation are separate context.
- The shared cysteine-adenylation reaction is used twice. The three-ATP total is a formal stoichiometric derivation, not a measured yield.
- PchE aryl and peptidyl carrier sites occupy the same polypeptide. Carrier-state coefficients and the reactive-group balance model do not establish whole-protein counts, complete protein formulas or a fixed PchDEFG assembly.
- Native CPD-9992 is a source-defined pyochelin I monoanion projection. The observed interconverting I/II products remain explicit; neither exclusive I production nor selective I release is claimed. Neutral CHEBI:67183, the broader neutral I/II class and the other epimer are not silently made exact equivalents.
- Current PAO1 proteins, historical PA14 sequences and engineered constructs remain distinct. The historical PAO1 PchF sequence also differs from the current entry. PchE dimer and bound-magnesium evidence retain their preparation scope; PchG analogue kinetics do not establish full carrier-substrate turnover or an assembly.
- Current inferred annotations, unreviewed PchG identity and iModulon expression context retain their evidence limits. The context accession G3XCL0 is not equated to Q9HWG5. Null-regulator parser failures and selected-table non-hits remain documented observations.

Full original bodies were inspected for the 2022 PchE study and supplement and the 2018 PchF and 2016 PchG studies. Older indexed abstracts and separately inspected web-only full text retain distinct access records; no unavailable response-body hash is invented. Original article, native database and API bodies remain external. The [curation dossier](pyochelin-curation.md), [source manifest](pyochelin-source-manifest.json) and [chemical bridges](pyochelin-chemical-bridges.json) retain the detailed source and structure decisions.

## Review lineage and integration

The original external record `c72de0b0…` and helper `ced1468e…`, initial independent findings and reproduced unsafe PASS remain unchanged. [Issue 397](https://github.com/CultureBotAI/PathwayMech/issues/397) is addressed by exactly five source-local evidence scalars in the accepted record `b3dfb5d0…`. [Issue 398](https://github.com/CultureBotAI/PathwayMech/issues/398) is addressed by the accepted helper `19cf087a…`, independently tested with the full original-source replay and the same authentic late-metadata mutation. The latter now rejects without producing a success receipt. Focused controls are distinguished from full scientific replay.

The [copy plan](pyochelin-copy-plan.json) and [root adoption](root-copy-adoption.json) map current and historical observations, 251 exact-byte aliases and all 83 formal input occurrences. Archived Python is inert `.py.txt`; logs, diffs and TSV artifacts use lossless wrappers. Historical external observations are not fabricated canonical review records.

[Root source acceptance](root-source-acceptance.json) independently rehashed all 95 original bodies and 58 supporting artifacts. The authority preparation used unchanged canonical builders; root independently checked original labels and exact synonyms before adopting their exact outputs. It adds 23 source inputs, six ontology terms and 26 source terms while preserving all prior entries. The preserved execution receipts distinguish the actual external builder run from later artifact adoption.

All record and infrastructure history was written before final rendering. The [maintained replay adoption](integrated-replay-root-adoption.json) binds the actual current record and authority root, all 95 original bodies and 47 formal/runtime inputs. It preserves the original helper receipt and explains its generic external-author wording rather than rewriting that observation.

[All seven corpus gates](full-gates-root-adoption.json) passed: render, validate, tests, lint, identifier checks, KGX export and whitespace checks. The test result is 1,256 passed and three skipped; the separate vendored check confirms all 22 governed artifacts match. [The independent programmatic graph audit](independent-graph-root-adoption.json) verifies 42 SVG nodes, 43 KGX nodes, 91 edges and all 242 evidence blocks. The scope-only taxon remains in the component table and KGX. All 216 prior records, 956 record/history/review/page files, 10,247 edges and 6,802 record contexts are preserved. This is not a browser interaction inspection.

The [integration receipt](integration-receipt.json) seals these current inputs for the separate canonical scientific review. The final review adoption, later PR review, actual merge and deployed-byte verification remain distinct lifecycle observations; this dossier does not pre-claim them.

## Replay

Run the maintained `pyochelin-replay.py` with explicit `--repo-root`, `--record`, `--source-manifest`, `--source-projection`, `--authority-root`, `--reactive-helper`, `--rdkit-python` and a fresh `--output`. Original-body locations in the manifest identify the retained evidence and must remain unchanged. The [copy handoff](pyochelin-copy-handoff.json) records the exact integrated command and environment. The replay checks source membership, chemical sides and balances, sequence scope, evidence pointers and KGX equality, and rechecks bound inputs before creating its receipt exclusively. It does not replace whole-corpus validation or independent scientific review.

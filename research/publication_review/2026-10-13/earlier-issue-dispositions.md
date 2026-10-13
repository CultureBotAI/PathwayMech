# Earlier issue closure assessment

All 13 requested issues are verifiably fixed in the cumulative work: #481, #484, #485, #486, #488, #489, #494, #495, #496, #497, #499, #500 and #502. None of these 13 requires deferral. Their closing keywords were added only to the temporary PR draft `/private/tmp/pathwaymech-publish243-pr-body-20261013.md`; this assessment did not close issues remotely.

## Scope and method

Reviewed checkout: `/private/tmp/pathwaymech-next-243-local-20261012`. Cumulative nine-commit range: `e1c66917e753105c4bf5b7b026193fcefa2b000f` through `70903536191206d2586cd23e46f7d70c32fef92e`, plus the current #504 consumer correction where it preserves and strengthens #500's earlier fix.

Read the complete 13 issue bodies from `/private/tmp/pathwaymech-publish243-open-issues-20261013.json`. Compared their acceptance requirements with actual current maintained code, tests, records and exports; archived corrected helper source; recorded independent controls; root execution receipts; and independent actual-output acceptance. A matching issue reference or comment was not treated as sufficient evidence.

Content-addressed ZIP members were located through each `archive-inventory.json`; inspected helper/report bodies were checked against recorded hashes. For #494's actual-native acceptance, the five-part evidence archive was read in order and its part hashes, combined archive hash and requested member hash were checked. All five #497 script bodies were independently decompressed and compared with the maintained storage-map sizes/hashes. All three #495 maintained histories were checked against accepted hashes and their actual `session.actors` values. The six #486 current first owners and the three #496 current THIO SSSOM mappings were read directly.

Searches used to establish absence included ignored and hidden files. The five exact removed raw-script paths were additionally checked with `os.path.lexists`, covering literal paths and broken links independently of ignore rules.

No new broad test suite, native authority build, source reacquisition, scientific reinterpretation, remote mutation, staging, commit or branch operation was performed in this assessment. References to passing affected tests are to the earlier executed #504 affected regression run (2,148 passed), not a rerun during this closure assessment. Archived execution/review results remain attributed to their original producers and reviewers.

## Dispositions

Here, **THIO** means `research/pathway_additions/2026-10-12-next-233/`. Archive locators use the original filename recorded in `archive-inventory.json`.

| Issue | Disposition | Verified fix and evidence |
|---|---|---|
| #481 | Close | Formatting/import-only successor independently assessed in `THIO/archives/canonical-preparation-audit.zip → REPORT.md`; normalized AST/import proof in `canonical-preparation.zip → runtime-bridge-proof.json`. Subsequent maintained lint receipt exits zero. |
| #484 | Close | Archived `owner-recovery-preparation.zip → common.py:63` calls `identity()` before hashing. `canonical-successor-audit.zip → REPORT.md` records direct/linked FIFO rejection before the reader, plus regular-file controls. Completed successor execution is retained. |
| #485 | Close | Archived `prepare_and_build.py:390–440` freezes expected verification paths and bindings before validators, then rechecks them. Independent hidden/nested-file, replacement and drift controls pass. `verification-output-audit.zip → REPORT.md` confirms actual output matches the predeclared inventory. |
| #486 | Close | Current authority retains `rhea-components-142` for both RHEA components and `uniprot-ecoli-reviewed-cofactors` for all four proteins. `owner-recovery-review.zip → REPORT.md` verifies complete-source first-owner extraction; actual-output audit confirms 2,548 terms/642 owners and preserved unowned manifest entries. |
| #488 | Close | Archived verification successor stages regular internal authority copies. `verification-output-audit.zip → REPORT.md` verifies both paths, unchanged containment rules, all 234 record gates and complete KGX. Root execution receipt exits zero. |
| #489 | Close | Archived `verification-recovery-preparation.zip → verification_common.py:38` validates identity before decoding. `verification-json-reader-finding.zip → json-reader-checks.json` records negative controls and empty decoder-spy calls; completed execution/output audit follows. |
| #494 | Close | `scripts/build_ontology_identifier_snapshot.py:49` excludes citation-only references while preserving nested selectors and explicit retention. Dedicated cases start at `tests/test_identifier_snapshot_builders.py:195`. `RHEA:29170` remains in the record's references. Next-234 evidence index retains actual native successor acceptance for 235 records and full KGX. |
| #495 | Close | All three maintained histories match their accepted hashes and identify `session.actors: codex/gpt-6/codex`. `THIO/native-integration/history-correction/completion.json` records successful history validation/final gates; original scaffolds remain archived. |
| #496 | Close | Current SSSOM contains exactly the three THIO NADP/NADPH/PROTON mappings. `history-correction/sssom-regeneration.json` records native export matching the failed test's expectation and preserving old rows; completion records subsequent full checks. |
| #497 | Close | Independently decompressed all five `.py.gz` bodies and matched storage-map sizes/hashes. Literal-path checks confirm the five raw copies are absent, including ignored/broken-link cases. `receipt-encoding-correction/preservation.json` documents bounded changes; its actual repository lint receipt exits zero. |
| #499 | Close | `src/pathwaymech/biocyc_pathway.py` establishes typed whole-Pathway identity and reconstructs retained source projection. `tests/test_nitrate_native_authority.py` covers whole originals, malformed identities/slots, misleading HTML, placement and conflicts. |
| #500 | Close | Current `_native_assertion_kinds` compares complete named-complex projections and release before term selection. `tests/test_named_complex_consumer_conflicts.py` covers coefficient, GO context and release collisions, both orders, unselected owners and identical duplicates. These tests passed in the affected regression run. |
| #502 | Close | `biocyc_aceto.py:766` includes existing unnamed complexes in the forward assembly graph. `tests/test_aceto_legacy_cycles.py` exercises producer/consumer, both orders, selected/unselected owners and acyclic controls. These tests passed in the affected regression run. |

## Concrete retained checks

- #495 maintained history bodies: `history/records/thioredoxin-pathway/2026-10-12T135141Z-codex-7c7866.yaml`, `history/records/desferrioxamine-b-biosynthesis/2026-10-12T135147Z-codex-27f03d.yaml`, and `history/infrastructure/thioredoxin-carrier-authority/2026-10-12T135152Z-codex-65a503.yaml`. Each actor is `{type: ai_agent, name: codex, model: gpt-6, agent_tool: codex}`.
- #486 first-owner identities: `RHEA-COMP:10698`, `RHEA-COMP:10700`, `UniProtKB:P0A9P4`, `UniProtKB:P0AA25`, `UniProtKB:P0ACQ4`, `UniProtKB:P0AGG4`.
- #496 mappings: `MetaCyc:NADP → CHEBI:58349`, `MetaCyc:NADPH → CHEBI:57783`, `MetaCyc:PROTON → CHEBI:15378`, each scoped to `MetaCyc:THIOREDOX-PWY`.
- #494 accepted actual-native receipt: indexed historical owner `/private/tmp/pathwaymech-next-234-root-actual-native-acceptance-20261012.json`, SHA256 `aae7f282180ca7d4fb701e56781e17fe9f64abac5c12ac5bce08a595278b8381`; complete 235-record state and 4,217-node/11,803-edge KGX are recorded, with the failed predecessor retained.
- THIO actual completed verification: `THIO/actual-native-acceptance.json`; archived root execution receipt SHA256 `7b28b2a30c3034a89e27fe1320d4f4ac999712e1cf16c403c420049e4202a5a2`, exit zero; independently accepted actual-output handoff `1df7658ad10ed6a77b14c5bb5b242e76c1079a4af7e3bfd2db3b6effd1a2264e`. Earlier failed wrappers remain failed.

These dispositions concern the specified defects and their concrete acceptance criteria. They do not establish public-release licensing clearance or make a fresh browser/scientific-source review claim.

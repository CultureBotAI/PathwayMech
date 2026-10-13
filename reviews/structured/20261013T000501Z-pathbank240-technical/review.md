# Technical review of E. coli spermidine PathBank context integration

- Review: 20261013T000501Z-pathbank240-technical
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-13T00:04:04Z
- Finished UTC: 2026-10-13T00:05:01Z
- Reviewer: Codex /root/adapter_continue (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Eight exact technical owners pass current maintained integration review. All old objects/files/cache, complete mappings and current graph are preserved; actual native gates pass. Both resolved local context findings, inherited science and static layout limits remain explicit.

## Scope And Provenance

Eight runtime/configuration/fixture/test/authority owners after completed record 240 gates, with complete maintained context.

Selection: All eight nonrecord primary owners from committed 239 baseline 5eb77a4b8039e98d9b53a61d09af52fa9f5b3d7a; no sampling.
Coverage: full; 8 reviewed / 8 in the declared population.
Source: working_tree at Git base 5eb77a4b8039e98d9b53a61d09af52fa9f5b3d7a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| owner-1 | conf/identifier_sources.json | maintained | conf/identifier_sources.json |
| owner-2 | data/identifier_authorities/sources.json | maintained | data/identifier_authorities/sources.json |
| owner-3 | scripts/build_source_identifier_snapshot.py | maintained | scripts/build_source_identifier_snapshot.py |
| owner-4 | src/pathwaymech/identifiers.py | maintained | src/pathwaymech/identifiers.py |
| owner-5 | src/pathwaymech/pathbank_context.py | maintained | src/pathwaymech/pathbank_context.py |
| owner-6 | tests/fixtures/pathbank_context/SMP0002097.owl | maintained | tests/fixtures/pathbank_context/SMP0002097.owl |
| owner-7 | tests/fixtures/pathbank_context/SMP0002097.receipt.json | maintained | tests/fixtures/pathbank_context/SMP0002097.receipt.json |
| owner-8 | tests/test_pathbank_context_authority.py | maintained | tests/test_pathbank_context_authority.py |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Actual native history-1 | passed | False | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native history-2 | passed | False | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native sssom | passed | True | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native render | passed | True | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native skills | passed | True | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native validate | passed | True | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native tests | passed | True | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native lint | passed | True | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native kgx | passed | True | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native vendored | passed | True | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native diff-check | passed | True | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native site-current | passed | True | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Independent maintained target QA | passed | True | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Whole maintained check passed after all native gates. |
| Independent maintained checkout QA | passed | True | owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8 | Whole maintained check passed after all native gates. |

## Scientific And Domain Assessments

### conf/identifier_sources.json

ownership: supported. Targets: owner-1.

Whole maintained owner equals the accepted deterministic runtime/configuration/native-output payload. The complete context contract and producer/consumer changes were independently reviewed upstream; current maintained integration and the actual full regression are verified here. Generated snapshot changes must be rebuilt from maintained configuration and adapters.

### data/identifier_authorities/sources.json

ownership: supported. Targets: owner-2.

Whole maintained owner equals the accepted deterministic runtime/configuration/native-output payload. The complete context contract and producer/consumer changes were independently reviewed upstream; current maintained integration and the actual full regression are verified here. Generated snapshot changes must be rebuilt from maintained configuration and adapters.

### scripts/build_source_identifier_snapshot.py

ownership: supported. Targets: owner-3.

Whole maintained owner equals the accepted deterministic runtime/configuration/native-output payload. The complete context contract and producer/consumer changes were independently reviewed upstream; current maintained integration and the actual full regression are verified here. Generated snapshot changes must be rebuilt from maintained configuration and adapters.

### src/pathwaymech/identifiers.py

ownership: supported. Targets: owner-4.

Whole maintained owner equals the accepted deterministic runtime/configuration/native-output payload. The complete context contract and producer/consumer changes were independently reviewed upstream; current maintained integration and the actual full regression are verified here. Generated snapshot changes must be rebuilt from maintained configuration and adapters.

### src/pathwaymech/pathbank_context.py

ownership: supported. Targets: owner-5.

Whole maintained owner equals the accepted deterministic runtime/configuration/native-output payload. The complete context contract and producer/consumer changes were independently reviewed upstream; current maintained integration and the actual full regression are verified here. Generated snapshot changes must be rebuilt from maintained configuration and adapters.

### tests/fixtures/pathbank_context/SMP0002097.owl

ownership: supported. Targets: owner-6.

Whole maintained owner equals the accepted deterministic runtime/configuration/native-output payload. The complete context contract and producer/consumer changes were independently reviewed upstream; current maintained integration and the actual full regression are verified here. Generated snapshot changes must be rebuilt from maintained configuration and adapters.

### tests/fixtures/pathbank_context/SMP0002097.receipt.json

ownership: supported. Targets: owner-7.

Whole maintained owner equals the accepted deterministic runtime/configuration/native-output payload. The complete context contract and producer/consumer changes were independently reviewed upstream; current maintained integration and the actual full regression are verified here. Generated snapshot changes must be rebuilt from maintained configuration and adapters.

### tests/test_pathbank_context_authority.py

ownership: supported. Targets: owner-8.

Whole maintained owner equals the accepted deterministic runtime/configuration/native-output payload. The complete context contract and producer/consumer changes were independently reviewed upstream; current maintained integration and the actual full regression are verified here. Generated snapshot changes must be rebuilt from maintained configuration and adapters.

### Whole authority and checkout preservation

provenance: supported. Targets: owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8.

All prior authority objects, nested order and first owners survive. The 892-entry manifest preserves all 887 old rows; ontology and Rhea are unchanged. All 240 old records/pages, 124 review pairs and 408 histories remain exact. Two actual histories precede SSSOM and first rendering.

### Whole graph and current page

graph: supported. Targets: owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8.

All 58 edges, 44 display nodes, four qualifiers, 42 references and 43 identities resolve. Current KGX has 4357 nodes/12110 edges and preserves all 12052 old edges plus prior node payloads/order. Only six shared nodes gain exact target contexts; no aggregate field or category-union changes.

### Complete source mappings

representation: supported. Targets: owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8.

Native SSSOM preserves complete header and 62 old rows, every cell, multiplicity and relative order; it adds four exact target mappings for 66 total, following native subject sorting.

### Fresh maintained validation

schema: supported. Targets: owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8.

All nine native gates passed for 241 records: 4773 tests passed, 3 skipped and 3 warnings retained. Render, skills, validation, lint, KGX, vendored, diff and site-current evidence is complete. Native execution was by the integration agent; this reviewer verified receipts and streams rather than rerunning passing broad gates.

### Whole evidence provenance

completeness: supported. Targets: owner-1, owner-2, owner-3, owner-4, owner-5, owner-6, owner-7, owner-8.

Accepted preparation retains 2761 whole bodies, 1844 reused and 917 new, across 14 current packets; 891 authority originals and all 92 acquisition attempts/66 received scientific bodies are retained. All 42 reference hashes resolve. The preparer complete portable replay is inherited; the maintained index and payload bytes are freshly bound. Both resolved local technical findings and original failures remain available.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native-history-1 | research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/history-1.execution.json | supports | Actual native command and complete original streams verified. Executed by the integration agent; this reviewer did not repeat it. |
| native-history-2 | research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/history-2.execution.json | supports | Actual native command and complete original streams verified. Executed by the integration agent; this reviewer did not repeat it. |
| native-sssom | research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/sssom.execution.json | supports | Actual native command and complete original streams verified. Executed by the integration agent; this reviewer did not repeat it. |
| native-render | research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/render.execution.json | supports | Actual native command and complete original streams verified. Executed by the integration agent; this reviewer did not repeat it. |
| native-skills | research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/skills.execution.json | supports | Actual native command and complete original streams verified. Executed by the integration agent; this reviewer did not repeat it. |
| native-validate | research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/validate.execution.json | supports | Actual native command and complete original streams verified. Executed by the integration agent; this reviewer did not repeat it. |
| native-tests | research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/tests.execution.json | supports | Actual native command and complete original streams verified. Executed by the integration agent; this reviewer did not repeat it. |
| native-lint | research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/lint.execution.json | supports | Actual native command and complete original streams verified. Executed by the integration agent; this reviewer did not repeat it. |
| native-kgx | research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/kgx.execution.json | supports | Actual native command and complete original streams verified. Executed by the integration agent; this reviewer did not repeat it. |
| native-vendored | research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/vendored-gate/vendored.execution.json | supports | Actual native command and complete original streams verified. Executed by the integration agent; this reviewer did not repeat it. |
| native-diff-check | research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/diff-check.execution.json | supports | Actual native command and complete original streams verified. Executed by the integration agent; this reviewer did not repeat it. |
| native-site-current | research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/site-current.execution.json | supports | Actual native command and complete original streams verified. Executed by the integration agent; this reviewer did not repeat it. |
| independent-target | research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/target.execution.json | supports | This independent reviewer executed complete current target/render/export or physical checkout/cache checks after native gates completed. |
| independent-checkout | research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/checkout.execution.json | supports | This independent reviewer executed complete current target/render/export or physical checkout/cache checks after native gates completed. |
| native-packet | research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/native-execution-intake.json | supports | Fresh ignored-inclusive no-follow closure of the exact sealed81-artifact native gate packet plus two seals; every complete receipt and stream remains byte bound. |
| canonical | research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/canonical-acceptance.json | supports | Root accepted whole native source/ontology outputs and independent old-object/order/KGX preservation review. |
| prior-actual-audit | research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/prior-actual-review-handoff.json | supports | This reviewer previously audited all 1921 actual artifacts plus two seals, whole scientific corpus, complete source objects/order, all selectors and complete KGX. That unchanged audit is inherited explicitly. |
| integration | research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/integration-acceptance.json | supports | Root accepted exact 18 destinations, nine primary owners, complete guards/native stages and hidden/ignored baseline/cache. The preparer 2761-body portable replay is inherited. |
| implementation | research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/implementation-acceptance.json | supports | The incomplete child PathWhiz/interface reference context finding is resolved; this reviewer previously ran 191 focused tests and 34 independent controls. That exact reviewed implementation contract is inherited. |
| ordering | research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/order-acceptance.json | supports | Root independently reproduced the old context-owner order defect and fixed deterministic serialization across five hash seeds. The only production correction is explicit metadata field order; prior identities, values and validation remain unchanged. |
| target-results | research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/target-qa.json | supports | Complete maintained scoped YAML, 58 arrows, 44 display nodes, four qualifiers, 43 identities, 42 references and rendered evidence checked. Authorities and whole exports equal accepted native bodies; SSSOM retains 62 old plus four new rows. |
| checkout-results | research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/checkout-preservation.json | supports | Ignored-inclusive complete physical owners/cache checked. All 240 old records/pages, 124 review pairs and 408 histories remain exact; only declared owners/generated files and two histories change. |
| visual | research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/visual-assessment.json | supports | Whole maintained SVG/CSS/JS equal the root-viewed scoped preview; root static visual appraisal is inherited explicitly, with dense junctions, truncated labels and blank canvas limitations. |
| preview | research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/preview-acceptance.json | supports | Root personally viewed the complete corrected-target static light graph; no browser interaction, responsive, dark or print acceptance. |

## Limits And Additional Notes

- Prior complete implementation adversarial tests, actual canonical audit and accepted preparation portable replay are inherited explicitly; current maintained page, exports, owners, full physical inventory/cache and native gate receipt/streams are freshly checked.
- The root personally viewed static light scoped preview is inherited only after whole current SVG/CSS/JS equality. This reviewer claims no new visual or browser interaction test. Dense junctions, label truncation and blank canvas remain; responsive, keyboard, dark and print behavior are untested.
- Actual regression retains 3 skips and 3 warnings with 4773 passes.
- Evidence references name planned concrete dossier destinations. Native save requires exact-byte evidence adoption and a current-input recheck; this external proposal is not a saved native review.
- Native inspection followed completed gates and independent maintained QA; every captured current input hash was rechecked before this proposal.
- The technical review uses the native repository review schema/serialization contract; it does not claim the separate full scientific skill workflow.
- Original local findings pathbank240-incomplete-interface-context and pathbank240-context-owner-order remain distinct from their accepted successor dispositions; no GitHub issue is claimed.
- No SQL full hashes, broad test suites or native builders were repeated by this reviewer; no maintained product edit, native save, public action or licensing clearance occurred.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T000501Z-pathbank240-technical
kind: repository
repository: CultureBotAI/PathwayMech
title: Technical review of E. coli spermidine PathBank context integration
started_at: '2026-10-13T00:04:04Z'
finished_at: '2026-10-13T00:05:01Z'
reviewer:
  identity: Codex /root/adapter_continue
  kind: agent
  independence: independent
  independence_basis: This reviewer did not author the scientific record, production
    adapter, canonical preparation/execution, maintained adoption or native gate execution.
    The reviewer previously independently audited the complete context implementation
    and actual canonical outputs, and authored only external review helpers/artifacts.
    The later ordering correction is inherited from distinct root independent review.
    Independent SCI review belongs to a separate agent.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Eight exact technical owners pass current maintained integration review.
  All old objects/files/cache, complete mappings and current graph are preserved;
  actual native gates pass. Both resolved local context findings, inherited science
  and static layout limits remain explicit.
source:
  git_revision: 5eb77a4b8039e98d9b53a61d09af52fa9f5b3d7a
  state: working_tree
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: conf/identifier_policy.yaml
    sha256: f2991a22f16f0d14d83226c6ac261bc779b253b2547fae9724474d8596b411c7
    role: context
  - path: conf/identifier_sources.json
    sha256: df3d89e4cb7c06970f5092b3febd1a16118391375d9ae17e85bad6dc69f167c8
    role: target
  - path: conf/rhea_identifier_updates.json
    sha256: 5c6a356a56a4b4df882ac2898587576216895a07fc2b455082da136ebd91a49d
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: f155aeff12118e7aa7176c58f32ea231ad61fa25cd43a1c90aa6ff6f383ef9e2
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 6bb6f0e5b7def56b35cd94fc5828e9429e9c7025a1f93da5248f7838e91f2391
    role: target
  - path: data/pathways/spermidine-biosynthesis-and-metabolism-escherichia-coli.yaml
    sha256: 0adef1da2d818af7c62d7e3952b2115585b47b8f132ec189cde2b435d2721680
    role: context
  - path: docs/record-review-profile.md
    sha256: f3f00eebb7841e9d5ac891271e269f45e926995e16856b8e9a885436570c7819
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: output/kgx/edges.tsv
    sha256: 9be8042b255d61750887d0cbfa78da5440b340420cc0f502aed86ea28341992e
    role: context
  - path: output/kgx/nodes.tsv
    sha256: e40e2a5d141473c7430c5c11af31129c1173f09361b2e6183dccb66f77517894
    role: context
  - path: output/sssom/source_mappings.sssom.tsv
    sha256: 0fb8b80e1f2fab8846e22a552fb4b9660f878704cdbe977763de84f0d5bde30d
    role: context
  - path: pages/records/PathBank_SMP0002097.html
    sha256: b300e5a2bae4e5b6c1ae0f6557ff3429936dfd1ae4dcaf8d46b3b21747d0d5fa
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/README.md
    sha256: 6c039831841b5711bb0e4ec8f4981f22af3de46aa214248c70f570310b518513
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/archives/evidence-bodies.zip.part-001
    sha256: d2cbbf665f993b4cd07c5fc2aaca999228ef89ada28ac343ba0d4556f9cae860
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/archives/integration-preparation.zip
    sha256: 1b06b49ca4339dd8674fa61bda31551ec4e0822223bda9074cce1a811abd63ad
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/common.py.gz
    sha256: a725ab367f79affdf42f05891f736bc1b6f1a9f3d3cfad56afa8876c109a81c6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/evidence-index.json.gz
    sha256: ecb1e1f7fd746a625eaebf58dcb777841393a6fcef35069fab7d04b5152fb236
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/external-packet-closures.json.gz
    sha256: 3d36adb31c01251494bb4299236f80f947367ab87ce64bbea53c67c2b161430b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/integration-preparation.json
    sha256: b1c305e5bd9231e05bbdd2ff13c941f7fd00b98ad5cb2847417c7593a9479b2e
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/local-integration-decision.json
    sha256: 2eea2749fd751f5b4cbf73e6928ed575e6d76640eed3a5063b30d757bbcc7067
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/README.md
    sha256: 1ef1684d96b94f6ffb1659ef2147c7476d81167c4ecc4c12125643b5e68ac14c
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/finalization-plan.zip
    sha256: 4c70a40fe33a4cdff3e76b2e118b527bfb7b92e2d8d9c280790a20499a669b48
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/REPORT.md
    sha256: 8ca4929c00b70667078bdf05e90b184fc0e674faece776d45c6bbf25393fe30e
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/accepted-reading.json
    sha256: a1aacc2999e69f4b66efdf7b083628255af5f1b404dfce6c16867faad31613c4
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native-copy.json
    sha256: 9881268fa4c2db9369ca232356ddf180ba2811963a03db330a24eebb55a3e418
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/REPORT.md
    sha256: c1e05640680b61499a171c723a9774d1e4661007fd24176da08fd9b22e98be28
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/actual-tool-provenance.json
    sha256: 268598db5a99336a56569458d99cc4357262cd88d771b3868b5380f4489bd6db
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/artifact-manifest.json
    sha256: 77b5cb3c57695411c9653df8899a277fcf98311890b32e889daaa0d118d5f9e3
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/execution-summary.json
    sha256: a39e049540d0aa4ce4a5be56da7aa91729e0e970ad3606c04fa6beb6b96996ec
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/completion.json
    sha256: 4858b5f869c00c8159b39008709a70be0dccd2ae64b7c801ae5c960de0c07f3d
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/diff-check.execution.json
    sha256: 6020c09c830834e303806ad929121b9ca2a4f892c1198331dd3e5db9111932d6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/diff-check.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/diff-check.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/phase-start.json
    sha256: bfef57046998134c2a3fe1f241780094bf0ab5dbee7381003c38d3bbcf33998b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/runner-at-start.py.gz
    sha256: 466d5c9f79634f3f840878cfa31c4fe3c8592d81c23edf8fdd72c58e88fcdce6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/site-current.execution.json
    sha256: 03aca7888d8518a34bc3dbbee1bf53682672b68498e2ec4163669a9286352a09
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/site-current.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/site-current.stdout
    sha256: 6a3c7d3b2baaabf37a5603b1181a253b7c3170047f6eb4bd14fcdae0b57a9a6e
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/handoff.json
    sha256: 60f2975595c25f337752cedcb300171937b4d5044d570b28bc70903bfe234575
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/completion.json
    sha256: 7d00b090a8f2e50647215f6f2ee6de386afa32323a37b3ecc1664a4f55f247eb
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/histories-before-generation.json
    sha256: 133612d98e007dd70d093acc2d808eb62ce2eca5992c47c346d572e93ad0a9ea
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/history-1.execution.json
    sha256: d89fab8fc11cd861d03e1d976f1a56e1adf597e6aac3ba856cbab2c523b125c0
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/history-1.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/history-1.stdout
    sha256: 96ce2a0b5b8c0b7004c35224d43b4d8276d9587201ea09b09efcf6c11d02622c
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/history-2.execution.json
    sha256: f099a9f0c7abfdb408c6aa18d62fa9a6dabd3359e631ddf196f583713a9f7756
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/history-2.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/history-2.stdout
    sha256: 2e0e5cda18318279feee5fc4e6b706883975fe88936737367a4c7b79011ab403
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/phase-start.json
    sha256: 59f3d47f964fda34e742dc708233dde992896d0e51c26f01d219deab646b6723
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/render.execution.json
    sha256: 55f02fa84b35cb747620aff98e1b074b083e975da676ab1198555e4c53bf6f5c
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/render.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/render.stdout
    sha256: 99cdbab169addc85b5c762d238e48a9d50b57165d32caa5aa1d4f5f7876c394e
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/runner-at-start.py.gz
    sha256: 466d5c9f79634f3f840878cfa31c4fe3c8592d81c23edf8fdd72c58e88fcdce6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/skills.execution.json
    sha256: bd29e269e6ac5e2ee7a58b72f435ad245e0c8ecc235009097745a8fe71001500
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/skills.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/skills.stdout
    sha256: aa2d3652343b880d16a176d45deb7b4907fb11f43e31f1840d7724658478a527
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/sssom-preservation.json
    sha256: 114bf445aba0ccd63435622bd04a294924947648835bc8de00973fe171c2f167
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/sssom.execution.json
    sha256: f960632565146eb4f37b6d28b558f1ff877c61d790bb6b5021399fbdc73307fd
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/sssom.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/sssom.stdout
    sha256: 2ff0a41c2e52f79a6579a91a5dd2cbd0571336d39c214361f630978718aade23
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/input-receipts/adoption.json
    sha256: 203298ee3d6c4434a1822a108cd89d8f26a78bc256a98b6ba54e7fdd34c7b76b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/input-receipts/root-acceptance.json
    sha256: 3871988b2223c3f7d660f10e709ed8b5145b057913534b0de27b61f8b36f086f
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/input-receipts/runner-binding.json
    sha256: eeecd47b7716111255ae78e0420244ef7fd64d190a069b056e638efa6cbd59ad
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/input-receipts/sealer-lineage.json
    sha256: 7ce901d90a07c2475d5855daa2fc704e07c77b6d461566549ed7a62aff44a232
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/input-receipts/sealer-predecessor.patch
    sha256: a617d5bac0a6e2b5effe32647ceaf9f60bdd0516ed2bd07e55ed33bf79ea1744
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/input-receipts/stages.json
    sha256: 5e1cfe5b3b3b12603375718fbb264717f0d5f236d094ec73cb898487b5e953d5
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/adoption/execution.json
    sha256: 5e00c1de5cf3600c661051f0e078b368f3ceadc1b3e43c23cddd0cd6bd6b41f5
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/adoption/helper-at-start.py.gz
    sha256: 809e44820f0eab39178e59bef7db27f09e6485631b4ec8eb77c11cceb8afe18e
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/adoption/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/adoption/stdout
    sha256: 4c471337a9cab01102d6104be401af59991af4b71637f341fc0c84c9706005d4
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/capture-wrapper.py.gz
    sha256: 4f14d326e9cbb7c563fb67f335c5f57a07656d90d2f08baf67975ae65f75ec83
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/final-gates/execution.json
    sha256: fef6d9f16cd45a57b3261271ebb595559e56c108af831caa5b3f3467af369f08
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/final-gates/helper-at-start.py.gz
    sha256: 466d5c9f79634f3f840878cfa31c4fe3c8592d81c23edf8fdd72c58e88fcdce6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/final-gates/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/final-gates/stdout
    sha256: e0eb1de2bb525e1d043cf22f993d098fe16ec031803904d2a1eca89c598bbb30
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/history-and-generation/execution.json
    sha256: 7731699dcf9e035e9a42e925b1aeb7267b0467a820bccf1d2a0d14bff3ac0b8a
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/history-and-generation/helper-at-start.py.gz
    sha256: 466d5c9f79634f3f840878cfa31c4fe3c8592d81c23edf8fdd72c58e88fcdce6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/history-and-generation/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/history-and-generation/stdout
    sha256: 4e1711fc1871d8451764b7d31be861b997991358d99efe04e3656ce15299e4cd
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/remaining-offline-gates/execution.json
    sha256: ffdce826b07ee098ff65a986722923997402a0b7ce521cd02e409eae2796ded1
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/remaining-offline-gates/helper-at-start.py.gz
    sha256: 466d5c9f79634f3f840878cfa31c4fe3c8592d81c23edf8fdd72c58e88fcdce6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/remaining-offline-gates/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/remaining-offline-gates/stdout
    sha256: 4ca0afd118684c623bbc1477b37a197ffe8de0df5ea39d046395180b59bec32c
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/vendored-gate/execution.json
    sha256: 3351f99dc0cc5506fb8c682862c71d7de540ec354c336cee6c747dd550be81d9
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/vendored-gate/helper-at-start.py.gz
    sha256: 466d5c9f79634f3f840878cfa31c4fe3c8592d81c23edf8fdd72c58e88fcdce6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/vendored-gate/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/outer-tool-streams/vendored-gate/stdout
    sha256: 6f4766d39be12b3694deefa1eef1d4c1eace07b8dae134bf29e2a6f596e28ae8
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/completion.json
    sha256: 5205cd01da7da8b293e5dd64e9abea412c1d7603bc5b2c77c82dd52c81b0f860
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/kgx.execution.json
    sha256: 1a0b8783b92bfbb80d92b5bb0fa946edf37f131e0d39b67e87843bce5739287e
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/kgx.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/kgx.stdout
    sha256: bfe34680175c1f91ae12c8435ca73a7ce32349d79c74b7e1b88ec1f2fccb2b13
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/lint.execution.json
    sha256: f53a17171b605412e6926cd6d760c5d8917bd38d625fe83e495cb422557766f9
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/lint.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/lint.stdout
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/phase-start.json
    sha256: 25fa92016a01a8e030e05d3729df1bc067eabb6e15639151642116516cd972ce
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/runner-at-start.py.gz
    sha256: 466d5c9f79634f3f840878cfa31c4fe3c8592d81c23edf8fdd72c58e88fcdce6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/tests.execution.json
    sha256: 96ed16641526398d18ebbd2cfcacc644adfb2b9aea38d8ebced5d9791051d41b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/tests.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/tests.stdout
    sha256: 3da3143786475e65cfab16526423a6e45bbc65139abf70cf4cffa5b6d5948225
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/validate.execution.json
    sha256: 1700dc731723f94513c7a20429e7f7b6f328a860d57b7bc0c2e7b7ccfa730fc9
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/validate.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/validate.stdout
    sha256: 211c8cd27b4e6e15dd719a73f6671906426d34be72372853195aefdf050f4d13
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/sealing-helper.py.gz
    sha256: dc92d42ce0682ed3a0232cf5d631364a5d64fe1298c8929637a6588d64c9dc1d
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/vendored-gate/completion.json
    sha256: 06655f7b9c5e9d17741188120afdaa5dc2d5e5f9294d3c93d8e32a1d5e32d39e
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/vendored-gate/phase-start.json
    sha256: d9e63ff4734e6dbf5b6400a1b8064d1862c3ddcc1b43e5c38e3b9aeb64ccd2be
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/vendored-gate/runner-at-start.py.gz
    sha256: 466d5c9f79634f3f840878cfa31c4fe3c8592d81c23edf8fdd72c58e88fcdce6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/vendored-gate/vendored.execution.json
    sha256: ddc5645c3a5caf68648b6c061595488cd578f9d50c96e3a265850be1af4d5580
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/vendored-gate/vendored.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/vendored-gate/vendored.stdout
    sha256: 3b073aa29da7dc3996edbe18c83d0d6593ba6d03238b663efc40286be4cf428e
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-tool-provenance.json
    sha256: 840b07287987db7b7c47d2e27ea6fdeed113639a2f2b9751b7c4b42568352814
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/artifact-manifest.json
    sha256: 76342db9c8c893bd105087977ae90b8dd144247f71324f9b3281b9ecc360c108
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/completed-review-ready.yaml
    sha256: 5746d02cd0ceddf927e533b64537fa5b5958039c64c8c4040533a5d4ccb14436
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/completed-review.yaml
    sha256: 5746d02cd0ceddf927e533b64537fa5b5958039c64c8c4040533a5d4ccb14436
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/currentness-checker-correction.json
    sha256: fccf442c87828c9a2333c4bc3c496e69373d41f766ba49239d419e11a52dcf4a
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/currentness-checker-correction.patch
    sha256: fdd89e5c1b09bef98d3300fbd69bf00037911ad89465bde000ce22b0ab9dfdbb
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/durable-adoption-instructions.json
    sha256: 03259cae11c39b0aeeb2435a46bd18aa4bb58f4eabf4798dfba6b74dc6d59602
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/edge-appraisals.json
    sha256: 69d7b71f9fec5032c811899d4a1ebbf205ecbbfc921c1337da65a43d8d698a7b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/final-native-inspect/completion.json
    sha256: 39be6a5e1668682ba0a2634c819ca8992c544cb1fd28391147dc168c75405a71
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/final-native-inspect/helper.py.gz
    sha256: 0b33fc307b600cc6e3009198f44f0ae85f4af15899d12a5c43f1b9ac74291a60
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/final-native-inspect/start.json
    sha256: 67df58482b908c1cfc939ba54e589a0d72c2ce5fbec2b09bf5cbc479f3d1e832
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/final-native-inspect/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/final-native-inspect/stdout
    sha256: 7bc410395ec58392e53c195f733e7afff50b3fded6dffab25aeb80930d6a7ee2
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/maintained-science-currentness-corrected/completion.json
    sha256: 3379cc9ffed83f1b7267c5a593b97cf5e771f1625706b80265f333f9e3e068ee
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/maintained-science-currentness-corrected/helper.py.gz
    sha256: 7a8b583d4e5837b7055d71ae4d1b6c7ce4d98ae3b7d359bbdbb74a69ccb70c2b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/maintained-science-currentness-corrected/start.json
    sha256: 0be98c602bf3a127ac241c41fabd056108ca7d9d0d4c257a63356c234cfa0cdc
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/maintained-science-currentness-corrected/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/maintained-science-currentness-corrected/stdout
    sha256: f2c20d983406be003cb4d368270ad0ad73e2d10fd51980e042dfa0937f1a2fe8
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/maintained-science-currentness/completion.json
    sha256: 794059d4f1a4c36801e8f3b745072dfaf58c7a20a8b99f56ca9ef556d09d664b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/maintained-science-currentness/helper.py.gz
    sha256: 18aec409dafd05f37796accbc04852701b7033d2d68205c54b1fc584e4f00345
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/maintained-science-currentness/start.json
    sha256: a523a2eecd0d1ca17df70df44a972308798de75817715141af93b9e2140d41e4
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/maintained-science-currentness/stderr
    sha256: 0c404ab80ed46b53879efcd281845e5216327ddcf5d1d64f9ceb98d4387f58bb
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/maintained-science-currentness/stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/native-validation/completion.json
    sha256: 300099d1facd5913689fe2931e9166928942c3f1f6193e74d7c3403067e5196d
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/native-validation/helper.py.gz
    sha256: bb2d8d21a2e264797331c22023b351233353b813af960994ad612a2bf086e0a3
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/native-validation/start.json
    sha256: 9ed257bc4d6f2f16021fcee8c83511cd76c5fb691801f0afc7018ee92e476902
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/native-validation/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/native-validation/stdout
    sha256: 8a7621cc6f2fe227c6a2e421a486d294c081e0ee284f03f6845811a10f5f8cff
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/serialize-scientific/completion.json
    sha256: 277d106281173f81b26d5427f3d81d1cdadfdc9f9b31fea69d92924f27af272f
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/serialize-scientific/helper.py.gz
    sha256: fbef8762e2f4510c3b0954d32f74ed99c8f9085dd392d891ca957fa905f468f7
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/serialize-scientific/start.json
    sha256: 55c8f226d5afc8855700550a607d0232c9a947d53a7a239c1903834369b4f7f6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/serialize-scientific/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/executions/serialize-scientific/stdout
    sha256: 08ccd581b9921430a2aff507b24fcc99c6e91f2b6818f4db0df1838625c3fb34
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/final-current-bindings.json
    sha256: eadbd8aa199dffc025d2fe299dfe5722148cbe32a630162c7c83e6abf2d789f3
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/final-native-binding.json
    sha256: 3b75e286b949ca87a1c13c01315800e9e172964e3b318a17e2edcb4d6706bfc7
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/final-review-summary.json
    sha256: 034edf34eb5ef87ca9104636c88e5525dc6dae6ed4965cb323176246a313b95b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/final-shared-QA-binding.json
    sha256: 34500de4fe1ea1745933e18b38bdfa02ca1e7126bdc9cbafa3c31fb6ed4a7cc9
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/finalize_science.py.final-predecessor.patch
    sha256: 891576ae92cb42f1e00be147f5e74cfb14bfadfba842231e8b9686300889b623
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/finalize_science.py.gz
    sha256: fbef8762e2f4510c3b0954d32f74ed99c8f9085dd392d891ca957fa905f468f7
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/handoff.json
    sha256: 451462ac9d26eb1e8793cc147ac4dad47200e7cecbff392fcd52fe9b444b8d0f
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/helper-lineage-final.json
    sha256: c3ace448643177dc1f59ba9b79b0e3c477a0b68258926dd6ce082e53d5d079f1
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/helper-lineage.json
    sha256: 1e42eafe9785c3f95286548b20c855e82e10010cc65f678a5cbbbcba738e9368
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/history/initial-currentness/edge-appraisals.json
    sha256: 69d7b71f9fec5032c811899d4a1ebbf205ecbbfc921c1337da65a43d8d698a7b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/history/initial-currentness/identity-appraisals.json
    sha256: 40168eb2afc75eddfc525152c465b36fe8fbb3fdf44592534cc548e06b933558
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/history/initial-currentness/mapping-appraisals.json
    sha256: 6ec1e1d58ac2eeb7cb52936dfdc2558460b2ad8b2ec901735828f2efb38027d3
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/history/initial-currentness/paragraph-appraisals.json
    sha256: ac4f2e875ad13ffcfb758f8019dadabe817c1583b3dcbc01a39ee1190dcd809a
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/history/initial-currentness/qualifier-appraisals.json
    sha256: 3a3fba94f1a24cbb9f187ca3024ba85d359e741737c661e021f7c31e6e867f1b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/history/initial-currentness/reference-appraisals.json
    sha256: 05861883dbc15fcfb5cb174d12bf65b4e166ecee30b65e818b5a7c2cd1596a74
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/history/initial-currentness/whole-source-closure.json
    sha256: 7d6042c3591e0f1f604b305476d99ac88306866c2f9a52663c110acdeeb09e5b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/identity-appraisals.json
    sha256: 40168eb2afc75eddfc525152c465b36fe8fbb3fdf44592534cc548e06b933558
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/incidental-final-header-read.json
    sha256: aeeafad5d5a66edb449ab93e47ed56a76a2fc22cbc4284278633487243bd5441
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/inspect_final.py.final-predecessor.patch
    sha256: c9c91e668eba9876c1fda0ff228e36e70c09a1016df44c919a9923b0801d26b7
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/inspect_final.py.gz
    sha256: 0b33fc307b600cc6e3009198f44f0ae85f4af15899d12a5c43f1b9ac74291a60
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/inspect_final.py.predecessor.patch
    sha256: c9c91e668eba9876c1fda0ff228e36e70c09a1016df44c919a9923b0801d26b7
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/locator-currentness.json
    sha256: ebeb059bd26fe93235d8db6c2ae9c03d14a397a1416e684bd53de0898300a304
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/mapping-appraisals.json
    sha256: 6ec1e1d58ac2eeb7cb52936dfdc2558460b2ad8b2ec901735828f2efb38027d3
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/native-inspection.execution.json
    sha256: d4d0029740b3fdaf63b6b4c3e609d2f419d208f1d1cf3c85a111e52b1e084e2a
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/native-inspection.json
    sha256: 36558c5853e7537011713ebabea33d990d8295a488fdeb32aec0f3f425b00f4a
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/native-inspection.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/native-validation.execution.json
    sha256: ed1a9da6a10f2b2cb5461e39b4d88d2cfd8e5023c04834ab7f44175301fc2d97
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/native-validation.stderr
    sha256: e2cf5a8ee56373cb7afeb23be8ac2a30d67f13afa55bb51424877fc908e2a25f
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/native-validation.stdout
    sha256: b42ee0197bdb886694684431f9da0d2fba4020263ed572ff756b9eaf0b042ba6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/paragraph-appraisals.json
    sha256: ac4f2e875ad13ffcfb758f8019dadabe817c1583b3dcbc01a39ee1190dcd809a
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/planned-native-commands.json
    sha256: 0da2bf241317b25adc1679685c88b4334c75a90b0ada9e947ca19afa0632a554
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/preparation-results.json
    sha256: 8eefa5b0e84a64e31053417ac2f9920e79830ce2dcf6c1c9469ecaefcd2129c6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/prepare_science.py.final-predecessor.patch
    sha256: 550adc31de5671664fbfa58701b67702de1f126f7d2dc92ba01b9e8fa16a65ec
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/prepare_science.py.gz
    sha256: 7a8b583d4e5837b7055d71ae4d1b6c7ce4d98ae3b7d359bbdbb74a69ccb70c2b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/prepare_science.py.predecessor.patch
    sha256: 550adc31de5671664fbfa58701b67702de1f126f7d2dc92ba01b9e8fa16a65ec
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/prereading.json
    sha256: 929e79dbf564d94c8340fe29232c793bda2c669688422d86c5246f1dab7a2ac2
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/prior-native-review-search.json
    sha256: 9fb0303397f0aaa0b62728e819f08ddf2d3a4580e78d12f46ea477d6239ebcb7
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/qualifier-appraisals.json
    sha256: 3a3fba94f1a24cbb9f187ca3024ba85d359e741737c661e021f7c31e6e867f1b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/read-coverage-final.json
    sha256: 2cce0bd5eb9a7cf50fc28f2fca1c0491792aec29ac9dcae7d6a508448088f903
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/reference-appraisals.json
    sha256: 05861883dbc15fcfb5cb174d12bf65b4e166ecee30b65e818b5a7c2cd1596a74
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/run_step.py.final-predecessor.patch
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/run_step.py.gz
    sha256: 87a5a0b4b49d92c272bf799aed2cf7c3aba964bc17465e6f46d6fe37f4870ec0
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/run_step.py.predecessor.patch
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/scientific-judgment.json
    sha256: 9a0541fd1d1a2e0dc8bb18047096ebefc38b427aedb575a77f1bd67f9c071219
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/seal_review.py.final-predecessor.patch
    sha256: f8ae6caef20a7d1f5e18ac82d9818b2fb3d6688e85ce4effd2c5f2c12d75294a
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/seal_review.py.gz
    sha256: 88aa48680aca99ca26fb87ae617359cec4ed28df652bfdd89378d3bad5108871
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/sealing-currentness.json
    sha256: d3038e961ad7e0cd0288f11e131a41f8b2bf60510a844f8a98b7a856ad8cc6e5
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/shared-QA-currentness.json
    sha256: d8e4a67ed5a581e89f236553b37177fa74a7312f6a938ff5d35f69785968ad91
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/shared-target-results-read.json
    sha256: a8d75e8f73079df4a6667a3cd5d087d0f670b18034e37f4a2c561a29feba8ac4
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/targets.yaml
    sha256: 422ca59250057dc5914b9721a9f21fe1c73539d7fd5b2bd654e9e80ea7f13055
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/validate_proposal.py.final-predecessor.patch
    sha256: 568c019af97bda9b278b3bb433c5ab04d2199989085aa627b0506ed133ec14df
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/validate_proposal.py.gz
    sha256: bb2d8d21a2e264797331c22023b351233353b813af960994ad612a2bf086e0a3
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/validate_proposal.py.predecessor.patch
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/whole-source-closure.json
    sha256: e712700e284e7edb5f652efb88a6ef42b1fde81b806790ccbe07c31d5f9cc748
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/REPORT.md
    sha256: 99a3120b94f2bdf941e8db1718c5213605880da4291c39eb22064c7a547f75aa
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/actual-review-tools.json
    sha256: 0b1f60d3d53682a273cc2ab3f1e4dad277d4b9f503055fbbab6bbb5cb8a65c38
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/artifact-manifest.json
    sha256: 1d7ec6ae1ba2250fef86b144aeeeb01d95e0968f93a6382bcdcaa025b9d46b94
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/canonical-acceptance.json
    sha256: 951053a78a7123c8ac43019db578873877bd89d5b1c177dbb9543675fb3c4938
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/check_checkout.py.gz
    sha256: 772c2b32df95c275de665246b1fac858b6a6fb13cb8f6e2d2f1ea93b07d2e26e
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/check_target.py.gz
    sha256: ee08636013e2a1abcda645f5af1cfb3159d049bce6c2e01accf264ccd59c9098
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/checkout-preservation.json
    sha256: 418bcc73cc0697c4bbf19000646aef22c05c52b6126f260308c2838d7cb2cecd
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/checkout.execution.json
    sha256: 41cd780064d4e710d03a62946c6cb18d2054a037a1f2c7663bd7f240eb7f77ca
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/checkout.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/checkout.stdout
    sha256: 981e1fb7d02b2a8a547815165ef105ad7a37b8ab58151f27aec793ddd88033b9
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/handoff.json
    sha256: 48984f231ec9dc5eba226668c751347ca80f4b1f7452abbf6bdb82e653fa414b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/helper-lineage.json
    sha256: 57605a7529c086b215c0145bf266c934ed6dec102f4fd09e435ff3fb531f5df0
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/helper-rebase.patch
    sha256: 7a39b340807921c82ec0896a063c20278e26a1f01aa2d05c29f71f99f687725b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/implementation-acceptance.json
    sha256: 3cd2e4509b6edc4f738e02a554a7c0b4327da1790d899c36ea38af244415dd4e
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/incidental-lookups.json
    sha256: 8bb7a63bee22fefa0ed11ba76153c41b8cf8ca3b15f723e3103b2d15609fff6d
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/inspect_technical.py.gz
    sha256: 3b6c259279f2face75f94468390ec8e15c12eb8beb47c8d1e16e01a4a2bd50d5
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/integration-acceptance.json
    sha256: 3871988b2223c3f7d660f10e709ed8b5145b057913534b0de27b61f8b36f086f
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/native-execution-intake.json
    sha256: c2a31555258f35c470c697d34050c350f16b3c8d389b6b142173df3f0dce40fb
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/order-acceptance.json
    sha256: 319ce1daa083b9c77abbd5189a59d40704b268165e0d0f849fc27cba337398bf
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/preview-acceptance.json
    sha256: 1ea16397ca767965f4fab59b6742dd74106a83e647483687da282b1104023df7
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/prior-actual-review-handoff.json
    sha256: 243571dc5b62d1171af8c326f2dff30d7234fd2dda92f17b1502c47c1d630538
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/review-result.json
    sha256: 4c98a98f54d09a1ff45b5b82e039a9fd2d65f34d4cd6392e35fc7211e45118df
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/run_qa.py.gz
    sha256: e0015e7175886845eba91ff503d375afc8ae73bb1f0f52147aa55f88ef5f4e48
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/target-qa.json
    sha256: 8182168448450c0c06ecb43373c1797450779ca9e2bd13da5ea6eb745c9cce38
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/target.execution.json
    sha256: aa3ad62601d5f02c1fcfc1d9cba8234ae43fa4e2835e843f1813f5ead01b6312
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/target.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/target.stdout
    sha256: c836d939dca2ca1283a709ee939e01f3f02758ec422b79c5878f7153dd48de0c
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/technical-inspect.execution.json
    sha256: d3ebeb8fca00231a3d363df76510c8a4cf62a70de4e47874a239fee30fbd20e1
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/technical-inspect.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/technical-inspect.stdout
    sha256: 007ba0a9d7dc7a1316f89d3e17e52c1ce356f5db92b0a57fd94679012ef11665
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/technical-proposal.json
    sha256: 759abcea4507985d4af786eed9518403b12d0a4576ad0a51d55e5c667c49e4f9
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/technical-targets.json
    sha256: beeb5e836d7b380ed699ea7794c76e275ffe6249e9eb08ba880f9679aad59cee
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/technical-validate.execution.json
    sha256: a462f7eb03d3ce039bb04bae007eb8925171e2ee42a085de6aecc53ab40abdc1
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/technical-validate.stderr
    sha256: e2cf5a8ee56373cb7afeb23be8ac2a30d67f13afa55bb51424877fc908e2a25f
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/technical-validate.stdout
    sha256: b42ee0197bdb886694684431f9da0d2fba4020263ed572ff756b9eaf0b042ba6
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/validate_technical.py.gz
    sha256: 816e2551e75b7bf6b86a5f43f1b6dbeb28ffa5c93bd29be87eaed6461ab3dfe1
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/visual-assessment.json
    sha256: 03b396168ab33bb882fe94dfb4326c737c1a90b6225b5861e4f89e4e1e860ed9
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/write_technical_proposal.py.gz
    sha256: d1c18d51b6e20204d2f2613d6cdaa0030ae19ae3e1e46ea7426e725b94758c06
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/maintained-review-acceptance.json
    sha256: 14d51d6e9c06f73952b0e1ebb6c0b89984a1e952213f137758c861acc4096de7
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/root-storage-map.json
    sha256: 3bcda1b178813411740c7557b994825d5d8ac36988246fa07d0eba542a43a24e
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/scientific-review-acceptance.json
    sha256: 36073f4ee2b7a03945d74d9b410a8de627c8d1a7ab2548918df0557d47ad850b
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/native-integration/storage-ledger.json
    sha256: 0e35b5ba416cc9da5147ab5506268109bab60166b872acb9b0a17bca015673a7
    role: context
  - path: research/pathway_additions/2026-10-12-next-240/verify_portable.py.gz
    sha256: 039e18aa6cd8de2df6244c19ebb6847130827f4d8f072cf24b8e52c670206eaa
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/build_ontology_identifier_snapshot.py
    sha256: fc8bee76c1c07c4d3b86eb72021f8eaf8203ae339258ff16768dd3e1f1b2be81
    role: context
  - path: scripts/build_source_identifier_snapshot.py
    sha256: 7e483d89b36ec82c1e3f87cdcfd5b14f168474c31ea550905e6fb668cf41a9e0
    role: target
  - path: src/pathwaymech/identifiers.py
    sha256: 43898697bf0dd570f687d5179ebd30daae9eb26845f866f2ea18b4c9338bacf2
    role: target
  - path: src/pathwaymech/pathbank_context.py
    sha256: fc7ce7782678bf7c45786948425e4010e6d7bc3d811d6769d84012e0d0235f3c
    role: target
  - path: src/pathwaymech/schema.py
    sha256: bd99c1e6ca1f6eec5c82c58aa1ae3f43f696d30be66fbe0977dcace81292e0b8
    role: context
  - path: tests/fixtures/pathbank_context/SMP0002097.owl
    sha256: 03524344c6d1ba883c1fce39a48f852a1f92c3440542ccfe81d141ff9e862bf2
    role: target
  - path: tests/fixtures/pathbank_context/SMP0002097.receipt.json
    sha256: 4f7d881ee071e9e5270e928d5af1b7344ac278c1bb270a0fa332faa3baa0704a
    role: target
  - path: tests/test_pathbank_context_authority.py
    sha256: cc79ae33a7c3554a529faef34306733bb14537cb5ac0843237cb4d735d38e5b7
    role: target
scope:
  description: Eight runtime/configuration/fixture/test/authority owners after completed
    record 240 gates, with complete maintained context.
  selection: All eight nonrecord primary owners from committed 239 baseline 5eb77a4b8039e98d9b53a61d09af52fa9f5b3d7a;
    no sampling.
  coverage: full
  population_size: 8
  reviewed_target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  exclusions:
  - target: New primary scientific judgment
    reason: Separate independent maintained scientific review.
  - target: Publication and browser interaction
    reason: Not performed or authorized within this local technical review.
targets:
- target_id: owner-1
  path: conf/identifier_sources.json
  label: conf/identifier_sources.json
  kind: maintained
  ownership_note: Exact adopted source configuration, reviewed runtime/fixture/test,
    or native authority snapshot. Generated snapshots require rebuilding from maintained
    configuration and adapters.
- target_id: owner-2
  path: data/identifier_authorities/sources.json
  label: data/identifier_authorities/sources.json
  kind: maintained
  ownership_note: Exact adopted source configuration, reviewed runtime/fixture/test,
    or native authority snapshot. Generated snapshots require rebuilding from maintained
    configuration and adapters.
- target_id: owner-3
  path: scripts/build_source_identifier_snapshot.py
  label: scripts/build_source_identifier_snapshot.py
  kind: maintained
  ownership_note: Exact adopted source configuration, reviewed runtime/fixture/test,
    or native authority snapshot. Generated snapshots require rebuilding from maintained
    configuration and adapters.
- target_id: owner-4
  path: src/pathwaymech/identifiers.py
  label: src/pathwaymech/identifiers.py
  kind: maintained
  ownership_note: Exact adopted source configuration, reviewed runtime/fixture/test,
    or native authority snapshot. Generated snapshots require rebuilding from maintained
    configuration and adapters.
- target_id: owner-5
  path: src/pathwaymech/pathbank_context.py
  label: src/pathwaymech/pathbank_context.py
  kind: maintained
  ownership_note: Exact adopted source configuration, reviewed runtime/fixture/test,
    or native authority snapshot. Generated snapshots require rebuilding from maintained
    configuration and adapters.
- target_id: owner-6
  path: tests/fixtures/pathbank_context/SMP0002097.owl
  label: tests/fixtures/pathbank_context/SMP0002097.owl
  kind: maintained
  ownership_note: Exact adopted source configuration, reviewed runtime/fixture/test,
    or native authority snapshot. Generated snapshots require rebuilding from maintained
    configuration and adapters.
- target_id: owner-7
  path: tests/fixtures/pathbank_context/SMP0002097.receipt.json
  label: tests/fixtures/pathbank_context/SMP0002097.receipt.json
  kind: maintained
  ownership_note: Exact adopted source configuration, reviewed runtime/fixture/test,
    or native authority snapshot. Generated snapshots require rebuilding from maintained
    configuration and adapters.
- target_id: owner-8
  path: tests/test_pathbank_context_authority.py
  label: tests/test_pathbank_context_authority.py
  kind: maintained
  ownership_note: Exact adopted source configuration, reviewed runtime/fixture/test,
    or native authority snapshot. Generated snapshots require rebuilding from maintained
    configuration and adapters.
checks:
- check_id: native-history-1
  name: Actual native history-1
  status: passed
  required: false
  summary: Actual recorded process exited 0; scientific interpretation is separately
    reviewed.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B scripts/new_history_record.py
    --kind record --slug spermidine-biosynthesis-and-metabolism-escherichia-coli --target-root
    data/pathways --event CREATE --outcome changed --summary 'Add complete evidence-backed
    E. coli spermidine biosynthesis and metabolism.' --details 'Exact accepted scoped
    PathBank:SMP0002097:18 paragraphs,58 edges,4 qualifiers,43 IDs,42 references and4
    mappings; all four biochemical events plus transport,22 sides and generic SAM
    interface retained. Native assembly, taxon/construct, chemical-identity, transport
    and source-access limits remain. Whole original bodies and all92 acquisition attempts
    retained in research/pathway_additions/2026-10-12-next-240. Maintained gates/native
    review remain pending.' --actor-name codex --agent-tool codex --model gpt-6
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - native-history-1
- check_id: native-history-2
  name: Actual native history-2
  status: passed
  required: false
  summary: Actual recorded process exited 0; scientific interpretation is separately
    reviewed.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B scripts/new_history_record.py
    --kind infrastructure --slug pathbank240-native-authority --path scripts/build_source_identifier_snapshot.py
    --event EDIT --outcome changed --summary 'Integrate complete typed PathBank context
    and deterministic owner serialization.' --details 'Adopt reviewed280-file runtime
    via exact seven changed effective owners,892-row manifest retaining887 old entries,
    and actual source snapshot; ontology remains byte identical. Preserve both local
    findings pathbank240-incomplete-interface-context and pathbank240-context-owner-order,
    original failures and accepted dispositions. All old authority objects, first
    owners, graph rows and contexts remain exact. No aggregate field changes. Both
    histories precede SSSOM/render; maintained gates/native reviews remain pending.'
    --actor-name codex --agent-tool codex --model gpt-6
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - native-history-2
- check_id: native-sssom
  name: Actual native sssom
  status: passed
  required: true
  summary: Actual recorded process exited 0; scientific interpretation is separately
    reviewed.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B -c 'from
    pathwaymech.cli import export_sssom_main; raise SystemExit(export_sssom_main())'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - native-sssom
- check_id: native-render
  name: Actual native render
  status: passed
  required: true
  summary: Actual recorded process exited 0; scientific interpretation is separately
    reviewed.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B -c 'from
    pathwaymech.cli import render_pages_main; raise SystemExit(render_pages_main())'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - native-render
- check_id: native-skills
  name: Actual native skills
  status: passed
  required: true
  summary: Actual recorded process exited 0; scientific interpretation is separately
    reviewed.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B scripts/validate_claude_skills.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - native-skills
- check_id: native-validate
  name: Actual native validate
  status: passed
  required: true
  summary: Actual recorded process exited 0; scientific interpretation is separately
    reviewed.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B -c 'from
    pathwaymech.cli import run_qc_main; raise SystemExit(run_qc_main())'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - native-validate
- check_id: native-tests
  name: Actual native tests
  status: passed
  required: true
  summary: Actual recorded process exited 0; scientific interpretation is separately
    reviewed.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B -m pytest
    -q -p no:cacheprovider --basetemp /private/tmp/pathwaymech-next-240-local-gate-tests-20261012
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - native-tests
- check_id: native-lint
  name: Actual native lint
  status: passed
  required: true
  summary: Actual recorded process exited 0; scientific interpretation is separately
    reviewed.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B -m ruff
    check --no-cache .
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - native-lint
- check_id: native-kgx
  name: Actual native kgx
  status: passed
  required: true
  summary: Actual recorded process exited 0; scientific interpretation is separately
    reviewed.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B -c 'from
    pathwaymech.cli import export_kgx_main; raise SystemExit(export_kgx_main())'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - native-kgx
- check_id: native-vendored
  name: Actual native vendored
  status: passed
  required: true
  summary: Actual recorded process exited 0; scientific interpretation is separately
    reviewed.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: bash scripts/check_vendored_sync.sh
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - native-vendored
- check_id: native-diff-check
  name: Actual native diff-check
  status: passed
  required: true
  summary: Actual recorded process exited 0; scientific interpretation is separately
    reviewed.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - native-diff-check
- check_id: native-site-current
  name: Actual native site-current
  status: passed
  required: true
  summary: Actual recorded process exited 0; scientific interpretation is separately
    reviewed.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B -c 'from
    pathwaymech.cli import render_pages_main; raise SystemExit(render_pages_main(["--check"]))'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - native-site-current
- check_id: independent-target
  name: Independent maintained target QA
  status: passed
  required: true
  summary: Whole maintained check passed after all native gates.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-240-independent-maintained-tech-20261012/check_target.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - independent-target
- check_id: independent-checkout
  name: Independent maintained checkout QA
  status: passed
  required: true
  summary: Whole maintained check passed after all native gates.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-240-independent-maintained-tech-20261012/check_checkout.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - independent-checkout
evidence:
- evidence_id: native-history-1
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/history-1.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by the integration agent; this reviewer did not repeat it.
  snapshot_sha256: d89fab8fc11cd861d03e1d976f1a56e1adf597e6aac3ba856cbab2c523b125c0
- evidence_id: native-history-2
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/history-2.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by the integration agent; this reviewer did not repeat it.
  snapshot_sha256: f099a9f0c7abfdb408c6aa18d62fa9a6dabd3359e631ddf196f583713a9f7756
- evidence_id: native-sssom
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/sssom.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by the integration agent; this reviewer did not repeat it.
  snapshot_sha256: f960632565146eb4f37b6d28b558f1ff877c61d790bb6b5021399fbdc73307fd
- evidence_id: native-render
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/render.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by the integration agent; this reviewer did not repeat it.
  snapshot_sha256: 55f02fa84b35cb747620aff98e1b074b083e975da676ab1198555e4c53bf6f5c
- evidence_id: native-skills
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/history-and-generation/skills.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by the integration agent; this reviewer did not repeat it.
  snapshot_sha256: bd29e269e6ac5e2ee7a58b72f435ad245e0c8ecc235009097745a8fe71001500
- evidence_id: native-validate
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/validate.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by the integration agent; this reviewer did not repeat it.
  snapshot_sha256: 1700dc731723f94513c7a20429e7f7b6f328a860d57b7bc0c2e7b7ccfa730fc9
- evidence_id: native-tests
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/tests.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by the integration agent; this reviewer did not repeat it.
  snapshot_sha256: 96ed16641526398d18ebbd2cfcacc644adfb2b9aea38d8ebced5d9791051d41b
- evidence_id: native-lint
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/lint.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by the integration agent; this reviewer did not repeat it.
  snapshot_sha256: f53a17171b605412e6926cd6d760c5d8917bd38d625fe83e495cb422557766f9
- evidence_id: native-kgx
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/remaining-offline-gates/kgx.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by the integration agent; this reviewer did not repeat it.
  snapshot_sha256: 1a0b8783b92bfbb80d92b5bb0fa946edf37f131e0d39b67e87843bce5739287e
- evidence_id: native-vendored
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/vendored-gate/vendored.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by the integration agent; this reviewer did not repeat it.
  snapshot_sha256: ddc5645c3a5caf68648b6c061595488cd578f9d50c96e3a265850be1af4d5580
- evidence_id: native-diff-check
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/diff-check.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by the integration agent; this reviewer did not repeat it.
  snapshot_sha256: 6020c09c830834e303806ad929121b9ca2a4f892c1198331dd3e5db9111932d6
- evidence_id: native-site-current
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-qa/actual-native/final-gates/site-current.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by the integration agent; this reviewer did not repeat it.
  snapshot_sha256: 03aca7888d8518a34bc3dbbee1bf53682672b68498e2ec4163669a9286352a09
- evidence_id: independent-target
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/target.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: This independent reviewer executed complete current target/render/export
    or physical checkout/cache checks after native gates completed.
  snapshot_sha256: aa3ad62601d5f02c1fcfc1d9cba8234ae43fa4e2835e843f1813f5ead01b6312
- evidence_id: independent-checkout
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/checkout.execution.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: This independent reviewer executed complete current target/render/export
    or physical checkout/cache checks after native gates completed.
  snapshot_sha256: 41cd780064d4e710d03a62946c6cb18d2054a037a1f2c7663bd7f240eb7f77ca
- evidence_id: native-packet
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/native-execution-intake.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Fresh ignored-inclusive no-follow closure of the exact sealed81-artifact
    native gate packet plus two seals; every complete receipt and stream remains byte
    bound.
  snapshot_sha256: c2a31555258f35c470c697d34050c350f16b3c8d389b6b142173df3f0dce40fb
- evidence_id: canonical
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/canonical-acceptance.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Root accepted whole native source/ontology outputs and independent old-object/order/KGX
    preservation review.
  snapshot_sha256: 951053a78a7123c8ac43019db578873877bd89d5b1c177dbb9543675fb3c4938
- evidence_id: prior-actual-audit
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/prior-actual-review-handoff.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: This reviewer previously audited all 1921 actual artifacts plus two seals,
    whole scientific corpus, complete source objects/order, all selectors and complete
    KGX. That unchanged audit is inherited explicitly.
  snapshot_sha256: 243571dc5b62d1171af8c326f2dff30d7234fd2dda92f17b1502c47c1d630538
- evidence_id: integration
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/integration-acceptance.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Root accepted exact 18 destinations, nine primary owners, complete guards/native
    stages and hidden/ignored baseline/cache. The preparer 2761-body portable replay
    is inherited.
  snapshot_sha256: 3871988b2223c3f7d660f10e709ed8b5145b057913534b0de27b61f8b36f086f
- evidence_id: implementation
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/implementation-acceptance.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: The incomplete child PathWhiz/interface reference context finding is resolved;
    this reviewer previously ran 191 focused tests and 34 independent controls. That
    exact reviewed implementation contract is inherited.
  snapshot_sha256: 3cd2e4509b6edc4f738e02a554a7c0b4327da1790d899c36ea38af244415dd4e
- evidence_id: ordering
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/order-acceptance.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Root independently reproduced the old context-owner order defect and fixed
    deterministic serialization across five hash seeds. The only production correction
    is explicit metadata field order; prior identities, values and validation remain
    unchanged.
  snapshot_sha256: 319ce1daa083b9c77abbd5189a59d40704b268165e0d0f849fc27cba337398bf
- evidence_id: target-results
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/target-qa.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Complete maintained scoped YAML, 58 arrows, 44 display nodes, four qualifiers,
    43 identities, 42 references and rendered evidence checked. Authorities and whole
    exports equal accepted native bodies; SSSOM retains 62 old plus four new rows.
  snapshot_sha256: 8182168448450c0c06ecb43373c1797450779ca9e2bd13da5ea6eb745c9cce38
- evidence_id: checkout-results
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/checkout-preservation.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Ignored-inclusive complete physical owners/cache checked. All 240 old records/pages,
    124 review pairs and 408 histories remain exact; only declared owners/generated
    files and two histories change.
  snapshot_sha256: 418bcc73cc0697c4bbf19000646aef22c05c52b6126f260308c2838d7cb2cecd
- evidence_id: visual
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/visual-assessment.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Whole maintained SVG/CSS/JS equal the root-viewed scoped preview; root
    static visual appraisal is inherited explicitly, with dense junctions, truncated
    labels and blank canvas limitations.
  snapshot_sha256: 03b396168ab33bb882fe94dfb4326c737c1a90b6225b5861e4f89e4e1e860ed9
- evidence_id: preview
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-240/native-integration/independent-tech-review/preview-acceptance.json
  accessed_at: '2026-10-13T00:05:01Z'
  support: supports
  summary: Root personally viewed the complete corrected-target static light graph;
    no browser interaction, responsive, dark or print acceptance.
  snapshot_sha256: 1ea16397ca767965f4fab59b6742dd74106a83e647483687da282b1104023df7
assessments:
- assessment_id: owner-1
  area: ownership
  topic: conf/identifier_sources.json
  outcome: supported
  summary: Whole maintained owner equals the accepted deterministic runtime/configuration/native-output
    payload. The complete context contract and producer/consumer changes were independently
    reviewed upstream; current maintained integration and the actual full regression
    are verified here. Generated snapshot changes must be rebuilt from maintained
    configuration and adapters.
  target_ids:
  - owner-1
  evidence_ids:
  - canonical
  - implementation
  - ordering
  - independent-target
  - integration
- assessment_id: owner-2
  area: ownership
  topic: data/identifier_authorities/sources.json
  outcome: supported
  summary: Whole maintained owner equals the accepted deterministic runtime/configuration/native-output
    payload. The complete context contract and producer/consumer changes were independently
    reviewed upstream; current maintained integration and the actual full regression
    are verified here. Generated snapshot changes must be rebuilt from maintained
    configuration and adapters.
  target_ids:
  - owner-2
  evidence_ids:
  - canonical
  - implementation
  - ordering
  - independent-target
  - integration
- assessment_id: owner-3
  area: ownership
  topic: scripts/build_source_identifier_snapshot.py
  outcome: supported
  summary: Whole maintained owner equals the accepted deterministic runtime/configuration/native-output
    payload. The complete context contract and producer/consumer changes were independently
    reviewed upstream; current maintained integration and the actual full regression
    are verified here. Generated snapshot changes must be rebuilt from maintained
    configuration and adapters.
  target_ids:
  - owner-3
  evidence_ids:
  - canonical
  - implementation
  - ordering
  - independent-target
  - integration
- assessment_id: owner-4
  area: ownership
  topic: src/pathwaymech/identifiers.py
  outcome: supported
  summary: Whole maintained owner equals the accepted deterministic runtime/configuration/native-output
    payload. The complete context contract and producer/consumer changes were independently
    reviewed upstream; current maintained integration and the actual full regression
    are verified here. Generated snapshot changes must be rebuilt from maintained
    configuration and adapters.
  target_ids:
  - owner-4
  evidence_ids:
  - canonical
  - implementation
  - ordering
  - independent-target
  - integration
- assessment_id: owner-5
  area: ownership
  topic: src/pathwaymech/pathbank_context.py
  outcome: supported
  summary: Whole maintained owner equals the accepted deterministic runtime/configuration/native-output
    payload. The complete context contract and producer/consumer changes were independently
    reviewed upstream; current maintained integration and the actual full regression
    are verified here. Generated snapshot changes must be rebuilt from maintained
    configuration and adapters.
  target_ids:
  - owner-5
  evidence_ids:
  - canonical
  - implementation
  - ordering
  - independent-target
  - integration
- assessment_id: owner-6
  area: ownership
  topic: tests/fixtures/pathbank_context/SMP0002097.owl
  outcome: supported
  summary: Whole maintained owner equals the accepted deterministic runtime/configuration/native-output
    payload. The complete context contract and producer/consumer changes were independently
    reviewed upstream; current maintained integration and the actual full regression
    are verified here. Generated snapshot changes must be rebuilt from maintained
    configuration and adapters.
  target_ids:
  - owner-6
  evidence_ids:
  - canonical
  - implementation
  - ordering
  - independent-target
  - integration
- assessment_id: owner-7
  area: ownership
  topic: tests/fixtures/pathbank_context/SMP0002097.receipt.json
  outcome: supported
  summary: Whole maintained owner equals the accepted deterministic runtime/configuration/native-output
    payload. The complete context contract and producer/consumer changes were independently
    reviewed upstream; current maintained integration and the actual full regression
    are verified here. Generated snapshot changes must be rebuilt from maintained
    configuration and adapters.
  target_ids:
  - owner-7
  evidence_ids:
  - canonical
  - implementation
  - ordering
  - independent-target
  - integration
- assessment_id: owner-8
  area: ownership
  topic: tests/test_pathbank_context_authority.py
  outcome: supported
  summary: Whole maintained owner equals the accepted deterministic runtime/configuration/native-output
    payload. The complete context contract and producer/consumer changes were independently
    reviewed upstream; current maintained integration and the actual full regression
    are verified here. Generated snapshot changes must be rebuilt from maintained
    configuration and adapters.
  target_ids:
  - owner-8
  evidence_ids:
  - canonical
  - implementation
  - ordering
  - independent-target
  - integration
- assessment_id: prior-preservation
  area: provenance
  topic: Whole authority and checkout preservation
  outcome: supported
  summary: All prior authority objects, nested order and first owners survive. The
    892-entry manifest preserves all 887 old rows; ontology and Rhea are unchanged.
    All 240 old records/pages, 124 review pairs and 408 histories remain exact. Two
    actual histories precede SSSOM and first rendering.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  evidence_ids:
  - prior-actual-audit
  - checkout-results
  - native-history-1
  - native-history-2
- assessment_id: graph-exports
  area: graph
  topic: Whole graph and current page
  outcome: supported
  summary: All 58 edges, 44 display nodes, four qualifiers, 42 references and 43 identities
    resolve. Current KGX has 4357 nodes/12110 edges and preserves all 12052 old edges
    plus prior node payloads/order. Only six shared nodes gain exact target contexts;
    no aggregate field or category-union changes.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  evidence_ids:
  - canonical
  - prior-actual-audit
  - target-results
  - visual
- assessment_id: mapping-export
  area: representation
  topic: Complete source mappings
  outcome: supported
  summary: Native SSSOM preserves complete header and 62 old rows, every cell, multiplicity
    and relative order; it adds four exact target mappings for 66 total, following
    native subject sorting.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  evidence_ids:
  - native-sssom
  - target-results
- assessment_id: native-gates
  area: schema
  topic: Fresh maintained validation
  outcome: supported
  summary: 'All nine native gates passed for 241 records: 4773 tests passed, 3 skipped
    and 3 warnings retained. Render, skills, validation, lint, KGX, vendored, diff
    and site-current evidence is complete. Native execution was by the integration
    agent; this reviewer verified receipts and streams rather than rerunning passing
    broad gates.'
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  evidence_ids:
  - native-packet
  - native-validate
  - native-tests
  - native-lint
  - native-kgx
  - native-vendored
  - native-diff-check
  - native-site-current
- assessment_id: portable-evidence
  area: completeness
  topic: Whole evidence provenance
  outcome: supported
  summary: Accepted preparation retains 2761 whole bodies, 1844 reused and 917 new,
    across 14 current packets; 891 authority originals and all 92 acquisition attempts/66
    received scientific bodies are retained. All 42 reference hashes resolve. The
    preparer complete portable replay is inherited; the maintained index and payload
    bytes are freshly bound. Both resolved local technical findings and original failures
    remain available.
  target_ids:
  - owner-1
  - owner-2
  - owner-3
  - owner-4
  - owner-5
  - owner-6
  - owner-7
  - owner-8
  evidence_ids:
  - integration
  - implementation
  - ordering
  - independent-target
  - checkout-results
findings: []
actions: []
limitations:
- Prior complete implementation adversarial tests, actual canonical audit and accepted
  preparation portable replay are inherited explicitly; current maintained page, exports,
  owners, full physical inventory/cache and native gate receipt/streams are freshly
  checked.
- The root personally viewed static light scoped preview is inherited only after whole
  current SVG/CSS/JS equality. This reviewer claims no new visual or browser interaction
  test. Dense junctions, label truncation and blank canvas remain; responsive, keyboard,
  dark and print behavior are untested.
- Actual regression retains 3 skips and 3 warnings with 4773 passes.
- Evidence references name planned concrete dossier destinations. Native save requires
  exact-byte evidence adoption and a current-input recheck; this external proposal
  is not a saved native review.
notes:
- Native inspection followed completed gates and independent maintained QA; every
  captured current input hash was rechecked before this proposal.
- The technical review uses the native repository review schema/serialization contract;
  it does not claim the separate full scientific skill workflow.
- Original local findings pathbank240-incomplete-interface-context and pathbank240-context-owner-order
  remain distinct from their accepted successor dispositions; no GitHub issue is claimed.
- No SQL full hashes, broad test suites or native builders were repeated by this reviewer;
  no maintained product edit, native save, public action or licensing clearance occurred.
links: []
tags:
- spermidine
- pathbank-context
- technical-review
- local-only
```

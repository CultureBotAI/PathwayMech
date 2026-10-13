# Technical review of BaeSR source-authority integration

- Review: 20261013T004524Z-baesr243-technical
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-13T00:45:01Z
- Finished UTC: 2026-10-13T00:45:24Z
- Reviewer: Codex /root/deoxy237_science_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Two source-authority owners pass current maintained review. Runtime and ontology are unchanged; complete prior payloads, accepted graph ordering, mappings and cache are preserved. Actual native gates pass with inherited scientific and static-preview limitations.

## Scope And Provenance

Two source manifest/snapshot owners after completed record 243 gates, with complete maintained context.

Selection: Both nonrecord primary owners from clean committed 240 baseline 63bc0ba99c63e4d4cdbdf70b8fb3f6f8417eeacf; no sampling.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 63bc0ba99c63e4d4cdbdf70b8fb3f6f8417eeacf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| owner-1 | conf/identifier_sources.json | maintained | conf/identifier_sources.json |
| owner-2 | data/identifier_authorities/sources.json | maintained | data/identifier_authorities/sources.json |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Actual native history-1 | passed | False | owner-1, owner-2 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native history-2 | passed | False | owner-1, owner-2 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native sssom | passed | True | owner-1, owner-2 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native render | passed | True | owner-1, owner-2 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native skills | passed | True | owner-1, owner-2 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native validate | passed | True | owner-1, owner-2 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native tests | passed | True | owner-1, owner-2 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native lint | passed | True | owner-1, owner-2 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native kgx | passed | True | owner-1, owner-2 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native vendored | passed | True | owner-1, owner-2 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native diff-check | passed | True | owner-1, owner-2 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Actual native site-current | passed | True | owner-1, owner-2 | Actual recorded process exited 0; scientific interpretation is separately reviewed. |
| Independent maintained target QA | passed | True | owner-1, owner-2 | Whole maintained check passed after all native gates. |
| Independent maintained checkout QA | passed | True | owner-1, owner-2 | Whole maintained check passed after all native gates. |

## Scientific And Domain Assessments

### conf/identifier_sources.json

ownership: supported. Targets: owner-1.

The whole maintained source manifest or source-authority snapshot equals the exact accepted actual output. One ordinary PathBank source entry adds six selected terms; product runtime and ontology remain unchanged. Identity/name projection does not assert typed biochemical context.

### data/identifier_authorities/sources.json

ownership: supported. Targets: owner-2.

The whole maintained source manifest or source-authority snapshot equals the exact accepted actual output. One ordinary PathBank source entry adds six selected terms; product runtime and ontology remain unchanged. Identity/name projection does not assert typed biochemical context.

### Whole authority and checkout preservation

provenance: supported. Targets: owner-1, owner-2.

The 893-row manifest retains all 892 prior rows. All 2688 old source terms/711 owners and their nested encounter order survive in 2694 terms/712 owners. Ontology remains 2016 terms/five owners with exact old bytes. All 241 old scientific records/pages, 126 review pairs and 410 histories remain exact; two new histories precede SSSOM/render.

### Whole graph, exact contexts and encounter order

graph: supported. Targets: owner-1, owner-2.

All 15 arrows, 18 display nodes, eight qualifiers, 18 references and 12 identities resolve. Whole current KGX equals accepted 4363 nodes/12125 edges. Every prior edge payload and relative order and every prior node aggregate/context survives. Six exact target contexts are inserted at the accepted positions, preserving every prior context in exact relative order and whole payload. The complete old-node vector equals the accepted ATP/ADP encounter permutation; removing those two IDs preserves all other relative order. Phosphate remains unconnected.

### Complete source mappings

representation: supported. Targets: owner-1, owner-2.

Native SSSOM preserves its complete header and all 66 old rows, cells, multiplicity and relative order, adding four exact mappings for 70 total.

### Fresh maintained validation

schema: supported. Targets: owner-1, owner-2.

All nine native gates passed for 242 records: 4773 tests passed, 3 skipped and 3 warnings retained. Root executed those commands; this reviewer verified exact receipts and streams without repeating passing broad gates.

### Whole source and review provenance

completeness: supported. Targets: owner-1, owner-2.

Accepted preparation retains 2421 whole portable bodies. Its complete replay is inherited; maintained dossier/index bodies and all 18 reference-hash bindings are fresh. Ordinary source identity/name support remains separate from scientific assembly, donor-state, site, phosphate and strain interpretation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native-history-1 | research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/history-1.execution.json | supports | Actual native command and complete original streams verified. Executed by root; this reviewer did not repeat it. |
| native-history-2 | research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/history-2.execution.json | supports | Actual native command and complete original streams verified. Executed by root; this reviewer did not repeat it. |
| native-sssom | research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/sssom.execution.json | supports | Actual native command and complete original streams verified. Executed by root; this reviewer did not repeat it. |
| native-render | research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/render.execution.json | supports | Actual native command and complete original streams verified. Executed by root; this reviewer did not repeat it. |
| native-skills | research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/skills.execution.json | supports | Actual native command and complete original streams verified. Executed by root; this reviewer did not repeat it. |
| native-validate | research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/validate.execution.json | supports | Actual native command and complete original streams verified. Executed by root; this reviewer did not repeat it. |
| native-tests | research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/tests.execution.json | supports | Actual native command and complete original streams verified. Executed by root; this reviewer did not repeat it. |
| native-lint | research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/lint.execution.json | supports | Actual native command and complete original streams verified. Executed by root; this reviewer did not repeat it. |
| native-kgx | research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/kgx.execution.json | supports | Actual native command and complete original streams verified. Executed by root; this reviewer did not repeat it. |
| native-vendored | research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/vendored-gate/vendored.execution.json | supports | Actual native command and complete original streams verified. Executed by root; this reviewer did not repeat it. |
| native-diff-check | research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/diff-check.execution.json | supports | Actual native command and complete original streams verified. Executed by root; this reviewer did not repeat it. |
| native-site-current | research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/site-current.execution.json | supports | Actual native command and complete original streams verified. Executed by root; this reviewer did not repeat it. |
| independent-target | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/target.execution.json | supports | This reviewer executed complete current target/render/export or physical checkout/cache checks after native gates completed. |
| independent-checkout | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/checkout.execution.json | supports | This reviewer executed complete current target/render/export or physical checkout/cache checks after native gates completed. |
| target-helper-correction | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/target-helper-correction.json | supports | Initial external target QA failed on an append-only context assumption. Exact helper, receipt, streams and partial checks are retained; the bounded corrected check requires whole canonical KGX equality, every old context as an exact ordered subsequence and precisely the accepted target contexts/multiplicity. Checkout and all native gates passed first attempt and were not repeated. |
| native-packet | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/native-execution-intake.json | supports | Fresh no-follow complete closure of 81 native artifacts plus two seals, including hidden/ignored paths and every complete phase stream. |
| canonical | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/canonical-acceptance.json | supports | Root accepted one native source builder and byte-exact inherited ontology; all prior objects/order, first owners and six exact added graph contexts survive. |
| prior-actual-audit | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/prior-actual-review-handoff.json | supports | Distinct Adapter independent audit checked all 1922 actual artifacts plus two seals, all 242 scientific records, complete source objects/order and KGX. That accepted audit is inherited; I audited earlier canonical preparation, not this actual execution. |
| integration | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-acceptance.json | supports | Root accepted the exact three primary owners and 12 complete planned destinations with guarded native stages. The preparer whole 2421-body portable replay is inherited. |
| integration-compatibility | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/handoff.json | supports | Complete distinct 14-file compatibility review is retained with both seals, original Rhea-role assertion failure, exact failed/successor helpers and full streams. Its accepted mechanics appraisal is inherited, not repeated. |
| sealer-template | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/native-sealer-template-review.json | supports | This reviewer read the whole bounded native sealer template and exact predecessor diff; receipt-origin/stream/closure controls remain unchanged. Static template review is distinct from root actual native execution and final runner binding. |
| post-package-retention | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/post-package-evidence-retention.json | supports | Whole post-package compatibility and template-review bodies are retained with exact original paths, sizes, hashes and modes. These reviews postdate the scientific portable package and are retained separately here. |
| target-results | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/target-qa.json | supports | Whole accepted YAML, 15 arrows, 18 display nodes, eight qualifiers, 12 identities, 18 references and all 31 evidence occurrences match. Current graph equals accepted outputs and the root-viewed static preview; mappings retain 66 old plus four new rows. |
| checkout-results | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/checkout-preservation.json | supports | Complete physical inventory includes hidden/ignored paths. All 241 old records/pages, 126 review pairs, 410 histories and 800 cache entries remain exact outside the accepted scope. |
| visual | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/visual-assessment.json | supports | Original preview assessment by Nitrate; root independently viewed this same whole raster as documented in the root scientific review. Current whole SVG/CSS/JS equality binds it. No personal new visual or browser assessment is claimed here. |
| science-scope | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/scientific-scope-acceptance.json | supports | Exact accepted corrected scientific target and complete source-state/sequence/taxon/chemical/GO limitations are inherited. Separate maintained SCI judgment belongs to Adapter. |
| root-preview-reading | research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/root-scientific-review-handoff.json | supports | Root scientific review explicitly documents personal full static-raster reading, including disconnected phosphate and overlap/truncation/blank-space limitations. |

## Limits And Additional Notes

- One external target-QA attempt failed because its helper required new contexts to append. The exact failed helper/streams/partial report are retained. A narrow helper correction passed; no product, accepted native output or native gate was changed. Complete checkout passed once and was not repeated.
- Prior distinct actual-output audit, accepted scientific reading and integration portable replay are inherited. Fresh scope is maintained record/page/export/owner preservation, full physical inventory/cache and native receipt/stream currentness. No paper reread or broad test rerun.
- Only one source builder ran for the accepted canonical output. Ontology was reused byte exactly. Historical SQL descriptors retain obsolete rehash prose; no new SQL hash/query or ontology builder is claimed.
- The root personally viewed static light preview is inherited after exact whole current SVG/CSS/JS equality. Dense convergence, long return paths, overlapping/truncated labels and tall blank canvas remain. No personal new visual, interactive, responsive, keyboard, dark or print check.
- Actual regression retains 3 skips and 3 warnings with 4773 passes.
- Evidence references name concrete proposed dossier destinations. Exact-byte adoption and current input inspection/validation are required before native save; this external proposal itself is not saved.
- Every native input hash was rechecked after actual gates and fresh maintained QA, before this proposal.
- The technical review uses the native repository review contract and does not claim the separate full scientific skill workflow.
- No maintained product edit, review save, public action or licensing clearance was performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T004524Z-baesr243-technical
kind: repository
repository: CultureBotAI/PathwayMech
title: Technical review of BaeSR source-authority integration
started_at: '2026-10-13T00:45:01Z'
finished_at: '2026-10-13T00:45:24Z'
reviewer:
  identity: Codex /root/deoxy237_science_review
  kind: agent
  independence: independent
  independence_basis: Authored the accepted 240 baseline and independently audited
    243 canonical preparation. Did not author the 243 scientific record, authority
    design, canonical execution, maintained integration or native gates. Distinct
    Adapter actual-output audit and root scientific reading are inherited. Separate
    maintained SCI belongs to Adapter. This review judges the 243 source-only delta
    and whole maintained preservation, not a new independent review of the authored
    240 baseline.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Two source-authority owners pass current maintained review. Runtime and ontology
  are unchanged; complete prior payloads, accepted graph ordering, mappings and cache
  are preserved. Actual native gates pass with inherited scientific and static-preview
  limitations.
source:
  git_revision: 63bc0ba99c63e4d4cdbdf70b8fb3f6f8417eeacf
  state: working_tree
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: conf/identifier_policy.yaml
    sha256: f2991a22f16f0d14d83226c6ac261bc779b253b2547fae9724474d8596b411c7
    role: context
  - path: conf/identifier_sources.json
    sha256: 066b504bc00b8fd3b2bb15d9833524277dccf2ce4961c70e00d68dfbd324aed3
    role: target
  - path: conf/rhea_identifier_updates.json
    sha256: 5c6a356a56a4b4df882ac2898587576216895a07fc2b455082da136ebd91a49d
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: f155aeff12118e7aa7176c58f32ea231ad61fa25cd43a1c90aa6ff6f383ef9e2
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: aa22a12f65bfe5a0d24123fbac324cd19c0258230c7fc51f1bbea841984d4fa1
    role: target
  - path: data/pathways/baesr-two-component-signal-transduction.yaml
    sha256: 1cf9262a0df376a19517b3f55ccaac67dacc8af8ce58bd8a1b2046e93a951824
    role: context
  - path: docs/record-review-profile.md
    sha256: f3f00eebb7841e9d5ac891271e269f45e926995e16856b8e9a885436570c7819
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: output/kgx/edges.tsv
    sha256: a90aef8cc289bff2e4db8f3a59d56270c2ce140c98e733ea5d5a4ea893ab1f7f
    role: context
  - path: output/kgx/nodes.tsv
    sha256: e96a38b15a7f99eb5c72bb3767e857e2be70ceb0846a54244dac43aa6b9809c6
    role: context
  - path: output/sssom/source_mappings.sssom.tsv
    sha256: 1b9bb94dc0bcf221c93709ae37a77df90e69cce6472a78a51e0cd0a99154afc7
    role: context
  - path: pages/records/PathBank_SMP0002123.html
    sha256: 2446e297bd0a16414cfc277e2af26e83db140105e8152a1444ba1d9fcde4f440
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/README.md
    sha256: 6907c68c9b19a722a50643e6165649285bada478eb8a0089cef4e94ed74c10ec
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/archives/evidence-bodies.zip.part-001
    sha256: 26a883af6b5bbaaaec92f67e9bb4ce02c3ac233ea8b8dd6d4a724ea9492288eb
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/archives/integration-preparation.zip
    sha256: 67dc2cab6c5e6354a7f63c88901f0aba5c777303ee803a5854cea011ae5002f5
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/common.py.gz
    sha256: f96739937ce6752a391bf6e786683fd31329eeb64d0bfb1a6c8664ef7dca0da1
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/evidence-index.json.gz
    sha256: b8dcb5a661b55a2a01083b9af138fd8a55c3dda8bb24ad16e95bb29f9d78dc65
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/external-packet-closures.json.gz
    sha256: 7e70d161fc9e5a61d768414c858e49a35af28fc59a359096d196928a2d340e59
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/integration-preparation.json
    sha256: afe74da5ea9d16c72f638d6b4c03f5e0692adc04809fca33626bb4eeafd93912
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/local-integration-decision.json
    sha256: d2cb33390d4a7810d6761b067471b0463b993d038c252a2b87ad057347cc3884
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/README.md
    sha256: 1cb451aa77840c873be38e0b8718809812471d0a9917d604d33e6ec62ff041cc
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/finalization-plan.zip
    sha256: 165437b827ee24f18f9d72ef8309005a1e0cce91817325bfad52f18dec242d28
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/REPORT.md
    sha256: 292bfa643cbac0fc0b1fae2d2819cfb9144341dc8a1bf7792cb1bf6398d65c80
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/accepted-basis.json
    sha256: 1f3663794b7699a5b86f7adab02cfb62c62455034d74653b38437ac9bfc3254a
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/accepted-reading.json
    sha256: 3e00fb3977fe70899a2a90ac5645a29e116c9bf793ed9443b06dcd4bbadc239c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native-copy.json
    sha256: ed5ed6b8df32d45c818271eb153ce1e60bd61900d0a728bc22b32a800558e6be
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/REPORT.md
    sha256: a6e40c2e5308d40243e876a1906ed59415b0b55cf1585649c5f63294aa32c2c6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/actual-tool-provenance.json
    sha256: f7378dcdbfa13eea6f98e4791f691acfd90aa15fc0bcda34946e4323030f22cc
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/artifact-manifest.json
    sha256: 3cc233aab11897a162d3a6853195aeb2f20db4a785ca6299d99de4dcfe72e5fb
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/execution-summary.json
    sha256: a4ede28a31c6e4707d970369082aab84ef886efc91cfe45312635a63b5add004
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/completion.json
    sha256: 34c10f6380090baa4247e91e2c66c932efd0c266c97f31d9115eecb800f33f8c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/diff-check.execution.json
    sha256: 677a89dbe4d15cdbc6209e68acfcd7f262177a08893962e33bb7765e43c6134b
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/diff-check.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/diff-check.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/phase-start.json
    sha256: ee79f55c788013df6b0b10f91f6bafc4e8a8d63931094d4187246b2e1c388bd2
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/runner-at-start.py.gz
    sha256: fc457bc387a89b7a9a5866efa84d7bfbd2e9d21bdde3f639616e4b2074c28952
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/site-current.execution.json
    sha256: 696729c51f9e2bc05babb0f6e72fe45ef6e6188bde687a990106c1706f8449eb
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/site-current.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/site-current.stdout
    sha256: ae19c9046079a587831c4d408725c91e0d84179d9cf3b9dffe74de818c990b99
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/handoff.json
    sha256: 10d944650f09b46a665ff5e07469e709cfbc1e855211096a045fb23ad7db0626
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/completion.json
    sha256: 447ff6c8b811c3939100d776ccfff56629370bc89180f5f7ed26e000d1698264
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/histories-before-generation.json
    sha256: de8545cfd98ae25668e1e76d758067598baf5be82cd1617fb61744b886e64b86
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/history-1.execution.json
    sha256: 61f0a3d5cc7fa0851b6165fe84ab713887006e601e6b924f6ea81e4e888b7e98
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/history-1.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/history-1.stdout
    sha256: 3fa74d8d417318803d7cc8476fb8c073c3b6e370dfd73d2bdd8f1712c7f6eef6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/history-2.execution.json
    sha256: 83cac1e13ad4099806a540562eea680ce98325320b866b2aa3cde22e613e863d
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/history-2.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/history-2.stdout
    sha256: fc5d56db46c4cb4f63ebe2db5ad2b6b5f436efed1990031dd4ae1c7b83195430
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/phase-start.json
    sha256: 659cb9954b9dc022e3d0ca371084ae1e76159fc8635d88eeb8f92ebcfc9234c4
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/render.execution.json
    sha256: b3af417cc226ebb7556fbf08577d2e74f2148117b13824fa1dfe73573834003e
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/render.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/render.stdout
    sha256: 0a32e30a0b8c8047f44a17835f89cbd9c94fd7d19231bfbec3f743bf6e7f483c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/runner-at-start.py.gz
    sha256: fc457bc387a89b7a9a5866efa84d7bfbd2e9d21bdde3f639616e4b2074c28952
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/skills.execution.json
    sha256: 3361284edb5808b1719d09e3261f2b22bb05da1be77de61b63517535b9ad0ae9
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/skills.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/skills.stdout
    sha256: aa2d3652343b880d16a176d45deb7b4907fb11f43e31f1840d7724658478a527
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/sssom-preservation.json
    sha256: 16f19331eba1e22aa8381f3b6d7a9ad7a922eb72537c2cc00a46e68135621673
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/sssom.execution.json
    sha256: 0c650ee9fb7d3dc5d7ec97058434d6510b037cfab727460d05d7606dac0779b2
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/sssom.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/sssom.stdout
    sha256: bb8ef8ce127c8585bd9d5f1c806d1358847327cf4d078be777977b296e87159a
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/input-receipts/adoption.json
    sha256: 956b53a162220f796225b515b45c0c145c54ab6e7ed1bdc3cfcaad8ef1371e35
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/input-receipts/root-acceptance.json
    sha256: c25d3612b3e9060c3d7f89fca186a3ebb1f3d277d3e35779d71b980ffbd57c33
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/input-receipts/runner-binding.json
    sha256: 978be9996762c27c533bb638b0d23d7beeab3885112d46e54f654f43906260ee
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/input-receipts/sealer-lineage.json
    sha256: d806ee4a303f58104c88bf14eab5393d336689ee4f1e2b5fd5136a2661d98de7
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/input-receipts/sealer-predecessor.patch
    sha256: da470394150463b4ac9dadaad15814cac4dd16f178bc734e822c6fc42275744d
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/input-receipts/stages.json
    sha256: 56fc10ece82d03a96332a589af5e93c631ed309e22ca1b4c923219dd2434a1d3
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/adoption/execution.json
    sha256: 84903d78a9168d68fb2a8f509ae8de05046dab659baa5fd2c40d18e7ed6f2f2b
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/adoption/helper-at-start.py.gz
    sha256: 14000c38d3717c78547a952f5840d1bd6ca5083eaaa60250414d6479d85a79d0
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/adoption/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/adoption/stdout
    sha256: 4c471337a9cab01102d6104be401af59991af4b71637f341fc0c84c9706005d4
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/capture-wrapper.py.gz
    sha256: 85fcc7f39dad2da07c59a8ddb61eb5ee33c829fdfda62d0a1e0959ba1f23262a
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/final-gates/execution.json
    sha256: 41cb173517884735f0f84bbabdc143301ad53e94d61a6d80fd24b4d7870b0fea
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/final-gates/helper-at-start.py.gz
    sha256: fc457bc387a89b7a9a5866efa84d7bfbd2e9d21bdde3f639616e4b2074c28952
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/final-gates/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/final-gates/stdout
    sha256: f9cda6ea1c6299b18277711cae9e99e00159355e052453daafa3d29814822a9a
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/history-and-generation/execution.json
    sha256: ab0947c52173aa26508ebb1f5de6a3d8b0928e765805f000894def087db03223
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/history-and-generation/helper-at-start.py.gz
    sha256: fc457bc387a89b7a9a5866efa84d7bfbd2e9d21bdde3f639616e4b2074c28952
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/history-and-generation/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/history-and-generation/stdout
    sha256: eaac22c230bbfe6171e7e65d05de0b145ce2eafd1339790b5ff7c3fc2c8ff1bd
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/remaining-offline-gates/execution.json
    sha256: 4189a5f2fd4ad9db1ba62b87141435608ccb5ca53f2e08df79cf849b6931222f
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/remaining-offline-gates/helper-at-start.py.gz
    sha256: fc457bc387a89b7a9a5866efa84d7bfbd2e9d21bdde3f639616e4b2074c28952
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/remaining-offline-gates/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/remaining-offline-gates/stdout
    sha256: 244d38a70966eb141a4d7963859fa44e1a234781d97ed3b874bf770359d484c1
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/vendored-gate/execution.json
    sha256: 267e7ca3e1420cd3b5e924a90d8b69f2752baf735f1e853220248abc74df404c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/vendored-gate/helper-at-start.py.gz
    sha256: fc457bc387a89b7a9a5866efa84d7bfbd2e9d21bdde3f639616e4b2074c28952
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/vendored-gate/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/outer-tool-streams/vendored-gate/stdout
    sha256: 57f2ebea6e2f260d76e0e97fa2786bfaee44eb64a9253047eb6b5064dbdf2254
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/completion.json
    sha256: 8b07bb12d4dcc10527741935513b6491991d5d4743be9b361447b1c94a2b4fb0
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/kgx.execution.json
    sha256: 5c0e76cd2dc22d91323e5de6a0d86483f42e531343d6acf840f279d43d80023c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/kgx.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/kgx.stdout
    sha256: f603ab73b0b0af103a5bfad9c3acacc76c80cf41da086ed3a0117e218eccc957
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/lint.execution.json
    sha256: 557a452124f6fda677efb6eff1d959aff9bf53fda4abb0e4fb06b636f42e36bd
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/lint.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/lint.stdout
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/phase-start.json
    sha256: 82d14a71465c385e6f40206647efb26191103cf8a15fabaefb685e457a435901
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/runner-at-start.py.gz
    sha256: fc457bc387a89b7a9a5866efa84d7bfbd2e9d21bdde3f639616e4b2074c28952
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/tests.execution.json
    sha256: 6ddf943cc4462f34f5ed1509d1c3750f62faac89ed877a1acf42e9cdf395892a
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/tests.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/tests.stdout
    sha256: 5109409789ba7094f83b7ac1252f2b3044970a92923899ef3ad1c28fcda4aa2d
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/validate.execution.json
    sha256: 9dc9b518ce37d31e23047ca737443f8281f228fb74bfc7ca493dbb8308be231b
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/validate.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/validate.stdout
    sha256: 26c9e21f96b391391ba250b50d311b70f680e3bb1788a63ee69f88180faf39fd
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/sealing-helper.py.gz
    sha256: 297c621192944f3e28a7e624a142c9f7bd8d30bc669df27e229d74256cc14ea5
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/vendored-gate/completion.json
    sha256: 6616a878dba7c1e71aee8a7a6d91de34d5ff1b0d3ad1180437112cc20fb87775
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/vendored-gate/phase-start.json
    sha256: 0ba3f36d68402a3b9d84205227c5009e9f9a051f5affef0cf074e8edecf1fbf2
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/vendored-gate/runner-at-start.py.gz
    sha256: fc457bc387a89b7a9a5866efa84d7bfbd2e9d21bdde3f639616e4b2074c28952
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/vendored-gate/vendored.execution.json
    sha256: fa82b46a641ca1fa0435353c9dc640ad161c1fbd75c127c7ad6a70eb864a05e7
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/vendored-gate/vendored.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/vendored-gate/vendored.stdout
    sha256: 3b073aa29da7dc3996edbe18c83d0d6593ba6d03238b663efc40286be4cf428e
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/artifact-manifest.json
    sha256: c267334d109806304729264efa770852fa13125249c974d57cfd408fa3b368e7
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/completed-helper-steps.json
    sha256: 43def039f0f1a810d79d6fad95762deae3617828f1fe7348f495ad615904daf5
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/completed-review-ready.yaml
    sha256: a40deda27a0ac23c8d6a444f590a989ac5676c4b7eceeb4db9ec5dc2cb69b4cc
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/completed-review.yaml
    sha256: a40deda27a0ac23c8d6a444f590a989ac5676c4b7eceeb4db9ec5dc2cb69b4cc
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/durable-adoption-instructions.json
    sha256: 11bd54f25575ca3971cc2abcb8c29ff55200c69f2e4751ccde52ee05be8dbdb5
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/edge-appraisals.json
    sha256: 6f4adac64709f94828f1e39bc69d43d6cabd6c84a0a7aaa2e9f7ed9621fe47ca
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/current-judgment-and-census/completion.json
    sha256: 3b00f5329d8acaf17e191567722f0964d4e6da3f8c5b468a01b34139e33b3bbd
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/current-judgment-and-census/helper.py.gz
    sha256: 0ccf6e8342c5783dc796bec972248e84c517f582c6bab150feaf0bcbd06772c2
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/current-judgment-and-census/start.json
    sha256: 8787e9cfd553f506c46da420c3943bbe995a06ed9df60f649218fc4b34cf1aa4
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/current-judgment-and-census/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/current-judgment-and-census/stdout
    sha256: c65f144edaffe761240adb36d6d8ba5633e4ad3547da68056d6988417b1e4177
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/final-native-inspect/completion.json
    sha256: a889676d46092aafc1aad8745679714fec94747a1495da48787aaa05969c08cb
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/final-native-inspect/helper.py.gz
    sha256: ece3fb2f8b83e6d3cdf8f0bb9261d2d8bc75a84a27bf12d7a466c55d1bf70bbf
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/final-native-inspect/start.json
    sha256: b996fee2fd8235296a16d946a44bb314d48d712db252c70edf55beec6e689418
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/final-native-inspect/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/final-native-inspect/stdout
    sha256: 7bc410395ec58392e53c195f733e7afff50b3fded6dffab25aeb80930d6a7ee2
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/maintained-science-currentness/completion.json
    sha256: 605d832a07dd27da28afe4f7b762828ebfcb3d7b9ea1a1e60ba7255be7d8f4f5
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/maintained-science-currentness/helper.py.gz
    sha256: 3cc4ecfb74fde59f6e8cffbcf5dd705abf24cb7e11bd52cdbd312662cb211170
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/maintained-science-currentness/start.json
    sha256: eda08f6587539ac38f8948839c49d485d242361c5e04d2682cf5a76e8d8919d9
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/maintained-science-currentness/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/maintained-science-currentness/stdout
    sha256: 6b3e5133c2c062f93123f62887cd297b80a91eaed1c700f04bd090b5c32eb212
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/native-validate/completion.json
    sha256: 5b6ce25c2c71c9ecce2a4cd1d5b74b26b7963afdd6b958de55fb3c72041af752
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/native-validate/helper.py.gz
    sha256: bb2d8d21a2e264797331c22023b351233353b813af960994ad612a2bf086e0a3
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/native-validate/start.json
    sha256: eba453ff7b84ef9c8ec3fb49735280d90534a3944d1d0ed891ce05312bcf7f62
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/native-validate/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/native-validate/stdout
    sha256: 8a7621cc6f2fe227c6a2e421a486d294c081e0ee284f03f6845811a10f5f8cff
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/serialize-scientific/completion.json
    sha256: 1218f45e3ce022312480c4ca0befaad36ed3acb62d17e07e3f3299ab7fb1ec2a
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/serialize-scientific/helper.py.gz
    sha256: 817da5f3fc699de914c87f7cd4202ed127af06c94ecb933d031bbcca62285c80
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/serialize-scientific/start.json
    sha256: a2854f42090df75e9a5f458ab752445e86ae1009001f2e0da80355c7189b479d
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/serialize-scientific/stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/executions/serialize-scientific/stdout
    sha256: 33d0946129f0b0fd5c6a99ee5f4f22c2879dbdacd4049f75ab32f3fbf6507e91
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/final-current-bindings.json
    sha256: e0404c4d6e520ebf9e76ded82a1482d637e96b106a9797c09df7201a4b3c74e8
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/final-native-binding.json
    sha256: d274855a8aa41ff3179518034e39a2aa6f0fcbcc93a1367e15ad237d1ab0d349
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/final-review-summary.json
    sha256: 88e2d003b1f418ed090cbf3fa97c76fd742d877dc2707b60d84a3216bf1a620a
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/final-shared-QA-binding.json
    sha256: d040b102cb42b844a84aa07ad02c3c5de9d70fd398d96b1fff209504a1cf360c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/finalize_science.pre-attribution.py.gz
    sha256: 43c74412158e386c2fe53ad93a291fba7f0a17201d6acc2aba56fa9354596b9b
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/finalize_science.py.gz
    sha256: 817da5f3fc699de914c87f7cd4202ed127af06c94ecb933d031bbcca62285c80
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/handoff.json
    sha256: e83edab67519d3f1a8a37ee831192d704e7e05526818d98ef74a293633d58509
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/identity-appraisals.json
    sha256: 49aa71cf37fb645e71d5708533043e24f49eba69994f60ae49f4821de3421b00
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/inspect_final.py.gz
    sha256: ece3fb2f8b83e6d3cdf8f0bb9261d2d8bc75a84a27bf12d7a466c55d1bf70bbf
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/locator-currentness.json
    sha256: 746a18e7d2db6ef43f882bec0431a21f93244af01ac690fc5a4c77299bc4f99f
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/mapping-appraisals.json
    sha256: 1ac72b10e1fb7bcafec00917054f9bdc26450d9556ee03024425a41c7619bb57
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/native-inspection.execution.json
    sha256: 6d71ccdfb66e9f69d078d920e3dc5a922726a5566ff004182c5e2eb295bb4e6c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/native-inspection.json
    sha256: 56c178c013c3342caff4517360a5e23ffee5862ce2de0097b871382355f980e3
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/native-inspection.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/native-validation.execution.json
    sha256: 03bf811129628400ba55b125560cf42ad6acbbdbb9dfb757f9bb0477abfeeac9
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/native-validation.stderr
    sha256: e2cf5a8ee56373cb7afeb23be8ac2a30d67f13afa55bb51424877fc908e2a25f
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/native-validation.stdout
    sha256: b42ee0197bdb886694684431f9da0d2fba4020263ed572ff756b9eaf0b042ba6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/paragraph-appraisals.json
    sha256: 7bcebac9c8a6535217458dd2fa68e08ec197d8b084fbc25ddd8e77fe32f93812
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/planned-native-commands.json
    sha256: 044fcde3c040e5703785be4b8d794d3c8437354e0f1a77ae8f1db24c50763d1c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/preparation-origin.json
    sha256: 619aa2ea0323ce8156b10fecde591a47b8cf1598f035720b3afe66d4bfb3b008
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/preparation-results.json
    sha256: fef730e51b08aa189c77ee43e3db11678144c7100e975f45947ea79ab66236e2
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/prepare_science.py.gz
    sha256: 3cc4ecfb74fde59f6e8cffbcf5dd705abf24cb7e11bd52cdbd312662cb211170
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/prepare_sealer.py.gz
    sha256: 98b6c2af80adb5972b4c61b2277307a14a17e74dab50e29bf2c4bda5ade9196c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/prereading.json
    sha256: 05ae07faeb7dea89fe2911dcc086be9f8bd8fb17c37b0aac4cd6259ab187da5d
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/prior-native-review-search.json
    sha256: 58071d23f6ffdbdad69757d607ae3814c80f1f1dde418ad2714ca77bb661a456
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/qualifier-appraisals.json
    sha256: 15be162ba2571da0b8bbd851ebbb2024d4d4f7d54fef19f75b5e2c47179495ad
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/read-coverage-final.json
    sha256: c03beb5ef7cd4bd09a4614d88f2561ab0132e4a825d2075aca0eb3d1f25e962c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/read-coverage.json
    sha256: 1990dc8c3432d7ab9f43ce1c94a2e760d3b9bcf747cdd6659d5af1faa574f048
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/record_judgment.py.gz
    sha256: 0ccf6e8342c5783dc796bec972248e84c517f582c6bab150feaf0bcbd06772c2
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/reference-appraisals.json
    sha256: f44907c9cbfe21dbfc8806f7c7a9e4f249a349760e2353553ea7a3d3982f8018
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/run_step.py.gz
    sha256: 87a5a0b4b49d92c272bf799aed2cf7c3aba964bc17465e6f46d6fe37f4870ec0
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/scientific-judgment.json
    sha256: 5e4e2a48c8309ff27643c8d8fda74e6b02e31e9c627e0834070ab27b0641518c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/seal_review.py.gz
    sha256: 6922357818af51fcb9f0cbe554befb53c4caebfa999816ea7a46e3494bf27bff
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/sealer-lineage.json
    sha256: e9803bef2f534e285c2e985383acadfb764440a87ccdb54311ea78885fc148ac
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/sealer-rebase.patch
    sha256: c65e576d3d2770b8695e8b914e3fe8aa7f07ff642a7bf7b8ee9b48c0691b17e6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/sealing-currentness.json
    sha256: 8a698828456625ef6332a7aa9970758bc093d31a5f4e4c4a5764528693ab6b07
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/serialization-attribution.json
    sha256: 95e7df9028644d181cf22ae948248ee30f8537157447b210789d58bc57c51fe9
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/serialization-attribution.patch
    sha256: 28e9f14aaf64b069fae41c294e4628be1f8ab692a644940f82752dc1e06e0c6e
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/shared-QA-currentness.json
    sha256: 9fa2a1ada41b3be547f03e8de1eb7373b5c18408ee70362744086825b4cd926a
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/targets.yaml
    sha256: 467d7f36cdfd6860e489e9f5ad89e9af4dfcb612dee2b27215a9a9324b3ade53
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/validate_proposal.py.gz
    sha256: bb2d8d21a2e264797331c22023b351233353b813af960994ad612a2bf086e0a3
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/whole-source-closure.json
    sha256: 66ec8e3a85488ad5d86ab574b6ff7203720e2f8e34115fbfb89e758069083c94
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/REPORT.md
    sha256: 3b8dd0e71174a09d0a0f506dd28581b0794b0bf1d41448027b28692d917a4849
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/actual-review-tools.json
    sha256: c489e1616d08a8df482869cd7ebe63a279dad1b3126d3bddbc2d7a06b158aa25
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/artifact-manifest.json
    sha256: 15ffe5ae1049abfdd93fa882e336ded44624e2131efecf74f65b57b62fc9af7d
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/attribution-correction.json
    sha256: cb9102349a15311bf96cb636d70cf5e878eaca36619d29baba4e51691324c2ec
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/attribution-correction.patch
    sha256: 95ce431038bbe464873fa12f8687416878110c157b3de5a23f4af3dee474f1b8
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/attribution-successor-result.json
    sha256: e48be2de8a7ec3d270487e4d2099cc9077a02bdfe13bfee7be2b43c565ef51cc
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/canonical-acceptance.json
    sha256: 5e97f64c23ccb7d12a1fd198b49d2325fa937bd1b41a25d454507197aafe1f13
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/check_checkout.py.gz
    sha256: a31ec94319f86a2fdaf154a327d34beff50ad0eaf5c51d2c1c25c4c7d585b615
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/check_target.py.gz
    sha256: ab4aeb7ec0de279c9acaaaaef5abe2a2cc997e63ce0e6d26cfa1c63f3727e138
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/checkout-preservation.json
    sha256: 4d4f5cb80b8c64237ee2f15323ddbc0b32ecb2f8b68dad6944d8315f960c8dfa
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/checkout.execution.json
    sha256: 8d64fa03c97feded60088ca34f5f682f1f194ed2035d3b9d96d8cd53f3614e87
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/checkout.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/checkout.stdout
    sha256: 467e962e9f7ca52cc02292b7704ba5abbcbe4fb86e1ee8937bc09df8f8eff0fe
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/create_attribution_successor.py.gz
    sha256: 1405e951cf65164ed456b6ad3e5925ad98b37d1a6325e7aebf48e62831cef8b8
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/final-helper-lineage.json
    sha256: 77e73a88ff9da8f582db90131b0728192b2f9b388cb8d01584ec33e1df1d60b5
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/final-helper-rebase.patch
    sha256: 4b15a28515baa5de043656ebde09f747fad0b768df7a4fc8a96d2b6cc324b37a
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/handoff.json
    sha256: 87fc22aa9da9a4ec696f5bdc1edb9eb32dac80e593f6e490414dd6b7c1740780
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/helper-lineage.json
    sha256: aadea94a9fa690abe9fdb85c16f4b7f56fef82e91958b74092344aa8552b2b66
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/helper-rebase.patch
    sha256: ba9b65f46e3a1acc50087fa757ec0c9b987efc24bbfe382db8dd3ed5b5ff69b8
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/REPORT.md
    sha256: dc245f27077c370df1a2b5fe3d5108946d02473a1e287da20286ea667c14f25f
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/actual-review-tools.json
    sha256: c489e1616d08a8df482869cd7ebe63a279dad1b3126d3bddbc2d7a06b158aa25
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/artifact-manifest.json
    sha256: 61522df24d1a57c9e112f029e91ce1ab96b00ea55c5e66a98cdf0ee4b3da12f7
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/canonical-acceptance.json
    sha256: 5e97f64c23ccb7d12a1fd198b49d2325fa937bd1b41a25d454507197aafe1f13
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/check_checkout.py.gz
    sha256: a31ec94319f86a2fdaf154a327d34beff50ad0eaf5c51d2c1c25c4c7d585b615
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/check_target.py.gz
    sha256: ab4aeb7ec0de279c9acaaaaef5abe2a2cc997e63ce0e6d26cfa1c63f3727e138
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/checkout-preservation.json
    sha256: 4d4f5cb80b8c64237ee2f15323ddbc0b32ecb2f8b68dad6944d8315f960c8dfa
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/checkout.execution.json
    sha256: 8d64fa03c97feded60088ca34f5f682f1f194ed2035d3b9d96d8cd53f3614e87
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/checkout.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/checkout.stdout
    sha256: 467e962e9f7ca52cc02292b7704ba5abbcbe4fb86e1ee8937bc09df8f8eff0fe
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/final-helper-lineage.json
    sha256: 77e73a88ff9da8f582db90131b0728192b2f9b388cb8d01584ec33e1df1d60b5
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/final-helper-rebase.patch
    sha256: 4b15a28515baa5de043656ebde09f747fad0b768df7a4fc8a96d2b6cc324b37a
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/handoff.json
    sha256: 010df1957c8b1e7bfe6147c44fcdb6541e345639ef4cc602d809cb45fd53b6f6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/helper-lineage.json
    sha256: aadea94a9fa690abe9fdb85c16f4b7f56fef82e91958b74092344aa8552b2b66
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/helper-rebase.patch
    sha256: ba9b65f46e3a1acc50087fa757ec0c9b987efc24bbfe382db8dd3ed5b5ff69b8
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/history/proposal-pre-qa-correction/write_technical_proposal.py.gz
    sha256: faefdfee829b0fc181ffee8152becfb619a8a7b609f124da607c1920afda43d6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/history/target-initial/check_target.py.gz
    sha256: c3841aaed9bdab915e763fa77cc488a84b864116fb1e393816f3cdb49804131f
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/history/target-initial/run_qa.py.gz
    sha256: 8a4abac6b5b80f17758348b06489d7c475cd9a234133dc9e781edc584c99ee38
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/history/target-initial/target-qa-failed.json
    sha256: fdec2b3e8dd2aa6589679e3af7ba6875d0bcc42c652a7abc5ae7ebf100a85ba9
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/history/target-initial/target.execution.json
    sha256: 384ea9430afd2996b7bbad41f8b9e04fe3fd2d01a952ca285a2184a6a56aa3ea
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/history/target-initial/target.stderr
    sha256: dcf421c44f0d7d6f6cc2b76712772c4c168f82de6303e2c6eac3605d35defcb6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/history/target-initial/target.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/inspect_technical.py.gz
    sha256: 5c5693a0107c489e43b194f267f7f5c8a42133052a008d46e7a3c1268539bc0e
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-acceptance.json
    sha256: c25d3612b3e9060c3d7f89fca186a3ebb1f3d277d3e35779d71b980ffbd57c33
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/REPORT.md
    sha256: 854246e3957d7c67d8775154dddcb305a1a96154a12b4a6fa1b60b0775fc48c6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/artifact-manifest.json
    sha256: 7f82ae65c411c81444b591d176ecddad5fd34381d053b37ec062246ecdc488f5
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/check-1.json
    sha256: a3182fc4d12c4a1e5e2d64163e696e7355a031f20acbc07968a197f26796f794
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/check-1.stderr
    sha256: d940c0abdeed39b1e534d34b6aa6c88866d90394d6a7c5b575713668066d69e1
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/check-1.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/check-2.json
    sha256: 368586a54a3c4da910251a414af772febb54a48a6483040b7dc3e44a74010520
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/check-2.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/check-2.stdout
    sha256: fa976d974a09d20ec0cca95f6997bae0e1f495422785b841354c2a6662243b31
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/check-first.py.gz
    sha256: f856320d3d2f856ddf56072bfcb26f0185d024c4108b1af0f3f3af114660628c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/check.py.gz
    sha256: 6a884f7d7b4ae70ed09bd7c31c34e0b111e505c50ba9b583d19eddf47d1180cd
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/checks.json
    sha256: 9017bc376095358add270b12f77a7395ce1f3dd6edaba718b9e689b726ee088b
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/handoff.json
    sha256: 82588756797985d1ef80e2632251d06173a622d4b61d9b896c2bd8bc96490b8b
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/preserved-failures.json
    sha256: 849ded9a245f841dcc85609e444956c935112eee8b0887420d7dc785153dc96d
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/integration-compatibility-review/review-result.json
    sha256: 3249415c1ca107cae81f67a2d1b400f8594b78538494303869d1cc13aaaf6381
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/native-execution-intake.json
    sha256: cd57c1b3b182bdee105dff7ab1357ac72fdd50dccca18f0cb5fde2e69449e581
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/native-sealer-template-review.json
    sha256: b9272b7c3faab74bb9447763094c0f3447d1b68d680dba5704bdcd4f4fdd1884
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/post-package-evidence-retention.json
    sha256: 664e54426e595211789d296a0af3b73f7922d161d08bef9bfb7861b6c6cb7bc6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/preparation-status.json
    sha256: a33e7d13d6d893be50aeb8d1ca0216acc9fe0a5c56ed3138bbc4978ce1dc4317
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/prepare_helpers.py.gz
    sha256: d2cc57d74233547d61eb60c51964c0a07700b3c7c40ed2067e623db830d0ceec
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/prior-actual-review-handoff.json
    sha256: 5a04bf72613deb8a9a5377d8363c59a98b8d82c3aa946dd97641c12c20b75d03
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/review-result.json
    sha256: e1d227a737e0483579bbe41f4b40825e7916f89321375ce50fbccda44b354fce
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/root-scientific-review-handoff.json
    sha256: d4d646bcbb46d5e591818e2e86b2c7538b3299e236a88f32b9d52d6c34646c6b
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/run_qa.py.gz
    sha256: 8a4abac6b5b80f17758348b06489d7c475cd9a234133dc9e781edc584c99ee38
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/scientific-scope-acceptance.json
    sha256: 1319e3a8652b956269884618c035b4b0a5e0ef49319ee562d13edbe9c31789c2
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/seal_review.py.gz
    sha256: b624864d647f6a81dc62cffe6c81d4b499d696f8e646d57f3112354c3435eca8
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/target-helper-correction.json
    sha256: c1eb26f369f4d5824aef4678e6e4ca0e281c00a9b919559f7e7e59f8f3109c81
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/target-helper-correction.patch
    sha256: 5d2c3cd38c2bee4ee157b86bdc5aec5a0fc71894827960e8eaf075207452a5a1
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/target-qa.json
    sha256: e2acd56843664486d7623f2a794d32fa88ab66cb8c4433190c7e019eb242eb4d
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/target.execution.json
    sha256: f8ea6203c2e6597d4cb38b5a800f3ae9fe0dfe2a15b724091eaeaabee0e151b6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/target.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/target.stdout
    sha256: 820280660c0760468b969bed8c39a285a28995b0c17f6435d3ea11407e5b57ed
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/technical-inspect.execution.json
    sha256: 2c6ecd43f7293da6eaedf93e4b0a1d0daaddbff389cb2b811414011cc97a3649
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/technical-inspect.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/technical-inspect.stdout
    sha256: 18777a4a4d591a2b5bbffd3235fc63abba3be112023e1b84afad336f487c4ab6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/technical-proposal.json
    sha256: aa14416837b400521cf6514289fede777899fecad80f5119a6eb918592b34e37
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/technical-targets.json
    sha256: fac4fb6b95c4ff1778e693e4e49215ab791acd9f031c7bdaba24bbc76206ce7b
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/technical-validate.execution.json
    sha256: f8f3975f0312c66ab1367dd901026536f26b73b8f5689dd24f3b4e26c65783d5
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/technical-validate.stderr
    sha256: e2cf5a8ee56373cb7afeb23be8ac2a30d67f13afa55bb51424877fc908e2a25f
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/technical-validate.stdout
    sha256: b42ee0197bdb886694684431f9da0d2fba4020263ed572ff756b9eaf0b042ba6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/validate_technical.py.gz
    sha256: f3b80cff4b9abe978560ed341787750718ef724d4e8771dafb41f3070bb10f17
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/visual-assessment.json
    sha256: 6575db3eb58877e29e2c69f25d53bfc14916d548a352d0bcd00a4092f8e6b84f
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/original-sealed-review/write_technical_proposal.py.gz
    sha256: 252d04d426331aa3f989fc5f30de78087a088230915a88d624217505cc54e7dc
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/proposal-pre-qa-correction/write_technical_proposal.py.gz
    sha256: faefdfee829b0fc181ffee8152becfb619a8a7b609f124da607c1920afda43d6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/target-initial/check_target.py.gz
    sha256: c3841aaed9bdab915e763fa77cc488a84b864116fb1e393816f3cdb49804131f
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/target-initial/run_qa.py.gz
    sha256: 8a4abac6b5b80f17758348b06489d7c475cd9a234133dc9e781edc584c99ee38
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/target-initial/target-qa-failed.json
    sha256: fdec2b3e8dd2aa6589679e3af7ba6875d0bcc42c652a7abc5ae7ebf100a85ba9
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/target-initial/target.execution.json
    sha256: 384ea9430afd2996b7bbad41f8b9e04fe3fd2d01a952ca285a2184a6a56aa3ea
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/target-initial/target.stderr
    sha256: dcf421c44f0d7d6f6cc2b76712772c4c168f82de6303e2c6eac3605d35defcb6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/history/target-initial/target.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/inspect_technical.py.gz
    sha256: 5c5693a0107c489e43b194f267f7f5c8a42133052a008d46e7a3c1268539bc0e
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-acceptance.json
    sha256: c25d3612b3e9060c3d7f89fca186a3ebb1f3d277d3e35779d71b980ffbd57c33
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/REPORT.md
    sha256: 854246e3957d7c67d8775154dddcb305a1a96154a12b4a6fa1b60b0775fc48c6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/artifact-manifest.json
    sha256: 7f82ae65c411c81444b591d176ecddad5fd34381d053b37ec062246ecdc488f5
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/check-1.json
    sha256: a3182fc4d12c4a1e5e2d64163e696e7355a031f20acbc07968a197f26796f794
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/check-1.stderr
    sha256: d940c0abdeed39b1e534d34b6aa6c88866d90394d6a7c5b575713668066d69e1
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/check-1.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/check-2.json
    sha256: 368586a54a3c4da910251a414af772febb54a48a6483040b7dc3e44a74010520
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/check-2.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/check-2.stdout
    sha256: fa976d974a09d20ec0cca95f6997bae0e1f495422785b841354c2a6662243b31
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/check-first.py.gz
    sha256: f856320d3d2f856ddf56072bfcb26f0185d024c4108b1af0f3f3af114660628c
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/check.py.gz
    sha256: 6a884f7d7b4ae70ed09bd7c31c34e0b111e505c50ba9b583d19eddf47d1180cd
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/checks.json
    sha256: 9017bc376095358add270b12f77a7395ce1f3dd6edaba718b9e689b726ee088b
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/handoff.json
    sha256: 82588756797985d1ef80e2632251d06173a622d4b61d9b896c2bd8bc96490b8b
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/preserved-failures.json
    sha256: 849ded9a245f841dcc85609e444956c935112eee8b0887420d7dc785153dc96d
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/review-result.json
    sha256: 3249415c1ca107cae81f67a2d1b400f8594b78538494303869d1cc13aaaf6381
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/native-execution-intake.json
    sha256: cd57c1b3b182bdee105dff7ab1357ac72fdd50dccca18f0cb5fde2e69449e581
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/native-sealer-template-review.json
    sha256: b9272b7c3faab74bb9447763094c0f3447d1b68d680dba5704bdcd4f4fdd1884
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/post-package-evidence-retention.json
    sha256: 664e54426e595211789d296a0af3b73f7922d161d08bef9bfb7861b6c6cb7bc6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/preparation-status.json
    sha256: a33e7d13d6d893be50aeb8d1ca0216acc9fe0a5c56ed3138bbc4978ce1dc4317
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/prepare_helpers.py.gz
    sha256: d2cc57d74233547d61eb60c51964c0a07700b3c7c40ed2067e623db830d0ceec
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/prior-actual-review-handoff.json
    sha256: 5a04bf72613deb8a9a5377d8363c59a98b8d82c3aa946dd97641c12c20b75d03
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/review-result.json
    sha256: 298e637f4df17a440dc6102e6f52e0c3b3023044d3289b5cc548c815fd337ef5
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/root-scientific-review-handoff.json
    sha256: d4d646bcbb46d5e591818e2e86b2c7538b3299e236a88f32b9d52d6c34646c6b
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/run_qa.py.gz
    sha256: 8a4abac6b5b80f17758348b06489d7c475cd9a234133dc9e781edc584c99ee38
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/scientific-scope-acceptance.json
    sha256: 1319e3a8652b956269884618c035b4b0a5e0ef49319ee562d13edbe9c31789c2
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/seal_attribution_successor.py.gz
    sha256: 52434116541e8b63fcbeb488d0816acab14a556a919efbd57949477da48fb234
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/seal_review.py.gz
    sha256: 6fe624043cf6fbe9d8585d749bffab58f484df6fdfacd6f3d69593a2e7e87455
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/target-helper-correction.json
    sha256: c1eb26f369f4d5824aef4678e6e4ca0e281c00a9b919559f7e7e59f8f3109c81
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/target-helper-correction.patch
    sha256: 5d2c3cd38c2bee4ee157b86bdc5aec5a0fc71894827960e8eaf075207452a5a1
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/target-qa.json
    sha256: e2acd56843664486d7623f2a794d32fa88ab66cb8c4433190c7e019eb242eb4d
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/target.execution.json
    sha256: f8ea6203c2e6597d4cb38b5a800f3ae9fe0dfe2a15b724091eaeaabee0e151b6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/target.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/target.stdout
    sha256: 820280660c0760468b969bed8c39a285a28995b0c17f6435d3ea11407e5b57ed
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/technical-inspect.execution.json
    sha256: 2c6ecd43f7293da6eaedf93e4b0a1d0daaddbff389cb2b811414011cc97a3649
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/technical-inspect.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/technical-inspect.stdout
    sha256: 18777a4a4d591a2b5bbffd3235fc63abba3be112023e1b84afad336f487c4ab6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/technical-proposal.json
    sha256: 4a88b27e77178d9305cadf3bab20b21bdf500609a6ef3797559ae05c648ffd9e
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/technical-targets.json
    sha256: fac4fb6b95c4ff1778e693e4e49215ab791acd9f031c7bdaba24bbc76206ce7b
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/technical-validate.execution.json
    sha256: d723658e9a62d699165e4ccc88d085ba8a4bade47add3119abab8409bb0bdf01
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/technical-validate.stderr
    sha256: e2cf5a8ee56373cb7afeb23be8ac2a30d67f13afa55bb51424877fc908e2a25f
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/technical-validate.stdout
    sha256: b42ee0197bdb886694684431f9da0d2fba4020263ed572ff756b9eaf0b042ba6
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/validate_technical.py.gz
    sha256: f3b80cff4b9abe978560ed341787750718ef724d4e8771dafb41f3070bb10f17
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/visual-assessment.json
    sha256: 6575db3eb58877e29e2c69f25d53bfc14916d548a352d0bcd00a4092f8e6b84f
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/write_technical_proposal.py.gz
    sha256: 6aff171911fcee50538459f5439c07d147cc990e0b1614d18a5f817ad54121fc
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/maintained-review-acceptance.json
    sha256: 14fb0c73f105ac29a8c9bd97f27909fb192d6b4f42fe844d18e31ba079c417df
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/root-storage-map.json
    sha256: 55a837210044e4043acd61c2e0cd4441cde304d520bbafc06e0755eb78e7d334
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/scientific-review-acceptance.json
    sha256: 06fcf3fe2f48324880f3c85b5286709f6b7b61001fd3c53df01a24cb08d34180
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/native-integration/storage-ledger.json
    sha256: c16440887a714410600077c387447067aa5316e699e32e4a5391e5bedbc4f0d9
    role: context
  - path: research/pathway_additions/2026-10-12-next-243/verify_portable.py.gz
    sha256: 039e18aa6cd8de2df6244c19ebb6847130827f4d8f072cf24b8e52c670206eaa
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/build_ontology_identifier_snapshot.py
    sha256: fc8bee76c1c07c4d3b86eb72021f8eaf8203ae339258ff16768dd3e1f1b2be81
    role: context
  - path: src/pathwaymech/schema.py
    sha256: bd99c1e6ca1f6eec5c82c58aa1ae3f43f696d30be66fbe0977dcace81292e0b8
    role: context
scope:
  description: Two source manifest/snapshot owners after completed record 243 gates,
    with complete maintained context.
  selection: Both nonrecord primary owners from clean committed 240 baseline 63bc0ba99c63e4d4cdbdf70b8fb3f6f8417eeacf;
    no sampling.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - owner-1
  - owner-2
  exclusions:
  - target: New primary scientific judgment
    reason: Separate independent maintained SCI.
  - target: Publication and browser interaction
    reason: Outside this local technical review.
targets:
- target_id: owner-1
  path: conf/identifier_sources.json
  label: conf/identifier_sources.json
  kind: maintained
  ownership_note: Exact adopted source manifest or native source-authority snapshot;
    product runtime and ontology are unchanged. Generated snapshots require rebuilding
    from maintained configuration and adapters.
- target_id: owner-2
  path: data/identifier_authorities/sources.json
  label: data/identifier_authorities/sources.json
  kind: maintained
  ownership_note: Exact adopted source manifest or native source-authority snapshot;
    product runtime and ontology are unchanged. Generated snapshots require rebuilding
    from maintained configuration and adapters.
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
  command: '/private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B scripts/new_history_record.py
    --kind record --slug baesr-two-component-signal-transduction --target-root data/pathways
    --event CREATE --outcome changed --summary ''Add evidence-backed E. coli BaeSR
    signal transduction.'' --details ''Exact accepted PathBank:SMP0002123: 13 paragraphs,
    15 edges, 8 qualifiers, 12 IDs, 18 references, 4 mappings. Preserve complete native
    states, two phosphorylation events, six formal sides and two interpreted donor
    sides, construct/sequence/site/chemical/access limitations. Whole originals, receipts
    and prior failed attempts retained in research/pathway_additions/2026-10-12-next-243.
    Maintained gates and native reviews pending.'' --actor-name codex --agent-tool
    codex --model gpt-6'
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
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B scripts/new_history_record.py
    --kind infrastructure --slug baesr243-native-authority --path conf/identifier_sources.json
    --event EDIT --outcome changed --summary 'Add BaeSR ordinary PathBank identity
    authority and source snapshot.' --details 'Manifest 892-row prefix retained with
    one append, source 2694 terms/712 owners; all old authority objects and first
    owners exact. Runtime code and ontology unchanged. Old KGX edge payloads/order
    and contexts retained; six contexts added and exact accepted ATP/ADP node encounter
    permutation. Histories precede SSSOM/render; maintained gates/native reviews pending.'
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
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B -m pytest
    -q -p no:cacheprovider --basetemp /private/tmp/pathwaymech-next-243-local-gate-tests-20261012
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
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-243-independent-maintained-tech-20261012/check_target.py
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
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-243-independent-maintained-tech-20261012/check_checkout.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - independent-checkout
evidence:
- evidence_id: native-history-1
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/history-1.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by root; this reviewer did not repeat it.
  snapshot_sha256: 61f0a3d5cc7fa0851b6165fe84ab713887006e601e6b924f6ea81e4e888b7e98
- evidence_id: native-history-2
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/history-2.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by root; this reviewer did not repeat it.
  snapshot_sha256: 83cac1e13ad4099806a540562eea680ce98325320b866b2aa3cde22e613e863d
- evidence_id: native-sssom
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/sssom.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by root; this reviewer did not repeat it.
  snapshot_sha256: 0c650ee9fb7d3dc5d7ec97058434d6510b037cfab727460d05d7606dac0779b2
- evidence_id: native-render
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/render.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by root; this reviewer did not repeat it.
  snapshot_sha256: b3af417cc226ebb7556fbf08577d2e74f2148117b13824fa1dfe73573834003e
- evidence_id: native-skills
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/history-and-generation/skills.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by root; this reviewer did not repeat it.
  snapshot_sha256: 3361284edb5808b1719d09e3261f2b22bb05da1be77de61b63517535b9ad0ae9
- evidence_id: native-validate
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/validate.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by root; this reviewer did not repeat it.
  snapshot_sha256: 9dc9b518ce37d31e23047ca737443f8281f228fb74bfc7ca493dbb8308be231b
- evidence_id: native-tests
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/tests.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by root; this reviewer did not repeat it.
  snapshot_sha256: 6ddf943cc4462f34f5ed1509d1c3750f62faac89ed877a1acf42e9cdf395892a
- evidence_id: native-lint
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/lint.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by root; this reviewer did not repeat it.
  snapshot_sha256: 557a452124f6fda677efb6eff1d959aff9bf53fda4abb0e4fb06b636f42e36bd
- evidence_id: native-kgx
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/remaining-offline-gates/kgx.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by root; this reviewer did not repeat it.
  snapshot_sha256: 5c0e76cd2dc22d91323e5de6a0d86483f42e531343d6acf840f279d43d80023c
- evidence_id: native-vendored
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/vendored-gate/vendored.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by root; this reviewer did not repeat it.
  snapshot_sha256: fa82b46a641ca1fa0435353c9dc640ad161c1fbd75c127c7ad6a70eb864a05e7
- evidence_id: native-diff-check
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/diff-check.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by root; this reviewer did not repeat it.
  snapshot_sha256: 677a89dbe4d15cdbc6209e68acfcd7f262177a08893962e33bb7765e43c6134b
- evidence_id: native-site-current
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-qa/actual-native/final-gates/site-current.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Actual native command and complete original streams verified. Executed
    by root; this reviewer did not repeat it.
  snapshot_sha256: 696729c51f9e2bc05babb0f6e72fe45ef6e6188bde687a990106c1706f8449eb
- evidence_id: independent-target
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/target.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: This reviewer executed complete current target/render/export or physical
    checkout/cache checks after native gates completed.
  snapshot_sha256: f8ea6203c2e6597d4cb38b5a800f3ae9fe0dfe2a15b724091eaeaabee0e151b6
- evidence_id: independent-checkout
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/checkout.execution.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: This reviewer executed complete current target/render/export or physical
    checkout/cache checks after native gates completed.
  snapshot_sha256: 8d64fa03c97feded60088ca34f5f682f1f194ed2035d3b9d96d8cd53f3614e87
- evidence_id: target-helper-correction
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/target-helper-correction.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Initial external target QA failed on an append-only context assumption.
    Exact helper, receipt, streams and partial checks are retained; the bounded corrected
    check requires whole canonical KGX equality, every old context as an exact ordered
    subsequence and precisely the accepted target contexts/multiplicity. Checkout
    and all native gates passed first attempt and were not repeated.
  snapshot_sha256: c1eb26f369f4d5824aef4678e6e4ca0e281c00a9b919559f7e7e59f8f3109c81
- evidence_id: native-packet
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/native-execution-intake.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Fresh no-follow complete closure of 81 native artifacts plus two seals,
    including hidden/ignored paths and every complete phase stream.
  snapshot_sha256: cd57c1b3b182bdee105dff7ab1357ac72fdd50dccca18f0cb5fde2e69449e581
- evidence_id: canonical
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/canonical-acceptance.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Root accepted one native source builder and byte-exact inherited ontology;
    all prior objects/order, first owners and six exact added graph contexts survive.
  snapshot_sha256: 5e97f64c23ccb7d12a1fd198b49d2325fa937bd1b41a25d454507197aafe1f13
- evidence_id: prior-actual-audit
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/prior-actual-review-handoff.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Distinct Adapter independent audit checked all 1922 actual artifacts plus
    two seals, all 242 scientific records, complete source objects/order and KGX.
    That accepted audit is inherited; I audited earlier canonical preparation, not
    this actual execution.
  snapshot_sha256: 5a04bf72613deb8a9a5377d8363c59a98b8d82c3aa946dd97641c12c20b75d03
- evidence_id: integration
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-acceptance.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Root accepted the exact three primary owners and 12 complete planned destinations
    with guarded native stages. The preparer whole 2421-body portable replay is inherited.
  snapshot_sha256: c25d3612b3e9060c3d7f89fca186a3ebb1f3d277d3e35779d71b980ffbd57c33
- evidence_id: integration-compatibility
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/integration-compatibility-review/handoff.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Complete distinct 14-file compatibility review is retained with both seals,
    original Rhea-role assertion failure, exact failed/successor helpers and full
    streams. Its accepted mechanics appraisal is inherited, not repeated.
  snapshot_sha256: 82588756797985d1ef80e2632251d06173a622d4b61d9b896c2bd8bc96490b8b
- evidence_id: sealer-template
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/native-sealer-template-review.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: This reviewer read the whole bounded native sealer template and exact predecessor
    diff; receipt-origin/stream/closure controls remain unchanged. Static template
    review is distinct from root actual native execution and final runner binding.
  snapshot_sha256: b9272b7c3faab74bb9447763094c0f3447d1b68d680dba5704bdcd4f4fdd1884
- evidence_id: post-package-retention
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/post-package-evidence-retention.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Whole post-package compatibility and template-review bodies are retained
    with exact original paths, sizes, hashes and modes. These reviews postdate the
    scientific portable package and are retained separately here.
  snapshot_sha256: 664e54426e595211789d296a0af3b73f7922d161d08bef9bfb7861b6c6cb7bc6
- evidence_id: target-results
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/target-qa.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Whole accepted YAML, 15 arrows, 18 display nodes, eight qualifiers, 12
    identities, 18 references and all 31 evidence occurrences match. Current graph
    equals accepted outputs and the root-viewed static preview; mappings retain 66
    old plus four new rows.
  snapshot_sha256: e2acd56843664486d7623f2a794d32fa88ab66cb8c4433190c7e019eb242eb4d
- evidence_id: checkout-results
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/checkout-preservation.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Complete physical inventory includes hidden/ignored paths. All 241 old
    records/pages, 126 review pairs, 410 histories and 800 cache entries remain exact
    outside the accepted scope.
  snapshot_sha256: 4d4f5cb80b8c64237ee2f15323ddbc0b32ecb2f8b68dad6944d8315f960c8dfa
- evidence_id: visual
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/visual-assessment.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Original preview assessment by Nitrate; root independently viewed this
    same whole raster as documented in the root scientific review. Current whole SVG/CSS/JS
    equality binds it. No personal new visual or browser assessment is claimed here.
  snapshot_sha256: 6575db3eb58877e29e2c69f25d53bfc14916d548a352d0bcd00a4092f8e6b84f
- evidence_id: science-scope
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/scientific-scope-acceptance.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Exact accepted corrected scientific target and complete source-state/sequence/taxon/chemical/GO
    limitations are inherited. Separate maintained SCI judgment belongs to Adapter.
  snapshot_sha256: 1319e3a8652b956269884618c035b4b0a5e0ef49319ee562d13edbe9c31789c2
- evidence_id: root-preview-reading
  kind: prior_review
  reference: research/pathway_additions/2026-10-12-next-243/native-integration/independent-tech-review/root-scientific-review-handoff.json
  accessed_at: '2026-10-13T00:45:24Z'
  support: supports
  summary: Root scientific review explicitly documents personal full static-raster
    reading, including disconnected phosphate and overlap/truncation/blank-space limitations.
  snapshot_sha256: d4d646bcbb46d5e591818e2e86b2c7538b3299e236a88f32b9d52d6c34646c6b
assessments:
- assessment_id: owner-1
  area: ownership
  topic: conf/identifier_sources.json
  outcome: supported
  summary: The whole maintained source manifest or source-authority snapshot equals
    the exact accepted actual output. One ordinary PathBank source entry adds six
    selected terms; product runtime and ontology remain unchanged. Identity/name projection
    does not assert typed biochemical context.
  target_ids:
  - owner-1
  evidence_ids:
  - canonical
  - prior-actual-audit
  - independent-target
  - integration
- assessment_id: owner-2
  area: ownership
  topic: data/identifier_authorities/sources.json
  outcome: supported
  summary: The whole maintained source manifest or source-authority snapshot equals
    the exact accepted actual output. One ordinary PathBank source entry adds six
    selected terms; product runtime and ontology remain unchanged. Identity/name projection
    does not assert typed biochemical context.
  target_ids:
  - owner-2
  evidence_ids:
  - canonical
  - prior-actual-audit
  - independent-target
  - integration
- assessment_id: prior-preservation
  area: provenance
  topic: Whole authority and checkout preservation
  outcome: supported
  summary: The 893-row manifest retains all 892 prior rows. All 2688 old source terms/711
    owners and their nested encounter order survive in 2694 terms/712 owners. Ontology
    remains 2016 terms/five owners with exact old bytes. All 241 old scientific records/pages,
    126 review pairs and 410 histories remain exact; two new histories precede SSSOM/render.
  target_ids:
  - owner-1
  - owner-2
  evidence_ids:
  - canonical
  - prior-actual-audit
  - checkout-results
  - native-history-1
  - native-history-2
- assessment_id: graph-exports
  area: graph
  topic: Whole graph, exact contexts and encounter order
  outcome: supported
  summary: All 15 arrows, 18 display nodes, eight qualifiers, 18 references and 12
    identities resolve. Whole current KGX equals accepted 4363 nodes/12125 edges.
    Every prior edge payload and relative order and every prior node aggregate/context
    survives. Six exact target contexts are inserted at the accepted positions, preserving
    every prior context in exact relative order and whole payload. The complete old-node
    vector equals the accepted ATP/ADP encounter permutation; removing those two IDs
    preserves all other relative order. Phosphate remains unconnected.
  target_ids:
  - owner-1
  - owner-2
  evidence_ids:
  - canonical
  - prior-actual-audit
  - target-results
  - target-helper-correction
  - visual
- assessment_id: mapping-export
  area: representation
  topic: Complete source mappings
  outcome: supported
  summary: Native SSSOM preserves its complete header and all 66 old rows, cells,
    multiplicity and relative order, adding four exact mappings for 70 total.
  target_ids:
  - owner-1
  - owner-2
  evidence_ids:
  - native-sssom
  - target-results
- assessment_id: native-gates
  area: schema
  topic: Fresh maintained validation
  outcome: supported
  summary: 'All nine native gates passed for 242 records: 4773 tests passed, 3 skipped
    and 3 warnings retained. Root executed those commands; this reviewer verified
    exact receipts and streams without repeating passing broad gates.'
  target_ids:
  - owner-1
  - owner-2
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
  topic: Whole source and review provenance
  outcome: supported
  summary: Accepted preparation retains 2421 whole portable bodies. Its complete replay
    is inherited; maintained dossier/index bodies and all 18 reference-hash bindings
    are fresh. Ordinary source identity/name support remains separate from scientific
    assembly, donor-state, site, phosphate and strain interpretation.
  target_ids:
  - owner-1
  - owner-2
  evidence_ids:
  - integration
  - integration-compatibility
  - sealer-template
  - post-package-retention
  - canonical
  - science-scope
  - independent-target
  - checkout-results
findings: []
actions: []
limitations:
- One external target-QA attempt failed because its helper required new contexts to
  append. The exact failed helper/streams/partial report are retained. A narrow helper
  correction passed; no product, accepted native output or native gate was changed.
  Complete checkout passed once and was not repeated.
- Prior distinct actual-output audit, accepted scientific reading and integration
  portable replay are inherited. Fresh scope is maintained record/page/export/owner
  preservation, full physical inventory/cache and native receipt/stream currentness.
  No paper reread or broad test rerun.
- Only one source builder ran for the accepted canonical output. Ontology was reused
  byte exactly. Historical SQL descriptors retain obsolete rehash prose; no new SQL
  hash/query or ontology builder is claimed.
- The root personally viewed static light preview is inherited after exact whole current
  SVG/CSS/JS equality. Dense convergence, long return paths, overlapping/truncated
  labels and tall blank canvas remain. No personal new visual, interactive, responsive,
  keyboard, dark or print check.
- Actual regression retains 3 skips and 3 warnings with 4773 passes.
- Evidence references name concrete proposed dossier destinations. Exact-byte adoption
  and current input inspection/validation are required before native save; this external
  proposal itself is not saved.
notes:
- Every native input hash was rechecked after actual gates and fresh maintained QA,
  before this proposal.
- The technical review uses the native repository review contract and does not claim
  the separate full scientific skill workflow.
- No maintained product edit, review save, public action or licensing clearance was
  performed.
links: []
tags:
- baesr
- pathbank
- technical-review
- local-only
```

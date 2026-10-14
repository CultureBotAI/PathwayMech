# Initial integration review of shikimate degradation II

- Review: 20261014T205748Z-shikimate-ii-integration-initial
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-14T20:23:04Z
- Finished UTC: 2026-10-14T20:57:48Z
- Reviewer: codex /root/next258_integration (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

Independent integration and provenance checks pass, including exact baseline preservation, full authority rebuilds, typed gene gates, evidence retention and SVG/KGX fidelity. All initial repository gates passed. Two minor reference-display defects require bounded YAML corrections. Scientific interpretation, including separately tracked downstream category issue #549, is not reassessed here.

## Scope And Provenance

One-record provenance, authority, typed identifier and generated-export integration audit. This is not a literature/scientific review.

Selection: Exact new maintained record MetaCyc:PWY-6419 and its frozen initial author integration.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 495de27ec09f99367d1cdd5c457a5e54a93c9a0b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-6419 | data/pathways/shikimate-degradation-ii.yaml | maintained | shikimate degradation II |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Independent Git baseline and complete-original cache comparison | passed | True | MetaCyc:PWY-6419 | All 254 baseline records, authority objects and original source digests preserved. |
| Independent authority promotion and selection comparison | passed | True | MetaCyc:PWY-6419 | Seven exact planned additions, six exact new owners; no policy/schema/governed drift. |
| Independent canonical source builder | passed | True | MetaCyc:PWY-6419 | Builder exited zero; reproduced full output is byte-identical to promoted snapshot. The enclosing reviewer summary later failed; builder receipts remain successful. |
| Independent canonical ontology builder | passed | True | MetaCyc:PWY-6419 | Builder exited zero; reproduced full output is byte-identical to promoted snapshot. The enclosing reviewer summary later failed; builder receipts remain successful. |
| Independent consumer replay | passed | True | MetaCyc:PWY-6419 | Both reconstructed complete authority snapshots accepted. |
| Actual gene identity/category/label probes | passed | True | MetaCyc:PWY-6419 | 13 actual-source acceptance/rejection cases passed after documented fixture repair. |
| SVG and KGX fidelity inspection | passed | True | MetaCyc:PWY-6419 | 32 edges, nine qualified endpoints and 30 node contexts preserved exactly. |
| just render-pages | passed | True | MetaCyc:PWY-6419 | Completed with exit code 0; exact retained log inspected. Root executed; reviewer independently checked captured log digest and relevant input hashes. |
| just validate | passed | True | MetaCyc:PWY-6419 | history links: 447 record(s), 0 invalid; 447 history record(s) valid against src/pathwaymech/schema/history.yaml; validated 255 pathway records; validated 255 records against the closed LinkML schema; validated 30 source records Root executed; reviewer independently checked captured log digest and relevant input hashes. |
| just test | passed | True | MetaCyc:PWY-6419 | =========== 5118 passed, 3 skipped, 7 warnings in 1443.06s (0:24:03) =========== Root executed; reviewer independently checked captured log digest and relevant input hashes. |
| just lint | passed | True | MetaCyc:PWY-6419 | All checks passed! Root executed; reviewer independently checked captured log digest and relevant input hashes. |
| just vendored-check | passed | True | MetaCyc:PWY-6419 | Completed with exit code 0; exact retained log inspected. Root executed; reviewer independently checked captured log digest and relevant input hashes. This is the successful scoped retry after the preserved initial DNS failure. |
| git diff --check | passed | True | MetaCyc:PWY-6419 | Completed with exit code 0; exact retained log inspected. Root executed; reviewer independently checked captured log digest and relevant input hashes. |

## Scientific And Domain Assessments

### Baseline, authority selection and original sources

provenance: supported. Targets: MetaCyc:PWY-6419.

All 254 pre-existing pathway YAMLs, all 4,947 authority terms/865 source owners and the 1,041-entry manifest prefix are unchanged. The only authority additions are the seven planned IDs backed by six new complete source entries and the pinned Rhea source.

### Canonical builder and consumer reproducibility

consistency: supported. Targets: MetaCyc:PWY-6419.

Independent full source and ontology builds reproduce the promoted snapshot bytes, and both canonical consumers accept the reconstructed data. The corpus selector supplies IDs only; issuing originals supply labels.

### Native gene label/category enforcement

grounding: supported. Targets: MetaCyc:PWY-6419.

Actual selected KEGG genes resolve to their complete typed native owners. Canonical locus labels and participant/gene placement remain enforced before contextual exceptions. The five code-review input files remain unchanged.

### Exact evidence retention and failure accounting

provenance: supported. Targets: MetaCyc:PWY-6419.

All 187 author-artifact mappings and source-ledger bindings are byte-verified. The separate scientific-review package also preserves all 18 mapped artifacts, its transcript wrapper and 36 inspected input hashes. Initial author failures and two reviewer harness failures remain explicit; corrected execution does not rewrite earlier evidence.

### Claim-payload fidelity in generated SVG and KGX

graph: supported. Targets: MetaCyc:PWY-6419.

All 32 edges, nine qualified endpoints and 30 local node contexts survive export with complete evidence and reference metadata. This does not certify biological category choices or source interpretation.

### Initial full-corpus repository gates

schema: supported. Targets: MetaCyc:PWY-6419.

All six effective initial gates passed on the unchanged reviewed core input bytes. The first vendored-check failed DNS resolution; its failure is retained and the same command passed on a scoped network retry. Four prior successes were preserved, followed by the remaining whitespace check. Deterministic validity is separate from scientific approval.

### Human-readable reference source versions

representation: concern. Targets: MetaCyc:PWY-6419.

Five reference entries contain joined words/date-number tokens, and one additional UniProt reference displays serialized entryAudit JSON. The generated page faithfully repeats these maintained strings; the fixes belong to the YAML reference metadata.

## Findings

### F1: Reference source versions concatenate words with dates and numbers

minor / open / confirmed; issue key: shikimate-ii-reference-source-version-spacing.

The rendered references reproduce retrieved2026-10-14 in PMID19376919, PMID24674055 and PMID32822353, Table1 twice in PMID23929881, and returned403 in PMID25406451. Normalize spacing and readable wording in maintained source_version strings while preserving retrieval dates, artifact digests and access limitations. This is a confirmed new-record recurrence related to broad issue #522; the scoped fix does not close that older corpus-wide issue.

### F2: ShiR reference displays serialized UniProt audit JSON as a version

minor / open / confirmed; issue key: shikimate-ii-uniprot-source-version-json.

Exactly one new-record reference, UniProtKB:A4QH19, renders its entire serialized entryAudit mapping under source version at page #reference-31. Replace the display string with readable entry/version/date text grounded in the same complete original; retain its source_sha256 and the complete JSON in raw evidence. A4QH18 already uses readable text. This bounded recurrence is related to broad issue #523 and does not establish that older records are fixed.

## Recommended Actions And Acceptance Checks

### correct-reference-display

Normalize the six affected reference source-version fields, preserving exact evidence scope and source digests; regenerate Pages and rerun required gates. Leave older broad issues #522/#523 open unless independently resolved.

- No source_sha256, identifier, URL, access limitation or mechanistic edge changes from this presentation correction.
- Inspect generated references #25, #26, #27, #28, #30 and #31 for readable date/version wording.
- just render-pages; just validate; just test; just lint; git diff --check

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/pathways/shikimate-degradation-ii.yaml | supports | Full initial maintained record: 30 named IDs, 32 mechanistic edges, nine qualified endpoints and 31 references. |
| baseline | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/baseline-audit-results.json | supports | Independently compared all 254 baseline YAMLs with Git and staged copies, all 4,947 authority terms and 865 source-owner objects, 1,041-entry manifest prefix, governed files, schema and identifier policy. |
| cache | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/complete-original-cache-check.json | supports | Independent streaming SHA-256 verification of all 1,062 recursive source descriptors across 1,046 paths, including companion source objects. |
| union | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/union-audit-results.json | supports | Exactly seven planned identifiers and six source owners added; promoted bytes match union outputs and the maintained record equals the frozen assembled draft. |
| source-replay | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/source_builder-replay-receipt.json | supports | Independent canonical source builder exited zero and reproduced the promoted source snapshot byte for byte. |
| ontology-replay | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/ontology_builder-replay-receipt.json | supports | Independent canonical ontology builder exited zero and reproduced the promoted ontology snapshot byte for byte. |
| consumer | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/consumer-replay-results.json | supports | Canonical consumer accepts both independently reconstructed snapshots: 2,863 source terms/866 owners and 2,091 ontology terms/five owners. |
| typed | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/typed-integration-results.json | supports | Thirteen reviewer-executed file-based cases using the three actual KEGG gene owners preserve locus labels and reject aliases, incorrect categories/sections and contextual-label waivers. |
| code-review | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/code-review-verification.json | supports | Independently inspected the separate code reviewer’s 11 frozen artifacts, five unchanged implementation/test/doc inputs, 432-test regression receipt, 60 adversarial outcomes and four complete original CDS responses. These are the separate reviewer’s executions. |
| retention | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/retention/results.json | supports | Delegated independent provenance audit verifies 187 mappings, 23 explicit external bindings, 385 raw-source ledger entries and seven original package manifests; 15 failure-evidence items preserved. Inventories include hidden and ignored files. |
| science-retention | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/science-retention-audit.json | supports | Independent provenance-only follow-up verifies all 18 scientific-review artifact mappings, exact recovery of the 27,961-byte transcript wrapper, all 13 external manifest artifacts and 36 shared-inspection input hashes; 116 checks passed. Scientific conclusions are not reassessed. |
| references | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/reference-original-bindings.json | supports | All 31 maintained reference source digests match independently hashed originals, including the complete GO SQL database. This verifies byte identity, not scientific support. |
| exports | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/graph-export-results.json | supports | Parsed generated SVG/KGX preserve all 32 edges, all nine qualified endpoints, complete evidence/reference payloads and all 30 per-record node contexts. |
| display | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/reference-display-findings.json | refutes | Direct YAML-to-rendered-reference comparison demonstrates joined words/date-number tokens and one serialized UniProt entryAudit JSON source-version value. |
| policy | conf/identifier_policy.yaml | supports | Existing canonical and contextual label policy is unchanged; typed native genes require canonical locus labels and gene placement. |
| wrapper-failure | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/consumer-wrapper-failure.json | context_only | Preserved reviewer wrapper failure after both successful builder runs; the return-shape summary error was corrected by a separate consumer-only replay. |
| probe-failure | research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/attempt-typed-probe-missing-collections/receipt.json | context_only | Preserved reviewer fixture omission rejected before typed semantics were reached; corrected fixture replay passes all 13 cases. |
| gates | research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/receipts.json | supports | Root executed all six initial repository gates against the same unchanged core input hashes; this reviewer inspected exact receipts and decoded retained logs. |
| gate-retry | research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/failed-attempts.json | context_only | The first vendored-check attempt failed DNS resolution. Its exact initial receipt and original log remain retained; only the same network command was retried successfully before the remaining whitespace check. The four prior successes were preserved and core inputs did not change. |
| gate-original | research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/initial-attempt-receipts.json | context_only | Original five-command receipt sequence retains four successful checks and the failed vendored fetch; it is not replaced by the effective final success sequence. |
| gate-original-log | research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/just-vendored-check.log.json | context_only | Lossless wrapper of the original 378-byte vendored-check failure log explicitly records DNS resolution failure for raw.githubusercontent.com. |
| tested-inputs | research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/tested-core-input-hashes.json | supports | Root gate input hashes bind the maintained record, implementation, authorities, schema and generated artifacts; intersecting review inputs were independently compared. |

## Limits And Additional Notes

- This provenance-only review does not reassess scientific claim support, sequence translation, organism/genome crosswalk biology, full-source exhaustiveness or licensing clearance.
- The separate code reviewer executed the cited 432-test regression and 60-case adversarial suite; this reviewer inspected their exact artifacts and executed the additional 13 actual-source consumer cases.
- Full original caches and reproduced trial snapshots remain external under /private/tmp and hash-bound. Local reproducibility was demonstrated; long-term external-cache durability is not established.
- Generated output checks parsed HTML/SVG/KGX payloads and anchors, rather than performing a browser screenshot layout audit.
- The input state is an inspected working tree. A later exact-commit review is required after corrections, saved review bundles and final gates.
- Two reviewer harness mistakes are preserved and corrected; neither canonical builder failed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T205748Z-shikimate-ii-integration-initial
kind: record
repository: CultureBotAI/PathwayMech
title: Initial integration review of shikimate degradation II
started_at: '2026-10-14T20:23:04Z'
finished_at: '2026-10-14T20:57:48Z'
reviewer:
  identity: codex /root/next258_integration
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Did not author the maintained pathway, adapter implementation,
    authority snapshots or biological evidence. Wrote independent read-only audits
    and review artifacts; a separate delegated reviewer verified artifact retention.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: false
summary: 'Independent integration and provenance checks pass, including exact baseline
  preservation, full authority rebuilds, typed gene gates, evidence retention and
  SVG/KGX fidelity. All initial repository gates passed. Two minor reference-display
  defects require bounded YAML corrections. Scientific interpretation, including separately
  tracked downstream category issue #549, is not reassessed here.'
source:
  git_revision: 495de27ec09f99367d1cdd5c457a5e54a93c9a0b
  state: working_tree
  inputs:
  - path: .claude/skills/add-pathway/SKILL.md
    sha256: f0d394f29cad1a1cd6a004abceb5f59f8e567d6b885cd6c4ff07c629c4d6db7a
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: CLAUDE.md
    sha256: c067d99547f9e9e9a6edb892d71126b6765239348d0021b907f3102907a4cf00
    role: context
  - path: conf/identifier_policy.yaml
    sha256: f57137cbec6ee2ffb4abc1c2e448dd93766e37edac9b07c43cab24c5809d27f7
    role: context
  - path: conf/identifier_sources.json
    sha256: 37a280d8bcdfbdb79485b14c69ecbe8c8238d89e6be494143c402105ea97e877
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: f6ea2aeabd0736e70448e01d19080080317e4a24a6dd6c660f1e857b7d76ef87
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 8fb26d7ec0ff199d64ccada289ac7cd84ecfddc1ffb1d90c273cbef9aabe488c
    role: context
  - path: data/pathways/shikimate-degradation-ii.yaml
    sha256: 3c3e9665a0c3cab33572fd12fc419bbbb46d0e8d3232da046e7aaaaf75290303
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 4f3f46d1f4b8ebafa9b2d04d9700510df18b6ec6f881856fda521879f494d153
    role: context
  - path: docs/CURATION.md
    sha256: 408f7c7705b4e6d667b513920e4c39612162d549e0c2666d85bfd53b2c2687f7
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 072884773d626ea909bd1e4f275901f0a6053f660d5e68a294ee54149b6496b0
    role: context
  - path: docs/IDENTIFIERS.md
    sha256: bef68ac2a8e6f5c08d563b6d969ff040e1099a170dd568c4e436a20c4034b25d
    role: context
  - path: docs/record-review-profile.md
    sha256: f3f00eebb7841e9d5ac891271e269f45e926995e16856b8e9a885436570c7819
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: pages/downloads/edges.tsv
    sha256: f4af8087cba179d3169c69a71467038d67b6e791a7ed520f5f4241ddc7334f36
    role: context
  - path: pages/downloads/nodes.tsv
    sha256: d7aebe7547e0fbd5324ddb62677c016dee9a606be7fca484450c34a8a2937e9b
    role: context
  - path: pages/records/MetaCyc_PWY-6419.html
    sha256: a4ef65564777e23325ef19be1cdae061ca18f7013d71d657830b0cada28d9f5e
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/README.md
    sha256: a5d7c3f355f0a4453ab75107d490d040bf6673fcdfda2fe428637bf5a9fb0b79
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/assembly/assembled-record.json
    sha256: 389a5dc0d34b3179a3266b494dfe5acea263d4ad15ef085cd01094e392ebc397
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/authorities/canonical-build-commands.json
    sha256: 99ea1c22db99054fb6c564c52b00b04f32c526c2b0fcf777090da1149372e0dc
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/authorities/preservation-and-promotion.json
    sha256: 47bff752768c7cc130deb5ba160e50c0bca09f5090cce20f00728eba0836ac41
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/authorities/snapshot-bindings.json
    sha256: d05b1e0de4c74d2d5c6710b3c290dd32254d56c2994dc26bec1a6cea1ddd4d6d
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/code-review/initial/adversarial-results.json
    sha256: 55e3c18db21818f16ab7f52f0b6561ee73b1ffa865048cbabdf760a9c9288298
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/code-review/initial/artifact-manifest.json
    sha256: 337f4ebb8aece6bb2aecc8c94a0677d2c9dc74b326d80f5ab3bfe21563da005d
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/code-review/initial/input-bindings.json
    sha256: dfdc19c3ec13a7b8ad4fda04ab7e54c07e511e8bac435fe301f8be8b7a144b79
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/code-review/initial/regression-receipt.json
    sha256: 4c06ff5b98c1be531c45f3f975887d4851c9dd8cdcf5c85256ceb93af92d473d
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/code-review/initial/regression.log.txt
    sha256: fcd4dd80dfa2e01a47835d549e29ae612c88b95797028cfe26c962ac73949ec6
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/code-review/initial/retention.json
    sha256: 20564fc8293c462412e42e6939589a5679f78b9cd00b3c236543a7beeff605bf
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/identifier-inventory.json
    sha256: 7af32fe1a55368d7a730d707bff205213372be5877667a4154818820415f8f65
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/artifact-manifest.json
    sha256: 872f54b85d5c8747fc2dd5e4767a66faf584fe281f3b61e5a1027a79d8f70b7f
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/attempt-typed-probe-missing-collections/receipt.json
    sha256: 9dea983ae8c361e4eb157fadb3b70e840029b36d94b15a8148afbef7b650f6be
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/baseline-audit-results.json
    sha256: d1896e6269b4f2381191c0f0035eb71fae29d4c8886982e8d1803ba2e770c852
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/baseline-record-comparison.json
    sha256: cfb1c66c3e6d09ab49e834842419fef816d617e267bc4690cbde039bf1b3130d
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/code-review-verification.json
    sha256: fdcc586135b1973d8dec54b3858ab64cf2a0d4746229e6406bc22787ba8609e1
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/complete-original-cache-check.json
    sha256: 934b3a443a615de5a92986d4eee39b6a0502cb3ffbcbf994fad424468b76a2dd
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/consumer-replay-results.json
    sha256: b9c1f4e137a8cc0cbca9144f2613af5c87c2c184a9d016d2963f2b2fb106b0da
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/consumer-wrapper-failure.json
    sha256: fc0848e3cde993f809f622e3d63f8676bec4194a97cfdfee52e2084a4947eced
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/graph-export-results.json
    sha256: c7c3e5555da4e6121ec01d8cf5eb6ec7f5373334af32408cbac375cf49ceecc0
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/input-bindings.json
    sha256: a82bdcea6057fec90eec40e01862dfee6c964649702178c991b034841ad55e82
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/ontology_builder-replay-receipt.json
    sha256: 8bf3844e49d4188da2625c637b6a1bff9be12843fd6cc98698a0278b8404f057
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/reference-display-findings.json
    sha256: 12f677ee9a31038c7e359ee766d6f0e39e4308327654a1d5869997d08766f632
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/reference-original-bindings.json
    sha256: 1dbe39705b16adc936347449e101f5f99d3c3ad69dd0238c3395a96198d909f8
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/retention.json
    sha256: 97897af31c759b9bf9d6999ca748381eb340e746f9cda9e462054554bae59da5
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/retention/execution-receipt.json
    sha256: 8f146cdde45b10556b329691a978091e8a435ecbe305cd9ac4b7d3d75c1f75d9
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/retention/input-hashes.json
    sha256: ca099d31c7f7901d540c630d1d71128707c8e1b5cb7e74ec629cbbb0fb256342
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/retention/results.json
    sha256: 14f2a5d9755d802b594026cfc1dd3d9e7dfee6bfc70c731dec6f6177016ae75a
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/science-retention-audit-retention.json
    sha256: fa27efed4ce89a5b618a7fd69c065b7d7b12f05aece0964c7208744af187f984
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/science-retention-audit.json
    sha256: a63025a16bee500df46bf86ed59f30226a710c47a469fa3546838a8bc665819f
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/science-retention-audit.py.txt
    sha256: bafe19cdcb5b72f0486800d7faeb67547c6324f6a28950fe87e7671f71c76963
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/source_builder-replay-receipt.json
    sha256: 9cf256289cbb429edbd211cc1e6d177cad86e88d32df3217471c3aeadcc649b1
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/typed-integration-results.json
    sha256: 0716c29339b8952787a76eac7034b513314cc7117b23b4398e1df91be30b3d40
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/union-audit-input-bindings.json
    sha256: e851ef6aab79b5a1668c41aa64110d03a890643518c173bfa5952b559f2774d3
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/union-audit-results.json
    sha256: d770f68aae5414de5882b2a1902bd8d937228c99b247276450daf732efd5b510
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/science/initial/retained-inspection-binding.json
    sha256: a774032a8b37a7e47ba84eba3c0abfd72fb7d7f9db691a95e0d91cca5f5657ce
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/science/initial/retention-manifest.json
    sha256: 3d528cc8c52b7a714eb7bfa9d51fbc0fa27c6d2823945b9d9de3959fb0cf4160
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/environment.json
    sha256: e737891d875e2165af3709c583bb30c5cd1b920b4c919173d85c3905eedc6349
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/failed-attempts.json
    sha256: 26304443888d32c44bcb133f01b76d29455a78614ef4107259b33e1fc5a94fee
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/final-input-preservation.json
    sha256: 9e65703a9a8eca09c0b6c83a6f5cd72acf2157124e219b2d21057fc188463bd8
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/git-diff-check.log.json
    sha256: abd85a4bdac87f1685fab06231e738ae771dca8a4fb489605678aa21f3680c40
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/initial-attempt-receipts.json
    sha256: 6147d32892e5763cdcc7183aa703c1aa0ee094411bfb51e7a4b6b4d63d138d8a
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/just-lint.log.json
    sha256: d09696fe24e852805c00a035d0f1055926c6da1c117273a4b19156415c8dd0f4
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/just-render-pages.log.json
    sha256: 7a548079737e3a44729963c4bcc21819a91b2ad9d0ad5ecf34631015db167ebb
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/just-test.log.json
    sha256: acc14883cdf9b63ea507f34babf6eac8beae1ea1165a5365cea5ea41b4a8dfd2
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/just-validate.log.json
    sha256: e41b4d8c5209468ce86923566168c607d55c651bc8c7b12561bc01ad1da4be34
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/just-vendored-check-network-retry.log.json
    sha256: ccdd3c8f5f64bc97bc7a06d2f051fcedf77234d2401bea727c141e35fd8cb3d3
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/just-vendored-check.log.json
    sha256: a5994b8deaf7e0865adf8c1976d8a2adfbb6a8ba2a9bcb1fb59cb94dd9a0d0bd
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/receipts.json
    sha256: 258c0c52ce96a287f08a7e2d8f9e2d806e9c45ffaa90613639b82ac768caa081
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/resume_after_fetch_failure.py.txt
    sha256: 93ea65564aa088b8a5104ed4558074163f24661a6495feee8e9bd3f7b71c778a
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/resumed-attempt-receipts.json
    sha256: 258c0c52ce96a287f08a7e2d8f9e2d806e9c45ffaa90613639b82ac768caa081
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/retention.json
    sha256: 97367294f96b9b6370c137c39d12ab67890b8701229a389126f0cc4273c67c9b
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/run_checks.py.txt
    sha256: 978b443ac337845582dfbda7eac047e9769a2dce8a58c05c3764465a3ab5f015
    role: context
  - path: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/tested-core-input-hashes.json
    sha256: f869a06bcc032b7370b4c4364f6852e61234a99c72fb796a6b96c5af91d4eee2
    role: context
  - path: scripts/build_ontology_identifier_snapshot.py
    sha256: fc8bee76c1c07c4d3b86eb72021f8eaf8203ae339258ff16768dd3e1f1b2be81
    role: context
  - path: scripts/build_source_identifier_snapshot.py
    sha256: 5b9d72448d9c6b798f4a054a5119c3cc8f000c693c4b26cf6d01e29100e959dd
    role: context
  - path: src/pathwaymech/graph_view.py
    sha256: 45bbedd4459f21d4189e3eeb35504ff71ba664e975f4cdde7250a61e9ae3215b
    role: context
  - path: src/pathwaymech/identifiers.py
    sha256: d1a014fa77c4f1affd82ce999f98334493e0363dd250fd546f34e5fa26253165
    role: context
  - path: src/pathwaymech/kegg_gene.py
    sha256: cd55029144f0ed438ca026a607423956d21dae5ccc28b34b13523f68e6d1ec1d
    role: context
  - path: src/pathwaymech/kgx.py
    sha256: 4419ba74ee3949ac84a1ca1bb3cde3bf3ce73a5c975ebeab81ec1ef09dcdf3f9
    role: context
  - path: src/pathwaymech/schema.py
    sha256: bd99c1e6ca1f6eec5c82c58aa1ae3f43f696d30be66fbe0977dcace81292e0b8
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: c66be7d0ae830e5041608eb6b2ce9755c601ed596ec9df5fb3567d41b202478b
    role: context
  - path: tests/test_kegg_gene_authority.py
    sha256: b9def406bb9b54215b0fcd8acce06907449e4e660450e76bd5c9cb3902025a04
    role: context
scope:
  description: One-record provenance, authority, typed identifier and generated-export
    integration audit. This is not a literature/scientific review.
  selection: Exact new maintained record MetaCyc:PWY-6419 and its frozen initial author
    integration.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-6419
  exclusions:
  - target: Biological mechanisms, literature support and downstream pathway category
    reason: 'Separately assessed by independent scientific reviewer; known issue #549
      is neither duplicated nor retired by this technical review.'
  - target: Older source-version presentation defects across the corpus
    reason: 'Only this new record is assessed; broader issues #522 and #523 remain
      separate.'
targets:
- target_id: MetaCyc:PWY-6419
  path: data/pathways/shikimate-degradation-ii.yaml
  label: shikimate degradation II
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/shikimate-degradation-ii.yaml
    role: maintained mechanism record and reference display strings
checks:
- check_id: baseline-and-cache
  name: Independent Git baseline and complete-original cache comparison
  status: passed
  required: true
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-258-integration/initial/audit_baseline.py
  exit_code: 0
  summary: All 254 baseline records, authority objects and original source digests
    preserved.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - baseline
  - cache
- check_id: union
  name: Independent authority promotion and selection comparison
  status: passed
  required: true
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-258-integration/initial/audit_union.py
  exit_code: 0
  summary: Seven exact planned additions, six exact new owners; no policy/schema/governed
    drift.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - union
  - baseline
- check_id: source_builder
  name: Independent canonical source builder
  status: passed
  required: true
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B scripts/build_source_identifier_snapshot.py
    --manifest /private/tmp/pathwaymech-next-258-authorities/identifier_sources.json
    --cache-dir /private/tmp/pathwaymech-next-258-authorities/originals --records
    /private/tmp/pathwaymech-next-258-authorities/records --output /private/tmp/pathwaymech-next-258-integration/initial/source_builder-reproduced.json
  exit_code: 0
  summary: Builder exited zero; reproduced full output is byte-identical to promoted
    snapshot. The enclosing reviewer summary later failed; builder receipts remain
    successful.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - union
  - source-replay
  - wrapper-failure
- check_id: ontology_builder
  name: Independent canonical ontology builder
  status: passed
  required: true
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B scripts/build_ontology_identifier_snapshot.py
    --source GO=/private/tmp/pathwaymech-curation-authorities/go.db --source CHEBI=/private/tmp/pathwaymech-curation-authorities/chebi.db
    --source NCBITaxon=/private/tmp/pathwaymech-curation-authorities/ncbitaxon.db
    --source RHEA=/private/tmp/pathwaymech-curation-authorities/rhea.db --rhea-updates
    /private/tmp/pathwaymech-next-258-authorities/baseline/rhea_identifier_updates.json
    --cache-dir /private/tmp/pathwaymech-next-258-authorities/originals --corpus /private/tmp/pathwaymech-next-258-authorities/records
    --include-id GO:0008150 --include-id GO:0006096 --include-id GO:0005975 --output
    /private/tmp/pathwaymech-next-258-integration/initial/ontology_builder-reproduced.json
  exit_code: 0
  summary: Builder exited zero; reproduced full output is byte-identical to promoted
    snapshot. The enclosing reviewer summary later failed; builder receipts remain
    successful.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - union
  - ontology-replay
  - wrapper-failure
- check_id: consumer
  name: Independent consumer replay
  status: passed
  required: true
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-258-integration/initial/replay_consumer.py
  exit_code: 0
  summary: Both reconstructed complete authority snapshots accepted.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - consumer
- check_id: typed-consumer
  name: Actual gene identity/category/label probes
  status: passed
  required: true
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-258-integration/initial/check_typed_integration.py
  exit_code: 0
  summary: 13 actual-source acceptance/rejection cases passed after documented fixture
    repair.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - typed
  - probe-failure
- check_id: graph-exports
  name: SVG and KGX fidelity inspection
  status: passed
  required: true
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-258-integration/initial/check_graph_exports.py
  exit_code: 0
  summary: 32 edges, nine qualified endpoints and 30 node contexts preserved exactly.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - exports
- check_id: just-render-pages
  name: just render-pages
  status: passed
  required: true
  command: just render-pages
  exit_code: 0
  summary: Completed with exit code 0; exact retained log inspected. Root executed;
    reviewer independently checked captured log digest and relevant input hashes.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - gates
  - tested-inputs
- check_id: just-validate
  name: just validate
  status: passed
  required: true
  command: just validate
  exit_code: 0
  summary: 'history links: 447 record(s), 0 invalid; 447 history record(s) valid against
    src/pathwaymech/schema/history.yaml; validated 255 pathway records; validated
    255 records against the closed LinkML schema; validated 30 source records Root
    executed; reviewer independently checked captured log digest and relevant input
    hashes.'
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - gates
  - tested-inputs
- check_id: just-test
  name: just test
  status: passed
  required: true
  command: just test
  exit_code: 0
  summary: =========== 5118 passed, 3 skipped, 7 warnings in 1443.06s (0:24:03) ===========
    Root executed; reviewer independently checked captured log digest and relevant
    input hashes.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - gates
  - tested-inputs
- check_id: just-lint
  name: just lint
  status: passed
  required: true
  command: just lint
  exit_code: 0
  summary: All checks passed! Root executed; reviewer independently checked captured
    log digest and relevant input hashes.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - gates
  - tested-inputs
- check_id: just-vendored-check
  name: just vendored-check
  status: passed
  required: true
  command: just vendored-check
  exit_code: 0
  summary: Completed with exit code 0; exact retained log inspected. Root executed;
    reviewer independently checked captured log digest and relevant input hashes.
    This is the successful scoped retry after the preserved initial DNS failure.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - gates
  - tested-inputs
  - gate-retry
  - gate-original
  - gate-original-log
- check_id: git-diff-check
  name: git diff --check
  status: passed
  required: true
  command: git diff --check
  exit_code: 0
  summary: Completed with exit code 0; exact retained log inspected. Root executed;
    reviewer independently checked captured log digest and relevant input hashes.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - gates
  - tested-inputs
evidence:
- evidence_id: target
  kind: record_content
  reference: data/pathways/shikimate-degradation-ii.yaml
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: 'Full initial maintained record: 30 named IDs, 32 mechanistic edges, nine
    qualified endpoints and 31 references.'
  snapshot_sha256: 3c3e9665a0c3cab33572fd12fc419bbbb46d0e8d3232da046e7aaaaf75290303
- evidence_id: baseline
  kind: authority
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/baseline-audit-results.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Independently compared all 254 baseline YAMLs with Git and staged copies,
    all 4,947 authority terms and 865 source-owner objects, 1,041-entry manifest prefix,
    governed files, schema and identifier policy.
  snapshot_sha256: d1896e6269b4f2381191c0f0035eb71fae29d4c8886982e8d1803ba2e770c852
- evidence_id: cache
  kind: authority
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/complete-original-cache-check.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Independent streaming SHA-256 verification of all 1,062 recursive source
    descriptors across 1,046 paths, including companion source objects.
  snapshot_sha256: 934b3a443a615de5a92986d4eee39b6a0502cb3ffbcbf994fad424468b76a2dd
- evidence_id: union
  kind: authority
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/union-audit-results.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Exactly seven planned identifiers and six source owners added; promoted
    bytes match union outputs and the maintained record equals the frozen assembled
    draft.
  snapshot_sha256: d770f68aae5414de5882b2a1902bd8d937228c99b247276450daf732efd5b510
- evidence_id: source-replay
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/source_builder-replay-receipt.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Independent canonical source builder exited zero and reproduced the promoted
    source snapshot byte for byte.
  snapshot_sha256: 9cf256289cbb429edbd211cc1e6d177cad86e88d32df3217471c3aeadcc649b1
- evidence_id: ontology-replay
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/ontology_builder-replay-receipt.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Independent canonical ontology builder exited zero and reproduced the promoted
    ontology snapshot byte for byte.
  snapshot_sha256: 8bf3844e49d4188da2625c637b6a1bff9be12843fd6cc98698a0278b8404f057
- evidence_id: consumer
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/consumer-replay-results.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: 'Canonical consumer accepts both independently reconstructed snapshots:
    2,863 source terms/866 owners and 2,091 ontology terms/five owners.'
  snapshot_sha256: b9c1f4e137a8cc0cbca9144f2613af5c87c2c184a9d016d2963f2b2fb106b0da
- evidence_id: typed
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/typed-integration-results.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Thirteen reviewer-executed file-based cases using the three actual KEGG
    gene owners preserve locus labels and reject aliases, incorrect categories/sections
    and contextual-label waivers.
  snapshot_sha256: 0716c29339b8952787a76eac7034b513314cc7117b23b4398e1df91be30b3d40
- evidence_id: code-review
  kind: prior_review
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/code-review-verification.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Independently inspected the separate code reviewer’s 11 frozen artifacts,
    five unchanged implementation/test/doc inputs, 432-test regression receipt, 60
    adversarial outcomes and four complete original CDS responses. These are the separate
    reviewer’s executions.
  snapshot_sha256: fdcc586135b1973d8dec54b3858ab64cf2a0d4746229e6406bc22787ba8609e1
- evidence_id: retention
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/retention/results.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Delegated independent provenance audit verifies 187 mappings, 23 explicit
    external bindings, 385 raw-source ledger entries and seven original package manifests;
    15 failure-evidence items preserved. Inventories include hidden and ignored files.
  snapshot_sha256: 14f2a5d9755d802b594026cfc1dd3d9e7dfee6bfc70c731dec6f6177016ae75a
- evidence_id: science-retention
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/science-retention-audit.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Independent provenance-only follow-up verifies all 18 scientific-review
    artifact mappings, exact recovery of the 27,961-byte transcript wrapper, all 13
    external manifest artifacts and 36 shared-inspection input hashes; 116 checks
    passed. Scientific conclusions are not reassessed.
  snapshot_sha256: a63025a16bee500df46bf86ed59f30226a710c47a469fa3546838a8bc665819f
- evidence_id: references
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/reference-original-bindings.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: All 31 maintained reference source digests match independently hashed originals,
    including the complete GO SQL database. This verifies byte identity, not scientific
    support.
  snapshot_sha256: 1dbe39705b16adc936347449e101f5f99d3c3ad69dd0238c3395a96198d909f8
- evidence_id: exports
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/graph-export-results.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Parsed generated SVG/KGX preserve all 32 edges, all nine qualified endpoints,
    complete evidence/reference payloads and all 30 per-record node contexts.
  snapshot_sha256: c7c3e5555da4e6121ec01d8cf5eb6ec7f5373334af32408cbac375cf49ceecc0
- evidence_id: display
  kind: record_content
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/reference-display-findings.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: refutes
  summary: Direct YAML-to-rendered-reference comparison demonstrates joined words/date-number
    tokens and one serialized UniProt entryAudit JSON source-version value.
  snapshot_sha256: 12f677ee9a31038c7e359ee766d6f0e39e4308327654a1d5869997d08766f632
- evidence_id: policy
  kind: authority
  reference: conf/identifier_policy.yaml
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Existing canonical and contextual label policy is unchanged; typed native
    genes require canonical locus labels and gene placement.
  snapshot_sha256: f57137cbec6ee2ffb4abc1c2e448dd93766e37edac9b07c43cab24c5809d27f7
- evidence_id: wrapper-failure
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/consumer-wrapper-failure.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: context_only
  summary: Preserved reviewer wrapper failure after both successful builder runs;
    the return-shape summary error was corrected by a separate consumer-only replay.
  snapshot_sha256: fc0848e3cde993f809f622e3d63f8676bec4194a97cfdfee52e2084a4947eced
- evidence_id: probe-failure
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/integration/initial/attempt-typed-probe-missing-collections/receipt.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: context_only
  summary: Preserved reviewer fixture omission rejected before typed semantics were
    reached; corrected fixture replay passes all 13 cases.
  snapshot_sha256: 9dea983ae8c361e4eb157fadb3b70e840029b36d94b15a8148afbef7b650f6be
- evidence_id: gates
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/receipts.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Root executed all six initial repository gates against the same unchanged
    core input hashes; this reviewer inspected exact receipts and decoded retained
    logs.
  snapshot_sha256: 258c0c52ce96a287f08a7e2d8f9e2d806e9c45ffaa90613639b82ac768caa081
- evidence_id: gate-retry
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/failed-attempts.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: context_only
  summary: The first vendored-check attempt failed DNS resolution. Its exact initial
    receipt and original log remain retained; only the same network command was retried
    successfully before the remaining whitespace check. The four prior successes were
    preserved and core inputs did not change.
  snapshot_sha256: 26304443888d32c44bcb133f01b76d29455a78614ef4107259b33e1fc5a94fee
- evidence_id: gate-original
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/initial-attempt-receipts.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: context_only
  summary: Original five-command receipt sequence retains four successful checks and
    the failed vendored fetch; it is not replaced by the effective final success sequence.
  snapshot_sha256: 6147d32892e5763cdcc7183aa703c1aa0ee094411bfb51e7a4b6b4d63d138d8a
- evidence_id: gate-original-log
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/just-vendored-check.log.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: context_only
  summary: Lossless wrapper of the original 378-byte vendored-check failure log explicitly
    records DNS resolution failure for raw.githubusercontent.com.
  snapshot_sha256: a5994b8deaf7e0865adf8c1976d8a2adfbb6a8ba2a9bcb1fb59cb94dd9a0d0bd
- evidence_id: tested-inputs
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-258/shikimate-ii/validation/initial/tested-core-input-hashes.json
  accessed_at: '2026-10-14T20:57:48Z'
  support: supports
  summary: Root gate input hashes bind the maintained record, implementation, authorities,
    schema and generated artifacts; intersecting review inputs were independently
    compared.
  snapshot_sha256: f869a06bcc032b7370b4c4364f6852e61234a99c72fb796a6b96c5af91d4eee2
assessments:
- assessment_id: preservation
  area: provenance
  topic: Baseline, authority selection and original sources
  outcome: supported
  summary: All 254 pre-existing pathway YAMLs, all 4,947 authority terms/865 source
    owners and the 1,041-entry manifest prefix are unchanged. The only authority additions
    are the seven planned IDs backed by six new complete source entries and the pinned
    Rhea source.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - baseline
  - cache
  - union
  - references
- assessment_id: reproduction
  area: consistency
  topic: Canonical builder and consumer reproducibility
  outcome: supported
  summary: Independent full source and ontology builds reproduce the promoted snapshot
    bytes, and both canonical consumers accept the reconstructed data. The corpus
    selector supplies IDs only; issuing originals supply labels.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - source-replay
  - ontology-replay
  - consumer
  - union
- assessment_id: typed-identity
  area: grounding
  topic: Native gene label/category enforcement
  outcome: supported
  summary: Actual selected KEGG genes resolve to their complete typed native owners.
    Canonical locus labels and participant/gene placement remain enforced before contextual
    exceptions. The five code-review input files remain unchanged.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - typed
  - code-review
  - policy
- assessment_id: retained-evidence
  area: provenance
  topic: Exact evidence retention and failure accounting
  outcome: supported
  summary: All 187 author-artifact mappings and source-ledger bindings are byte-verified.
    The separate scientific-review package also preserves all 18 mapped artifacts,
    its transcript wrapper and 36 inspected input hashes. Initial author failures
    and two reviewer harness failures remain explicit; corrected execution does not
    rewrite earlier evidence.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - retention
  - science-retention
  - references
  - wrapper-failure
  - probe-failure
- assessment_id: exports
  area: graph
  topic: Claim-payload fidelity in generated SVG and KGX
  outcome: supported
  summary: All 32 edges, nine qualified endpoints and 30 local node contexts survive
    export with complete evidence and reference metadata. This does not certify biological
    category choices or source interpretation.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - target
  - exports
- assessment_id: gate-assessment
  area: schema
  topic: Initial full-corpus repository gates
  outcome: supported
  summary: All six effective initial gates passed on the unchanged reviewed core input
    bytes. The first vendored-check failed DNS resolution; its failure is retained
    and the same command passed on a scoped network retry. Four prior successes were
    preserved, followed by the remaining whitespace check. Deterministic validity
    is separate from scientific approval.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - gates
  - tested-inputs
  - gate-retry
  - gate-original
  - gate-original-log
- assessment_id: presentation
  area: representation
  topic: Human-readable reference source versions
  outcome: concern
  summary: Five reference entries contain joined words/date-number tokens, and one
    additional UniProt reference displays serialized entryAudit JSON. The generated
    page faithfully repeats these maintained strings; the fixes belong to the YAML
    reference metadata.
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - display
  - target
findings:
- category: representation
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - display
  - target
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/shikimate-degradation-ii.yaml
    role: maintained reference source_version display strings
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/550
  finding_id: F1
  issue_key: shikimate-ii-reference-source-version-spacing
  title: Reference source versions concatenate words with dates and numbers
  description: 'The rendered references reproduce retrieved2026-10-14 in PMID19376919,
    PMID24674055 and PMID32822353, Table1 twice in PMID23929881, and returned403 in
    PMID25406451. Normalize spacing and readable wording in maintained source_version
    strings while preserving retrieval dates, artifact digests and access limitations.
    This is a confirmed new-record recurrence related to broad issue #522; the scoped
    fix does not close that older corpus-wide issue.'
  field_paths:
  - references[24].source_version
  - references[25].source_version
  - references[26].source_version
  - references[27].source_version
  - references[29].source_version
  native_severity: minor
  normalization_reason: Bounded reader-facing provenance formatting defect; identifiers,
    hashes and mechanism assertions remain intact.
- category: representation
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - MetaCyc:PWY-6419
  evidence_ids:
  - display
  - target
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/shikimate-degradation-ii.yaml
    role: maintained reference source_version display strings
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/550
  finding_id: F2
  issue_key: shikimate-ii-uniprot-source-version-json
  title: ShiR reference displays serialized UniProt audit JSON as a version
  description: 'Exactly one new-record reference, UniProtKB:A4QH19, renders its entire
    serialized entryAudit mapping under source version at page #reference-31. Replace
    the display string with readable entry/version/date text grounded in the same
    complete original; retain its source_sha256 and the complete JSON in raw evidence.
    A4QH18 already uses readable text. This bounded recurrence is related to broad
    issue #523 and does not establish that older records are fixed.'
  field_paths:
  - references[30].source_version
  native_severity: minor
  normalization_reason: A bounded reference-display problem, not an identifier authority
    or source-integrity defect.
actions:
- action_id: correct-reference-display
  description: 'Normalize the six affected reference source-version fields, preserving
    exact evidence scope and source digests; regenerate Pages and rerun required gates.
    Leave older broad issues #522/#523 open unless independently resolved.'
  finding_ids:
  - F1
  - F2
  target_ids:
  - MetaCyc:PWY-6419
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/shikimate-degradation-ii.yaml
    role: maintained reference source_version display strings
  acceptance_checks:
  - No source_sha256, identifier, URL, access limitation or mechanistic edge changes
    from this presentation correction.
  - 'Inspect generated references #25, #26, #27, #28, #30 and #31 for readable date/version
    wording.'
  - just render-pages; just validate; just test; just lint; git diff --check
  generator: pathwaymech.cli:render_pages_main through just render-pages
limitations:
- This provenance-only review does not reassess scientific claim support, sequence
  translation, organism/genome crosswalk biology, full-source exhaustiveness or licensing
  clearance.
- The separate code reviewer executed the cited 432-test regression and 60-case adversarial
  suite; this reviewer inspected their exact artifacts and executed the additional
  13 actual-source consumer cases.
- Full original caches and reproduced trial snapshots remain external under /private/tmp
  and hash-bound. Local reproducibility was demonstrated; long-term external-cache
  durability is not established.
- Generated output checks parsed HTML/SVG/KGX payloads and anchors, rather than performing
  a browser screenshot layout audit.
- The input state is an inspected working tree. A later exact-commit review is required
  after corrections, saved review bundles and final gates.
- Two reviewer harness mistakes are preserved and corrected; neither canonical builder
  failed.
tags:
- integration
- provenance
- shikimate-degradation-ii
- initial-review
```

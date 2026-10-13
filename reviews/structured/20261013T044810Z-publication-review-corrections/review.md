# Resolve cumulative publication review findings

- Review: 20261013T044810Z-publication-review-corrections
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-13T04:18:25Z
- Finished UTC: 2026-10-13T04:48:10Z
- Reviewer: Codex /root (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Three confirmed cumulative-review defects are corrected and verified: typed-owner downgrade/conflict validation, SSSOM prefix completeness and one Rhea source-direction scalar. Original reviews remain immutable. The review does not renew full scientific approval.

## Scope And Provenance

Bounded review of three corrected maintained owners and their generated consequences.

Selection: Three confirmed findings from cumulative review of public base e1c66917e753105c4bf5b7b026193fcefa2b000f through local 70903536191206d2586cd23e46f7d70c32fef92e.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 70903536191206d2586cd23e46f7d70c32fef92e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| authority | src/pathwaymech/identifiers.py | maintained | Typed authority consumer |
| sssom | src/pathwaymech/sssom.py | maintained | SSSOM export prefix contract |
| aceto | data/pathways/acetoacetate-degradation.yaml | maintained | Acetoacetate RHEA:21038 source orientation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| tests | passed | True | authority, sssom, aceto | Final execution passed; complete stdout/stderr accompany the receipt. |
| validate | passed | True | authority, sssom, aceto | Final execution passed; complete stdout/stderr accompany the receipt. |
| lint | passed | True | authority, sssom, aceto | Final execution passed; complete stdout/stderr accompany the receipt. |
| skills | passed | True | authority, sssom, aceto | Final execution passed; complete stdout/stderr accompany the receipt. |
| vendored-network | passed | True | authority, sssom, aceto | Final execution passed; complete stdout/stderr accompany the receipt. |
| diff-check | passed | True | authority, sssom, aceto | Final execution passed; complete stdout/stderr accompany the receipt. |
| Exact generated artifact and maintained record preservation | passed | True | sssom, aceto | All edges and mapping rows preserved; exact one-scalar record correction and intended generated direction/provenance changes. |

## Scientific And Domain Assessments

### Issue504 complete typed source registry

identity: supported. Targets: authority.

Retained native identities cannot be downgraded by selecting a legacy source. Complete conflicting projections, counterparts, polymer members and kind collisions are rejected before dispatch; identical compatible owners and current corpus terms remain valid.

### Issue505 declared SSSOM namespaces

representation: supported. Targets: sssom.

All 70 mapping rows are preserved. EcoCyc/MetaCyc native frame namespaces and explicitly project-scoped PathBank identifiers expand correctly; undeclared prefixes cannot overwrite a valid export.

### Issue506 RHEA21038 source orientation

graph: supported. Targets: aceto.

Source orientation is right_to_left because the directed reaction consumes master side R and produces side L. Only this scalar changes; the printed equation and all 46 mechanistic edges retain their previous exact content.

This corrects scientific review 20261012T210220Z-aceto236-scientific identity-18/reference-13 and technical review 20261012T210222Z-aceto236-technical kgx-and-sssom insofar as they accepted this direction discrepancy. The prior reviews contain no native finding identity for it, so no fabricated resolved-finding lineage is created. Earlier literature and other scientific claims are outside this bounded reassessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| typed-review | research/publication_review/2026-10-13/runtime-crossreview.md; Complete retained report or execution receipt | supports | Independent reviewer compared complete owner registration and producer parity; 87 dedicated tests pass, valid corpus authority remains unchanged. |
| mapping-review | research/publication_review/2026-10-13/sssom-crossreview.md; Complete retained report or execution receipt | supports | Independent SSSOM review and consumer tests verify declared native/scoped prefixes and reject unknown prefixes before output replacement. |
| rhea | research/publication_review/2026-10-13/rhea-direction-selected-replay.json; Complete retained report or execution receipt | supports | Six complete issuing Rhea object projections were independently matched to all fragments in the SHA-256-verified release142 original. 21038 substrates are 21036_R, products 21036_L. |
| direction-review | research/publication_review/2026-10-13/rhea-direction-review.md; Complete retained report or execution receipt | supports | Independent adjudication documents the one-scalar correction and precisely bounds the earlier aceto review interpretation it supersedes. |
| artifact-check | research/publication_review/2026-10-13/artifact-preservation.json; Complete retained report or execution receipt | supports | Complete before/after artifact comparison verifies exact chemistry, edge and mapping preservation while source direction and generated provenance are updated. |
| prior-interpretation | research/publication_review/2026-10-13/prior-review-interpretation.md; Complete retained report or execution receipt | supports | Full paired prior reviews were read and their immutable YAML/Markdown identity checked; neither contains finding IDs. Exact direction acceptance is corrected without renewing other scientific judgments. |
| prior-dispositions | research/publication_review/2026-10-13/earlier-issue-dispositions.md; Complete retained report or execution receipt | supports | Read-only reassessment verifies thirteen earlier issue fixes from current code, complete historical execution and acceptance evidence. |
| gate-tests | research/publication_review/2026-10-13/gates/tests.json; Complete retained report or execution receipt | supports | Actual command, timestamps, exit code and companion full stdout/stderr retained. |
| gate-validate | research/publication_review/2026-10-13/gates/validate.json; Complete retained report or execution receipt | supports | Actual command, timestamps, exit code and companion full stdout/stderr retained. |
| gate-lint | research/publication_review/2026-10-13/gates/lint.json; Complete retained report or execution receipt | supports | Actual command, timestamps, exit code and companion full stdout/stderr retained. |
| gate-skills | research/publication_review/2026-10-13/gates/skills.json; Complete retained report or execution receipt | supports | Actual command, timestamps, exit code and companion full stdout/stderr retained. |
| gate-vendored-network | research/publication_review/2026-10-13/gates/vendored-network.json; Complete retained report or execution receipt | supports | Actual command, timestamps, exit code and companion full stdout/stderr retained. |
| gate-diff-check | research/publication_review/2026-10-13/gates/diff-check.json; Complete retained report or execution receipt | supports | Actual command, timestamps, exit code and companion full stdout/stderr retained. |

## Limits And Additional Notes

- Scientific_review is false: this is a bounded correction/disposition, not a new complete literature review of acetoacetate or the nine new records.
- Prior source access and assay/strain limits remain. Previously observed dense graph junction overlaps and long construct-label truncation remain documented; complete evidence stays in tables. No interactive, responsive or dark-theme check is claimed.
- Initial vendored check failed sandbox DNS; its retained failed receipt is followed by a successful read-only network-enabled execution.
- The original nine-commit payload audit is pinned to 7090353; final small correction-delta audit is separate. Source license/release labels remain deferred.
- The GitHub issues had no structured native finding predecessors. Verified fixes are recorded as assessments and external issue links, not invented terminal finding lineages.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T044810Z-publication-review-corrections
kind: repository
repository: CultureBotAI/PathwayMech
title: Resolve cumulative publication review findings
started_at: '2026-10-13T04:18:25Z'
finished_at: '2026-10-13T04:48:10Z'
reviewer:
  identity: Codex /root
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Root coordinated fixes, history, generation and final checks.
    Separate independent runtime and record/export reviewers found the defects; each
    code fix received a cross-review. Root and the record reviewer independently checked
    issuing Rhea direction. Independent evidence is attributed individually in the
    retained reports.
skill: .claude/skills/pathwaymech-resolve-reviews/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: 'Three confirmed cumulative-review defects are corrected and verified: typed-owner
  downgrade/conflict validation, SSSOM prefix completeness and one Rhea source-direction
  scalar. Original reviews remain immutable. The review does not renew full scientific
  approval.'
source:
  git_revision: 70903536191206d2586cd23e46f7d70c32fef92e
  state: working_tree
  inputs:
  - path: .claude/skills/pathwaymech-resolve-reviews/SKILL.md
    sha256: 3d3b9d3b9e56cc782cf4ff63d491c5b589e9bdcde71438a695384b228edc4aea
    role: context
  - path: conf/record_review.yaml
    sha256: a2d6578719a7d080eadc9520695ea7203618b0a7b274ee78fb25dbc17794876b
    role: context
  - path: data/pathways/acetoacetate-degradation.yaml
    sha256: 7b11ec62ac5121cef00cadfcea79114d080c9d989a5dcdb3a1c585a946b3116b
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
    sha256: 45987bc8640120721cfa5d3b2e99b695ad0b017b4165a7de53771b62ed407dd3
    role: context
  - path: output/sssom/source_mappings.sssom.tsv
    sha256: f58b7a07ac6630c37d4df2e509b0e6ab96ee9c9a47b1d23ec10b3acd74c83efa
    role: context
  - path: pages/downloads/edges.tsv
    sha256: a90aef8cc289bff2e4db8f3a59d56270c2ce140c98e733ea5d5a4ea893ab1f7f
    role: context
  - path: pages/downloads/manifest.json
    sha256: a19dda0c62355bd6aeead50f503c694da60dd6dce4ffcbcd4d1d7391dab7733d
    role: context
  - path: pages/downloads/nodes.tsv
    sha256: 45987bc8640120721cfa5d3b2e99b695ad0b017b4165a7de53771b62ed407dd3
    role: context
  - path: pages/records/MetaCyc_ACETOACETATE-DEG-PWY.html
    sha256: bf24bba87cb9441e4b5c52d0ed7309f94cb83ffe196ce3bc9e5e208430f0fc6a
    role: context
  - path: research/publication_review/2026-10-13/README.md
    sha256: 195da5b0069ea1243799b7583f03a2f3a3d0d6bb5795330991c6b6f3f7153a80
    role: context
  - path: research/publication_review/2026-10-13/artifact-preservation-check.py.txt
    sha256: b16d36dc0557601eb1d9e7468e6d4834f98fe8d3f038f58b5a80dee4704e4bf2
    role: context
  - path: research/publication_review/2026-10-13/artifact-preservation.json
    sha256: c5f701e559a0c45909ba007aa35236adde02b44c2840511de571897a3e389722
    role: context
  - path: research/publication_review/2026-10-13/artifact-preservation.md
    sha256: 0bf7dc5d1cf3ad05bbc0471dab70a722db9c06469b67f5b941d3e3e98a86d33b
    role: context
  - path: research/publication_review/2026-10-13/earlier-issue-dispositions.md
    sha256: a1dff15e47056feacb744eed1319a5a4309fc66147a180e247ade3f5c8e46dc9
    role: context
  - path: research/publication_review/2026-10-13/gate-runner.py.txt
    sha256: 8d5a50058d1df1656e6d3cd1de45018e3be605ba42f03b2f1bfe4419df92d502
    role: context
  - path: research/publication_review/2026-10-13/gates/diff-check.json
    sha256: e8fe9cc6b2c07d99a9b12570392ddd964d71d86fcf15635af146d02b5b9772cb
    role: context
  - path: research/publication_review/2026-10-13/gates/diff-check.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/gates/diff-check.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/gates/history504.json
    sha256: fe28066a4432bc6cc790213b0d799b24a176936a0ed977bb70d7c3191dd2382c
    role: context
  - path: research/publication_review/2026-10-13/gates/history504.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/gates/history504.stdout
    sha256: b33042c0db272f68bec644aff5895e23cc506ae35c7a6ecbe1a0db7bc9cca3f8
    role: context
  - path: research/publication_review/2026-10-13/gates/history505.json
    sha256: b2266e0a29e9bf9435732aa55911f55744ddcfdd8880f904b38cb36c2dfa6a2b
    role: context
  - path: research/publication_review/2026-10-13/gates/history505.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/gates/history505.stdout
    sha256: d12ba49e83222dbd5642da5501449992f0056978d294791c8d05e6152a44b4db
    role: context
  - path: research/publication_review/2026-10-13/gates/history506.json
    sha256: f3e742349521e61384efb93a38c7f3601ba209ffebf9d44a535cfba2f46941c7
    role: context
  - path: research/publication_review/2026-10-13/gates/history506.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/gates/history506.stdout
    sha256: 43642124a8891afe2c1fef2df00708473771b3a9e7f7c3b71649dd863ebf2604
    role: context
  - path: research/publication_review/2026-10-13/gates/kgx.json
    sha256: 4c476fd781d0e5b6bb831681cb3b339126ff47bad3679ca5fae847d71e22376e
    role: context
  - path: research/publication_review/2026-10-13/gates/kgx.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/gates/kgx.stdout
    sha256: f603ab73b0b0af103a5bfad9c3acacc76c80cf41da086ed3a0117e218eccc957
    role: context
  - path: research/publication_review/2026-10-13/gates/lint.json
    sha256: 6fae46eaa513e7b5acb8e9e5e47c58ae24fffd0e624c02af2540194b4db5990a
    role: context
  - path: research/publication_review/2026-10-13/gates/lint.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/gates/lint.stdout
    sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
    role: context
  - path: research/publication_review/2026-10-13/gates/render.json
    sha256: fcae22141217a0a20344deb911f55600cb28b38e760c9451354cad1ee1c096d0
    role: context
  - path: research/publication_review/2026-10-13/gates/render.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/gates/render.stdout
    sha256: 0a32e30a0b8c8047f44a17835f89cbd9c94fd7d19231bfbec3f743bf6e7f483c
    role: context
  - path: research/publication_review/2026-10-13/gates/skills.json
    sha256: 8ccee16474e2d561066cf00875736ec91305cfa2698e2bd2e2bff07ebc22aa69
    role: context
  - path: research/publication_review/2026-10-13/gates/skills.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/gates/skills.stdout
    sha256: aa2d3652343b880d16a176d45deb7b4907fb11f43e31f1840d7724658478a527
    role: context
  - path: research/publication_review/2026-10-13/gates/tests.json
    sha256: a8ce0a4194cdac327442f252fca2d7a7b8a613a6263c29b5b17156a7f5aaa1a3
    role: context
  - path: research/publication_review/2026-10-13/gates/tests.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/gates/tests.stdout
    sha256: 219f947202190d844046b8c95bb5901af04496185c080371778635b4c13a8bf6
    role: context
  - path: research/publication_review/2026-10-13/gates/validate.json
    sha256: f33d811f9ed8eaf88b8b563f0f17bfe8f0db2031a14b4b1a737ea847acdb8152
    role: context
  - path: research/publication_review/2026-10-13/gates/validate.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/gates/validate.stdout
    sha256: f23fc6ad8db4b5509076ef0ff7e07198a17437fb4c0e593fc0781133fe472efd
    role: context
  - path: research/publication_review/2026-10-13/gates/vendored-network.json
    sha256: 4e84fe9f0fa3227ed9eff9cdcb26e6534485a03f33424cafc7e56b8d580466e2
    role: context
  - path: research/publication_review/2026-10-13/gates/vendored-network.stderr
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/gates/vendored-network.stdout
    sha256: 3b073aa29da7dc3996edbe18c83d0d6593ba6d03238b663efc40286be4cf428e
    role: context
  - path: research/publication_review/2026-10-13/gates/vendored.json
    sha256: 61d7014a12918148803c3ec289904f88bd5573391187e17bf24ac5dde0940c7b
    role: context
  - path: research/publication_review/2026-10-13/gates/vendored.stderr
    sha256: ede217865e5d787bac31473163e00ab87cb7b8b1cda244481cffa493a1a844d3
    role: context
  - path: research/publication_review/2026-10-13/gates/vendored.stdout
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: research/publication_review/2026-10-13/payload-review.md
    sha256: c6dc8f730caa29a3604464bd72f174946676a91f69b8e4d68b9f513ec28067c1
    role: context
  - path: research/publication_review/2026-10-13/prior-review-interpretation.md
    sha256: f71ec9b3a14497b5d51fcb69212c9dbab519f0fdec76a866da26985fd22eec14
    role: context
  - path: research/publication_review/2026-10-13/records-review.md
    sha256: 1e7f566e9af362b91af660ae5320b72a06494e7ec7d3f01d0f9bbc2ff00f0bf0
    role: context
  - path: research/publication_review/2026-10-13/rhea-direction-proof.json
    sha256: 5609aebd9565d41f79681a1461bb04ede2b6b7bd975d3b7941359817413ee631
    role: context
  - path: research/publication_review/2026-10-13/rhea-direction-review.md
    sha256: a4524550ea14bd5adb40b1d67740193d255a5dc3cefb9474b67019149bf92293
    role: context
  - path: research/publication_review/2026-10-13/rhea-direction-selected-replay.json
    sha256: a516c4ff8be4e2acdc2964c5890f3e7e442c01672639172e28ffd2bea596cd0e
    role: context
  - path: research/publication_review/2026-10-13/runtime-crossreview.md
    sha256: c1e538cd2383894d754f67c01dbe7336cfbb38d8375f2817f520bd3d3e61f02e
    role: context
  - path: research/publication_review/2026-10-13/runtime-fix-handoff.md
    sha256: d9b5802adf247451e1877196bf455be397de73c87b7aa040fde68ea1833a1ae7
    role: context
  - path: research/publication_review/2026-10-13/runtime-review.md
    sha256: 3ca2367da7a7bcf06ac5504752a4e0c5d06b2fe8aa74ae5eff56e9223fdd13af
    role: context
  - path: research/publication_review/2026-10-13/sssom-crossreview.md
    sha256: 5a8c051cbd33fd02119f6e36919daaf06b4e046594f73fa1a8e76fce64ee7eae
    role: context
  - path: reviews/structured/20261012T210220Z-aceto236-scientific/review.md
    sha256: 625eeaf40b02a842a6b922e6b4b7e20848c1fffa9ee8422057944d2c55ec4ae4
    role: context
  - path: reviews/structured/20261012T210220Z-aceto236-scientific/review.yaml
    sha256: 038a92307d232cebe825d521a9ccd5b4be3999d9ce72aa7f6b52c5522e47d73c
    role: context
  - path: reviews/structured/20261012T210222Z-aceto236-technical/review.md
    sha256: fb99bd850b451550809aac8a490f4ea9f9828ac6bd33453de687244e79446ee3
    role: context
  - path: reviews/structured/20261012T210222Z-aceto236-technical/review.yaml
    sha256: 781a81470322b4603b6c7d2bda95bdf4700ec774c4e8a0f721776f79857aa91b
    role: context
  - path: src/pathwaymech/identifiers.py
    sha256: c402be20883584745a2f28c1e73b70d72d563cd5e82cc88efb63bc7658abc173
    role: target
  - path: src/pathwaymech/sssom.py
    sha256: a3022c70d07c44ab8ca0eb59b6095abd5b15aa4831fd24c160a53930ef23c6a7
    role: target
  - path: tests/test_sssom_export.py
    sha256: 582c202623ca5ceb11b3296f5f512a3e74f30d8e4454cdabb2613bf9c463974b
    role: context
  - path: tests/test_typed_authority_consumer_integrity.py
    sha256: a05ed5cb33b06ce6c424be5fefc6f1d177e8d580173afd9be937c28a0aac1e4a
    role: context
scope:
  description: Bounded review of three corrected maintained owners and their generated
    consequences.
  selection: Three confirmed findings from cumulative review of public base e1c66917e753105c4bf5b7b026193fcefa2b000f
    through local 70903536191206d2586cd23e46f7d70c32fef92e.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - authority
  - sssom
  - aceto
  exclusions:
  - target: Other scientific fields, primary papers and full pathway corpus
    reason: Existing scientific judgments are retained, not renewed; current biological
      reassessment is limited to the Rhea source-orientation assertion.
  - target: Public release licensing and interactive browser behavior
    reason: No clearance or new browser verification is established.
targets:
- target_id: authority
  path: src/pathwaymech/identifiers.py
  label: Typed authority consumer
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: src/pathwaymech/identifiers.py
    role: maintained owner
- target_id: sssom
  path: src/pathwaymech/sssom.py
  label: SSSOM export prefix contract
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: src/pathwaymech/sssom.py
    role: maintained owner
- target_id: aceto
  path: data/pathways/acetoacetate-degradation.yaml
  label: Acetoacetate RHEA:21038 source orientation
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/acetoacetate-degradation.yaml
    role: maintained owner
checks:
- check_id: tests
  name: tests
  status: passed
  required: true
  summary: Final execution passed; complete stdout/stderr accompany the receipt.
  target_ids:
  - authority
  - sssom
  - aceto
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B -m pytest
    -q
  exit_code: 0
  evidence_ids:
  - gate-tests
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Final execution passed; complete stdout/stderr accompany the receipt.
  target_ids:
  - authority
  - sssom
  - aceto
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B scripts/run_qc.py
  exit_code: 0
  evidence_ids:
  - gate-validate
- check_id: lint
  name: lint
  status: passed
  required: true
  summary: Final execution passed; complete stdout/stderr accompany the receipt.
  target_ids:
  - authority
  - sssom
  - aceto
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B -m ruff
    check .
  exit_code: 0
  evidence_ids:
  - gate-lint
- check_id: skills
  name: skills
  status: passed
  required: true
  summary: Final execution passed; complete stdout/stderr accompany the receipt.
  target_ids:
  - authority
  - sssom
  - aceto
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B scripts/validate_claude_skills.py
  exit_code: 0
  evidence_ids:
  - gate-skills
- check_id: vendored-network
  name: vendored-network
  status: passed
  required: true
  summary: Final execution passed; complete stdout/stderr accompany the receipt.
  target_ids:
  - authority
  - sssom
  - aceto
  command: bash scripts/check_vendored_sync.sh
  exit_code: 0
  evidence_ids:
  - gate-vendored-network
- check_id: diff-check
  name: diff-check
  status: passed
  required: true
  summary: Final execution passed; complete stdout/stderr accompany the receipt.
  target_ids:
  - authority
  - sssom
  - aceto
  command: git diff --check
  exit_code: 0
  evidence_ids:
  - gate-diff-check
- check_id: artifact-preservation
  name: Exact generated artifact and maintained record preservation
  status: passed
  required: true
  summary: All edges and mapping rows preserved; exact one-scalar record correction
    and intended generated direction/provenance changes.
  target_ids:
  - sssom
  - aceto
  evidence_ids:
  - artifact-check
evidence:
- evidence_id: typed-review
  kind: validation
  reference: research/publication_review/2026-10-13/runtime-crossreview.md
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Independent reviewer compared complete owner registration and producer
    parity; 87 dedicated tests pass, valid corpus authority remains unchanged.
- evidence_id: mapping-review
  kind: validation
  reference: research/publication_review/2026-10-13/sssom-crossreview.md
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Independent SSSOM review and consumer tests verify declared native/scoped
    prefixes and reject unknown prefixes before output replacement.
- evidence_id: rhea
  kind: database
  reference: research/publication_review/2026-10-13/rhea-direction-selected-replay.json
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Six complete issuing Rhea object projections were independently matched
    to all fragments in the SHA-256-verified release142 original. 21038 substrates
    are 21036_R, products 21036_L.
- evidence_id: direction-review
  kind: prior_review
  reference: research/publication_review/2026-10-13/rhea-direction-review.md
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Independent adjudication documents the one-scalar correction and precisely
    bounds the earlier aceto review interpretation it supersedes.
- evidence_id: artifact-check
  kind: validation
  reference: research/publication_review/2026-10-13/artifact-preservation.json
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Complete before/after artifact comparison verifies exact chemistry, edge
    and mapping preservation while source direction and generated provenance are updated.
- evidence_id: prior-interpretation
  kind: prior_review
  reference: research/publication_review/2026-10-13/prior-review-interpretation.md
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Full paired prior reviews were read and their immutable YAML/Markdown identity
    checked; neither contains finding IDs. Exact direction acceptance is corrected
    without renewing other scientific judgments.
- evidence_id: prior-dispositions
  kind: prior_review
  reference: research/publication_review/2026-10-13/earlier-issue-dispositions.md
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Read-only reassessment verifies thirteen earlier issue fixes from current
    code, complete historical execution and acceptance evidence.
- evidence_id: gate-tests
  kind: validation
  reference: research/publication_review/2026-10-13/gates/tests.json
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Actual command, timestamps, exit code and companion full stdout/stderr
    retained.
- evidence_id: gate-validate
  kind: validation
  reference: research/publication_review/2026-10-13/gates/validate.json
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Actual command, timestamps, exit code and companion full stdout/stderr
    retained.
- evidence_id: gate-lint
  kind: validation
  reference: research/publication_review/2026-10-13/gates/lint.json
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Actual command, timestamps, exit code and companion full stdout/stderr
    retained.
- evidence_id: gate-skills
  kind: validation
  reference: research/publication_review/2026-10-13/gates/skills.json
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Actual command, timestamps, exit code and companion full stdout/stderr
    retained.
- evidence_id: gate-vendored-network
  kind: validation
  reference: research/publication_review/2026-10-13/gates/vendored-network.json
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Actual command, timestamps, exit code and companion full stdout/stderr
    retained.
- evidence_id: gate-diff-check
  kind: validation
  reference: research/publication_review/2026-10-13/gates/diff-check.json
  locator: Complete retained report or execution receipt
  accessed_at: '2026-10-13T04:48:10Z'
  support: supports
  summary: Actual command, timestamps, exit code and companion full stdout/stderr
    retained.
assessments:
- assessment_id: typed-owner-integrity
  area: identity
  topic: Issue504 complete typed source registry
  outcome: supported
  target_ids:
  - authority
  evidence_ids:
  - typed-review
  - gate-tests
  summary: Retained native identities cannot be downgraded by selecting a legacy source.
    Complete conflicting projections, counterparts, polymer members and kind collisions
    are rejected before dispatch; identical compatible owners and current corpus terms
    remain valid.
- assessment_id: mapping-prefixes
  area: representation
  topic: Issue505 declared SSSOM namespaces
  outcome: supported
  target_ids:
  - sssom
  evidence_ids:
  - mapping-review
  - artifact-check
  - gate-tests
  summary: All 70 mapping rows are preserved. EcoCyc/MetaCyc native frame namespaces
    and explicitly project-scoped PathBank identifiers expand correctly; undeclared
    prefixes cannot overwrite a valid export.
- assessment_id: source-orientation
  area: graph
  topic: Issue506 RHEA21038 source orientation
  outcome: supported
  target_ids:
  - aceto
  evidence_ids:
  - rhea
  - direction-review
  - prior-interpretation
  - artifact-check
  summary: Source orientation is right_to_left because the directed reaction consumes
    master side R and produces side L. Only this scalar changes; the printed equation
    and all 46 mechanistic edges retain their previous exact content.
  details: This corrects scientific review 20261012T210220Z-aceto236-scientific identity-18/reference-13
    and technical review 20261012T210222Z-aceto236-technical kgx-and-sssom insofar
    as they accepted this direction discrepancy. The prior reviews contain no native
    finding identity for it, so no fabricated resolved-finding lineage is created.
    Earlier literature and other scientific claims are outside this bounded reassessment.
findings: []
actions: []
limitations:
- 'Scientific_review is false: this is a bounded correction/disposition, not a new
  complete literature review of acetoacetate or the nine new records.'
- Prior source access and assay/strain limits remain. Previously observed dense graph
  junction overlaps and long construct-label truncation remain documented; complete
  evidence stays in tables. No interactive, responsive or dark-theme check is claimed.
- Initial vendored check failed sandbox DNS; its retained failed receipt is followed
  by a successful read-only network-enabled execution.
- The original nine-commit payload audit is pinned to 7090353; final small correction-delta
  audit is separate. Source license/release labels remain deferred.
- The GitHub issues had no structured native finding predecessors. Verified fixes
  are recorded as assessments and external issue links, not invented terminal finding
  lineages.
related_reviews:
- repository: CultureBotAI/PathwayMech
  review_id: 20261012T210220Z-aceto236-scientific
  relationship: Corrects the bounded RHEA21038 source-orientation interpretation while
    preserving all unrelated judgments and limitations.
- repository: CultureBotAI/PathwayMech
  review_id: 20261012T210222Z-aceto236-technical
  relationship: Corrects the bounded RHEA21038 source-orientation interpretation while
    preserving all unrelated judgments and limitations.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/504
- https://github.com/CultureBotAI/PathwayMech/issues/505
- https://github.com/CultureBotAI/PathwayMech/issues/506
tags:
- publication-review
- issue-resolution
- bounded-correction
```

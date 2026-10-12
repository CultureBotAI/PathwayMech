# Ribose phosphorylation: lossless archive packaging follow-up

- Review: 20261012T023031Z-ribose-archive-packaging
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-12T02:29:28.933629Z
- Finished UTC: 2026-10-12T02:30:31.151641Z
- Reviewer: Codex /root (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Two inert archived helper copies had trailing blank lines rejected by staged whitespace. They now use lossless UTF-8 JSON wrappers preserving exact original bytes. The archive summary and README describe the conversion. All193 tested bindings, 246 other initial review inputs, and the independent scientific review pair are unchanged. Current archive input hashes follow an explicit reassessment, not a silent refresh. No biological, code or generated-output change.

## Scope And Provenance

Archive serialization and preservation of the exact previously reviewed ribose target and tested inputs. No new biological or primary-literature assessment.

Selection: One exact target MetaCyc:RIBOKIN-PWY, after the two documented archive helper conversions.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9dc303d33d7f798904edf82993211dc53312903d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:RIBOKIN-PWY | data/pathways/ribose-phosphorylation.yaml | maintained | ribose phosphorylation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native packaging follow-up inspect | passed | True | MetaCyc:RIBOKIN-PWY | 255 current inputs captured after explicit archive delta reassessment; actual native inspect passed 2a6bf6/0. |
| Lossless helper conversion and exact preserved inputs | passed | True | MetaCyc:RIBOKIN-PWY | Both wrapper text fields decode to original helper bytes and prior input SHA256; all193 previously tested bindings remain identical. Exactly four prior archive input paths differ, all explicitly assessed. |
| Complete staged whitespace after packaging correction | passed | True | MetaCyc:RIBOKIN-PWY | Passed with empty output in actual root terminal416d55/0; earlier failure76c0b1/2 is retained and resolved. The new review pair still requires the final staged check. |

## Scientific And Domain Assessments

### Lossless archive serialization and preserved scientific inputs

provenance: supported. Targets: MetaCyc:RIBOKIN-PWY.

Original helper byte counts and hashes are restored by decoding the two wrappers. Only their storage representation, accompanying archive summary and README changed. The unchanged target and implementation retain their prior independently assessed biology and passed gate evidence. The previous review remains historical; no prior observation was edited.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| delta | research/pathway_additions/2026-10-12-next-226/packaging/delta.json | supports | Exact four old archive-input changes, two byte-lossless helper wrappers, 246 unchanged prior input files and all193 unchanged tested bindings. |
| science | reviews/structured/20261012T022238Z-ribose-phosphorylation/review.yaml | context_only | Immutable independent complete scientific review of exact unchanged target, implementation and products; this follow-up does not repeat its literature review. |

## Limits And Additional Notes

- This is a provenance-only self-review; literature support was not reassessed. The earlier independent scientific review retains its explicit source, strain, anomer, assay and static-graph limits.
- Full maintained gates were not repeated for an archive serialization change. Their193 bound files remain exact; this is identity evidence, not new scientific proof.
- Native validate/save/check and final staged whitespace follow assembly; this review does not predeclare those outcomes, commit, PR, merge, publication or source exhaustion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T023031Z-ribose-archive-packaging
kind: record
repository: CultureBotAI/PathwayMech
title: 'Ribose phosphorylation: lossless archive packaging follow-up'
started_at: '2026-10-12T02:29:28.933629Z'
finished_at: '2026-10-12T02:30:31.151641Z'
reviewer:
  identity: Codex /root
  kind: agent
  independence: self_review
  independence_basis: Root made and inspected this archive-only packaging correction.
    Independent complete scientific review remains immutable and is inherited only
    for byte-identical target, code and generated products. No independent or new
    literature review is claimed here.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Two inert archived helper copies had trailing blank lines rejected by staged
  whitespace. They now use lossless UTF-8 JSON wrappers preserving exact original
  bytes. The archive summary and README describe the conversion. All193 tested bindings,
  246 other initial review inputs, and the independent scientific review pair are
  unchanged. Current archive input hashes follow an explicit reassessment, not a silent
  refresh. No biological, code or generated-output change.
source:
  git_revision: 9dc303d33d7f798904edf82993211dc53312903d
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
    sha256: f2991a22f16f0d14d83226c6ac261bc779b253b2547fae9724474d8596b411c7
    role: context
  - path: conf/identifier_sources.json
    sha256: 2bd233afdd4d6ebad95581af32381bba0ecac8c0cef8af262a6b7e4bb84dc4c4
    role: context
  - path: conf/record_review.yaml
    sha256: a2d6578719a7d080eadc9520695ea7203618b0a7b274ee78fb25dbc17794876b
    role: context
  - path: conf/rhea_identifier_updates.json
    sha256: f09408d99b8e60b6e2621307c5e4d0845d5451a6de70868690a6b072a2248eb7
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: b81ee9bd9eee83be34b5ddb7f27dc780f8b83b78a35c864a6aa91a16efd118e1
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: e3a8720ae5298efce2122f2469ea6f5a4cc3348d3135ff8549a1ce05a4840a32
    role: context
  - path: data/pathways/ribose-phosphorylation.yaml
    sha256: 385101d166c9150936d81bb0f1c6c0d134b6ac1e6a6454d86e238ac0576e3d71
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 4f3f46d1f4b8ebafa9b2d04d9700510df18b6ec6f881856fda521879f494d153
    role: context
  - path: docs/CURATION.md
    sha256: 408f7c7705b4e6d667b513920e4c39612162d549e0c2666d85bfd53b2c2687f7
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 3af37b2e92b0103da74bc462bedda1021c6bd262d3da13c030eb47344d08b61f
    role: context
  - path: docs/IDENTIFIERS.md
    sha256: 54b17fd51db2fd77285dc1d13522864b945d486140d0ac53c8ad6eb0e45fa46b
    role: context
  - path: docs/record-review-profile.md
    sha256: f3f00eebb7841e9d5ac891271e269f45e926995e16856b8e9a885436570c7819
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/infrastructure/ribose-native-reaction-authority/2026-10-12T020320Z-Codex-7cc4c2.yaml
    sha256: 802e6ff99a5e24b920cbc762c821ef2bb0435f73d3fc23cdb1e6fd887377eb8e
    role: context
  - path: history/records/ribose-phosphorylation/2026-10-12T020318Z-Codex-789d32.yaml
    sha256: efbdb34907a4fb870eb76bacff1b3cc3840508beb0a93854e2e0fdc64ac8be2a
    role: context
  - path: justfile
    sha256: 6d3df7c8fb17835c316a5f37a59c0ff7e61541bbb0781d4dd62ee6ec5fce7df2
    role: context
  - path: output/kgx/edges.tsv
    sha256: 1792ac17158abf6eae033be8db2fe5bf814ed3f115e43778d7e62c380aebc79d
    role: context
  - path: output/kgx/nodes.tsv
    sha256: 7c55cc1d2d1af75fad9e45b5a5531d369ec612feaa7b706f29cbc216714e4a5b
    role: context
  - path: pages/browse.html
    sha256: 2332a85217115c577a0670a82a38391abb00c8011d9bc573c780d0b05838c871
    role: context
  - path: pages/downloads/edges.tsv
    sha256: 1792ac17158abf6eae033be8db2fe5bf814ed3f115e43778d7e62c380aebc79d
    role: context
  - path: pages/downloads/manifest.json
    sha256: 6349e097e3aefc34038658f089082b9a4470be56f3f560025bd039dfc9f559b3
    role: context
  - path: pages/downloads/nodes.tsv
    sha256: 7c55cc1d2d1af75fad9e45b5a5531d369ec612feaa7b706f29cbc216714e4a5b
    role: context
  - path: pages/index.html
    sha256: 0c3745dbb902a7dcdc573fdd3de1d5950407b8e8ec21a6995383430a6ecb6d87
    role: context
  - path: pages/pathway_index.json
    sha256: 12aab727475e84a496de834e62a70fe5759f79110c695d723fc74f57b7ac6883
    role: context
  - path: pages/records/MetaCyc_RIBOKIN-PWY.html
    sha256: c903ccb0036af1a5cd4b3bf248e22774e1e7fd178ef8cab9b94d5fbcffd30a31
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/README.md
    sha256: 3071221b3bec6371da95ecf91190b605aec468d1cb11d4b8f5d6c6040910a813
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/adoption.json
    sha256: 37b07ad5c5a8925c005de8f0580132b4da877d05e80fac25fb5133ad56fd7c15
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/archive-map.json
    sha256: 2fc3b30962248669aa28a6bcfd52523356809d149d3d08fa85787ed5112bc6df
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author-audit/audit.json
    sha256: a99cda35fca7faa854311a3aeb07a61835f845d7853398f4e8bedd04bc6ca410
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author-audit/audit.md
    sha256: 267fc94afcffb78afc19235bf518df4041e470ea4eeed664a21903585af80024
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author-audit/handoff.json
    sha256: 11fcf03fe7bc3b7acbdb6b9adaa0696da4c4edb4bebd4e41ce6448d885760fc7
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author-audit/manifest.json
    sha256: 65d06198bc42a25e19c3f7cee819c0bafbc9ed0cba07fd077ab63be1f34ef01b
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author-audit/rhea-original-replay.json
    sha256: e2918bbc6e1ad620627b53430346d666ed31bfe70dcae36727787af6b7c70ed3
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author-audit/rhea-participants-replay.json
    sha256: 1acc76681f057136025e76b53bc94418f01ff2b97f99b9094e936719175af080
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author-audit/xpath-replay.json
    sha256: 89fc4e9d4754aa0ca6a0b0fe912e8f0a2cdefc05610d6e9e2a78470db16af8f4
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/artifact-manifest.json
    sha256: 568bd267e950c3cda5917f64f0a8fc18bd85911414d14689667f378a8afe9ef6
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/assessment.md
    sha256: 30b81366a36e1b3d82de8d7fb8b3181275e836af890c825e7713715e7701c08d
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/author-counts.json
    sha256: 18e21388235ee2e988f821a96bc6237ea392e7ef960c334527b6c7516ec2a55d
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/author-provenance.json
    sha256: 969111415bd2ef01eae6f98f4b8e245ce6bb4d6d49c0333a56d764128082b925
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/authority-conservation.json
    sha256: c1316c0c29879a8542e3aeb4ed56710c419dbe0b420732a7f6231f6ce1af0189
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/chemistry-replay.json
    sha256: 078a7de8424b61d0994a08d50e6e04b0bc0c84c3107876a9f4931f67d28c6d9b
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/dedup-bridge-search-receipt.json
    sha256: 54c421a1b42dc90e9d4bc95da7f92749f357219505581256a3e346286565d0de
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/edge-evidence-ledger.json
    sha256: 06e47d1a3b0ad6adc23d8be3146d804de8718c6c17ec9f56a2051585fc4207fd
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/gene-identity-replay.json
    sha256: 058b28b1e9adbe8414c0b0fdb62e3ce5ff0db12d94a6f6e3571e0e71b0b31d4d
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/handoff.json
    sha256: 3f0332202b7885be8d8fe9f686bbc5ccfcdda3eedaf811dd6dec4085cd81a57b
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/identity-ledger.json
    sha256: c6622949aeb163bfcab3cad64630e1491d73a5097e03a3dcba35cff0e7aac716
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/imodulon-context.json
    sha256: 53ea72584b5c7f6ff0120cef59e95127cedc817d73c9f4084dc80d1ec242fae0
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/independent-author-audit-bindings.json
    sha256: 262b22425d13734551364fdc14e171ae91933b687216ca7e60e3ddc1c56ea2af
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/negative-controls.json
    sha256: ffe78f8655dc82b903005555f9745021cd7fc2318f70b2169e6f7ff3e83bda12
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/ontology-authority-replay.json
    sha256: c5653a4531e24c2218c6b191511100d1d62fe94f876038d819780d71ea473430
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/reference-original-bindings.json
    sha256: 316d37eb3f54722107a11b1b647a7c505a2961c9138707f613afea04b46c192f
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/rhea-identifier-updates-proposal.json
    sha256: 851bd5f3c795b55c4d66a3a67cda20b870628ba336fa8ad3d2aedf71460b412e
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/seal-verification.json
    sha256: 2e2693bef320bdb1774f44e42141d0b8ef48508627e3deab1fd849c653640bfe
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/sealed-threonine-and-baseline-dedup-bridge.json
    sha256: 54ad4e5d7124b2ec5d7ce749e4d6b78347b1ee9b32e1743154c89547ec086624
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/source-authority-replay.json
    sha256: 06ec69443d86f4f574b03f1916f924cf1fb2e7823694cca64ff2dfcd866a145b
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/source-manifest-additions.json
    sha256: 4a9a62503f03786edb819c810cafff797cc911018a88ab27f9f7e4138659b954
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/source-original-bindings-projection.json
    sha256: 60cfc13d901c93c7a411c9b48b1045fc39862742ddf925106c37b6154da51c33
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/source_replay.py.txt
    sha256: d99e5ccfcbdd3c4163067f5bab2d626724a594b160d9dc7182acc575a9b36a03
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/terminal-receipts.json
    sha256: f9b9e15abab14786a44d40efd0ef2f9e796fb33cd1c465d88dbbc8cc50af52a0
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/threonine-provisional-correction-dedup-bridge.json
    sha256: 30c792fdf41e36ed4add6f7581d9b076375bd2a42a0a0cac9da5b57650498124
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/unnamed-reaction-adapter-proposal.md
    sha256: a584aee6cfe4df5c3bfdcf80d6a723d37ae0a3f2a434948c89d3075560f267b4
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/author/validation-result.json
    sha256: 67bbc64140ad2087c746d2ed3b3bb6464d6084210f1abd378d43501a594e10f0
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/artifact-manifest.json
    sha256: a482f14b1260a6d44786b1b6df62ef6b5308546fcb64e80ee7f9136a7addc405
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/assessment.md
    sha256: 358316297dae78782d768eb3faae404665ec29894c57616020dae803d66a059f
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/composed-changes.json
    sha256: ce55e19e013c7570964f73402943c5d1ddabc8baf0806c369ac71b46a6df560a
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/composed.patch.json
    sha256: 66a71bb6d57b52843ed06d68c28426fbbefc929a1359c0babddddb78e76aa355
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/delta-changes.json
    sha256: 4436cc7fd233de9335d208a0ebf19890be740f0c5534f24b3f0d89b69c532b63
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/delta.patch.json
    sha256: 380aa697f3203e535df07622c5a84e9176db8826f90c2b56752e1894376b5e11
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/draft-provenance-probes.json
    sha256: 458de20b5acb5f09d993478a3a05dc1b51fbe65e85c1c327bb9562c58273b438
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/execution-ledger.json
    sha256: 3106c9ff9d5de99f23d46057886814eb2fffb883be5c5aff4e511923e90c0f13
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/handoff.json
    sha256: 2c816026bf8497e8081322f5731e357a87cb83d066454d2993e49c6c17790517
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/input-bindings.json
    sha256: d0d50355092aaa496baeebd121c361d22ddbeb30a18d682245378ac82b06b727
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/intake.json
    sha256: cf00b88ad632b0aa778480599540f1632904fb83228ccb14d1cf46ceabff5c66
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/logs/authority-suite.log.json
    sha256: 364f505f1482ba96a9334671344cf09cace12cd1b7353ae6608eff23f3453af5
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/logs/composed-patch-replay.log.json
    sha256: f7568a45769c6f4373faed7cfd2439daf4d83a3e414e53883b0df07fccb16d17
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/logs/delta-patch-replay.log.json
    sha256: c4effe4159ee86f51a5c1e7b2a1a6112e78b52cb9ddb710982475461beab75c7
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/logs/draft-provenance-probes.log.json
    sha256: 813ece53d29807e1801d29c1cc4d2c4bff87a818555df4d5b03e7115079eafd0
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/logs/final-reaction-tests.log.json
    sha256: 46c1338169221a69cfbac63ef8e9a97e81ad831f9e39632abc6dca270aabba92
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/logs/final-ruff.log.json
    sha256: 69ef8be89769a19cbb7d702a568355f29a04c0fbef43c5604ef0008bac8a3001
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/logs/native-replay.log.json
    sha256: f33f50e9ab6a61184b334e4ec8bff8c747c3d488254e6454e6474e629abdff76
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/logs/reviewed-defect-regressions-against-initial-isolated.log.json
    sha256: b32ec214e209796987cdaede0c0f0bf9802ee451f2bc56ac6afe59da216d93ee
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/logs/reviewed-defect-regressions-against-initial.log.json
    sha256: aba0e30eee5b57a660b07de373c78487bc0e9a62f47d8d480294cb602f867817
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/logs/ruff.log.json
    sha256: 4e2d8d2ba6d7bf493dfbef05e22c4179c3783a1ff7ac9d7b0dd72e1839fbf65a
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/native-replay.json
    sha256: 39590a1b6a2a14fe81d594b9d154bf8c5b32b3ff25ae369f660729a3d481b409
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/run-checks-initial-import-attempt.py.txt
    sha256: 7a1917ea057c7eb9f4e18e8423cae6959fe9b3c061c28efeb68cfab725c07aea
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/terminal-bindings.json
    sha256: 03e1f40b2989757245dab16989d120c472947d1dcd7eb8704cfe91f13b563239
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-correction/verification.json
    sha256: f1770d8be2e37ad5fe07ebce60618efdeebc05fea1c4a221b3ed532b9ea3bb53
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/actual-bounded-snapshot.json
    sha256: a9150b4f84fbf303d8e61a0c1f7082203b013f17171160fd501994980189bfb0
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/actual-replay-verification.json
    sha256: 698a95c9e16be3d0d2c33ef0fd339d74096bc767f14212f794c72b4d98e7fea3
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/actual-source-manifest.json
    sha256: dcdaeadd8de61e610a11dee7b600a32086c44b516d41ebdc3be309225087c2b0
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/actual-source-receipt.json
    sha256: 902c3e4c5680b4a497bd6dd76f4da11f9e4f159ca8d66307d3fbc11e45fc19e2
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/artifact-manifest.json
    sha256: 3af2aeaf74a6969408c5bfe671f59c8420c89e9aab7cb10507b35ad2761daa08
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/assessment.md
    sha256: 5752838f6e03f52edc970aa2f22762ec20afbff25235c0cb0a44b653ae611b34
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/base-bindings.json
    sha256: 68eea89faae2c1636b2aa44747d38b9352edf07b8241f169ec11e43af8c6c51a
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/changes.json
    sha256: 29b3340ec3100364ace2a8e57f51f71fc0ab938a0f923c92fc7d02c9d7de3b27
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/changes.patch.json
    sha256: 2dd11bcf5da6422a45749f74ad8c81ad0a6ba615823e5367ca7bf63fc554b837
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/execution-ledger.json
    sha256: 0efb1a4443ee685bd5bd03f712f763b44a790c78e97c021eeecc4c92fd54916c
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/handoff.json
    sha256: b4b8ef10c7af40e1dc35a8f7971f030a2828151c7b5b4933ab389962a1091157
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/logs/actual-replay.log.json
    sha256: 7f3703414867d156707fe1bd05602eadafb5110adf76e5bda66618cbce5efa65
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/logs/authority-suite-initial-collection-error.log.json
    sha256: 5c6fe177365b69e8d892922accb056b783e86c1959959a9aedf6991bb1a74da2
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/logs/authority-suite.log.json
    sha256: 3c2e1aee9bf904438a1991886ab83076ce245f418f03717ef640724cf7445a9b
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/logs/patch-replay.log.json
    sha256: ebdf2bb661d05bc662b448bd147b9db280eaa30d01e787125db91d830bac0521
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/logs/ruff.log.json
    sha256: dfa006806a6de24b091a139c9e64f701adf72ef08e6502473c1bb102842abb92
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/prior-adapter-conservation.json
    sha256: 46350394bc4414553997f6350933a8fcb4a95b75b0d94a64e727902867118edf
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-initial/verification.json
    sha256: f8a6e0ae67ce5792d079cc6105140a581aafb85318df85fd2c142032ae81c48a
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/artifact-manifest.json
    sha256: d72f91acab8efd14da4820cf6790dbec0fc6f687ecaba7a033e3b4687c8c1127
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/execution-ledger.json
    sha256: 4c4e89a169634e48e4cbc08796bedea6387bde003eae2b66391084011c7f1b48
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/handoff.json
    sha256: 7baf1f36f0dcf6ad0fb0bd16ed237d4a258d310fda573ba778a2320aa1c6de20
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/input-bindings.json
    sha256: 9ef17e7bbc2e3d6ec0a5762acf04a3c3a410bc065dc02f395764c14774928536
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/intake.json
    sha256: badc31bc8f9c0148cda77258f7ad5a3488453d323c2c4855c3ec4dfb429bd7e5
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/native-replay.json
    sha256: 0ad422c06af6d1fa02feb9684e7a886851a88ab9716a79f9fd95ffbb8ef14628
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/probes.json
    sha256: 66262e6af3421f0660bd096569034ed9fc12bf1b73e3c026506e961354ad789e
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/probes.py.txt
    sha256: 2dd090adbdfc1b8af59576e1b08ca4ef1a55c1bb6c1d9b94272650a98c48505d
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/reproduce-execution.json
    sha256: b96566476be98cecacd25aeee0acec47e705e71e92fb8277d7fcfadcae0e06ae
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/reproduce.stderr.log.json
    sha256: e711148eca288a060facce3d160d697df69c4db780941321da1c45c1b227e041
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/reproduce.stdout.log.json
    sha256: 747e5a53d1f7154f8a7cb2539572b40c1e72a73d3bbd2eb205720ace150f9f49
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/reproduction.json
    sha256: 0fb6c3651325fe9cfdfb531079143a9afb4cd649c5dc4ebdffdf8c42e8e430fd
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/review.json
    sha256: d35a145efa280fc45791f855342884f6b12088e8ace4622d311a5deb0b94e101
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-review/review.md
    sha256: ff40379366d2259deaac8419d649bccfef8f329f94b3f0ee5ab1d79968b92fe6
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/artifact-manifest.json
    sha256: 568f1057b5beac69af6594aa46cdd28a3717c39487a07547406fcc291fc58e82
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/composed-patch.stderr.log.json
    sha256: 3009958004d52e58f120495d5d2d5e7e78873e7ea6121ccf23d311c595493979
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/composed-patch.stdout.log.json
    sha256: 5ab8d26855c03054a13e8ac786dfc7d9253a1a9f63a38a118183cdcea2fcfe62
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/delta-patch.stderr.log.json
    sha256: 92f717d1eee470c73b349c4c256fc3a720d24880ccff9ca0db3ebe6112367a2c
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/delta-patch.stdout.log.json
    sha256: 08cf6864011053639ac25bc21d0fb7cd52781c92edd4fd9387f98f359a7eb8a7
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/dispositions.json
    sha256: cdff3923bae781583c1128a803957fe9809e73733835439f15a224e1a809e8a4
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/execution-ledger.json
    sha256: 6bf303ea9ff3cb3360728b5fb7a775e8bb3348513c39c46f85a46d8f5c84f515
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/handoff.json
    sha256: e18c5b6908418ba6bf12df9d81bc7d7e89b3acc9ee4ed10ee96010b1a620daf6
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/independent-probes.json
    sha256: 5ff4920a3985fd75d443a04a61f5f7ed57e938ed86f3da59e82207d5864a1891
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/independent-probes.py.txt
    sha256: 7b5f5261dd4cbdfd9153b8f6246a0a0404ea4e951746503f133d15677a3a865c
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/input-bindings.json
    sha256: 29f580799986bb61070322069353b6ba68d1059775dcb105de3e33d016b08667
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/intake.json
    sha256: 8c8b7dbe7f759cf6d483290924c037770653bfe1175aaad1265f54764944c0d2
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/review.json
    sha256: 3e7908387b912d9f6df814246bbcffe2ca62e26c1030f6884c36fe633e07eb56
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/authority-successor-review/review.md
    sha256: 32ec25d80e1034d366adb0bf837256be768ef7a7cf2f1bcb8a9140d5d0dbec4c
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/artifact-manifest.json
    sha256: a15eb8e981a1b02c751a968278bc1c2f7629e00a446e2cab167226b6e9e254a5
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/assessment.md
    sha256: d778767228238eef818f1b87f7335846af6967c2abd69d911b45f42fbc2f12db
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/baseline-capture.json
    sha256: 5e604fc67060518e6ff0fcc63067dfc375c571d3105982b820d17690ffc755f8
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/code-change-bindings.json
    sha256: d0cb26806234d31ea106cba624ba9296316ad5f5d5a049661355cb8ab206c715
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/commands.json
    sha256: 8f11d77c90027e78c36db5eb703f8cadcdb941d5fcbf50160a5d9c2ef624c1ea
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/corpus-bindings.json
    sha256: f6732e6d2aeed162e7d8b89d46dbf713eb18f4e43f87fdd618d3de9deb2cfb32
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/execution-ledger.json
    sha256: fc50b3c2bfdab12c9dd01d5bc183ce14ef464384f297a8d2082d1fd0847f8eb5
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/expected-additions.json
    sha256: f03836e387dbf585fad94505dd555871cca13e550ccbaa963c470ad7182a0c7c
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/handoff.json
    sha256: aa9b5159d994cc55e36db673f0376028cc364b88accccc840bfae25f7c587566
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/new-originals-copy-plan.json
    sha256: ea33a36be4817af763d1c1a5d2068b044aff7885bb6b5c3056494b0333f35259
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/ontology-original-bindings.json
    sha256: f1ca1c169270e14e0a82384ed078f40d613bbaa52d95f7003f3048725d7b3cc2
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/ontology_builder-execution.json
    sha256: 8a577bf59cb46b855bca66a4c3e5211e9a3d54a8a1c0ff3869c02ca17b3914a1
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/ontology_builder.stderr.json
    sha256: 49a6b9c028b3286c13df121e608c0aed71ad0608472687fdb3e5a2f21cab4e12
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/ontology_builder.stdout.json
    sha256: 2c79453e91333628d0d2d6d044989a5a575584c6278228a03c70fc4c4717303f
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/prepare-and-build.py.txt
    sha256: 5b66b97d99eb79857bd1ae2bda55de974a06101b4a41ecffdbd2c29161515091
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/retained-attempts/pathwaymech-next-226-canonical-prepare-attempt1.json
    sha256: a5a465feb0afe8aa74454d9aa66b5c087811e4070187e6b3bf826578421dbb54
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/retained-attempts/pathwaymech-next-226-canonical-prepare-attempt1.py.txt
    sha256: 33ada46c659522d15b017cbaa29f1734a06a95836d6a7f3581b776e08a6b74a1
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/seal-intake.json
    sha256: 4c38f5a96b92d26f11de0bf371499e6b6b14ba84053094ff74ec19881973e4a0
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/source-original-bindings.json
    sha256: c0330c8fac8cf63ee8abef04e09d4ccc9033a518554a1f4257b7efe1e52df866
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/source_builder-execution.json
    sha256: 31773844665a2e8c588ce1cbf9af70252bce90795ec75d0d07f33a63fa205cfc
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/source_builder.stderr.json
    sha256: 00ae86b35225c3d7bc470422cccd097335382c62d846a0556b0010cf76887928
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/source_builder.stdout.json
    sha256: 39530419746030bf5863d4674ea2d7130ea145f7e5850695113ba3e0f55492e1
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/tool-terminal-receipts.json
    sha256: 61bf6ad1c2aa86e6405f4ca873418248558d63280100351b6ee1cf1ea196fc18
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-build/verification.json
    sha256: 8a5ccafab082704bbd8582f2e6593b5c010ebf347a3bf67b97436e07ddc7c277
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-root-review/artifact-manifest.json
    sha256: 01e163641ef8540dd3b2253d36ce5171eee86397505a888a268068dacac3bfb8
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-root-review/audit.py.txt
    sha256: 6fdb581bd15a656a82cc700143569e06e79546d2399ae7bf4511c981c16da406
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-root-review/checked-bindings.json
    sha256: f881ea1a904dba8b8dadbe92a52a959fecbb7e6642a85cb71c46d05658a522be
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-root-review/execution-ledger.json
    sha256: eded62036c8a13847c9b5719011cee602286f1fe7c525adadef9d5b0cebc805f
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-root-review/handoff.json
    sha256: 818eaa3a95a6048b448efc45cfab3640df062ea68d82fe79ee5121a9659b8666
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-root-review/review.json
    sha256: 5d78a001e9658dacdc92fbc30d011ba565a2da10a9ee6d5838477d1d922f4ca4
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-root-review/review.md
    sha256: 67f4c1b7009a12b59c48532d777baeb22e5b7131257ce2ee603b607a3ea549b2
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-root-review/snapshot-loader-check.json
    sha256: 64ff8065894fa3a9e345d6f34c3e513c8e695164767496ad4e73967c4ce758ca
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/canonical-root-review/verification.json
    sha256: fab70379a6a5d260ad2a83a1c347a96298e0759392f7747ceaf5d16c55333ee2
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/README.md
    sha256: e26ecada16c2537caa382e443929b553cdc96625e427f642a1e155d0678cbec6
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/adopt.py.txt
    sha256: 5fc038a1023995c83799a4c7ea12604ffd7e863f79832c75732b4b78ccb56f13
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/approved-node-display-delta.json
    sha256: 37dd3658d71368bcd24d4f42a1064c646c502e3fa5bfb912841b2969747e532c
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/capture-baseline.py.json
    sha256: d930cf95137c7a162844bcf33f50da8b0656b6ae309689f4e113608954cb11d8
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/diff-check.stderr.json
    sha256: b5783cca330dc31b2b2372724628077bac04f66c3eed45d9ebe2b9415833d991
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/diff-check.stdout.json
    sha256: 9d97c2892f3dbf29be99735768b15d4f910ddc7e5b63cc096b9ef19090a4ee6d
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/execution.json
    sha256: 6b47a5e7a5e1274cd735b43ea42a633a774f981c54a5955ca9061d03190f1597
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/gate-inputs.json
    sha256: 255089f42d3fbe3d3d4e82c39303e3fd5938d939aaf6b9cd5a0d40d7f8baf35f
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/history-execution.json
    sha256: 2bb96303a2606e72fbce65dbc261d2f0b86d9e7d4d91987e944c13a736b1813a
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/integration-bindings.json
    sha256: d3272a8dff28f54ab1e1a82b3dbf5a487a96ba4604aa882617065ec65f836b81
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/integration-common.py.json
    sha256: dd4e01ee6f18234f2a4525561f0784070263f1c4cb712a359d9a3e4111c39b0a
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/kgx.stderr.json
    sha256: 2d1c1421e689e9c4c9957f4f6584eaa2b679632fa3ce226e6cd5883f14f0d7ca
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/kgx.stdout.json
    sha256: 536583256880a6597e17f37872698cba1b14336d885aa527b017c1baa6959f1f
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/lint.stderr.json
    sha256: 21fb1edaa942f13aa24fe29838cfb3d34b03e8f1cccf97a4fcf059f015baeecb
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/lint.stdout.json
    sha256: e9f3910f1534c35feccc0be3681427108d69604e7671a8cac7486b4ccbb4abe8
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/merged-baseline-receipt.json
    sha256: f355656a5933c89b985c01922d419ad33a03dfc8a939c5cd4a3e73d8066d3317
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/merged-baseline.json
    sha256: 3401ad624ade92f6abfd7186a73ec333d074d0409209b6d1194f70b3d993934e
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/node-display-assessment.json
    sha256: fc6edb0e59983faf6134e726399703c05624eb38092b9058e51243995cd5068c
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/pre-gate-bindings.json
    sha256: 1af44d81e617945b7362017adfe13efcb6ad93efc64874cb1f6fe837aaf43838
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/preservation.json
    sha256: 2a8a04d64d7b3bf985531c8fa521565f46bca0bfb7d0b7a45ac54dca6cbe001c
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/preserve-maintained.py.txt
    sha256: 5daf48b0dd8a69d23c98a8d9f9b12e5bee9f6e049a4dfee1a281eab3393bbc84
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/render.stderr.json
    sha256: bd03e9614372cf42c2abfdf28eb19aa6dce8128af33bb204bc937dc629b88ff9
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/render.stdout.json
    sha256: cf5c0db60cfb878187d0843d84467f635bb5aaf9a3d611096a3a2108edbdfba5
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/run-gates.py.txt
    sha256: d53224bd265b2c017a5340b7bf88861e52761587c4e6b1ff4ff650417d757c87
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/skills.stderr.json
    sha256: 9a00b8c8bff53f2a9fe9d282dccd42031c9d5c6292d77d9fd75083ef1696dca7
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/skills.stdout.json
    sha256: 07e3987822cf162a8ae3c409ac59e8318a19c385566465c9f3f545f60313a899
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/static-preview-observation.json
    sha256: f276925c1bedf49de1d4b656b33b92994ee8ad555e622dbcd45c03d889d8fd57
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/summary.json
    sha256: 413d2d6c456b96b7786b9e27c8aafda8de706ff76eff0a9d6d426aa51ef9ad15
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/tested-inputs.json
    sha256: 93dff6afb2cf220d80314a3c2e80e213f02be9f3f73d674c6c54b705f8c62d71
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/tests.stderr.json
    sha256: 577397510072d7d99adb50b5b8909431e2b1851a391294b34264f3ddae045824
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/tests.stdout.json
    sha256: da157f49c84676f382d7fd354ed34b91c6d76b5128737976ad5ede56df5cd7dc
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/validate.stderr.json
    sha256: bb741a1dbee80edeb2d04bddcbd3ba0e030b41a36ba0d8956717a8513cb26018
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/validate.stdout.json
    sha256: 2559dc888aeac06a3998ad8f8dab672fd6f74f1e99f8cef1754977fdb36b33b6
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/vendored.stderr.json
    sha256: 25aaddab5200b7341af43e416a9a08b2c7a559ec2edc8eb8bf0c67344fba4a28
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-gates/vendored.stdout.json
    sha256: 9af048f93d5f6a7a626447ace2a2913cd4ea35569704c8a3a705765ad5622819
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-predecessor-bridge/artifact-manifest.json
    sha256: 116ab3f1c3c61fea03ad22e80d55c2533a29ba855b003d670e237297ba1ddbd2
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-predecessor-bridge/comparison.json
    sha256: 7eec47111813b8309eff9cf4d540e939e881b2a7fadc3abbc274632f1e9f6b0e
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-predecessor-bridge/current-corpus-records.json
    sha256: 1c7b0ef2361a5497cbfe8532989ae87cdc655e09113e1a4701df74638563b4dd
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-predecessor-bridge/handoff.json
    sha256: e54845bfc403e9d576390273bf650e475c35f34542543f6c835488c50ed58559
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-predecessor-bridge/input-bindings.json
    sha256: 23dce550308755c5dbf99c3e1bc0798fbfb363655d88760851a85dfd67c94d19
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-predecessor-bridge/report.json
    sha256: ee1da17d124ce9142413d593367d2a886b170ec691dbc9d9db8849fbab825f13
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-predecessor-bridge/report.md
    sha256: 14fef94383995c2d8a4c0ee474c43f4e6b72d1779971eeffb08bda97ec38b34c
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-predecessor-bridge/seal-verification.json
    sha256: 2c567b174d0559238ab5844ac4ca3e8fa13e9b7967ce6ca24649b17d500d57cf
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-predecessor-bridge/search-adjudication.json
    sha256: a70140b2d70fdb3b4e3f5b18318c248910ec2da81805c5fd7512671b08a15f80
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/final-predecessor-bridge/terminal-receipts.json
    sha256: e1dd47d9e7fb77f4e373d777d0c017547665bd1999ab50b24e3bfedf177c3de3
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/issues/436-typed-reaction-provenance.md
    sha256: 77c9a39bcd07c02f08c39f5367ceec540d2793b551b17f7e8997e86e91e78bea
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/packaging/delta.json
    sha256: a28eea6145d97799085e6e25f6445343cc0f3802f99c06accf591c147bfab81e
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/packaging/prior-final-gate-summary.json
    sha256: 0afdd927b3616a4d3d4d177222ef268a1db76ecaebcb66d2c9168ceb8f414c6c
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/page-qa/page-qa.py.txt
    sha256: 323b1fafadc64cf8248d122ac42deec351b1d7d0968f99ac77baf26d78a821e7
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/page-qa/receipt.json
    sha256: 3185e7e899187ec8342823519e471a864b0fd7718330d9678ed3a763bf969564
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/page-qa/visual-assessment.md
    sha256: b400520707d412b74ed56d4889bfea62c221aa23de0da06dcc70ba209fa2f4a0
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/review-completion.json
    sha256: 946059ab34289ac0b0edccb885e28bec8cbdfd05a7c8ba7cb11b72ee07c34c6d
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/root-intake/pathwaymech-next-226-authority-correction-seal-audit-20261012.json
    sha256: 243fb8cf0680d87c9ececcdfe261f14ffb72c36e6ae668cffb073d5f61fbbe63
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/root-intake/pathwaymech-next-226-authority-root-successor-intake-20261012.json
    sha256: 1300136255e72ff1c2a2b0b8ca290999a329521036caabd9ef4867c4020b6b5b
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/root-intake/pathwaymech-next-226-root-author-intake-20261012.json
    sha256: f232c3dc6e1b3b2945c4093638373dd5cb83836effe96d217ec67f05b1be8381
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/root-intake/pathwaymech-next-226-root-canonical-review-intake-20261012.json
    sha256: 717d65270aa55446ac87a5f48c3e8554df69f7a550eeb9070a9b327ff408e35e
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/root-intake/pathwaymech-next-226-root-final-bridge-intake-20261012.json
    sha256: 64c575977dd002270f947cdd08cb4610bda82e21c0563ed30b905c776db4cdb9
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/root-intake/pathwaymech-next-226-root-preflight-acceptance-20261012.json
    sha256: d4bb3e208f8e2f29d4434a6d2fc63b59ad29cbd972ab2161b16bb6775573355e
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/science/artifact-manifest.json
    sha256: cb90f42dedcf06f6c39ec446b747fe6f35a07dd0adbb81711c39713cac2d51f8
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/science/domain-probes.json
    sha256: 06f16b9a6877d0586dc6729aacd58d91934258ccd59c5d4baf88e5036bef93be
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/science/handoff.json
    sha256: 0d8e488bc38ca666c0fff8333a416987823c5ac9eb6242f87d906279d822275b
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/science/independent-locator-probes.json
    sha256: 1f7b74c8f52ec1f24a359895cdce64158e44c4146de392a06325191c9eb9a7b8
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/science/independent-negative-controls.json
    sha256: f885d04fd889e56c7b5f7680e8bdc862268718ba4c26b011c4d16076bd1f670d
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/science/input-seal-check.json
    sha256: 4e1b15abd695847d1fb912bb18f776d96afdb5776866485cbf7afc1c64b0af45
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/science/reference-hash-checks.json
    sha256: 6c50c5d45dd9a395282c6c86e505641d43ce3b96e7d43cc3e92864a0f0ebbe01
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/science/review.json
    sha256: f17ba81c496211163e573ca7d4d238939048b509204d1f0987e2eb2fc229b64c
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/science/review.md
    sha256: 6e19288b4c5e35748db3dbd85214abe40fc68f2c1682ef47eed12473cc9a9d4f
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/science/seal-verification.json
    sha256: 94c9aeb933b39a79ea727c902a4d67c16341be019553bb4068f144867333fbc7
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/science/supplemental-probes.json
    sha256: 411ff62d44db08dc83f021cd1c9c6365ee10fc153d5aea4ba5e8c100173f75c0
    role: context
  - path: research/pathway_additions/2026-10-12-next-226/science/terminal-receipts.json
    sha256: 3eb24cb5f03d4e8dcbd16470fc1345508a379cb80e8dd4ee1b16fb6f1ba358c1
    role: context
  - path: reviews/structured/20261012T022238Z-ribose-phosphorylation/review.md
    sha256: b47a2434fdac47fe279f956234ec0e8c1e4ef77ea08242ee6839342d798d0769
    role: context
  - path: reviews/structured/20261012T022238Z-ribose-phosphorylation/review.yaml
    sha256: 412d87a6eb2e14e3ccab883477e59ca5205f9d7429f08997da93aa1330130671
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/build_ontology_identifier_snapshot.py
    sha256: 538dc16bbe67b5f5a3faacf01c968f32900b6fdb76e71f55ebb933ccf8e7a715
    role: context
  - path: scripts/build_source_identifier_snapshot.py
    sha256: 730021774afeff293808d5128133be5360b2aac7472c3eb7ae9153bde37a9aed
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/pathwaymech/graph_view.py
    sha256: df277b9222b84ed0d225d6a9e2c8933ac210773239d46e26faf77e19e179d923
    role: context
  - path: src/pathwaymech/identifiers.py
    sha256: e54c82d8098c007c2061fe1767c25b3f1bd5faccbe24cb36e08aed2c0b7eae7a
    role: context
  - path: src/pathwaymech/kgx.py
    sha256: 4419ba74ee3949ac84a1ca1bb3cde3bf3ce73a5c975ebeab81ec1ef09dcdf3f9
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 73c77e3935d0e402ecbdd205298aded196ca6a39cd6b376e1018dd4ff5225bf2
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 13bc49026ce56817797f2faea8903f1484238901c50e49c6bc13571beb5657c3
    role: context
  - path: src/pathwaymech/strict.py
    sha256: 2f6a7edf501952ee4aaa41be2f9512d20e1edb2dd87a22b6add6d26928c0dc84
    role: context
  - path: tests/test_browse_interaction.py
    sha256: 1bb51280d026cf639b4628f354cb283925f0107b04100d4188a6e30ca695d101
    role: context
  - path: tests/test_graph_interaction.py
    sha256: 4b4bbe570371fe77fc88d51d2e92ad216ddff7ecdacadd6cc78753aff350d071
    role: context
  - path: tests/test_local_source_recipes.py
    sha256: 3de220417bb7aa7884b6f5e312de8315901132eff108cf3b95ce686d4fec505a
    role: context
  - path: tests/test_metacyc_reaction_authority.py
    sha256: 7514919341517740a5b86d1634b9dfda2e4e077ea7e357cddbf1fc9ad7842732
    role: context
scope:
  description: Archive serialization and preservation of the exact previously reviewed
    ribose target and tested inputs. No new biological or primary-literature assessment.
  selection: One exact target MetaCyc:RIBOKIN-PWY, after the two documented archive
    helper conversions.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:RIBOKIN-PWY
  exclusions:
  - target: New literature review or biological reassessment
    reason: Product bytes remain identical to the separately saved independent scientific
      review.
targets:
- target_id: MetaCyc:RIBOKIN-PWY
  path: data/pathways/ribose-phosphorylation.yaml
  label: ribose phosphorylation
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/ribose-phosphorylation.yaml
    role: Maintained pathway identity, chemical scope, components and edge evidence
      owner
checks:
- check_id: inspect
  name: Native packaging follow-up inspect
  status: passed
  required: true
  summary: 255 current inputs captured after explicit archive delta reassessment;
    actual native inspect passed 2a6bf6/0.
  target_ids:
  - MetaCyc:RIBOKIN-PWY
  evidence_ids:
  - delta
  exit_code: 0
- check_id: lossless
  name: Lossless helper conversion and exact preserved inputs
  status: passed
  required: true
  summary: Both wrapper text fields decode to original helper bytes and prior input
    SHA256; all193 previously tested bindings remain identical. Exactly four prior
    archive input paths differ, all explicitly assessed.
  target_ids:
  - MetaCyc:RIBOKIN-PWY
  evidence_ids:
  - delta
  exit_code: 0
- check_id: staged-whitespace
  name: Complete staged whitespace after packaging correction
  status: passed
  required: true
  command: git diff --cached --check
  summary: Passed with empty output in actual root terminal416d55/0; earlier failure76c0b1/2
    is retained and resolved. The new review pair still requires the final staged
    check.
  target_ids:
  - MetaCyc:RIBOKIN-PWY
  evidence_ids:
  - delta
  exit_code: 0
evidence:
- evidence_id: delta
  kind: validation
  reference: research/pathway_additions/2026-10-12-next-226/packaging/delta.json
  accessed_at: '2026-10-12T02:30:31.151641Z'
  support: supports
  summary: Exact four old archive-input changes, two byte-lossless helper wrappers,
    246 unchanged prior input files and all193 unchanged tested bindings.
  snapshot_sha256: a28eea6145d97799085e6e25f6445343cc0f3802f99c06accf591c147bfab81e
- evidence_id: science
  kind: prior_review
  reference: reviews/structured/20261012T022238Z-ribose-phosphorylation/review.yaml
  accessed_at: '2026-10-12T02:30:31.151641Z'
  support: context_only
  summary: Immutable independent complete scientific review of exact unchanged target,
    implementation and products; this follow-up does not repeat its literature review.
  snapshot_sha256: 412d87a6eb2e14e3ccab883477e59ca5205f9d7429f08997da93aa1330130671
assessments:
- assessment_id: packaging
  area: provenance
  topic: Lossless archive serialization and preserved scientific inputs
  outcome: supported
  summary: Original helper byte counts and hashes are restored by decoding the two
    wrappers. Only their storage representation, accompanying archive summary and
    README changed. The unchanged target and implementation retain their prior independently
    assessed biology and passed gate evidence. The previous review remains historical;
    no prior observation was edited.
  target_ids:
  - MetaCyc:RIBOKIN-PWY
  evidence_ids:
  - delta
  - science
findings: []
actions: []
limitations:
- This is a provenance-only self-review; literature support was not reassessed. The
  earlier independent scientific review retains its explicit source, strain, anomer,
  assay and static-graph limits.
- Full maintained gates were not repeated for an archive serialization change. Their193
  bound files remain exact; this is identity evidence, not new scientific proof.
- Native validate/save/check and final staged whitespace follow assembly; this review
  does not predeclare those outcomes, commit, PR, merge, publication or source exhaustion.
related_reviews:
- repository: CultureBotAI/PathwayMech
  review_id: 20261012T022238Z-ribose-phosphorylation
  relationship: Packaging-only follow-up; complete independent scientific assessment
    retained for unchanged product inputs.
tags:
- ribose
- packaging
- provenance
```

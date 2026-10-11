# Independent initial glyoxylate assimilation review: native hydration attribution

- Review: 20261011T101702Z-glyoxylate-initial-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T10:07:50Z
- Finished UTC: 2026-10-11T10:17:02Z
- Reviewer: Codex independent reviewer (/root/pathway_authority_cache) (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The complete native glyoxylate-assimilation cycle, exact current chemical sides and biological scope are supported with explicit strain, assembly and source-structure limits. One minor native hydration source-assertion defect requires a bounded correction and successor review. All initial coordinated gates passed.

## Scope And Provenance

Full scientific assessment of one frozen target and its edge-level original evidence.

Selection: Exact target SHA256 b28136c61fae7fcf2b9673d176e74d0c001b6cfedeab652ba75ab4ac01aa01e5.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a3a31179b0533cacbf59559a3151c8ebcaac4f97.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-5744 | data/pathways/glyoxylate-assimilation.yaml | maintained | glyoxylate assimilation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical initial and final expanded input inspection | passed | True | MetaCyc:PWY-5744 | Initial inspection preceded assessment. Final expanded inspection confirmed all 12 initial input hashes unchanged and captured the sealed initial integration and graph receipts. A first attempt used a nonexistent ontologies.json filename and was corrected to the actual ontology.json; the target capture itself was unchanged. |
| Independent original-source and chemistry replay | passed | True | MetaCyc:PWY-5744 | Actual reviewer session 50825 exit 0: 79 original bodies rehashed, 220499 RDF nodes parsed, all 13 directed equations, 54 chemical sides, 13 atom/charge balances and 14 material-flow links passed. Protein-scaffold cancellation is explicit for the two carrier reactions. Evidence prose was assessed separately. |
| Independent native/current stereochemistry comparison | passed | True | MetaCyc:PWY-5744 | Actual reviewer session 41340 exit 0. The native CPD-9409 acyl stereocenters differ from current CHEBI:75634; primary Figure 1 and 2008 chemistry support the selected form. CPD-627 shares S acyl stereochemistry with CHEBI:58668 but leaves CoA stereocenters unspecified. |
| Coordinated render | passed | True | MetaCyc:PWY-5744 | Actual renderer exited 0 for all 209 records. |
| Coordinated validate | passed | True | MetaCyc:PWY-5744 | Actual full corpus QC exited 0: 209 native/closed/identifier-checked records, 12566 evidence blocks, 317 valid histories, 30 sources, six documentation files and current pages. |
| Coordinated test | passed | True | MetaCyc:PWY-5744 | Actual full child command exited 0: 1059 passed, 3 skipped and 3 warnings in 406.23 seconds. The archived log and digest were independently inspected. This is the initial pre-correction result. |
| Coordinated lint | passed | True | MetaCyc:PWY-5744 | Actual lint command exited 0, All checks passed. |
| Coordinated identifiers | passed | True | MetaCyc:PWY-5744 | Actual identifier/name-policy gate exited 0 for all 209 records. |
| Coordinated kgx | passed | True | MetaCyc:PWY-5744 | Actual separate CLI export exited 0 for 209 records; the sealed artifact audit preserves all 107 target edges and 184 evidence blocks. |
| Coordinated diff | passed | True | MetaCyc:PWY-5744 | Actual git diff --check exited 0. This check does not by itself cover untracked additions. |
| Exact organism dataset applicability | not_applicable | True | MetaCyc:PWY-5744 | Chloroflexus is absent from the inspected 20-organism/28-dataset inventory. Console availability failed before requests; unchanged direct-client acquisition and offline parsing succeeded. No negative expression or pathway inference. |

## Scientific And Domain Assessments

### Complete native second-cycle boundary

identity: supported. Targets: MetaCyc:PWY-5744.

The record retains all 13 native reaction objects and regenerates acetyl-CoA while converting glyoxylate plus CO2 to pyruvate. Prior scout and hidden/ignored-inclusive searches distinguish this from first-cycle glyoxylate production and the whole bicycle. Shared precursor reactions do not make it a duplicate.

### Directed chemistry, carrier forms and stereochemistry

grounding: supported. Targets: MetaCyc:PWY-5744.

All 54 sides, coefficients, 13 balances and 14 shared-intermediate links pass independent original-RDF replay. Whole protein carrier states are retained. The native CPD-9409 stereochemical conflict is explicit; the primary figure and Mch study support the selected current methylmalyl form. Native CPD-627 unspecified CoA stereocenters are not silently treated as exact identity.

### Strain and experimental identity

evidence: supported. Targets: MetaCyc:PWY-5744.

Species-level scope is appropriate with explicit OK-70 preparations and J-10 genome/construct assignments. Reviewed and unreviewed protein evidence is graded; exact PCS sequence identity was independently checked. Similarity does not become direct strain-specific experimental evidence.

### Enzymes, assemblies, cofactors and regulatory limits

evidence: supported. Targets: MetaCyc:PWY-5744.

MCR dimer, Mcl hexamer, Mch/Mct/Meh dimers and fused BC/BCCP tetramer have source-specific support. PCS remains a functional role with trimer/tetramer uncertainty, and no exact whole ACC assembly is invented. Primary K/Mg dependence, similarity-based CT zinc, metal stimulation and assay-only inhibition remain distinct. No pathway-specific transcriptional regulator is inferred from gene clustering.

### Evidence and generated graph preservation

provenance: supported. Targets: MetaCyc:PWY-5744.

The sealed programmatic audit preserves all 107 target edges and 184 evidence blocks, categories, endpoints and references across YAML, SVG and actual CLI KGX. No browser visual inspection is claimed. All initial gates passed.

### iModulonDB applicability

evidence: not_applicable. Targets: MetaCyc:PWY-5744.

The retained dataset inventory has no Chloroflexus coverage. This is an applicability limit, not evidence against the pathway.

### Exact native hydration assertion

provenance: concern. Targets: MetaCyc:PWY-5744.

glyox-edge-066 evidence[1] incorrectly describes RXN-8965 as carboxyl transfer. The target reaction and chemical edges are correct, but the source assertion and locator need a bounded correction.

## Findings

### f-native-hydration-attribution: Native hydration evidence describes an unrelated carboxyl-transfer reaction

minor / open / confirmed; issue key: glyoxylate-rxn8965-native-hydration-attribution.

glyox-edge-066 evidence[1] cites MetaCyc:RXN-8965 but its source_assertion describes transfer from protein-bound carboxybiotin to acetyl-CoA. The original RXN-8965 stores CPD-627 on the left, CPD-14205 plus WATER on the right, and RIGHT-TO-LEFT physiological direction: mesaconyl-C4-CoA hydration to (S)-citramalyl-CoA. A no-Rhea-cross-reference fallback copied text appropriate to RXN0-5055. Independent inspection of all 13 originals found this one affected assertion. Keep the correct selected RHEA:38273 chemistry and separate master 38271 identity evidence, replacing only the native assertion and adding reaction-direction to its locator.

## Recommended Actions And Acceptance Checks

### correct-native-hydration

Preserve the initial review and input bytes, correct the native RXN-8965 source assertion and locator, update its projection and add a targeted no-xref source guard.

- Archive all initial inspected inputs before mutation.
- Native assertion explicitly describes CPD-627 versus CPD-14205 plus WATER and RIGHT-TO-LEFT hydration; separate current Rhea identity evidence remains intact.
- Regression distinguishes RXN-8965 hydration from RXN0-5055 carboxyl transfer; replay all chemical/source/schema/export checks and applicable shared gates.
- Save an immutable successor with the same issue key and exact previous occurrence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | MetaCyc:PWY-5744 and 13 original reaction XML objects; reaction-list; left; right; reaction-direction; enzymatic-reaction; dblink | supports | All native members and physiological directions independently inspected. The exact second cycle includes the shared acetyl-CoA-to-propionyl-CoA module and all five glyoxylate-assimilation transformations. |
| primary-cycle | PMID:19955419 / PMC2795484; Results sections 2–7; Discussion sections 8–14; Methods section 15; independently viewed Figure 1 | supports | Four-enzyme reconstitution, complete boundary, specific CoA ester identities, assemblies, kinetics and separate OK-70/J-10 scopes support the record. Figure 1 explicitly names the selected (2R,3S) methylmalyl form. |
| primary-enzymes | PMID:11948153; PMID:18065535; PMID:24206647; PMID:12374834; PMID:36535006; PMID:38572988; Exact independently inspected Results/Methods and source-body hashes in glyoxylate-independent-review-audit.json | supports | Primary MCR, Mch, Mcl, Mct, Meh and fused BC/BCCP results were checked with their strain and construct limits. Ion dependence versus mere assay presence and uncertain oligomers are distinguished. |
| pcs | PMID:11821399; Original author-paper web rendering: Methods, Cell Material and Characterization of the Enzyme; Results, Molecular Properties, Stoichiometry, Catalytic Properties and Possible Intermediates | supports | The original paper supports OK-70 PCS activity, NADPH specificity, ATP to AMP/PPi, K/Mg omission and add-back, and uncertain trimer/tetramer mass. Compound X is likely, not conclusively identified, 3-hydroxypropionyl-CoA. No local original-byte hash is claimed. |
| protein | Nine original current UniProt entries; NCBIProtein:AAL47820.2; native complex/monomer XML; Exact sequence, organism, comments, evidence codes, indexed references and component coefficients | supports | All selected entry identities and explicit inference tiers inspected. Original 1822-residue AAL47820.2 sequence exactly matches Q8VRG6, with OK-70-fl source qualifier. No arbitrary native/current strain identity or whole-ACC stoichiometry is inferred. |
| replay | research/pathway_additions/2026-10-11-next-206/glyoxylate-independent-review-audit.json; original_source_replay; stereochemistry_replay; sequence_bridge; deduplication | supports | Independent complete-source replay and scientific assessment preserve all source conflicts and the one bounded provenance finding. |
| wrong-native-assertion | MetaCyc:RXN-8965; Reaction[@detail="full"]/left; right; reaction-direction | refutes | The native object contains CPD-627 on the left and CPD-14205 plus WATER on the right, with RIGHT-TO-LEFT direction. It does not describe biotin carboxyl transfer. Only the RXN-8965 no-Rhea-cross-reference fallback is wrong; RXN0-5055 correctly uses the carboxyl-transfer text. |
| gates | research/pathway_additions/2026-10-11-next-206/initial-integration-receipt.json; gates; test_summary; supporting_receipts | supports | All seven initial coordinated commands passed. Each archived log was read and rehashed. Programmatic graph/KGX checks preserve the complete target and baseline; these results do not establish scientific truth. |
| context | research/pathway_additions/2026-10-11-next-206/imodulondb-applicability.json; covered organism/dataset inventory and offline-parser receipt | context_only | Chloroflexus is not represented in this inventory; transcriptomic context is not applicable. |

## Limits And Additional Notes

- PCS original full paper was inspected through the author-copy web rendering; no stable downloaded original-byte digest is claimed.
- The precise strain and construct limits, inferred CT subunit roles/zinc, uncertain PCS oligomer count and MCR intermediate trapping remain explicit; deterministic replay does not resolve these experimentally.
- This is the initial pre-correction observation, not acceptance of future edited bytes.
- Generated SVG/KGX evidence was checked programmatically; no browser interaction or visual rendering inspection is claimed.
- All 12 initially captured input hashes were rechecked unchanged before expanded inspection.
- The source assertion defect does not invalidate the selected hydration chemistry or imply another pathway gap.
- The external ordinary-python attempt lacked PyYAML; the repository environment was used successfully for the subsequent bounded sequence/metadata check.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T101702Z-glyoxylate-initial-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: 'Independent initial glyoxylate assimilation review: native hydration attribution'
started_at: '2026-10-11T10:07:50Z'
finished_at: '2026-10-11T10:17:02Z'
reviewer:
  identity: Codex independent reviewer (/root/pathway_authority_cache)
  kind: agent
  independence: independent
  independence_basis: Authored the separate archaeal HP/HB record and participated
    in shared source/chemistry discussion. Did not author this glyoxylate target or
    its author dossiers; independently inspected original evidence and implemented
    the reviewer RDF/chemical replay.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The complete native glyoxylate-assimilation cycle, exact current chemical
  sides and biological scope are supported with explicit strain, assembly and source-structure
  limits. One minor native hydration source-assertion defect requires a bounded correction
  and successor review. All initial coordinated gates passed.
source:
  git_revision: a3a31179b0533cacbf59559a3151c8ebcaac4f97
  state: working_tree
  inputs:
  - path: data/identifier_authorities/ontology.json
    sha256: 62778b0fc25173af80c79041830e7fd04f34025aa782cd1f072e37aabb14cc48
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 18ae3d0007bd2e12d8848689791001efd6582541b2e8d395af585cb37f1c8a42
    role: context
  - path: data/pathways/glyoxylate-assimilation.yaml
    sha256: b28136c61fae7fcf2b9673d176e74d0c001b6cfedeab652ba75ab4ac01aa01e5
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: c635a91493a53b519ed2c8e0f825adcca320e1c8d96ef87a69459c8a2cb14937
    role: context
  - path: docs/CURATION.md
    sha256: 408f7c7705b4e6d667b513920e4c39612162d549e0c2666d85bfd53b2c2687f7
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 3af37b2e92b0103da74bc462bedda1021c6bd262d3da13c030eb47344d08b61f
    role: context
  - path: docs/record-review-profile.md
    sha256: a3d4b48de5f227515f9b5de12dd172cd1eb626068235b2b2e58bc4f6a5ee567d
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/generated-graph-kgx-audit.json
    sha256: ee045b6ec5256ce52b6d99bb93f38bf814328fee5c62208f55d5389885e4c0c0
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/glyoxylate-curation.md
    sha256: 721d9291ae822ec0a4cf762d8ca7575ebadd2ef1de81275e9afa4941f84c583d
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/glyoxylate-independent-review-audit.json
    sha256: 152632e38fd9cab5a9140e07ab22d40c11255eff48a5b36a1e0f34ca4ed312d1
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/glyoxylate-native-coverage.json
    sha256: 0ae55d84381aea044bda2c5060b7737a7098b2c5700dde19440461a94183721a
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/glyoxylate-protein-projection.json
    sha256: 86f24ad4b7ff69e5bf568281ca9d104cdd13c36a2dcef46a3fe0e53b1f67f160
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/glyoxylate-source-manifest.json
    sha256: 7886446b3418310c18af35ad938da01013d75581a416270ff2fa087c56f73b22
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/glyoxylate-source-projection.json
    sha256: c57429d7f98dc66f43fe0e8819a2a0b6aa8bc402cab44e826ec04b86c95786a0
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/glyoxylate-validation.json
    sha256: f4a25edfd42020b49213dbd80a79cc2cd71f9e247a6024cf5977c7f873f45b82
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/imodulondb-applicability.json
    sha256: dc02de15ecea776c0b50e1a02e4f39eea82e8c87c95d0e2d246c0651005d7433
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/imodulondb-offline-replay.json
    sha256: 5bc6ed355358b6c9c83c754e9037fa0e876ea2b6e4909c0c08ba3c2a13b9f2c0
    role: context
  - path: research/pathway_additions/2026-10-11-next-206/initial-integration-receipt.json
    sha256: 73fcb487b20ac73e5459105e218abdd3de36befb503adeee5522e375ae9469ff
    role: context
  - path: src/pathwaymech/schema.py
    sha256: f006e5b99cedd91b57a2c5fb938315a84b68822586d1602d4df9ccfdc851e98c
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: ffa1107da83c8ff173833662e78ba73c779bbab9f2da33cea993b614e99d6345
    role: context
targets:
- target_id: MetaCyc:PWY-5744
  path: data/pathways/glyoxylate-assimilation.yaml
  label: glyoxylate assimilation
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glyoxylate-assimilation.yaml
    role: maintained_record
scope:
  description: Full scientific assessment of one frozen target and its edge-level
    original evidence.
  selection: Exact target SHA256 b28136c61fae7fcf2b9673d176e74d0c001b6cfedeab652ba75ab4ac01aa01e5.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-5744
  exclusions:
  - target: Other cohort records and corpus-wide scientific completeness
    reason: Outside this individual independent review.
checks:
- check_id: inspect
  name: Canonical initial and final expanded input inspection
  command: PYTHONPATH=src .venv/bin/python scripts/record_review.py inspect --targets
    /private/tmp/pathwaymech-glyoxylate-independent-review/targets.json --input research/pathway_additions/2026-10-11-next-206/glyoxylate-curation.md
    --input research/pathway_additions/2026-10-11-next-206/glyoxylate-native-coverage.json
    --input research/pathway_additions/2026-10-11-next-206/glyoxylate-protein-projection.json
    --input research/pathway_additions/2026-10-11-next-206/glyoxylate-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-206/glyoxylate-source-projection.json
    --input research/pathway_additions/2026-10-11-next-206/glyoxylate-validation.json
    --input research/pathway_additions/2026-10-11-next-206/glyoxylate-independent-review-audit.json
    --input research/pathway_additions/2026-10-11-next-206/imodulondb-applicability.json
    --input research/pathway_additions/2026-10-11-next-206/imodulondb-offline-replay.json
    --input research/pathway_additions/2026-10-11-next-206/initial-integration-receipt.json
    --input research/pathway_additions/2026-10-11-next-206/generated-graph-kgx-audit.json
    --input docs/CURATION.md --input docs/HARMONIZATION.md --input docs/CAUSAL_GRAPHS.md
    --input docs/record-review-profile.md --input src/pathwaymech/schema.py --input
    src/pathwaymech/schema/pathwaymech.yaml --input data/identifier_authorities/ontology.json
    --input data/identifier_authorities/sources.json
  status: passed
  required: true
  summary: Initial inspection preceded assessment. Final expanded inspection confirmed
    all 12 initial input hashes unchanged and captured the sealed initial integration
    and graph receipts. A first attempt used a nonexistent ontologies.json filename
    and was corrected to the actual ontology.json; the target capture itself was unchanged.
  target_ids:
  - MetaCyc:PWY-5744
  exit_code: 0
- check_id: independent-replay
  name: Independent original-source and chemistry replay
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    .venv/bin/python /private/tmp/pathwaymech-glyoxylate-independent-review/replay.py
  status: passed
  required: true
  summary: 'Actual reviewer session 50825 exit 0: 79 original bodies rehashed, 220499
    RDF nodes parsed, all 13 directed equations, 54 chemical sides, 13 atom/charge
    balances and 14 material-flow links passed. Protein-scaffold cancellation is explicit
    for the two carrier reactions. Evidence prose was assessed separately.'
  target_ids:
  - MetaCyc:PWY-5744
  exit_code: 0
- check_id: stereo
  name: Independent native/current stereochemistry comparison
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache uv run --offline
    --no-project --with rdkit python (original InChI comparison)
  status: passed
  required: true
  summary: Actual reviewer session 41340 exit 0. The native CPD-9409 acyl stereocenters
    differ from current CHEBI:75634; primary Figure 1 and 2008 chemistry support the
    selected form. CPD-627 shares S acyl stereochemistry with CHEBI:58668 but leaves
    CoA stereocenters unspecified.
  target_ids:
  - MetaCyc:PWY-5744
  exit_code: 0
- check_id: root-render
  name: Coordinated render
  command: PYTHONPATH=/private/tmp/pathwaymech-next-206-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just render-pages
  status: passed
  required: true
  summary: Actual renderer exited 0 for all 209 records.
  target_ids:
  - MetaCyc:PWY-5744
  exit_code: 0
- check_id: root-validate
  name: Coordinated validate
  command: PYTHONPATH=/private/tmp/pathwaymech-next-206-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just validate
  status: passed
  required: true
  summary: 'Actual full corpus QC exited 0: 209 native/closed/identifier-checked records,
    12566 evidence blocks, 317 valid histories, 30 sources, six documentation files
    and current pages.'
  target_ids:
  - MetaCyc:PWY-5744
  exit_code: 0
- check_id: root-test
  name: Coordinated test
  command: PYTHONPATH=/private/tmp/pathwaymech-next-206-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just test
  status: passed
  required: true
  summary: 'Actual full child command exited 0: 1059 passed, 3 skipped and 3 warnings
    in 406.23 seconds. The archived log and digest were independently inspected. This
    is the initial pre-correction result.'
  target_ids:
  - MetaCyc:PWY-5744
  exit_code: 0
- check_id: root-lint
  name: Coordinated lint
  command: PYTHONPATH=/private/tmp/pathwaymech-next-206-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just lint
  status: passed
  required: true
  summary: Actual lint command exited 0, All checks passed.
  target_ids:
  - MetaCyc:PWY-5744
  exit_code: 0
- check_id: root-identifiers
  name: Coordinated identifiers
  command: PYTHONPATH=/private/tmp/pathwaymech-next-206-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just check-identifiers
  status: passed
  required: true
  summary: Actual identifier/name-policy gate exited 0 for all 209 records.
  target_ids:
  - MetaCyc:PWY-5744
  exit_code: 0
- check_id: root-kgx
  name: Coordinated kgx
  command: PYTHONPATH=/private/tmp/pathwaymech-next-206-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just kgx-export --output-dir
    /private/tmp/pathwaymech-next-206-kgx
  status: passed
  required: true
  summary: Actual separate CLI export exited 0 for 209 records; the sealed artifact
    audit preserves all 107 target edges and 184 evidence blocks.
  target_ids:
  - MetaCyc:PWY-5744
  exit_code: 0
- check_id: root-diff
  name: Coordinated diff
  command: PYTHONPATH=/private/tmp/pathwaymech-next-206-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache git diff --check
  status: passed
  required: true
  summary: Actual git diff --check exited 0. This check does not by itself cover untracked
    additions.
  target_ids:
  - MetaCyc:PWY-5744
  exit_code: 0
- check_id: imodulondb
  name: Exact organism dataset applicability
  command: Inspect retained canonical-client inventory and imodulondb-applicability.json
  status: not_applicable
  required: true
  summary: Chloroflexus is absent from the inspected 20-organism/28-dataset inventory.
    Console availability failed before requests; unchanged direct-client acquisition
    and offline parsing succeeded. No negative expression or pathway inference.
  target_ids:
  - MetaCyc:PWY-5744
evidence:
- evidence_id: native
  kind: database
  reference: MetaCyc:PWY-5744 and 13 original reaction XML objects
  locator: reaction-list; left; right; reaction-direction; enzymatic-reaction; dblink
  accessed_at: '2026-10-11T10:17:02Z'
  support: supports
  summary: All native members and physiological directions independently inspected.
    The exact second cycle includes the shared acetyl-CoA-to-propionyl-CoA module
    and all five glyoxylate-assimilation transformations.
- evidence_id: primary-cycle
  kind: primary_source
  reference: PMID:19955419 / PMC2795484
  locator: Results sections 2–7; Discussion sections 8–14; Methods section 15; independently
    viewed Figure 1
  accessed_at: '2026-10-11T10:17:02Z'
  support: supports
  summary: Four-enzyme reconstitution, complete boundary, specific CoA ester identities,
    assemblies, kinetics and separate OK-70/J-10 scopes support the record. Figure
    1 explicitly names the selected (2R,3S) methylmalyl form.
  snapshot_sha256: ef7bbdc7b8ebc8cd62ae4d586fe953a767fdce2865900f742e43336381fde7b1
- evidence_id: primary-enzymes
  kind: primary_source
  reference: PMID:11948153; PMID:18065535; PMID:24206647; PMID:12374834; PMID:36535006;
    PMID:38572988
  locator: Exact independently inspected Results/Methods and source-body hashes in
    glyoxylate-independent-review-audit.json
  accessed_at: '2026-10-11T10:17:02Z'
  support: supports
  summary: Primary MCR, Mch, Mcl, Mct, Meh and fused BC/BCCP results were checked
    with their strain and construct limits. Ion dependence versus mere assay presence
    and uncertain oligomers are distinguished.
- evidence_id: pcs
  kind: primary_source
  reference: PMID:11821399
  locator: 'Original author-paper web rendering: Methods, Cell Material and Characterization
    of the Enzyme; Results, Molecular Properties, Stoichiometry, Catalytic Properties
    and Possible Intermediates'
  accessed_at: '2026-10-11T10:17:02Z'
  support: supports
  summary: The original paper supports OK-70 PCS activity, NADPH specificity, ATP
    to AMP/PPi, K/Mg omission and add-back, and uncertain trimer/tetramer mass. Compound
    X is likely, not conclusively identified, 3-hydroxypropionyl-CoA. No local original-byte
    hash is claimed.
- evidence_id: protein
  kind: database
  reference: Nine original current UniProt entries; NCBIProtein:AAL47820.2; native
    complex/monomer XML
  locator: Exact sequence, organism, comments, evidence codes, indexed references
    and component coefficients
  accessed_at: '2026-10-11T10:17:02Z'
  support: supports
  summary: All selected entry identities and explicit inference tiers inspected. Original
    1822-residue AAL47820.2 sequence exactly matches Q8VRG6, with OK-70-fl source
    qualifier. No arbitrary native/current strain identity or whole-ACC stoichiometry
    is inferred.
- evidence_id: replay
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-206/glyoxylate-independent-review-audit.json
  locator: original_source_replay; stereochemistry_replay; sequence_bridge; deduplication
  accessed_at: '2026-10-11T10:17:02Z'
  support: supports
  summary: Independent complete-source replay and scientific assessment preserve all
    source conflicts and the one bounded provenance finding.
  snapshot_sha256: 152632e38fd9cab5a9140e07ab22d40c11255eff48a5b36a1e0f34ca4ed312d1
- evidence_id: wrong-native-assertion
  kind: database
  reference: MetaCyc:RXN-8965
  locator: Reaction[@detail="full"]/left; right; reaction-direction
  accessed_at: '2026-10-11T10:17:02Z'
  support: refutes
  summary: The native object contains CPD-627 on the left and CPD-14205 plus WATER
    on the right, with RIGHT-TO-LEFT direction. It does not describe biotin carboxyl
    transfer. Only the RXN-8965 no-Rhea-cross-reference fallback is wrong; RXN0-5055
    correctly uses the carboxyl-transfer text.
  snapshot_sha256: 80aeedc50b829d6b556452268c16265d38602828453e8214d7445f5071c4f9d2
- evidence_id: gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-206/initial-integration-receipt.json
  locator: gates; test_summary; supporting_receipts
  accessed_at: '2026-10-11T10:17:02Z'
  support: supports
  summary: All seven initial coordinated commands passed. Each archived log was read
    and rehashed. Programmatic graph/KGX checks preserve the complete target and baseline;
    these results do not establish scientific truth.
  snapshot_sha256: 73fcb487b20ac73e5459105e218abdd3de36befb503adeee5522e375ae9469ff
- evidence_id: context
  kind: database
  reference: research/pathway_additions/2026-10-11-next-206/imodulondb-applicability.json
  locator: covered organism/dataset inventory and offline-parser receipt
  accessed_at: '2026-10-11T10:17:02Z'
  support: context_only
  summary: Chloroflexus is not represented in this inventory; transcriptomic context
    is not applicable.
  snapshot_sha256: dc02de15ecea776c0b50e1a02e4f39eea82e8c87c95d0e2d246c0651005d7433
assessments:
- assessment_id: identity
  area: identity
  topic: Complete native second-cycle boundary
  outcome: supported
  summary: The record retains all 13 native reaction objects and regenerates acetyl-CoA
    while converting glyoxylate plus CO2 to pyruvate. Prior scout and hidden/ignored-inclusive
    searches distinguish this from first-cycle glyoxylate production and the whole
    bicycle. Shared precursor reactions do not make it a duplicate.
  target_ids:
  - MetaCyc:PWY-5744
  evidence_ids:
  - native
  - primary-cycle
  - replay
- assessment_id: chemistry
  area: grounding
  topic: Directed chemistry, carrier forms and stereochemistry
  outcome: supported
  summary: All 54 sides, coefficients, 13 balances and 14 shared-intermediate links
    pass independent original-RDF replay. Whole protein carrier states are retained.
    The native CPD-9409 stereochemical conflict is explicit; the primary figure and
    Mch study support the selected current methylmalyl form. Native CPD-627 unspecified
    CoA stereocenters are not silently treated as exact identity.
  target_ids:
  - MetaCyc:PWY-5744
  evidence_ids:
  - native
  - primary-cycle
  - primary-enzymes
  - replay
- assessment_id: organism
  area: evidence
  topic: Strain and experimental identity
  outcome: supported
  summary: Species-level scope is appropriate with explicit OK-70 preparations and
    J-10 genome/construct assignments. Reviewed and unreviewed protein evidence is
    graded; exact PCS sequence identity was independently checked. Similarity does
    not become direct strain-specific experimental evidence.
  target_ids:
  - MetaCyc:PWY-5744
  evidence_ids:
  - protein
  - primary-cycle
  - primary-enzymes
  - pcs
  dimensions:
  - name: taxon_scope
    value: NCBITaxon:1108 with distinct OK-70-fl and J-10-fl source scopes
    definition: The record does not claim all experimental proteins came from a single
      strain.
    evidence_ids:
    - primary-cycle
    - protein
- assessment_id: assemblies
  area: evidence
  topic: Enzymes, assemblies, cofactors and regulatory limits
  outcome: supported
  summary: MCR dimer, Mcl hexamer, Mch/Mct/Meh dimers and fused BC/BCCP tetramer have
    source-specific support. PCS remains a functional role with trimer/tetramer uncertainty,
    and no exact whole ACC assembly is invented. Primary K/Mg dependence, similarity-based
    CT zinc, metal stimulation and assay-only inhibition remain distinct. No pathway-specific
    transcriptional regulator is inferred from gene clustering.
  target_ids:
  - MetaCyc:PWY-5744
  evidence_ids:
  - primary-enzymes
  - pcs
  - protein
- assessment_id: export
  area: provenance
  topic: Evidence and generated graph preservation
  outcome: supported
  summary: The sealed programmatic audit preserves all 107 target edges and 184 evidence
    blocks, categories, endpoints and references across YAML, SVG and actual CLI KGX.
    No browser visual inspection is claimed. All initial gates passed.
  target_ids:
  - MetaCyc:PWY-5744
  evidence_ids:
  - gates
- assessment_id: context-assessment
  area: evidence
  topic: iModulonDB applicability
  outcome: not_applicable
  summary: The retained dataset inventory has no Chloroflexus coverage. This is an
    applicability limit, not evidence against the pathway.
  target_ids:
  - MetaCyc:PWY-5744
  evidence_ids:
  - context
- assessment_id: native-attribution
  area: provenance
  topic: Exact native hydration assertion
  outcome: concern
  summary: glyox-edge-066 evidence[1] incorrectly describes RXN-8965 as carboxyl transfer.
    The target reaction and chemical edges are correct, but the source assertion and
    locator need a bounded correction.
  target_ids:
  - MetaCyc:PWY-5744
  evidence_ids:
  - wrong-native-assertion
  - replay
findings:
- finding_id: f-native-hydration-attribution
  issue_key: glyoxylate-rxn8965-native-hydration-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Native hydration evidence describes an unrelated carboxyl-transfer reaction
  description: 'glyox-edge-066 evidence[1] cites MetaCyc:RXN-8965 but its source_assertion
    describes transfer from protein-bound carboxybiotin to acetyl-CoA. The original
    RXN-8965 stores CPD-627 on the left, CPD-14205 plus WATER on the right, and RIGHT-TO-LEFT
    physiological direction: mesaconyl-C4-CoA hydration to (S)-citramalyl-CoA. A no-Rhea-cross-reference
    fallback copied text appropriate to RXN0-5055. Independent inspection of all 13
    originals found this one affected assertion. Keep the correct selected RHEA:38273
    chemistry and separate master 38271 identity evidence, replacing only the native
    assertion and adding reaction-direction to its locator.'
  target_ids:
  - MetaCyc:PWY-5744
  field_paths:
  - mechanistic_edges[id=glyox-edge-066].evidence[1].source_assertion
  - mechanistic_edges[id=glyox-edge-066].evidence[1].source_locator
  evidence_ids:
  - wrong-native-assertion
  - native
  - replay
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glyoxylate-assimilation.yaml
    role: maintained_record
  rule_id: review-yaml-record structured source assertion and exact locator correspondence
  native_severity: minor
  normalization_reason: Bounded provenance-copy defect; pathway identity, selected
    reaction direction, chemical endpoints and other supporting evidence remain correct.
actions:
- action_id: correct-native-hydration
  description: Preserve the initial review and input bytes, correct the native RXN-8965
    source assertion and locator, update its projection and add a targeted no-xref
    source guard.
  finding_ids:
  - f-native-hydration-attribution
  target_ids:
  - MetaCyc:PWY-5744
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/glyoxylate-assimilation.yaml
    role: maintained_record
  acceptance_checks:
  - Archive all initial inspected inputs before mutation.
  - Native assertion explicitly describes CPD-627 versus CPD-14205 plus WATER and
    RIGHT-TO-LEFT hydration; separate current Rhea identity evidence remains intact.
  - Regression distinguishes RXN-8965 hydration from RXN0-5055 carboxyl transfer;
    replay all chemical/source/schema/export checks and applicable shared gates.
  - Save an immutable successor with the same issue key and exact previous occurrence.
limitations:
- PCS original full paper was inspected through the author-copy web rendering; no
  stable downloaded original-byte digest is claimed.
- The precise strain and construct limits, inferred CT subunit roles/zinc, uncertain
  PCS oligomer count and MCR intermediate trapping remain explicit; deterministic
  replay does not resolve these experimentally.
- This is the initial pre-correction observation, not acceptance of future edited
  bytes.
- Generated SVG/KGX evidence was checked programmatically; no browser interaction
  or visual rendering inspection is claimed.
notes:
- All 12 initially captured input hashes were rechecked unchanged before expanded
  inspection.
- The source assertion defect does not invalidate the selected hydration chemistry
  or imply another pathway gap.
- The external ordinary-python attempt lacked PyYAML; the repository environment was
  used successfully for the subsequent bounded sequence/metadata check.
links:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2795484/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2238226/
```

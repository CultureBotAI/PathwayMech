# Independent review of allantoin degradation to glyoxylate III

- Review: 20261011T054326Z-allantoin-glyoxylate-iii-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T05:34:40Z
- Finished UTC: 2026-10-11T05:43:26.055714Z
- Reviewer: Codex independent reviewer (/root/verify_graph_publication) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The full native four-reaction AllB/AllC/AllE/AllA route is supported within explicit strain, preparation, annotation and assembly limits. Independent replay verifies43 source bodies,4 direction families,17 chemical sides,4 balances and41 edges/80 evidence. No actionable findings.

## Scope And Provenance

Complete one-record review:21 participants,4 reactions,41 mechanistic edges,80 evidence and23 references; primary/native claims independently inspected.

Selection: Exact frozen MetaCyc:PWY-5705 SHA256 1fe731570ceb2038b0b153686be184c99afbd82ab6ba9a9516694b2277de1b37
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 0919419d95f65d097e867c6d8452f1ca552f550b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-5705 | data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml | maintained | allantoin degradation to glyoxylate III |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Initial and final canonical input inspection | passed | True | MetaCyc:PWY-5705 | Initial inspect preceded assessment at 2026-10-11T05:34:40Z; final inspect rechecked every 18 original input hash without changes. Newly final shared receipts, authority snapshots and generated inputs were read and assessed. Actual final inspect exit0. |
| Independent original source, chemistry and KGX replay | passed | True | MetaCyc:PWY-5705 | Actual reviewer session57209 terminal0, completed2026-10-11T05:36:17Z. Independently parsed full Rhea RDF without author helper: 43 original body hashes,23 reference bodies,4 master/directed bridges,17 chemical sides,4 atom/charge balances,10 native ChEBI/InChI crosswalks,4 current protein identities,41 KGX edges/80 evidence pass. |
| Actual generated HTML/SVG/evidence parity | passed | True | MetaCyc:PWY-5705 | Actual terminal0 at2026-10-11T05:38:02Z. All41 graph triples and80 complete evidence assertion/locator pairs match YAML; all graph/evidence anchors resolve. Page SHA256 ac67a98bcda803677cba6c4807b19f4b676aa32681d100481f31d9266cd4bd4d. Programmatic inspection only. |
| Exact structured expression-context source recheck | passed | False | MetaCyc:PWY-5705 | Console runner unavailable; root used unchanged canonical direct client and offline parser replay. Reviewer independently rehashed26 original bodies and read component3 six-gene table and exact allA/allB/allC/allE locus search responses. Computational context only; no negative membership inference. |
| Final full-corpus render | passed | True | MetaCyc:PWY-5705 | Delegated root actual exit0, 2026-10-11T05:34:56.977375+00:00 to 2026-10-11T05:35:48.512628+00:00. Actual log inspected: /private/tmp/pathwaymech-next-192-final-render.log SHA256 c9360c998fc556281b8d7141b0df5a75232fa20fb415cb788b57473a3682c67d. |
| Final full-corpus validate | passed | True | MetaCyc:PWY-5705 | Delegated root actual exit0, 2026-10-11T05:35:48.514283+00:00 to 2026-10-11T05:37:55.477094+00:00. Actual log inspected: /private/tmp/pathwaymech-next-192-final-validate.log SHA256 a196afe7a0a514170f83e75e3a4bb123db4e215d92418210456ff4b077d5fde5. |
| Final full-corpus test | passed | True | MetaCyc:PWY-5705 | Delegated root actual exit0, 2026-10-11T05:35:48.514598+00:00 to 2026-10-11T05:41:25.076217+00:00. Actual log inspected: /private/tmp/pathwaymech-next-192-final-test.log SHA256 87a0802c44e6f18ee33c9e1a4b682cea44d453d1a2b487250937531beecd3511. =========== 1050 passed, 3 skipped, 3 warnings in 334.54s (0:05:34) ============ |
| Final full-corpus lint | passed | True | MetaCyc:PWY-5705 | Delegated root actual exit0, 2026-10-11T05:35:48.514843+00:00 to 2026-10-11T05:35:48.824868+00:00. Actual log inspected: /private/tmp/pathwaymech-next-192-final-lint.log SHA256 df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41. |
| Final full-corpus identifiers | passed | True | MetaCyc:PWY-5705 | Delegated root actual exit0, 2026-10-11T05:35:48.825421+00:00 to 2026-10-11T05:36:12.466098+00:00. Actual log inspected: /private/tmp/pathwaymech-next-192-final-identifiers.log SHA256 352d595d204d38b6b4ad9a4e7487331be258189a62cf08cda5e7a15a250fd3da. |
| Final full-corpus kgx | passed | True | MetaCyc:PWY-5705 | Delegated root actual exit0, 2026-10-11T05:36:12.466657+00:00 to 2026-10-11T05:36:33.179033+00:00. Actual log inspected: /private/tmp/pathwaymech-next-192-final-kgx.log SHA256 523e1c2079d278abec2dbc2d02afff4f974efed80415ef854c834d0f9b2e9d92. |
| Final full-corpus diff | passed | True | MetaCyc:PWY-5705 | Delegated root actual exit0, 2026-10-11T05:36:33.179451+00:00 to 2026-10-11T05:36:33.483023+00:00. Actual log inspected: /private/tmp/pathwaymech-next-192-final-diff.log SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. |

## Scientific And Domain Assessments

### Complete exact native four-reaction boundary

identity: supported. Targets: MetaCyc:PWY-5705.

PWY5705 includes nested three-stepPWY5698 plus AllA; the native hierarchy is not truncated. Existing oxamateIV and yeast glyoxylateI are mechanistically distinct.

### Direction families, charge, stereo and balance

consistency: supported. Targets: MetaCyc:PWY-5705.

Four Rhea master/directed bridges and17 chemical sides match the source. AllC legacyxref conflict is disclosed and separately normalized using current evidence. All4 balances pass.

### Assemblies, roles and cofactors

evidence: supported. Targets: MetaCyc:PWY-5705.

AllB tetramer/AllC dimer native identities verified. AllE annotation monomer and AllA inferred structural dimer limitations remain visible; enables avoids invented catalyst complex identity. Alternative metal conditions are not simultaneous occupancy.

### Organism and experimental physiology

scope: supported. Targets: MetaCyc:PWY-5705.

K12 derivative genetic and purified-protein observations remain separate from MG1655 annotations. AllA activity is not essentiality, sole-carbon growth or constitutive species-wide flux.

### Exact nearest-source attribution and rendering

provenance: supported. Targets: MetaCyc:PWY-5705.

All41 edges/80 evidence items have inspected native, primary or explicitly qualified annotation support. Native ordering versus normalized chemical identity is separately grounded; generated graph/evidence preserve source bytes.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e-target | data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml; Entire YAML;41 edges and23 references | supports | Complete record reviewed, with80 evidence items independently scoped to inspected sources. |
| e-native | https://pathway.yeastgenome.org/getxml?META:PWY-5705; Pathway/common-name; nested PWY-5698 and terminal UREIDOGLYCOLATE-LYASE-RXN; ordering and reaction layouts | supports | Complete four-reaction native boundary is correct. Shared first three reactions with oxamate IV do not duplicate terminal urea/glyoxylate branch. Yeast routeI has different allantoicase cleavage. |
| e-rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Masters17029,27485,25241,11304 directionalReaction; directed17030,27486,25242,11305 substrate/product/contains/compound triples | supports | All17 selected sides, coefficients, stereo/charge and4 balances replayed. Native obsolete AllC13594 does not ground the current equation; separately inspected P77425/Rhea27485 does. |
| e-allA | https://pmc.ncbi.nlm.nih.gov/articles/PMC3793230/; PMID24107613 full Results,Fig2A-C,Methods/JW0493 clone | supports | Purified AllA releases urea, not ammonia; EDTA removes activity and nickel restores it. Glyoxylate hydration does not settle microscopic water mechanism. Source-specific recombinant scope is retained. |
| e-physiology | https://pmc.ncbi.nlm.nih.gov/articles/PMC94204/; PMID10601204 full HTML; sec13,JA174 allA deletion, ECL1 growth | supports | K12 derivative anaerobic allantoin nitrogen use with xylose; allA deletion loses cleavage activity without losing growth. Record does not claim sole-carbon growth, essentiality or universal strain flux. |
| e-allB-assembly | https://pmc.ncbi.nlm.nih.gov/articles/PMC94829/; PMID11092864 full relevant Results/Methods;Figs3B and4;Table2 | supports | Purified AllB tetramer is supported by gel filtration/crosslinking and50.5kDa subunits. Metal stimulation is preparation-specific. |
| e-allB-metal | https://pmc.ncbi.nlm.nih.gov/articles/PMC141845/; PMID12486048 full relevant Results/Discussion;Enantioselectivity/Fig6 | supports | Zn physiological preference is inference. Co/Ni reconstitution and Co-associated slowerR turnover are qualified; S route remains exact, with no requirement for simultaneous alternative metals. |
| e-abstracts | PMID:17362992; PMID:20038185; PMID:19935661; Retained full indexed abstracts only, in primary-assemblies-metals.json | supports | AllC dimer/twoZn older structural evidence, modernS-ureidoglycine true product, and EcAllE Mn-dependent inversion toS-ureidoglycolate are supported at actual inspected abstract scope. No unavailable full text is claimed read. |
| e-proteins | research/pathway_additions/2026-10-11-next-192/allantoin-independent-review-audit.json; Native CPLX-64/CPLX-7524 components;UniProtP77671/P77425/P75713/P77731 comments,evidence,xrefs;PDB1XSQ assembly | supports | AllB4 and AllC2 components verified; AllE monomer is annotation inference; AllA dimer is structural/annotation support and uses enables. Alternative cofactors and AllC/AllE localization tiers are explicit. |
| e-context | research/pathway_additions/2026-10-11-next-192/imodulondb-source-manifest.json; 26 original source response hashes;component3 table;four exact locus search responses | supports | Computational MG1655 expression context only. Search hits do not establish catalysis, pathway identity or absent membership. |
| e-late | https://pmc.ncbi.nlm.nih.gov/articles/PMC12535856/; PMID41016821 Abstract,Introduction/Fig1,Methods | supports | 2025 study addresses oxamate allF/ArcA regulation inMC4100 and confirms AllA glyoxylate/urea branch distinction. Retained2023PMC10163214 fullXML AllB/GlxK regulation was also independently read. Neither extends this native catalytic boundary. |
| e-integration | research/pathway_additions/2026-10-11-next-192/integration-receipt.json; All actual final command receipts and graph/baseline audits | supports | Required full-corpus checks pass with exact logs; separate scientific evidence remains necessary. Prior192 records/pages and all8713 baseline edges are retained. |

## Limits And Additional Notes

- PMID17362992,20038185,19935661 were inspected as complete indexed abstracts, not unavailable full papers. Claims retain their exact evidence tier.
- AllE monomer is curator inference. AllA dimer uses annotation and crystallographic biological-assembly support rather than an independent solution oligomer measurement.
- Metal preference and occupancy depend on purified preparation. AllB physiological Zn and alternative Ni/Co/Mn, AllC Zn/Mn, AllE Mn/Co and AllA nickel activity are qualified, not simultaneous-metal requirements.
- K12 derivative experiments do not establish universal MG1655/species-wide native flux; allA deletion phenotype is distinguished from growth necessity.
- iModulonDB runner was unavailable; unchanged direct canonical client and independently rehashed responses supply computational context only. No absence-of-membership inference.
- No available browser surface was used. Actual generated HTML/SVG/KGX parsing is a structural/content check, not visual browser QA.
- All 18 initial captured input hashes remain unchanged. Final shared receipts and correct authority snapshot paths were added and inspected before save.
- Reviewer source audit truthfully retains its earlier pending-full-gates timestamp; this final bundle adds the subsequently completed actual shared checks.
- Scientific source replay is independent of the author helper. Full corpus commands were executed by root and independently inspected through actual logs/digests.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T054326Z-allantoin-glyoxylate-iii-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent review of allantoin degradation to glyoxylate III
started_at: '2026-10-11T05:34:40Z'
finished_at: '2026-10-11T05:43:26.055714Z'
reviewer:
  identity: Codex independent reviewer (/root/verify_graph_publication)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Reviewer authored separate adenine/adenosine salvageI in this
    cohort, not this Allantoin record. Independently read entire target and original
    primary/native bodies, replayed chemistry/identity and generated outputs without
    editing this target.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The full native four-reaction AllB/AllC/AllE/AllA route is supported within
  explicit strain, preparation, annotation and assembly limits. Independent replay
  verifies43 source bodies,4 direction families,17 chemical sides,4 balances and41
  edges/80 evidence. No actionable findings.
source:
  git_revision: 0919419d95f65d097e867c6d8452f1ca552f550b
  state: working_tree
  inputs:
  - path: .claude/skills/add-pathway/SKILL.md
    sha256: 296ab1a206afa3aa9b487eae7f5f8d836c09001a4ce9ee8016c36abe198cdc0d
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: CLAUDE.md
    sha256: c067d99547f9e9e9a6edb892d71126b6765239348d0021b907f3102907a4cf00
    role: context
  - path: conf/identifier_sources.json
    sha256: 0a9935940ece68b9dc9d01e53bbb686adb9bb88761c0d4a8ed51222662314cc2
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: ee16d51dd29aa1691fff45c143fa1a1a4c22c58b1058e3e264e34241bb100e0d
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 6d0fba1a3e20b0bf97732406e3a65cb29feaa0ecafd3f402c76ff3e3e2d7d1a0
    role: context
  - path: data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml
    sha256: 1fe731570ceb2038b0b153686be184c99afbd82ab6ba9a9516694b2277de1b37
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
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 6d3df7c8fb17835c316a5f37a59c0ff7e61541bbb0781d4dd62ee6ec5fce7df2
    role: context
  - path: pages/records/MetaCyc_PWY-5705.html
    sha256: ac67a98bcda803677cba6c4807b19f4b676aa32681d100481f31d9266cd4bd4d
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/allantoin-duplicate-disposition.json
    sha256: 35ecef2409f8cfb08ffa33f4b63872d95f636edb1807e71c6f119177d1727ae8
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-curation.md
    sha256: b74176f7239a93a889708a3c2fde006372ebff6807535d4ecd5d27766b5435f4
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-dedup.json
    sha256: cd9741b7b391fa0d460745a3884156ca3728b5bf94428c181bba3c6ce5ca022b
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-identifiers.json
    sha256: 885e846469f126469a233446be27f15acf0bd92c325ee51bccfd7fbc8cc14c51
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-replay.py
    sha256: 5ed53cecc47f8a1f2f38f1a8d6e36a845385beb326b2c5a3fd5020df2ff9e340
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-source-manifest.json
    sha256: 562c95a107c5614f0ab9424894a288864f8f233c0f6d49915ada971a1d9e19c5
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-source-projection.json
    sha256: 3469a98a7b1ac980a7df72f5b668d3255416a12fdd0ec5ad59795c69548b9348
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-validation.json
    sha256: 987c05e33ebc903946b67bb298bc9b915f44773f70a6723e172a1979777935c4
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/allantoin-independent-review-audit.json
    sha256: 099227d9b204228a98417f8324dc9e103dcb35da0054af47e44ea386b6ef67de
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/authority-integration.json
    sha256: 31b4563e05bb824f024f3548f78e4f5e5fa6b2e6b775fcf638574a8ffda7ee4d
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/authority-source-inspection.json
    sha256: 914e2cebbd8f869b39c27d42403b8dd2ca3ac5f0e459d5b405dfcfec7655700c
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/baseline-preservation.json
    sha256: 2a3d92c4aea373d3dcf1aa8d4140bf367027b859e46f19a18903b76813d0a934
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/chemical-entity-independent-audit.json
    sha256: cecf2e1e815be86a3730742a46d378dfa466664c5ca4ab28509f010ba1be7ab2
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/generated-graph-kgx-audit.json
    sha256: 61df1ae5af025bfedce15c11cdcff1da7283c32c77d207233b9af7f18fe7340b
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/imodulondb-context.json
    sha256: 558b20bcf108fdcb7604177f8a8cc83c3dbc30d28b1bc4c43ad467a4dc6a894d
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/imodulondb-parser-replay.json
    sha256: 3e55fee75d36a27a3b2d78d0e2a423b1753f00f4fc0776bfbeeb58181a80760d
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/imodulondb-runner-availability.json
    sha256: 324fd5ef0fcfea2b301cdac3791bbb4a507682897f7eca35406ffa7de3db6fa5
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/imodulondb-source-manifest.json
    sha256: 261292c60259cafc66bc8cb82de6738d6c819fb7d50cde184f2c3d8ecad3b4f7
    role: context
  - path: research/pathway_additions/2026-10-11-next-192/integration-receipt.json
    sha256: ce0c463e3aab7995f7ee06112969a0fd6df89d7eb990b9912444b323e89cf212
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/pathwaymech/graph_view.py
    sha256: 3f133d2251dd965a4152cdc91b9169e75776c3615bd80c7a5a679abe27e4f86a
    role: context
  - path: src/pathwaymech/kgx.py
    sha256: 574dbe45598843d9e6a2e751f40990bb7f342e978b487ddad882b8b11a71dacb
    role: context
  - path: src/pathwaymech/schema.py
    sha256: f006e5b99cedd91b57a2c5fb938315a84b68822586d1602d4df9ccfdc851e98c
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: ffa1107da83c8ff173833662e78ba73c779bbab9f2da33cea993b614e99d6345
    role: context
targets:
- target_id: MetaCyc:PWY-5705
  path: data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml
  label: allantoin degradation to glyoxylate III
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml
    role: Maintained scientific record; generated page and KGX are outputs.
scope:
  description: Complete one-record review:21 participants,4 reactions,41 mechanistic
    edges,80 evidence and23 references; primary/native claims independently inspected.
  selection: Exact frozen MetaCyc:PWY-5705 SHA256 1fe731570ceb2038b0b153686be184c99afbd82ab6ba9a9516694b2277de1b37
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-5705
  exclusions:
  - target: Other pathway scientific claims and corpus exhaustion
    reason: Outside one-record scientific scope.
checks:
- check_id: governed-inspection
  name: Initial and final canonical input inspection
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 .venv/bin/python
    scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-192-allantoin-review/targets.yaml
    --input .claude/skills/add-pathway/SKILL.md --input .claude/skills/review-yaml-record/SKILL.md
    --input CLAUDE.md --input conf/identifier_sources.json --input data/identifier_authorities/ontology.json
    --input data/identifier_authorities/sources.json --input data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml
    --input docs/CAUSAL_GRAPHS.md --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/record-review-profile.md --input docs/record-reviews.md --input justfile
    --input pages/records/MetaCyc_PWY-5705.html --input research/pathway_additions/2026-10-11-next-192/allantoin-duplicate-disposition.json
    --input research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-curation.md
    --input research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-dedup.json
    --input research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-identifiers.json
    --input research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-replay.py
    --input research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-source-projection.json
    --input research/pathway_additions/2026-10-11-next-192/allantoin-glyoxylate-validation.json
    --input research/pathway_additions/2026-10-11-next-192/allantoin-independent-review-audit.json
    --input research/pathway_additions/2026-10-11-next-192/authority-integration.json
    --input research/pathway_additions/2026-10-11-next-192/authority-source-inspection.json
    --input research/pathway_additions/2026-10-11-next-192/baseline-preservation.json
    --input research/pathway_additions/2026-10-11-next-192/chemical-entity-independent-audit.json
    --input research/pathway_additions/2026-10-11-next-192/generated-graph-kgx-audit.json
    --input research/pathway_additions/2026-10-11-next-192/imodulondb-context.json
    --input research/pathway_additions/2026-10-11-next-192/imodulondb-parser-replay.json
    --input research/pathway_additions/2026-10-11-next-192/imodulondb-runner-availability.json
    --input research/pathway_additions/2026-10-11-next-192/imodulondb-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-192/integration-receipt.json
    --input schema/record_review.yaml --input src/pathwaymech/graph_view.py --input
    src/pathwaymech/kgx.py --input src/pathwaymech/schema.py --input src/pathwaymech/schema/pathwaymech.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Initial inspect preceded assessment at 2026-10-11T05:34:40Z; final inspect
    rechecked every 18 original input hash without changes. Newly final shared receipts,
    authority snapshots and generated inputs were read and assessed. Actual final
    inspect exit0.
  target_ids:
  - MetaCyc:PWY-5705
- check_id: independent-source-replay
  name: Independent original source, chemistry and KGX replay
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 .venv/bin/python
    /private/tmp/pathwaymech-next-192-allantoin-review/replay.py
  status: passed
  required: true
  exit_code: 0
  summary: 'Actual reviewer session57209 terminal0, completed2026-10-11T05:36:17Z.
    Independently parsed full Rhea RDF without author helper: 43 original body hashes,23
    reference bodies,4 master/directed bridges,17 chemical sides,4 atom/charge balances,10
    native ChEBI/InChI crosswalks,4 current protein identities,41 KGX edges/80 evidence
    pass.'
  target_ids:
  - MetaCyc:PWY-5705
- check_id: independent-page-parity
  name: Actual generated HTML/SVG/evidence parity
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 .venv/bin/python
    /private/tmp/pathwaymech-next-192-allantoin-review/page-audit.py
  status: passed
  required: true
  exit_code: 0
  summary: Actual terminal0 at2026-10-11T05:38:02Z. All41 graph triples and80 complete
    evidence assertion/locator pairs match YAML; all graph/evidence anchors resolve.
    Page SHA256 ac67a98bcda803677cba6c4807b19f4b676aa32681d100481f31d9266cd4bd4d.
    Programmatic inspection only.
  target_ids:
  - MetaCyc:PWY-5705
- check_id: context-replay
  name: Exact structured expression-context source recheck
  command: Independent SHA256 and original response-table inspection of all26 iModulonDB
    bodies
  status: passed
  required: false
  exit_code: 0
  summary: Console runner unavailable; root used unchanged canonical direct client
    and offline parser replay. Reviewer independently rehashed26 original bodies and
    read component3 six-gene table and exact allA/allB/allC/allE locus search responses.
    Computational context only; no negative membership inference.
  target_ids:
  - MetaCyc:PWY-5705
- check_id: final-render
  name: Final full-corpus render
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  status: passed
  required: true
  exit_code: 0
  summary: 'Delegated root actual exit0, 2026-10-11T05:34:56.977375+00:00 to 2026-10-11T05:35:48.512628+00:00.
    Actual log inspected: /private/tmp/pathwaymech-next-192-final-render.log SHA256
    c9360c998fc556281b8d7141b0df5a75232fa20fb415cb788b57473a3682c67d.'
  target_ids:
  - MetaCyc:PWY-5705
- check_id: final-validate
  name: Final full-corpus validate
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  status: passed
  required: true
  exit_code: 0
  summary: 'Delegated root actual exit0, 2026-10-11T05:35:48.514283+00:00 to 2026-10-11T05:37:55.477094+00:00.
    Actual log inspected: /private/tmp/pathwaymech-next-192-final-validate.log SHA256
    a196afe7a0a514170f83e75e3a4bb123db4e215d92418210456ff4b077d5fde5.'
  target_ids:
  - MetaCyc:PWY-5705
- check_id: final-test
  name: Final full-corpus test
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  status: passed
  required: true
  exit_code: 0
  summary: 'Delegated root actual exit0, 2026-10-11T05:35:48.514598+00:00 to 2026-10-11T05:41:25.076217+00:00.
    Actual log inspected: /private/tmp/pathwaymech-next-192-final-test.log SHA256
    87a0802c44e6f18ee33c9e1a4b682cea44d453d1a2b487250937531beecd3511. ===========
    1050 passed, 3 skipped, 3 warnings in 334.54s (0:05:34) ============'
  target_ids:
  - MetaCyc:PWY-5705
- check_id: final-lint
  name: Final full-corpus lint
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  status: passed
  required: true
  exit_code: 0
  summary: 'Delegated root actual exit0, 2026-10-11T05:35:48.514843+00:00 to 2026-10-11T05:35:48.824868+00:00.
    Actual log inspected: /private/tmp/pathwaymech-next-192-final-lint.log SHA256
    df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41.'
  target_ids:
  - MetaCyc:PWY-5705
- check_id: final-identifiers
  name: Final full-corpus identifiers
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    check-identifiers
  status: passed
  required: true
  exit_code: 0
  summary: 'Delegated root actual exit0, 2026-10-11T05:35:48.825421+00:00 to 2026-10-11T05:36:12.466098+00:00.
    Actual log inspected: /private/tmp/pathwaymech-next-192-final-identifiers.log
    SHA256 352d595d204d38b6b4ad9a4e7487331be258189a62cf08cda5e7a15a250fd3da.'
  target_ids:
  - MetaCyc:PWY-5705
- check_id: final-kgx
  name: Final full-corpus kgx
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-next-192-kgx
  status: passed
  required: true
  exit_code: 0
  summary: 'Delegated root actual exit0, 2026-10-11T05:36:12.466657+00:00 to 2026-10-11T05:36:33.179033+00:00.
    Actual log inspected: /private/tmp/pathwaymech-next-192-final-kgx.log SHA256 523e1c2079d278abec2dbc2d02afff4f974efed80415ef854c834d0f9b2e9d92.'
  target_ids:
  - MetaCyc:PWY-5705
- check_id: final-diff
  name: Final full-corpus diff
  command: git diff --check
  status: passed
  required: true
  exit_code: 0
  summary: 'Delegated root actual exit0, 2026-10-11T05:36:33.179451+00:00 to 2026-10-11T05:36:33.483023+00:00.
    Actual log inspected: /private/tmp/pathwaymech-next-192-final-diff.log SHA256
    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.'
  target_ids:
  - MetaCyc:PWY-5705
evidence:
- evidence_id: e-target
  kind: record_content
  reference: data/pathways/allantoin-degradation-to-glyoxylate-iii.yaml
  locator: Entire YAML;41 edges and23 references
  accessed_at: '2026-10-11T05:43:26.055714Z'
  support: supports
  summary: Complete record reviewed, with80 evidence items independently scoped to
    inspected sources.
  snapshot_sha256: 1fe731570ceb2038b0b153686be184c99afbd82ab6ba9a9516694b2277de1b37
- evidence_id: e-native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY-5705
  locator: Pathway/common-name; nested PWY-5698 and terminal UREIDOGLYCOLATE-LYASE-RXN;
    ordering and reaction layouts
  accessed_at: '2026-10-11T05:43:26.055714Z'
  support: supports
  summary: Complete four-reaction native boundary is correct. Shared first three reactions
    with oxamate IV do not duplicate terminal urea/glyoxylate branch. Yeast routeI
    has different allantoicase cleavage.
  snapshot_sha256: e13b689bbcc88cc5521fcb520d0ea8c4471f24aed4d38da236948686c1f692e4
- evidence_id: e-rhea
  kind: database
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Masters17029,27485,25241,11304 directionalReaction; directed17030,27486,25242,11305
    substrate/product/contains/compound triples
  accessed_at: '2026-10-11T05:43:26.055714Z'
  support: supports
  summary: All17 selected sides, coefficients, stereo/charge and4 balances replayed.
    Native obsolete AllC13594 does not ground the current equation; separately inspected
    P77425/Rhea27485 does.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: e-allA
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3793230/
  locator: PMID24107613 full Results,Fig2A-C,Methods/JW0493 clone
  accessed_at: '2026-10-11T05:43:26.055714Z'
  support: supports
  summary: Purified AllA releases urea, not ammonia; EDTA removes activity and nickel
    restores it. Glyoxylate hydration does not settle microscopic water mechanism.
    Source-specific recombinant scope is retained.
  snapshot_sha256: 856f106774e34dca4bbfde4bc74c741c9f461ff9b23686ad5a9a2510e22a7a4d
- evidence_id: e-physiology
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC94204/
  locator: PMID10601204 full HTML; sec13,JA174 allA deletion, ECL1 growth
  accessed_at: '2026-10-11T05:43:26.055714Z'
  support: supports
  summary: K12 derivative anaerobic allantoin nitrogen use with xylose; allA deletion
    loses cleavage activity without losing growth. Record does not claim sole-carbon
    growth, essentiality or universal strain flux.
  snapshot_sha256: a8fdc4fde9bbbb25a906b2f84c34a5cfa72914a2ffa8afcdfc066e5604a19350
- evidence_id: e-allB-assembly
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC94829/
  locator: PMID11092864 full relevant Results/Methods;Figs3B and4;Table2
  accessed_at: '2026-10-11T05:43:26.055714Z'
  support: supports
  summary: Purified AllB tetramer is supported by gel filtration/crosslinking and50.5kDa
    subunits. Metal stimulation is preparation-specific.
  snapshot_sha256: 2f4e068944272532911d29449d7a133e5b995b1db7fa27984219f82364fb8304
- evidence_id: e-allB-metal
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC141845/
  locator: PMID12486048 full relevant Results/Discussion;Enantioselectivity/Fig6
  accessed_at: '2026-10-11T05:43:26.055714Z'
  support: supports
  summary: Zn physiological preference is inference. Co/Ni reconstitution and Co-associated
    slowerR turnover are qualified; S route remains exact, with no requirement for
    simultaneous alternative metals.
  snapshot_sha256: b10a113c20794a750b2c58a1fdae1278800153b085f1d18b329f258b0b0665b4
- evidence_id: e-abstracts
  kind: primary_source
  reference: PMID:17362992; PMID:20038185; PMID:19935661
  locator: Retained full indexed abstracts only, in primary-assemblies-metals.json
  accessed_at: '2026-10-11T05:43:26.055714Z'
  support: supports
  summary: AllC dimer/twoZn older structural evidence, modernS-ureidoglycine true
    product, and EcAllE Mn-dependent inversion toS-ureidoglycolate are supported at
    actual inspected abstract scope. No unavailable full text is claimed read.
  snapshot_sha256: 8752189e192ffec0125e1750211c19a9973e72313c508ffd76811bb5b1345a29
- evidence_id: e-proteins
  kind: database
  reference: research/pathway_additions/2026-10-11-next-192/allantoin-independent-review-audit.json
  locator: Native CPLX-64/CPLX-7524 components;UniProtP77671/P77425/P75713/P77731
    comments,evidence,xrefs;PDB1XSQ assembly
  accessed_at: '2026-10-11T05:43:26.055714Z'
  support: supports
  summary: AllB4 and AllC2 components verified; AllE monomer is annotation inference;
    AllA dimer is structural/annotation support and uses enables. Alternative cofactors
    and AllC/AllE localization tiers are explicit.
  snapshot_sha256: 099227d9b204228a98417f8324dc9e103dcb35da0054af47e44ea386b6ef67de
- evidence_id: e-context
  kind: database
  reference: research/pathway_additions/2026-10-11-next-192/imodulondb-source-manifest.json
  locator: 26 original source response hashes;component3 table;four exact locus search
    responses
  accessed_at: '2026-10-11T05:43:26.055714Z'
  support: supports
  summary: Computational MG1655 expression context only. Search hits do not establish
    catalysis, pathway identity or absent membership.
  snapshot_sha256: 261292c60259cafc66bc8cb82de6738d6c819fb7d50cde184f2c3d8ecad3b4f7
- evidence_id: e-late
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC12535856/
  locator: PMID41016821 Abstract,Introduction/Fig1,Methods
  accessed_at: '2026-10-11T05:43:26.055714Z'
  support: supports
  summary: 2025 study addresses oxamate allF/ArcA regulation inMC4100 and confirms
    AllA glyoxylate/urea branch distinction. Retained2023PMC10163214 fullXML AllB/GlxK
    regulation was also independently read. Neither extends this native catalytic
    boundary.
- evidence_id: e-integration
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-192/integration-receipt.json
  locator: All actual final command receipts and graph/baseline audits
  accessed_at: '2026-10-11T05:43:26.055714Z'
  support: supports
  summary: Required full-corpus checks pass with exact logs; separate scientific evidence
    remains necessary. Prior192 records/pages and all8713 baseline edges are retained.
  snapshot_sha256: ce0c463e3aab7995f7ee06112969a0fd6df89d7eb990b9912444b323e89cf212
assessments:
- assessment_id: a-identity
  area: identity
  topic: Complete exact native four-reaction boundary
  outcome: supported
  summary: PWY5705 includes nested three-stepPWY5698 plus AllA; the native hierarchy
    is not truncated. Existing oxamateIV and yeast glyoxylateI are mechanistically
    distinct.
  target_ids:
  - MetaCyc:PWY-5705
  evidence_ids:
  - e-native
  - e-target
- assessment_id: a-chemistry
  area: consistency
  topic: Direction families, charge, stereo and balance
  outcome: supported
  summary: Four Rhea master/directed bridges and17 chemical sides match the source.
    AllC legacyxref conflict is disclosed and separately normalized using current
    evidence. All4 balances pass.
  target_ids:
  - MetaCyc:PWY-5705
  evidence_ids:
  - e-rhea
  - e-proteins
- assessment_id: a-catalysts
  area: evidence
  topic: Assemblies, roles and cofactors
  outcome: supported
  summary: AllB tetramer/AllC dimer native identities verified. AllE annotation monomer
    and AllA inferred structural dimer limitations remain visible; enables avoids
    invented catalyst complex identity. Alternative metal conditions are not simultaneous
    occupancy.
  target_ids:
  - MetaCyc:PWY-5705
  evidence_ids:
  - e-proteins
  - e-allB-assembly
  - e-allB-metal
  - e-allA
  - e-abstracts
- assessment_id: a-scope
  area: scope
  topic: Organism and experimental physiology
  outcome: supported
  summary: K12 derivative genetic and purified-protein observations remain separate
    from MG1655 annotations. AllA activity is not essentiality, sole-carbon growth
    or constitutive species-wide flux.
  target_ids:
  - MetaCyc:PWY-5705
  evidence_ids:
  - e-physiology
  - e-allA
  - e-context
  - e-late
- assessment_id: a-provenance
  area: provenance
  topic: Exact nearest-source attribution and rendering
  outcome: supported
  summary: All41 edges/80 evidence items have inspected native, primary or explicitly
    qualified annotation support. Native ordering versus normalized chemical identity
    is separately grounded; generated graph/evidence preserve source bytes.
  target_ids:
  - MetaCyc:PWY-5705
  evidence_ids:
  - e-target
  - e-native
  - e-rhea
  - e-integration
findings: []
actions: []
limitations:
- PMID17362992,20038185,19935661 were inspected as complete indexed abstracts, not
  unavailable full papers. Claims retain their exact evidence tier.
- AllE monomer is curator inference. AllA dimer uses annotation and crystallographic
  biological-assembly support rather than an independent solution oligomer measurement.
- Metal preference and occupancy depend on purified preparation. AllB physiological
  Zn and alternative Ni/Co/Mn, AllC Zn/Mn, AllE Mn/Co and AllA nickel activity are
  qualified, not simultaneous-metal requirements.
- K12 derivative experiments do not establish universal MG1655/species-wide native
  flux; allA deletion phenotype is distinguished from growth necessity.
- iModulonDB runner was unavailable; unchanged direct canonical client and independently
  rehashed responses supply computational context only. No absence-of-membership inference.
- No available browser surface was used. Actual generated HTML/SVG/KGX parsing is
  a structural/content check, not visual browser QA.
notes:
- All 18 initial captured input hashes remain unchanged. Final shared receipts and
  correct authority snapshot paths were added and inspected before save.
- Reviewer source audit truthfully retains its earlier pending-full-gates timestamp;
  this final bundle adds the subsequently completed actual shared checks.
- Scientific source replay is independent of the author helper. Full corpus commands
  were executed by root and independently inspected through actual logs/digests.
links: []
```

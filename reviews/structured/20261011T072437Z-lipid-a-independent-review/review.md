# Independent scientific review of the complete L-Ara4N lipid-A modification pathway

- Review: 20261011T072437Z-lipid-a-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T07:13:37Z
- Finished UTC: 2026-10-11T07:24:37Z
- Reviewer: Codex independent reviewer (/root/verify_graph_publication) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete six-step MetaCyc PWY0-1338 mechanism is supported within its explicitly qualified E.coli K-12 implementation. Independent original-source review and replay support all 50 edges/98 evidence, exact stoichiometry/directions and assembly/strain limits. No actionable finding was identified. Older abstract-only sources and unresolved E.coli assembly/metal details remain explicit; final coordinated gates pass.

## Scope And Provenance

One full frozen maintained record, every participant/reaction/edge/reference and material source assertion, original chemistry and experimental scope, final graph/gate evidence.

Selection: Exact MetaCyc:PWY0-1338 target at SHA256 6c9f87fc7a7b6ae411092a5e34330df52f18bb574a09b25eae79fc48182d3955
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 720ebcddbc421fbc01a4a82461fcbf13da7ea44f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY0-1338 | data/pathways/l-ara4n-modified-lipid-a-biosynthesis.yaml | maintained | polymyxin resistance |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical initial and final input inspections | passed | True | MetaCyc:PWY0-1338 | Initial canonical inspect at 2026-10-11T07:13:37Z captured the whole target before assessment. Final inspection includes the actual stable dossiers, authority snapshots, graph/baseline and final gate seal. Target SHA is unchanged; initial alias label was normalized to the native canonical label in final target metadata. |
| Independent native/Rhea/source/KGX replay | passed | True | MetaCyc:PWY0-1338 | Executed independently, session 32457 exit 0. Rehashed all 34 references; independently extracted 26 sides from full Rhea RDF and checked 6 formula/charge balances/directions, native members, exact source locators, seven K-12 protein identities, ArnA assembly bridge and actual 50-edge/98-evidence KGX. A separate subsequent check rehashed 34 iModulon bodies and read exact component 68 entries. An earlier helper attempt incorrectly looked for RHEA in the source-name snapshot rather than ontology snapshot; that reviewer-helper assumption was corrected with no product edit. |
| Inspected actual author replay and exact dossier bytes | passed | True | MetaCyc:PWY0-1338 | Executed by the author, session 65964 exit 0; reviewer inspected stdout/dossier hashes,38 source bodies, native+closed schemas, full six-reaction weighted net balance and actual export. This is delegated verification, not claimed as reviewer execution. |
| Coordinated render | passed | False | MetaCyc:PWY0-1338 | Executed by integration agent, exit 0; inspected actual log /private/tmp/pathwaymech-next-198-verification-render.log SHA256 f474e395e2d89a95cabc61e10d2fd111e1c4852d51b023f421de697f7dd96755; 2026-10-11T07:15:05.880831+00:00 through 2026-10-11T07:15:49.193064+00:00. Corpus-wide gate, not a new reviewer execution. |
| Coordinated validate | passed | True | MetaCyc:PWY0-1338 | Executed by integration agent, exit 0; inspected actual log /private/tmp/pathwaymech-next-198-verification-validate.log SHA256 106851f36e8e3b27753cbe5b9317702aeff20f31e3ff42731663b5073f003d3c; 2026-10-11T07:15:49.194647+00:00 through 2026-10-11T07:18:21.589424+00:00. Corpus-wide gate, not a new reviewer execution. |
| Coordinated lint | passed | True | MetaCyc:PWY0-1338 | Executed by integration agent, exit 0; inspected actual log /private/tmp/pathwaymech-next-198-verification-lint.log SHA256 df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41; 2026-10-11T07:15:49.194899+00:00 through 2026-10-11T07:15:49.601540+00:00. Corpus-wide gate, not a new reviewer execution. |
| Coordinated identifiers | passed | False | MetaCyc:PWY0-1338 | Executed by integration agent, exit 0; inspected actual log /private/tmp/pathwaymech-next-198-verification-identifiers.log SHA256 d1ff997b826fe0c478aee483a401c5d579827ddc8bd36f76d5acb1813b3cd719; 2026-10-11T07:15:49.195092+00:00 through 2026-10-11T07:16:11.441591+00:00. Corpus-wide gate, not a new reviewer execution. |
| Coordinated kgx | passed | False | MetaCyc:PWY0-1338 | Executed by integration agent, exit 0; inspected actual log /private/tmp/pathwaymech-next-198-verification-kgx.log SHA256 2cc7a4ebafad46c0f34f1fa6edeba1f0197cf1c1a270df440b451f26950c9f4f; 2026-10-11T07:15:49.602429+00:00 through 2026-10-11T07:16:13.240580+00:00. Corpus-wide gate, not a new reviewer execution. |
| Coordinated diff | passed | True | MetaCyc:PWY0-1338 | Executed by integration agent, exit 0; inspected actual log /private/tmp/pathwaymech-next-198-verification-diff.log SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; 2026-10-11T07:16:11.442168+00:00 through 2026-10-11T07:16:12.031129+00:00. Corpus-wide gate, not a new reviewer execution. |
| Final frozen full test suite | passed | True | MetaCyc:PWY0-1338 | Executed by integration agent; final full suite exit 0. Actual log /private/tmp/pathwaymech-next-198-verification-test-final.log SHA256 9a5d08bea9d6de04c0c8b3ef4475fdfc23e438e5e78101039d1517e3616e7b01. Final summary: =========== 1059 passed, 3 skipped, 3 warnings in 409.16s (0:06:49) ============. The retained initial verification-test.log exited1 with 1058 passed,1 stale-site test failure,3 skipped,3 warnings after overlapping final source/page work; it is not represented as a pass. Final suite was rerun on the stable rendered state. |

## Scientific And Domain Assessments

### Complete native aminoarabinose-lipid-A mechanism

identity: supported. Targets: MetaCyc:PWY0-1338.

The phenotype-named PWY0-1338 record denotes exactly the inspected complete six-step route, not all polymyxin resistance mechanisms. Its supplied upstream UDP-glucuronate/acceptor boundaries and two legacy map dispositions are explicit.

### Full chemistry and selected direction

grounding: supported. Targets: MetaCyc:PWY0-1338.

Current ChEBI/Rhea chemistry, proton/charge conventions, ArnB reverse orientation and ArnT bis-transfer stoichiometry are exact. Native maps with incorrect donor/return species are preserved as rejected source facts rather than silently imported.

### Assemblies, component roles and cofactor scope

representation: supported. Targets: MetaCyc:PWY0-1338.

Only source-supported ArnA physical hexamer is asserted and its non-exclusive assembly limits remain. Other proteins use qualified function enables roles. ArnB PLP is directly supported; Salmonella ArnC/ArnD assemblies/metals and proposed ArnEF heterodimer are not generalized.

### Strains, constructs and conditional phenotype

scope: supported. Targets: MetaCyc:PWY0-1338.

Reviewed K-12 molecular identities, conditional E.coli pmrAc deletion experiments, overproduced proteins and purified Salmonella constructs are distinguished at nearest edges. No constitutive species-wide resistance or direct wild-type flux is claimed.

### Nearest edge support and publication access

evidence: supported. Targets: MetaCyc:PWY0-1338.

All50 edges were read with their98 evidence blocks and original sources, including source-defined reaction ordering, exact family bridges, functional/assembly distinctions and transport context. Abstract-only evidence is transparently identified; no material unsupported assertion was found.

### Structured source context

provenance: supported. Targets: MetaCyc:PWY0-1338.

Canonical acquisition/replay and independent retained-body verification agree on exact arnA/B/C expression context; the graph does not promote this to biochemical or regulatory proof.

### Frozen record/export and coordinated gates

graph: supported. Targets: MetaCyc:PWY0-1338.

Local node declarations, exact reference bodies, labels, predicates, source locators and evidence export passed independent replay. Final corpus validation and rerun tests pass; generated output is assessed programmatically without a browser.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | MetaCyc:PWY0-1338; RXN0-1861/1863/1862/3521/5409/2001; Original native XML pathway reaction-list/predecessors, exact reaction chemical sides and RHEA dblinks; root independently acquired canonical PWY0-1338 HTML | supports | Original six-reaction boundary starts at supplied UDP-glucuronate and finishes with aminoarabinose-modified lipid A. Native phenotype title is scoped to this exact mechanism. Ugd and acceptor assembly are outside these six members; current equations are mapped through exact family triples, including bidirectional 24713 to master 24710 and reverse 24712. |
| chemistry | Rhea 142 full original RDF/directions; ChEBI 255 original SQLite; Independent audit rhea_sides/balanced_reactions; directed 24703,24712,24707,27723,27735,35372 and all 26 participant/compound side triples | supports | All26 sides, coefficients, formulas, charges and six balances independently agree. Final ArnT equation retains two donors and two monophosphate carrier products; this is a net two-transfer reaction, not a single elementary event. N10-formyl-THF charged monoglutamate form is not asserted exactly identical to broader native folate classes. |
| pathbank | PathBank:SMP0002065/PW002052.owl; SMP0122234/PW123542.owl; Original BioPAX reactions3356/5994/5995; donor PW_C042606 and product PW_C042616; lipid-a-source-projection.json dispositions | supports | Independently confirmed both full six-reaction documents and material source errors: wrong reaction 3356 enzyme label, unbalanced 5994 coefficients, copied formamido donor formula, and erroneous terminal diphosphate return. Maintained record rejects those source assertions using separately inspected current Rhea/ChEBI and primary donor evidence. Pseudomonas candidate proteins are not substituted into the E.coli implementation. |
| uniprot | UniProtKB:P77398/P77690/P77757/P76472/P76473/Q47377/P76474; Original reviewed JSON primaryAccession/organism/gene/catalytic/cofactor/subunit/subcellular-location comments; exact node/edge locators in independent audit | supports | All seven identities are reviewed E.coli K-12 entries. ArnB dimer is similarity-transferred; ArnD remains probable in current annotation. ArnT lipid-IVA catalytic text is an alternative acceptor, not evidence for the entire Kdo2 net equation. Functional enables edges preserve these limits. |
| arna | PMID:15939024/PMC2997725; PMID:15807526/PMC2583347; PMID:31344437 inspected abstract; Full PMC2997725 P8/P10/P17/P29; PMC2583347 P14-P19; original abstract result PMID31344437; native CPLX0-7718 component6 G7168-MONOMER and exact UNIPROT P77398 dblink | supports | E.coli full-length ArnA hexamer/dimer-of-trimers and independently active domains support both functions with non-exclusive assembly. Later tetramer/hexamer observation is retained. ATP crystallographic mimic is not a pathway substrate or bound cofactor; NAD is a reducible reaction participant. |
| arnb | PMID:12704196 inspected primary abstract; primary-abstracts-1.json resultList/result[id=12704196]/abstractText | supports | Overproduced E.coli ArnB supports PLP, cytoplasmic localization, reversible NMR-characterized transamination and equilibrium near 0.1 toward biosynthesis. Reverse directed reaction represents selected biosynthetic flux without asserting irreversibility. Full text was not inspected. |
| arnc | PMID:15695810 inspected abstract; PMID:39865303/PMC11761694; PMID:37782650/PMC10914315; 2005 abstract result; full 2025 pro70037-sec-0003(2.1), sec-0008(3.2), sec-0009(3.3); 2023 P19 | supports | Formylated sugar specificity is supported. The 2025 structural enzyme is Salmonella Typhimurium expressed in E.coli C43; tetramer/Mn preparation is not transferred to E.coli ArnC. At reported map resolution Mn was not confidently modeled. The 2023 preparation likewise uses Salmonella ArnC with MnCl2. |
| arnd | PMID:37782650/PMC10914315; Full original HTML P10/P13/P21 Figure1D; P28-P30 Figure5A | supports | E.coli K-12-derived pmrAc arnD mutant accumulates formylated donor; purified Salmonella ArnD directly catalyzes deformylation. EDTA/Mn/Co effects are purified Salmonella assay conditions, not an E.coli physiological metal assignment. Later direct functional evidence is distinguished from older native hypothetical annotation. |
| arnt | PMID:11535604 and PMID:11535605 inspected primary abstracts; PMID:17928292/PMC2613183; Primary abstract result IDs11535604/11535605; full PMC2613183 P36 | supports | Kdo-bearing lipid-A acceptors permit two additions while lipidIVA supports one. E.coli donor MS/31P/NMR supports one phosphate and alpha-aminoarabinose headgroup. E.coli arnT mutant loses lipid modification while donor access persists. Full 2001 papers were unavailable and are not claimed inspected. |
| arnef | PMID:17928292/PMC2613183; Full original HTML P34-P40 and P45; membrane-impermeable versus permeable labeling/deletion/complementation experiments | supports | E.coli ArnE/F enable transport-associated whole-pathway function; original roughly four- to fivefold access difference, residual lipid modification and proposed heterodimer status are explicit. No purified fixed assembly, individual-subunit sufficiency, energy-coupling or channeling claim is made. |
| imodulon | iModulonDB e_coli/precise_mg1655 component 68; 34 independently rehashed retained response bodies; d17f162020f4ccc4.json seven rows, exact arnA/b2255/P77398, arnB/b2253/P77690, arnC/b2254/P77757 rows; canonical parser replay | context_only | The three exact genes are computational module members. Console runner unavailable; root used the unchanged canonical direct client and replayed original responses. This context supplies no independent catalytic, regulatory or phenotype proof and no negative membership inference. |
| graph | research/pathway_additions/2026-10-11-next-198/lipid-a-independent-review-audit.json; actual_kgx, source_locators_checked, original_reference_bodies_rehashed, independent_imodulondb_context_check | supports | Independent actual export preserves all 50 edges and 98 evidence blocks across 39 nodes; all 34 reference body hashes and named node grounding checked. This is programmatic verification, not browser visual QA. |
| gates | research/pathway_additions/2026-10-11-next-198/integration-receipt.json; Final gate logs and receipts; generated-graph-kgx-audit.json; baseline-preservation.json | supports | Final delegated corpus checks and hashes inspected. Required native/closed schema, identifiers, lint, full tests and whitespace checks pass in their declared final scope; initial stale-page failure is retained separately. |

## Limits And Additional Notes

- Older ArnB/formylation/ArnT/donor primary studies and 2019 ArnA oligomer study were inspected as complete primary abstracts, not full text.
- Fresh PMC web opens returned anti-bot interstitials; retained original full HTML bodies were read directly and exact referenced digests independently reverified.
- E.coli ArnD physiological metal, ArnC physical oligomer and purified ArnEF complex/energy coupling are not resolved; the graph faithfully limits its assertions.
- iModulon expression membership is context only, not proof of chemistry, regulation or constitutive resistance.
- Final corpus gates were run by the integration agent and inspected via actual terminal receipts/log hashes, not redundantly rerun by this reviewer. Initial stale-page failure and final rerun remain distinct.
- No browser surfaces were available; generated graph/export integrity was assessed programmatically.
- Initial canonical inspect captured only the stable target before assessment. Final expanded inputs were read and reassessed after shared freeze; target bytes never changed during this review.
- The independent reviewer source-audit JSON was sealed while shared gates were pending and intentionally preserves that earlier temporal limitation; this final review adds actual final gate evidence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T072437Z-lipid-a-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of the complete L-Ara4N lipid-A modification
  pathway
started_at: '2026-10-11T07:13:37Z'
finished_at: '2026-10-11T07:24:37Z'
reviewer:
  identity: Codex independent reviewer (/root/verify_graph_publication)
  kind: agent
  independence: independent
  independence_basis: Did not author this lipid-A record or its dossiers. Authored
    the separate pyrimidine deoxyribonucleotide salvage target in this cohort, excluded
    from this scientific judgement. Independently read full target and original primary/native
    sources and replayed chemistry/source/KGX checks.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete six-step MetaCyc PWY0-1338 mechanism is supported within its
  explicitly qualified E.coli K-12 implementation. Independent original-source review
  and replay support all 50 edges/98 evidence, exact stoichiometry/directions and
  assembly/strain limits. No actionable finding was identified. Older abstract-only
  sources and unresolved E.coli assembly/metal details remain explicit; final coordinated
  gates pass.
source:
  git_revision: 720ebcddbc421fbc01a4a82461fcbf13da7ea44f
  state: working_tree
  inputs:
  - path: conf/identifier_policy.yaml
    sha256: 3e19ecbbe980e44198405ae0cf37b5fd17ae4c88c05dbf36fab482b2ddd38bd1
    role: context
  - path: conf/identifier_sources.json
    sha256: 2da971dcc8cb423d3d88459c9a46ddcc1791692a5a06d6af78ab4ac6c09f2050
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 5c89c140a1a674239a015dff3366a0d5ba5481447f733869e805ee9751e49dfe
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 9ce682d16ed2758938d09e93288630d8cd67b40564a8acb349d122e9364c06e8
    role: context
  - path: data/pathways/l-ara4n-modified-lipid-a-biosynthesis.yaml
    sha256: 6c9f87fc7a7b6ae411092a5e34330df52f18bb574a09b25eae79fc48182d3955
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
  - path: research/pathway_additions/2026-10-11-next-198/authority-integration.json
    sha256: 4d0e517beaf62d0ecb1339ba678e83c689abaad6da45a814c1b4251cfcb7d7a1
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/authority-source-inspection.json
    sha256: 4061c095b040cb564b3bdebeb25d7965fb9238fd5fe9e32dad164a113b4a1104
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/baseline-preservation.json
    sha256: e2122765592484b44baa3acca4f86bda132efc0e447ec4321012c5d2711bbc86
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/generated-graph-kgx-audit.json
    sha256: 2aad2f41ce08b6b353966fcd5e3c368dc8299c5c601c4b831a1df7c6d3e822b0
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/imodulondb-context.json
    sha256: 7f2e54b533ed54a9618a78710528a8e37fc3bff1d2ea3d8b69ab36ae5a27a4a8
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/imodulondb-parser-replay.json
    sha256: 27014ecdd833ec140b6d99d4e3cc21b01735dfb0cb342ce429c67cc87bab7ae2
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/imodulondb-runner-availability.json
    sha256: 7a77ee5a8a9e92e7ddc0086f45051e4f0f4f9f15f50d7560ef74725689dc48d0
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/imodulondb-source-manifest.json
    sha256: 9ec7ebcf1fe2a959a24a196ea82f7417649690b93f3a1356aa4f2e37be32289c
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/integration-receipt.json
    sha256: 5a29f0d35faff53985010301cd322e4170424e6031dcc85ea705423a730ed985
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/lipid-a-authority-delta.json
    sha256: 8ed420322b0435f1016f3d47222ffa76613b6270c3a02a0371f931626a3b4ddc
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/lipid-a-curation.md
    sha256: f0c8463e90e44fa0fc755a31018192fc3519639f049bca5b9d555cb0c0a8aa8c
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/lipid-a-dedup.json
    sha256: 78adc090b29a6a4874ee7d98858b837da638bb3ae2ee77cff6a583e35fbaf23b
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/lipid-a-identifiers.json
    sha256: 7ccc0d9112e9131f7f072f498fdb7a39c84f63d0e15f6a6eb82d2566fa04cc29
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/lipid-a-independent-review-audit.json
    sha256: 8faee2d47f49d648304777a8be60d398b085d7d4254653d2f369319ecf201daf
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/lipid-a-protein-projection.json
    sha256: 18762253212430cafaf1d85af0c37338864e135e5a744f8659f74a9c965f1dec
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/lipid-a-replay.py
    sha256: 7c12c8643a7f9afa9b17780aa2233062c5f306a11c401252feec1c423f06f9ca
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/lipid-a-source-manifest.json
    sha256: 7557e68124f2803ee1ffe6366a80881acb5829c55dd58e63e897193d544bbcb9
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/lipid-a-source-projection.json
    sha256: 5e11fd6cd9de0d446257166c7036e5f20da3216738e83169f3693b0e733daef5
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/lipid-a-validation.json
    sha256: bbbbf2237ed4e1c16c4f056547faa985c11afe8e073b3d92b83b340242eb5bbe
    role: context
  - path: src/pathwaymech/schema.py
    sha256: f006e5b99cedd91b57a2c5fb938315a84b68822586d1602d4df9ccfdc851e98c
    role: context
targets:
- target_id: MetaCyc:PWY0-1338
  path: data/pathways/l-ara4n-modified-lipid-a-biosynthesis.yaml
  label: polymyxin resistance
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/l-ara4n-modified-lipid-a-biosynthesis.yaml
    role: maintained pathway record
scope:
  description: One full frozen maintained record, every participant/reaction/edge/reference
    and material source assertion, original chemistry and experimental scope, final
    graph/gate evidence.
  selection: Exact MetaCyc:PWY0-1338 target at SHA256 6c9f87fc7a7b6ae411092a5e34330df52f18bb574a09b25eae79fc48182d3955
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY0-1338
  exclusions:
  - target: Other cohort records and older corpus science
    reason: Separate independent reviewers cover other records; reviewer does not
      independently certify authored salvage science.
  - target: Ugd/UDP-glucuronate production, lipid-A acceptor assembly and all other
      resistance mechanisms
    reason: Outside the exact native six-step pathway boundary.
checks:
- check_id: inspect
  name: Canonical initial and final input inspections
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    .venv/bin/python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-198-lipid-final-targets.yaml
    --input conf/identifier_policy.yaml --input conf/identifier_sources.json --input
    data/identifier_authorities/ontology.json --input data/identifier_authorities/sources.json
    --input src/pathwaymech/schema.py --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/CAUSAL_GRAPHS.md --input research/pathway_additions/2026-10-11-next-198/lipid-a-authority-delta.json
    --input research/pathway_additions/2026-10-11-next-198/lipid-a-curation.md --input
    research/pathway_additions/2026-10-11-next-198/lipid-a-dedup.json --input research/pathway_additions/2026-10-11-next-198/lipid-a-identifiers.json
    --input research/pathway_additions/2026-10-11-next-198/lipid-a-independent-review-audit.json
    --input research/pathway_additions/2026-10-11-next-198/lipid-a-protein-projection.json
    --input research/pathway_additions/2026-10-11-next-198/lipid-a-replay.py --input
    research/pathway_additions/2026-10-11-next-198/lipid-a-source-manifest.json --input
    research/pathway_additions/2026-10-11-next-198/lipid-a-source-projection.json
    --input research/pathway_additions/2026-10-11-next-198/lipid-a-validation.json
    --input research/pathway_additions/2026-10-11-next-198/authority-integration.json
    --input research/pathway_additions/2026-10-11-next-198/authority-source-inspection.json
    --input research/pathway_additions/2026-10-11-next-198/imodulondb-context.json
    --input research/pathway_additions/2026-10-11-next-198/imodulondb-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-198/imodulondb-parser-replay.json
    --input research/pathway_additions/2026-10-11-next-198/imodulondb-runner-availability.json
    --input research/pathway_additions/2026-10-11-next-198/integration-receipt.json
    --input research/pathway_additions/2026-10-11-next-198/generated-graph-kgx-audit.json
    --input research/pathway_additions/2026-10-11-next-198/baseline-preservation.json
  status: passed
  required: true
  summary: Initial canonical inspect at 2026-10-11T07:13:37Z captured the whole target
    before assessment. Final inspection includes the actual stable dossiers, authority
    snapshots, graph/baseline and final gate seal. Target SHA is unchanged; initial
    alias label was normalized to the native canonical label in final target metadata.
  target_ids:
  - MetaCyc:PWY0-1338
  exit_code: 0
- check_id: independent-source-replay
  name: Independent native/Rhea/source/KGX replay
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    .venv/bin/python /private/tmp/pathwaymech-next-198-lipid-independent.py
  status: passed
  required: true
  summary: Executed independently, session 32457 exit 0. Rehashed all 34 references;
    independently extracted 26 sides from full Rhea RDF and checked 6 formula/charge
    balances/directions, native members, exact source locators, seven K-12 protein
    identities, ArnA assembly bridge and actual 50-edge/98-evidence KGX. A separate
    subsequent check rehashed 34 iModulon bodies and read exact component 68 entries.
    An earlier helper attempt incorrectly looked for RHEA in the source-name snapshot
    rather than ontology snapshot; that reviewer-helper assumption was corrected with
    no product edit.
  target_ids:
  - MetaCyc:PWY0-1338
  exit_code: 0
- check_id: author-replay-receipt
  name: Inspected actual author replay and exact dossier bytes
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    .venv/bin/python research/pathway_additions/2026-10-11-next-198/lipid-a-replay.py
  status: passed
  required: true
  summary: Executed by the author, session 65964 exit 0; reviewer inspected stdout/dossier
    hashes,38 source bodies, native+closed schemas, full six-reaction weighted net
    balance and actual export. This is delegated verification, not claimed as reviewer
    execution.
  target_ids:
  - MetaCyc:PWY0-1338
  exit_code: 0
- check_id: root-render
  name: Coordinated render
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just render-pages
  status: passed
  required: false
  summary: Executed by integration agent, exit 0; inspected actual log /private/tmp/pathwaymech-next-198-verification-render.log
    SHA256 f474e395e2d89a95cabc61e10d2fd111e1c4852d51b023f421de697f7dd96755; 2026-10-11T07:15:05.880831+00:00
    through 2026-10-11T07:15:49.193064+00:00. Corpus-wide gate, not a new reviewer
    execution.
  target_ids:
  - MetaCyc:PWY0-1338
  exit_code: 0
- check_id: root-validate
  name: Coordinated validate
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just validate
  status: passed
  required: true
  summary: Executed by integration agent, exit 0; inspected actual log /private/tmp/pathwaymech-next-198-verification-validate.log
    SHA256 106851f36e8e3b27753cbe5b9317702aeff20f31e3ff42731663b5073f003d3c; 2026-10-11T07:15:49.194647+00:00
    through 2026-10-11T07:18:21.589424+00:00. Corpus-wide gate, not a new reviewer
    execution.
  target_ids:
  - MetaCyc:PWY0-1338
  exit_code: 0
- check_id: root-lint
  name: Coordinated lint
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just lint
  status: passed
  required: true
  summary: Executed by integration agent, exit 0; inspected actual log /private/tmp/pathwaymech-next-198-verification-lint.log
    SHA256 df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41; 2026-10-11T07:15:49.194899+00:00
    through 2026-10-11T07:15:49.601540+00:00. Corpus-wide gate, not a new reviewer
    execution.
  target_ids:
  - MetaCyc:PWY0-1338
  exit_code: 0
- check_id: root-identifiers
  name: Coordinated identifiers
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just check-identifiers
  status: passed
  required: false
  summary: Executed by integration agent, exit 0; inspected actual log /private/tmp/pathwaymech-next-198-verification-identifiers.log
    SHA256 d1ff997b826fe0c478aee483a401c5d579827ddc8bd36f76d5acb1813b3cd719; 2026-10-11T07:15:49.195092+00:00
    through 2026-10-11T07:16:11.441591+00:00. Corpus-wide gate, not a new reviewer
    execution.
  target_ids:
  - MetaCyc:PWY0-1338
  exit_code: 0
- check_id: root-kgx
  name: Coordinated kgx
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just kgx-export --output-dir
    /private/tmp/pathwaymech-next-198-kgx
  status: passed
  required: false
  summary: Executed by integration agent, exit 0; inspected actual log /private/tmp/pathwaymech-next-198-verification-kgx.log
    SHA256 2cc7a4ebafad46c0f34f1fa6edeba1f0197cf1c1a270df440b451f26950c9f4f; 2026-10-11T07:15:49.602429+00:00
    through 2026-10-11T07:16:13.240580+00:00. Corpus-wide gate, not a new reviewer
    execution.
  target_ids:
  - MetaCyc:PWY0-1338
  exit_code: 0
- check_id: root-diff
  name: Coordinated diff
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache git diff --check
  status: passed
  required: true
  summary: Executed by integration agent, exit 0; inspected actual log /private/tmp/pathwaymech-next-198-verification-diff.log
    SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855; 2026-10-11T07:16:11.442168+00:00
    through 2026-10-11T07:16:12.031129+00:00. Corpus-wide gate, not a new reviewer
    execution.
  target_ids:
  - MetaCyc:PWY0-1338
  exit_code: 0
- check_id: root-test
  name: Final frozen full test suite
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just test
  status: passed
  required: true
  summary: 'Executed by integration agent; final full suite exit 0. Actual log /private/tmp/pathwaymech-next-198-verification-test-final.log
    SHA256 9a5d08bea9d6de04c0c8b3ef4475fdfc23e438e5e78101039d1517e3616e7b01. Final
    summary: =========== 1059 passed, 3 skipped, 3 warnings in 409.16s (0:06:49) ============.
    The retained initial verification-test.log exited1 with 1058 passed,1 stale-site
    test failure,3 skipped,3 warnings after overlapping final source/page work; it
    is not represented as a pass. Final suite was rerun on the stable rendered state.'
  target_ids:
  - MetaCyc:PWY0-1338
  exit_code: 0
evidence:
- evidence_id: native
  kind: database
  reference: MetaCyc:PWY0-1338; RXN0-1861/1863/1862/3521/5409/2001
  locator: Original native XML pathway reaction-list/predecessors, exact reaction
    chemical sides and RHEA dblinks; root independently acquired canonical PWY0-1338
    HTML
  accessed_at: '2026-10-11T07:23:37Z'
  support: supports
  summary: Original six-reaction boundary starts at supplied UDP-glucuronate and finishes
    with aminoarabinose-modified lipid A. Native phenotype title is scoped to this
    exact mechanism. Ugd and acceptor assembly are outside these six members; current
    equations are mapped through exact family triples, including bidirectional 24713
    to master 24710 and reverse 24712.
- evidence_id: chemistry
  kind: authority
  reference: Rhea 142 full original RDF/directions; ChEBI 255 original SQLite
  locator: Independent audit rhea_sides/balanced_reactions; directed 24703,24712,24707,27723,27735,35372
    and all 26 participant/compound side triples
  accessed_at: '2026-10-11T07:23:37Z'
  support: supports
  summary: All26 sides, coefficients, formulas, charges and six balances independently
    agree. Final ArnT equation retains two donors and two monophosphate carrier products;
    this is a net two-transfer reaction, not a single elementary event. N10-formyl-THF
    charged monoglutamate form is not asserted exactly identical to broader native
    folate classes.
- evidence_id: pathbank
  kind: database
  reference: PathBank:SMP0002065/PW002052.owl; SMP0122234/PW123542.owl
  locator: Original BioPAX reactions3356/5994/5995; donor PW_C042606 and product PW_C042616;
    lipid-a-source-projection.json dispositions
  accessed_at: '2026-10-11T07:23:37Z'
  support: supports
  summary: 'Independently confirmed both full six-reaction documents and material
    source errors: wrong reaction 3356 enzyme label, unbalanced 5994 coefficients,
    copied formamido donor formula, and erroneous terminal diphosphate return. Maintained
    record rejects those source assertions using separately inspected current Rhea/ChEBI
    and primary donor evidence. Pseudomonas candidate proteins are not substituted
    into the E.coli implementation.'
- evidence_id: uniprot
  kind: database
  reference: UniProtKB:P77398/P77690/P77757/P76472/P76473/Q47377/P76474
  locator: Original reviewed JSON primaryAccession/organism/gene/catalytic/cofactor/subunit/subcellular-location
    comments; exact node/edge locators in independent audit
  accessed_at: '2026-10-11T07:23:37Z'
  support: supports
  summary: All seven identities are reviewed E.coli K-12 entries. ArnB dimer is similarity-transferred;
    ArnD remains probable in current annotation. ArnT lipid-IVA catalytic text is
    an alternative acceptor, not evidence for the entire Kdo2 net equation. Functional
    enables edges preserve these limits.
- evidence_id: arna
  kind: primary_source
  reference: PMID:15939024/PMC2997725; PMID:15807526/PMC2583347; PMID:31344437 inspected
    abstract
  locator: Full PMC2997725 P8/P10/P17/P29; PMC2583347 P14-P19; original abstract result
    PMID31344437; native CPLX0-7718 component6 G7168-MONOMER and exact UNIPROT P77398
    dblink
  accessed_at: '2026-10-11T07:23:37Z'
  support: supports
  summary: E.coli full-length ArnA hexamer/dimer-of-trimers and independently active
    domains support both functions with non-exclusive assembly. Later tetramer/hexamer
    observation is retained. ATP crystallographic mimic is not a pathway substrate
    or bound cofactor; NAD is a reducible reaction participant.
- evidence_id: arnb
  kind: primary_source
  reference: PMID:12704196 inspected primary abstract
  locator: primary-abstracts-1.json resultList/result[id=12704196]/abstractText
  accessed_at: '2026-10-11T07:23:37Z'
  support: supports
  summary: Overproduced E.coli ArnB supports PLP, cytoplasmic localization, reversible
    NMR-characterized transamination and equilibrium near 0.1 toward biosynthesis.
    Reverse directed reaction represents selected biosynthetic flux without asserting
    irreversibility. Full text was not inspected.
- evidence_id: arnc
  kind: primary_source
  reference: PMID:15695810 inspected abstract; PMID:39865303/PMC11761694; PMID:37782650/PMC10914315
  locator: 2005 abstract result; full 2025 pro70037-sec-0003(2.1), sec-0008(3.2),
    sec-0009(3.3); 2023 P19
  accessed_at: '2026-10-11T07:23:37Z'
  support: supports
  summary: Formylated sugar specificity is supported. The 2025 structural enzyme is
    Salmonella Typhimurium expressed in E.coli C43; tetramer/Mn preparation is not
    transferred to E.coli ArnC. At reported map resolution Mn was not confidently
    modeled. The 2023 preparation likewise uses Salmonella ArnC with MnCl2.
- evidence_id: arnd
  kind: primary_source
  reference: PMID:37782650/PMC10914315
  locator: Full original HTML P10/P13/P21 Figure1D; P28-P30 Figure5A
  accessed_at: '2026-10-11T07:23:37Z'
  support: supports
  summary: E.coli K-12-derived pmrAc arnD mutant accumulates formylated donor; purified
    Salmonella ArnD directly catalyzes deformylation. EDTA/Mn/Co effects are purified
    Salmonella assay conditions, not an E.coli physiological metal assignment. Later
    direct functional evidence is distinguished from older native hypothetical annotation.
- evidence_id: arnt
  kind: primary_source
  reference: PMID:11535604 and PMID:11535605 inspected primary abstracts; PMID:17928292/PMC2613183
  locator: Primary abstract result IDs11535604/11535605; full PMC2613183 P36
  accessed_at: '2026-10-11T07:23:37Z'
  support: supports
  summary: Kdo-bearing lipid-A acceptors permit two additions while lipidIVA supports
    one. E.coli donor MS/31P/NMR supports one phosphate and alpha-aminoarabinose headgroup.
    E.coli arnT mutant loses lipid modification while donor access persists. Full
    2001 papers were unavailable and are not claimed inspected.
- evidence_id: arnef
  kind: primary_source
  reference: PMID:17928292/PMC2613183
  locator: Full original HTML P34-P40 and P45; membrane-impermeable versus permeable
    labeling/deletion/complementation experiments
  accessed_at: '2026-10-11T07:23:37Z'
  support: supports
  summary: E.coli ArnE/F enable transport-associated whole-pathway function; original
    roughly four- to fivefold access difference, residual lipid modification and proposed
    heterodimer status are explicit. No purified fixed assembly, individual-subunit
    sufficiency, energy-coupling or channeling claim is made.
- evidence_id: imodulon
  kind: database
  reference: iModulonDB e_coli/precise_mg1655 component 68
  locator: 34 independently rehashed retained response bodies; d17f162020f4ccc4.json
    seven rows, exact arnA/b2255/P77398, arnB/b2253/P77690, arnC/b2254/P77757 rows;
    canonical parser replay
  accessed_at: '2026-10-11T07:23:37Z'
  support: context_only
  summary: The three exact genes are computational module members. Console runner
    unavailable; root used the unchanged canonical direct client and replayed original
    responses. This context supplies no independent catalytic, regulatory or phenotype
    proof and no negative membership inference.
- evidence_id: graph
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-198/lipid-a-independent-review-audit.json
  locator: actual_kgx, source_locators_checked, original_reference_bodies_rehashed,
    independent_imodulondb_context_check
  accessed_at: '2026-10-11T07:23:37Z'
  support: supports
  summary: Independent actual export preserves all 50 edges and 98 evidence blocks
    across 39 nodes; all 34 reference body hashes and named node grounding checked.
    This is programmatic verification, not browser visual QA.
- evidence_id: gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-198/integration-receipt.json
  locator: Final gate logs and receipts; generated-graph-kgx-audit.json; baseline-preservation.json
  accessed_at: '2026-10-11T07:23:37Z'
  support: supports
  summary: Final delegated corpus checks and hashes inspected. Required native/closed
    schema, identifiers, lint, full tests and whitespace checks pass in their declared
    final scope; initial stale-page failure is retained separately.
assessments:
- assessment_id: identity
  area: identity
  topic: Complete native aminoarabinose-lipid-A mechanism
  outcome: supported
  summary: The phenotype-named PWY0-1338 record denotes exactly the inspected complete
    six-step route, not all polymyxin resistance mechanisms. Its supplied upstream
    UDP-glucuronate/acceptor boundaries and two legacy map dispositions are explicit.
  target_ids:
  - MetaCyc:PWY0-1338
  evidence_ids:
  - native
  - pathbank
- assessment_id: chemistry
  area: grounding
  topic: Full chemistry and selected direction
  outcome: supported
  summary: Current ChEBI/Rhea chemistry, proton/charge conventions, ArnB reverse orientation
    and ArnT bis-transfer stoichiometry are exact. Native maps with incorrect donor/return
    species are preserved as rejected source facts rather than silently imported.
  target_ids:
  - MetaCyc:PWY0-1338
  evidence_ids:
  - chemistry
  - pathbank
  - arnt
- assessment_id: roles
  area: representation
  topic: Assemblies, component roles and cofactor scope
  outcome: supported
  summary: Only source-supported ArnA physical hexamer is asserted and its non-exclusive
    assembly limits remain. Other proteins use qualified function enables roles. ArnB
    PLP is directly supported; Salmonella ArnC/ArnD assemblies/metals and proposed
    ArnEF heterodimer are not generalized.
  target_ids:
  - MetaCyc:PWY0-1338
  evidence_ids:
  - uniprot
  - arna
  - arnb
  - arnc
  - arnd
  - arnef
- assessment_id: scope
  area: scope
  topic: Strains, constructs and conditional phenotype
  outcome: supported
  summary: Reviewed K-12 molecular identities, conditional E.coli pmrAc deletion experiments,
    overproduced proteins and purified Salmonella constructs are distinguished at
    nearest edges. No constitutive species-wide resistance or direct wild-type flux
    is claimed.
  target_ids:
  - MetaCyc:PWY0-1338
  evidence_ids:
  - uniprot
  - arnd
  - arnef
  - arnc
  dimensions:
  - name: taxon_and_condition
    value: E.coli K-12 annotation; explicitly qualified experimental strains/pmrAc
      conditions and cross-species purified assays
    definition: Scope of evidence supporting the recorded implementation, not an assertion
      all studies used one strain.
    evidence_ids:
    - uniprot
    - arnd
    - arnef
    - arnc
- assessment_id: evidence
  area: evidence
  topic: Nearest edge support and publication access
  outcome: supported
  summary: All50 edges were read with their98 evidence blocks and original sources,
    including source-defined reaction ordering, exact family bridges, functional/assembly
    distinctions and transport context. Abstract-only evidence is transparently identified;
    no material unsupported assertion was found.
  target_ids:
  - MetaCyc:PWY0-1338
  evidence_ids:
  - native
  - chemistry
  - uniprot
  - arna
  - arnb
  - arnc
  - arnd
  - arnt
  - arnef
- assessment_id: context
  area: provenance
  topic: Structured source context
  outcome: supported
  summary: Canonical acquisition/replay and independent retained-body verification
    agree on exact arnA/B/C expression context; the graph does not promote this to
    biochemical or regulatory proof.
  target_ids:
  - MetaCyc:PWY0-1338
  evidence_ids:
  - imodulon
- assessment_id: validation
  area: graph
  topic: Frozen record/export and coordinated gates
  outcome: supported
  summary: Local node declarations, exact reference bodies, labels, predicates, source
    locators and evidence export passed independent replay. Final corpus validation
    and rerun tests pass; generated output is assessed programmatically without a
    browser.
  target_ids:
  - MetaCyc:PWY0-1338
  evidence_ids:
  - graph
  - gates
findings: []
actions: []
limitations:
- Older ArnB/formylation/ArnT/donor primary studies and 2019 ArnA oligomer study were
  inspected as complete primary abstracts, not full text.
- Fresh PMC web opens returned anti-bot interstitials; retained original full HTML
  bodies were read directly and exact referenced digests independently reverified.
- E.coli ArnD physiological metal, ArnC physical oligomer and purified ArnEF complex/energy
  coupling are not resolved; the graph faithfully limits its assertions.
- iModulon expression membership is context only, not proof of chemistry, regulation
  or constitutive resistance.
- Final corpus gates were run by the integration agent and inspected via actual terminal
  receipts/log hashes, not redundantly rerun by this reviewer. Initial stale-page
  failure and final rerun remain distinct.
- No browser surfaces were available; generated graph/export integrity was assessed
  programmatically.
notes:
- Initial canonical inspect captured only the stable target before assessment. Final
  expanded inputs were read and reassessed after shared freeze; target bytes never
  changed during this review.
- The independent reviewer source-audit JSON was sealed while shared gates were pending
  and intentionally preserves that earlier temporal limitation; this final review
  adds actual final gate evidence.
tags:
- independent-scientific-review
- pathway-completeness
- source-provenance
- strain-scope
```

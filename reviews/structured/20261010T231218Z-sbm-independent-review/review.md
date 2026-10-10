# Independent scientific review of proposed Sbm succinate-to-propanoate cycle

- Review: 20261010T231218Z-sbm-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-10T23:02:16Z
- Finished UTC: 2026-10-10T23:12:18Z
- Reviewer: Codex /root/pathway_literature_candidates (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The proposed three-enzyme cycle is grounded in sources with explicit unresolved ScpB stereochemistry and physiological-flux limits. One initial minor citation locator defect was corrected under issue #324 and independently verified before save; no unresolved finding remains. Required corpus validation, tests and lint passed on frozen inputs.

## Scope And Provenance

One exact maintained Sbm record, all nodes/edges/evidence/references; source-grounded scientific assessment plus final integration validation.

Selection: Explicit parent assignment of data/pathways/succinate-to-propanoate.yaml, MetaCyc:PWY0-43
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 722257adc1882495f8454cc229b8fa0c187cf868.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY0-43 | data/pathways/succinate-to-propanoate.yaml | maintained | conversion of succinate to propanoate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Documented corpus validate | passed | True | MetaCyc:PWY0-43 | 167 native and closed-schema records; identifier/label policies, 8731 evidence blocks, 30 sources, 248 histories, documentation/research and current pages passed. Executed by root coordinator; this reviewer inspected the final log. |
| Documented corpus test | passed | True | MetaCyc:PWY0-43 | 1043 passed, 3 skipped, 3 upstream deprecation warnings in 351.55 seconds. Executed by root coordinator; this reviewer inspected the final log. |
| Documented corpus lint | passed | True | MetaCyc:PWY0-43 | Ruff: all checks passed. Executed by root coordinator; this reviewer inspected the final log. |
| Documented corpus render | passed | False | MetaCyc:PWY0-43 | Rendered 167 pathway records. Executed by root coordinator; this reviewer inspected the final log. |
| Documented corpus vendored | passed | False | MetaCyc:PWY0-43 | All 22 governed artifacts match pinned CLAW revision. Executed by root coordinator; this reviewer inspected the final log. |
| Working and staged diff whitespace checks | passed | True | MetaCyc:PWY0-43 | Both real read-only commands exited0 on final staged integration state. |
| Governed target/input capture and reassessment | passed | True | MetaCyc:PWY0-43 | Initial inspection preceded assessment. Final capture contains 21 inputs; only initial target changed, solely issue #324 locator, independently reconstructed and rechecked. Added authority/source/page/audit inputs were inspected. All final hashes were rechecked before completion. |
| Independent scientific source replay | passed | False | MetaCyc:PWY0-43 | Actual exit 0: full native Rhea parsing, 10 exact sides and coefficients, directed/master/bidirectional source bridges, chemical balance, canonical labels and 20 reference body hashes. Not a substitute for full corpus validators. |
| Canonical structured dataset context | passed | False | MetaCyc:PWY0-43 | Coordinator ran documented adapter commands with terminal exit 0. Reviewer read dataset and exact gene output bytes and verified recorded hashes; each query returns 1 gene / 0 module hits. No summarize is applicable and no negative biology inference is made. |
| Actual generated publication check | passed | False | MetaCyc:PWY0-43 | Assigned artifact auditor reported and preserved terminal exit 0 for separate CLI and inspected-helper audit. Sbm 22 edges/38 evidence, reference metadata, directions, source categories and corrected locator are exact in actual KGX/page; CLI bytes match downloads. Programmatic only; auditor authored Sbm and this is not used as independent scientific proof. |

## Scientific And Domain Assessments

### Exact proposed Sbm/ScpABC cycle and taxon scope

identity: supported. Targets: MetaCyc:PWY0-43.

The record faithfully denotes MetaCyc PWY0-43 as a named three-enzyme biochemical proposal. Its MG1655 annotation is separate from recombinant experimental hosts and claims no wild-type flux. It is not the sodium-pumping biotin-dependent route, a broad propionate map, or an engineered epimerase pathway.

### Exact charged chemistry and source direction

grounding: supported. Targets: MetaCyc:PWY0-43.

All 10 side occurrences, coefficients, Rhea master/bidirectional bridges and three selected directions are verified. Proton is retained in decarboxylation; cobamamide is a cofactor, not a consumed generic B12 pool. No stereochemical or protonation repair was guessed.

### Catalysts, native assemblies and AdoCbl

evidence: supported. Targets: MetaCyc:PWY0-43.

Source-mapped Sbm dimer and ScpB hexamer have supported component roles. CoA-transferase P52043 is not assigned an unsupported oligomeric state. AdoCbl support is experimental; assay MgCl2 and crystallization Ni do not establish required cofactor edges.

### Stereochemical conflict retained without gap filling

scope: supported. Targets: MetaCyc:PWY0-43.

R-specific ScpB chemistry is explicitly represented as current Rhea/UniProt annotation. The record does not claim enantiomer-resolved experimental proof: original coupled support,2017 engineered epimerase dependence and 2019 R/S assay limitations are all retained. These qualify interpretation of the cycle, rather than justify swapping R for S or inventing an endogenous epimerase.

### Bounded graph/source coverage and justified exclusions

completeness: supported. Targets: MetaCyc:PWY0-43.

All22 maintained edges and38 evidence entries were inspected. Three enzyme reactions, both supported assemblies, cofactor and three cycle material links are represented. Native flux, YgfD catalysis, heterologous epimerase, alternative sodium/biotin mechanisms, hydrolysis branch and metal/cofactor extrapolations are appropriately excluded or kept as contextual limits.

### Exact sources and corrected issue #324

provenance: supported. Targets: MetaCyc:PWY0-43.

All 20 reference body hashes match the inspected native/full-text/abstract artifacts; source types and access limits remain explicit. No direct quote is present. The one initial minor locator defect was corrected and independently rechecked before saving this immutable review; no unresolved finding remains. Global UniProt release is supported by preserved response headers.

### Final corpus contract and generated representation

schema: supported. Targets: MetaCyc:PWY0-43.

Full required gates pass; refreshed authority snapshots preserve all baseline values and independently support named identities. Generated Sbm graph/KGX retains exact scoped evidence and corrected locator. No browser visual verification is claimed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-target | data/pathways/succinate-to-propanoate.yaml; Entire maintained YAML, all 22 edges/38 evidence entries and 20 references | supports | All declared components, three reactions, all edge endpoints/predicates/evidence and reference metadata were read. Final revision retains the proposal/annotation limits and the corrected issue #324 locator. |
| ev-native | https://pathway.yeastgenome.org/getxml?META:PWY0-43; Native Pathway reaction-list/reaction-ordering/reaction-layout/species/comment; associated nine native XML objects listed in sbm-sources.json | supports | Native three-reaction cyclic proposal, MG1655 scope and explicit lack of demonstrated metabolic role match the record. Reaction native crossrefs22891/27667/28013 independently join the selected Rhea directions. CPLX0-7741 has 2 Sbm subunits, CPLX0-254 has 6 ScpB subunits; monomer objects map by UniProt unification to P27253/P52045/P52043. |
| ev-rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Release142; full RDF independently parsed, repeated-subject properties merged; 22888/22890/22891,27666/27667,28010/28011/28013 and all contains1 participant/compound objects | supports | All 10 side occurrences match exact charged ChEBI participants at coefficient1. 22890 is selected right-to-left;27667/28011 left-to-right. Elemental and charge balances pass separately; cycle cancels CoA carriers to succinate(2-)+H+→propionate+CO2. |
| ev-protein | https://rest.uniprot.org/uniprotkb/P27253.json ; https://rest.uniprot.org/uniprotkb/P52045.json ; https://rest.uniprot.org/uniprotkb/P52043.json; All FUNCTION/CATALYTIC ACTIVITY/COFACTOR/SUBUNIT comments, exact crossrefs/ECO codes, gene/locus/taxon and entryAudit; bodies listed in sbm-sources.json | supports | Reviewed K-12 proteins and catalytic Rhea masters match. P27253 homodimer and adenosylcobalamin are experimentally annotated; P52045 is a dimer of trimers and retains R-specific annotation; P52043 has no asserted oligomeric state. Global2026_03 derives from preserved selected response headers, independently compared with prior committed manifest. |
| ev-haller | PMID:10769117; DOI:10.1021/bi992888d; https://static.igem.org/mediawiki/2013/c/c1/HUST-4.pdf; Full8-page primary PDF; pp4624–4625 assay methods, pp4626–4627 functions/Table1, pp4627–4628 physiology limitations | supports | Inspected recombinant activities: AdoCbl reconstitution and coupled Sbm/YgfG assay, methylmalonyl-CoA decarboxylation, reversible propionyl-CoA/succinate CoA transfer. Donor strain1655 and BL21 host are distinct. Coupled chromatography did not establish isolated ScpB enantiomer specificity; proposed physiological context remained unknown. |
| ev-froese | PMID:18950999; https://pmc.ncbi.nlm.nih.gov/articles/PMC2741639/?pdf=render; Complete returned primary HTML; Results P17, Fig4B and4C panel2, Discussion; native expression and in-vivo interaction results | supports | Apo-Sbm is a monomer/dimer mixture; the approximate YgfD-Sbm assembly is a distinct complex. Native expression and interaction do not prove full carbon-conversion flux. Corrected edge011 locator now reaches this actual evidence. |
| ev-2017 | PMID:28716098; DOI:10.1186/s12934-017-0735-4; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5512728/fullTextXML; Primary full text: Methods strain/plasmid/medium details; Results epimerase co-expression, Tables4–5, DH5alpha experiment; Discussion | partial | BL21/DH5alpha engineered cultures required heterologous P.acidipropionici epimerase for propionate from glucose/minimal medium. This conflicts with a universally complete three-enzyme physiological cycle but does not itself identify a native epimerase or directly assay purified ScpB R-versus-S specificity. Record preserves both this and the older indirect evidence. |
| ev-2019 | DOI:10.1021/jacs.9b00650.s001; https://ndownloader.figshare.com/files/14641211; Primary supporting PDF ppS12–S15 SectionsV–VIII; FiguresS4–S5 ppS27–S28; ACS Figshare article7863569 metadata independently read | partial | Assay uses MMCD-His6 and R/S methylmalonyl-CoA, and quantifies propionyl-CoA plus hydrolysis/free CoA. S2A construct is used for crystallography. MgCl2 in assay and Ni in crystallization do not prove required catalytic metal. This supplement does not resolve enantiomer specificity. |
| ev-abstracts | PMID:10769118/DOI:10.1021/bi9928896 and PMID:11955068/DOI:10.1021/bi015593k; EuropePMC core primary-extra.json; both complete indexed abstracts | supports | Original ScpB crystal study directly reports a hexamer/dimer of trimers. Dayem 2002 supports mutase production of2R-methylmalonyl-CoA and an engineered epimerase route. No full-text or detailed kinetic claims are inferred from these abstracts. |
| ev-imodulon | research/pathway_additions/2026-10-10-citrate-sbm/imodulondb-context.json; Current-session canonical datasets then exact b2917/b2919/b2920 searches; raw output bytes inspected and compared with receipt | context_only | Each e_coli/precise_mg1655 query returned one matching scpA/scpB/scpC gene and no module hits. This is expression-dataset context only; no catalysis, regulatory relation or absence-of-module inference. No summarize call applicable. |
| ev-issue324 | https://github.com/CultureBotAI/PathwayMech/issues/324; Independent original inspection6ee1a9265b1f8e0a6392a73009815a690fdc9a8395357707aa8dc7916c049a75; edge011; primary P17/Fig4B/4C panel2; post-fix receipt | supports | Reviewer found incorrect Fig 3A/Table 2 locator (minor). Author corrected only that locator. Replacing the final locator with the originally inspected string reconstructs exact initial SHA256; final d074e8d7a820bfd22e788074de1651b62db5f7f8b584162fec14d13d5913b268 was independently checked against raw HTML. This is a pre-save correction, not fabricated structured-review lineage. |
| ev-replay | /private/tmp/pathwaymech-citrate-sbm-evidence/sbm-review/replay.py; Independent reviewer source replay; replay.json/replay.log | supports | Independent full-RDF side/direction/master bridge/formula-charge checks, canonical ChEBI/Rhea/taxon/protein labels and every referenced raw-body SHA256 passed. The target differs from initial replay only by separately rechecked issue #324 locator. |
| ev-search | Bounded public literature search2026-10-10; Queries: ScpB methylmalonyl CoA decarboxylase stereospecificity R S2019 2025; ygfG epimerase2024 | context_only | Search used only as a lead check. Returned primary sources were the inspected2017/2019 studies or different proteins/taxa; no additional exact claim was added from snippets. Not an exhaustive literature-absence finding. |
| ev-gate-validate | /private/tmp/pathwaymech-citrate-sbm-validate.log; Actual coordinator terminal execution log; exit0 confirmed by coordinator | supports | 167 native and closed-schema records; identifier/label policies, 8731 evidence blocks, 30 sources, 248 histories, documentation/research and current pages passed. |
| ev-gate-test | /private/tmp/pathwaymech-citrate-sbm-test.log; Actual coordinator terminal execution log; exit0 confirmed by coordinator | supports | 1043 passed, 3 skipped, 3 upstream deprecation warnings in 351.55 seconds. |
| ev-gate-lint | /private/tmp/pathwaymech-citrate-sbm-lint.log; Actual coordinator terminal execution log; exit0 confirmed by coordinator | supports | Ruff: all checks passed. |
| ev-gate-render | /private/tmp/pathwaymech-citrate-sbm-render.log; Actual coordinator terminal execution log; exit0 confirmed by coordinator | supports | Rendered 167 pathway records. |
| ev-gate-vendored | /private/tmp/pathwaymech-citrate-sbm-vendored.log; Actual coordinator terminal execution log; exit0 confirmed by coordinator | supports | All 22 governed artifacts match pinned CLAW revision. |
| ev-graph | research/pathway_additions/2026-10-10-citrate-sbm/generated-graph-kgx-audit.json; Sbm target entry and complete publication audit, actual logs/source hashes | supports | 22 Sbm edges, 38 evidence and 17 SVG nodes / 18 named scope nodes preserved; exact node directions/categories/contexts, endpoints, anchors, geometry and reference metadata checked. Corrected issue #324 locator independently seen on page; no browser or visual interaction claim. |
| ev-authorities | research/pathway_additions/2026-10-10-citrate-sbm/authority-integration.json; Canonical regeneration receipt plus independent reviewer comparison against Gitbase722257adc1882495f8454cc229b8fa0c187cf868 | supports | Reviewer independently compared every pre-existing term/source JSON value in both snapshots with base; all retained unchanged. New target identities match independently read Rhea/ChEBI/UniProt/native source values. This tests identity/provenance, not biochemical truth. |

## Limits And Additional Notes

- This is a qualified assessment of a proposed biochemical route, not proof of native physiological operation.
- ScpB R-specific annotation is not an enantiomer-resolved experiment; the 2017 engineered-strain conflict remains unresolved and 2019 uses an R/S mixture.
- PMID:10769118 and PMID:11955068 were inspected as complete indexed abstracts; 2019 main article full text was unavailable, while its original primary supplement was inspected.
- Bounded literature search is not an exhaustive claim that no later source exists.
- Full required checks were executed by the coordinator and their final logs inspected by this reviewer. The programmatic graph audit is structural, not an independent scientific review or browser visual test.
- Issue #324 was discovered during this review before any immutable predecessor was saved. Initial SHA 6ee1a9265b1f8e0a6392a73009815a690fdc9a8395357707aa8dc7916c049a75 and final SHA d074e8d7a820bfd22e788074de1651b62db5f7f8b584162fec14d13d5913b268 are preserved in evidence-linked assessment, without invented resolved-finding lineage.
- Initial external helper invocations using system Python lacked optional lxml/unused PyYAML imports; no target assertion or check outcome depended on those failed reads. Standard-library parsing and repository interpreter were used successfully.
- Generated-input ownership: pages/records/MetaCyc_PWY0-43.html is generated from the maintained target by src/pathwaymech/cli.py and src/pathwaymech/graph_view.py; KGX downloads are owned by src/pathwaymech/kgx.py. Source snapshots are canonical-builder output from conf/identifier_sources.json and verified raw authorities; fixes must target those maintained owners rather than edit generated pages.
- Review findings list is empty for final corrected bytes. Initial minor finding and evidence-backed post-fix check remain explicitly recorded in the issue #324 assessment; this does not imply fleet-wide scientific coverage.
- Initial review-content validation rejected YAML aliases produced by the serializer. Serialization was corrected to emit no anchors or aliases; no target or scientific assertion changed. Canonical validation was then repeated before save.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T231218Z-sbm-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of proposed Sbm succinate-to-propanoate cycle
started_at: '2026-10-10T23:02:16Z'
finished_at: '2026-10-10T23:12:18Z'
reviewer:
  identity: Codex /root/pathway_literature_candidates
  kind: agent
  independence: independent
  independence_basis: This reviewer did not author the Sbm record or its source projections.
    It independently read the entire target and primary/native source bodies, replayed
    identities/chemistry, found issue324, and verified the author correction. It authored
    the separate citrate record in the same batch.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'The proposed three-enzyme cycle is grounded in sources with explicit unresolved
  ScpB stereochemistry and physiological-flux limits. One initial minor citation locator
  defect was corrected under issue #324 and independently verified before save; no
  unresolved finding remains. Required corpus validation, tests and lint passed on
  frozen inputs.'
source:
  git_revision: 722257adc1882495f8454cc229b8fa0c187cf868
  state: working_tree
  inputs:
  - path: .claude/skills/add-pathway/SKILL.md
    sha256: 296ab1a206afa3aa9b487eae7f5f8d836c09001a4ce9ee8016c36abe198cdc0d
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 6a57ac6065171e35499578522a38c576e7bf7b6213286487d6cc0947fc477f3f
    role: context
  - path: conf/identifier_policy.yaml
    sha256: d1d18735600fe87f44822cfbc2448c82c10764fec2d45a9780a52c694a892d63
    role: context
  - path: conf/identifier_sources.json
    sha256: 33192380665155203ef45ef7d6a143078dc030bbfd281754f383d602107175d5
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 1d4a27d8e22ebe51808d4b0e180f57818e0693263c9eaa768019693bf35c596a
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 12ef38773f0fe35a8df5a923775efeea6130f092c785cda45f0dfd30bfc90ae2
    role: context
  - path: data/pathways/succinate-to-propanoate.yaml
    sha256: d074e8d7a820bfd22e788074de1651b62db5f7f8b584162fec14d13d5913b268
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 3c861f2ab78e3bc62146d05af5ed5c4c4ae3e65343fc9bd44afa76da7f0b62e7
    role: context
  - path: docs/CURATION.md
    sha256: 408f7c7705b4e6d667b513920e4c39612162d549e0c2666d85bfd53b2c2687f7
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 3af37b2e92b0103da74bc462bedda1021c6bd262d3da13c030eb47344d08b61f
    role: context
  - path: pages/records/MetaCyc_PWY0-43.html
    sha256: b6007a7686368ed4d2bbfcb29902065a937b33527d0b04b667084514f49a60f9
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/authority-integration.json
    sha256: 46371b13cc93b314b41f59583370ec4dea718b23fb98c16fc521bcb7ad5e764c
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/generated-graph-kgx-audit.json
    sha256: 7dd446cd0b98282d0986c31661f6d217d824fbf036af1cc903406bb44e507dfd
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/imodulondb-context.json
    sha256: e49c7b0a498e9af1cda54a961bc37989e3a034f922043f44e21a73300957040f
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/sbm-chemistry.json
    sha256: 0258ad4d0c7ae0f8f5edf0d3d3fcb0ac84b5d43f132551e4b8800645e94e6cec
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/sbm-curation.md
    sha256: 1452ec36f37e6c27687773c05fda5d0186718eb8e38aef0f123596c66e8c65f2
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/sbm-native-projection.json
    sha256: 74850ab6a22b622c3fdfacac2d24d1119879023a8174ecd6b174d67ea39d96d1
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/sbm-protein-projection.json
    sha256: 6df303f9e9efa99f13d4bb7778f49aa549480ac11fe739e98e074d438b163c96
    role: context
  - path: research/pathway_additions/2026-10-10-citrate-sbm/sbm-sources.json
    sha256: abb7c7c5c784486399984473d11b0c74ddb5f1a61ffa3bd8638168d48ccd2586
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
scope:
  description: One exact maintained Sbm record, all nodes/edges/evidence/references;
    source-grounded scientific assessment plus final integration validation.
  selection: Explicit parent assignment of data/pathways/succinate-to-propanoate.yaml,
    MetaCyc:PWY0-43
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY0-43
  exclusions:
  - target: Other pathway records, including citrate
    reason: Outside this scientific review; full gates cover corpus structure, not
      corpus-wide scientific truth.
  - target: Detailed stereochemical kinetic determination and native physiological
      flux
    reason: Not resolved by inspected primary literature; no new experimental claim.
targets:
- target_id: MetaCyc:PWY0-43
  path: data/pathways/succinate-to-propanoate.yaml
  label: conversion of succinate to propanoate
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/succinate-to-propanoate.yaml
    role: maintained pathway YAML
checks:
- check_id: validate
  name: Documented corpus validate
  status: passed
  required: true
  summary: 167 native and closed-schema records; identifier/label policies, 8731 evidence
    blocks, 30 sources, 248 histories, documentation/research and current pages passed.
    Executed by root coordinator; this reviewer inspected the final log.
  target_ids:
  - MetaCyc:PWY0-43
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-gate-validate
- check_id: test
  name: Documented corpus test
  status: passed
  required: true
  summary: 1043 passed, 3 skipped, 3 upstream deprecation warnings in 351.55 seconds.
    Executed by root coordinator; this reviewer inspected the final log.
  target_ids:
  - MetaCyc:PWY0-43
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-gate-test
- check_id: lint
  name: Documented corpus lint
  status: passed
  required: true
  summary: 'Ruff: all checks passed. Executed by root coordinator; this reviewer inspected
    the final log.'
  target_ids:
  - MetaCyc:PWY0-43
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-gate-lint
- check_id: render
  name: Documented corpus render
  status: passed
  required: false
  summary: Rendered 167 pathway records. Executed by root coordinator; this reviewer
    inspected the final log.
  target_ids:
  - MetaCyc:PWY0-43
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-gate-render
- check_id: vendored
  name: Documented corpus vendored
  status: passed
  required: false
  summary: All 22 governed artifacts match pinned CLAW revision. Executed by root
    coordinator; this reviewer inspected the final log.
  target_ids:
  - MetaCyc:PWY0-43
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    vendored-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-gate-vendored
- check_id: diff
  name: Working and staged diff whitespace checks
  status: passed
  required: true
  summary: Both real read-only commands exited0 on final staged integration state.
  target_ids:
  - MetaCyc:PWY0-43
  command: git diff --check && git diff --cached --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-target
- check_id: inspect
  name: Governed target/input capture and reassessment
  status: passed
  required: true
  summary: 'Initial inspection preceded assessment. Final capture contains 21 inputs;
    only initial target changed, solely issue #324 locator, independently reconstructed
    and rechecked. Added authority/source/page/audit inputs were inspected. All final
    hashes were rechecked before completion.'
  target_ids:
  - MetaCyc:PWY0-43
  command: uv run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-citrate-sbm-evidence/sbm-review/targets.yaml
    (with exact --input list retained in final-inspect.py)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-target
  - ev-issue324
- check_id: replay
  name: Independent scientific source replay
  status: passed
  required: false
  summary: 'Actual exit 0: full native Rhea parsing, 10 exact sides and coefficients,
    directed/master/bidirectional source bridges, chemical balance, canonical labels
    and 20 reference body hashes. Not a substitute for full corpus validators.'
  target_ids:
  - MetaCyc:PWY0-43
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 .venv/bin/python
    /private/tmp/pathwaymech-citrate-sbm-evidence/sbm-review/replay.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-replay
  - ev-rhea
- check_id: imodulon
  name: Canonical structured dataset context
  status: passed
  required: false
  summary: Coordinator ran documented adapter commands with terminal exit 0. Reviewer
    read dataset and exact gene output bytes and verified recorded hashes; each query
    returns 1 gene / 0 module hits. No summarize is applicable and no negative biology
    inference is made.
  target_ids:
  - MetaCyc:PWY0-43
  command: kg-microbe-sources imodulondb datasets; kg-microbe-sources imodulondb search
    --organism e_coli --dataset precise_mg1655 --query b2917/b2919/b2920 (three separate
    queries)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-imodulon
- check_id: kgx
  name: Actual generated publication check
  status: passed
  required: false
  summary: Assigned artifact auditor reported and preserved terminal exit 0 for separate
    CLI and inspected-helper audit. Sbm 22 edges/38 evidence, reference metadata,
    directions, source categories and corrected locator are exact in actual KGX/page;
    CLI bytes match downloads. Programmatic only; auditor authored Sbm and this is
    not used as independent scientific proof.
  target_ids:
  - MetaCyc:PWY0-43
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-citrate-sbm-kgx; .venv/bin/python
    /private/tmp/pathwaymech-citrate-sbm-graph-audit.py --root /private/tmp/pathwaymech-citrate-sbm-20261010
    --comparison-kgx-dir /private/tmp/pathwaymech-citrate-sbm-kgx
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-graph
evidence:
- evidence_id: ev-target
  kind: record_content
  reference: data/pathways/succinate-to-propanoate.yaml
  locator: Entire maintained YAML, all 22 edges/38 evidence entries and 20 references
  accessed_at: '2026-10-10T23:05:50Z'
  support: supports
  summary: 'All declared components, three reactions, all edge endpoints/predicates/evidence
    and reference metadata were read. Final revision retains the proposal/annotation
    limits and the corrected issue #324 locator.'
  snapshot_sha256: d074e8d7a820bfd22e788074de1651b62db5f7f8b584162fec14d13d5913b268
- evidence_id: ev-native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY0-43
  locator: Native Pathway reaction-list/reaction-ordering/reaction-layout/species/comment;
    associated nine native XML objects listed in sbm-sources.json
  accessed_at: '2026-10-10T23:05:50Z'
  support: supports
  summary: Native three-reaction cyclic proposal, MG1655 scope and explicit lack of
    demonstrated metabolic role match the record. Reaction native crossrefs22891/27667/28013
    independently join the selected Rhea directions. CPLX0-7741 has 2 Sbm subunits,
    CPLX0-254 has 6 ScpB subunits; monomer objects map by UniProt unification to P27253/P52045/P52043.
  snapshot_sha256: 4a16c5ff09d436aacfe989620832fbda176740ab625ca479dbc2612eae11a151
- evidence_id: ev-rhea
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Release142; full RDF independently parsed, repeated-subject properties
    merged; 22888/22890/22891,27666/27667,28010/28011/28013 and all contains1 participant/compound
    objects
  accessed_at: '2026-10-10T23:05:50Z'
  support: supports
  summary: All 10 side occurrences match exact charged ChEBI participants at coefficient1.
    22890 is selected right-to-left;27667/28011 left-to-right. Elemental and charge
    balances pass separately; cycle cancels CoA carriers to succinate(2-)+H+→propionate+CO2.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: ev-protein
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P27253.json ; https://rest.uniprot.org/uniprotkb/P52045.json
    ; https://rest.uniprot.org/uniprotkb/P52043.json
  locator: All FUNCTION/CATALYTIC ACTIVITY/COFACTOR/SUBUNIT comments, exact crossrefs/ECO
    codes, gene/locus/taxon and entryAudit; bodies listed in sbm-sources.json
  accessed_at: '2026-10-10T23:05:50Z'
  support: supports
  summary: Reviewed K-12 proteins and catalytic Rhea masters match. P27253 homodimer
    and adenosylcobalamin are experimentally annotated; P52045 is a dimer of trimers
    and retains R-specific annotation; P52043 has no asserted oligomeric state. Global2026_03
    derives from preserved selected response headers, independently compared with
    prior committed manifest.
  snapshot_sha256: 6df303f9e9efa99f13d4bb7778f49aa549480ac11fe739e98e074d438b163c96
- evidence_id: ev-haller
  kind: primary_source
  reference: PMID:10769117; DOI:10.1021/bi992888d; https://static.igem.org/mediawiki/2013/c/c1/HUST-4.pdf
  locator: Full8-page primary PDF; pp4624–4625 assay methods, pp4626–4627 functions/Table1,
    pp4627–4628 physiology limitations
  accessed_at: '2026-10-10T23:05:50Z'
  support: supports
  summary: 'Inspected recombinant activities: AdoCbl reconstitution and coupled Sbm/YgfG
    assay, methylmalonyl-CoA decarboxylation, reversible propionyl-CoA/succinate CoA
    transfer. Donor strain1655 and BL21 host are distinct. Coupled chromatography
    did not establish isolated ScpB enantiomer specificity; proposed physiological
    context remained unknown.'
  snapshot_sha256: d7a629eba85789aacbd57a4b813867c68f16e28d9ac9ef603ff40a4da9a40492
- evidence_id: ev-froese
  kind: primary_source
  reference: PMID:18950999; https://pmc.ncbi.nlm.nih.gov/articles/PMC2741639/?pdf=render
  locator: Complete returned primary HTML; Results P17, Fig4B and4C panel2, Discussion;
    native expression and in-vivo interaction results
  accessed_at: '2026-10-10T23:05:50Z'
  support: supports
  summary: Apo-Sbm is a monomer/dimer mixture; the approximate YgfD-Sbm assembly is
    a distinct complex. Native expression and interaction do not prove full carbon-conversion
    flux. Corrected edge011 locator now reaches this actual evidence.
  snapshot_sha256: dfda3e02e329753cf3db0d38473e24b0c7a97555f411de1ee91a8a7bd308e013
- evidence_id: ev-2017
  kind: primary_source
  reference: PMID:28716098; DOI:10.1186/s12934-017-0735-4; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5512728/fullTextXML
  locator: 'Primary full text: Methods strain/plasmid/medium details; Results epimerase
    co-expression, Tables4–5, DH5alpha experiment; Discussion'
  accessed_at: '2026-10-10T23:05:50Z'
  support: partial
  summary: BL21/DH5alpha engineered cultures required heterologous P.acidipropionici
    epimerase for propionate from glucose/minimal medium. This conflicts with a universally
    complete three-enzyme physiological cycle but does not itself identify a native
    epimerase or directly assay purified ScpB R-versus-S specificity. Record preserves
    both this and the older indirect evidence.
  snapshot_sha256: 65cdfdcf56021b9e915e3013da82cc731379455e71df92a9e35ab35c167113cf
- evidence_id: ev-2019
  kind: primary_source
  reference: DOI:10.1021/jacs.9b00650.s001; https://ndownloader.figshare.com/files/14641211
  locator: Primary supporting PDF ppS12–S15 SectionsV–VIII; FiguresS4–S5 ppS27–S28;
    ACS Figshare article7863569 metadata independently read
  accessed_at: '2026-10-10T23:05:50Z'
  support: partial
  summary: Assay uses MMCD-His6 and R/S methylmalonyl-CoA, and quantifies propionyl-CoA
    plus hydrolysis/free CoA. S2A construct is used for crystallography. MgCl2 in
    assay and Ni in crystallization do not prove required catalytic metal. This supplement
    does not resolve enantiomer specificity.
  snapshot_sha256: b979ec82a7ffc27790053dac5949f67c4bb99d91db827f6445bfb788b79aa1b2
- evidence_id: ev-abstracts
  kind: primary_source
  reference: PMID:10769118/DOI:10.1021/bi9928896 and PMID:11955068/DOI:10.1021/bi015593k
  locator: EuropePMC core primary-extra.json; both complete indexed abstracts
  accessed_at: '2026-10-10T23:05:50Z'
  support: supports
  summary: Original ScpB crystal study directly reports a hexamer/dimer of trimers.
    Dayem 2002 supports mutase production of2R-methylmalonyl-CoA and an engineered
    epimerase route. No full-text or detailed kinetic claims are inferred from these
    abstracts.
  snapshot_sha256: d9ccd88e2de20db134af2d13aee3d42b8c86262c58db485f4f863722dc49fd33
- evidence_id: ev-imodulon
  kind: database
  reference: research/pathway_additions/2026-10-10-citrate-sbm/imodulondb-context.json
  locator: Current-session canonical datasets then exact b2917/b2919/b2920 searches;
    raw output bytes inspected and compared with receipt
  accessed_at: '2026-10-10T23:05:50Z'
  support: context_only
  summary: Each e_coli/precise_mg1655 query returned one matching scpA/scpB/scpC gene
    and no module hits. This is expression-dataset context only; no catalysis, regulatory
    relation or absence-of-module inference. No summarize call applicable.
  snapshot_sha256: e49c7b0a498e9af1cda54a961bc37989e3a034f922043f44e21a73300957040f
- evidence_id: ev-issue324
  kind: validation
  reference: https://github.com/CultureBotAI/PathwayMech/issues/324
  locator: Independent original inspection6ee1a9265b1f8e0a6392a73009815a690fdc9a8395357707aa8dc7916c049a75;
    edge011; primary P17/Fig4B/4C panel2; post-fix receipt
  accessed_at: '2026-10-10T23:05:50Z'
  support: supports
  summary: Reviewer found incorrect Fig 3A/Table 2 locator (minor). Author corrected
    only that locator. Replacing the final locator with the originally inspected string
    reconstructs exact initial SHA256; final d074e8d7a820bfd22e788074de1651b62db5f7f8b584162fec14d13d5913b268
    was independently checked against raw HTML. This is a pre-save correction, not
    fabricated structured-review lineage.
  snapshot_sha256: f207ccc8a5913099cb6eddf78ae59fb9645a2516f5e086c62eafed74a15487b8
- evidence_id: ev-replay
  kind: validation
  reference: /private/tmp/pathwaymech-citrate-sbm-evidence/sbm-review/replay.py
  locator: Independent reviewer source replay; replay.json/replay.log
  accessed_at: '2026-10-10T23:05:50Z'
  support: supports
  summary: 'Independent full-RDF side/direction/master bridge/formula-charge checks,
    canonical ChEBI/Rhea/taxon/protein labels and every referenced raw-body SHA256
    passed. The target differs from initial replay only by separately rechecked issue
    #324 locator.'
  snapshot_sha256: e8a1c4765893e31f3ac69e60dc3565cbff0f4871864e8356276cf0f884459a83
- evidence_id: ev-search
  kind: search
  reference: Bounded public literature search2026-10-10
  locator: 'Queries: ScpB methylmalonyl CoA decarboxylase stereospecificity R S2019
    2025; ygfG epimerase2024'
  accessed_at: '2026-10-10T23:05:50Z'
  support: context_only
  summary: Search used only as a lead check. Returned primary sources were the inspected2017/2019
    studies or different proteins/taxa; no additional exact claim was added from snippets.
    Not an exhaustive literature-absence finding.
  search_scope: Two bounded web queries; local repository absence claims are not based
    on this search. Primary source inspection, not snippet support, determines the
    verdict.
- evidence_id: ev-gate-validate
  kind: validation
  reference: /private/tmp/pathwaymech-citrate-sbm-validate.log
  locator: Actual coordinator terminal execution log; exit0 confirmed by coordinator
  accessed_at: '2026-10-10T23:12:18Z'
  support: supports
  summary: 167 native and closed-schema records; identifier/label policies, 8731 evidence
    blocks, 30 sources, 248 histories, documentation/research and current pages passed.
  snapshot_sha256: 71b37f71dd760991ef7b9ae6b2bc0802f3063ab62d3185afd8f3c92be5bd4f15
- evidence_id: ev-gate-test
  kind: validation
  reference: /private/tmp/pathwaymech-citrate-sbm-test.log
  locator: Actual coordinator terminal execution log; exit0 confirmed by coordinator
  accessed_at: '2026-10-10T23:12:18Z'
  support: supports
  summary: 1043 passed, 3 skipped, 3 upstream deprecation warnings in 351.55 seconds.
  snapshot_sha256: f8fc42dab2ef354b53bcf49ba77007711700f8340597d06ce0c00630a49e19b0
- evidence_id: ev-gate-lint
  kind: validation
  reference: /private/tmp/pathwaymech-citrate-sbm-lint.log
  locator: Actual coordinator terminal execution log; exit0 confirmed by coordinator
  accessed_at: '2026-10-10T23:12:18Z'
  support: supports
  summary: 'Ruff: all checks passed.'
  snapshot_sha256: df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41
- evidence_id: ev-gate-render
  kind: validation
  reference: /private/tmp/pathwaymech-citrate-sbm-render.log
  locator: Actual coordinator terminal execution log; exit0 confirmed by coordinator
  accessed_at: '2026-10-10T23:12:18Z'
  support: supports
  summary: Rendered 167 pathway records.
  snapshot_sha256: fda3f26afc96f351f927b3d8311c050e644c49a3dd847affdaeaeb99e804c710
- evidence_id: ev-gate-vendored
  kind: validation
  reference: /private/tmp/pathwaymech-citrate-sbm-vendored.log
  locator: Actual coordinator terminal execution log; exit0 confirmed by coordinator
  accessed_at: '2026-10-10T23:12:18Z'
  support: supports
  summary: All 22 governed artifacts match pinned CLAW revision.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: ev-graph
  kind: validation
  reference: research/pathway_additions/2026-10-10-citrate-sbm/generated-graph-kgx-audit.json
  locator: Sbm target entry and complete publication audit, actual logs/source hashes
  accessed_at: '2026-10-10T23:12:18Z'
  support: supports
  summary: '22 Sbm edges, 38 evidence and 17 SVG nodes / 18 named scope nodes preserved;
    exact node directions/categories/contexts, endpoints, anchors, geometry and reference
    metadata checked. Corrected issue #324 locator independently seen on page; no
    browser or visual interaction claim.'
  snapshot_sha256: 7dd446cd0b98282d0986c31661f6d217d824fbf036af1cc903406bb44e507dfd
- evidence_id: ev-authorities
  kind: validation
  reference: research/pathway_additions/2026-10-10-citrate-sbm/authority-integration.json
  locator: Canonical regeneration receipt plus independent reviewer comparison against
    Gitbase722257adc1882495f8454cc229b8fa0c187cf868
  accessed_at: '2026-10-10T23:12:18Z'
  support: supports
  summary: Reviewer independently compared every pre-existing term/source JSON value
    in both snapshots with base; all retained unchanged. New target identities match
    independently read Rhea/ChEBI/UniProt/native source values. This tests identity/provenance,
    not biochemical truth.
  snapshot_sha256: 46371b13cc93b314b41f59583370ec4dea718b23fb98c16fc521bcb7ad5e764c
assessments:
- assessment_id: identity
  area: identity
  topic: Exact proposed Sbm/ScpABC cycle and taxon scope
  outcome: supported
  summary: The record faithfully denotes MetaCyc PWY0-43 as a named three-enzyme biochemical
    proposal. Its MG1655 annotation is separate from recombinant experimental hosts
    and claims no wild-type flux. It is not the sodium-pumping biotin-dependent route,
    a broad propionate map, or an engineered epimerase pathway.
  target_ids:
  - MetaCyc:PWY0-43
  evidence_ids:
  - ev-target
  - ev-native
  - ev-haller
  - ev-2017
  dimensions:
  - name: taxon-scope
    value: NCBITaxon:511145 annotated route; recombinant1655-derived proteins/BL21
      host;2017 BL21 and DH5alpha engineering
    definition: Separates source-organism identity, protein experimental context and
      physiological claim scope
    evidence_ids:
    - ev-native
    - ev-haller
    - ev-2017
- assessment_id: chemistry
  area: grounding
  topic: Exact charged chemistry and source direction
  outcome: supported
  summary: All 10 side occurrences, coefficients, Rhea master/bidirectional bridges
    and three selected directions are verified. Proton is retained in decarboxylation;
    cobamamide is a cofactor, not a consumed generic B12 pool. No stereochemical or
    protonation repair was guessed.
  target_ids:
  - MetaCyc:PWY0-43
  evidence_ids:
  - ev-rhea
  - ev-target
  - ev-replay
- assessment_id: enzymes
  area: evidence
  topic: Catalysts, native assemblies and AdoCbl
  outcome: supported
  summary: Source-mapped Sbm dimer and ScpB hexamer have supported component roles.
    CoA-transferase P52043 is not assigned an unsupported oligomeric state. AdoCbl
    support is experimental; assay MgCl2 and crystallization Ni do not establish required
    cofactor edges.
  target_ids:
  - MetaCyc:PWY0-43
  evidence_ids:
  - ev-native
  - ev-protein
  - ev-haller
  - ev-froese
  - ev-abstracts
  - ev-2019
- assessment_id: conflict
  area: scope
  topic: Stereochemical conflict retained without gap filling
  outcome: supported
  summary: 'R-specific ScpB chemistry is explicitly represented as current Rhea/UniProt
    annotation. The record does not claim enantiomer-resolved experimental proof:
    original coupled support,2017 engineered epimerase dependence and 2019 R/S assay
    limitations are all retained. These qualify interpretation of the cycle, rather
    than justify swapping R for S or inventing an endogenous epimerase.'
  target_ids:
  - MetaCyc:PWY0-43
  evidence_ids:
  - ev-target
  - ev-protein
  - ev-haller
  - ev-2017
  - ev-2019
  dimensions:
  - name: evidence-tier
    value: Reviewed structured annotation with indirect coupled assay support and
      explicitly unresolved experimental stereospecificity
    definition: Strength and limitations of the R-specific ScpB assignment
    evidence_ids:
    - ev-protein
    - ev-haller
    - ev-2017
    - ev-2019
- assessment_id: coverage
  area: completeness
  topic: Bounded graph/source coverage and justified exclusions
  outcome: supported
  summary: All22 maintained edges and38 evidence entries were inspected. Three enzyme
    reactions, both supported assemblies, cofactor and three cycle material links
    are represented. Native flux, YgfD catalysis, heterologous epimerase, alternative
    sodium/biotin mechanisms, hydrolysis branch and metal/cofactor extrapolations
    are appropriately excluded or kept as contextual limits.
  target_ids:
  - MetaCyc:PWY0-43
  evidence_ids:
  - ev-target
  - ev-native
  - ev-haller
  - ev-froese
  - ev-2019
  - ev-imodulon
- assessment_id: provenance
  area: provenance
  topic: 'Exact sources and corrected issue #324'
  outcome: supported
  summary: All 20 reference body hashes match the inspected native/full-text/abstract
    artifacts; source types and access limits remain explicit. No direct quote is
    present. The one initial minor locator defect was corrected and independently
    rechecked before saving this immutable review; no unresolved finding remains.
    Global UniProt release is supported by preserved response headers.
  target_ids:
  - MetaCyc:PWY0-43
  evidence_ids:
  - ev-target
  - ev-replay
  - ev-issue324
  - ev-protein
  - ev-abstracts
- assessment_id: integration
  area: schema
  topic: Final corpus contract and generated representation
  outcome: supported
  summary: Full required gates pass; refreshed authority snapshots preserve all baseline
    values and independently support named identities. Generated Sbm graph/KGX retains
    exact scoped evidence and corrected locator. No browser visual verification is
    claimed.
  target_ids:
  - MetaCyc:PWY0-43
  evidence_ids:
  - ev-gate-validate
  - ev-gate-test
  - ev-gate-lint
  - ev-graph
  - ev-authorities
findings: []
actions: []
limitations:
- This is a qualified assessment of a proposed biochemical route, not proof of native
  physiological operation.
- ScpB R-specific annotation is not an enantiomer-resolved experiment; the 2017 engineered-strain
  conflict remains unresolved and 2019 uses an R/S mixture.
- PMID:10769118 and PMID:11955068 were inspected as complete indexed abstracts; 2019
  main article full text was unavailable, while its original primary supplement was
  inspected.
- Bounded literature search is not an exhaustive claim that no later source exists.
- Full required checks were executed by the coordinator and their final logs inspected
  by this reviewer. The programmatic graph audit is structural, not an independent
  scientific review or browser visual test.
notes:
- 'Issue #324 was discovered during this review before any immutable predecessor was
  saved. Initial SHA 6ee1a9265b1f8e0a6392a73009815a690fdc9a8395357707aa8dc7916c049a75
  and final SHA d074e8d7a820bfd22e788074de1651b62db5f7f8b584162fec14d13d5913b268 are
  preserved in evidence-linked assessment, without invented resolved-finding lineage.'
- Initial external helper invocations using system Python lacked optional lxml/unused
  PyYAML imports; no target assertion or check outcome depended on those failed reads.
  Standard-library parsing and repository interpreter were used successfully.
- 'Generated-input ownership: pages/records/MetaCyc_PWY0-43.html is generated from
  the maintained target by src/pathwaymech/cli.py and src/pathwaymech/graph_view.py;
  KGX downloads are owned by src/pathwaymech/kgx.py. Source snapshots are canonical-builder
  output from conf/identifier_sources.json and verified raw authorities; fixes must
  target those maintained owners rather than edit generated pages.'
- 'Review findings list is empty for final corrected bytes. Initial minor finding
  and evidence-backed post-fix check remain explicitly recorded in the issue #324
  assessment; this does not imply fleet-wide scientific coverage.'
- Initial review-content validation rejected YAML aliases produced by the serializer.
  Serialization was corrected to emit no anchors or aliases; no target or scientific
  assertion changed. Canonical validation was then repeated before save.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/324
```

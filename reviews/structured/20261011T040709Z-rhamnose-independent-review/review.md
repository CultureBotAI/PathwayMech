# Independent scientific review of dTDP-rhamnose biosynthesis

- Review: 20261011T040709Z-rhamnose-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T03:54:02.421394Z
- Finished UTC: 2026-10-11T04:07:09.318263Z
- Reviewer: Codex /root/verify_graph_publication (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete four-step native dTDP-rhamnose route, all 31 edges and 67 evidence entries are supported with explicit direct-versus-inferred evidence, strain, assay and assembly limits. No findings. Final shared QC, identifiers, lint and graph checks pass. The initial full test run had one stale-site failure; its final stable-page rerun passed. A fresh full-suite pass is not claimed.

## Scope And Provenance

Complete one-record review: 19 participants, 4 reactions, 31 edges, 67 evidence entries and 21 references.

Selection: Root assigned the frozen exact target; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 407f1e2d992494f4a61ba336bedfc24155ea5574.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0019305 | data/pathways/dtdp-l-rhamnose-biosynthesis.yaml | maintained | dTDP-rhamnose biosynthetic process |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical capture and final unchanged-input verification | passed | True | GO:0019305 | Initial canonical inspection preceded scientific assessment. All eight initial target/dossier hashes still match. Final added shared inputs were inspected, and every final command-log and supporting-receipt hash was independently rechecked. |
| Independent original-source and chemistry replay | passed | True | GO:0019305 | Actual reviewer replay exited 0: full native route and assemblies, all source hashes/reference digests, exact Rhea family triples and 15 chemical sides, four balances, reviewed protein locators and per-edge evidence. Manual assessment accompanies the mechanical replay. |
| Shared final validate | passed | True | GO:0019305 | Root actually executed this command; reviewer inspected the original log and verified its SHA-256 against the sealed receipt. /private/tmp/pathwaymech-next-186-validate.log SHA256 5051636db304c924a912bd2de42fdb946fcc26993ccd601572d5f9fe4bc23635 |
| Shared final lint | passed | True | GO:0019305 | Root actually executed this command; reviewer inspected the original log and verified its SHA-256 against the sealed receipt. /private/tmp/pathwaymech-next-186-lint.log SHA256 df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41 |
| Shared final identifiers | passed | True | GO:0019305 | Root actually executed this command; reviewer inspected the original log and verified its SHA-256 against the sealed receipt. /private/tmp/pathwaymech-next-186-identifiers.log SHA256 2db33e23e4fe99e63540609fc45ab3dcb523e564f276b19f7dfd44de0bf4f614 |
| Shared final kgx | passed | True | GO:0019305 | Root actually executed this command; reviewer inspected the original log and verified its SHA-256 against the sealed receipt. /private/tmp/pathwaymech-next-186-kgx.log SHA256 1b214a9aa255c5d1f80b7e1a0b81836af1cb17d28730403d76665f4bbb094400 |
| Shared final diff | passed | True | GO:0019305 | Root actually executed this command; reviewer inspected the original log and verified its SHA-256 against the sealed receipt. /private/tmp/pathwaymech-next-186-diff.log SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| Initial full test run (retained failed attempt) | failed | False | GO:0019305 | Actual exit 1: 1 failed, 1047 passed, 3 skipped, 3 warnings in 510.51 s. Sole failure tests/test_render_pages.py::test_the_committed_site_is_current reported pages/index.html and phenylethylamine page stale while another record evidence correction and rendering overlapped. This superseded attempt is retained, not relabeled a full-suite pass. |
| Final targeted resolution of the sole failed test | passed | True | GO:0019305 | Actual exit 0, 1 passed in 47.14 s on stable final record/page state. Alongside the unchanged-code 1047 prior passes this resolves the observed local failure; no final full-suite run occurred. Exact-head CI remains a publication gate. |
| Generated SVG and KGX evidence parity | passed | True | GO:0019305 | Final root audit verifies all 31 rhamnose triples and 67 evidence blocks, endpoints, anchors, geometry and separate CLI parity. Browser was unavailable; no visual interaction claim. |
| Structured expression-context replay | passed | False | GO:0019305 | Console runner unavailable and initial DNS failure are preserved. Authorized unchanged-client retry and offline replay exited 0. Exact rfbA/B/C/D gene hits are contextual; six broad substring component hits have no selected rhamnose members. This is not global absence or biochemical evidence. |

## Scientific And Domain Assessments

### Complete exact pathway boundary

identity: supported. Targets: GO:0019305.

GO0019305 identity is consistent with the full native4step route; nucleotide sugar endpoint and distinct peripheral routes are explicit.

### All reaction sides and source-relative directions

grounding: supported. Targets: GO:0019305.

All15sides,4balances and3sharedintermediates match actualRDF; RmlD reverse master orientation remains explicit.

### Exact protein and evidentiary tier

evidence: supported. Targets: GO:0019305.

RmlA experimental versus RmlB/RmlC/RmlD inference and probable distinctions are preserved per edge.

### Native assemblies and cofactor assertions

representation: supported. Targets: GO:0019305.

Two verified native assemblies, RmlA4 andRmlB2 copies, have exact monomer crosswalks. FunctionalRmlC/D and qualified Mg do not assert monomeric sufficiency or invented jointcomplex.

### Primary strain and assay boundaries

scope: supported. Targets: GO:0019305.

K12 lineage defects/repairedrfb experiments are distinguished from all-strain phenotype; M.tuberculosis stereo and Salmonella homolog work stay scoped.

### Nearest-source attachment and exact identity

provenance: supported. Targets: GO:0019305.

Every31edge was independently assessed; all21reference digests and currentprotein exactJSON locators verified. Native and RDF family source assertions remain separated.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/pathways/dtdp-l-rhamnose-biosynthesis.yaml; Complete YAML:description,taxon,participants,reactions,all31edges/67evidence and21references. | supports | Read complete frozen target before assessment; all material claims checked against nearest original sources. |
| audit | research/pathway_additions/2026-10-11-next-186/rhamnose-independent-review-audit.json; Reviewer-authored source replay, per-edge assessments, primary PDF reproduction and bounded dedup. | supports | Independent original-source replay and manual31edge scientific assessment support the target with explicit limitations; deterministic checks alone are not the scientific verdict. |
| native | https://pathway.yeastgenome.org/getxml?META:DTDPRHAMSYN-PWY; Four reaction-list members, all native reaction-layout/directions and predecessor orderings; four reaction unification cross-references; exact two complex and monomer frames. | supports | Full route starts glucose1phosphate+dTTP and ends dTDP-beta-L-rhamnose. First native Rhea crossref15228 is bidirectional and bridged explicitly; final native reaction R2L agrees with selected Rhea21798. |
| rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Release142 master15225/17221/16969/21796 to directed15226/17222/16970/21798; original substrates/products/contains/participant/compound triples. | supports | Fresh reviewer parse of full RDF confirms all15chemical sides and all exact RDF locator objects/triples. Four formula/charge balances pass; final direction is right_to_left relative to master. |
| chemistry | http://purl.obolibrary.org/obo/chebi/255/chebi.owl; Current semantic SQL ChEBI identity/label/formula/charge for all13selected metabolites/cofactors. | supports | Exact beta-L-rhamnose product is canonical dTDP-6-deoxy-beta-L-mannose(2-); no alpha sugar or free-rhamnose substitution. Cofactor NAD cycles internally; NADPH is net consumed. |
| proteins | https://rest.uniprot.org/uniprotkb/P37744.json; Full current P37744/P37759/P37745/P37760 entries and inference-source P27830/P26394/P26392; FUNCTION/CATALYTIC/COFACTOR/SUBUNIT/evidenceCodes/taxon/name. | supports | All selected proteins are reviewed K-12 tax83333. RmlA direct experimental annotation is distinct from RmlB RffG inference and RmlC/D Salmonella inference. Exact comment pointers and release2026_03 retained response headers checked. |
| rmla | https://pubmed.ncbi.nlm.nih.gov/11697907/; Full indexed abstract in retained original EuropePMC coreJSON. | supports | Abstract directly supports E.coli reversible kinetics and homotetramer; does not itself specify Mg, correctly sourced separately to current experimental UniProt annotation. |
| stern | https://www.microbiologyresearch.org/content/journal/micro/10.1099/13500872-145-3-663?crawler=true&amp;mimetype=application/pdf; Complete nine-page original PDF; Table1/Fig1 p664; K-12 deletion/extract Results and purified M.tuberculosis assays pp667–668; Discussionp669. | supports | K-12 BW24599 versus rmlC deletion supports free intermediate and pathway function. Purified stereo experiments are M.tuberculosis. Native obligatory C-D channeling prose conflicts with primary data and is explicitly rejected; possible in-vivo interaction remains open. |
| stevenson | https://europepmc.org/articles/PMC205614?pdf=render; Complete13page original PDF, pp4144/4150 abstract and TDP-Rha biosynthetic pathway genes; independent rendered page inspection. | supports | K-12 gene assignments by homology and engineered O16-restored strain are distinct from phenotypes of defective laboratory lineages; record does not imply universal O-antigen expression. |
| rffg | https://bif.wisc.edu/wp-content/uploads/sites/389/2017/11/Hegeman2002.pdf; p2797 explicit RffG name, boundNAD and homodimer; independent original PDF re-extraction. | context_only | The dehydratase mechanistic study concerns RffG paralog; target correctly retains similarity evidence for RmlB rather than claiming this is direct RmlB characterization. |
| marolda | https://europepmc.org/articles/PMC177362?pdf=render; Original1995PDF title/abstract/Methods and relevant Results/Discussion donor,expressionhost and rff compensation. | context_only | VW187 O7 donor enzyme work and K-12 host do not establish direct K-12 RmlB characterization. RffG/H alternatives are outside the selected native core, not asserted absent. |
| rmld | https://doi.org/10.1016/S0969-2126(02)00770-0; Original indexed abstract and independently browsed publisher abstract. | context_only | Salmonella RmlD structural study supports donor/Mg/dimer context, correctly not relabeled a direct E.coli K-12 measurement. |
| names | research/pathway_additions/2026-10-11-next-186/authority-source-inspection.json; Two independent original HTML pages:CPLX0-8034 andDTDPGLUCDEHYDRAT-CPLX exact native object and title. | supports | Fresh reviewer exactID/title/bodyhash check confirms canonical complex names, separately from molecular function evidence. |
| gates | research/pathway_additions/2026-10-11-next-186/integration-receipt.json; All actual final command results, log hashes, failed initial full test and successful targeted rerun | supports | Original logs independently read and hashed; no scientific input changed. Final QC validates 189 records and current pages; test sequence retains its scope and failure. |
| graph | research/pathway_additions/2026-10-11-next-186/generated-graph-kgx-audit.json; GO:0019305 record entry; actual final page and KGX downloads | supports | Generated SVG contains every target edge and evidence anchor; KGX retains full source evidence and reference metadata. Generated artifacts are owned by the YAML and renderer, not hand-edited. |
| imodulon | research/pathway_additions/2026-10-11-next-186/imodulondb-context.json; e_coli/precise1k gene queries and summarized components 43,53,77,90,100,104 | context_only | Exact native gene rows and all 51 source body digests independently checked. Computational expression context only; no absent-pathway or regulatory inference. |

## Limits And Additional Notes

- RmlB exact catalysis/NAD/dimer is inference from K-12RffG, not a purified K-12RmlB assay.
- RmlC exact reaction/dimer annotation derives from Salmonella; K-12 mutant/extract support is distinct from M.tuberculosis purified stereochemical experiments.
- RmlD pathway assignment remains probable and exact catalysis/Mg/dimer derive from Salmonella; functional enables does not claim monomer sufficiency.
- PMID11697907 full publisher article was unavailable. Its complete indexed abstract supports kinetics/tetramer; Mg binding is attributed separately to experimental UniProt annotation.
- No blanket K-12 O-antigen production, physiological flux under all conditions, or absence of possible C-D interaction is claimed.
- Expression-module context cannot establish catalysis or regulation.
- No browser visual interaction inspection is claimed.
- Initial full test command exited 1 with one stale-page failure during another record correction. The sole failed test was rerun successfully after final rendering; the full suite was not rerun in full. Exact-head CI is a separate publication gate.
- Preliminary scratch target descriptor named native MetaCyc scope; it was corrected to maintained GO0019305 and canonical inspect repeated before scientific assessment. Record bytes never changed.
- The maintained independent audit retains its actual earlier pending-gate observation. This final governed review inspects the sealed completed checks, verifies every log digest, rechecks all initial inputs unchanged, and adds actual final shared/page hashes.
- Generated page and KGX are context inputs owned by data/pathways/dtdp-l-rhamnose-biosynthesis.yaml and the unchanged src/pathwaymech renderer/exporter. Baseline byte preservation was independently checked; this is not reassessment of baseline scientific claims.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T040709Z-rhamnose-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of dTDP-rhamnose biosynthesis
started_at: '2026-10-11T03:54:02.421394Z'
finished_at: '2026-10-11T04:07:09.318263Z'
reviewer:
  identity: Codex /root/verify_graph_publication
  kind: agent
  independence: independent
  independence_basis: Did not author the rhamnose record or author dossiers. Authored
    the separate guanine salvage record; its scientific assessment is excluded. Root
    owns shared integration gates and publication.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete four-step native dTDP-rhamnose route, all 31 edges and 67 evidence
  entries are supported with explicit direct-versus-inferred evidence, strain, assay
  and assembly limits. No findings. Final shared QC, identifiers, lint and graph checks
  pass. The initial full test run had one stale-site failure; its final stable-page
  rerun passed. A fresh full-suite pass is not claimed.
source:
  git_revision: 407f1e2d992494f4a61ba336bedfc24155ea5574
  state: working_tree
  inputs:
  - path: conf/identifier_sources.json
    sha256: bc28f89ce9c4eacb5800b3d1dcc97e5f5a0af66df74e5fb3c98823fa42cd1fdd
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: f1497d9708ec44a0f50f4c5aca13fd78e901e972bacc24fe0beb9758e8a08e50
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 1c65fa323339295a2d51185a3f5c1e6159930489d8b8009243142f6620fbe602
    role: context
  - path: data/pathways/dtdp-l-rhamnose-biosynthesis.yaml
    sha256: 75ec1f4ffa088e6647182cde01b7959df161261cb03d48cd471609b2a9b42de9
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
  - path: pages/downloads/edges.tsv
    sha256: 5928c0f3440fdf7f94969f13d060b5698b4a3f30e4ec17923b18db4972f69a24
    role: context
  - path: pages/downloads/manifest.json
    sha256: f157d47d042ca8f6897a6f31ecfc6ee4703bfdfdcc4d313efb2b6afde7626371
    role: context
  - path: pages/downloads/nodes.tsv
    sha256: 8b9021448907737a493b869c7869d2434b6b9fa59579c8a2e4f5b78ed5588c42
    role: context
  - path: pages/records/GO_0019305.html
    sha256: 2cc7e0ea6d1aae4c490791dc12ce176db294ed5b661ccc56e12945dc278f0d8c
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/authority-integration.json
    sha256: c25cb92057407745b0e97972f45027817fb0693d4b91e8ea7bef5e9e1afc2726
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/authority-source-inspection.json
    sha256: 0ddf55d70f0f0727e8e88aeabc77939e7d61259e8f018faf70944041ee76ed5a
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/baseline-preservation.json
    sha256: 7db42e2bd2be9b043726e36b461875cc85ef3d3175eb3ef31be079c7b1c61e60
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/generated-graph-kgx-audit.json
    sha256: 6f312e62b07e243e75fb22244063aa1465fb021293f3deb149fe314e96621129
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/imodulondb-context.json
    sha256: 72381f3f518a5c4fd20ae4a8c1305eb7444d9cb1d07de514c8b4b67dfe1f265c
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/imodulondb-parser-replay.json
    sha256: c80d1a0049bcaabff525a88dd876aa766794aa7f6500c2c74888737d573bca05
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/imodulondb-runner-availability.json
    sha256: 38ebb9d9ebd6e2e2ff38e22449d0390987bb3f8a9d58d117e9c55244c8f8a636
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/imodulondb-source-manifest.json
    sha256: 3c0557921cc80b248734219e18fab90801487cab44ee6107b0df3bd656dbbd94
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/integration-receipt.json
    sha256: f89210d51159c95348997b664e7aedb3766dbebcf7ff10d8e68627c4ca89320a
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/rhamnose-curation.md
    sha256: 6df175e2eadc9beb9411a01f363770cc16155fad5e7a9f2d3d91a6a96f89a171
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/rhamnose-identifiers.json
    sha256: 6d07e79460d3f75026719b45bd9b1b86d9653c93a85bb8fa59135444e9cb7576
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/rhamnose-independent-review-audit.json
    sha256: 384e86648c80ba6cefe668050ee716f2c0965140c2f1601c03ce654a9af2273d
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/rhamnose-replay.py
    sha256: fe6cae3618981c02032c2f64cbaaf2b4913bc26194f92d1074bca4296cf6c94f
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/rhamnose-search-ledger.json
    sha256: 791f697fad924f52f09d5f4be9fd12360e5beff1153271f6e3d001f602284008
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/rhamnose-source-manifest.json
    sha256: edc7650bbdcc531c80eb38562edbe5bd4ec300e86a6144445ccf38db397c903a
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/rhamnose-source-projection.json
    sha256: efc022ca2e83d9ec9f0f2cd7c4aaec0ff5683109d5ba1b7c5a13d54b2416dc36
    role: context
  - path: research/pathway_additions/2026-10-11-next-186/rhamnose-validation.json
    sha256: 7d7ec03de53a3997d4517522c36fb8c6e76183dd7455e0700b2a4c05b5c2408f
    role: context
  - path: src/pathwaymech/kgx.py
    sha256: e1d2f085f8e257170a434400265a400ffac07e4aa23b1b830a8fde990ba6a520
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
scope:
  description: 'Complete one-record review: 19 participants, 4 reactions, 31 edges,
    67 evidence entries and 21 references.'
  selection: Root assigned the frozen exact target; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0019305
  exclusions:
  - target: Guanine salvage, phenylethylamine degradation and baseline pathway science
    reason: Separate author/reviewer assignments; not assessed here.
targets:
- target_id: GO:0019305
  path: data/pathways/dtdp-l-rhamnose-biosynthesis.yaml
  label: dTDP-rhamnose biosynthetic process
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/dtdp-l-rhamnose-biosynthesis.yaml
    role: Maintained scientific record; future fixes belong here, pages are generated
checks:
- check_id: inspect
  name: Canonical capture and final unchanged-input verification
  command: .venv/bin/python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-186-evidence/rhamnose-review/targets.yaml
    --input research/pathway_additions/2026-10-11-next-186/rhamnose-curation.md --input
    research/pathway_additions/2026-10-11-next-186/rhamnose-identifiers.json --input
    research/pathway_additions/2026-10-11-next-186/rhamnose-replay.py --input research/pathway_additions/2026-10-11-next-186/rhamnose-search-ledger.json
    --input research/pathway_additions/2026-10-11-next-186/rhamnose-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-186/rhamnose-source-projection.json
    --input research/pathway_additions/2026-10-11-next-186/rhamnose-validation.json
    --input src/pathwaymech/schema.py --input src/pathwaymech/kgx.py --input docs/CAUSAL_GRAPHS.md
    --input docs/CURATION.md --input docs/HARMONIZATION.md --input conf/identifier_sources.json
    --input data/identifier_authorities/ontology.json --input data/identifier_authorities/sources.json
    --input pages/records/GO_0019305.html --input pages/downloads/edges.tsv --input
    pages/downloads/nodes.tsv --input pages/downloads/manifest.json --input research/pathway_additions/2026-10-11-next-186/rhamnose-independent-review-audit.json
    --input research/pathway_additions/2026-10-11-next-186/authority-integration.json
    --input research/pathway_additions/2026-10-11-next-186/authority-source-inspection.json
    --input research/pathway_additions/2026-10-11-next-186/imodulondb-context.json
    --input research/pathway_additions/2026-10-11-next-186/imodulondb-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-186/imodulondb-runner-availability.json
    --input research/pathway_additions/2026-10-11-next-186/imodulondb-parser-replay.json
    --input research/pathway_additions/2026-10-11-next-186/integration-receipt.json
    --input research/pathway_additions/2026-10-11-next-186/generated-graph-kgx-audit.json
    --input research/pathway_additions/2026-10-11-next-186/baseline-preservation.json
  status: passed
  required: true
  summary: Initial canonical inspection preceded scientific assessment. All eight
    initial target/dossier hashes still match. Final added shared inputs were inspected,
    and every final command-log and supporting-receipt hash was independently rechecked.
  target_ids:
  - GO:0019305
  exit_code: 0
- check_id: independent-source-replay
  name: Independent original-source and chemistry replay
  command: .venv/bin/python /private/tmp/pathwaymech-next-186-evidence/rhamnose-review/independent.py
  status: passed
  required: true
  summary: 'Actual reviewer replay exited 0: full native route and assemblies, all
    source hashes/reference digests, exact Rhea family triples and 15 chemical sides,
    four balances, reviewed protein locators and per-edge evidence. Manual assessment
    accompanies the mechanical replay.'
  target_ids:
  - GO:0019305
  exit_code: 0
  evidence_ids:
  - audit
  - rhea
  - native
  - proteins
- check_id: validate
  name: Shared final validate
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  status: passed
  required: true
  summary: Root actually executed this command; reviewer inspected the original log
    and verified its SHA-256 against the sealed receipt. /private/tmp/pathwaymech-next-186-validate.log
    SHA256 5051636db304c924a912bd2de42fdb946fcc26993ccd601572d5f9fe4bc23635
  target_ids:
  - GO:0019305
  exit_code: 0
  evidence_ids:
  - gates
- check_id: lint
  name: Shared final lint
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  status: passed
  required: true
  summary: Root actually executed this command; reviewer inspected the original log
    and verified its SHA-256 against the sealed receipt. /private/tmp/pathwaymech-next-186-lint.log
    SHA256 df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41
  target_ids:
  - GO:0019305
  exit_code: 0
  evidence_ids:
  - gates
- check_id: identifiers
  name: Shared final identifiers
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    check-identifiers
  status: passed
  required: true
  summary: Root actually executed this command; reviewer inspected the original log
    and verified its SHA-256 against the sealed receipt. /private/tmp/pathwaymech-next-186-identifiers.log
    SHA256 2db33e23e4fe99e63540609fc45ab3dcb523e564f276b19f7dfd44de0bf4f614
  target_ids:
  - GO:0019305
  exit_code: 0
  evidence_ids:
  - gates
- check_id: kgx
  name: Shared final kgx
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-next-186-kgx
  status: passed
  required: true
  summary: Root actually executed this command; reviewer inspected the original log
    and verified its SHA-256 against the sealed receipt. /private/tmp/pathwaymech-next-186-kgx.log
    SHA256 1b214a9aa255c5d1f80b7e1a0b81836af1cb17d28730403d76665f4bbb094400
  target_ids:
  - GO:0019305
  exit_code: 0
  evidence_ids:
  - gates
- check_id: diff
  name: Shared final diff
  command: git diff --check
  status: passed
  required: true
  summary: Root actually executed this command; reviewer inspected the original log
    and verified its SHA-256 against the sealed receipt. /private/tmp/pathwaymech-next-186-diff.log
    SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  target_ids:
  - GO:0019305
  exit_code: 0
  evidence_ids:
  - gates
- check_id: test-initial
  name: Initial full test run (retained failed attempt)
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  status: failed
  required: false
  summary: 'Actual exit 1: 1 failed, 1047 passed, 3 skipped, 3 warnings in 510.51
    s. Sole failure tests/test_render_pages.py::test_the_committed_site_is_current
    reported pages/index.html and phenylethylamine page stale while another record
    evidence correction and rendering overlapped. This superseded attempt is retained,
    not relabeled a full-suite pass.'
  target_ids:
  - GO:0019305
  exit_code: 1
  evidence_ids:
  - gates
- check_id: test-final-page
  name: Final targeted resolution of the sole failed test
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 .venv/bin/pytest
    tests/test_render_pages.py::test_the_committed_site_is_current -q
  status: passed
  required: true
  summary: Actual exit 0, 1 passed in 47.14 s on stable final record/page state. Alongside
    the unchanged-code 1047 prior passes this resolves the observed local failure;
    no final full-suite run occurred. Exact-head CI remains a publication gate.
  target_ids:
  - GO:0019305
  exit_code: 0
  evidence_ids:
  - gates
- check_id: generated-graph
  name: Generated SVG and KGX evidence parity
  command: Root separate just kgx-export and graph-audit.py; reviewer independently
    reads actual HTML and TSV
  status: passed
  required: true
  summary: Final root audit verifies all 31 rhamnose triples and 67 evidence blocks,
    endpoints, anchors, geometry and separate CLI parity. Browser was unavailable;
    no visual interaction claim.
  target_ids:
  - GO:0019305
  exit_code: 0
  evidence_ids:
  - graph
- check_id: imodulon
  name: Structured expression-context replay
  command: Canonical direct-client execution and offline parser replay by separate
    agent; reviewer independently rehashed 51 raw bodies and inspected six returned
    component tables
  status: passed
  required: false
  summary: Console runner unavailable and initial DNS failure are preserved. Authorized
    unchanged-client retry and offline replay exited 0. Exact rfbA/B/C/D gene hits
    are contextual; six broad substring component hits have no selected rhamnose members.
    This is not global absence or biochemical evidence.
  target_ids:
  - GO:0019305
  exit_code: 0
  evidence_ids:
  - imodulon
evidence:
- evidence_id: record
  kind: record_content
  reference: data/pathways/dtdp-l-rhamnose-biosynthesis.yaml
  locator: Complete YAML:description,taxon,participants,reactions,all31edges/67evidence
    and21references.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: supports
  summary: Read complete frozen target before assessment; all material claims checked
    against nearest original sources.
- evidence_id: audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-186/rhamnose-independent-review-audit.json
  locator: Reviewer-authored source replay, per-edge assessments, primary PDF reproduction
    and bounded dedup.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: supports
  summary: Independent original-source replay and manual31edge scientific assessment
    support the target with explicit limitations; deterministic checks alone are not
    the scientific verdict.
- evidence_id: native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:DTDPRHAMSYN-PWY
  locator: Four reaction-list members, all native reaction-layout/directions and predecessor
    orderings; four reaction unification cross-references; exact two complex and monomer
    frames.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: supports
  summary: Full route starts glucose1phosphate+dTTP and ends dTDP-beta-L-rhamnose.
    First native Rhea crossref15228 is bidirectional and bridged explicitly; final
    native reaction R2L agrees with selected Rhea21798.
- evidence_id: rhea
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Release142 master15225/17221/16969/21796 to directed15226/17222/16970/21798;
    original substrates/products/contains/participant/compound triples.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: supports
  summary: Fresh reviewer parse of full RDF confirms all15chemical sides and all exact
    RDF locator objects/triples. Four formula/charge balances pass; final direction
    is right_to_left relative to master.
- evidence_id: chemistry
  kind: authority
  reference: http://purl.obolibrary.org/obo/chebi/255/chebi.owl
  locator: Current semantic SQL ChEBI identity/label/formula/charge for all13selected
    metabolites/cofactors.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: supports
  summary: Exact beta-L-rhamnose product is canonical dTDP-6-deoxy-beta-L-mannose(2-);
    no alpha sugar or free-rhamnose substitution. Cofactor NAD cycles internally;
    NADPH is net consumed.
- evidence_id: proteins
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P37744.json
  locator: Full current P37744/P37759/P37745/P37760 entries and inference-source P27830/P26394/P26392;
    FUNCTION/CATALYTIC/COFACTOR/SUBUNIT/evidenceCodes/taxon/name.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: supports
  summary: All selected proteins are reviewed K-12 tax83333. RmlA direct experimental
    annotation is distinct from RmlB RffG inference and RmlC/D Salmonella inference.
    Exact comment pointers and release2026_03 retained response headers checked.
- evidence_id: rmla
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/11697907/
  locator: Full indexed abstract in retained original EuropePMC coreJSON.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: supports
  summary: Abstract directly supports E.coli reversible kinetics and homotetramer;
    does not itself specify Mg, correctly sourced separately to current experimental
    UniProt annotation.
- evidence_id: stern
  kind: primary_source
  reference: https://www.microbiologyresearch.org/content/journal/micro/10.1099/13500872-145-3-663?crawler=true&mimetype=application/pdf
  locator: Complete nine-page original PDF; Table1/Fig1 p664; K-12 deletion/extract
    Results and purified M.tuberculosis assays pp667–668; Discussionp669.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: supports
  summary: K-12 BW24599 versus rmlC deletion supports free intermediate and pathway
    function. Purified stereo experiments are M.tuberculosis. Native obligatory C-D
    channeling prose conflicts with primary data and is explicitly rejected; possible
    in-vivo interaction remains open.
- evidence_id: stevenson
  kind: primary_source
  reference: https://europepmc.org/articles/PMC205614?pdf=render
  locator: Complete13page original PDF, pp4144/4150 abstract and TDP-Rha biosynthetic
    pathway genes; independent rendered page inspection.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: supports
  summary: K-12 gene assignments by homology and engineered O16-restored strain are
    distinct from phenotypes of defective laboratory lineages; record does not imply
    universal O-antigen expression.
- evidence_id: rffg
  kind: primary_source
  reference: https://bif.wisc.edu/wp-content/uploads/sites/389/2017/11/Hegeman2002.pdf
  locator: p2797 explicit RffG name, boundNAD and homodimer; independent original
    PDF re-extraction.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: context_only
  summary: The dehydratase mechanistic study concerns RffG paralog; target correctly
    retains similarity evidence for RmlB rather than claiming this is direct RmlB
    characterization.
- evidence_id: marolda
  kind: primary_source
  reference: https://europepmc.org/articles/PMC177362?pdf=render
  locator: Original1995PDF title/abstract/Methods and relevant Results/Discussion
    donor,expressionhost and rff compensation.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: context_only
  summary: VW187 O7 donor enzyme work and K-12 host do not establish direct K-12 RmlB
    characterization. RffG/H alternatives are outside the selected native core, not
    asserted absent.
- evidence_id: rmld
  kind: primary_source
  reference: https://doi.org/10.1016/S0969-2126(02)00770-0
  locator: Original indexed abstract and independently browsed publisher abstract.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: context_only
  summary: Salmonella RmlD structural study supports donor/Mg/dimer context, correctly
    not relabeled a direct E.coli K-12 measurement.
- evidence_id: names
  kind: authority
  reference: research/pathway_additions/2026-10-11-next-186/authority-source-inspection.json
  locator: Two independent original HTML pages:CPLX0-8034 andDTDPGLUCDEHYDRAT-CPLX
    exact native object and title.
  accessed_at: '2026-10-11T03:54:02.421394Z'
  support: supports
  summary: Fresh reviewer exactID/title/bodyhash check confirms canonical complex
    names, separately from molecular function evidence.
- evidence_id: gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-186/integration-receipt.json
  locator: All actual final command results, log hashes, failed initial full test
    and successful targeted rerun
  accessed_at: '2026-10-11T04:07:09.318263Z'
  support: supports
  summary: Original logs independently read and hashed; no scientific input changed.
    Final QC validates 189 records and current pages; test sequence retains its scope
    and failure.
  snapshot_sha256: f89210d51159c95348997b664e7aedb3766dbebcf7ff10d8e68627c4ca89320a
- evidence_id: graph
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-186/generated-graph-kgx-audit.json
  locator: GO:0019305 record entry; actual final page and KGX downloads
  accessed_at: '2026-10-11T04:07:09.318263Z'
  support: supports
  summary: Generated SVG contains every target edge and evidence anchor; KGX retains
    full source evidence and reference metadata. Generated artifacts are owned by
    the YAML and renderer, not hand-edited.
  snapshot_sha256: 6f312e62b07e243e75fb22244063aa1465fb021293f3deb149fe314e96621129
- evidence_id: imodulon
  kind: database
  reference: research/pathway_additions/2026-10-11-next-186/imodulondb-context.json
  locator: e_coli/precise1k gene queries and summarized components 43,53,77,90,100,104
  accessed_at: '2026-10-11T04:07:09.318263Z'
  support: context_only
  summary: Exact native gene rows and all 51 source body digests independently checked.
    Computational expression context only; no absent-pathway or regulatory inference.
  snapshot_sha256: 72381f3f518a5c4fd20ae4a8c1305eb7444d9cb1d07de514c8b4b67dfe1f265c
assessments:
- assessment_id: identity
  area: identity
  topic: Complete exact pathway boundary
  outcome: supported
  summary: GO0019305 identity is consistent with the full native4step route; nucleotide
    sugar endpoint and distinct peripheral routes are explicit.
  target_ids:
  - GO:0019305
  evidence_ids:
  - record
  - native
  - chemistry
- assessment_id: chemistry
  area: grounding
  topic: All reaction sides and source-relative directions
  outcome: supported
  summary: All15sides,4balances and3sharedintermediates match actualRDF; RmlD reverse
    master orientation remains explicit.
  target_ids:
  - GO:0019305
  evidence_ids:
  - audit
  - rhea
  - chemistry
- assessment_id: catalysts
  area: evidence
  topic: Exact protein and evidentiary tier
  outcome: supported
  summary: RmlA experimental versus RmlB/RmlC/RmlD inference and probable distinctions
    are preserved per edge.
  target_ids:
  - GO:0019305
  evidence_ids:
  - proteins
  - rmla
  - rffg
  - rmld
- assessment_id: assembly
  area: representation
  topic: Native assemblies and cofactor assertions
  outcome: supported
  summary: Two verified native assemblies, RmlA4 andRmlB2 copies, have exact monomer
    crosswalks. FunctionalRmlC/D and qualified Mg do not assert monomeric sufficiency
    or invented jointcomplex.
  target_ids:
  - GO:0019305
  evidence_ids:
  - native
  - proteins
  - names
  - stern
- assessment_id: strain
  area: scope
  topic: Primary strain and assay boundaries
  outcome: supported
  summary: K12 lineage defects/repairedrfb experiments are distinguished from all-strain
    phenotype; M.tuberculosis stereo and Salmonella homolog work stay scoped.
  target_ids:
  - GO:0019305
  evidence_ids:
  - stern
  - stevenson
  - marolda
  - rmld
- assessment_id: provenance
  area: provenance
  topic: Nearest-source attachment and exact identity
  outcome: supported
  summary: Every31edge was independently assessed; all21reference digests and currentprotein
    exactJSON locators verified. Native and RDF family source assertions remain separated.
  target_ids:
  - GO:0019305
  evidence_ids:
  - audit
  - rhea
  - proteins
  - native
findings: []
actions: []
limitations:
- RmlB exact catalysis/NAD/dimer is inference from K-12RffG, not a purified K-12RmlB
  assay.
- RmlC exact reaction/dimer annotation derives from Salmonella; K-12 mutant/extract
  support is distinct from M.tuberculosis purified stereochemical experiments.
- RmlD pathway assignment remains probable and exact catalysis/Mg/dimer derive from
  Salmonella; functional enables does not claim monomer sufficiency.
- PMID11697907 full publisher article was unavailable. Its complete indexed abstract
  supports kinetics/tetramer; Mg binding is attributed separately to experimental
  UniProt annotation.
- No blanket K-12 O-antigen production, physiological flux under all conditions, or
  absence of possible C-D interaction is claimed.
- Expression-module context cannot establish catalysis or regulation.
- No browser visual interaction inspection is claimed.
- Initial full test command exited 1 with one stale-page failure during another record
  correction. The sole failed test was rerun successfully after final rendering; the
  full suite was not rerun in full. Exact-head CI is a separate publication gate.
notes:
- Preliminary scratch target descriptor named native MetaCyc scope; it was corrected
  to maintained GO0019305 and canonical inspect repeated before scientific assessment.
  Record bytes never changed.
- The maintained independent audit retains its actual earlier pending-gate observation.
  This final governed review inspects the sealed completed checks, verifies every
  log digest, rechecks all initial inputs unchanged, and adds actual final shared/page
  hashes.
- Generated page and KGX are context inputs owned by data/pathways/dtdp-l-rhamnose-biosynthesis.yaml
  and the unchanged src/pathwaymech renderer/exporter. Baseline byte preservation
  was independently checked; this is not reassessment of baseline scientific claims.
```

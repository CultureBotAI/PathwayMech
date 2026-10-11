# Independent scientific review of pseudouridine degradation

- Review: 20261011T020108Z-pseudouridine-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T01:52:11.716180Z
- Finished UTC: 2026-10-11T02:01:08Z
- Reviewer: Codex /root/verify_graph_publication (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete two-step pseudouridine pathway is supported with no confirmed curation findings. Its K-12 protein assignments, physical PsuG trimer, exact charged chemistry and cleavage direction retain explicit strain, equilibrium and evidence-tier limitations. Required final integration gates passed; structural graph checks passed without claiming unavailable browser inspection.

## Scope And Provenance

Full scientific review of the single resolved pseudouridine pathway, all fourteen participants, two reactions, eighteen edges and thirty-six evidence entries.

Selection: Parent explicitly assigned the frozen target from the three-record cohort; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a331b8b9fd7bf4d9f7b6d2f6626b29157b47a69.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-6019 | data/pathways/pseudouridine-degradation.yaml | maintained | pseudouridine degradation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Governed initial and final input inspections | passed | True | MetaCyc:PWY-6019 | Initial inspect preceded scientific assessment; final inspection rechecked all original input hashes unchanged and captured stable shared artifacts. |
| Independent exact-source replay | passed | True | MetaCyc:PWY-6019 | Nine sides, two balanced equations, reaction-family bridges, native trimer/protein/taxon links, all source hashes and primary sequence peptides passed; all eighteen edges assessed. |
| Canonical iModulon context and documented fallback | passed | True | MetaCyc:PWY-6019 | Inspected root acquisition and unchanged canonical parser replay. Exact psuK/b2166 and psuG/b2165 gene hits have no module-name hits; no membership or mechanistic inference. The console failed missing dotenv; unchanged direct client fallback succeeded. |
| just render-pages | passed | True | MetaCyc:PWY-6019 | pass |
| just lint | passed | True | MetaCyc:PWY-6019 | pass |
| just check-identifiers | passed | True | MetaCyc:PWY-6019 | pass |
| git diff --check | passed | True | MetaCyc:PWY-6019 | pass |
| just kgx-export --output-dir /private/tmp/pathwaymech-next-pathways-kgx | passed | True | MetaCyc:PWY-6019 | pass |
| just validate | passed | True | MetaCyc:PWY-6019 | pass |
| just test | passed | True | MetaCyc:PWY-6019 | 1048 passed, 3 skipped, 3 warnings in 234.69 seconds; actual final full-suite terminal exit 0. |
| UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just vendored-check | passed | True | MetaCyc:PWY-6019 | All governed artifacts match pinned canonical revision; terminal success observed. |
| Interactive browser diagram inspection | unavailable | False | MetaCyc:PWY-6019 | Root inventory found no enabled browser surfaces; structural generated SVG/KGX audit was completed instead. No visual interaction success claimed. |

## Scientific And Domain Assessments

### Exact complete pathway boundary

identity: supported. Targets: MetaCyc:PWY-6019.

MetaCyc PWY-6019 resolves both sequential reactions. The misleading discovery title and adjacent nucleoside pathways do not justify merging or broadening this target.

### Charged species, stereochemistry and source-relative direction

grounding: supported. Targets: MetaCyc:PWY-6019.

All nine substrate/product assertions and the exact shared intermediate agree with native Rhea. Both equations balance; the right-to-left metadata denotes the source master orientation, while explicit chemical edges denote cleavage.

### Strain and sequence-specific catalytic assignments

evidence: supported. Targets: MetaCyc:PWY-6019.

The selected K-12 annotations and direct K-12 PsuG construct evidence are distinguished from UTI89 physiology and BL21 kinase structures. PsuK enables its activity without asserting monomer sufficiency; PsuG catalysis is assigned to its native trimer.

### Alternative metals and reversible enzyme chemistry

representation: supported. Targets: MetaCyc:PWY-6019.

PsuG Mn/Fe/Co alternatives have source support and explicit occupancy limits. Reverse-synthesis kinetics and equilibrium do not become claimed forward flux. No unsourced kinase free-metal binding or compartment edges were added.

### Edge-local sources and independent authorities

provenance: supported. Targets: MetaCyc:PWY-6019.

All eighteen edges have nearest-source evidence, correct native/Rhea family bridges and scoped primary locators. All twelve reference body hashes and retained acquisition digests passed independent replay. Every named node has matching authority labels.

### Computational expression evidence

scope: supported. Targets: MetaCyc:PWY-6019.

The exact iModulon gene/locus results and documented canonical-client fallback are valid contextual receipts; no catalysis or absence-of-membership inference was transferred to the graph.

### Frozen full-corpus gates and generated graph

schema: supported. Targets: MetaCyc:PWY-6019.

Final required gates passed on the integrated corpus, with their actual results and log hashes inspected. Generated SVG/KGX structural checks preserve target evidence and context; browser availability is explicitly limited.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/pathways/pseudouridine-degradation.yaml; Complete file: identity, description, 14 participants, 2 reactions, 18 edges and 36 evidence blocks. | supports | Complete target read and reassessed after final input/hash verification. |
| audit | research/pathway_additions/2026-10-11-next-pathways/pseudouridine-independent-review-audit.json; Independent replay checks, actual timestamps, source digests, all-edge assessment and ignored-inclusive search. | supports | Independent scientific source audit completed before shared gates; its pending-gate limitation is superseded by the separately observed final integration receipt. |
| native | https://pathway.yeastgenome.org/getxml?META:PWY-6019; PWY-6019 reaction-list, reaction-layout and reaction-ordering; exact CPLX0-8233 component/coefficient and EG12033-MONOMER UNIPROT/species. | supports | Native route contains kinase and glycosidase only, with explicit order. The native PsuG trimer contains three P33025-linked subunits. Source PathBank map has a misleading Purine Degradation title and is not used as pathway identity. |
| rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Masters 22448/18337; rh:directionalReaction 22449/18339, rh:bidirectionalReaction 18340, selected original sides/contains1/participants/compound triples. | supports | Both exact equations balance atoms and charge. Glycosidase uses the right-to-left cleavage member with D-ribofuranose 5-phosphate of unspecified anomer; broader or differently protonated native species are not declared exact matches. |
| uniprot | https://rest.uniprot.org/uniprotkb/P30235.json ; https://rest.uniprot.org/uniprotkb/P33025.json; Organism/genes/proteinDescription; complete FUNCTION, CATALYTIC ACTIVITY, COFACTOR and SUBUNIT comments; sequence. | supports | Current reviewed K-12 entries support the assigned activities. PsuG preserves experimental and HAMAP evidence tiers and alternative metals. PsuK has no inspected K-12 oligomeric-state annotation. |
| primary2008 | https://pubmed.ncbi.nlm.nih.gov/18591240/; Retained Europe PMC core response abstractText; full PDF was inaccessible. | supports | Indexed primary abstract supports sequential kinase/glycosidase chemistry and UTI89 knockout phenotype. It is not evidence of measured K-12 whole-cell flux. |
| primary2012 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3526674/; Complete Methods/Results/Discussion; BioC offsets 6100, 6949, 17266, 18370, 23628, 24413, 31636 and 34501. | supports | K-12 DNA origin, trimeric structure, metal coordination and reverse-synthesis assay scope support the bounded record. Both measured peptides independently match the selected P33025 sequence exactly. |
| primary2022 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9247573/; Complete Methods/Results/Discussion; construct A0A140N873, SEC dimer, activity assay, uncertain Mg sites. | supports | BL21-derived kinase is dimeric in this study. Record correctly treats it as strain-specific structural context rather than direct evidence for K-12 assembly. Assay ingredients alone are not presented as separate K-12 metal-binding edges. |
| authorities | research/pathway_additions/2026-10-11-next-pathways/authority-protein-crosscheck.json; P30235/P33025 entries; exact native META 22.5 HTML titles; 18 named nodes in ontology/source snapshots. | supports | Independent raw HTML hashes/titles and source/ontology labels match the record. Fresh protein names agree with earlier selected authority names without changing earlier provenance. |
| imodulon | research/pathway_additions/2026-10-11-next-pathways/imodulondb-context.json; e_coli/precise_mg1655 psuK/b2166 and psuG/b2165 queries; parser and runner-availability receipts. | context_only | Expression-database context was inspected; no module-name hit does not establish biological absence and does not support catalysis. |
| gates | research/pathway_additions/2026-10-11-next-pathways/integration-validation.json; All terminal check results and exact external log paths/digests. | supports | Final full-corpus commands were executed by the integrating root; this reviewer independently rehashed their logs and inspected results. |
| graph | research/pathway_additions/2026-10-11-next-pathways/generated-graph-kgx-audit.json; Pseudouridine row and retained evidence/description/category/direction checks; browser availability receipt. | supports | Generated graph and KGX structural audit preserves the record semantics. No browser visual inspection is claimed. |
| dedup | research/pathway_additions/2026-10-11-next-pathways/pseudouridine-independent-review-audit.json; dedup command/matched files and author search-ledger dispositions. | supports | Fresh hidden/ignored-inclusive current-worktree search finds the new target as the only matching maintained pathway. Prior inventory mentions and adjacent purine/pyrimidine routes do not duplicate its exact two reactions. |

## Limits And Additional Notes

- 2008 primary article was inspected as indexed abstract only; author full-PDF attempt failed. K-12 kinase assignment rests on current reviewed annotation.
- K-12 kinase oligomeric state remains unestablished in inspected sources; BL21 dimer and metal conditions are not transferred.
- PsuG kinetics measured reverse synthesis, not forward whole-cell flux; pathway degradation direction is native physiological selection.
- Alternative PsuG metals do not establish simultaneous occupancy or dominant in vivo metal.
- Canonical iModulon console command failed missing dotenv; root used unchanged direct client and retained source bodies. This reviewer inspected receipts/results, did not independently rerun network acquisition.
- The scientific scope is this one pathway only. Homogentisate was authored by this reviewer and is independently assessed by another agent; thiamine and deferred nicotine science are excluded here.
- Full-corpus gate and graph-audit execution was delegated to the integrating root; the reviewer inspected actual receipts/logs instead of duplicating expensive runs.
- No browser surface was available; generated diagram assessment is structural, not visual or interactive.
- Initial governed inspection captured SHA256 a11010f36c6af2d7f3304357cb920ba75fda74b067f01e0a64e9855123452159; scientific target and all initial recorded inputs were unchanged at final inspection.
- The audit JSON was created before shared gates completed and deliberately records that temporal limitation; this later immutable review includes the actual final results.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T020108Z-pseudouridine-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of pseudouridine degradation
started_at: '2026-10-11T01:52:11.716180Z'
finished_at: '2026-10-11T02:01:08Z'
reviewer:
  identity: Codex /root/verify_graph_publication
  kind: agent
  independence: independent
  independence_basis: Did not author or edit pseudouridine record/dossiers. Independently
    read native and primary bodies and replayed original source assertions. Authored
    the separate homogentisate record; that science is excluded.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete two-step pseudouridine pathway is supported with no confirmed
  curation findings. Its K-12 protein assignments, physical PsuG trimer, exact charged
  chemistry and cleavage direction retain explicit strain, equilibrium and evidence-tier
  limitations. Required final integration gates passed; structural graph checks passed
  without claiming unavailable browser inspection.
source:
  git_revision: 6a331b8b9fd7bf4d9f7b6d2f6626b29157b47a69
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
  - path: conf/identifier_policy.yaml
    sha256: 3e19ecbbe980e44198405ae0cf37b5fd17ae4c88c05dbf36fab482b2ddd38bd1
    role: context
  - path: conf/identifier_sources.json
    sha256: f10c5134fb3c06b60f0aac9d68f09219fd2d8cb385bb5030c32629d61c66b9a5
    role: context
  - path: conf/sources.yaml
    sha256: 49507bca325f9529bd25b3507b062a1241c403916293dbab96d3cb598d6a7a95
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 53301d6edd435f9fa3191ba317efbfabeb45a0843c2d88ade0e80c8244714049
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 7fe18e8cb41db75a16c9d4afdb45f4db1a86a1fef47cf609c25263d3b567e743
    role: context
  - path: data/pathways/pseudouridine-degradation.yaml
    sha256: a11010f36c6af2d7f3304357cb920ba75fda74b067f01e0a64e9855123452159
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
  - path: docs/record-review-profile.md
    sha256: a3d4b48de5f227515f9b5de12dd172cd1eb626068235b2b2e58bc4f6a5ee567d
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 6d3df7c8fb17835c316a5f37a59c0ff7e61541bbb0781d4dd62ee6ec5fce7df2
    role: context
  - path: pages/downloads/edges.tsv
    sha256: f6fd02a0660b98f8c42490ebe948e66bdd5fdf652a22c955715e8d29acee3ba8
    role: context
  - path: pages/downloads/nodes.tsv
    sha256: 8c6ee912a2e4b51b303899d2f2e297051ae365729e28bf7b1b97c3ced1c864fb
    role: context
  - path: pages/records/MetaCyc_PWY-6019.html
    sha256: cd2a338690657c316a16c30683219ab67c8f9904e107191a9e44e6b7d7a6ee7b
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/authority-integration.json
    sha256: 6e0bebf1ed4802f103db47a98e4a0be4eaf9a3a9e4c3c4c13470544087bf0d37
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/authority-protein-crosscheck.json
    sha256: 5c1519318f2e620043479613c0b7b789d1475a906ae071b40acefc5b49ceee0c
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/authority-source-inspection.json
    sha256: 7b7054c90254ec8bbed9c75ce351dc22b6e784a30175a9dbb281fde48db1f1c5
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/baseline-preservation.json
    sha256: 9ed2262fda352de3246e42357f38109fee36b41753750bc84219aa1bb5ee009f
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/browser-availability.json
    sha256: 190ba0aad5bc1c4a7f3271c08cae5bf74d66b0b9f1ead5258ab514d3be2c9e11
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/generated-graph-kgx-audit.json
    sha256: 87fe919bba958ee2804f782d7efa0a3a8ec895d324aa2e7e83e9bf13312c4730
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/imodulondb-context.json
    sha256: 9476cb4d416878ab16deeb8a1d57a89b9fd448355a4b38b8994661c4b0c5d1cf
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/imodulondb-parser-replay.json
    sha256: 986d5e3ebeb6036d2acd2705da067e116049013fe6701a09c99eacd2676676d7
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/imodulondb-runner-availability.json
    sha256: 9cf704bc4d5e2adfe144e745cce0c8fb0525ce3254e0be9d22078dcf0f608823
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/imodulondb-source-manifest.json
    sha256: a308db444c631f2bb75b79c3bdab1894aab67dc45b6c4784077deff0981494da
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/integration-validation.json
    sha256: c54763a27294bf2d6ea829ac31aba1b87f59884d74a27d03df4aaa356c2149d5
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/native-authority-fetch.json
    sha256: bf5546e5aaaecacd206fafc3b794ee2b1e7f2bc09e4bf239e0bc07721beeaec3
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/pseudouridine-curation.md
    sha256: f03769f2ffa42eea981225bf0f7cf6ebb1a9bdc6d88512f6a67ccd21935bcf25
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/pseudouridine-identifiers.json
    sha256: 0c1769ba8d3275767a20498e70f432e8490ca37f1a4c714aceb3288b4e66d3bc
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/pseudouridine-independent-review-audit.json
    sha256: 522acfe573524e34fc2ffd5720f41a42c6a8fe7ae863f5bd5cc3d5113322a34f
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/pseudouridine-replay.py
    sha256: 07874f5c064b129a55cb4afe37129365d0106b79d10ac31482316bd9df890507
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/pseudouridine-search-ledger.json
    sha256: 36ca11cf460324d4dada847b396e3f9e8ca8ff8cadcaceca1852fbe7fde44564
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/pseudouridine-source-manifest.json
    sha256: 35bb4b4ccd1b6769045579866d40154da020ed24bc7a588a133ae3b3f3a009c7
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/pseudouridine-source-projection.json
    sha256: a5b239589b9a3fe98ac30aa4710acbfd7d82d91f0ee1e1b64f4bb8fc5f701170
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/pseudouridine-validation.json
    sha256: 65e215b12336c1b341cd385c1fbe33e8cf3c68c6995030e42cc40d10be9cead6
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/vendored-check.json
    sha256: 2c821fb0c3c1c350930095cc46f95231270a69efb9f38a6fdc7770f3dc7b419c
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
scope:
  description: Full scientific review of the single resolved pseudouridine pathway,
    all fourteen participants, two reactions, eighteen edges and thirty-six evidence
    entries.
  selection: Parent explicitly assigned the frozen target from the three-record cohort;
    no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-6019
  exclusions:
  - target: Other pathway records and deferred nicotine candidate
    reason: Separate authors/reviewers own their scientific assessments; corpus gates
      are integration context only.
targets:
- target_id: MetaCyc:PWY-6019
  path: data/pathways/pseudouridine-degradation.yaml
  label: pseudouridine degradation
  kind: maintained
  record_class: Pathway
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/pseudouridine-degradation.yaml
    role: maintained scientific record
checks:
- check_id: governed-inspect
  name: Governed initial and final input inspections
  status: passed
  required: true
  summary: Initial inspect preceded scientific assessment; final inspection rechecked
    all original input hashes unchanged and captured stable shared artifacts.
  target_ids:
  - MetaCyc:PWY-6019
  command: Initial and final .venv/bin/python scripts/record_review.py inspect --targets
    /private/tmp/pathwaymech-next-pathways-review-pseudouridine/targets.yaml with
    the input list retained in the source attestation.
  exit_code: 0
  evidence_ids:
  - audit
- check_id: independent-science-replay
  name: Independent exact-source replay
  status: passed
  required: true
  summary: Nine sides, two balanced equations, reaction-family bridges, native trimer/protein/taxon
    links, all source hashes and primary sequence peptides passed; all eighteen edges
    assessed.
  target_ids:
  - MetaCyc:PWY-6019
  command: .venv/bin/python /private/tmp/pathwaymech-next-pathways-review-pseudouridine/independent-audit.py
  exit_code: 0
  evidence_ids:
  - audit
  - native
  - rhea
  - uniprot
  - primary2012
- check_id: imodulon-context
  name: Canonical iModulon context and documented fallback
  status: passed
  required: true
  summary: Inspected root acquisition and unchanged canonical parser replay. Exact
    psuK/b2166 and psuG/b2165 gene hits have no module-name hits; no membership or
    mechanistic inference. The console failed missing dotenv; unchanged direct client
    fallback succeeded.
  target_ids:
  - MetaCyc:PWY-6019
  evidence_ids:
  - imodulon
  scope_note: Delegated acquisition/parser execution, independently inspected results;
    reviewer did not independently requery the network.
- check_id: integration-1
  name: just render-pages
  status: passed
  required: true
  summary: pass
  target_ids:
  - MetaCyc:PWY-6019
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    render-pages
  exit_code: 0
  evidence_ids:
  - gates
  scope_note: Actual integrating-root execution on the frozen full corpus; log/result
    inspected by this reviewer. This is not a one-record gate or an independently
    rerun full suite.
- check_id: integration-2
  name: just lint
  status: passed
  required: true
  summary: pass
  target_ids:
  - MetaCyc:PWY-6019
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    lint
  exit_code: 0
  evidence_ids:
  - gates
  scope_note: Actual integrating-root execution on the frozen full corpus; log/result
    inspected by this reviewer. This is not a one-record gate or an independently
    rerun full suite.
- check_id: integration-3
  name: just check-identifiers
  status: passed
  required: true
  summary: pass
  target_ids:
  - MetaCyc:PWY-6019
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    check-identifiers
  exit_code: 0
  evidence_ids:
  - gates
  scope_note: Actual integrating-root execution on the frozen full corpus; log/result
    inspected by this reviewer. This is not a one-record gate or an independently
    rerun full suite.
- check_id: integration-4
  name: git diff --check
  status: passed
  required: true
  summary: pass
  target_ids:
  - MetaCyc:PWY-6019
  command: git diff --check
  exit_code: 0
  evidence_ids:
  - gates
  scope_note: Actual integrating-root execution on the frozen full corpus; log/result
    inspected by this reviewer. This is not a one-record gate or an independently
    rerun full suite.
- check_id: integration-5
  name: just kgx-export --output-dir /private/tmp/pathwaymech-next-pathways-kgx
  status: passed
  required: true
  summary: pass
  target_ids:
  - MetaCyc:PWY-6019
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    kgx-export --output-dir /private/tmp/pathwaymech-next-pathways-kgx
  exit_code: 0
  evidence_ids:
  - gates
  scope_note: Actual integrating-root execution on the frozen full corpus; log/result
    inspected by this reviewer. This is not a one-record gate or an independently
    rerun full suite.
- check_id: integration-6
  name: just validate
  status: passed
  required: true
  summary: pass
  target_ids:
  - MetaCyc:PWY-6019
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    validate
  exit_code: 0
  evidence_ids:
  - gates
  scope_note: Actual integrating-root execution on the frozen full corpus; log/result
    inspected by this reviewer. This is not a one-record gate or an independently
    rerun full suite.
- check_id: integration-7
  name: just test
  status: passed
  required: true
  summary: 1048 passed, 3 skipped, 3 warnings in 234.69 seconds; actual final full-suite
    terminal exit 0.
  target_ids:
  - MetaCyc:PWY-6019
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    test
  exit_code: 0
  evidence_ids:
  - gates
  scope_note: Actual integrating-root execution on the frozen full corpus; log/result
    inspected by this reviewer. This is not a one-record gate or an independently
    rerun full suite.
- check_id: integration-8
  name: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  status: passed
  required: true
  summary: All governed artifacts match pinned canonical revision; terminal success
    observed.
  target_ids:
  - MetaCyc:PWY-6019
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  exit_code: 0
  evidence_ids:
  - gates
  scope_note: Actual integrating-root execution on the frozen full corpus; log/result
    inspected by this reviewer. This is not a one-record gate or an independently
    rerun full suite.
- check_id: browser-visual
  name: Interactive browser diagram inspection
  status: unavailable
  required: false
  summary: Root inventory found no enabled browser surfaces; structural generated
    SVG/KGX audit was completed instead. No visual interaction success claimed.
  target_ids:
  - MetaCyc:PWY-6019
  evidence_ids:
  - graph
evidence:
- evidence_id: record
  kind: record_content
  reference: data/pathways/pseudouridine-degradation.yaml
  locator: 'Complete file: identity, description, 14 participants, 2 reactions, 18
    edges and 36 evidence blocks.'
  accessed_at: '2026-10-11T02:01:08Z'
  support: supports
  summary: Complete target read and reassessed after final input/hash verification.
  snapshot_sha256: a11010f36c6af2d7f3304357cb920ba75fda74b067f01e0a64e9855123452159
- evidence_id: audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-pathways/pseudouridine-independent-review-audit.json
  locator: Independent replay checks, actual timestamps, source digests, all-edge
    assessment and ignored-inclusive search.
  accessed_at: '2026-10-11T02:01:08Z'
  support: supports
  summary: Independent scientific source audit completed before shared gates; its
    pending-gate limitation is superseded by the separately observed final integration
    receipt.
  snapshot_sha256: 522acfe573524e34fc2ffd5720f41a42c6a8fe7ae863f5bd5cc3d5113322a34f
- evidence_id: native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY-6019
  locator: PWY-6019 reaction-list, reaction-layout and reaction-ordering; exact CPLX0-8233
    component/coefficient and EG12033-MONOMER UNIPROT/species.
  accessed_at: '2026-10-11T01:54:09.230770Z'
  support: supports
  summary: Native route contains kinase and glycosidase only, with explicit order.
    The native PsuG trimer contains three P33025-linked subunits. Source PathBank
    map has a misleading Purine Degradation title and is not used as pathway identity.
- evidence_id: rhea
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Masters 22448/18337; rh:directionalReaction 22449/18339, rh:bidirectionalReaction
    18340, selected original sides/contains1/participants/compound triples.
  accessed_at: '2026-10-11T01:54:09.230770Z'
  support: supports
  summary: Both exact equations balance atoms and charge. Glycosidase uses the right-to-left
    cleavage member with D-ribofuranose 5-phosphate of unspecified anomer; broader
    or differently protonated native species are not declared exact matches.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: uniprot
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P30235.json ; https://rest.uniprot.org/uniprotkb/P33025.json
  locator: Organism/genes/proteinDescription; complete FUNCTION, CATALYTIC ACTIVITY,
    COFACTOR and SUBUNIT comments; sequence.
  accessed_at: '2026-10-11T01:54:09.230770Z'
  support: supports
  summary: Current reviewed K-12 entries support the assigned activities. PsuG preserves
    experimental and HAMAP evidence tiers and alternative metals. PsuK has no inspected
    K-12 oligomeric-state annotation.
- evidence_id: primary2008
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/18591240/
  locator: Retained Europe PMC core response abstractText; full PDF was inaccessible.
  accessed_at: '2026-10-11T01:54:09.230770Z'
  support: supports
  summary: Indexed primary abstract supports sequential kinase/glycosidase chemistry
    and UTI89 knockout phenotype. It is not evidence of measured K-12 whole-cell flux.
  snapshot_sha256: 6c00509a7d51990543f07b857a3d9b68d3f83f7dd021434ab741c69d9ac89715
- evidence_id: primary2012
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3526674/
  locator: Complete Methods/Results/Discussion; BioC offsets 6100, 6949, 17266, 18370,
    23628, 24413, 31636 and 34501.
  accessed_at: '2026-10-11T01:54:09.230770Z'
  support: supports
  summary: K-12 DNA origin, trimeric structure, metal coordination and reverse-synthesis
    assay scope support the bounded record. Both measured peptides independently match
    the selected P33025 sequence exactly.
  snapshot_sha256: aefa88d2a4a9e3912cdf48af62c6e521462388134b75a730c6d93be1008dadfe
- evidence_id: primary2022
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9247573/
  locator: Complete Methods/Results/Discussion; construct A0A140N873, SEC dimer, activity
    assay, uncertain Mg sites.
  accessed_at: '2026-10-11T01:54:09.230770Z'
  support: supports
  summary: BL21-derived kinase is dimeric in this study. Record correctly treats it
    as strain-specific structural context rather than direct evidence for K-12 assembly.
    Assay ingredients alone are not presented as separate K-12 metal-binding edges.
  snapshot_sha256: 4e3aa540e9310c71c6dbfa13261254cd1fa9c1708ac2e226d7eba87fc9e75ba1
- evidence_id: authorities
  kind: authority
  reference: research/pathway_additions/2026-10-11-next-pathways/authority-protein-crosscheck.json
  locator: P30235/P33025 entries; exact native META 22.5 HTML titles; 18 named nodes
    in ontology/source snapshots.
  accessed_at: '2026-10-11T02:01:08Z'
  support: supports
  summary: Independent raw HTML hashes/titles and source/ontology labels match the
    record. Fresh protein names agree with earlier selected authority names without
    changing earlier provenance.
  snapshot_sha256: 5c1519318f2e620043479613c0b7b789d1475a906ae071b40acefc5b49ceee0c
- evidence_id: imodulon
  kind: database
  reference: research/pathway_additions/2026-10-11-next-pathways/imodulondb-context.json
  locator: e_coli/precise_mg1655 psuK/b2166 and psuG/b2165 queries; parser and runner-availability
    receipts.
  accessed_at: '2026-10-11T02:01:08Z'
  support: context_only
  summary: Expression-database context was inspected; no module-name hit does not
    establish biological absence and does not support catalysis.
  snapshot_sha256: 9476cb4d416878ab16deeb8a1d57a89b9fd448355a4b38b8994661c4b0c5d1cf
- evidence_id: gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-pathways/integration-validation.json
  locator: All terminal check results and exact external log paths/digests.
  accessed_at: '2026-10-11T02:01:08Z'
  support: supports
  summary: Final full-corpus commands were executed by the integrating root; this
    reviewer independently rehashed their logs and inspected results.
  snapshot_sha256: c54763a27294bf2d6ea829ac31aba1b87f59884d74a27d03df4aaa356c2149d5
- evidence_id: graph
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-pathways/generated-graph-kgx-audit.json
  locator: Pseudouridine row and retained evidence/description/category/direction
    checks; browser availability receipt.
  accessed_at: '2026-10-11T02:01:08Z'
  support: supports
  summary: Generated graph and KGX structural audit preserves the record semantics.
    No browser visual inspection is claimed.
  snapshot_sha256: 87fe919bba958ee2804f782d7efa0a3a8ec895d324aa2e7e83e9bf13312c4730
- evidence_id: dedup
  kind: search
  reference: research/pathway_additions/2026-10-11-next-pathways/pseudouridine-independent-review-audit.json
  locator: dedup command/matched files and author search-ledger dispositions.
  accessed_at: '2026-10-11T01:54:09.230770Z'
  support: supports
  summary: Fresh hidden/ignored-inclusive current-worktree search finds the new target
    as the only matching maintained pathway. Prior inventory mentions and adjacent
    purine/pyrimidine routes do not duplicate its exact two reactions.
  search_scope: rg --no-ignore --hidden --files-with-matches over accessible current
    worktree, excluding only .git and .venv; exact pathway, catalyst and native reaction
    identifiers plus pseudouridine degradation/catabolism. Original Documents checkout
    remains inaccessible; no global absence claim.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact complete pathway boundary
  outcome: supported
  summary: MetaCyc PWY-6019 resolves both sequential reactions. The misleading discovery
    title and adjacent nucleoside pathways do not justify merging or broadening this
    target.
  target_ids:
  - MetaCyc:PWY-6019
  evidence_ids:
  - native
  - dedup
  - record
- assessment_id: chemistry
  area: grounding
  topic: Charged species, stereochemistry and source-relative direction
  outcome: supported
  summary: All nine substrate/product assertions and the exact shared intermediate
    agree with native Rhea. Both equations balance; the right-to-left metadata denotes
    the source master orientation, while explicit chemical edges denote cleavage.
  target_ids:
  - MetaCyc:PWY-6019
  evidence_ids:
  - rhea
  - audit
- assessment_id: proteins
  area: evidence
  topic: Strain and sequence-specific catalytic assignments
  outcome: supported
  summary: The selected K-12 annotations and direct K-12 PsuG construct evidence are
    distinguished from UTI89 physiology and BL21 kinase structures. PsuK enables its
    activity without asserting monomer sufficiency; PsuG catalysis is assigned to
    its native trimer.
  target_ids:
  - MetaCyc:PWY-6019
  evidence_ids:
  - uniprot
  - primary2008
  - primary2012
  - primary2022
  - native
  dimensions:
  - name: taxon-evidence
    value: K-12 protein annotation and direct PsuG; UTI89 physiology and BL21 kinase
      structure are bounded context
    definition: Experimental source organism is not inferred from expression host
      or projected across strains.
    evidence_ids:
    - primary2008
    - primary2012
    - primary2022
    - uniprot
- assessment_id: metals
  area: representation
  topic: Alternative metals and reversible enzyme chemistry
  outcome: supported
  summary: PsuG Mn/Fe/Co alternatives have source support and explicit occupancy limits.
    Reverse-synthesis kinetics and equilibrium do not become claimed forward flux.
    No unsourced kinase free-metal binding or compartment edges were added.
  target_ids:
  - MetaCyc:PWY-6019
  evidence_ids:
  - uniprot
  - primary2012
  - primary2022
  - record
- assessment_id: provenance
  area: provenance
  topic: Edge-local sources and independent authorities
  outcome: supported
  summary: All eighteen edges have nearest-source evidence, correct native/Rhea family
    bridges and scoped primary locators. All twelve reference body hashes and retained
    acquisition digests passed independent replay. Every named node has matching authority
    labels.
  target_ids:
  - MetaCyc:PWY-6019
  evidence_ids:
  - audit
  - authorities
  - native
  - rhea
- assessment_id: context
  area: scope
  topic: Computational expression evidence
  outcome: supported
  summary: The exact iModulon gene/locus results and documented canonical-client fallback
    are valid contextual receipts; no catalysis or absence-of-membership inference
    was transferred to the graph.
  target_ids:
  - MetaCyc:PWY-6019
  evidence_ids:
  - imodulon
- assessment_id: gates
  area: schema
  topic: Frozen full-corpus gates and generated graph
  outcome: supported
  summary: Final required gates passed on the integrated corpus, with their actual
    results and log hashes inspected. Generated SVG/KGX structural checks preserve
    target evidence and context; browser availability is explicitly limited.
  target_ids:
  - MetaCyc:PWY-6019
  evidence_ids:
  - gates
  - graph
  - record
findings: []
actions: []
limitations:
- 2008 primary article was inspected as indexed abstract only; author full-PDF attempt
  failed. K-12 kinase assignment rests on current reviewed annotation.
- K-12 kinase oligomeric state remains unestablished in inspected sources; BL21 dimer
  and metal conditions are not transferred.
- PsuG kinetics measured reverse synthesis, not forward whole-cell flux; pathway degradation
  direction is native physiological selection.
- Alternative PsuG metals do not establish simultaneous occupancy or dominant in vivo
  metal.
- Canonical iModulon console command failed missing dotenv; root used unchanged direct
  client and retained source bodies. This reviewer inspected receipts/results, did
  not independently rerun network acquisition.
- The scientific scope is this one pathway only. Homogentisate was authored by this
  reviewer and is independently assessed by another agent; thiamine and deferred nicotine
  science are excluded here.
- Full-corpus gate and graph-audit execution was delegated to the integrating root;
  the reviewer inspected actual receipts/logs instead of duplicating expensive runs.
- No browser surface was available; generated diagram assessment is structural, not
  visual or interactive.
notes:
- Initial governed inspection captured SHA256 a11010f36c6af2d7f3304357cb920ba75fda74b067f01e0a64e9855123452159;
  scientific target and all initial recorded inputs were unchanged at final inspection.
- The audit JSON was created before shared gates completed and deliberately records
  that temporal limitation; this later immutable review includes the actual final
  results.
links:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3526674/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9247573/
- https://pathway.yeastgenome.org/getxml?META:PWY-6019
tags:
- independent-review
- pseudouridine
- pathway
```

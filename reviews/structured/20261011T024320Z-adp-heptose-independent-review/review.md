# Independent scientific review of ADP-heptose biosynthesis

- Review: 20261011T024320Z-adp-heptose-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T02:28:16.659091Z
- Finished UTC: 2026-10-11T02:43:20Z
- Reviewer: Codex /root (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete five-step ADP-L-glycero-beta-D-manno-heptose pathway is supported with no confirmed finding. Exact chemistry, K-12 proteins and physical assemblies preserve anomer, cofactor, strain and evidence-tier limitations. Final corpus and generated structural checks pass.

## Scope And Provenance

Entire single resolved pathway: 26 participants, 5 reactions, 43 edges and 86 evidence blocks.

Selection: Root independently reviews the record authored by another agent; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e3bceba7613eb0525af3ff76ef32520201ae9f33.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY0-1241 | data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml | maintained | ADP-L-glycero-beta-D-manno-heptose biosynthesis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Governed input inspection | passed | True | MetaCyc:PWY0-1241 | Initial inspection preceded the scientific assessment. Final inspection rechecked every original hash unchanged and captured final shared inputs. |
| Independent original-source replay | passed | True | MetaCyc:PWY0-1241 | All 19 chemical sides, 5 atom/charge balances, 5 native reaction mappings, 3 physical assemblies and 30 reference hashes passed independently of the author replay. |
| just render-pages | passed | True | MetaCyc:PWY0-1241 | Actual terminal exit 0; exact log digest verified. |
| just lint | passed | True | MetaCyc:PWY0-1241 | Actual terminal exit 0; exact log digest verified. |
| git diff --check | passed | True | MetaCyc:PWY0-1241 | Actual terminal exit 0; exact log digest verified. |
| just check-identifiers | passed | True | MetaCyc:PWY0-1241 | Actual terminal exit 0; exact log digest verified. |
| just kgx-export --output-dir /private/tmp/pathwaymech-nicotine-next-kgx | passed | True | MetaCyc:PWY0-1241 | Actual terminal exit 0; exact log digest verified. |
| just validate | passed | True | MetaCyc:PWY0-1241 | Actual terminal exit 0; exact log digest verified. |
| just test | passed | True | MetaCyc:PWY0-1241 | {'passed': 1048, 'skipped': 3, 'warnings': 3, 'seconds': 594.56} |
| UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just vendored-check | passed | True | MetaCyc:PWY0-1241 | Actual terminal exit 0; exact log digest verified. |
| Interactive browser inspection | unavailable | False | MetaCyc:PWY0-1241 | Actual enabled-surface inventory was empty; no visual or interaction claim. |

## Scientific And Domain Assessments

### Complete native boundary

identity: supported. Targets: MetaCyc:PWY0-1241.

Full five-step native pathway is maintained, including the upstream isomerase omitted by narrower GO:0097171. Discovery names alone are not grounds for equivalence.

### Exact charged species and formal anomer equation

grounding: supported. Targets: MetaCyc:PWY0-1241.

All five equations and nineteen chemical sides match original Rhea and balance. The two-substrate formal GmhA equation records both anomers without asserting a 1:1 physiological pool.

### K-12 enzymes, assemblies and source organisms

evidence: supported. Targets: MetaCyc:PWY0-1241.

All four proteins and three exact assemblies are supported. Native and UniProt bridges match. Heterologous GmhA in the 2002 assay remains separate from K-12 protein annotation.

### Catalytic alternatives and retained cofactors

representation: supported. Targets: MetaCyc:PWY0-1241.

GmhA Zn is inferred, GmhB catalytic Mg/Mn/Co differs from loop Zn, and HldD bound NADP is retained rather than added to net substrate/product chemistry.

### Edge-local evidence and authority integrity

provenance: supported. Targets: MetaCyc:PWY0-1241.

All 43 mechanistic assertions and 86 evidence entries were assessed against their nearest source, with full-text vs abstract and direct vs inferred tiers retained. All 30 retained reference-body digests match.

### Expression evidence stays contextual

scope: supported. Targets: MetaCyc:PWY0-1241.

The actual canonical-client fallback and replay are recorded; expression search does not establish pathway identity, catalysis or biological absence.

### Corpus validation and generated graph

schema: supported. Targets: MetaCyc:PWY0-1241.

Required full-corpus checks pass after final rendering. Generated SVG and KGX preserve local evidence and graph semantics. Scientific assessment is independent of deterministic checks.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml; Entire 890-line target; all 26 participants, 5 reactions, 43 edges, 86 evidence entries. | supports | Independent full target assessment after governed initial inspect; scientific target and author evidence inputs stayed unchanged. |
| audit | research/pathway_additions/2026-10-11-nicotine-next/adhp-independent-audit.json; Independent original RDF/native XML replay, all 30 reference hashes and primary passage locators. | supports | Root did not author ADP; independently wrote direct source checks and inspected the source text. Nineteen exact reaction sides, five atom/charge balances and three exact assemblies pass. |
| native | https://pathway.yeastgenome.org/getxml?META:PWY0-1241; Complete reaction-list/reaction-ordering and each native reaction Rhea dblink; CPLX0-7660/3661/3681 and exact UniProt monomer bridges. | supports | Full native five-step route begins at sedoheptulose 7-phosphate. GO:0097171 begins one reaction later. Native complexes support GmhA tetramer, HldE dimer and HldD pentamer. |
| rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Masters 27490,27474,28519,27466,17578; native sides, contains coefficients and ChEBI identities. | supports | All equations balance. GmhA formal equation yields both anomers from two substrates; it does not measure their cellular ratio. Charge, stereochemistry and hydrolysis products are exact. |
| uniprot | https://rest.uniprot.org/uniprotkb/P63224.json ; https://rest.uniprot.org/uniprotkb/P76658.json ; https://rest.uniprot.org/uniprotkb/P63228.json ; https://rest.uniprot.org/uniprotkb/P67910.json; Complete organism/gene, function, catalytic activity, cofactor and subunit annotations; each raw body hash in audit. | supports | Correct K-12 catalysts and molecular assemblies. GmhA zinc is inferred by similarity; GmhB catalytic metal alternatives and loop zinc differ in role. HldD bound NADP is recycled, not consumed in its net equation. |
| primary2002 | https://pmc.ncbi.nlm.nih.gov/articles/PMC139585/; Original article //article//p14,19,21,23,25,29; PMID:11751812 body hash in audit. | supports | ATP-dependent bifunctional HldE and GmhB support the route; the GmhA reagent is from Aneurinibacillus, not E. coli, and that source scope is preserved. |
| primary2010 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2844806/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC2844805/; BioC offsets 6284,12476,15508,16641,17361,20251,21102,23631,28097 and second article paragraph 43. | supports | GmhB is monomeric and strongly beta-selective with measurable alpha activity. Mg catalysis and alternative Mn/Co are distinct from the cysteine-loop zinc site whose physiological role remains unresolved. |
| otherprimary | https://pubmed.ncbi.nlm.nih.gov/18056714/ ; https://pubmed.ncbi.nlm.nih.gov/16030223/ ; https://pubmed.ncbi.nlm.nih.gov/10896473/ ; https://pubmed.ncbi.nlm.nih.gov/11313358/ ; https://pubmed.ncbi.nlm.nih.gov/17316025/ ; https://pubmed.ncbi.nlm.nih.gov/7929099/; Retained indexed abstracts; exact response body hashes in independent audit. | supports | These scoped abstracts support enzyme structure/function and historical cofactor context. Functional HldE dimer is distinguished from domain-only measurements; HldD pentamer from a crystal pair of pentamers; later NADP evidence refines earlier NAD wording. |
| authorities | research/pathway_additions/2026-10-11-nicotine-next/authority-protein-crosscheck.json; P63224/P76658/P63228/P67910 rows and source/ontology authority crosschecks. | supports | Names and identities match independently acquired current authorities. Discovery PathBank human LPCAT4 and organic-dye diphosphate near-misses were rejected. |
| dedup | research/pathway_additions/2026-10-11-nicotine-next/adhp-dedup.json; Ignored-inclusive author search ledger and root full maintained-record comparison. | supports | No duplicate exact maintained route among180 baseline records. Broader GO boundaries and adjacent sugar routes were compared explicitly. |
| imodulon | research/pathway_additions/2026-10-11-nicotine-next/imodulondb-context.json; Exact E. coli gene and locus queries; separate unchanged-client parser replay and raw-response hashes. | context_only | Expression context provides no direct catalysis evidence. No module-name matches are treated as evidence of biological absence. |
| gates | research/pathway_additions/2026-10-11-nicotine-next/integration-validation.json; Terminal full-corpus command exits, log digests, exact scope and reports. | supports | Root executed final data/QC gates on frozen inputs and inspected terminal logs. Full tests began before other targets final wording fixes and completed after them; implementation/tests were unchanged. Earlier stale-page failure was corrected by rerender and final validation. |
| graph | research/pathway_additions/2026-10-11-nicotine-next/generated-graph-kgx-audit.json; ADP-heptose graph row and full export projection checks. | supports | Generated graph nodes,43 edges, 86 evidence entries, direction and context survive rendering/export; assessment is structural. No enabled browser was available. |

## Limits And Additional Notes

- Six additional primary studies were inspected as indexed abstracts; no full-text claims are attributed to them.
- GmhA formal alpha/beta equation does not measure physiological anomer ratio; the 2002 GmhA assay reagent is heterologous.
- GmhA zinc remains similarity-based; GmhB loop-zinc physiological role remains unresolved, and alternative catalytic metals do not imply simultaneous occupancy.
- Later NADP characterization and earlier NAD activity are preserved without treating either as net consumed cofactor.
- No browser surface was available; diagram checks are structural, not visual or interactive.
- Original Documents checkout remains inaccessible; ignored-inclusive dedup claims cover the accessible worktree, not that checkout.
- This review covers ADP-heptose science only; shared technical gate authorship is disclosed.
- started_at records actual initial inspection-file completion time, before target/source assessment. All four original input hashes remained unchanged at final inspection.
- Source acquisition was shared; interpretation and independent RDF/native replay were performed separately from author validation.
- Earlier whole-corpus validation detected pages rendered before other targets final edits; final integrated pages were rerendered and validated. No ADP science change was needed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T024320Z-adp-heptose-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of ADP-heptose biosynthesis
started_at: '2026-10-11T02:28:16.659091Z'
finished_at: '2026-10-11T02:43:20Z'
reviewer:
  identity: Codex /root
  kind: agent
  independence: independent
  independence_basis: Did not author ADP record or author evidence dossiers/replay.
    Independently read the whole target, inspected original primary and structured
    sources and wrote a distinct source audit. Owns shared integration and authored
    the separate lipoate target, excluded here.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete five-step ADP-L-glycero-beta-D-manno-heptose pathway is supported
  with no confirmed finding. Exact chemistry, K-12 proteins and physical assemblies
  preserve anomer, cofactor, strain and evidence-tier limitations. Final corpus and
  generated structural checks pass.
source:
  git_revision: e3bceba7613eb0525af3ff76ef32520201ae9f33
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
    sha256: 563ace71ecbab2ccdf71e353813afe89988024b9f46288611cbfb97db726c67f
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 88dfc909cc4efc39e0c4c05a7c4d721ec6f2e68d4d4f431df1f1d4c4307d80fe
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: c5efa10d14da146c39262662f330c6a39be9be71c5072dd619d644bc2724be6c
    role: context
  - path: data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
    sha256: affa9eb37e5575d895dc7ae93173037ff18019e2a5e74012139b6aacb6febaf3
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
    sha256: d6b86bb8115d079f0f70a03dbcdf0956c058ca397b4688aa0da1bc0646829c5d
    role: context
  - path: pages/downloads/nodes.tsv
    sha256: 7e793435baa97d19bc0ecc1e839fcad7dd6dddf7bd9be89f4d0ba0873c9c9d07
    role: context
  - path: pages/records/MetaCyc_PWY0-1241.html
    sha256: 94f9cdddc144f862675cd5ea4d7b9514219e3b268c8ae3cd6cd9b70124f07eeb
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/adhp-chemistry-projection.json
    sha256: c69f933ecd1a576ac4e8ab06d6d8619fb26dad892779a51bdf13968bca426850
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/adhp-curation.md
    sha256: c3bf6496ff5dd33f013dbad77cb200f90eae7cbdce75fe88b7f84b20f1964b93
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/adhp-dedup.json
    sha256: d228c3c9838258a08c0e876aed9ae3eab54de43f23bb436849e45ac4a9df45da
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/adhp-independent-audit.json
    sha256: f49acb6977c4abb7359e56e45855eda53e5c44289445621a3f548eac53366101
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/adhp-source-manifest.json
    sha256: a1a02c4e537c99f16ea7aeb5ad752afbf1302d9383919732076bf353e1f0ea3b
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/adhp-validation.json
    sha256: 86b9341ccd24fb57eea9da7899c6334c688908700fb747d403744a7de11d1dd4
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/authority-integration.json
    sha256: 508115133210b4b274705562e606b38ce33b774d0b26f9779dc1cd539eff34f1
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/authority-protein-crosscheck.json
    sha256: 7865b01494836dd3e6b104bc804cc013cdefd424f6ee2fcbcdbd3661fcb571eb
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/authority-source-inspection.json
    sha256: 6819051b3cde54f86e72f75c4ddcf7a576a5d56334b32a338125fa211fb4b216
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/baseline-preservation.json
    sha256: 1759ef38d27e253e1f35206ac7a5d0269ff0d8e1325ceb710b58676624229492
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/browser-availability.json
    sha256: 7dd0d8c23add2134ecf6331ccd914d32bcc071e731387a7b76548cf72bce2242
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/generated-graph-kgx-audit.json
    sha256: 2012413903397cabd2554fcd7a80841f8db8e3e6c059dc2d2d4f390860d7720a
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/identifiers-added.json
    sha256: 2ded3d838d4b40e718ec883fed44dc04d2cecd2c660faaed7c43130ff7e736d5
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-context.json
    sha256: 44fe95b9cef24af8f4ba69d7b845142d40e63e1ed42ac29db6e8a26361c0c0a9
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-parser-replay.json
    sha256: e0615d4d3eade07658e352e572426479dac155c525c1cf460daaa6846f601f91
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-runner-availability.json
    sha256: f996c636a02f9e017b5831003fa27d0577576dfe355fa9a5097f59644c880698
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-source-manifest.json
    sha256: 4ae60106c78976dcf8396ec0646e69f74d70ea70c018659430223d37e66a9af6
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/integration-validation.json
    sha256: 33ca08ff4c31d5f2c03c0b3732b731e2b9d64ad583066f4360cfcddcf5797975
    role: context
  - path: research/pathway_additions/2026-10-11-nicotine-next/vendored-check.json
    sha256: 6fec71b0699a897e0ec24c7842d08687d52d1e9da5525b7a28b5914f859fa6e8
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
scope:
  description: 'Entire single resolved pathway: 26 participants, 5 reactions, 43 edges
    and 86 evidence blocks.'
  selection: Root independently reviews the record authored by another agent; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY0-1241
  exclusions:
  - target: Other pathways including root-authored lipoate
    reason: Separate independent reviewers own those scientific assessments.
targets:
- target_id: MetaCyc:PWY0-1241
  path: data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
  label: ADP-L-glycero-beta-D-manno-heptose biosynthesis
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
    role: maintained_record
  record_class: Pathway
checks:
- check_id: initial-final-inspect
  name: Governed input inspection
  status: passed
  required: true
  summary: Initial inspection preceded the scientific assessment. Final inspection
    rechecked every original hash unchanged and captured final shared inputs.
  command: scripts/record_review.py inspect with retained targets and input paths
  exit_code: 0
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - record
  - audit
- check_id: independent-source-replay
  name: Independent original-source replay
  status: passed
  required: true
  summary: All 19 chemical sides, 5 atom/charge balances, 5 native reaction mappings,
    3 physical assemblies and 30 reference hashes passed independently of the author
    replay.
  command: .venv/bin/python /private/tmp/pathwaymech-adhp-independent-audit.py
  exit_code: 0
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - audit
  - rhea
  - native
- check_id: corpus-1
  name: just render-pages
  status: passed
  required: true
  summary: Actual terminal exit 0; exact log digest verified.
  command: just render-pages
  exit_code: 0
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - gates
  scope_note: Full integrated corpus execution by this root reviewer, separate from
    scientific judgement. See integration receipt for full-test timing across other
    targets wording edits.
- check_id: corpus-2
  name: just lint
  status: passed
  required: true
  summary: Actual terminal exit 0; exact log digest verified.
  command: just lint
  exit_code: 0
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - gates
  scope_note: Full integrated corpus execution by this root reviewer, separate from
    scientific judgement. See integration receipt for full-test timing across other
    targets wording edits.
- check_id: corpus-3
  name: git diff --check
  status: passed
  required: true
  summary: Actual terminal exit 0; exact log digest verified.
  command: git diff --check
  exit_code: 0
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - gates
  scope_note: Full integrated corpus execution by this root reviewer, separate from
    scientific judgement. See integration receipt for full-test timing across other
    targets wording edits.
- check_id: corpus-4
  name: just check-identifiers
  status: passed
  required: true
  summary: Actual terminal exit 0; exact log digest verified.
  command: just check-identifiers
  exit_code: 0
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - gates
  scope_note: Full integrated corpus execution by this root reviewer, separate from
    scientific judgement. See integration receipt for full-test timing across other
    targets wording edits.
- check_id: corpus-5
  name: just kgx-export --output-dir /private/tmp/pathwaymech-nicotine-next-kgx
  status: passed
  required: true
  summary: Actual terminal exit 0; exact log digest verified.
  command: just kgx-export --output-dir /private/tmp/pathwaymech-nicotine-next-kgx
  exit_code: 0
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - gates
  scope_note: Full integrated corpus execution by this root reviewer, separate from
    scientific judgement. See integration receipt for full-test timing across other
    targets wording edits.
- check_id: corpus-6
  name: just validate
  status: passed
  required: true
  summary: Actual terminal exit 0; exact log digest verified.
  command: just validate
  exit_code: 0
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - gates
  scope_note: Full integrated corpus execution by this root reviewer, separate from
    scientific judgement. See integration receipt for full-test timing across other
    targets wording edits.
- check_id: corpus-7
  name: just test
  status: passed
  required: true
  summary: '{''passed'': 1048, ''skipped'': 3, ''warnings'': 3, ''seconds'': 594.56}'
  command: just test
  exit_code: 0
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - gates
  scope_note: Full integrated corpus execution by this root reviewer, separate from
    scientific judgement. See integration receipt for full-test timing across other
    targets wording edits.
- check_id: corpus-8
  name: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  status: passed
  required: true
  summary: Actual terminal exit 0; exact log digest verified.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  exit_code: 0
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - gates
  scope_note: Full integrated corpus execution by this root reviewer, separate from
    scientific judgement. See integration receipt for full-test timing across other
    targets wording edits.
- check_id: browser
  name: Interactive browser inspection
  status: unavailable
  required: false
  summary: Actual enabled-surface inventory was empty; no visual or interaction claim.
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - graph
evidence:
- evidence_id: record
  kind: record_content
  reference: data/pathways/adp-l-glycero-beta-d-manno-heptose-biosynthesis.yaml
  locator: Entire 890-line target; all 26 participants, 5 reactions, 43 edges, 86
    evidence entries.
  accessed_at: '2026-10-11T02:43:20Z'
  support: supports
  summary: Independent full target assessment after governed initial inspect; scientific
    target and author evidence inputs stayed unchanged.
  snapshot_sha256: affa9eb37e5575d895dc7ae93173037ff18019e2a5e74012139b6aacb6febaf3
- evidence_id: audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-nicotine-next/adhp-independent-audit.json
  locator: Independent original RDF/native XML replay, all 30 reference hashes and
    primary passage locators.
  accessed_at: '2026-10-11T02:43:20Z'
  support: supports
  summary: Root did not author ADP; independently wrote direct source checks and inspected
    the source text. Nineteen exact reaction sides, five atom/charge balances and
    three exact assemblies pass.
  snapshot_sha256: f49acb6977c4abb7359e56e45855eda53e5c44289445621a3f548eac53366101
- evidence_id: native
  kind: database
  reference: https://pathway.yeastgenome.org/getxml?META:PWY0-1241
  locator: Complete reaction-list/reaction-ordering and each native reaction Rhea
    dblink; CPLX0-7660/3661/3681 and exact UniProt monomer bridges.
  accessed_at: '2026-10-11T02:43:20Z'
  support: supports
  summary: Full native five-step route begins at sedoheptulose 7-phosphate. GO:0097171
    begins one reaction later. Native complexes support GmhA tetramer, HldE dimer
    and HldD pentamer.
- evidence_id: rhea
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Masters 27490,27474,28519,27466,17578; native sides, contains coefficients
    and ChEBI identities.
  accessed_at: '2026-10-11T02:43:20Z'
  support: supports
  summary: All equations balance. GmhA formal equation yields both anomers from two
    substrates; it does not measure their cellular ratio. Charge, stereochemistry
    and hydrolysis products are exact.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: uniprot
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P63224.json ; https://rest.uniprot.org/uniprotkb/P76658.json
    ; https://rest.uniprot.org/uniprotkb/P63228.json ; https://rest.uniprot.org/uniprotkb/P67910.json
  locator: Complete organism/gene, function, catalytic activity, cofactor and subunit
    annotations; each raw body hash in audit.
  accessed_at: '2026-10-11T02:43:20Z'
  support: supports
  summary: Correct K-12 catalysts and molecular assemblies. GmhA zinc is inferred
    by similarity; GmhB catalytic metal alternatives and loop zinc differ in role.
    HldD bound NADP is recycled, not consumed in its net equation.
- evidence_id: primary2002
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC139585/
  locator: Original article //article//p14,19,21,23,25,29; PMID:11751812 body hash
    in audit.
  accessed_at: '2026-10-11T02:43:20Z'
  support: supports
  summary: ATP-dependent bifunctional HldE and GmhB support the route; the GmhA reagent
    is from Aneurinibacillus, not E. coli, and that source scope is preserved.
- evidence_id: primary2010
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2844806/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC2844805/
  locator: BioC offsets 6284,12476,15508,16641,17361,20251,21102,23631,28097 and second
    article paragraph 43.
  accessed_at: '2026-10-11T02:43:20Z'
  support: supports
  summary: GmhB is monomeric and strongly beta-selective with measurable alpha activity.
    Mg catalysis and alternative Mn/Co are distinct from the cysteine-loop zinc site
    whose physiological role remains unresolved.
- evidence_id: otherprimary
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/18056714/ ; https://pubmed.ncbi.nlm.nih.gov/16030223/
    ; https://pubmed.ncbi.nlm.nih.gov/10896473/ ; https://pubmed.ncbi.nlm.nih.gov/11313358/
    ; https://pubmed.ncbi.nlm.nih.gov/17316025/ ; https://pubmed.ncbi.nlm.nih.gov/7929099/
  locator: Retained indexed abstracts; exact response body hashes in independent audit.
  accessed_at: '2026-10-11T02:43:20Z'
  support: supports
  summary: These scoped abstracts support enzyme structure/function and historical
    cofactor context. Functional HldE dimer is distinguished from domain-only measurements;
    HldD pentamer from a crystal pair of pentamers; later NADP evidence refines earlier
    NAD wording.
- evidence_id: authorities
  kind: authority
  reference: research/pathway_additions/2026-10-11-nicotine-next/authority-protein-crosscheck.json
  locator: P63224/P76658/P63228/P67910 rows and source/ontology authority crosschecks.
  accessed_at: '2026-10-11T02:43:20Z'
  support: supports
  summary: Names and identities match independently acquired current authorities.
    Discovery PathBank human LPCAT4 and organic-dye diphosphate near-misses were rejected.
  snapshot_sha256: 7865b01494836dd3e6b104bc804cc013cdefd424f6ee2fcbcdbd3661fcb571eb
- evidence_id: dedup
  kind: search
  reference: research/pathway_additions/2026-10-11-nicotine-next/adhp-dedup.json
  locator: Ignored-inclusive author search ledger and root full maintained-record
    comparison.
  accessed_at: '2026-10-11T02:43:20Z'
  support: supports
  summary: No duplicate exact maintained route among180 baseline records. Broader
    GO boundaries and adjacent sugar routes were compared explicitly.
  snapshot_sha256: d228c3c9838258a08c0e876aed9ae3eab54de43f23bb436849e45ac4a9df45da
  search_scope: Root rg --no-ignore --hidden over the accessible worktree, excluding
    Git internals and .venv, using exact PWY0-1241 and pathway-name patterns; author
    ledger also records broader candidate comparison. Only the new target matched
    a maintained pathway. Original Documents checkout is inaccessible.
- evidence_id: imodulon
  kind: database
  reference: research/pathway_additions/2026-10-11-nicotine-next/imodulondb-context.json
  locator: Exact E. coli gene and locus queries; separate unchanged-client parser
    replay and raw-response hashes.
  accessed_at: '2026-10-11T02:43:20Z'
  support: context_only
  summary: Expression context provides no direct catalysis evidence. No module-name
    matches are treated as evidence of biological absence.
  snapshot_sha256: 44fe95b9cef24af8f4ba69d7b845142d40e63e1ed42ac29db6e8a26361c0c0a9
- evidence_id: gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-nicotine-next/integration-validation.json
  locator: Terminal full-corpus command exits, log digests, exact scope and reports.
  accessed_at: '2026-10-11T02:43:20Z'
  support: supports
  summary: Root executed final data/QC gates on frozen inputs and inspected terminal
    logs. Full tests began before other targets final wording fixes and completed
    after them; implementation/tests were unchanged. Earlier stale-page failure was
    corrected by rerender and final validation.
  snapshot_sha256: 33ca08ff4c31d5f2c03c0b3732b731e2b9d64ad583066f4360cfcddcf5797975
- evidence_id: graph
  kind: validation
  reference: research/pathway_additions/2026-10-11-nicotine-next/generated-graph-kgx-audit.json
  locator: ADP-heptose graph row and full export projection checks.
  accessed_at: '2026-10-11T02:43:20Z'
  support: supports
  summary: Generated graph nodes,43 edges, 86 evidence entries, direction and context
    survive rendering/export; assessment is structural. No enabled browser was available.
  snapshot_sha256: 2012413903397cabd2554fcd7a80841f8db8e3e6c059dc2d2d4f390860d7720a
assessments:
- assessment_id: identity
  area: identity
  topic: Complete native boundary
  outcome: supported
  summary: Full five-step native pathway is maintained, including the upstream isomerase
    omitted by narrower GO:0097171. Discovery names alone are not grounds for equivalence.
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - record
  - native
  - dedup
- assessment_id: chemistry
  area: grounding
  topic: Exact charged species and formal anomer equation
  outcome: supported
  summary: All five equations and nineteen chemical sides match original Rhea and
    balance. The two-substrate formal GmhA equation records both anomers without asserting
    a 1:1 physiological pool.
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - rhea
  - audit
- assessment_id: proteins
  area: evidence
  topic: K-12 enzymes, assemblies and source organisms
  outcome: supported
  summary: All four proteins and three exact assemblies are supported. Native and
    UniProt bridges match. Heterologous GmhA in the 2002 assay remains separate from
    K-12 protein annotation.
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - native
  - uniprot
  - primary2002
  - otherprimary
- assessment_id: cofactors
  area: representation
  topic: Catalytic alternatives and retained cofactors
  outcome: supported
  summary: GmhA Zn is inferred, GmhB catalytic Mg/Mn/Co differs from loop Zn, and
    HldD bound NADP is retained rather than added to net substrate/product chemistry.
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - uniprot
  - primary2010
  - otherprimary
- assessment_id: provenance
  area: provenance
  topic: Edge-local evidence and authority integrity
  outcome: supported
  summary: All 43 mechanistic assertions and 86 evidence entries were assessed against
    their nearest source, with full-text vs abstract and direct vs inferred tiers
    retained. All 30 retained reference-body digests match.
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - record
  - audit
  - authorities
- assessment_id: context
  area: scope
  topic: Expression evidence stays contextual
  outcome: supported
  summary: The actual canonical-client fallback and replay are recorded; expression
    search does not establish pathway identity, catalysis or biological absence.
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - imodulon
- assessment_id: integration
  area: schema
  topic: Corpus validation and generated graph
  outcome: supported
  summary: Required full-corpus checks pass after final rendering. Generated SVG and
    KGX preserve local evidence and graph semantics. Scientific assessment is independent
    of deterministic checks.
  target_ids:
  - MetaCyc:PWY0-1241
  evidence_ids:
  - gates
  - graph
findings: []
actions: []
limitations:
- Six additional primary studies were inspected as indexed abstracts; no full-text
  claims are attributed to them.
- GmhA formal alpha/beta equation does not measure physiological anomer ratio; the
  2002 GmhA assay reagent is heterologous.
- GmhA zinc remains similarity-based; GmhB loop-zinc physiological role remains unresolved,
  and alternative catalytic metals do not imply simultaneous occupancy.
- Later NADP characterization and earlier NAD activity are preserved without treating
  either as net consumed cofactor.
- No browser surface was available; diagram checks are structural, not visual or interactive.
- Original Documents checkout remains inaccessible; ignored-inclusive dedup claims
  cover the accessible worktree, not that checkout.
- This review covers ADP-heptose science only; shared technical gate authorship is
  disclosed.
notes:
- started_at records actual initial inspection-file completion time, before target/source
  assessment. All four original input hashes remained unchanged at final inspection.
- Source acquisition was shared; interpretation and independent RDF/native replay
  were performed separately from author validation.
- Earlier whole-corpus validation detected pages rendered before other targets final
  edits; final integrated pages were rerendered and validated. No ADP science change
  was needed.
links:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC139585/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2844806/
- https://pathway.yeastgenome.org/getxml?META:PWY0-1241
tags:
- independent-review
- adp-heptose
- pathway
```

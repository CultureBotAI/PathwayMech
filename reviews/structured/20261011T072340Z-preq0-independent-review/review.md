# Independent review of complete preQ0 biosynthesis and current Rhea authority

- Review: 20261011T072340Z-preq0-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T07:14:12Z
- Finished UTC: 2026-10-11T07:23:40Z
- Reviewer: Codex independent reviewer (/root/pathway_literature_candidates) (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete four-reaction GTP-to-preQ0 route is supported with explicit source and organism limits. All 30 local nodes, 41 edges and 70 evidence blocks were assessed. Current two-ATP QueC accounting independently agrees with original Rhea 142 and current UniProt. No actionable finding remains in this scope; inferred E. coli activities, cross-species experiments and alternative QueD assemblies remain explicit.

## Scope And Provenance

Full scientific assessment of one frozen complete preQ0 pathway plus the directly relevant Rhea authority integration.

Selection: Exact target SHA bbcf3f41f8c8996e045827f21672281f8f3040c2e51357eafb74e14fc050d4a6; canonical inspection preceded assessment; final source and gate inputs were rechecked.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 720ebcddbc421fbc01a4a82461fcbf13da7ea44f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097288 | data/pathways/7-cyano-7-deazaguanine-biosynthesis.yaml | maintained | 7-cyano-7-deazaguanine biosynthetic process |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical initial inspection | passed | True | GO:0097288 | Captured exact target and initial source hashes before judgment. |
| Independent original-source and export replay | passed | False | GO:0097288 | Actual session 80447 exited 0. Rehashed 44 original bodies, independently parsed 22 Rhea sides/four balances, checked native/UniProt pointers and literal quote, verified original current extractor outputs, all 1603 baseline ontology terms/four source metadata entries unchanged, and actual 41-edge/70-evidence KGX preservation. |
| Independent focused authority regression tests | passed | False | GO:0097288 | Actual session 51496 exited 0: 17 passed in 1.26s. Hash/missing/duplicate/identity/status/equation/class/unselected failures leave existing output untouched. |
| Independent unchanged-client offline replay | passed | False | GO:0097288 | Actual exit 0: 34 bodies, 31 searches and 2 component tables match acquisition context. QueD/E/C gene contexts are not catalytic proof; only returned modules inspected. |
| Read current issue 363 acceptance | passed | False | GO:0097288 | Network-restricted first read failed; authorized public API retry succeeded. Issue is OPEN; code/science acceptance assessed without claiming GitHub closure. |
| Canonical final input inspection | passed | True | GO:0097288 | All initial inputs independently rehashed unchanged; added final gate and technical inputs were read and rechecked before capture. |
| Coordinated superseded-initial-validate | failed | False | GO:0097288 | Observed exit 1; log SHA256 719abd105443efe46e141cd18c6fc7373f8d4cafadcc583a3178dfc1e167cd65. Initial page freshness failed because the lipid-A evidence changed after render. This is superseded by the full final rerender and full validation/test, not counted as a pass. Initial full test: one failed, 1058 passed, 3 skipped, 3 warnings. |
| Coordinated superseded-initial-test | failed | False | GO:0097288 | Observed exit 1; log SHA256 744b6c5d6a5152361d0c77bbe81f09684681cd3c94074062efaaee38796e8616. Initial page freshness failed because the lipid-A evidence changed after render. This is superseded by the full final rerender and full validation/test, not counted as a pass. Initial full test: one failed, 1058 passed, 3 skipped, 3 warnings. |
| Coordinated render | passed | True | GO:0097288 | Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-render.log independently rehashed to f474e395e2d89a95cabc61e10d2fd111e1c4852d51b023f421de697f7dd96755. Final frozen 201-record corpus and generated surface. |
| Coordinated validate | passed | True | GO:0097288 | Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-validate.log independently rehashed to 106851f36e8e3b27753cbe5b9317702aeff20f31e3ff42731663b5073f003d3c. Final frozen 201-record corpus and generated surface. |
| Coordinated lint | passed | True | GO:0097288 | Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-lint.log independently rehashed to df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41. Final frozen 201-record corpus and generated surface. |
| Coordinated identifiers | passed | True | GO:0097288 | Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-identifiers.log independently rehashed to d1ff997b826fe0c478aee483a401c5d579827ddc8bd36f76d5acb1813b3cd719. Final frozen 201-record corpus and generated surface. |
| Coordinated kgx | passed | True | GO:0097288 | Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-kgx.log independently rehashed to 2cc7a4ebafad46c0f34f1fa6edeba1f0197cf1c1a270df440b451f26950c9f4f. Final frozen 201-record corpus and generated surface. |
| Coordinated diff | passed | True | GO:0097288 | Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-diff.log independently rehashed to e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. Final frozen 201-record corpus and generated surface. |
| Coordinated test | passed | True | GO:0097288 | Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-test-final.log independently rehashed to 9a5d08bea9d6de04c0c8b3ef4475fdfc23e438e5e78101039d1517e3616e7b01. 1059 passed, 3 skipped, 3 warnings in 409.16s (0:06:49) |
| Coordinated vendored | passed | True | GO:0097288 | 22 governed artifacts match; observed exit 0 and exact log hash b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6. |

## Scientific And Domain Assessments

### Exact full native endpoint

identity: supported. Targets: GO:0097288.

GO:0097288 matches the independently defined complete PWY-6703 route. The broad nine-reaction PathBank map is explicitly a lead, with all 18 combined source reactions dispositioned. QueF and RNA maturation are outside the chosen independently defined pathway.

### Charged chemistry and current net equations

grounding: supported. Targets: GO:0097288.

All four directed reactions, 22 coefficient-bearing sides, named metabolites and three material-flow connections are supported. Current QueC chemistry is retained with source-version differences explicit.

### Protein identities, roles, assemblies and cofactor scope

evidence: supported. Targets: GO:0097288.

Direct FolE/QueD evidence and inferred QueE/QueC roles remain distinct. Original source assertions support the declared assemblies and cofactors at their stated grades; no universal assembly, monomer sufficiency or cross-species experiment is implied.

### Nearest source attribution and quote fidelity

provenance: supported. Targets: GO:0097288.

All 70 evidence entries are source-separated and locators were checked against original bodies. The literal zinc quote matches. Primary access limitations are explicit; indexed abstracts are not presented as full-text experiments.

### Expression and assay limits

scope: supported. Targets: GO:0097288.

The record does not infer catalysis from iModulon data, anaerobic-only cellular flux from handling conditions, or a physiological QueE donor from assay components.

### Current Rhea authority without label-policy relaxation

representation: supported. Targets: GO:0097288.

The implemented issue 363 fix satisfies the inspected extraction/preservation/fail-closed acceptance criteria. Named current equations are independently grounded; the canonical GO reaction-label policy remains unchanged. Reference-only historical master labels are accurately source-versioned and are not active named-node chemical assertions.

### Complete exported local graph and gates

graph: supported. Targets: GO:0097288.

All 30 local nodes, 41 edges, 70 evidence entries and reference metadata survive the actual export. Final coordinated gates and graph checks support publication consistency within the stated scientific limits.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: GO:0097288. Retain the exact complete free-preQ0 route; do not equate it with the broader PathBank metabolism map or append downstream RNA chemistry.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | MetaCyc:PWY-6703 and GO:0097288; Native pathway reaction-list/species and QuickGO results[0]/definition/text | supports | Original native source explicitly includes the four selected transformations and MG1655; exact GO definition ends at free preQ0. Broader PathBank objects were independently inspected and not silently equated to this endpoint. |
| chemistry | Official Rhea 142 RDF and ChEBI 255 original sources; Four directionalReaction/side/containsN/participant/compound/accession chains; source labels/formulas/charges | supports | All 22 chemical side occurrences and four equations independently balance. QueC uses 2 ATP → 2 AMP + 2 diphosphate; old MetaCyc/PathBank/Rhea 139 one-ATP accounting is explicitly superseded. No duplicate component reactions or net SAM consumption. Independent review audit preserves exact source hashes. |
| protein | UniProt:P0A6T5,P65870,P64554,P77756 and original native assemblies; Full original comments/features/cross-references; native component/coefficient/catalyzes | supports | Four reviewed K-12 identities, FolE decamer, QueD source-defined hexamer and alternative solution states, exact catalytic/cofactor inference grades and source pointers independently checked. QueE/QueC enables roles do not assert monomer sufficiency. |
| qued | PMID:19231875 / PMC3227869; BioC passages 5–9; Figure 2A/D and caption 17 | supports | Direct E. coli FolE/QueD assays, isotope-resolved product identification, synthetic co-elution, acetaldehyde and 1.1 zinc equivalents support the selected chemistry. The one literal quote exactly occurs in passage 9. |
| reconstruction | PMID:19354300 / PMC2693876; BioC passages 9–22, 34–43, 104–105 | supports | Original cloning and assays establish a mixed-species reconstruction: E. coli FolE/QueD, Bacillus QueE/QueC or Streptomyces ToyM. The isolated inconsistent E. coli section heading is not treated as enzyme provenance. Zinc and isotope chemistry retain source taxa. |
| quee | PMID:23194065 / PMC4022186; BioC passages 1, 7–8, 19–20, 31–44, 47–68; Figure 3e | supports | Bacillus QueE cluster, magnesium dependence, homodimer and 15-fold SAM-supported turnover were independently read. E. coli FldA/FPR are assay activation components, not proven physiological donors to E. coli QueE. |
| toym | PMID:26228534 / PMC4767005; BioC passages 3–11; Figures 3–5 | supports | Streptomyces ToyM experiments resolve two ATP-dependent adenylations through an amide, with AMP and PPi. This supports current net mechanism without claiming directly measured E. coli stoichiometry. |
| genetics | PMID:16199558; EuropePMC resultList/result[0]/abstractText | supports | B105 complementation and upstream placement support the E. coli genetic role; the abstract does not measure purified-protein net stoichiometry. |
| expression | iModulonDB e_coli/precise_mg1655; Retained query bodies, dataset inventory and component 39/68 tables | context_only | Independent offline unchanged-client replay agrees with all 34 retained bodies. No QueD/E/C membership in the two returned tables is a bounded observation, not biological absence. |
| technical | Issue363 and current Rhea authority implementation; scripts/build_ontology_identifier_snapshot.py:143; conf/rhea_identifier_updates.json; 17 focused tests | supports | Independently inspected native identity/status/equation checks, pinned full RDF digest, exact two-ID selection, no stale synonym and fail-before-write behavior. Actual current extraction matches independent RDF parsing; all prior ontology terms and metadata are preserved. |
| gates | Root coordinated final gate and graph receipts; Final integration receipt and byte-hashed terminal logs | supports | Actual final results were inspected; initial incomplete/stale-page results are retained distinctly in checks. Deterministic gates support repository consistency, not biological truth. |

## Limits And Additional Notes

- E. coli QueE/QueC exact activities and associated cofactors are reviewed HAMAP inferences; the primary Bacillus/Streptomyces experiments do not become purified E. coli measurements.
- The QueD native crystallographic hexamer and reviewed solution trimer/dodecamer states are not resolved into one universal physiological assembly.
- Complete BioC manuscripts were inspected for four principal biochemical papers. The 2005 genetics and two 2014 structure papers were inspected as abstracts; supporting information and raw spectra were not independently obtained.
- The reconstructed full route uses mixed species in primary experiments. Anaerobic assay handling and activation reagents do not establish exclusively anaerobic cellular flux or a specific E. coli electron donor.
- iModulonDB is bounded computational context, not catalytic proof or evidence of biological absence.
- Two newly named directional labels use current Rhea 142. Reference-only master terms retain accurately identified pinned Rhea 139 authority metadata; their historical labels are not current named-node equation assertions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T072340Z-preq0-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent review of complete preQ0 biosynthesis and current Rhea authority
started_at: '2026-10-11T07:14:12Z'
finished_at: '2026-10-11T07:23:40Z'
reviewer:
  identity: Codex independent reviewer (/root/pathway_literature_candidates)
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Reviewer did not author preQ0, its source dossiers, or the new
    Rhea authority extractor. Full target and original source assertions were independently
    read and replayed. Reviewer-authored lipid-A record is excluded.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete four-reaction GTP-to-preQ0 route is supported with explicit
  source and organism limits. All 30 local nodes, 41 edges and 70 evidence blocks
  were assessed. Current two-ATP QueC accounting independently agrees with original
  Rhea 142 and current UniProt. No actionable finding remains in this scope; inferred
  E. coli activities, cross-species experiments and alternative QueD assemblies remain
  explicit.
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
  - path: conf/rhea_identifier_updates.json
    sha256: b6126588233559a7243fbcba3ff4c3a94594831d57c64b3841d4805b1b5a27a1
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 5c89c140a1a674239a015dff3366a0d5ba5481447f733869e805ee9751e49dfe
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 9ce682d16ed2758938d09e93288630d8cd67b40564a8acb349d122e9364c06e8
    role: context
  - path: data/pathways/7-cyano-7-deazaguanine-biosynthesis.yaml
    sha256: bbcf3f41f8c8996e045827f21672281f8f3040c2e51357eafb74e14fc050d4a6
    role: target
  - path: docs/IDENTIFIERS.md
    sha256: e7970dcf5e070e34f605e6376ed23cc40985f4d17838fd11d4710fdda1aefa0b
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/authority-integration.json
    sha256: 4d0e517beaf62d0ecb1339ba678e83c689abaad6da45a814c1b4251cfcb7d7a1
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
  - path: research/pathway_additions/2026-10-11-next-198/preq0-authority-inputs.json
    sha256: a56dc34a7a002ec47bf193f9c2b2091bb6737f19f94f5c90afc666c71835b3f8
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/preq0-curation.md
    sha256: a20d9a48929823dfbc228bcbf4f4329b46db149df751afb61d30143ebe04d4fc
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/preq0-dedup.json
    sha256: 825b3cc7097e5b6837df4746564d2220cac5e96b28478cb44bd05c07cc008c8b
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/preq0-identifiers.json
    sha256: da1610eaf95fd07c6c91d72b2ff5d923fceb4595e724e4012e819ca53a7391ae
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/preq0-independent-review-audit.json
    sha256: 1aebacc653fa4d8c1165d3679deb5b53a919ebbdb0e02727fd4ee282eef8b548
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/preq0-replay.py
    sha256: b61611f09236c72e64f53ffee8cab9d1c5ad404629a1439663673633fcee6e1b
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/preq0-source-manifest.json
    sha256: 3f97bb43b31fc42a11072096c39e57d036878a076ded2fc845f4d7593fba340b
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/preq0-source-projection.json
    sha256: 8d20abcf79d2d5b70cdb1c120a22680a9975dd7115264c6cec490a7e414159cc
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/preq0-validation.json
    sha256: be5faa7e3732cdf0b434f2a8af7437ca7fc541c540b561453d9d73f6d196bff1
    role: context
  - path: research/pathway_additions/2026-10-11-next-198/rhea-equation-update-audit.json
    sha256: 7d4222d3151394225dc78b7ca59bd0dd78af0cfa064bb2fcdb3ceb097ba8c704
    role: context
  - path: scripts/build_ontology_identifier_snapshot.py
    sha256: 538dc16bbe67b5f5a3faacf01c968f32900b6fdb76e71f55ebb933ccf8e7a715
    role: context
  - path: src/pathwaymech/schema.py
    sha256: f006e5b99cedd91b57a2c5fb938315a84b68822586d1602d4df9ccfdc851e98c
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: ffa1107da83c8ff173833662e78ba73c779bbab9f2da33cea993b614e99d6345
    role: context
  - path: tests/test_identifier_snapshot_builders.py
    sha256: 37351f7b99098b854ad6a91c9db66b793a127be04860efda230673382b868423
    role: context
targets:
- target_id: GO:0097288
  path: data/pathways/7-cyano-7-deazaguanine-biosynthesis.yaml
  label: 7-cyano-7-deazaguanine biosynthetic process
  kind: maintained
  ownership_note: Maintained pathway YAML; reviewed read-only by a non-author.
scope:
  description: Full scientific assessment of one frozen complete preQ0 pathway plus
    the directly relevant Rhea authority integration.
  selection: Exact target SHA bbcf3f41f8c8996e045827f21672281f8f3040c2e51357eafb74e14fc050d4a6;
    canonical inspection preceded assessment; final source and gate inputs were rechecked.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097288
  exclusions:
  - target: Reviewer-authored lipid-A record and all other pathway records
    reason: Outside this independent scientific scope.
  - target: All deazapurine or queuosine pathways and all organism-specific physiological
      conditions
    reason: The exact free-preQ0 endpoint is independently defined; downstream RNA
      chemistry is not covered by this record.
checks:
- check_id: initial-inspect
  name: Canonical initial inspection
  command: PYTHONPATH=src .venv/bin/python scripts/record_review.py inspect --targets
    /private/tmp/pathwaymech-next-198-preq0-review/targets.yaml (context inputs retained
    in inspect-initial.json)
  status: passed
  required: true
  exit_code: 0
  summary: Captured exact target and initial source hashes before judgment.
  target_ids:
  - GO:0097288
- check_id: original-source-replay
  name: Independent original-source and export replay
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    .venv/bin/python /private/tmp/pathwaymech-next-198-preq0-review/replay.py
  status: passed
  required: false
  exit_code: 0
  summary: Actual session 80447 exited 0. Rehashed 44 original bodies, independently
    parsed 22 Rhea sides/four balances, checked native/UniProt pointers and literal
    quote, verified original current extractor outputs, all 1603 baseline ontology
    terms/four source metadata entries unchanged, and actual 41-edge/70-evidence KGX
    preservation.
  target_ids:
  - GO:0097288
- check_id: builder-tests
  name: Independent focused authority regression tests
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    .venv/bin/pytest tests/test_identifier_snapshot_builders.py -q
  status: passed
  required: false
  exit_code: 0
  summary: 'Actual session 51496 exited 0: 17 passed in 1.26s. Hash/missing/duplicate/identity/status/equation/class/unselected
    failures leave existing output untouched.'
  target_ids:
  - GO:0097288
- check_id: imodulondb
  name: Independent unchanged-client offline replay
  command: PYTHONPATH=src .venv/bin/python /private/tmp/pathwaymech-next-198-preq0-review/imodulon-replay.py
  status: passed
  required: false
  exit_code: 0
  summary: 'Actual exit 0: 34 bodies, 31 searches and 2 component tables match acquisition
    context. QueD/E/C gene contexts are not catalytic proof; only returned modules
    inspected.'
  target_ids:
  - GO:0097288
- check_id: issue-read
  name: Read current issue 363 acceptance
  command: gh issue view 363 --repo CultureBotAI/PathwayMech --json number,title,body,state,url
  status: passed
  required: false
  exit_code: 0
  summary: Network-restricted first read failed; authorized public API retry succeeded.
    Issue is OPEN; code/science acceptance assessed without claiming GitHub closure.
  target_ids:
  - GO:0097288
- check_id: final-inspect
  name: Canonical final input inspection
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    .venv/bin/python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-198-preq0-review/targets.yaml
    --input conf/identifier_policy.yaml --input conf/identifier_sources.json --input
    conf/rhea_identifier_updates.json --input data/identifier_authorities/ontology.json
    --input data/identifier_authorities/sources.json --input docs/IDENTIFIERS.md --input
    research/pathway_additions/2026-10-11-next-198/authority-integration.json --input
    research/pathway_additions/2026-10-11-next-198/baseline-preservation.json --input
    research/pathway_additions/2026-10-11-next-198/generated-graph-kgx-audit.json
    --input research/pathway_additions/2026-10-11-next-198/imodulondb-context.json
    --input research/pathway_additions/2026-10-11-next-198/imodulondb-parser-replay.json
    --input research/pathway_additions/2026-10-11-next-198/imodulondb-runner-availability.json
    --input research/pathway_additions/2026-10-11-next-198/imodulondb-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-198/integration-receipt.json
    --input research/pathway_additions/2026-10-11-next-198/preq0-authority-inputs.json
    --input research/pathway_additions/2026-10-11-next-198/preq0-curation.md --input
    research/pathway_additions/2026-10-11-next-198/preq0-dedup.json --input research/pathway_additions/2026-10-11-next-198/preq0-identifiers.json
    --input research/pathway_additions/2026-10-11-next-198/preq0-independent-review-audit.json
    --input research/pathway_additions/2026-10-11-next-198/preq0-replay.py --input
    research/pathway_additions/2026-10-11-next-198/preq0-source-manifest.json --input
    research/pathway_additions/2026-10-11-next-198/preq0-source-projection.json --input
    research/pathway_additions/2026-10-11-next-198/preq0-validation.json --input research/pathway_additions/2026-10-11-next-198/rhea-equation-update-audit.json
    --input scripts/build_ontology_identifier_snapshot.py --input src/pathwaymech/schema.py
    --input src/pathwaymech/schema/pathwaymech.yaml --input tests/test_identifier_snapshot_builders.py
  status: passed
  required: true
  exit_code: 0
  summary: All initial inputs independently rehashed unchanged; added final gate and
    technical inputs were read and rechecked before capture.
  target_ids:
  - GO:0097288
- check_id: coordinated-0-superseded-initial-validate
  name: Coordinated superseded-initial-validate
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just validate
  status: failed
  required: false
  exit_code: 1
  summary: 'Observed exit 1; log SHA256 719abd105443efe46e141cd18c6fc7373f8d4cafadcc583a3178dfc1e167cd65.
    Initial page freshness failed because the lipid-A evidence changed after render.
    This is superseded by the full final rerender and full validation/test, not counted
    as a pass. Initial full test: one failed, 1058 passed, 3 skipped, 3 warnings.'
  target_ids:
  - GO:0097288
- check_id: coordinated-1-superseded-initial-test
  name: Coordinated superseded-initial-test
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just test
  status: failed
  required: false
  exit_code: 1
  summary: 'Observed exit 1; log SHA256 744b6c5d6a5152361d0c77bbe81f09684681cd3c94074062efaaee38796e8616.
    Initial page freshness failed because the lipid-A evidence changed after render.
    This is superseded by the full final rerender and full validation/test, not counted
    as a pass. Initial full test: one failed, 1058 passed, 3 skipped, 3 warnings.'
  target_ids:
  - GO:0097288
- check_id: coordinated-2-render
  name: Coordinated render
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just render-pages
  status: passed
  required: true
  exit_code: 0
  summary: Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-render.log
    independently rehashed to f474e395e2d89a95cabc61e10d2fd111e1c4852d51b023f421de697f7dd96755.
    Final frozen 201-record corpus and generated surface.
  target_ids:
  - GO:0097288
- check_id: coordinated-3-validate
  name: Coordinated validate
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just validate
  status: passed
  required: true
  exit_code: 0
  summary: Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-validate.log
    independently rehashed to 106851f36e8e3b27753cbe5b9317702aeff20f31e3ff42731663b5073f003d3c.
    Final frozen 201-record corpus and generated surface.
  target_ids:
  - GO:0097288
- check_id: coordinated-4-lint
  name: Coordinated lint
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just lint
  status: passed
  required: true
  exit_code: 0
  summary: Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-lint.log
    independently rehashed to df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41.
    Final frozen 201-record corpus and generated surface.
  target_ids:
  - GO:0097288
- check_id: coordinated-5-identifiers
  name: Coordinated identifiers
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just check-identifiers
  status: passed
  required: true
  exit_code: 0
  summary: Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-identifiers.log
    independently rehashed to d1ff997b826fe0c478aee483a401c5d579827ddc8bd36f76d5acb1813b3cd719.
    Final frozen 201-record corpus and generated surface.
  target_ids:
  - GO:0097288
- check_id: coordinated-6-kgx
  name: Coordinated kgx
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just kgx-export --output-dir
    /private/tmp/pathwaymech-next-198-kgx
  status: passed
  required: true
  exit_code: 0
  summary: Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-kgx.log
    independently rehashed to 2cc7a4ebafad46c0f34f1fa6edeba1f0197cf1c1a270df440b451f26950c9f4f.
    Final frozen 201-record corpus and generated surface.
  target_ids:
  - GO:0097288
- check_id: coordinated-7-diff
  name: Coordinated diff
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache git diff --check
  status: passed
  required: true
  exit_code: 0
  summary: Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-diff.log
    independently rehashed to e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
    Final frozen 201-record corpus and generated surface.
  target_ids:
  - GO:0097288
- check_id: coordinated-8-test
  name: Coordinated test
  command: PYTHONPATH=/private/tmp/pathwaymech-next-198-20261011/src UV_NO_SYNC=1
    UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just test
  status: passed
  required: true
  exit_code: 0
  summary: Observed terminal exit 0; exact log /private/tmp/pathwaymech-next-198-verification-test-final.log
    independently rehashed to 9a5d08bea9d6de04c0c8b3ef4475fdfc23e438e5e78101039d1517e3616e7b01.
    1059 passed, 3 skipped, 3 warnings in 409.16s (0:06:49)
  target_ids:
  - GO:0097288
- check_id: coordinated-9-vendored
  name: Coordinated vendored
  command: just vendored-check
  status: passed
  required: true
  exit_code: 0
  summary: 22 governed artifacts match; observed exit 0 and exact log hash b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6.
  target_ids:
  - GO:0097288
evidence:
- evidence_id: native
  kind: database
  reference: MetaCyc:PWY-6703 and GO:0097288
  locator: Native pathway reaction-list/species and QuickGO results[0]/definition/text
  accessed_at: '2026-10-11T07:23:40Z'
  support: supports
  summary: Original native source explicitly includes the four selected transformations
    and MG1655; exact GO definition ends at free preQ0. Broader PathBank objects were
    independently inspected and not silently equated to this endpoint.
  snapshot_sha256: 6ceddf0ef319853b2f7cbb8deebdb06f0f643fb6d256d79ce2cddb108d019db7
- evidence_id: chemistry
  kind: authority
  reference: Official Rhea 142 RDF and ChEBI 255 original sources
  locator: Four directionalReaction/side/containsN/participant/compound/accession
    chains; source labels/formulas/charges
  accessed_at: '2026-10-11T07:23:40Z'
  support: supports
  summary: All 22 chemical side occurrences and four equations independently balance.
    QueC uses 2 ATP → 2 AMP + 2 diphosphate; old MetaCyc/PathBank/Rhea 139 one-ATP
    accounting is explicitly superseded. No duplicate component reactions or net SAM
    consumption. Independent review audit preserves exact source hashes.
  snapshot_sha256: 1aebacc653fa4d8c1165d3679deb5b53a919ebbdb0e02727fd4ee282eef8b548
- evidence_id: protein
  kind: database
  reference: UniProt:P0A6T5,P65870,P64554,P77756 and original native assemblies
  locator: Full original comments/features/cross-references; native component/coefficient/catalyzes
  accessed_at: '2026-10-11T07:23:40Z'
  support: supports
  summary: Four reviewed K-12 identities, FolE decamer, QueD source-defined hexamer
    and alternative solution states, exact catalytic/cofactor inference grades and
    source pointers independently checked. QueE/QueC enables roles do not assert monomer
    sufficiency.
  snapshot_sha256: 3f97bb43b31fc42a11072096c39e57d036878a076ded2fc845f4d7593fba340b
- evidence_id: qued
  kind: primary_source
  reference: PMID:19231875 / PMC3227869
  locator: BioC passages 5–9; Figure 2A/D and caption 17
  accessed_at: '2026-10-11T07:23:40Z'
  support: supports
  summary: Direct E. coli FolE/QueD assays, isotope-resolved product identification,
    synthetic co-elution, acetaldehyde and 1.1 zinc equivalents support the selected
    chemistry. The one literal quote exactly occurs in passage 9.
  snapshot_sha256: 663cf3fe09cb4c85cedefde4f2dd34daacacae1fe4f0e8dff5a240a2d7a9c1b1
- evidence_id: reconstruction
  kind: primary_source
  reference: PMID:19354300 / PMC2693876
  locator: BioC passages 9–22, 34–43, 104–105
  accessed_at: '2026-10-11T07:23:40Z'
  support: supports
  summary: 'Original cloning and assays establish a mixed-species reconstruction:
    E. coli FolE/QueD, Bacillus QueE/QueC or Streptomyces ToyM. The isolated inconsistent
    E. coli section heading is not treated as enzyme provenance. Zinc and isotope
    chemistry retain source taxa.'
  snapshot_sha256: 96518ba9383486651b318b6e4097995880dbee1ec47b68d2c40e7ec69367e9fd
- evidence_id: quee
  kind: primary_source
  reference: PMID:23194065 / PMC4022186
  locator: BioC passages 1, 7–8, 19–20, 31–44, 47–68; Figure 3e
  accessed_at: '2026-10-11T07:23:40Z'
  support: supports
  summary: Bacillus QueE cluster, magnesium dependence, homodimer and 15-fold SAM-supported
    turnover were independently read. E. coli FldA/FPR are assay activation components,
    not proven physiological donors to E. coli QueE.
  snapshot_sha256: be5556c14ac6a44d5d16707cd10986e87fdf2310207ca4c91cf5aba6b6d223e9
- evidence_id: toym
  kind: primary_source
  reference: PMID:26228534 / PMC4767005
  locator: BioC passages 3–11; Figures 3–5
  accessed_at: '2026-10-11T07:23:40Z'
  support: supports
  summary: Streptomyces ToyM experiments resolve two ATP-dependent adenylations through
    an amide, with AMP and PPi. This supports current net mechanism without claiming
    directly measured E. coli stoichiometry.
  snapshot_sha256: 139b2847d21fd6929d4b5ed0db69ed2a8204c899c6a4e6ac54c0f1791d6995f2
- evidence_id: genetics
  kind: primary_source
  reference: PMID:16199558
  locator: EuropePMC resultList/result[0]/abstractText
  accessed_at: '2026-10-11T07:23:40Z'
  support: supports
  summary: B105 complementation and upstream placement support the E. coli genetic
    role; the abstract does not measure purified-protein net stoichiometry.
  snapshot_sha256: eb3c33d8e5cace384e83ca5723f231d8802b60bc9abfcbb82cc26552a0bc2c26
- evidence_id: expression
  kind: database
  reference: iModulonDB e_coli/precise_mg1655
  locator: Retained query bodies, dataset inventory and component 39/68 tables
  accessed_at: '2026-10-11T07:23:40Z'
  support: context_only
  summary: Independent offline unchanged-client replay agrees with all 34 retained
    bodies. No QueD/E/C membership in the two returned tables is a bounded observation,
    not biological absence.
  snapshot_sha256: 6eb0c20456431369a47f945a9379a9be66c68af11b229985c4ab8085583f28ea
- evidence_id: technical
  kind: validation
  reference: Issue363 and current Rhea authority implementation
  locator: scripts/build_ontology_identifier_snapshot.py:143; conf/rhea_identifier_updates.json;
    17 focused tests
  accessed_at: '2026-10-11T07:23:40Z'
  support: supports
  summary: Independently inspected native identity/status/equation checks, pinned
    full RDF digest, exact two-ID selection, no stale synonym and fail-before-write
    behavior. Actual current extraction matches independent RDF parsing; all prior
    ontology terms and metadata are preserved.
  snapshot_sha256: 1aebacc653fa4d8c1165d3679deb5b53a919ebbdb0e02727fd4ee282eef8b548
- evidence_id: gates
  kind: validation
  reference: Root coordinated final gate and graph receipts
  locator: Final integration receipt and byte-hashed terminal logs
  accessed_at: '2026-10-11T07:23:40Z'
  support: supports
  summary: Actual final results were inspected; initial incomplete/stale-page results
    are retained distinctly in checks. Deterministic gates support repository consistency,
    not biological truth.
  snapshot_sha256: 5a29f0d35faff53985010301cd322e4170424e6031dcc85ea705423a730ed985
assessments:
- assessment_id: identity
  area: identity
  topic: Exact full native endpoint
  outcome: supported
  summary: GO:0097288 matches the independently defined complete PWY-6703 route. The
    broad nine-reaction PathBank map is explicitly a lead, with all 18 combined source
    reactions dispositioned. QueF and RNA maturation are outside the chosen independently
    defined pathway.
  target_ids:
  - GO:0097288
  evidence_ids:
  - native
  - reconstruction
- assessment_id: chemistry
  area: grounding
  topic: Charged chemistry and current net equations
  outcome: supported
  summary: All four directed reactions, 22 coefficient-bearing sides, named metabolites
    and three material-flow connections are supported. Current QueC chemistry is retained
    with source-version differences explicit.
  target_ids:
  - GO:0097288
  evidence_ids:
  - chemistry
  - toym
- assessment_id: components
  area: evidence
  topic: Protein identities, roles, assemblies and cofactor scope
  outcome: supported
  summary: Direct FolE/QueD evidence and inferred QueE/QueC roles remain distinct.
    Original source assertions support the declared assemblies and cofactors at their
    stated grades; no universal assembly, monomer sufficiency or cross-species experiment
    is implied.
  target_ids:
  - GO:0097288
  evidence_ids:
  - protein
  - qued
  - quee
  - genetics
  - reconstruction
  dimensions:
  - name: ecoli_activity_tier
    value: FolE/QueD direct; QueE/QueC reviewed HAMAP inference
    definition: Catalytic role evidence distinguishes direct experiments from transferred
      annotation.
    evidence_ids:
    - protein
    - qued
    - reconstruction
  - name: qued_assembly
    value: Native crystallographic hexamer; solution trimers/dodecamers retained
    definition: Source-specific oligomer observations do not resolve one physiological
      state.
    evidence_ids:
    - protein
- assessment_id: provenance
  area: provenance
  topic: Nearest source attribution and quote fidelity
  outcome: supported
  summary: All 70 evidence entries are source-separated and locators were checked
    against original bodies. The literal zinc quote matches. Primary access limitations
    are explicit; indexed abstracts are not presented as full-text experiments.
  target_ids:
  - GO:0097288
  evidence_ids:
  - protein
  - qued
  - reconstruction
  - quee
  - toym
  - genetics
- assessment_id: context
  area: scope
  topic: Expression and assay limits
  outcome: supported
  summary: The record does not infer catalysis from iModulon data, anaerobic-only
    cellular flux from handling conditions, or a physiological QueE donor from assay
    components.
  target_ids:
  - GO:0097288
  evidence_ids:
  - expression
  - quee
- assessment_id: integration
  area: representation
  topic: Current Rhea authority without label-policy relaxation
  outcome: supported
  summary: The implemented issue 363 fix satisfies the inspected extraction/preservation/fail-closed
    acceptance criteria. Named current equations are independently grounded; the canonical
    GO reaction-label policy remains unchanged. Reference-only historical master labels
    are accurately source-versioned and are not active named-node chemical assertions.
  target_ids:
  - GO:0097288
  evidence_ids:
  - technical
  - chemistry
  - gates
- assessment_id: graph
  area: graph
  topic: Complete exported local graph and gates
  outcome: supported
  summary: All 30 local nodes, 41 edges, 70 evidence entries and reference metadata
    survive the actual export. Final coordinated gates and graph checks support publication
    consistency within the stated scientific limits.
  target_ids:
  - GO:0097288
  evidence_ids:
  - chemistry
  - technical
  - gates
findings: []
actions: []
limitations:
- E. coli QueE/QueC exact activities and associated cofactors are reviewed HAMAP inferences;
  the primary Bacillus/Streptomyces experiments do not become purified E. coli measurements.
- The QueD native crystallographic hexamer and reviewed solution trimer/dodecamer
  states are not resolved into one universal physiological assembly.
- Complete BioC manuscripts were inspected for four principal biochemical papers.
  The 2005 genetics and two 2014 structure papers were inspected as abstracts; supporting
  information and raw spectra were not independently obtained.
- The reconstructed full route uses mixed species in primary experiments. Anaerobic
  assay handling and activation reagents do not establish exclusively anaerobic cellular
  flux or a specific E. coli electron donor.
- iModulonDB is bounded computational context, not catalytic proof or evidence of
  biological absence.
- Two newly named directional labels use current Rhea 142. Reference-only master terms
  retain accurately identified pinned Rhea 139 authority metadata; their historical
  labels are not current named-node equation assertions.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/363
tags:
- preq0
- independent-review
- source-provenance
boundary_decisions:
- action: retain
  target_ids:
  - GO:0097288
  rationale: Retain the exact complete free-preQ0 route; do not equate it with the
    broader PathBank metabolism map or append downstream RNA chemistry.
  evidence_ids:
  - native
  - reconstruction
```

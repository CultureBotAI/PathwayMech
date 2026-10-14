# Initial adversarial scientific review of quinate degradation II

- Review: 20261014T191557Z-quinate-ii-initial-scientific-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-14T19:06:56Z
- Finished UTC: 2026-10-14T19:15:57Z
- Reviewer: codex /root/next257_adversarial (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact route identity, complete chemistry and most scoped bacterial/fungal claims are supported. One major QutB coenzyme-scope finding and three minor provenance/uncertainty findings remain open. Full-corpus validation failed separately on4 native participant labels; tests/lint have not run, so this is an honest partial initial observation.

## Scope And Provenance

One exact maintained pathway reviewed in full, with incomplete required technical gates.

Selection: Exact MetaCyc:PWY-6416 target requested for next257 adversarial review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 11afa1984bbb0d41c34dc82361bd0f0e1c0b9f37.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-6416 | data/pathways/quinate-degradation-ii.yaml | maintained | quinate degradation II |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus validation | failed | True | MetaCyc:PWY-6416 | Root executed just validate on exact input hashes;4 participant LABEL_MISMATCH results, exit1. Integration reviewer owns that separate finding. |
| Full test suite | skipped | True | MetaCyc:PWY-6416 | Root pipeline halted at failed validate before just test; no test pass claimed. |
| Repository lint | skipped | True | MetaCyc:PWY-6416 | Root pipeline halted at failed validate before just lint; no lint pass claimed. |
| Whitespace conflict check | passed | True | MetaCyc:PWY-6416 | Reviewer ran git diff --check and observed exit0. |
| Independent source and chemical replay | passed | False | MetaCyc:PWY-6416 | Raw42 reference bindings,8 molecular InChI identities and3 balanced Rhea families passed after reviewer-only RDF merge helper correction. |
| Independent protein/gene and construct replay | passed | False | MetaCyc:PWY-6416 | 22 protein/gene identities plus QsuD exact construct and QsuB CDS/primer boundaries verified. |
| Live structured source cross-check | passed | False | MetaCyc:PWY-6416 | Catalog and2 species-level searches succeeded; gene hits are context only and no component hit required summarize. |

## Scientific And Domain Assessments

### Exact pathway and reaction boundary

identity: supported. Targets: MetaCyc:PWY-6416.

Native PWY6416 denotes the NAD(P)-linked quinate→DHQ→DHS→PCA route; PQQ quinateI and two-step shikimate routes remain distinct. NAD-specific realization is explicitly not a fourth sequential step.

### Molecular sides, stereochemistry, charge and direction

grounding: supported. Targets: MetaCyc:PWY-6416.

Eight native molecules exactly match pinned ChEBI InChIs. Complete Rhea sides balance atoms and charge; native reversible DHQ dehydration and selected catabolic traversal remain distinct.

### Strain, assembly and construct grounding

scope: concern. Targets: MetaCyc:PWY-6416.

Exact source identities and major construct limitations are retained. QutB catalytic endpoint overstates NAD(P) scope; QsuB deposition wording exceeds the inspected evidence.

### Gene control, ligand and transport assertions

evidence: supported. Targets: MetaCyc:PWY-6416.

Gene-level QsuR and Qa regulator effects, qualified chorismate response and pH-dependent permease hypotheses have appropriately bounded support. Direct protein binding and broad physiological generalizations are not introduced.

### Selected native and literature coverage

completeness: supported. Targets: MetaCyc:PWY-6416.

All60 maintained edges and42 references reviewed. Formal reaction sides/order/taxa and relevant bacterial/fungal examples are represented; alternate PQQ enzymes, unrelated biosynthetic/petrobactin activities and unresolved source-metal spelling are legitimate exclusions. This is not exhaustive literature coverage.

### Edge-local source attribution

provenance: concern. Targets: MetaCyc:PWY-6416.

QsuB panel locator and missing nearest QsuD NADP-specificity evidence need bounded corrections. All42 source digests otherwise identify retained original artifacts.

### Full-corpus required gates

schema: concern. Targets: MetaCyc:PWY-6416.

Initial validate failed4 participant-label mismatches; this separately tracked integration defect blocks completion. Tests/lint were skipped when the pipeline halted.

## Findings

### F1: QutB assay is attached to a broader NAD(P) activity

major / open / confirmed; issue key: quinate-ii-qutb-nad-assay-scope.

Edge031 targets the broad native NAD(P) reaction although the inspected recombinant QutB table establishes NAD+ usage. Its description delegates coenzyme conditions to Table2 without retaining the actual NAD limitation. The exact NAD-specific reaction already exists locally; preserve the formal broad pathway member and native annotation context while targeting the measured chemistry.

### F2: QsuB qualifier overstates deposition absence

minor / open / confirmed; issue key: quinate-ii-qsub-deposition-absence.

All five QsuB qualifiers state that the complete internal assay-clone sequence was not independently deposited. The identity work establishes that no separately deposited complete assay-clone sequence was inspected; it does not establish global non-deposition. Retain this access limit rather than an unsupported absence claim.

### F3: Full-length QsuB inhibition cites the truncated-protein panel

minor / open / confirmed; issue key: quinate-ii-qsub-inhibition-panel.

Edge042 evidence locator says Fig7A, but the article caption assigns full-length QsuB to Fig7B and N-QsuB to Fig7A. Correct the locator or cite the figure plus caption without the conflicting panel letter; retain the already acknowledged concentration discrepancy.

### F4: QsuD NADP comparison lacks its nearest source assertion

minor / open / confirmed; issue key: quinate-ii-qsud-nadp-specificity-evidence.

Edge030 says NADP turnover is much lower but not absent. The retained native complex comment supports that statement; the two evidence objects on the edge do not. Add exact CPLX7981/comment evidence or remove the unsupported edge-local comparison. This lead was first raised by the author and independently verified by this reviewer.

## Recommended Actions And Acceptance Checks

### A1

Retarget qualified QutB catalysis to RHEA22365 and state NAD+ assay scope while retaining native broad annotation as context.

- Re-read primaryTable2 NAD+ and native ENZRXN17384.
- Confirm QutB catalytic edge targets exact RHEA22365 and retains fusion-conflict qualifier.
- Broad native formal pathway member and all reaction sides remain.
- Regenerate pathway pages and pass required full-corpus gates.

### A2

Replace non-deposition claim with inspected-access limitation on all5 QsuB qualifiers.

- All5 affected qualifiers say no separately deposited complete assay-clone sequence was inspected.
- No universal non-deposition assertion remains in target; source-gene/primer evidence remains unchanged.
- Regenerate pathway pages and pass required full-corpus gates.

### A3

Correct the QsuB inhibition source locator.

- Full-length inhibition locator agrees with caption or refers to Figure7 without wrong panel.
- Concentration discrepancy and construct-specific inhibition interpretation remain explicit.
- Regenerate pathway pages and pass required full-corpus gates.

### A4

Attach the native QsuD coenzyme-specificity comment to edge030.

- New structured evidence resolves exact CPLX7981/comment and faithfully states NADP turnover reduction.
- ATCC13032 construct versus strainR genetic scope stays distinct.
- Regenerate pathway pages and pass required full-corpus gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/pathways/quinate-degradation-ii.yaml; Entire YAML; 60 edges,41 participants,4 reactions,42 references | supports | Entire maintained target read, including every edge, qualifier, reference and the distinction between three formal steps and one NAD-specific realization. |
| raw | research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/raw-source-replay.json; reference_bindings; native_pathway; native_reactions; chemical_identities; rhea_sides | supports | Independently parsed raw MetaCyc XML and complete Rhea RDF:42 reference hashes bind originals;8 exact native/ChEBI InChIs agree;3 Rhea families have complete balanced sides. Native formal first reaction contains NAD(P), not exact NAD. |
| identities | research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/independent-identities.json; 22 selected gene/protein identities; QsuD_construct; QsuB_source_gene | supports | All selected UniProt/NCBIProtein/Entrez entries match exact accession and gene identity. QsuD structural sequence equals19-residue His6-containing prefix plus Q9X5C9. Independent QsuB CDS translation and P3/P4/P5 joins support source gene and terminal tag boundaries. |
| qutb | PMID:8257437; PMC1137716 scans pp455–456; Table2 | partial | Visually inspected Methods/Results and Table2. Assay table names NAD+; fusion preparation is described as N-terminal metal-chelating domain, while Table2 calls it GST. The draft preserves the fusion conflict but attaches catalysis to the broader NAD(P) reaction. |
| qsub | PMID:32822353; Complete inspected QsuB-2020 XML methods/results; supplement S1Table internally labelled S2Table; Fig7 | partial | ATCC13869/2256 PCR source, tagged constructs, DHS→PCA assay, alternative Co/Mg/Mn tests and PCA inhibition are supported. No full deposited assay-clone sequence was inspected. Caption assigns full-length QsuB to panelB, contrary to edge042 locatorA; Methods/caption concentration disagreement is preserved. |
| qsud | MetaCyc:CPLX-7981; /ptools-xml/Protein[@frameid="CPLX-7981"]/comment | partial | Native comment reports strong NAD preference and more than300-fold NADP turnover decrease. Edge030 currently cites only ENZRXN17380 and RXN20483, which do not contain that comparison. Its qualifier correctly separates associated structural sample and unknown cleavage across kinetics. |
| regulation | PMID:19376919; PMID:24674055; PMID:2943985; PMC2687277 Results/Fig5; publisher2014 web transcript Results202–288 and Methods; scanned1986 pp3596,3598 | supports | Inspected gene-level mutant/complementation effects, chorismate-dependent QsuR promoter-footprint data and historical Qa1F/Qa1S transcript genetics. Draft retains strain, experimental-construct and functional-versus-physical-binding distinctions. |
| qa2 | research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/qa2-primary-assessments.json; PMID126226 and143663 independently fetched primary abstracts; exact original hashes in artifact | supports | Native-host74-A purification and separate recombinant expression support the bounded curated Qa2 catalytic annotation. The draft correctly excludes UniProt Qa2 kinetic values misattributed from QutB Table2; it does not claim historical/reference-strain whole-sequence equality. |
| edge-ledger | research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/edge-assessments.json; All60 entries | supports | Every maintained edge assessed against raw source or inspected primary statement; retains curated inference, construct, direction, cofactor alternatives and bounded transport/regulation scope. |
| imodulon | research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/reviewer-check-history.json; Live public catalog and c_glutamicum/modulome263 qsu/quinate searches | supports | Species-level dataset is applicable. Searches return4 distinct gene annotations but zero iModulon components. These are expression-dataset annotation leads, not evidence of R/ATCC13869 protein identity or direct catalysis. No component summarization applicable. |
| gates | research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/receipts.json; just render-pages exit0; just validate exit1; exact 1240 core-input recheck artifact | refutes | Root ran full-corpus validation on exact inspected record. It failed4 MetaCyc participant label mismatches; test/lint pipeline did not run. Independent gate-input hash replay verified every bound path unchanged. This is a failed technical gate, not biological approval. |

## Limits And Additional Notes

- Required validate failed; required tests and lint were skipped after pipeline halt. No merge approval or completed technical pass.
- Several primary sources were available only as abstracts or selected scanned pages; the2014 QsuR full text was inspected through a retained publisher web transcript. No unavailable full-text methods are claimed inspected.
- No separately deposited complete QsuB assay-clone sequence was inspected. Primer/CDS joins establish source gene and construct boundaries without proving every internal assayed residue.
- Complete native source inventories were inspected as scoped author ledgers and raw targeted source objects; this review does not claim exhaustive biological characterization of all taxa or every cited background paper.
- iModulonDB gene annotation hits are context only. No direct catalysis or strain equivalence follows from expression-dataset presence.
- Raw complete source originals remain external; compact independent evidence and exact digests are retained in the repository.
- No maintained curation, authority files, history or pages were edited by this reviewer.
- Issue545 tracks F1/F4; issue546 tracks F2/F3.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T191557Z-quinate-ii-initial-scientific-review
kind: record
repository: CultureBotAI/PathwayMech
title: Initial adversarial scientific review of quinate degradation II
started_at: '2026-10-14T19:06:56Z'
finished_at: '2026-10-14T19:15:57Z'
reviewer:
  identity: codex /root/next257_adversarial
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Did not author or modify the maintained record, source acquisition
    plans, authority union or curation. Independently inspected originals and source
    text and wrote independent replay helpers. F4 was an author-suggested lead independently
    verified; root supplied exact-input gate receipts.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Exact route identity, complete chemistry and most scoped bacterial/fungal
  claims are supported. One major QutB coenzyme-scope finding and three minor provenance/uncertainty
  findings remain open. Full-corpus validation failed separately on4 native participant
  labels; tests/lint have not run, so this is an honest partial initial observation.
source:
  git_revision: 11afa1984bbb0d41c34dc82361bd0f0e1c0b9f37
  state: working_tree
  inputs:
  - path: data/pathways/quinate-degradation-ii.yaml
    sha256: c160a52490eafd406d7d4427c0a352cf05ef0a70fec2c01aaab164b3a2ceca09
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 4f3f46d1f4b8ebafa9b2d04d9700510df18b6ec6f881856fda521879f494d153
    role: context
  - path: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/edge-assessments.json
    sha256: 5be127a385bf532367f87fdf566aeed75a2cb546ffea4221282003e598549cb3
    role: context
  - path: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/independent-identities.json
    sha256: ca3cb473b6728d0ab01ca669b710281588aea354fcd2dfdce0823a21cb0717fe
    role: context
  - path: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/just-validate.log
    sha256: 7c15c75f33db91408eb7cdb06c7f95934ac2c24984c5d38c64c95f186283f556
    role: context
  - path: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/qa2-primary-assessments.json
    sha256: 8c2de6025dcd44a9d48210dfc133ef22357e01bde2ddadc291b71603acc5c4cc
    role: context
  - path: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/raw-source-replay.json
    sha256: 438f1291142acb0401771fa9846a781a4501af7311217a16e19230fea7a6dee2
    role: context
  - path: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/receipts.json
    sha256: 082a7c395ae65570ee34b81c79c1ee730c59e79aeddec88c9765abad0f804dc1
    role: context
  - path: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/reviewer-check-history.json
    sha256: c382f3ffdadcfd5c59fcb415d0f1954662d27bca1f4dc65826d5da8d25dc7d78
    role: context
  - path: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/root-gate-input-recheck.json
    sha256: be0a594b6ec628310446b7ea65f747ec38ee33ca1c41a4610d61717692284b71
    role: context
  - path: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/tested-core-input-hashes.json
    sha256: 005e8855057656a7fbb56dae9a4a4a980b82152f7b2c205570c3473d009838b2
    role: context
  - path: src/pathwaymech/schema.py
    sha256: bd99c1e6ca1f6eec5c82c58aa1ae3f43f696d30be66fbe0977dcace81292e0b8
    role: context
scope:
  description: One exact maintained pathway reviewed in full, with incomplete required
    technical gates.
  selection: Exact MetaCyc:PWY-6416 target requested for next257 adversarial review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-6416
  exclusions:
  - target: Other maintained pathways and full-source literature population
    reason: No fleet-wide review or exhaustive literature claim; additional organism
      extension leads remain.
  - target: Identifier-authority union preservation and four rejected participant
      labels
    reason: Separately reviewed by integration reviewer; validation failure explicitly
      retained here without duplicating its finding.
targets:
- target_id: MetaCyc:PWY-6416
  path: data/pathways/quinate-degradation-ii.yaml
  label: quinate degradation II
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/quinate-degradation-ii.yaml
    role: maintained pathway record
checks:
- check_id: validate
  name: Full-corpus validation
  status: failed
  required: true
  summary: Root executed just validate on exact input hashes;4 participant LABEL_MISMATCH
    results, exit1. Integration reviewer owns that separate finding.
  target_ids:
  - MetaCyc:PWY-6416
  command: just validate
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - gates
  scope_note: Reused actual root command receipt; reviewer independently verified
    all core input hashes and log digest.
- check_id: test
  name: Full test suite
  status: skipped
  required: true
  summary: Root pipeline halted at failed validate before just test; no test pass
    claimed.
  target_ids:
  - MetaCyc:PWY-6416
  scope_note: Not executed for this initial observation.
- check_id: lint
  name: Repository lint
  status: skipped
  required: true
  summary: Root pipeline halted at failed validate before just lint; no lint pass
    claimed.
  target_ids:
  - MetaCyc:PWY-6416
  scope_note: Not executed for this initial observation.
- check_id: diff
  name: Whitespace conflict check
  status: passed
  required: true
  summary: Reviewer ran git diff --check and observed exit0.
  target_ids:
  - MetaCyc:PWY-6416
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - record
- check_id: source-replay
  name: Independent source and chemical replay
  status: passed
  required: false
  summary: Raw42 reference bindings,8 molecular InChI identities and3 balanced Rhea
    families passed after reviewer-only RDF merge helper correction.
  target_ids:
  - MetaCyc:PWY-6416
  command: python -B /private/tmp/pathwaymech-next-257-adversarial/replay.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - raw
- check_id: identity-replay
  name: Independent protein/gene and construct replay
  status: passed
  required: false
  summary: 22 protein/gene identities plus QsuD exact construct and QsuB CDS/primer
    boundaries verified.
  target_ids:
  - MetaCyc:PWY-6416
  command: python -B /private/tmp/pathwaymech-next-257-adversarial/identities.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - identities
- check_id: imodulondb
  name: Live structured source cross-check
  status: passed
  required: false
  summary: Catalog and2 species-level searches succeeded; gene hits are context only
    and no component hit required summarize.
  target_ids:
  - MetaCyc:PWY-6416
  command: kg-microbe-sources imodulondb datasets; kg-microbe-sources imodulondb search
    --organism c_glutamicum --dataset modulome263 --query qsu; kg-microbe-sources
    imodulondb search --organism c_glutamicum --dataset modulome263 --query quinate
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - imodulon
evidence:
- evidence_id: record
  kind: record_content
  reference: data/pathways/quinate-degradation-ii.yaml
  locator: Entire YAML; 60 edges,41 participants,4 reactions,42 references
  accessed_at: '2026-10-14T19:15:57Z'
  support: supports
  summary: Entire maintained target read, including every edge, qualifier, reference
    and the distinction between three formal steps and one NAD-specific realization.
  snapshot_sha256: c160a52490eafd406d7d4427c0a352cf05ef0a70fec2c01aaab164b3a2ceca09
- evidence_id: raw
  kind: database
  reference: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/raw-source-replay.json
  locator: reference_bindings; native_pathway; native_reactions; chemical_identities;
    rhea_sides
  accessed_at: '2026-10-14T19:15:57Z'
  support: supports
  summary: Independently parsed raw MetaCyc XML and complete Rhea RDF:42 reference
    hashes bind originals;8 exact native/ChEBI InChIs agree;3 Rhea families have complete
    balanced sides. Native formal first reaction contains NAD(P), not exact NAD.
  snapshot_sha256: 438f1291142acb0401771fa9846a781a4501af7311217a16e19230fea7a6dee2
- evidence_id: identities
  kind: authority
  reference: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/independent-identities.json
  locator: 22 selected gene/protein identities; QsuD_construct; QsuB_source_gene
  accessed_at: '2026-10-14T19:15:57Z'
  support: supports
  summary: All selected UniProt/NCBIProtein/Entrez entries match exact accession and
    gene identity. QsuD structural sequence equals19-residue His6-containing prefix
    plus Q9X5C9. Independent QsuB CDS translation and P3/P4/P5 joins support source
    gene and terminal tag boundaries.
  snapshot_sha256: ca3cb473b6728d0ab01ca669b710281588aea354fcd2dfdce0823a21cb0717fe
- evidence_id: qutb
  kind: primary_source
  reference: PMID:8257437
  locator: PMC1137716 scans pp455–456; Table2
  accessed_at: '2026-10-14T19:15:57Z'
  support: partial
  summary: Visually inspected Methods/Results and Table2. Assay table names NAD+;
    fusion preparation is described as N-terminal metal-chelating domain, while Table2
    calls it GST. The draft preserves the fusion conflict but attaches catalysis to
    the broader NAD(P) reaction.
  snapshot_sha256: a72af294ca6a53d2a692d4baacc38a4efee00bb1d757c654398cca4cc599c191
- evidence_id: qsub
  kind: primary_source
  reference: PMID:32822353
  locator: Complete inspected QsuB-2020 XML methods/results; supplement S1Table internally
    labelled S2Table; Fig7
  accessed_at: '2026-10-14T19:15:57Z'
  support: partial
  summary: ATCC13869/2256 PCR source, tagged constructs, DHS→PCA assay, alternative
    Co/Mg/Mn tests and PCA inhibition are supported. No full deposited assay-clone
    sequence was inspected. Caption assigns full-length QsuB to panelB, contrary to
    edge042 locatorA; Methods/caption concentration disagreement is preserved.
  snapshot_sha256: e849838f31ba41586ccc3306f06f5041a5a01a5450e081c6a13a075e28ad9487
- evidence_id: qsud
  kind: database
  reference: MetaCyc:CPLX-7981
  locator: /ptools-xml/Protein[@frameid="CPLX-7981"]/comment
  accessed_at: '2026-10-14T19:15:57Z'
  support: partial
  summary: Native comment reports strong NAD preference and more than300-fold NADP
    turnover decrease. Edge030 currently cites only ENZRXN17380 and RXN20483, which
    do not contain that comparison. Its qualifier correctly separates associated structural
    sample and unknown cleavage across kinetics.
  snapshot_sha256: 49d3e4c3a8e369c04126358d5f7e486da873b1282c6aab080435cb41f407aadd
- evidence_id: regulation
  kind: primary_source
  reference: PMID:19376919; PMID:24674055; PMID:2943985
  locator: PMC2687277 Results/Fig5; publisher2014 web transcript Results202–288 and
    Methods; scanned1986 pp3596,3598
  accessed_at: '2026-10-14T19:15:57Z'
  support: supports
  summary: Inspected gene-level mutant/complementation effects, chorismate-dependent
    QsuR promoter-footprint data and historical Qa1F/Qa1S transcript genetics. Draft
    retains strain, experimental-construct and functional-versus-physical-binding
    distinctions.
- evidence_id: qa2
  kind: primary_source
  reference: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/qa2-primary-assessments.json
  locator: PMID126226 and143663 independently fetched primary abstracts; exact original
    hashes in artifact
  accessed_at: '2026-10-14T19:15:57Z'
  support: supports
  summary: Native-host74-A purification and separate recombinant expression support
    the bounded curated Qa2 catalytic annotation. The draft correctly excludes UniProt
    Qa2 kinetic values misattributed from QutB Table2; it does not claim historical/reference-strain
    whole-sequence equality.
  snapshot_sha256: 8c2de6025dcd44a9d48210dfc133ef22357e01bde2ddadc291b71603acc5c4cc
- evidence_id: edge-ledger
  kind: record_content
  reference: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/edge-assessments.json
  locator: All60 entries
  accessed_at: '2026-10-14T19:15:57Z'
  support: supports
  summary: Every maintained edge assessed against raw source or inspected primary
    statement; retains curated inference, construct, direction, cofactor alternatives
    and bounded transport/regulation scope.
  snapshot_sha256: 5be127a385bf532367f87fdf566aeed75a2cb546ffea4221282003e598549cb3
- evidence_id: imodulon
  kind: database
  reference: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/reviewer-check-history.json
  locator: Live public catalog and c_glutamicum/modulome263 qsu/quinate searches
  accessed_at: '2026-10-14T19:15:57Z'
  support: supports
  summary: Species-level dataset is applicable. Searches return4 distinct gene annotations
    but zero iModulon components. These are expression-dataset annotation leads, not
    evidence of R/ATCC13869 protein identity or direct catalysis. No component summarization
    applicable.
  snapshot_sha256: c382f3ffdadcfd5c59fcb415d0f1954662d27bca1f4dc65826d5da8d25dc7d78
- evidence_id: gates
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-257/quinate-ii/independent-scientific/initial/receipts.json
  locator: just render-pages exit0; just validate exit1; exact 1240 core-input recheck
    artifact
  accessed_at: '2026-10-14T19:15:57Z'
  support: refutes
  summary: Root ran full-corpus validation on exact inspected record. It failed4 MetaCyc
    participant label mismatches; test/lint pipeline did not run. Independent gate-input
    hash replay verified every bound path unchanged. This is a failed technical gate,
    not biological approval.
  snapshot_sha256: 082a7c395ae65570ee34b81c79c1ee730c59e79aeddec88c9765abad0f804dc1
assessments:
- assessment_id: identity
  area: identity
  topic: Exact pathway and reaction boundary
  outcome: supported
  summary: Native PWY6416 denotes the NAD(P)-linked quinate→DHQ→DHS→PCA route; PQQ
    quinateI and two-step shikimate routes remain distinct. NAD-specific realization
    is explicitly not a fourth sequential step.
  target_ids:
  - MetaCyc:PWY-6416
  evidence_ids:
  - record
  - raw
- assessment_id: chemistry
  area: grounding
  topic: Molecular sides, stereochemistry, charge and direction
  outcome: supported
  summary: Eight native molecules exactly match pinned ChEBI InChIs. Complete Rhea
    sides balance atoms and charge; native reversible DHQ dehydration and selected
    catabolic traversal remain distinct.
  target_ids:
  - MetaCyc:PWY-6416
  evidence_ids:
  - raw
- assessment_id: proteins
  area: scope
  topic: Strain, assembly and construct grounding
  outcome: concern
  summary: Exact source identities and major construct limitations are retained. QutB
    catalytic endpoint overstates NAD(P) scope; QsuB deposition wording exceeds the
    inspected evidence.
  target_ids:
  - MetaCyc:PWY-6416
  evidence_ids:
  - identities
  - qutb
  - qsub
  - qa2
  dimensions:
  - name: evidence_tier
    value: Mixed structured curated assertions, direct assays, genetic phenotypes,
      homology/rule inference
    definition: Each edge retains its nearest source tier; computational annotations
      are not newly inspected experiments.
    evidence_ids:
    - edge-ledger
  - name: strain_scope
    value: C.glutamicum R, ATCC13032 and ATCC13869 are distinct; fungi use explicitly
      scoped historical/issuing contexts
    definition: No silent transfer of purified enzyme experiments between strain-specific
      proteins.
    evidence_ids:
    - identities
    - regulation
    - qsub
- assessment_id: regulation
  area: evidence
  topic: Gene control, ligand and transport assertions
  outcome: supported
  summary: Gene-level QsuR and Qa regulator effects, qualified chorismate response
    and pH-dependent permease hypotheses have appropriately bounded support. Direct
    protein binding and broad physiological generalizations are not introduced.
  target_ids:
  - MetaCyc:PWY-6416
  evidence_ids:
  - regulation
  - edge-ledger
  - imodulon
- assessment_id: coverage
  area: completeness
  topic: Selected native and literature coverage
  outcome: supported
  summary: All60 maintained edges and42 references reviewed. Formal reaction sides/order/taxa
    and relevant bacterial/fungal examples are represented; alternate PQQ enzymes,
    unrelated biosynthetic/petrobactin activities and unresolved source-metal spelling
    are legitimate exclusions. This is not exhaustive literature coverage.
  target_ids:
  - MetaCyc:PWY-6416
  evidence_ids:
  - raw
  - edge-ledger
- assessment_id: provenance
  area: provenance
  topic: Edge-local source attribution
  outcome: concern
  summary: QsuB panel locator and missing nearest QsuD NADP-specificity evidence need
    bounded corrections. All42 source digests otherwise identify retained original
    artifacts.
  target_ids:
  - MetaCyc:PWY-6416
  evidence_ids:
  - qsub
  - qsud
  - raw
- assessment_id: schema
  area: schema
  topic: Full-corpus required gates
  outcome: concern
  summary: Initial validate failed4 participant-label mismatches; this separately
    tracked integration defect blocks completion. Tests/lint were skipped when the
    pipeline halted.
  target_ids:
  - MetaCyc:PWY-6416
  evidence_ids:
  - gates
findings:
- finding_id: F1
  issue_key: quinate-ii-qutb-nad-assay-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: QutB assay is attached to a broader NAD(P) activity
  description: Edge031 targets the broad native NAD(P) reaction although the inspected
    recombinant QutB table establishes NAD+ usage. Its description delegates coenzyme
    conditions to Table2 without retaining the actual NAD limitation. The exact NAD-specific
    reaction already exists locally; preserve the formal broad pathway member and
    native annotation context while targeting the measured chemistry.
  target_ids:
  - MetaCyc:PWY-6416
  field_paths:
  - mechanistic_edges[id=quinate-ii-031]
  evidence_ids:
  - record
  - qutb
  - raw
  rule_id: 'docs/CAUSAL_GRAPHS.md: preserve source cofactor scope'
  native_severity: major
  normalization_reason: 'Local review severity retained: unsupported scope in a mechanistic
    catalytic claim.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/quinate-degradation-ii.yaml
    role: maintained pathway record
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/545
- finding_id: F2
  issue_key: quinate-ii-qsub-deposition-absence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: QsuB qualifier overstates deposition absence
  description: All five QsuB qualifiers state that the complete internal assay-clone
    sequence was not independently deposited. The identity work establishes that no
    separately deposited complete assay-clone sequence was inspected; it does not
    establish global non-deposition. Retain this access limit rather than an unsupported
    absence claim.
  target_ids:
  - MetaCyc:PWY-6416
  field_paths:
  - mechanistic_edges[id=quinate-ii-038].endpoint_qualifiers
  - mechanistic_edges[id=quinate-ii-039].endpoint_qualifiers
  - mechanistic_edges[id=quinate-ii-040].endpoint_qualifiers
  - mechanistic_edges[id=quinate-ii-041].endpoint_qualifiers
  - mechanistic_edges[id=quinate-ii-042].endpoint_qualifiers
  evidence_ids:
  - record
  - qsub
  - identities
  rule_id: 'review-yaml-record: preserve uncertainty and evidence scope'
  native_severity: minor
  normalization_reason: 'Local review severity retained: bounded attribution or uncertainty
    wording defect with underlying biology supported.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/quinate-degradation-ii.yaml
    role: maintained pathway record
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/546
- finding_id: F3
  issue_key: quinate-ii-qsub-inhibition-panel
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Full-length QsuB inhibition cites the truncated-protein panel
  description: Edge042 evidence locator says Fig7A, but the article caption assigns
    full-length QsuB to Fig7B and N-QsuB to Fig7A. Correct the locator or cite the
    figure plus caption without the conflicting panel letter; retain the already acknowledged
    concentration discrepancy.
  target_ids:
  - MetaCyc:PWY-6416
  field_paths:
  - mechanistic_edges[id=quinate-ii-042].evidence[0].source_locator
  evidence_ids:
  - record
  - qsub
  rule_id: 'review-yaml-record: precise inspected source locator'
  native_severity: minor
  normalization_reason: 'Local review severity retained: bounded attribution or uncertainty
    wording defect with underlying biology supported.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/quinate-degradation-ii.yaml
    role: maintained pathway record
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/546
- finding_id: F4
  issue_key: quinate-ii-qsud-nadp-specificity-evidence
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: QsuD NADP comparison lacks its nearest source assertion
  description: Edge030 says NADP turnover is much lower but not absent. The retained
    native complex comment supports that statement; the two evidence objects on the
    edge do not. Add exact CPLX7981/comment evidence or remove the unsupported edge-local
    comparison. This lead was first raised by the author and independently verified
    by this reviewer.
  target_ids:
  - MetaCyc:PWY-6416
  field_paths:
  - mechanistic_edges[id=quinate-ii-030].evidence
  - mechanistic_edges[id=quinate-ii-030].description
  evidence_ids:
  - record
  - qsud
  rule_id: 'docs/CAUSAL_GRAPHS.md: evidence attached to narrowest supported edge'
  native_severity: minor
  normalization_reason: 'Local review severity retained: bounded attribution or uncertainty
    wording defect with underlying biology supported.'
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/quinate-degradation-ii.yaml
    role: maintained pathway record
  external_issues:
  - https://github.com/CultureBotAI/PathwayMech/issues/545
actions:
- action_id: A1
  description: Retarget qualified QutB catalysis to RHEA22365 and state NAD+ assay
    scope while retaining native broad annotation as context.
  finding_ids:
  - F1
  target_ids:
  - MetaCyc:PWY-6416
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/quinate-degradation-ii.yaml
    role: maintained pathway record
  acceptance_checks:
  - Re-read primaryTable2 NAD+ and native ENZRXN17384.
  - Confirm QutB catalytic edge targets exact RHEA22365 and retains fusion-conflict
    qualifier.
  - Broad native formal pathway member and all reaction sides remain.
  - Regenerate pathway pages and pass required full-corpus gates.
  generator: just render-pages
- action_id: A2
  description: Replace non-deposition claim with inspected-access limitation on all5
    QsuB qualifiers.
  finding_ids:
  - F2
  target_ids:
  - MetaCyc:PWY-6416
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/quinate-degradation-ii.yaml
    role: maintained pathway record
  acceptance_checks:
  - All5 affected qualifiers say no separately deposited complete assay-clone sequence
    was inspected.
  - No universal non-deposition assertion remains in target; source-gene/primer evidence
    remains unchanged.
  - Regenerate pathway pages and pass required full-corpus gates.
  generator: just render-pages
- action_id: A3
  description: Correct the QsuB inhibition source locator.
  finding_ids:
  - F3
  target_ids:
  - MetaCyc:PWY-6416
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/quinate-degradation-ii.yaml
    role: maintained pathway record
  acceptance_checks:
  - Full-length inhibition locator agrees with caption or refers to Figure7 without
    wrong panel.
  - Concentration discrepancy and construct-specific inhibition interpretation remain
    explicit.
  - Regenerate pathway pages and pass required full-corpus gates.
  generator: just render-pages
- action_id: A4
  description: Attach the native QsuD coenzyme-specificity comment to edge030.
  finding_ids:
  - F4
  target_ids:
  - MetaCyc:PWY-6416
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/quinate-degradation-ii.yaml
    role: maintained pathway record
  acceptance_checks:
  - New structured evidence resolves exact CPLX7981/comment and faithfully states
    NADP turnover reduction.
  - ATCC13032 construct versus strainR genetic scope stays distinct.
  - Regenerate pathway pages and pass required full-corpus gates.
  generator: just render-pages
limitations:
- Required validate failed; required tests and lint were skipped after pipeline halt.
  No merge approval or completed technical pass.
- Several primary sources were available only as abstracts or selected scanned pages;
  the2014 QsuR full text was inspected through a retained publisher web transcript.
  No unavailable full-text methods are claimed inspected.
- No separately deposited complete QsuB assay-clone sequence was inspected. Primer/CDS
  joins establish source gene and construct boundaries without proving every internal
  assayed residue.
- Complete native source inventories were inspected as scoped author ledgers and raw
  targeted source objects; this review does not claim exhaustive biological characterization
  of all taxa or every cited background paper.
- iModulonDB gene annotation hits are context only. No direct catalysis or strain
  equivalence follows from expression-dataset presence.
notes:
- Raw complete source originals remain external; compact independent evidence and
  exact digests are retained in the repository.
- No maintained curation, authority files, history or pages were edited by this reviewer.
- Issue545 tracks F1/F4; issue546 tracks F2/F3.
tags:
- next257
- quinate
- independent-scientific
- initial-review
```

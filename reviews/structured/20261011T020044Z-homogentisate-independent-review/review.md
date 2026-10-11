# Independent scientific review of homogentisate catabolic process

- Review: 20261011T020044Z-homogentisate-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T01:49:00.156874Z
- Finished UTC: 2026-10-11T02:00:44Z
- Reviewer: Codex /root/pathway_authority_cache (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact three-reaction Pseudomonas putida strain U homogentisate pathway is supported with explicit genetic/annotation limits. All 24 edges and 38 evidence blocks were reviewed; no confirmed finding remains. All final required repository gates pass; their actual receipts were inspected separately from the scientific assessment.

## Scope And Provenance

Full single-record scientific review: 24 edges and 38 evidence blocks.

Selection: Explicit parent assignment after a separate author froze the target; source bytes captured using governed inspect before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6a331b8b9fd7bf4d9f7b6d2f6626b29157b47a69.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1902000 | data/pathways/homogentisate-degradation.yaml | maintained | homogentisate catabolic process |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Governed initial input inspection | passed | True | GO:1902000 | Initial canonical inspect captured the exact target before assessment; primary and whole-record review followed. |
| Independent full source and target export replay | passed | True | GO:1902000 | {'edges': 24, 'evidence': 38, 'reaction_sides': 11, 'protein_translations': 3, 'source_bodies_rehashed': 32, 'kgx_nodes': 20}. Every source body and reference digest matched; source chemistry and exact evidence were independently checked. |
| Independent unchanged structured source adapter replay | passed | False | GO:1902000 | All 11 searches, datasets and component78 reproduced from 13 rehashed retained bodies. Offline replay of prior retrieved bodies, not fresh network. |
| just render-pages | passed | True | GO:1902000 | Delegated to root; actual terminal exit0 and retained log bytes independently inspected. pass |
| just lint | passed | True | GO:1902000 | Delegated to root; actual terminal exit0 and retained log bytes independently inspected. pass |
| just check-identifiers | passed | True | GO:1902000 | Delegated to root; actual terminal exit0 and retained log bytes independently inspected. pass |
| git diff --check | passed | True | GO:1902000 | Delegated to root; actual terminal exit0 and retained log bytes independently inspected. pass |
| just kgx-export --output-dir /private/tmp/pathwaymech-next-pathways-kgx | passed | True | GO:1902000 | Delegated to root; actual terminal exit0 and retained log bytes independently inspected. pass |
| just validate | passed | True | GO:1902000 | Delegated to root; actual terminal exit0 and retained log bytes independently inspected. pass |
| just test | passed | True | GO:1902000 | Delegated to root; actual terminal exit0 and retained log bytes independently inspected. 1,048 passed, 3 skipped, 3 upstream deprecation warnings in 234.69s. |
| UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just vendored-check | passed | True | GO:1902000 | Delegated to root; actual terminal exit0 and retained log bytes independently inspected. All governed artifacts match pinned canonical revision; terminal success observed. |
| Superseded vendored network attempt | failed | False | GO:1902000 | Root receipt retains a restricted-network DNS failure before the same unchanged command succeeded with network access. This initial result is not treated as the final gate. This is a delegated historical observation; the initial numeric exit code was not supplied and is not fabricated. |
| Final governed input capture and changed-input reassessment | passed | True | GO:1902000 | Initial captured inputs are unchanged; newly final shared inputs and generated page inspected. Every final source.input digest rechecked. |
| Superseded draft format validation | failed | False | GO:1902000 | External draft used +00:00 instead of required Z timestamp spelling and inspection target kind record instead of maintained. Corrected serialization only; source hashes, assessment and timestamps remain the same instants. |

## Scientific And Domain Assessments

### Exact three-step pathway boundary

identity: supported. Targets: GO:1902000.

GO:1902000 identifies the complete homogentisate-to-fumarate/acetoacetate route, unlike the broader five-reaction MetaCyc tyrosine pathway. The primary boxed route and current process identity agree.

### hmg-edge-001 through 011

grounding: supported. Targets: GO:1902000.

Eleven exact side/participant/coefficient source triples; three balanced equations, with dioxygen and water inputs and two net hydrons; no duplicate net reaction.

### hmg-edge-012 through 014

graph: supported. Targets: GO:1902000.

Three deposited U translations match UniProt exactly; primary figure and strain U genetic evidence support qualified enables. HmgB/C assignments rely on genetics plus sequence interpretation; no claim of purified strain U enzyme or sufficient monomer.

### hmg-edge-015 through 019

identity: supported. Targets: GO:1902000.

Exact GO process and primary boxed three-step boundary; order HmgA to HmgC to HmgB, separately confirmed by exact shared chemical intermediates. Broader five-step MetaCyc pathway is not substituted.

### hmg-edge-020 through 022

evidence: supported. Targets: GO:1902000.

Exact current cofactor annotations: HmgA broad iron cation via HAMAP ECO:0000255; HmgB Ca/Mg via ARBA/PIRSR ECO:0000256. Qualified as inferred/automatic, with no occupancy or simultaneous-requirement claim.

### hmg-edge-023 through 024

scope: supported. Targets: GO:1902000.

Exact GO:0005737 positions and IEA:TreeGrafter/IEA:InterPro retained; no direct localization/exclusive residence claim.

### Strain U genetics versus KT2440 assays

scope: supported. Targets: GO:1902000.

Native AY168855.1 is strain U; all three deposited translations match target UniProt entries exactly. Strain U genetic disruption/complementation supports the cluster, while exact HmgB/C activities remain genetics plus homology. KT2440 extract activity and FeSO4 conditions are not transferred to U.

### Bounded structured-source context

evidence: supported. Targets: GO:1902000.

Root resolved the canonical client after console-runner dependency failure. Reviewer independently reproduced the retained results offline. Computational expression association supports context only; dataset or hit absence is not biological absence.

### Final validation and generated artifacts

schema: supported. Targets: GO:1902000.

Final complete repository checks, target identity gate and structural SVG/KGX audit pass on unchanged final target hashes. No deterministic validation is substituted for the scientific source assessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/pathways/homogentisate-degradation.yaml; Entire maintained YAML; all local nodes, edges, evidence and references | supports | The exact three-reaction Pseudomonas putida strain U homogentisate pathway is supported with explicit genetic/annotation limits. All 24 edges and 38 evidence blocks were reviewed; no confirmed finding remains. |
| independent-audit | research/pathway_additions/2026-10-11-next-pathways/homogentisate-independent-review-audit.json; Full independent technical replay and per-edge scientific assessments | supports | Independent source rehashes, raw RDF side/coefficient replay, native identity/assembly checks and actual target KGX passed. These deterministic checks are supplemented by the primary/native scientific assessments recorded here. |
| rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Exact selected master/directional/bidirectional, side containsN, participant and compound triples | supports | All eleven chemical sides and three balances independently verified. |
| identity-search | Independent local exact and semantic search; Hidden/ignored-inclusive accessible worktree; native boundary and prior candidate dispositions | supports | The exact native pathway is distinct from other maintained routes; candidate and authority mentions do not establish an existing full record. |
| source-1 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1902000; /results/0/id; /results/0/name; /results/0/definition/text; /results/0/isObsolete; /results/0/aspect | supports | Gene Ontology homogentisate catabolic process. Inspected exact source assertions for hmg-edge-015, hmg-edge-016, hmg-edge-017. Source access/version scope: QuickGO response retrieved 2026-10-11. |
| source-2 | https://europepmc.org/articles/PMC451635?pdf=render; Arias-Barrau et al. (2004), Fig. 1B (p. 5063); Results and Discussion, Identification of the genes involved in the central pathway (pp. 5067-5069); Fig. 5.; Arias-Barrau et al. (2004), Fig. 1B (p. 5063), boxed central pathway.; Arias-Barrau et al. (2004), Fig. 1B (p. 5063). | supports | The homogentisate pathway: a central catabolic pathway involved in the degradation of L-phenylalanine, L-tyrosine, and 3-hydroxyphenylacetate in Pseudomonas putida.. Inspected exact source assertions for hmg-edge-012, hmg-edge-013, hmg-edge-014, hmg-edge-015, hmg-edge-016, hmg-edge-017, hmg-edge-018, hmg-edge-019. Source access/version scope: Journal of Bacteriology 186:5062-5077 (2004); complete 16-page primary PDF, relevant figure, methods and results inspected. |
| source-3 | https://rest.uniprot.org/uniprotkb/search?query=AY168855&amp;format=json&amp;size=500; /results/0/genes/0/geneName; /results/0/uniProtKBCrossReferences[database=EMBL,id=AY168855]; /results/0/references/0/referenceComments[type=STRAIN]; /results/0/comments/1/reaction; /results/0/comments/4; /results/0/comments/2/cofactors/0; /results/0/comments/2/cofactors/0/evidences; /results/0/uniProtKBCrossReferences/6 | supports | UniProtKB reviewed (Swiss-Prot) Q6EMI9: native sequence, function and annotation evidence. Inspected exact source assertions for hmg-edge-012, hmg-edge-020, hmg-edge-023. Source access/version scope: Native four-entry AY168855 response; Q6EMI9 entry version 76, sequence version 1, annotation updated 2026-01-28. |
| source-4 | https://rest.uniprot.org/uniprotkb/search?query=AY168855&amp;format=json&amp;size=500; /results/2/genes/0/geneName; /results/2/uniProtKBCrossReferences[database=EMBL,id=AY168855]; /results/2/references/0/referenceComments[type=STRAIN]; /results/2/uniProtKBCrossReferences/4 | supports | UniProtKB unreviewed (TrEMBL) Q6EMI7: native sequence, function and annotation evidence. Inspected exact source assertions for hmg-edge-013, hmg-edge-024. Source access/version scope: Native four-entry AY168855 response; Q6EMI7 entry version 79, sequence version 1, annotation updated 2026-09-02. |
| source-5 | https://rest.uniprot.org/uniprotkb/search?query=AY168855&amp;format=json&amp;size=500; /results/1/genes/0/geneName; /results/1/uniProtKBCrossReferences[database=EMBL,id=AY168855]; /results/1/references/0/referenceComments[type=STRAIN]; /results/1/comments/0/cofactors/0; /results/1/comments/0/cofactors/0/evidences; /results/1/comments/1/cofactors/0; /results/1/comments/1/cofactors/0/evidences | supports | UniProtKB unreviewed (TrEMBL) Q6EMI8: native sequence, function and annotation evidence. Inspected exact source assertions for hmg-edge-014, hmg-edge-021, hmg-edge-022. Source access/version scope: Native four-entry AY168855 response; Q6EMI8 entry version 72, sequence version 1, annotation updated 2026-09-02. |
| source-6 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15450']/rh:substrates; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15449_L']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_15449_compound_5206']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_15449_compound_5206']/rh:compound; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_5206']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15450']/rh:substrates; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15449_L']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_15449_compound_1198']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_15449_compound_1198']/rh:compound; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_1198']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15450']/rh:products; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15449_R']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_15449_compound_5213']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_15449_compound_5213']/rh:compound; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_5213']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15450']/rh:products; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15449_R']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_15449_compound_3249']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_15449_compound_3249']/rh:compound; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_3249']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15449']/rh:directionalReaction[@rdf:resource='http://rdf.rhea-db.org/15450']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15450']/rh:equation; rh:substrates; rh:products; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15450']/rh:products; rh:contains1/rh:compound/rh:chebi | supports | Rhea directed reaction 15450. Inspected exact source assertions for hmg-edge-001, hmg-edge-002, hmg-edge-003, hmg-edge-004, hmg-edge-012, hmg-edge-018. Source access/version scope: Rhea release 142; complete RDF, exact native triples projected in author dossier. |
| source-7 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; rdf:Description[@rdf:about='http://rdf.rhea-db.org/14818']/rh:substrates; rdf:Description[@rdf:about='http://rdf.rhea-db.org/14817_L']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_14817_compound_5213']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_14817_compound_5213']/rh:compound; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_5213']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/14818']/rh:products; rdf:Description[@rdf:about='http://rdf.rhea-db.org/14817_R']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_14817_compound_4618']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_14817_compound_4618']/rh:compound; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_4618']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/14817']/rh:directionalReaction[@rdf:resource='http://rdf.rhea-db.org/14818']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/14818']/rh:equation; rh:substrates; rh:products; rdf:Description[@rdf:about='http://rdf.rhea-db.org/14818']/rh:substrates; rh:contains1/rh:compound/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/14818']/rh:products; rh:contains1/rh:compound/rh:chebi | supports | Rhea directed reaction 14818. Inspected exact source assertions for hmg-edge-005, hmg-edge-006, hmg-edge-013, hmg-edge-018, hmg-edge-019. Source access/version scope: Rhea release 142; complete RDF, exact native triples projected in author dossier. |
| source-8 | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:substrates; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10244_L']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_10244_compound_4618']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_10244_compound_4618']/rh:compound; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_4618']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:substrates; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10244_L']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_10244_compound_1283']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_10244_compound_1283']/rh:compound; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_1283']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:products; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10244_R']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_10244_compound_3307']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_10244_compound_3307']/rh:compound; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_3307']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:products; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10244_R']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_10244_compound_3031']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_10244_compound_3031']/rh:compound; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_3031']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:products; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10244_R']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_10244_compound_3249']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_10244_compound_3249']/rh:compound; rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_3249']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10244']/rh:directionalReaction[@rdf:resource='http://rdf.rhea-db.org/10245']; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:equation; rh:substrates; rh:products; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:substrates; rh:contains1/rh:compound/rh:chebi | supports | Rhea directed reaction 10245. Inspected exact source assertions for hmg-edge-007, hmg-edge-008, hmg-edge-009, hmg-edge-010, hmg-edge-011, hmg-edge-014, hmg-edge-019. Source access/version scope: Rhea release 142; complete RDF, exact native triples projected in author dossier. |
| expression-context | research/pathway_additions/2026-10-11-next-pathways/imodulondb-homogentisate-context.json; p_putida/precise321/78 | context_only | KT2440 HmgR component contains PP_4621/Q88E47 and PP_4619/Q88E49; it does not establish strain U catalysis or regulation. |
| final-gates | research/pathway_additions/2026-10-11-next-pathways/integration-validation.json; Final terminal exit codes and preserved log digests | supports | Inspected actual final gate receipts and rehashed retained logs. Full corpus checks pass; no in-flight or earlier failure is reported as terminal success. |
| generated-audit | research/pathway_additions/2026-10-11-next-pathways/generated-graph-kgx-audit.json; This target SVG/KGX exact graph, evidence and reference preservation | supports | Separate actual CLI export and generated downloads match. Exact edge endpoints, complete evidence, source contexts and SVG anchors pass; this is structural artifact verification, not browser visual inspection. |
| authority-final | research/pathway_additions/2026-10-11-next-pathways/authority-integration.json; Pinned ontology/source additions, baseline preservation and exact native new identities | supports | Canonical snapshots resolve final target IDs, retaining all prior authority entries and source metadata. |

## Limits And Additional Notes

- Primary genetic complementation establishes the cluster; HmgB/C exact activities are not individually purified strain U assays.
- Strain U HmgA hexamer/iron and HmgB cofactors retain computational evidence levels; no imported human complex or strain-specific glutathione assertion.
- Species identifier NCBITaxon:303 is explicitly narrowed to strain U in prose and native sequence evidence.
- Comparative iModulonDB KT2440 module 78 cannot establish U biochemical or regulatory edges.
- Older primary sources inspected only as abstracts are explicitly labeled; current database assertions are not relabeled as new direct experiments.
- Original Documents checkout is OS-inaccessible; hidden/ignored searches cover the accessible worktree.
- No browser interaction or new experiments; final generated publication checks are programmatic and delegated to root.
- Primary PMC451635-europe-render.html is the actual 16-page PDF despite its extension; %PDF signature and exact body hash verified. The similarly named PMC451635.pdf challenge body was rejected. Independent PDFium text extraction and relevant page images were inspected after pdftotext was unavailable.
- A second external draft validation rejected the historical initial vendored observation because it named an executed command without a retained numeric exit code. Its command field was removed; the failed attempt remains an honest delegated observation. Final repeated vendored command has observed exit0.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T020044Z-homogentisate-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of homogentisate catabolic process
started_at: '2026-10-11T01:49:00.156874Z'
finished_at: '2026-10-11T02:00:44Z'
reviewer:
  identity: Codex /root/pathway_authority_cache
  kind: agent
  model: gpt-6
  independence: independent
  independence_basis: Did not author or edit this target or its mechanistic dossier.
    Authored the separate pseudouridine record in this cohort. Root owns shared authority
    integration and full repository gates. Independently inspected primary/native
    source bodies, scientific evidence grades and every edge; earlier shared authority-tool
    authorship does not substitute for raw source checks.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact three-reaction Pseudomonas putida strain U homogentisate pathway
  is supported with explicit genetic/annotation limits. All 24 edges and 38 evidence
  blocks were reviewed; no confirmed finding remains. All final required repository
  gates pass; their actual receipts were inspected separately from the scientific
  assessment.
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
  - path: conf/identifier_policy.yaml
    sha256: 3e19ecbbe980e44198405ae0cf37b5fd17ae4c88c05dbf36fab482b2ddd38bd1
    role: context
  - path: conf/identifier_sources.json
    sha256: f10c5134fb3c06b60f0aac9d68f09219fd2d8cb385bb5030c32629d61c66b9a5
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 53301d6edd435f9fa3191ba317efbfabeb45a0843c2d88ade0e80c8244714049
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 7fe18e8cb41db75a16c9d4afdb45f4db1a86a1fef47cf609c25263d3b567e743
    role: context
  - path: data/pathways/homogentisate-degradation.yaml
    sha256: a833e707d3dbd92ff09194e1d19b7c419aa3e2c4c45d3a53064c8915a2d755d2
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
  - path: pages/records/GO_1902000.html
    sha256: 565166b329fabb831318a46a8c56ce2f40a57d04046d9ec75afd0584497e349a
    role: generated page; maintained owner data/pathways/homogentisate-degradation.yaml;
      renderer src/pathwaymech/cli.py and graph_view.py
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
  - path: research/pathway_additions/2026-10-11-next-pathways/homogentisate-curation.md
    sha256: d9b1a682692ccc51a39338501bda32eebaa935e08ded13c76012eff1a5604f78
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/homogentisate-dedup.json
    sha256: caf0fa62d5c4842250b5224735c0af3aa9201c0ef3e93882b35561eea977d053
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/homogentisate-identifiers.json
    sha256: a0acfb56c11c1b3026d7834689108ab5a375efc109a7548f8fc605995c8939d4
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/homogentisate-independent-review-audit.json
    sha256: bfbd7744e75ebb6f6726924ec3035be94f404c49b30d02b48de89ad9c998c2e1
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/homogentisate-replay.py
    sha256: 853bc3069d71dc49b0b03fea2493819229cd9816058903008da39effd96ec5e1
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/homogentisate-source-manifest.json
    sha256: 8feee95d561454e59edf4b754f38cb315bf0ef6fe1492b691abad116deb92151
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/homogentisate-source-projection.json
    sha256: 552af979550d6d784341785450428b5d68c3a50918dc21921c952637ea029258
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/homogentisate-validation.json
    sha256: c94db286d9cecedf3adf11fa8307d4b32f008e760430b9ed86b8d10dd3f2b995
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/imodulondb-homogentisate-context.json
    sha256: e7532650b14f9a2fcac90d801ad061e1cb926557ec50bc0ea154e6f91e021534
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/imodulondb-homogentisate-parser-replay.json
    sha256: b18a801dcfba88b49d84098f9f54322c4971378dd489bc91ee802b29702f9f9a
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/imodulondb-homogentisate-source-manifest.json
    sha256: fce9acf0cb1256d8f04e203fc0d72e1346d7913860a28f751d12630fef881332
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/imodulondb-runner-availability.json
    sha256: 9cf704bc4d5e2adfe144e745cce0c8fb0525ce3254e0be9d22078dcf0f608823
    role: context
  - path: research/pathway_additions/2026-10-11-next-pathways/integration-validation.json
    sha256: c54763a27294bf2d6ea829ac31aba1b87f59884d74a27d03df4aaa356c2149d5
    role: context
  - path: src/pathwaymech/schema.py
    sha256: 46882d1cfda27a29a8a1224088e8a623bc55bc3a8c1929a5e5c0f07a2c00587f
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: 679a6bbeb8054d0e3f3eccfbbc6a6605d04d936d5f63f85d35d9cea732a48797
    role: context
scope:
  description: 'Full single-record scientific review: 24 edges and 38 evidence blocks.'
  selection: Explicit parent assignment after a separate author froze the target;
    source bytes captured using governed inspect before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1902000
  exclusions:
  - target: Other cohort and baseline pathway records
    reason: Not independent scientific targets of this bundle; adjacent sources inspected
      only for identity and scope boundaries.
  - target: Experimental replication and browser interaction
    reason: No wet-lab or interactive browser work is claimed; source assessment and
      programmatic generated-artifact checks have separate receipts.
targets:
- target_id: GO:1902000
  path: data/pathways/homogentisate-degradation.yaml
  label: homogentisate catabolic process
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/homogentisate-degradation.yaml
    role: maintained record
checks:
- check_id: inspect-initial
  name: Governed initial input inspection
  status: passed
  required: true
  summary: Initial canonical inspect captured the exact target before assessment;
    primary and whole-record review followed.
  target_ids:
  - GO:1902000
  evidence_ids:
  - target
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-pathways-evidence/homogentisate-review/targets.yaml
    --input conf/identifier_policy.yaml --input docs/CAUSAL_GRAPHS.md --input src/pathwaymech/schema.py
    --input src/pathwaymech/schema/pathwaymech.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: independent-replay
  name: Independent full source and target export replay
  status: passed
  required: true
  summary: '{''edges'': 24, ''evidence'': 38, ''reaction_sides'': 11, ''protein_translations'':
    3, ''source_bodies_rehashed'': 32, ''kgx_nodes'': 20}. Every source body and reference
    digest matched; source chemistry and exact evidence were independently checked.'
  target_ids:
  - GO:1902000
  evidence_ids:
  - independent-audit
  - rhea
  command: .venv/bin/python /private/tmp/pathwaymech-next-pathways-evidence/homogentisate-review/independent-replay.py
  exit_code: 0
  expected_exit_code: 0
- check_id: context-replay
  name: Independent unchanged structured source adapter replay
  status: passed
  required: false
  summary: All 11 searches, datasets and component78 reproduced from 13 rehashed retained
    bodies. Offline replay of prior retrieved bodies, not fresh network.
  target_ids:
  - GO:1902000
  evidence_ids:
  - independent-audit
  - expression-context
  command: .venv/bin/python - (unchanged canonical ImodulonDBClient injected retained
    URL/body transport)
  exit_code: 0
  expected_exit_code: 0
- check_id: root-gate-1
  name: just render-pages
  status: passed
  required: true
  summary: Delegated to root; actual terminal exit0 and retained log bytes independently
    inspected. pass
  target_ids:
  - GO:1902000
  evidence_ids:
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    render-pages
  exit_code: 0
  expected_exit_code: 0
- check_id: root-gate-2
  name: just lint
  status: passed
  required: true
  summary: Delegated to root; actual terminal exit0 and retained log bytes independently
    inspected. pass
  target_ids:
  - GO:1902000
  evidence_ids:
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    lint
  exit_code: 0
  expected_exit_code: 0
- check_id: root-gate-3
  name: just check-identifiers
  status: passed
  required: true
  summary: Delegated to root; actual terminal exit0 and retained log bytes independently
    inspected. pass
  target_ids:
  - GO:1902000
  evidence_ids:
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    check-identifiers
  exit_code: 0
  expected_exit_code: 0
- check_id: root-gate-4
  name: git diff --check
  status: passed
  required: true
  summary: Delegated to root; actual terminal exit0 and retained log bytes independently
    inspected. pass
  target_ids:
  - GO:1902000
  evidence_ids:
  - final-gates
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
- check_id: root-gate-5
  name: just kgx-export --output-dir /private/tmp/pathwaymech-next-pathways-kgx
  status: passed
  required: true
  summary: Delegated to root; actual terminal exit0 and retained log bytes independently
    inspected. pass
  target_ids:
  - GO:1902000
  evidence_ids:
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    kgx-export --output-dir /private/tmp/pathwaymech-next-pathways-kgx
  exit_code: 0
  expected_exit_code: 0
- check_id: root-gate-6
  name: just validate
  status: passed
  required: true
  summary: Delegated to root; actual terminal exit0 and retained log bytes independently
    inspected. pass
  target_ids:
  - GO:1902000
  evidence_ids:
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    validate
  exit_code: 0
  expected_exit_code: 0
- check_id: root-gate-7
  name: just test
  status: passed
  required: true
  summary: Delegated to root; actual terminal exit0 and retained log bytes independently
    inspected. 1,048 passed, 3 skipped, 3 upstream deprecation warnings in 234.69s.
  target_ids:
  - GO:1902000
  evidence_ids:
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 just
    test
  exit_code: 0
  expected_exit_code: 0
- check_id: root-gate-8
  name: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  status: passed
  required: true
  summary: Delegated to root; actual terminal exit0 and retained log bytes independently
    inspected. All governed artifacts match pinned canonical revision; terminal success
    observed.
  target_ids:
  - GO:1902000
  evidence_ids:
  - final-gates
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache just
    vendored-check
  exit_code: 0
  expected_exit_code: 0
- check_id: initial-vendored-network
  name: Superseded vendored network attempt
  status: failed
  required: false
  summary: Root receipt retains a restricted-network DNS failure before the same unchanged
    command succeeded with network access. This initial result is not treated as the
    final gate. This is a delegated historical observation; the initial numeric exit
    code was not supplied and is not fabricated.
  target_ids:
  - GO:1902000
  evidence_ids:
  - final-gates
- check_id: inspect-final
  name: Final governed input capture and changed-input reassessment
  status: passed
  required: true
  summary: Initial captured inputs are unchanged; newly final shared inputs and generated
    page inspected. Every final source.input digest rechecked.
  target_ids:
  - GO:1902000
  evidence_ids:
  - target
  - independent-audit
  - final-gates
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-pathways-evidence/homogentisate-review/targets.yaml
    --input .claude/skills/add-pathway/SKILL.md --input .claude/skills/review-yaml-record/SKILL.md
    --input conf/identifier_policy.yaml --input conf/identifier_sources.json --input
    data/identifier_authorities/ontology.json --input data/identifier_authorities/sources.json
    --input docs/CAUSAL_GRAPHS.md --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/record-review-profile.md --input docs/record-reviews.md --input justfile
    --input pages/records/GO_1902000.html --input research/pathway_additions/2026-10-11-next-pathways/authority-integration.json
    --input research/pathway_additions/2026-10-11-next-pathways/authority-protein-crosscheck.json
    --input research/pathway_additions/2026-10-11-next-pathways/authority-source-inspection.json
    --input research/pathway_additions/2026-10-11-next-pathways/baseline-preservation.json
    --input research/pathway_additions/2026-10-11-next-pathways/browser-availability.json
    --input research/pathway_additions/2026-10-11-next-pathways/generated-graph-kgx-audit.json
    --input research/pathway_additions/2026-10-11-next-pathways/homogentisate-curation.md
    --input research/pathway_additions/2026-10-11-next-pathways/homogentisate-dedup.json
    --input research/pathway_additions/2026-10-11-next-pathways/homogentisate-identifiers.json
    --input research/pathway_additions/2026-10-11-next-pathways/homogentisate-independent-review-audit.json
    --input research/pathway_additions/2026-10-11-next-pathways/homogentisate-replay.py
    --input research/pathway_additions/2026-10-11-next-pathways/homogentisate-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-pathways/homogentisate-source-projection.json
    --input research/pathway_additions/2026-10-11-next-pathways/homogentisate-validation.json
    --input research/pathway_additions/2026-10-11-next-pathways/imodulondb-homogentisate-context.json
    --input research/pathway_additions/2026-10-11-next-pathways/imodulondb-homogentisate-parser-replay.json
    --input research/pathway_additions/2026-10-11-next-pathways/imodulondb-homogentisate-source-manifest.json
    --input research/pathway_additions/2026-10-11-next-pathways/imodulondb-runner-availability.json
    --input research/pathway_additions/2026-10-11-next-pathways/integration-validation.json
    --input src/pathwaymech/schema.py --input src/pathwaymech/schema/pathwaymech.yaml
  exit_code: 0
  expected_exit_code: 0
- check_id: draft-format-validation
  name: Superseded draft format validation
  status: failed
  required: false
  summary: External draft used +00:00 instead of required Z timestamp spelling and
    inspection target kind record instead of maintained. Corrected serialization only;
    source hashes, assessment and timestamps remain the same instants.
  target_ids:
  - GO:1902000
  command: UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache UV_NO_SYNC=1 uv
    run python scripts/record_review.py validate /private/tmp/pathwaymech-next-pathways-evidence/homogentisate-review/draft-review.yaml
  exit_code: 1
  expected_exit_code: 0
  evidence_ids: []
evidence:
- evidence_id: target
  kind: record_content
  reference: data/pathways/homogentisate-degradation.yaml
  locator: Entire maintained YAML; all local nodes, edges, evidence and references
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: The exact three-reaction Pseudomonas putida strain U homogentisate pathway
    is supported with explicit genetic/annotation limits. All 24 edges and 38 evidence
    blocks were reviewed; no confirmed finding remains.
  snapshot_sha256: a833e707d3dbd92ff09194e1d19b7c419aa3e2c4c45d3a53064c8915a2d755d2
- evidence_id: independent-audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-pathways/homogentisate-independent-review-audit.json
  locator: Full independent technical replay and per-edge scientific assessments
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: Independent source rehashes, raw RDF side/coefficient replay, native identity/assembly
    checks and actual target KGX passed. These deterministic checks are supplemented
    by the primary/native scientific assessments recorded here.
  snapshot_sha256: bfbd7744e75ebb6f6726924ec3035be94f404c49b30d02b48de89ad9c998c2e1
- evidence_id: rhea
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Exact selected master/directional/bidirectional, side containsN, participant
    and compound triples
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: All eleven chemical sides and three balances independently verified.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: identity-search
  kind: search
  reference: Independent local exact and semantic search
  locator: Hidden/ignored-inclusive accessible worktree; native boundary and prior
    candidate dispositions
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: The exact native pathway is distinct from other maintained routes; candidate
    and authority mentions do not establish an existing full record.
  search_scope: rg --no-ignore --hidden over accessible worktree including ignored
    files, excluding .git/.venv and current generated/batch outputs. Original Documents
    checkout remains OS-inaccessible; no whole-computer absence claim.
  snapshot_sha256: bfbd7744e75ebb6f6726924ec3035be94f404c49b30d02b48de89ad9c998c2e1
- evidence_id: source-1
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1902000
  locator: /results/0/id; /results/0/name; /results/0/definition/text; /results/0/isObsolete;
    /results/0/aspect
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: 'Gene Ontology homogentisate catabolic process. Inspected exact source
    assertions for hmg-edge-015, hmg-edge-016, hmg-edge-017. Source access/version
    scope: QuickGO response retrieved 2026-10-11.'
  snapshot_sha256: 468663419157fd6a6c8f8fc08b28314a3a4581c8cef5596873240f44fe5e7218
- evidence_id: source-2
  kind: primary_source
  reference: https://europepmc.org/articles/PMC451635?pdf=render
  locator: Arias-Barrau et al. (2004), Fig. 1B (p. 5063); Results and Discussion,
    Identification of the genes involved in the central pathway (pp. 5067-5069); Fig.
    5.; Arias-Barrau et al. (2004), Fig. 1B (p. 5063), boxed central pathway.; Arias-Barrau
    et al. (2004), Fig. 1B (p. 5063).
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: 'The homogentisate pathway: a central catabolic pathway involved in the
    degradation of L-phenylalanine, L-tyrosine, and 3-hydroxyphenylacetate in Pseudomonas
    putida.. Inspected exact source assertions for hmg-edge-012, hmg-edge-013, hmg-edge-014,
    hmg-edge-015, hmg-edge-016, hmg-edge-017, hmg-edge-018, hmg-edge-019. Source access/version
    scope: Journal of Bacteriology 186:5062-5077 (2004); complete 16-page primary
    PDF, relevant figure, methods and results inspected.'
  snapshot_sha256: 3376702d6a5532036127514c819a777ebe2ea8546f917306f05314250ccb2ac8
- evidence_id: source-3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=AY168855&format=json&size=500
  locator: /results/0/genes/0/geneName; /results/0/uniProtKBCrossReferences[database=EMBL,id=AY168855];
    /results/0/references/0/referenceComments[type=STRAIN]; /results/0/comments/1/reaction;
    /results/0/comments/4; /results/0/comments/2/cofactors/0; /results/0/comments/2/cofactors/0/evidences;
    /results/0/uniProtKBCrossReferences/6
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: 'UniProtKB reviewed (Swiss-Prot) Q6EMI9: native sequence, function and
    annotation evidence. Inspected exact source assertions for hmg-edge-012, hmg-edge-020,
    hmg-edge-023. Source access/version scope: Native four-entry AY168855 response;
    Q6EMI9 entry version 76, sequence version 1, annotation updated 2026-01-28.'
  snapshot_sha256: 47e1db788538e999e1b5b29f9ba0083b48995dd40531ed184e36ac5eb12bfaa9
- evidence_id: source-4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=AY168855&format=json&size=500
  locator: /results/2/genes/0/geneName; /results/2/uniProtKBCrossReferences[database=EMBL,id=AY168855];
    /results/2/references/0/referenceComments[type=STRAIN]; /results/2/uniProtKBCrossReferences/4
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: 'UniProtKB unreviewed (TrEMBL) Q6EMI7: native sequence, function and annotation
    evidence. Inspected exact source assertions for hmg-edge-013, hmg-edge-024. Source
    access/version scope: Native four-entry AY168855 response; Q6EMI7 entry version
    79, sequence version 1, annotation updated 2026-09-02.'
  snapshot_sha256: 47e1db788538e999e1b5b29f9ba0083b48995dd40531ed184e36ac5eb12bfaa9
- evidence_id: source-5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=AY168855&format=json&size=500
  locator: /results/1/genes/0/geneName; /results/1/uniProtKBCrossReferences[database=EMBL,id=AY168855];
    /results/1/references/0/referenceComments[type=STRAIN]; /results/1/comments/0/cofactors/0;
    /results/1/comments/0/cofactors/0/evidences; /results/1/comments/1/cofactors/0;
    /results/1/comments/1/cofactors/0/evidences
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: 'UniProtKB unreviewed (TrEMBL) Q6EMI8: native sequence, function and annotation
    evidence. Inspected exact source assertions for hmg-edge-014, hmg-edge-021, hmg-edge-022.
    Source access/version scope: Native four-entry AY168855 response; Q6EMI8 entry
    version 72, sequence version 1, annotation updated 2026-09-02.'
  snapshot_sha256: 47e1db788538e999e1b5b29f9ba0083b48995dd40531ed184e36ac5eb12bfaa9
- evidence_id: source-6
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: rdf:Description[@rdf:about='http://rdf.rhea-db.org/15450']/rh:substrates;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/15449_L']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_15449_compound_5206'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_15449_compound_5206']/rh:compound;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_5206']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15450']/rh:substrates;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/15449_L']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_15449_compound_1198'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_15449_compound_1198']/rh:compound;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_1198']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15450']/rh:products;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/15449_R']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_15449_compound_5213'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_15449_compound_5213']/rh:compound;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_5213']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15450']/rh:products;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/15449_R']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_15449_compound_3249'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_15449_compound_3249']/rh:compound;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_3249']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15449']/rh:directionalReaction[@rdf:resource='http://rdf.rhea-db.org/15450'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/15450']/rh:equation; rh:substrates;
    rh:products; rdf:Description[@rdf:about='http://rdf.rhea-db.org/15450']/rh:products;
    rh:contains1/rh:compound/rh:chebi
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: 'Rhea directed reaction 15450. Inspected exact source assertions for hmg-edge-001,
    hmg-edge-002, hmg-edge-003, hmg-edge-004, hmg-edge-012, hmg-edge-018. Source access/version
    scope: Rhea release 142; complete RDF, exact native triples projected in author
    dossier.'
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: source-7
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: rdf:Description[@rdf:about='http://rdf.rhea-db.org/14818']/rh:substrates;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/14817_L']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_14817_compound_5213'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_14817_compound_5213']/rh:compound;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_5213']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/14818']/rh:products;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/14817_R']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_14817_compound_4618'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_14817_compound_4618']/rh:compound;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_4618']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/14817']/rh:directionalReaction[@rdf:resource='http://rdf.rhea-db.org/14818'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/14818']/rh:equation; rh:substrates;
    rh:products; rdf:Description[@rdf:about='http://rdf.rhea-db.org/14818']/rh:substrates;
    rh:contains1/rh:compound/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/14818']/rh:products;
    rh:contains1/rh:compound/rh:chebi
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: 'Rhea directed reaction 14818. Inspected exact source assertions for hmg-edge-005,
    hmg-edge-006, hmg-edge-013, hmg-edge-018, hmg-edge-019. Source access/version
    scope: Rhea release 142; complete RDF, exact native triples projected in author
    dossier.'
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: source-8
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:substrates;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/10244_L']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_10244_compound_4618'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_10244_compound_4618']/rh:compound;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_4618']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:substrates;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/10244_L']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_10244_compound_1283'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_10244_compound_1283']/rh:compound;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_1283']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:products;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/10244_R']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_10244_compound_3307'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_10244_compound_3307']/rh:compound;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_3307']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:products;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/10244_R']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_10244_compound_3031'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_10244_compound_3031']/rh:compound;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_3031']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:products;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/10244_R']/rh:contains1[@rdf:resource='http://rdf.rhea-db.org/Participant_10244_compound_3249'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Participant_10244_compound_3249']/rh:compound;
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/Compound_3249']/rh:chebi; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10244']/rh:directionalReaction[@rdf:resource='http://rdf.rhea-db.org/10245'];
    rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:equation; rh:substrates;
    rh:products; rdf:Description[@rdf:about='http://rdf.rhea-db.org/10245']/rh:substrates;
    rh:contains1/rh:compound/rh:chebi
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: 'Rhea directed reaction 10245. Inspected exact source assertions for hmg-edge-007,
    hmg-edge-008, hmg-edge-009, hmg-edge-010, hmg-edge-011, hmg-edge-014, hmg-edge-019.
    Source access/version scope: Rhea release 142; complete RDF, exact native triples
    projected in author dossier.'
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: expression-context
  kind: database
  reference: research/pathway_additions/2026-10-11-next-pathways/imodulondb-homogentisate-context.json
  locator: p_putida/precise321/78
  accessed_at: '2026-10-11T02:00:44Z'
  support: context_only
  summary: KT2440 HmgR component contains PP_4621/Q88E47 and PP_4619/Q88E49; it does
    not establish strain U catalysis or regulation.
  snapshot_sha256: e7532650b14f9a2fcac90d801ad061e1cb926557ec50bc0ea154e6f91e021534
- evidence_id: final-gates
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-pathways/integration-validation.json
  locator: Final terminal exit codes and preserved log digests
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: Inspected actual final gate receipts and rehashed retained logs. Full corpus
    checks pass; no in-flight or earlier failure is reported as terminal success.
  snapshot_sha256: c54763a27294bf2d6ea829ac31aba1b87f59884d74a27d03df4aaa356c2149d5
- evidence_id: generated-audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-pathways/generated-graph-kgx-audit.json
  locator: This target SVG/KGX exact graph, evidence and reference preservation
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: Separate actual CLI export and generated downloads match. Exact edge endpoints,
    complete evidence, source contexts and SVG anchors pass; this is structural artifact
    verification, not browser visual inspection.
  snapshot_sha256: 87fe919bba958ee2804f782d7efa0a3a8ec895d324aa2e7e83e9bf13312c4730
- evidence_id: authority-final
  kind: authority
  reference: research/pathway_additions/2026-10-11-next-pathways/authority-integration.json
  locator: Pinned ontology/source additions, baseline preservation and exact native
    new identities
  accessed_at: '2026-10-11T02:00:44Z'
  support: supports
  summary: Canonical snapshots resolve final target IDs, retaining all prior authority
    entries and source metadata.
  snapshot_sha256: 6e0bebf1ed4802f103db47a98e4a0be4eaf9a3a9e4c3c4c13470544087bf0d37
assessments:
- assessment_id: identity
  area: identity
  topic: Exact three-step pathway boundary
  outcome: supported
  summary: GO:1902000 identifies the complete homogentisate-to-fumarate/acetoacetate
    route, unlike the broader five-reaction MetaCyc tyrosine pathway. The primary
    boxed route and current process identity agree.
  target_ids:
  - GO:1902000
  evidence_ids:
  - target
  - identity-search
  - independent-audit
- assessment_id: edges-1
  area: grounding
  topic: hmg-edge-001 through 011
  outcome: supported
  summary: Eleven exact side/participant/coefficient source triples; three balanced
    equations, with dioxygen and water inputs and two net hydrons; no duplicate net
    reaction.
  target_ids:
  - GO:1902000
  evidence_ids:
  - independent-audit
  - rhea
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
  - source-7
  - source-8
- assessment_id: edges-2
  area: graph
  topic: hmg-edge-012 through 014
  outcome: supported
  summary: Three deposited U translations match UniProt exactly; primary figure and
    strain U genetic evidence support qualified enables. HmgB/C assignments rely on
    genetics plus sequence interpretation; no claim of purified strain U enzyme or
    sufficient monomer.
  target_ids:
  - GO:1902000
  evidence_ids:
  - independent-audit
  - rhea
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
  - source-7
  - source-8
- assessment_id: edges-3
  area: identity
  topic: hmg-edge-015 through 019
  outcome: supported
  summary: Exact GO process and primary boxed three-step boundary; order HmgA to HmgC
    to HmgB, separately confirmed by exact shared chemical intermediates. Broader
    five-step MetaCyc pathway is not substituted.
  target_ids:
  - GO:1902000
  evidence_ids:
  - independent-audit
  - rhea
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
  - source-7
  - source-8
- assessment_id: edges-4
  area: evidence
  topic: hmg-edge-020 through 022
  outcome: supported
  summary: 'Exact current cofactor annotations: HmgA broad iron cation via HAMAP ECO:0000255;
    HmgB Ca/Mg via ARBA/PIRSR ECO:0000256. Qualified as inferred/automatic, with no
    occupancy or simultaneous-requirement claim.'
  target_ids:
  - GO:1902000
  evidence_ids:
  - independent-audit
  - rhea
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
  - source-7
  - source-8
- assessment_id: edges-5
  area: scope
  topic: hmg-edge-023 through 024
  outcome: supported
  summary: Exact GO:0005737 positions and IEA:TreeGrafter/IEA:InterPro retained; no
    direct localization/exclusive residence claim.
  target_ids:
  - GO:1902000
  evidence_ids:
  - independent-audit
  - rhea
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
  - source-7
  - source-8
- assessment_id: primary-scope
  area: scope
  topic: Strain U genetics versus KT2440 assays
  outcome: supported
  summary: Native AY168855.1 is strain U; all three deposited translations match target
    UniProt entries exactly. Strain U genetic disruption/complementation supports
    the cluster, while exact HmgB/C activities remain genetics plus homology. KT2440
    extract activity and FeSO4 conditions are not transferred to U.
  target_ids:
  - GO:1902000
  evidence_ids:
  - source-1
  - source-2
  - source-3
  - source-4
  - source-5
  - source-6
  - source-7
  - source-8
  - independent-audit
- assessment_id: expression
  area: evidence
  topic: Bounded structured-source context
  outcome: supported
  summary: Root resolved the canonical client after console-runner dependency failure.
    Reviewer independently reproduced the retained results offline. Computational
    expression association supports context only; dataset or hit absence is not biological
    absence.
  target_ids:
  - GO:1902000
  evidence_ids:
  - expression-context
  - independent-audit
- assessment_id: gates
  area: schema
  topic: Final validation and generated artifacts
  outcome: supported
  summary: Final complete repository checks, target identity gate and structural SVG/KGX
    audit pass on unchanged final target hashes. No deterministic validation is substituted
    for the scientific source assessment.
  target_ids:
  - GO:1902000
  evidence_ids:
  - final-gates
  - generated-audit
  - authority-final
  - independent-audit
findings: []
actions: []
limitations:
- Primary genetic complementation establishes the cluster; HmgB/C exact activities
  are not individually purified strain U assays.
- Strain U HmgA hexamer/iron and HmgB cofactors retain computational evidence levels;
  no imported human complex or strain-specific glutathione assertion.
- Species identifier NCBITaxon:303 is explicitly narrowed to strain U in prose and
  native sequence evidence.
- Comparative iModulonDB KT2440 module 78 cannot establish U biochemical or regulatory
  edges.
- Older primary sources inspected only as abstracts are explicitly labeled; current
  database assertions are not relabeled as new direct experiments.
- Original Documents checkout is OS-inaccessible; hidden/ignored searches cover the
  accessible worktree.
- No browser interaction or new experiments; final generated publication checks are
  programmatic and delegated to root.
notes:
- Primary PMC451635-europe-render.html is the actual 16-page PDF despite its extension;
  %PDF signature and exact body hash verified. The similarly named PMC451635.pdf challenge
  body was rejected. Independent PDFium text extraction and relevant page images were
  inspected after pdftotext was unavailable.
- A second external draft validation rejected the historical initial vendored observation
  because it named an executed command without a retained numeric exit code. Its command
  field was removed; the failed attempt remains an honest delegated observation. Final
  repeated vendored command has observed exit0.
tags:
- scientific-review
- homogentisate
- independent
```

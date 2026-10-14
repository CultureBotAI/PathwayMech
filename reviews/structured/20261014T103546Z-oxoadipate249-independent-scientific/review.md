# Independent scientific review of 3-oxoadipate degradation

- Review: 20261014T103546Z-oxoadipate249-independent-scientific
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-14T10:10:24Z
- Finished UTC: 2026-10-14T10:35:46Z
- Reviewer: Codex /root/next249_scientific_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete record and all 22 edge claims are supported within the declared source and historical-strain limits. No actionable blocker, major or minor finding was identified. Independent original-source replay passed 63 checks and all required full-repository gates passed; partial primary-source access and native annotation conflicts remain explicit.

## Scope And Provenance

One maintained pathway record read in full, including every participant, reaction, edge and reference; original-source verification of all material claims.

Selection: Exact new MetaCyc:PWY-2361 record requested for independent adversarial scientific review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 40b878b91af87a41295bfa90c6bf72fd9efefecb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-2361 | data/pathways/3-oxoadipate-degradation.yaml | maintained | 3-oxoadipate degradation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native review inspect | passed | True | MetaCyc:PWY-2361 | Executed before source assessment; exact input hashes remain unchanged. |
| Independent original-source replay | passed | False | MetaCyc:PWY-2361 | All 63 source-binding, directional chemistry, identity and composition checks passed; this supplements manual scientific reading. |
| just validate | passed | True | MetaCyc:PWY-2361 | Coordinator executed the documented full-repository gate in the shared worktree; reviewer checked real exit 0 receipt/log, exact target and authority bytes unchanged. |
| just test | passed | True | MetaCyc:PWY-2361 | Coordinator executed the documented full-repository gate in the shared worktree; reviewer checked real exit 0 receipt/log, exact target and authority bytes unchanged. |
| just lint | passed | True | MetaCyc:PWY-2361 | Coordinator executed the documented full-repository gate in the shared worktree; reviewer checked real exit 0 receipt/log, exact target and authority bytes unchanged. |
| git diff --check | passed | True | MetaCyc:PWY-2361 | Coordinator executed the documented full-repository gate in the shared worktree; reviewer checked real exit 0 receipt/log, exact target and authority bytes unchanged. |

## Scientific And Domain Assessments

### Exact terminal pathway and full native boundary

identity: supported. Targets: MetaCyc:PWY-2361.

PWY2361 is the complete two-reaction terminal degradation module, with the P. putida catalyst context explicitly bounded. It is neither the entire beta-ketoadipate pathway nor a duplicate of the existing catechol branch.

### All chemical participants, directions and reaction-side edges

grounding: supported. Targets: MetaCyc:PWY-2361.

All seven chemical IDs are exact charged entities. Both reactions retain every side participant with unit coefficients; atomic composition and charge balance. Selected traversal is distinguished from native reversibility.

Reviewed step-1-membership, four step-1 side edges, step-2-membership, four step-2 side edges and transferase-provides-thiolase-intermediate. The shared CoA ester supports direct material transfer; regenerated succinyl-CoA is not an additional net reaction.

### Catalysis and subunit composition

evidence: supported. Targets: MetaCyc:PWY-2361.

Both catalysis edges and all three has_part edges faithfully reflect inspected native objects and retain their evidence tiers and oligomer disagreement. Native component IDs avoid an unjustified modern-strain substitution.

### Six expression-regulation edges and short primary quotations

evidence: supported. Targets: MetaCyc:PWY-2361.

All six regulation edges are supportable at expression level. The record does not claim direct inducer binding or allosteric enzyme activation. Original page pixels support both 1993 excerpts and the 1994 activity excerpt; the later abstract supports the two pcaF statements.

PcaR, 3-oxoadipate and experimental adipate each connect to transferase or thiolase expression. The pcaI reporter is interpreted in the independently established pcaIJ operon context. Abstract-only support and the earlier 1994 uncertainty remain explicit.

### Historical regulator and lineage

scope: supported. Targets: MetaCyc:PWY-2361.

Q52154 matches the deposited pcaR translation. ENA PRS1 metadata and UniProt PRS2000 context are reconciled only through the primary paper lineage and clone donor; the initiating methionine ambiguity remains explicit.

### Cofactors, compartments and adjacent activities

completeness: supported. Targets: MetaCyc:PWY-2361.

No supported component of the selected native reaction boundary is omitted. CoA is a consumed substrate, succinyl-CoA a donor/regenerated intermediate. Experimental magnesium chelate detection, recombinant promoter-binding assays, PcaK transport and other-strain inhibitors do not justify additional physiological edges here.

### All 22 edge claims and local graph grammar

graph: supported. Targets: MetaCyc:PWY-2361.

Every edge endpoint resolves locally, predicates match the native rubric, and evidence is attached to the specific claim. Structured assertions are not mislabelled paper quotations. Required corpus gates passed without changing the reviewed target.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| inspect | /private/tmp/pathwaymech-next-249-independent-review-20261014/inspect.json; source.inputs and targets | supports | Pre-assessment native inspect captured exact target, authority snapshots, local graph rubric and validator bytes. |
| native-pathway | https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=META:PWY-2361; Complete native Pathway: reaction-list, reaction-ordering, reaction-layout, comment, species | supports | Exactly two reactions form the complete terminal module; CoA transfer traverses L2R and thiolysis R2L. Upstream branches and TCA are linked neighbors. The erroneous Chan79/PMID761399 pointer is not used as primary support. |
| native-activities | /private/tmp/pathwaymech-next-249-native-20261014/originals; META-ENZRXN-3369.xml and META-ENZRXN-5295.xml; enzyme/reaction/evidence/comment; corresponding complete reaction objects | supports | Native transferase annotation cites purified protein; native thiolase annotation cites mutant phenotype. Reaction cross-references and reversible source orientation agree with the selected Rhea directions. Transferase synthesis induction is explicitly in ENZRXN-3369. |
| native-assemblies | /private/tmp/pathwaymech-next-249-native-20261014/originals; CPLX-2722 component/coefficient; CPLX-2746 component/coefficient; all three monomer component-of/species/dblink fields | supports | Native alpha2beta2 and PcaF homotetramer are source-scoped annotations. All reciprocal component links and P. putida species nodes resolve. CPLX-2722 contains the documented contradictory purification comment. |
| rhea | https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz; Original RDF subjects 12049/19483; side, contains1, participant, compound and ChEBI links | supports | Independent traversal of the complete RDF confirms all eight chemical-side claims and coefficient one. Both equations balance all atoms and charge, with no omitted proton or water. Succinyl-CoA is consumed then regenerated. |
| chebi | /private/tmp/pathwaymech-next-249-chemistry-20261014/originals; Complete issuing ChEBI JSON objects 15775,57348,57292,30031,57288,57287,17128; chemical_data/default_structure | supports | All seven exact charged labels, formulas, charges and structures match the maintained nodes. Adipate dianion is distinct from neutral adipic acid; it is only an experimental regulatory-context node. |
| native-chemical-identity | /private/tmp/pathwaymech-next-249-independent-review-20261014/native-chebi-identity-replay.json; All six original native compound XML InChIs and CML formula/charge versus issuing ChEBI JSON | supports | All six full InChIs, including stereochemistry and protonation, match exactly; formula and molecular charge also match. This independently closes the native-to-Rhea chemical identity bridge. |
| uniprot | /private/tmp/pathwaymech-next-249-native-20261014/originals; UniProt-Q52154.json, UniProt-Q01103.json, UniProt-P0A102.json; primaryAccession, comments, references, organism, sequence | supports | Reviewed PcaR is taxon303 with PRS2000 source metadata and positive-regulatory annotation; start methionine remains uncertain. The two transferase accessions independently retain Heterodimer annotations, which the record exposes as conflicting assembly context. |
| ena-pcar | https://www.ebi.ac.uk/ena/browser/api/embl/L33795; Source qualifiers and CDS/translation AAA57136.1 | supports | Independent extraction yields 291 residues exactly matching Q52154. ENA labels PRS1/ATCC12633; the original paper establishes PRS2000 as a PRS1 derivative and identifies the PCR donor as PRS2000. This does not assert complete-genome equivalence. |
| pcar-lineage | PMID:8083169; Original page scans pp.5771-5773 and 5776-5777: introduction, PCR amplification, Table 1, binding Results/Discussion | supports | Personally read the original pages: experimental strains derive from PRS2000, itself a wild-type PRS1 derivative; cloned PCR fragment originated in PRS2000. Recombinant extract DNA-binding experiments concern promoter recognition, not binding to native catalytic complexes. |
| transferase-regulation | PMID:8376330; Original p.5836 scan, Table 3, chromosomal fusion results and Fig. 6; first-page abstract/Methods read in the original scan; additional Methods read through OCR | supports | Both maintained excerpts were checked directly against page pixels. pcaI reporter induction depends on pcaR; adipate and beta-ketoadipate induce the pcaIJ promoter. The PRS4050 conditions are 10 mM glucose plus 20 mM adipate. These are expression assays. |
| thiolase-activity | PMID:7961399; Original pp.6481-6483,6485-6486: Table 1, pcaF mutant paragraph, activity continuation and Discussion | supports | PRS4061 carries the pcaF disruption. The quoted wild-type activity values and mutant residual activity were verified on p.6485; p.6483 provides growth conditions. The 1994 discussion explicitly leaves PcaR regulation of pcaF/pcaK unresolved. The p.6482 assay uses magnesium-chelate absorbance as the readout, not proof of a physiological cofactor. |
| thiolase-conditions | PMID:7961399; Original p.6483, bottom right paragraph continued across full-page Fig. 4 to p.6485 | supports | The comparison is growth on 10 mM glucose versus 10 mM glucose plus 20 mM adipate; this supports induction of extract activity, not acute allosteric activation of purified thiolase. |
| later-regulation | PMID:8522507; Original archived PMC177579 HTML abstract; title/PMID/DOI metadata | supports | The abstract explicitly identifies PRS2000 and reports independent pcaF/pcaK transcription, PcaR requirement and beta-ketoadipate induction. Both maintained short excerpts are exact. Full-paper experimental details were not independently accessible. |
| transferase-primary | PMID:1624453; Original pp.4657-4658 scans: abstract, introduction and pathway Figure1 | supports | Two transferase subunits and the terminal two-step route are supported. The primary report distinguishes the upstream aromatic branches from the shared terminal module and describes the clone-based enzyme assignment. |
| oligomer-primary | https://www.researchgate.net/publication/16417561_Evolutionarily_homologous_alpha_2_beta_2_oligomeric_structures_in_beta-ketoadipate_succinyl-CoA_transferases_from_Acinetobacter_calcoaceticus_and_Pseudomonas_putida; Rendered original-paper abstract, discussion pp.1565-1566 and Table VI; PMID6780551 | supports | Independent rendered-source reading supports homogeneous transferase preparations and the approximate native-size inference favoring alpha2beta2. The miniprint methods/results and original figures were not inspected; no PDF digest is claimed. |
| imodulondb | https://imodulondb.org/; Fresh official kg-microbe-sources CLI datasets, search p_putida/precise321 pca, summarize component 65 | context_only | The only returned P. putida dataset is precise321. Component65 includes 45 genes; pcaF-I/PP_1377, pcaI/PP_3951 and pcaJ/PP_3952 map to modern KT2440 accessions, not the historical PRS2000 proteins. This is expression-module context, not catalytic or direct-regulation evidence. |
| source-replay | /private/tmp/pathwaymech-next-249-independent-review-20261014/independent-original-replay.json; 63 checks; exact originals and SHA-256 manifest | supports | Independent reviewer-authored replay verifies native pathway completeness, original reference digests, exact species/component assertions, Rhea sides/coefficient/balance, ChEBI labels and PcaR translation equality. |
| gate-validate | /private/tmp/pathwaymech-next-249-checks/final/just-validate.log; Complete coordinator-executed log and matching receipt; same worktree and unchanged scientific inputs | supports | Reviewer read the coordinator-run gate log and verified its SHA-256. Command exited 0; this is a full repository gate, not a scientific truth certificate. |
| gate-test | /private/tmp/pathwaymech-next-249-checks/final/just-test.log; Complete coordinator-executed log and matching receipt; same worktree and unchanged scientific inputs | supports | Reviewer read the coordinator-run gate log and verified its SHA-256. Command exited 0; this is a full repository gate, not a scientific truth certificate. |
| gate-lint | /private/tmp/pathwaymech-next-249-checks/final/just-lint.log; Complete coordinator-executed log and matching receipt; same worktree and unchanged scientific inputs | supports | Reviewer read the coordinator-run gate log and verified its SHA-256. Command exited 0; this is a full repository gate, not a scientific truth certificate. |
| gate-check | /private/tmp/pathwaymech-next-249-checks/final/git-diff-check.log; Complete coordinator-executed log and matching receipt; same worktree and unchanged scientific inputs | supports | Reviewer read the coordinator-run gate log and verified its SHA-256. Command exited 0; this is a full repository gate, not a scientific truth certificate. |

## Limits And Additional Notes

- The 1981 original paper was independently read through its rendered abstract, discussion and Table VI; original miniprint methods/results and figure pixels were not read. No original PDF digest is claimed.
- The 1995 source is an inspected author abstract; full-paper methods, figures and tables were inaccessible, and the record explicitly limits those expression claims.
- PcaF homotetramer is retained as native database annotation, not proven oligomer measurement in the 1994 mutant paper. Transferase alpha2beta2 conflicts with current UniProt Heterodimer annotation; both remain visible.
- The exact deposited PcaR translation is supported, but initiating Met-1/23/45 remains uncertain. PRS1 lineage evidence does not establish universal strain or modern KT2440 equivalence.
- The reviewer personally inspected selected original pages supporting the current claims; the author dossier records more extensive full-paper reading. No claim of exhaustive new-source discovery, all-source re-download, interactive browser testing or public-release clearance is made.
- An independent replay helper initially stripped internal FT letters while removing EMBL line prefixes; that reviewer-only parser error was corrected to remove line-leading FT before the successful exact-sequence replay. No maintained record defect or edit resulted.
- Fresh iModulonDB CLI datasets/search/summarize commands exited 0; the resulting KT2440 module is contextual and is not promoted to PRS2000 evidence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T103546Z-oxoadipate249-independent-scientific
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of 3-oxoadipate degradation
started_at: '2026-10-14T10:10:24Z'
finished_at: '2026-10-14T10:35:46Z'
reviewer:
  identity: Codex /root/next249_scientific_review
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Fresh reviewer; did not author the record, authority updates
    or primary/chemical research. Independently read original native and issuing-source
    objects, selected primary page scans and exact abstract text, ran original-source
    replay and the official iModulonDB CLI. Parent supplied inherited context as leads,
    not proof.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete record and all 22 edge claims are supported within the declared
  source and historical-strain limits. No actionable blocker, major or minor finding
  was identified. Independent original-source replay passed 63 checks and all required
  full-repository gates passed; partial primary-source access and native annotation
  conflicts remain explicit.
source:
  git_revision: 40b878b91af87a41295bfa90c6bf72fd9efefecb
  state: working_tree
  inputs:
  - path: data/identifier_authorities/ontology.json
    sha256: a6d88afec992c8b2c198c8c95fd8f29427d36d1fb7839b3976b516eac069ec30
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: e60cf18738b14da2476ce10cdcb5d6cd7ea3535959152f7056135fbc9592ba72
    role: context
  - path: data/pathways/3-oxoadipate-degradation.yaml
    sha256: 214ef2d38ede4bb4e919f6f53699491e7c53b8d9b5b858c6ba80084e5b067032
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 4f3f46d1f4b8ebafa9b2d04d9700510df18b6ec6f881856fda521879f494d153
    role: context
  - path: src/pathwaymech/schema.py
    sha256: bd99c1e6ca1f6eec5c82c58aa1ae3f43f696d30be66fbe0977dcace81292e0b8
    role: context
scope:
  description: One maintained pathway record read in full, including every participant,
    reaction, edge and reference; original-source verification of all material claims.
  selection: Exact new MetaCyc:PWY-2361 record requested for independent adversarial
    scientific review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-2361
  exclusions:
  - target: Other pathway records, public-release licensing and merge readiness
    reason: Outside this one-record scientific verdict; full-corpus deterministic
      gates do not extend the scientific scope.
  - target: Exhaustive new literature discovery and whole-paper rereading of every
      source
    reason: Reviewed the claim-bearing original pages and structured sources; author
      reading coverage is not represented as the reviewer personally reading every
      page.
targets:
- target_id: MetaCyc:PWY-2361
  path: data/pathways/3-oxoadipate-degradation.yaml
  label: 3-oxoadipate degradation
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/3-oxoadipate-degradation.yaml
    role: maintained pathway record
checks:
- check_id: inspect
  name: Native review inspect
  status: passed
  required: true
  summary: Executed before source assessment; exact input hashes remain unchanged.
  target_ids:
  - MetaCyc:PWY-2361
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B scripts/record_review.py
    inspect --targets /private/tmp/pathwaymech-next-249-independent-review-20261014/targets.yaml
    --input src/pathwaymech/schema.py --input docs/CAUSAL_GRAPHS.md --input data/identifier_authorities/sources.json
    --input data/identifier_authorities/ontology.json
  exit_code: 0
  evidence_ids:
  - inspect
- check_id: source-replay
  name: Independent original-source replay
  status: passed
  required: false
  summary: All 63 source-binding, directional chemistry, identity and composition
    checks passed; this supplements manual scientific reading.
  target_ids:
  - MetaCyc:PWY-2361
  command: /private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B /private/tmp/pathwaymech-next-249-independent-review-20261014/replay.py
  exit_code: 0
  evidence_ids:
  - source-replay
- check_id: gate-validate
  name: just validate
  status: passed
  required: true
  summary: Coordinator executed the documented full-repository gate in the shared
    worktree; reviewer checked real exit 0 receipt/log, exact target and authority
    bytes unchanged.
  target_ids:
  - MetaCyc:PWY-2361
  command: just validate
  exit_code: 0
  evidence_ids:
  - gate-validate
  scope_note: The full corpus is checked deterministically; only PWY2361 is scientifically
    assessed here.
- check_id: gate-test
  name: just test
  status: passed
  required: true
  summary: Coordinator executed the documented full-repository gate in the shared
    worktree; reviewer checked real exit 0 receipt/log, exact target and authority
    bytes unchanged.
  target_ids:
  - MetaCyc:PWY-2361
  command: just test
  exit_code: 0
  evidence_ids:
  - gate-test
  scope_note: The full corpus is checked deterministically; only PWY2361 is scientifically
    assessed here.
- check_id: gate-lint
  name: just lint
  status: passed
  required: true
  summary: Coordinator executed the documented full-repository gate in the shared
    worktree; reviewer checked real exit 0 receipt/log, exact target and authority
    bytes unchanged.
  target_ids:
  - MetaCyc:PWY-2361
  command: just lint
  exit_code: 0
  evidence_ids:
  - gate-lint
  scope_note: The full corpus is checked deterministically; only PWY2361 is scientifically
    assessed here.
- check_id: gate-check
  name: git diff --check
  status: passed
  required: true
  summary: Coordinator executed the documented full-repository gate in the shared
    worktree; reviewer checked real exit 0 receipt/log, exact target and authority
    bytes unchanged.
  target_ids:
  - MetaCyc:PWY-2361
  command: git diff --check
  exit_code: 0
  evidence_ids:
  - gate-check
  scope_note: The full corpus is checked deterministically; only PWY2361 is scientifically
    assessed here.
evidence:
- evidence_id: inspect
  kind: validation
  reference: /private/tmp/pathwaymech-next-249-independent-review-20261014/inspect.json
  locator: source.inputs and targets
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Pre-assessment native inspect captured exact target, authority snapshots,
    local graph rubric and validator bytes.
  snapshot_sha256: 25c3ad182126fc49ab6f2421c3d55cb9c37698e2b93891e233855d94d1e246b8
- evidence_id: native-pathway
  kind: database
  reference: https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=META:PWY-2361
  locator: 'Complete native Pathway: reaction-list, reaction-ordering, reaction-layout,
    comment, species'
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Exactly two reactions form the complete terminal module; CoA transfer traverses
    L2R and thiolysis R2L. Upstream branches and TCA are linked neighbors. The erroneous
    Chan79/PMID761399 pointer is not used as primary support.
  snapshot_sha256: 7e8795224de295517ebd98df074c96a5063c856892968dbbe6b7a2431437bd58
- evidence_id: native-activities
  kind: database
  reference: /private/tmp/pathwaymech-next-249-native-20261014/originals
  locator: META-ENZRXN-3369.xml and META-ENZRXN-5295.xml; enzyme/reaction/evidence/comment;
    corresponding complete reaction objects
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Native transferase annotation cites purified protein; native thiolase annotation
    cites mutant phenotype. Reaction cross-references and reversible source orientation
    agree with the selected Rhea directions. Transferase synthesis induction is explicitly
    in ENZRXN-3369.
- evidence_id: native-assemblies
  kind: database
  reference: /private/tmp/pathwaymech-next-249-native-20261014/originals
  locator: CPLX-2722 component/coefficient; CPLX-2746 component/coefficient; all three
    monomer component-of/species/dblink fields
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Native alpha2beta2 and PcaF homotetramer are source-scoped annotations.
    All reciprocal component links and P. putida species nodes resolve. CPLX-2722
    contains the documented contradictory purification comment.
- evidence_id: rhea
  kind: authority
  reference: https://ftp.expasy.org/databases/rhea/rdf/rhea.rdf.gz
  locator: Original RDF subjects 12049/19483; side, contains1, participant, compound
    and ChEBI links
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Independent traversal of the complete RDF confirms all eight chemical-side
    claims and coefficient one. Both equations balance all atoms and charge, with
    no omitted proton or water. Succinyl-CoA is consumed then regenerated.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: chebi
  kind: authority
  reference: /private/tmp/pathwaymech-next-249-chemistry-20261014/originals
  locator: Complete issuing ChEBI JSON objects 15775,57348,57292,30031,57288,57287,17128;
    chemical_data/default_structure
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: All seven exact charged labels, formulas, charges and structures match
    the maintained nodes. Adipate dianion is distinct from neutral adipic acid; it
    is only an experimental regulatory-context node.
- evidence_id: native-chemical-identity
  kind: authority
  reference: /private/tmp/pathwaymech-next-249-independent-review-20261014/native-chebi-identity-replay.json
  locator: All six original native compound XML InChIs and CML formula/charge versus
    issuing ChEBI JSON
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: All six full InChIs, including stereochemistry and protonation, match exactly;
    formula and molecular charge also match. This independently closes the native-to-Rhea
    chemical identity bridge.
  snapshot_sha256: 97b7452a8bef94f443d8b5939fb148991c79c3a8b53d08c7e3c8123ea6ebd1ef
- evidence_id: uniprot
  kind: database
  reference: /private/tmp/pathwaymech-next-249-native-20261014/originals
  locator: UniProt-Q52154.json, UniProt-Q01103.json, UniProt-P0A102.json; primaryAccession,
    comments, references, organism, sequence
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Reviewed PcaR is taxon303 with PRS2000 source metadata and positive-regulatory
    annotation; start methionine remains uncertain. The two transferase accessions
    independently retain Heterodimer annotations, which the record exposes as conflicting
    assembly context.
- evidence_id: ena-pcar
  kind: authority
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/L33795
  locator: Source qualifiers and CDS/translation AAA57136.1
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Independent extraction yields 291 residues exactly matching Q52154. ENA
    labels PRS1/ATCC12633; the original paper establishes PRS2000 as a PRS1 derivative
    and identifies the PCR donor as PRS2000. This does not assert complete-genome
    equivalence.
  snapshot_sha256: e7269b567ac1de9ff97e197d6000f656b4349d3e059af024172c1c6eff2457c6
- evidence_id: pcar-lineage
  kind: primary_source
  reference: PMID:8083169
  locator: 'Original page scans pp.5771-5773 and 5776-5777: introduction, PCR amplification,
    Table 1, binding Results/Discussion'
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: 'Personally read the original pages: experimental strains derive from PRS2000,
    itself a wild-type PRS1 derivative; cloned PCR fragment originated in PRS2000.
    Recombinant extract DNA-binding experiments concern promoter recognition, not
    binding to native catalytic complexes.'
  snapshot_sha256: e5f47abbeb8771c15867605846d4baece79616c397a1e975c47c6299d52c45d4
- evidence_id: transferase-regulation
  kind: primary_source
  reference: PMID:8376330
  locator: Original p.5836 scan, Table 3, chromosomal fusion results and Fig. 6; first-page
    abstract/Methods read in the original scan; additional Methods read through OCR
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Both maintained excerpts were checked directly against page pixels. pcaI
    reporter induction depends on pcaR; adipate and beta-ketoadipate induce the pcaIJ
    promoter. The PRS4050 conditions are 10 mM glucose plus 20 mM adipate. These are
    expression assays.
  snapshot_sha256: 00dfc73098fd7472978b5c9f5dfc8cc3f99a82676459b0a12a1ba880d896cf51
- evidence_id: thiolase-activity
  kind: primary_source
  reference: PMID:7961399
  locator: 'Original pp.6481-6483,6485-6486: Table 1, pcaF mutant paragraph, activity
    continuation and Discussion'
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: PRS4061 carries the pcaF disruption. The quoted wild-type activity values
    and mutant residual activity were verified on p.6485; p.6483 provides growth conditions.
    The 1994 discussion explicitly leaves PcaR regulation of pcaF/pcaK unresolved.
    The p.6482 assay uses magnesium-chelate absorbance as the readout, not proof of
    a physiological cofactor.
  snapshot_sha256: 5f69718ba1094fcbf8836ecbd4eda381a2bd5bc99cf9629728fb1c40ae05f9de
- evidence_id: thiolase-conditions
  kind: primary_source
  reference: PMID:7961399
  locator: Original p.6483, bottom right paragraph continued across full-page Fig.
    4 to p.6485
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: The comparison is growth on 10 mM glucose versus 10 mM glucose plus 20
    mM adipate; this supports induction of extract activity, not acute allosteric
    activation of purified thiolase.
  snapshot_sha256: b09aea1be5e7bbda554087484bd7e1ac845b47601262fffa48629ef5d8284468
- evidence_id: later-regulation
  kind: primary_source
  reference: PMID:8522507
  locator: Original archived PMC177579 HTML abstract; title/PMID/DOI metadata
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: The abstract explicitly identifies PRS2000 and reports independent pcaF/pcaK
    transcription, PcaR requirement and beta-ketoadipate induction. Both maintained
    short excerpts are exact. Full-paper experimental details were not independently
    accessible.
  snapshot_sha256: 74023204ca88f44c6d55a110b5c1c3ed2cd25b17cf31f8bb13ceb16d81ee6e6c
- evidence_id: transferase-primary
  kind: primary_source
  reference: PMID:1624453
  locator: 'Original pp.4657-4658 scans: abstract, introduction and pathway Figure1'
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Two transferase subunits and the terminal two-step route are supported.
    The primary report distinguishes the upstream aromatic branches from the shared
    terminal module and describes the clone-based enzyme assignment.
  snapshot_sha256: 802c001adad64b2101616b8dbfc17dd6e07fce44afe7bf4667cda2016fa1b863
- evidence_id: oligomer-primary
  kind: primary_source
  reference: https://www.researchgate.net/publication/16417561_Evolutionarily_homologous_alpha_2_beta_2_oligomeric_structures_in_beta-ketoadipate_succinyl-CoA_transferases_from_Acinetobacter_calcoaceticus_and_Pseudomonas_putida
  locator: Rendered original-paper abstract, discussion pp.1565-1566 and Table VI;
    PMID6780551
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Independent rendered-source reading supports homogeneous transferase preparations
    and the approximate native-size inference favoring alpha2beta2. The miniprint
    methods/results and original figures were not inspected; no PDF digest is claimed.
- evidence_id: imodulondb
  kind: database
  reference: https://imodulondb.org/
  locator: Fresh official kg-microbe-sources CLI datasets, search p_putida/precise321
    pca, summarize component 65
  accessed_at: '2026-10-14T10:35:46Z'
  support: context_only
  summary: The only returned P. putida dataset is precise321. Component65 includes
    45 genes; pcaF-I/PP_1377, pcaI/PP_3951 and pcaJ/PP_3952 map to modern KT2440 accessions,
    not the historical PRS2000 proteins. This is expression-module context, not catalytic
    or direct-regulation evidence.
  snapshot_sha256: 51b9bdf4e6f176e5e4b91a21d12bb8b53461d3990bb3f78fa98032490864a277
  search_scope: Complete returned dataset inventory; pca query and component 65 summary.
    CLI displays top 20 genes; author full 45-row original payload was also read.
    This is not an exhaustive literature search or proof of absent unlisted datasets.
- evidence_id: source-replay
  kind: validation
  reference: /private/tmp/pathwaymech-next-249-independent-review-20261014/independent-original-replay.json
  locator: 63 checks; exact originals and SHA-256 manifest
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Independent reviewer-authored replay verifies native pathway completeness,
    original reference digests, exact species/component assertions, Rhea sides/coefficient/balance,
    ChEBI labels and PcaR translation equality.
  snapshot_sha256: 362e81540cdfb20d91d4882fc074f65d33138f0a069de5e539b5d76117e4485c
- evidence_id: gate-validate
  kind: validation
  reference: /private/tmp/pathwaymech-next-249-checks/final/just-validate.log
  locator: Complete coordinator-executed log and matching receipt; same worktree and
    unchanged scientific inputs
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Reviewer read the coordinator-run gate log and verified its SHA-256. Command
    exited 0; this is a full repository gate, not a scientific truth certificate.
  snapshot_sha256: 58bea3b1c98513e0bcb43972faf423484b32f612a50437406a562dd35dcb780f
- evidence_id: gate-test
  kind: validation
  reference: /private/tmp/pathwaymech-next-249-checks/final/just-test.log
  locator: Complete coordinator-executed log and matching receipt; same worktree and
    unchanged scientific inputs
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Reviewer read the coordinator-run gate log and verified its SHA-256. Command
    exited 0; this is a full repository gate, not a scientific truth certificate.
  snapshot_sha256: 35ce2f7fe1e90d778b993ca7e33404cea1ef7ec0de2a588a7e5d695918f91244
- evidence_id: gate-lint
  kind: validation
  reference: /private/tmp/pathwaymech-next-249-checks/final/just-lint.log
  locator: Complete coordinator-executed log and matching receipt; same worktree and
    unchanged scientific inputs
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Reviewer read the coordinator-run gate log and verified its SHA-256. Command
    exited 0; this is a full repository gate, not a scientific truth certificate.
  snapshot_sha256: df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41
- evidence_id: gate-check
  kind: validation
  reference: /private/tmp/pathwaymech-next-249-checks/final/git-diff-check.log
  locator: Complete coordinator-executed log and matching receipt; same worktree and
    unchanged scientific inputs
  accessed_at: '2026-10-14T10:35:46Z'
  support: supports
  summary: Reviewer read the coordinator-run gate log and verified its SHA-256. Command
    exited 0; this is a full repository gate, not a scientific truth certificate.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
assessments:
- assessment_id: identity
  area: identity
  topic: Exact terminal pathway and full native boundary
  outcome: supported
  summary: PWY2361 is the complete two-reaction terminal degradation module, with
    the P. putida catalyst context explicitly bounded. It is neither the entire beta-ketoadipate
    pathway nor a duplicate of the existing catechol branch.
  target_ids:
  - MetaCyc:PWY-2361
  evidence_ids:
  - native-pathway
  - transferase-primary
  dimensions:
  - name: taxon-scope
    value: Pseudomonas putida; historical PRS2000 lineage for regulation
    definition: Species context is broader than the specific experimental regulatory
      lineage; neither implies universal strain composition.
    evidence_ids:
    - native-pathway
    - pcar-lineage
    - transferase-regulation
    - later-regulation
- assessment_id: chemistry
  area: grounding
  topic: All chemical participants, directions and reaction-side edges
  outcome: supported
  summary: All seven chemical IDs are exact charged entities. Both reactions retain
    every side participant with unit coefficients; atomic composition and charge balance.
    Selected traversal is distinguished from native reversibility.
  target_ids:
  - MetaCyc:PWY-2361
  evidence_ids:
  - rhea
  - chebi
  - native-chemical-identity
  - source-replay
  details: Reviewed step-1-membership, four step-1 side edges, step-2-membership,
    four step-2 side edges and transferase-provides-thiolase-intermediate. The shared
    CoA ester supports direct material transfer; regenerated succinyl-CoA is not an
    additional net reaction.
- assessment_id: catalysts
  area: evidence
  topic: Catalysis and subunit composition
  outcome: supported
  summary: Both catalysis edges and all three has_part edges faithfully reflect inspected
    native objects and retain their evidence tiers and oligomer disagreement. Native
    component IDs avoid an unjustified modern-strain substitution.
  target_ids:
  - MetaCyc:PWY-2361
  evidence_ids:
  - native-activities
  - native-assemblies
  - uniprot
  - oligomer-primary
  - thiolase-activity
  dimensions:
  - name: evidence-tier
    value: 'Transferase: native purified-protein annotation plus partial primary reading;
      thiolase: mutant-phenotype annotation and extract activity'
    definition: Evidence for function does not independently establish all assembly
      stoichiometries.
    evidence_ids:
    - native-activities
    - thiolase-activity
    - oligomer-primary
- assessment_id: regulation
  area: evidence
  topic: Six expression-regulation edges and short primary quotations
  outcome: supported
  summary: All six regulation edges are supportable at expression level. The record
    does not claim direct inducer binding or allosteric enzyme activation. Original
    page pixels support both 1993 excerpts and the 1994 activity excerpt; the later
    abstract supports the two pcaF statements.
  target_ids:
  - MetaCyc:PWY-2361
  evidence_ids:
  - transferase-regulation
  - thiolase-activity
  - thiolase-conditions
  - later-regulation
  - uniprot
  details: PcaR, 3-oxoadipate and experimental adipate each connect to transferase
    or thiolase expression. The pcaI reporter is interpreted in the independently
    established pcaIJ operon context. Abstract-only support and the earlier 1994 uncertainty
    remain explicit.
- assessment_id: protein-identity
  area: scope
  topic: Historical regulator and lineage
  outcome: supported
  summary: Q52154 matches the deposited pcaR translation. ENA PRS1 metadata and UniProt
    PRS2000 context are reconciled only through the primary paper lineage and clone
    donor; the initiating methionine ambiguity remains explicit.
  target_ids:
  - MetaCyc:PWY-2361
  evidence_ids:
  - uniprot
  - ena-pcar
  - pcar-lineage
- assessment_id: exclusions
  area: completeness
  topic: Cofactors, compartments and adjacent activities
  outcome: supported
  summary: No supported component of the selected native reaction boundary is omitted.
    CoA is a consumed substrate, succinyl-CoA a donor/regenerated intermediate. Experimental
    magnesium chelate detection, recombinant promoter-binding assays, PcaK transport
    and other-strain inhibitors do not justify additional physiological edges here.
  target_ids:
  - MetaCyc:PWY-2361
  evidence_ids:
  - native-pathway
  - native-activities
  - rhea
  - thiolase-activity
  - pcar-lineage
  - imodulondb
- assessment_id: representation
  area: graph
  topic: All 22 edge claims and local graph grammar
  outcome: supported
  summary: Every edge endpoint resolves locally, predicates match the native rubric,
    and evidence is attached to the specific claim. Structured assertions are not
    mislabelled paper quotations. Required corpus gates passed without changing the
    reviewed target.
  target_ids:
  - MetaCyc:PWY-2361
  evidence_ids:
  - source-replay
  - gate-validate
  - gate-test
  - gate-lint
  - gate-check
findings: []
actions: []
limitations:
- The 1981 original paper was independently read through its rendered abstract, discussion
  and Table VI; original miniprint methods/results and figure pixels were not read.
  No original PDF digest is claimed.
- The 1995 source is an inspected author abstract; full-paper methods, figures and
  tables were inaccessible, and the record explicitly limits those expression claims.
- PcaF homotetramer is retained as native database annotation, not proven oligomer
  measurement in the 1994 mutant paper. Transferase alpha2beta2 conflicts with current
  UniProt Heterodimer annotation; both remain visible.
- The exact deposited PcaR translation is supported, but initiating Met-1/23/45 remains
  uncertain. PRS1 lineage evidence does not establish universal strain or modern KT2440
  equivalence.
- The reviewer personally inspected selected original pages supporting the current
  claims; the author dossier records more extensive full-paper reading. No claim of
  exhaustive new-source discovery, all-source re-download, interactive browser testing
  or public-release clearance is made.
notes:
- An independent replay helper initially stripped internal FT letters while removing
  EMBL line prefixes; that reviewer-only parser error was corrected to remove line-leading
  FT before the successful exact-sequence replay. No maintained record defect or edit
  resulted.
- Fresh iModulonDB CLI datasets/search/summarize commands exited 0; the resulting
  KT2440 module is contextual and is not promoted to PRS2000 evidence.
tags:
- scientific-review
- adversarial-review
- source-scoped
- next249
```

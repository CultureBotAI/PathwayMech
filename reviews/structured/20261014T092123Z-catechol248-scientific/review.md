# Independent scientific review of catechol degradation to beta-ketoadipate

- Review: 20261014T092123Z-catechol248-scientific
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-14T09:03:38.556929Z
- Finished UTC: 2026-10-14T09:21:23.210634Z
- Reviewer: Codex /root/catechol248_independent_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact four-reaction native catechol ortho-cleavage route is supported. All 32 edges, 18 participants, four core activities plus a typed downstream interface, 24 references and all material source-to-graph dispositions were assessed. The final corrected record has no unresolved actionable finding. Historical catalyst identities, inferred PcaD assembly, model-specific Fe(III), native expression-level induction and incomplete primary access remain explicit. All required final validation, test, lint and whitespace gates passed.

## Scope And Provenance

Complete independent scientific review of one maintained next248 catechol record, with contextual preservation checks for prior records and authority rows.

Selection: Exact maintained path and MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY identity requested by the parent curator; no sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 22f4279d66ab39cf153a9a1f7333150671d1b17b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | data/pathways/catechol-degradation-to-beta-ketoadipate.yaml | maintained | catechol degradation to β-ketoadipate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate | passed | True | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | Final-byte root-run check passed; log and receipt independently verified. |
| just test | passed | True | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | Final-byte root-run check passed; log and receipt independently verified. |
| just render-pages | passed | False | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | Final-byte root-run check passed; log and receipt independently verified. |
| just kgx-export --output-dir /private/tmp/pathwaymech-next-248-kgx | passed | False | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | Final-byte root-run check passed; log and receipt independently verified. |
| just lint | passed | True | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | Personally executed on final 39ca1eed; exit 0. |
| git diff --check | passed | True | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | Personally executed on final 39ca1eed; exit 0. |
| Initial superseded-draft validate | failed | False | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | Failure on unsupported year metadata in old 2e9b575b. This is historical, not the current required gate. |
| Initial superseded-draft test | failed | False | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | The old draft had one closed-schema failure and3478 passing tests before the run was interrupted. The final-byte complete rerun passed4867 tests with3 skips; this historical result is not the current required gate. |
| Initial reviewer lint environment attempt | failed | False | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | Environment/cache access failed before Ruff; final required lint retry passed. |
| Fresh native inspect after schema repair | passed | False | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | Exact final input bytes captured and change reassessed at unchanged HEAD. |
| Full source-to-graph and graph-to-source assessment | passed | False | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | All 32 edges, all record fields and10 material source-fact dispositions independently assessed. |
| Independent complete chemistry and native assembly replay | passed | False | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | 55 original-object checks pass. |
| Complete original reference digest verification | passed | False | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | 23 of 23 asserted hashes match; intentionally unhashed paper is disclosed. |
| Structured adapter datasets and catechol search | passed | False | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | Two actual commands passed; zero module hits means summarize is not applicable. |
| Static graph and exact export review | passed | False | MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY | Reviewer viewed full raster and read exact32-edge export replay; interactive browser unavailable. |

## Scientific And Domain Assessments

### Exact native pathway and downstream boundary

identity: supported. Targets: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY.

The four-reaction CATECHOL-ORTHO-CLEAVAGE-PWY ends at 3-oxoadipate. PWY-2361 receives that material as an explicitly typed interface; its CoA-transfer/thiolysis reactions are outside the core. The larger PWY-5417 is not conflated with this pathway.

### Complete sides, coefficients, charge and stereochemistry

grounding: supported. Targets: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY.

All four complete native/Rhea reactions agree, including oxygen, water and hydrons. RHEA:30033 source direction is right_to_left. Exact S-muconolactone is retained; a broader stereounspecified alternative is not silently equated.

### Database-scoped native catalysts and component roles

evidence: supported. Targets: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY.

All four enzymatic-reaction assignments and their species/component fields are supported by exact native objects. Generic CatA two-subunit wording does not imply all three C-1 isozyme variants are homodimers. Deleted Q9AEQ0 and modern Q88N36 are not selected identities.

### Historical hydrolase preparation and inferred trimer

evidence: supported. Targets: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY.

The recorded three 11 kDa-subunit interpretation faithfully reflects the 1980 inference and native component coefficient. PRS2260 preparation and denaturation dependence are explicit. Purifying an unmodified cellular enzyme does not itself establish an engineered protein construct; no modern sequence or definitive structural claim is made.

### Mn2+ native cofactor and scoped modeled Fe3+

evidence: supported. Targets: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY.

Native Mn2+ cofactor fields support cat-029. The issuing PDB 2AZQ CIF and exact FE chemical identity support cat-032 only in its C-1 molecular-state scope, with two Tyr/two His metal contacts and explicit model-assigned oxidation state. PCF binding does not establish a particular necessary physiological cofactor.

### Expression-level hydrolase induction

graph: supported. Targets: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY.

The native CPLX-2761 comment supports 3-oxoadipate induction. The generic regulates edge and explicit expression-level description avoid inventing direct ligand binding, catalytic activation or a regulator gene.

### Material source-to-graph accounting

completeness: supported. Targets: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY.

All core chemical and catalyst facts are represented. Neighboring modules, a Cupriavidus dechlorination example, modern sequence joins, PCF physiological necessity and 2010 A1501 experiments have explicit bounded exclusion reasons. The HPLC conflict is preserved rather than used to strengthen the pathway.

### Exact original bindings and preserved authority/corpus context

provenance: supported. Targets: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY.

All asserted reference hashes match complete original files. The one unhashed primary citation accurately reports its access limits. Source-local assertions, authority preservation and all 245 baseline record hashes are verified.

### Structured iModulonDB cross-check

scope: supported. Targets: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY.

Two catechol dioxygenase gene annotations in p_putida/precise321 supply bounded context; they do not establish historical catalyst sequence identity. Zero module hits is a query result, not negative biological evidence.

### Graph evidence and qualifier preservation

representation: supported. Targets: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY.

All 32 exported edges retain exact descriptions, evidence, endpoint qualifiers and full references. The separate C-1 model node and downstream pathway context are visible in static rendering. Interactive behavior remains untested.

### Final technical gates and repaired draft schema

schema: supported. Targets: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY.

The unsupported reference year field was removed without changing any scientific claim. Final-byte validation, full tests, lint and whitespace checks passed. Historical failures and environment retry remain preserved, with exact input scopes.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/pathways/catechol-degradation-to-beta-ketoadipate.yaml; Entire final record, all 32 edges and every qualifier | supports | Exact native pathway, local identities, complete chemical sides and bounded contextual claims are supported. |
| inspect | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/final-inspect.json; Fresh native inspect on 39ca1eed at 22f4279d | supports | All reviewed input hashes captured after exact one-line schema repair. |
| schema-fix | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/schema-fix-bridge.json; Byte reconstruction old 2e9b575b to final 39ca1eed | supports | Only references[22].year was removed; all scientific record bytes are unchanged. |
| chemical-replay | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/independent-audit.json; Complete native/Rhea sides, coefficients, directions, chemical InChIs and native assemblies | supports | 55 independent checks pass; RHEA:30033 is right_to_left, all four full equations and exact charged stereochemical identities agree. |
| edge-assessment | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/edge-assessment.json; cat-001 through cat-032 and ten source-to-graph dispositions | supports | All 32 edges and material represented/excluded source facts positively assessed; no new actionable findings. |
| reference-hashes | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/reference-hashes.json; All24 references against complete original bytes | supports | All 23 asserted digests match; PMID:7391022 intentionally has no original PDF digest. |
| authority | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/authority-assessment.json; Old/new term and owner comparison; ten ChEBI 255 semantic identities | supports | Preserves4757 old terms and 742 owners, adding 19 terms and 10 owners; selected formal chemical identities independently inspected. |
| corpus | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/corpus-preservation.json; All 245 baseline YAML byte hashes and246 current record paths | supports | Only the catechol record is added; every baseline record remains byte-identical. |
| imodulondb | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/imodulondb-check.json; p_putida/precise321 catechol search; PP_3166 and PP_3713 | supports | Two annotated gene hits and zero module hits are transcriptomic context, without exact native catalyst or strain equivalence. |
| reading-coverage | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/reading-coverage.json; Personal original-object reading and explicitly attributed contributor coverage | supports | Separates personally inspected sources from full-paper contributor appraisals and unavailable material. |
| visual | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/visual-assessment.json; Styled full SVG raster and exact export replay scope | supports | Reviewer observed no clipped node labels; interactive behavior was not exercised. |
| gate-replay | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/gate-replay.json; Current and historical gate receipt/log hashes | supports | Final required gates bind final 39ca1eed; historical failures remain visible with their old input hashes. |
| dedup | research/pathway_additions/2026-10-14-next-248/catechol/native/fresh-dedup-bridge.json; Precreation native search and baseline inventory | context_only | No pre-existing exact catechol core record was identified; retained DRAM source rows were research leads. |
| native-catalysts | research/pathway_additions/2026-10-14-next-248/catechol/native/provenance-manifest.json; Whole original META-CPLX-2842/2843/2844/2761, MONOMER3422/3423/3424/3221 and ENZRXN3585/3586/3587/3368 XML; exact IDs, species, component coefficients and activity evidence fields | supports | Reviewer independently read all source objects. Native catalyst, 2/8/10/3 component and Mn2+ statements remain database-scoped; no modern protein or gene accession is selected. |
| historical-pcad | https://www.researchgate.net/publication/15808123_Repetitions_in_the_NH2-terminal_amino_acid_sequence_of_b-ketoadipate_enol-lactone_hydrolase_from_Pseudomonas_putida; PMID:7391022 p 6336 trimer discussion; p 6339 bacterial strain/growth; p 6340 mass methods and corresponding captions | supports | Personally inspected bounded rendered text: authors infer a historical trimer from 30–33 kDa whole enzyme and 11 kDa subunit; PRS2260 derives from PRS2178. Urea and denaturation behavior qualify that interpretation. |
| historical-appraisal | research/pathway_additions/2026-10-14-next-248/catechol/primary/1980-historical-hydrolase-claims.json; Bounded primary appraisal, exact locators and unavailable-original statement | supports | Contributor appraisal agrees with personally inspected primary text; no modern Q88N36 sequence equivalence is established. |
| pdb2azq | https://files.rcsb.org/download/2AZQ.cif; _database_2 lines 9–16; _entity_src_nat lines 439–463; _chem_comp FE; _struct_conn metalc1–4; _atom_site FE line 3433; biological assembly 1 and PCF entity 3 | supports | Personally inspected issuing CIF: natural P. putida C-1 model, assigned FE(III), exactly two Tyr/two His metal contacts, unit model occupancy and author/software-defined dimer. PCF is co-bound structural context. |
| fe-identity | https://data.rcsb.org/rest/v1/core/chemcomp/FE; chem_comp.pdbx_formal_charge and rcsb_chem_comp_descriptor; matched ChEBI 255 CHEBI:29034 structure/charge | supports | Deposited component formal charge 3, Fe/q+3 InChI and exact key agree with selected iron(3+). |
| pdb-paper-abstract | https://pubmed.ncbi.nlm.nih.gov/16171781/; Complete PubMed abstract only | context_only | Abstract identifies the C-1 beta-beta isozyme and 2.65 angstrom structure; proposed lipid-mediated activity modulation is not evidence for a particular required physiological lipid cofactor. |
| primary-coverage | research/pathway_additions/2026-10-14-next-248/catechol/primary/reading-coverage.json; 2010 entire-body/8 figures/2 tables/supplement contributor appraisal;1966 and1980 access bounds | context_only | Full 2010 appraisal belongs to /root/next244_primary_evidence. This reviewer independently read selected original text and Figure 1/supplement. Unavailable 1966/1980 material is explicitly listed. |
| a1501 | research/pathway_additions/2026-10-14-next-248/catechol/primary/2010-claims.json; PMID:20137101 A1501 genotype/phenotype scope and HPLC inconsistency | context_only | P. stutzeri A1501 predicted map and mutant experiments do not establish native P. putida catalyst identities. Methods standards and figure peak labels conflict; that conflict is not silently resolved. |
| graph-export | research/pathway_additions/2026-10-14-next-248/catechol/validation/graph-export-replay.json; All 32 KGX rows and SVG evidence links;25 display nodes | supports | Read root-run exact payload replay on final 39ca1eed: descriptions, evidence, endpoint qualifier payloads and full reference metadata preserved. |
| gate-validate | research/pathway_additions/2026-10-14-next-248/catechol/validation/validate.json; Actual command/times/final-input hashes and compressed stdout | supports | Root-run command passed on final 39ca1eed. Reviewer independently verified receipt and decompressed log hashes. |
| gate-test | research/pathway_additions/2026-10-14-next-248/catechol/validation/test.json; Actual command/times/final-input hashes and compressed stdout | supports | Root-run command passed on final 39ca1eed. Reviewer independently verified receipt and decompressed log hashes. |
| gate-render | research/pathway_additions/2026-10-14-next-248/catechol/validation/render.json; Actual command/times/final-input hashes and compressed stdout | supports | Root-run command passed on final 39ca1eed. Reviewer independently verified receipt and decompressed log hashes. |
| gate-kgx | research/pathway_additions/2026-10-14-next-248/catechol/validation/kgx.json; Actual command/times/final-input hashes and compressed stdout | supports | Root-run command passed on final 39ca1eed. Reviewer independently verified receipt and decompressed log hashes. |
| gate-lint | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/lint.json; Actual reviewer-run final-byte command and log hash | supports | Successful reviewer-run current check. |
| gate-diff | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/diff.json; Actual reviewer-run final-byte command and log hash | supports | Successful reviewer-run current check. |
| initial-validate | research/pathway_additions/2026-10-14-next-248/catechol/validation/initial-failed/validate.json; Superseded2e9b575b draft command and retained compressed stdout | context_only | Failed initial draft check is preserved; issue 519 and exact one-line repair are recorded. Required current rerun is separately passed. |
| initial-test | research/pathway_additions/2026-10-14-next-248/catechol/validation/initial-failed/test.json; Superseded2e9b575b draft command and retained compressed stdout | context_only | Failed initial draft check is preserved; issue 519 and exact one-line repair are recorded. Required current rerun is separately passed. |
| initial-lint-cache | research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/lint-initial-cache-failure.json; Initial reviewer invocation before Ruff could start | context_only | UV could not open its default cache under the filesystem sandbox. A writable temporary UV_CACHE_DIR allowed the identical documented lint command to pass. |

## Limits And Additional Notes

- PMID:7391022 was inspected as bounded rendered primary text/captions. Original PDF bytes, original figure pixels and complete miniprint were unavailable. The three 11 kDa-subunit interpretation is a historical inference for the PRS2260 preparation, not a definitive modern Q88N36 assembly or sequence assignment.
- Native purified-protein evidence codes and most assembly/catalyst assertions are verified database statements. This reviewer did not read every underlying historical assay publication in full. Part I 1966 was unavailable; Part III was read only in selected substantive passages.
- Fe(III) is the deposited C-1 PDB 2AZQ model/component assignment, not an independent oxidation-state experiment or universal metal occupancy. The linked 2005 paper was read as an abstract, not its main body. Co-bound PCF remains structural/preparation context without an established particular required physiological cofactor claim.
- The complete 2010 A1501 article/figures/tables appraisal is attributed to /root/next244_primary_evidence. This reviewer independently checked claim-bearing text, Figure 1 and the entire supplement; no P. stutzeri experiment is transferred to P. putida native catalysts. Contradictory HPLC peak labels and standards are retained as a source limitation.
- Whole source originals remain in documented external archives. Repository-retained compact receipts and source hashes do not assure full recovery if those archives disappear. The pinned ChEBI 255 SQL identity rows were read independently, but its whole database digest was not freshly recomputed here.
- Visual QA is a static SVG raster and exact KGX replay. No interactive browser surface was available; dense context edges require zoom or the evidence table.
- The initial inspected draft 2e9b575b failed closed-schema validation because references[22] carried unsupported year: 1980. Issue 519 tracks that genuine unmerged-draft defect. Removing exactly that line yields final 39ca1eed; reinsertion reconstructs the old SHA. The corrected bytes were freshly inspected and scientifically reassessed at unchanged HEAD before save. No fabricated prior structured finding or previous_occurrences is used.
- Initial validation/test failures are preserved as historical checks on the superseded draft; the required current gates are the successful final-byte reruns. An initial reviewer lint attempt failed on a sandbox-inaccessible UV cache before lint ran; retry with writable temporary cache passed.
- All 245 baseline pathway YAMLs remain byte-identical and the candidate is the only added record. All 4757 old authority terms and 742 old owners remain;19 terms and 10 owners were added.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T092123Z-catechol248-scientific
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of catechol degradation to beta-ketoadipate
started_at: '2026-10-14T09:03:38.556929Z'
finished_at: '2026-10-14T09:21:23.210634Z'
reviewer:
  identity: Codex /root/catechol248_independent_review
  kind: agent
  independence: independent
  independence_basis: Did not author or edit the maintained record, chemical grounding,
    source authority union or generated outputs. Original database/authority objects
    and selected primary text were independently inspected; contributor whole-paper
    and technical appraisals are explicitly attributed.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact four-reaction native catechol ortho-cleavage route is supported.
  All 32 edges, 18 participants, four core activities plus a typed downstream interface,
  24 references and all material source-to-graph dispositions were assessed. The final
  corrected record has no unresolved actionable finding. Historical catalyst identities,
  inferred PcaD assembly, model-specific Fe(III), native expression-level induction
  and incomplete primary access remain explicit. All required final validation, test,
  lint and whitespace gates passed.
source:
  git_revision: 22f4279d66ab39cf153a9a1f7333150671d1b17b
  state: working_tree
  inputs:
  - path: conf/identifier_policy.yaml
    sha256: f2991a22f16f0d14d83226c6ac261bc779b253b2547fae9724474d8596b411c7
    role: context
  - path: conf/identifier_sources.json
    sha256: 953f5ef2c11807f29fcfb514e562f0caa1bd9c84a5f15a383c136084487a8b77
    role: context
  - path: conf/record_review.yaml
    sha256: a2d6578719a7d080eadc9520695ea7203618b0a7b274ee78fb25dbc17794876b
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 2eac75a4e02fde3adba995a1f529c84ed024c70d5d03c265904aa0998e36bf86
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: c15c835c2eea90824e96caa659ecf9e7663ddce78bb42c4c84285f7983da48a3
    role: context
  - path: data/pathways/catechol-degradation-to-beta-ketoadipate.yaml
    sha256: 39ca1eedee87cb3ee01d9d698359bdfdee505b1fa05e160154e976fa6514e6c6
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: 4f3f46d1f4b8ebafa9b2d04d9700510df18b6ec6f881856fda521879f494d153
    role: context
  - path: docs/CURATION.md
    sha256: 408f7c7705b4e6d667b513920e4c39612162d549e0c2666d85bfd53b2c2687f7
    role: context
  - path: docs/HARMONIZATION.md
    sha256: 072884773d626ea909bd1e4f275901f0a6053f660d5e68a294ee54149b6496b0
    role: context
  - path: docs/record-review-profile.md
    sha256: f3f00eebb7841e9d5ac891271e269f45e926995e16856b8e9a885436570c7819
    role: context
  - path: src/pathwaymech/schema.py
    sha256: bd99c1e6ca1f6eec5c82c58aa1ae3f43f696d30be66fbe0977dcace81292e0b8
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: c66be7d0ae830e5041608eb6b2ce9755c601ed596ec9df5fb3567d41b202478b
    role: context
scope:
  description: Complete independent scientific review of one maintained next248 catechol
    record, with contextual preservation checks for prior records and authority rows.
  selection: Exact maintained path and MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY identity
    requested by the parent curator; no sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  exclusions:
  - target: Other 245 maintained pathway records
    reason: Their bytes were independently verified unchanged; no fresh scientific
      review is claimed.
  - target: PWY-5417 superpathway, upstream catechol-producing modules and downstream
      PWY-2361 internal reactions
    reason: Outside the exact four-step native pathway. PWY-2361 is represented only
      as a typed material-transfer interface.
  - target: Modern gene/protein sequences and all-strain occurrence
    reason: No exact historical-to-modern sequence identity or universal species occurrence
      is established.
targets:
- target_id: MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  path: data/pathways/catechol-degradation-to-beta-ketoadipate.yaml
  label: catechol degradation to β-ketoadipate
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/catechol-degradation-to-beta-ketoadipate.yaml
    role: maintained pathway record
checks:
- check_id: validate
  name: just validate
  status: passed
  required: true
  summary: Final-byte root-run check passed; log and receipt independently verified.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - gate-validate
  - gate-replay
  command: just validate
  exit_code: 0
  scope_note: Corpus-wide documented command, not a one-record validator.
- check_id: test
  name: just test
  status: passed
  required: true
  summary: Final-byte root-run check passed; log and receipt independently verified.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - gate-test
  - gate-replay
  command: just test
  exit_code: 0
  scope_note: Corpus-wide documented command, not a one-record validator.
- check_id: render
  name: just render-pages
  status: passed
  required: false
  summary: Final-byte root-run check passed; log and receipt independently verified.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - gate-render
  - gate-replay
  command: just render-pages
  exit_code: 0
  scope_note: Corpus-wide documented command, not a one-record validator.
- check_id: kgx
  name: just kgx-export --output-dir /private/tmp/pathwaymech-next-248-kgx
  status: passed
  required: false
  summary: Final-byte root-run check passed; log and receipt independently verified.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - gate-kgx
  - gate-replay
  command: just kgx-export --output-dir /private/tmp/pathwaymech-next-248-kgx
  exit_code: 0
  scope_note: Corpus-wide documented command, not a one-record validator.
- check_id: lint
  name: just lint
  status: passed
  required: true
  summary: Personally executed on final 39ca1eed; exit 0.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - gate-lint
  command: just lint
  exit_code: 0
- check_id: diff
  name: git diff --check
  status: passed
  required: true
  summary: Personally executed on final 39ca1eed; exit 0.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - gate-diff
  command: git diff --check
  exit_code: 0
- check_id: initial-validate
  name: Initial superseded-draft validate
  status: failed
  required: false
  summary: Failure on unsupported year metadata in old 2e9b575b. This is historical,
    not the current required gate.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - initial-validate
  - schema-fix
  command: just validate
  exit_code: 1
  scope_note: Superseded draft only; required final rerun is listed separately.
- check_id: initial-test
  name: Initial superseded-draft test
  status: failed
  required: false
  summary: The old draft had one closed-schema failure and3478 passing tests before
    the run was interrupted. The final-byte complete rerun passed4867 tests with3
    skips; this historical result is not the current required gate.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - initial-test
  - schema-fix
  command: just test
  exit_code: 2
  scope_note: Superseded draft only; required final rerun is listed separately.
- check_id: initial-lint-cache
  name: Initial reviewer lint environment attempt
  status: failed
  required: false
  summary: Environment/cache access failed before Ruff; final required lint retry
    passed.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - initial-lint-cache
  - gate-lint
  command: just lint
  exit_code: 2
- check_id: native-inspect
  name: Fresh native inspect after schema repair
  status: passed
  required: false
  summary: Exact final input bytes captured and change reassessed at unchanged HEAD.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - inspect
  - schema-fix
  command: scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-248-independent-20261014/targets.json
    with declared context inputs
  exit_code: 0
- check_id: scientific-edges
  name: Full source-to-graph and graph-to-source assessment
  status: passed
  required: false
  summary: All 32 edges, all record fields and10 material source-fact dispositions
    independently assessed.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - edge-assessment
  - reading-coverage
- check_id: chemical-replay
  name: Independent complete chemistry and native assembly replay
  status: passed
  required: false
  summary: 55 original-object checks pass.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - chemical-replay
  command: python -B /private/tmp/pathwaymech-next-248-independent-20261014/independent-audit.py
  exit_code: 0
- check_id: reference-hashes
  name: Complete original reference digest verification
  status: passed
  required: false
  summary: 23 of 23 asserted hashes match; intentionally unhashed paper is disclosed.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - reference-hashes
- check_id: imodulondb
  name: Structured adapter datasets and catechol search
  status: passed
  required: false
  summary: Two actual commands passed; zero module hits means summarize is not applicable.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - imodulondb
  command: kg-microbe-sources imodulondb --timeout 30 datasets; kg-microbe-sources
    imodulondb --timeout 30 search --organism p_putida --dataset precise321 --query
    catechol
  exit_code: 0
- check_id: static-graph
  name: Static graph and exact export review
  status: passed
  required: false
  summary: Reviewer viewed full raster and read exact32-edge export replay; interactive
    browser unavailable.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - visual
  - graph-export
evidence:
- evidence_id: record
  kind: record_content
  reference: data/pathways/catechol-degradation-to-beta-ketoadipate.yaml
  locator: Entire final record, all 32 edges and every qualifier
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Exact native pathway, local identities, complete chemical sides and bounded
    contextual claims are supported.
  snapshot_sha256: 39ca1eedee87cb3ee01d9d698359bdfdee505b1fa05e160154e976fa6514e6c6
- evidence_id: inspect
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/final-inspect.json
  locator: Fresh native inspect on 39ca1eed at 22f4279d
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: All reviewed input hashes captured after exact one-line schema repair.
  snapshot_sha256: 82707d8b0df539485523e069dfed959ef2a396bb3e2b4b3bd867ad951482b1d5
- evidence_id: schema-fix
  kind: record_content
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/schema-fix-bridge.json
  locator: Byte reconstruction old 2e9b575b to final 39ca1eed
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Only references[22].year was removed; all scientific record bytes are unchanged.
  snapshot_sha256: b9dfa69085e4793c87b6a7218cd70b922e5112e8c57b1a56d10b2c300b817f95
- evidence_id: chemical-replay
  kind: authority
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/independent-audit.json
  locator: Complete native/Rhea sides, coefficients, directions, chemical InChIs and
    native assemblies
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: 55 independent checks pass; RHEA:30033 is right_to_left, all four full
    equations and exact charged stereochemical identities agree.
  snapshot_sha256: 2b7b21a215b3106e9c9558122aaf43bd4f0c89f67f3f957a23f985877b816490
- evidence_id: edge-assessment
  kind: record_content
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/edge-assessment.json
  locator: cat-001 through cat-032 and ten source-to-graph dispositions
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: All 32 edges and material represented/excluded source facts positively
    assessed; no new actionable findings.
  snapshot_sha256: cd5ccbd454bedd24346bdea4bf071b412645d0a3b3d73dfd1b08f1ae38624bb3
- evidence_id: reference-hashes
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/reference-hashes.json
  locator: All24 references against complete original bytes
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: All 23 asserted digests match; PMID:7391022 intentionally has no original
    PDF digest.
  snapshot_sha256: b781f9f9d04ba0a31ed4fda55da3a32fcd5a8f278515bdf91a8233afeeeace0d
- evidence_id: authority
  kind: authority
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/authority-assessment.json
  locator: Old/new term and owner comparison; ten ChEBI 255 semantic identities
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Preserves4757 old terms and 742 owners, adding 19 terms and 10 owners;
    selected formal chemical identities independently inspected.
  snapshot_sha256: 8a12b4312f930af74d568864dff610d319b150495b2ccd9ab4f3c0cc83cd3bb3
- evidence_id: corpus
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/corpus-preservation.json
  locator: All 245 baseline YAML byte hashes and246 current record paths
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Only the catechol record is added; every baseline record remains byte-identical.
  snapshot_sha256: fb939c2178d2a49e10005d26b1a3a1d81efe76e585d1cf510a951abb510ca3fd
- evidence_id: imodulondb
  kind: database
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/imodulondb-check.json
  locator: p_putida/precise321 catechol search; PP_3166 and PP_3713
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Two annotated gene hits and zero module hits are transcriptomic context,
    without exact native catalyst or strain equivalence.
  snapshot_sha256: 0b49a6240d2381dae320ddde383e1f0a7b6a4b0e3f4eb64a09e9e5ce85019569
- evidence_id: reading-coverage
  kind: record_content
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/reading-coverage.json
  locator: Personal original-object reading and explicitly attributed contributor
    coverage
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Separates personally inspected sources from full-paper contributor appraisals
    and unavailable material.
  snapshot_sha256: 8f2e7a973855ff6b8865eb02a28c55cc389e8926d7465d99dcd68f91205be7e8
- evidence_id: visual
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/visual-assessment.json
  locator: Styled full SVG raster and exact export replay scope
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Reviewer observed no clipped node labels; interactive behavior was not
    exercised.
  snapshot_sha256: 9c9459267509cf9063a73d517a2a912f5269ea8874b18d7f9850182cb1d4b565
- evidence_id: gate-replay
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/gate-replay.json
  locator: Current and historical gate receipt/log hashes
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Final required gates bind final 39ca1eed; historical failures remain visible
    with their old input hashes.
  snapshot_sha256: 393170b7ecf1d848a0b340c14b916e4ba0cfeb1980c95165c9d68d8230d12079
- evidence_id: dedup
  kind: search
  reference: research/pathway_additions/2026-10-14-next-248/catechol/native/fresh-dedup-bridge.json
  locator: Precreation native search and baseline inventory
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: context_only
  summary: No pre-existing exact catechol core record was identified; retained DRAM
    source rows were research leads.
  snapshot_sha256: 3f9b7e15f335e1384ee120aded65f355385bb89dd3f97ea42b9a842ca348b9f6
  search_scope: Precreation rg --no-ignore --hidden searches included ignored and
    hidden files over the original worktree for pathway identity/label and related
    reaction identifiers, plus parsed baseline 245 YAML inventory. Compressed interiors,
    symlink-directory traversal and live GitHub issue bodies were not included; no
    biological absence claim follows.
- evidence_id: native-catalysts
  kind: database
  reference: research/pathway_additions/2026-10-14-next-248/catechol/native/provenance-manifest.json
  locator: Whole original META-CPLX-2842/2843/2844/2761, MONOMER3422/3423/3424/3221
    and ENZRXN3585/3586/3587/3368 XML; exact IDs, species, component coefficients
    and activity evidence fields
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Reviewer independently read all source objects. Native catalyst, 2/8/10/3
    component and Mn2+ statements remain database-scoped; no modern protein or gene
    accession is selected.
  snapshot_sha256: adc7fbb83c4e3224e4358f9b85a5bdbd3aa511c49edca6d4388805a1662cc3ad
- evidence_id: historical-pcad
  kind: primary_source
  reference: https://www.researchgate.net/publication/15808123_Repetitions_in_the_NH2-terminal_amino_acid_sequence_of_b-ketoadipate_enol-lactone_hydrolase_from_Pseudomonas_putida
  locator: PMID:7391022 p 6336 trimer discussion; p 6339 bacterial strain/growth;
    p 6340 mass methods and corresponding captions
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: 'Personally inspected bounded rendered text: authors infer a historical
    trimer from 30–33 kDa whole enzyme and 11 kDa subunit; PRS2260 derives from PRS2178.
    Urea and denaturation behavior qualify that interpretation.'
  quote: a trimer formed by the association of identical subunits.
- evidence_id: historical-appraisal
  kind: primary_source
  reference: research/pathway_additions/2026-10-14-next-248/catechol/primary/1980-historical-hydrolase-claims.json
  locator: Bounded primary appraisal, exact locators and unavailable-original statement
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Contributor appraisal agrees with personally inspected primary text; no
    modern Q88N36 sequence equivalence is established.
  snapshot_sha256: f790c8b3e6c1215236873ea5cd066578ca432f211572304719bd93e4bf6fb8dd
- evidence_id: pdb2azq
  kind: database
  reference: https://files.rcsb.org/download/2AZQ.cif
  locator: _database_2 lines 9–16; _entity_src_nat lines 439–463; _chem_comp FE; _struct_conn
    metalc1–4; _atom_site FE line 3433; biological assembly 1 and PCF entity 3
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: 'Personally inspected issuing CIF: natural P. putida C-1 model, assigned
    FE(III), exactly two Tyr/two His metal contacts, unit model occupancy and author/software-defined
    dimer. PCF is co-bound structural context.'
  snapshot_sha256: 70af6472fde390809bea8d1144a153289f902a413ca9000df4e0efd4dd530766
- evidence_id: fe-identity
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/chemcomp/FE
  locator: chem_comp.pdbx_formal_charge and rcsb_chem_comp_descriptor; matched ChEBI
    255 CHEBI:29034 structure/charge
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Deposited component formal charge 3, Fe/q+3 InChI and exact key agree with
    selected iron(3+).
  snapshot_sha256: c42687f697be80e07b6e92ea9996f68938ff2c04c177b628664510437828d272
- evidence_id: pdb-paper-abstract
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/16171781/
  locator: Complete PubMed abstract only
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: context_only
  summary: Abstract identifies the C-1 beta-beta isozyme and 2.65 angstrom structure;
    proposed lipid-mediated activity modulation is not evidence for a particular required
    physiological lipid cofactor.
  snapshot_sha256: 4bb13662dbc8ab93508137b4522acf68ea65062272fa13b3c6ef6317c573c442
- evidence_id: primary-coverage
  kind: primary_source
  reference: research/pathway_additions/2026-10-14-next-248/catechol/primary/reading-coverage.json
  locator: 2010 entire-body/8 figures/2 tables/supplement contributor appraisal;1966
    and1980 access bounds
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: context_only
  summary: Full 2010 appraisal belongs to /root/next244_primary_evidence. This reviewer
    independently read selected original text and Figure 1/supplement. Unavailable
    1966/1980 material is explicitly listed.
  snapshot_sha256: 507a2c5d7aaf13e109ae48ef18a18d01e2a23d099573c94fafc238c2e6059a89
- evidence_id: a1501
  kind: primary_source
  reference: research/pathway_additions/2026-10-14-next-248/catechol/primary/2010-claims.json
  locator: PMID:20137101 A1501 genotype/phenotype scope and HPLC inconsistency
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: context_only
  summary: P. stutzeri A1501 predicted map and mutant experiments do not establish
    native P. putida catalyst identities. Methods standards and figure peak labels
    conflict; that conflict is not silently resolved.
  snapshot_sha256: f9d23ff92548149c083397e1e19eef8f12d4636a86ee24e5860a532b3c378320
- evidence_id: graph-export
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/validation/graph-export-replay.json
  locator: All 32 KGX rows and SVG evidence links;25 display nodes
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: 'Read root-run exact payload replay on final 39ca1eed: descriptions, evidence,
    endpoint qualifier payloads and full reference metadata preserved.'
  snapshot_sha256: d68bbf2dce259ec3ac5c1f3e6d9e2bf6e06d036789b1d7d3a0dbb51896c8db38
- evidence_id: gate-validate
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/validation/validate.json
  locator: Actual command/times/final-input hashes and compressed stdout
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Root-run command passed on final 39ca1eed. Reviewer independently verified
    receipt and decompressed log hashes.
  snapshot_sha256: d6373b4f0d21c36754e38ec32eb567e90aaa1faeabcfc55e9257c2409d4f1ec7
- evidence_id: gate-test
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/validation/test.json
  locator: Actual command/times/final-input hashes and compressed stdout
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Root-run command passed on final 39ca1eed. Reviewer independently verified
    receipt and decompressed log hashes.
  snapshot_sha256: 64a0ee75a31272adb9f7b20054c71100690c4df2d69947064f29f5f3bcdf8f14
- evidence_id: gate-render
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/validation/render.json
  locator: Actual command/times/final-input hashes and compressed stdout
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Root-run command passed on final 39ca1eed. Reviewer independently verified
    receipt and decompressed log hashes.
  snapshot_sha256: 26dbeac4ec0b4d4f29ecbc63a0bc2667a62081afe34b4fac7f16e19a2b2613d3
- evidence_id: gate-kgx
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/validation/kgx.json
  locator: Actual command/times/final-input hashes and compressed stdout
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Root-run command passed on final 39ca1eed. Reviewer independently verified
    receipt and decompressed log hashes.
  snapshot_sha256: 4f2cbf84d024d7321769659220b4646aadf34700150ecc3488bb7784c47c99b0
- evidence_id: gate-lint
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/lint.json
  locator: Actual reviewer-run final-byte command and log hash
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Successful reviewer-run current check.
  snapshot_sha256: 451cf207e26539071cd0ed11040ba6c66a800350ed2f05302ad5f067e38a8247
- evidence_id: gate-diff
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/diff.json
  locator: Actual reviewer-run final-byte command and log hash
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: supports
  summary: Successful reviewer-run current check.
  snapshot_sha256: ec82cfc8830948308dc21f5a349289a1c115ba75f6d398682be975a58363821b
- evidence_id: initial-validate
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/validation/initial-failed/validate.json
  locator: Superseded2e9b575b draft command and retained compressed stdout
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: context_only
  summary: Failed initial draft check is preserved; issue 519 and exact one-line repair
    are recorded. Required current rerun is separately passed.
  snapshot_sha256: 6febc62b187f4069272c6ce5fc1b54eb20ff381a548302be90b587c3b0335282
- evidence_id: initial-test
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/validation/initial-failed/test.json
  locator: Superseded2e9b575b draft command and retained compressed stdout
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: context_only
  summary: Failed initial draft check is preserved; issue 519 and exact one-line repair
    are recorded. Required current rerun is separately passed.
  snapshot_sha256: 4b8894fe5161e01ac27a520cdc9229403b6e1e49fc3a381a8d5cfc217b8eec06
- evidence_id: initial-lint-cache
  kind: validation
  reference: research/pathway_additions/2026-10-14-next-248/catechol/independent-scientific-audit/lint-initial-cache-failure.json
  locator: Initial reviewer invocation before Ruff could start
  accessed_at: '2026-10-14T09:21:23.210634Z'
  support: context_only
  summary: UV could not open its default cache under the filesystem sandbox. A writable
    temporary UV_CACHE_DIR allowed the identical documented lint command to pass.
  snapshot_sha256: 93e26ba56c1ea9672a096c9dc014f970b01d0a932b9cd546112a966749b2fd70
assessments:
- assessment_id: identity
  area: identity
  topic: Exact native pathway and downstream boundary
  outcome: supported
  summary: The four-reaction CATECHOL-ORTHO-CLEAVAGE-PWY ends at 3-oxoadipate. PWY-2361
    receives that material as an explicitly typed interface; its CoA-transfer/thiolysis
    reactions are outside the core. The larger PWY-5417 is not conflated with this
    pathway.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - record
  - chemical-replay
  - dedup
  - edge-assessment
- assessment_id: chemistry
  area: grounding
  topic: Complete sides, coefficients, charge and stereochemistry
  outcome: supported
  summary: All four complete native/Rhea reactions agree, including oxygen, water
    and hydrons. RHEA:30033 source direction is right_to_left. Exact S-muconolactone
    is retained; a broader stereounspecified alternative is not silently equated.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - chemical-replay
  - authority
  - edge-assessment
  dimensions:
  - name: source_object
    value: Whole MetaCyc 27.0 XML, Rhea 142 aggregated RDF and ChEBI 255 SQL chemical
      identities.
    definition: Original-object inspection and exact structural identity rather than
      cross-reference plausibility.
    evidence_ids:
    - chemical-replay
    - authority
- assessment_id: native-catalysts
  area: evidence
  topic: Database-scoped native catalysts and component roles
  outcome: supported
  summary: All four enzymatic-reaction assignments and their species/component fields
    are supported by exact native objects. Generic CatA two-subunit wording does not
    imply all three C-1 isozyme variants are homodimers. Deleted Q9AEQ0 and modern
    Q88N36 are not selected identities.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - native-catalysts
  - record
  - edge-assessment
  dimensions:
  - name: component_role
    value: Four complexes and four component frames; Mn2+ and qualified Fe3+ cofactors;
      PWY-2361 process interface.
    definition: Proteins, assemblies, chemicals and pathway context remain distinct
      roles.
    evidence_ids:
    - record
    - edge-assessment
  - name: evidence_tier
    value: Native EV-EXP-IDA-PURIFIED-PROTEIN is a database evidence assignment; the
      historical trimer is an author inference; Fe3+ is a deposited model assignment.
    definition: Preserves the kind and scope of support instead of upgrading database
      or model statements to new assay proof.
    evidence_ids:
    - native-catalysts
    - historical-pcad
    - pdb2azq
- assessment_id: historical-pcad
  area: evidence
  topic: Historical hydrolase preparation and inferred trimer
  outcome: supported
  summary: The recorded three 11 kDa-subunit interpretation faithfully reflects the
    1980 inference and native component coefficient. PRS2260 preparation and denaturation
    dependence are explicit. Purifying an unmodified cellular enzyme does not itself
    establish an engineered protein construct; no modern sequence or definitive structural
    claim is made.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - historical-pcad
  - historical-appraisal
  - record
  dimensions:
  - name: taxon_condition
    value: Native species 303; historical PRS2260 derivative ofPRS2178; separate natural
      C-1 structural model.
    definition: Historical preparation and structural specimen are retained without
      all-strain or modern-sequence extrapolation.
    evidence_ids:
    - historical-pcad
    - pdb2azq
    - record
- assessment_id: metals
  area: evidence
  topic: Mn2+ native cofactor and scoped modeled Fe3+
  outcome: supported
  summary: Native Mn2+ cofactor fields support cat-029. The issuing PDB 2AZQ CIF and
    exact FE chemical identity support cat-032 only in its C-1 molecular-state scope,
    with two Tyr/two His metal contacts and explicit model-assigned oxidation state.
    PCF binding does not establish a particular necessary physiological cofactor.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - native-catalysts
  - pdb2azq
  - fe-identity
  - pdb-paper-abstract
  - edge-assessment
- assessment_id: induction
  area: graph
  topic: Expression-level hydrolase induction
  outcome: supported
  summary: The native CPLX-2761 comment supports 3-oxoadipate induction. The generic
    regulates edge and explicit expression-level description avoid inventing direct
    ligand binding, catalytic activation or a regulator gene.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - native-catalysts
  - edge-assessment
  - record
- assessment_id: coverage
  area: completeness
  topic: Material source-to-graph accounting
  outcome: supported
  summary: All core chemical and catalyst facts are represented. Neighboring modules,
    a Cupriavidus dechlorination example, modern sequence joins, PCF physiological
    necessity and 2010 A1501 experiments have explicit bounded exclusion reasons.
    The HPLC conflict is preserved rather than used to strengthen the pathway.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - edge-assessment
  - primary-coverage
  - a1501
  - reading-coverage
- assessment_id: provenance
  area: provenance
  topic: Exact original bindings and preserved authority/corpus context
  outcome: supported
  summary: All asserted reference hashes match complete original files. The one unhashed
    primary citation accurately reports its access limits. Source-local assertions,
    authority preservation and all 245 baseline record hashes are verified.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - reference-hashes
  - authority
  - corpus
  - reading-coverage
- assessment_id: expression-context
  area: scope
  topic: Structured iModulonDB cross-check
  outcome: supported
  summary: Two catechol dioxygenase gene annotations in p_putida/precise321 supply
    bounded context; they do not establish historical catalyst sequence identity.
    Zero module hits is a query result, not negative biological evidence.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - imodulondb
- assessment_id: representation
  area: representation
  topic: Graph evidence and qualifier preservation
  outcome: supported
  summary: All 32 exported edges retain exact descriptions, evidence, endpoint qualifiers
    and full references. The separate C-1 model node and downstream pathway context
    are visible in static rendering. Interactive behavior remains untested.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - graph-export
  - visual
  - record
- assessment_id: technical
  area: schema
  topic: Final technical gates and repaired draft schema
  outcome: supported
  summary: The unsupported reference year field was removed without changing any scientific
    claim. Final-byte validation, full tests, lint and whitespace checks passed. Historical
    failures and environment retry remain preserved, with exact input scopes.
  target_ids:
  - MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY
  evidence_ids:
  - schema-fix
  - inspect
  - gate-replay
  - gate-validate
  - gate-test
  - gate-lint
  - gate-diff
findings: []
actions: []
limitations:
- PMID:7391022 was inspected as bounded rendered primary text/captions. Original PDF
  bytes, original figure pixels and complete miniprint were unavailable. The three
  11 kDa-subunit interpretation is a historical inference for the PRS2260 preparation,
  not a definitive modern Q88N36 assembly or sequence assignment.
- Native purified-protein evidence codes and most assembly/catalyst assertions are
  verified database statements. This reviewer did not read every underlying historical
  assay publication in full. Part I 1966 was unavailable; Part III was read only in
  selected substantive passages.
- Fe(III) is the deposited C-1 PDB 2AZQ model/component assignment, not an independent
  oxidation-state experiment or universal metal occupancy. The linked 2005 paper was
  read as an abstract, not its main body. Co-bound PCF remains structural/preparation
  context without an established particular required physiological cofactor claim.
- The complete 2010 A1501 article/figures/tables appraisal is attributed to /root/next244_primary_evidence.
  This reviewer independently checked claim-bearing text, Figure 1 and the entire
  supplement; no P. stutzeri experiment is transferred to P. putida native catalysts.
  Contradictory HPLC peak labels and standards are retained as a source limitation.
- Whole source originals remain in documented external archives. Repository-retained
  compact receipts and source hashes do not assure full recovery if those archives
  disappear. The pinned ChEBI 255 SQL identity rows were read independently, but its
  whole database digest was not freshly recomputed here.
- Visual QA is a static SVG raster and exact KGX replay. No interactive browser surface
  was available; dense context edges require zoom or the evidence table.
notes:
- 'The initial inspected draft 2e9b575b failed closed-schema validation because references[22]
  carried unsupported year: 1980. Issue 519 tracks that genuine unmerged-draft defect.
  Removing exactly that line yields final 39ca1eed; reinsertion reconstructs the old
  SHA. The corrected bytes were freshly inspected and scientifically reassessed at
  unchanged HEAD before save. No fabricated prior structured finding or previous_occurrences
  is used.'
- Initial validation/test failures are preserved as historical checks on the superseded
  draft; the required current gates are the successful final-byte reruns. An initial
  reviewer lint attempt failed on a sandbox-inaccessible UV cache before lint ran;
  retry with writable temporary cache passed.
- All 245 baseline pathway YAMLs remain byte-identical and the candidate is the only
  added record. All 4757 old authority terms and 742 old owners remain;19 terms and
  10 owners were added.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/519
tags:
- catechol
- ortho-cleavage
- scientific-review
```

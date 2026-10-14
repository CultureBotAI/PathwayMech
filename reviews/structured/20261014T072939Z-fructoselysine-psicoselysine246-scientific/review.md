# Independent scientific review of fructoselysine and psicoselysine degradation

- Review: 20261014T072939Z-fructoselysine-psicoselysine246-scientific
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-14T07:08:24.409943Z
- Finished UTC: 2026-10-14T07:29:39.291194Z
- Reviewer: Codex /root/ascorbate244_pr_review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All fields and35 edges of exact3e5b25fc were scientifically assessed. No new actionable defect was found. Exact native chemistry, bounded recombinant constructs and appropriately qualified regulatory inference are supported. All required gates passed on unchanged final record bytes.

## Scope And Provenance

One complete maintained pathway and its source-linked graph.

Selection: Exact final integrated3e5b25fc candidate requested for independent adversarial scientific review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4d0546f17b4a554322a0b38f8d689d5b77a1e3c8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY0-521 | data/pathways/fructoselysine-and-psicoselysine-degradation.yaml | maintained | fructoselysine and psicoselysine degradation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native pre-assessment inspection | passed | True | MetaCyc:PWY0-521 | Actual initial native inspect succeeded before assessment. |
| Final authority native inspection | passed | False | MetaCyc:PWY0-521 | Final authority files were inspected as added context; no existing inspected bytes changed. |
| Complete source-to-graph assessment | passed | False | MetaCyc:PWY0-521 | All35 edge objects and all remaining record fields independently assessed. |
| Contributor generated-output audit | passed | False | MetaCyc:PWY0-521 | Read the separate passing static graph/evidence/export audit; browser interaction was not exercised. |
| Reference original digest replay | passed | False | MetaCyc:PWY0-521 | All29 asserted digests verified; one intentionally unhashed complete-paper citation. |
| Structured iModulonDB cross-check | passed | False | MetaCyc:PWY0-521 | Both actual adapter commands succeeded; zero module hits makes summarize not applicable. |
| just render-pages | passed | False | MetaCyc:PWY0-521 | Actual root-run command passed on the unchanged final target; this reviewer verified retained receipt/log hashes and read its completion output. |
| just kgx-export | passed | False | MetaCyc:PWY0-521 | Actual root-run command passed on the unchanged final target; this reviewer verified retained receipt/log hashes and read its completion output. |
| just lint | passed | True | MetaCyc:PWY0-521 | Actual root-run command passed on the unchanged final target; this reviewer verified retained receipt/log hashes and read its completion output. |
| just validate | passed | True | MetaCyc:PWY0-521 | Actual root-run command passed on the unchanged final target; this reviewer verified retained receipt/log hashes and read its completion output. |
| just test | passed | True | MetaCyc:PWY0-521 | Actual root-run command passed on the unchanged final target; this reviewer verified retained receipt/log hashes and read its completion output. |
| git diff --check | passed | True | MetaCyc:PWY0-521 | Actual focused formatting check passed. |

## Scientific And Domain Assessments

### Native pathway boundary

identity: supported. Targets: MetaCyc:PWY0-521.

The three-reaction PWY0-521 adds upstream psicoselysine epimerization to the existing explicitly narrower GO1901281 pathway. Identity and graph boundary are supported without treating different prefixes as novelty.

### Exact structures, complete sides and direction

grounding: supported. Targets: MetaCyc:PWY0-521.

All core structures retain native charge and stereochemistry; first two Rhea directional IDs match complete sides, including ATP/ADP/H+. Native RXN0-963 preserves beta-G6P and source generality is not forced into a broader Rhea identifier. Source reversibility and chosen pathway direction remain distinct.

### FrlC catalysis, constructs and metals

evidence: supported. Targets: MetaCyc:PWY0-521.

Reversible biochemical conversion supports the epimerization event. The printed sequence discrepancy, donor-strain discrepancy, inferred octamer, extract metal assay and alternative-metal scope remain explicit; zinc inhibition is not generalized to physiology.

### FrlD and FrlB primary activity

evidence: supported. Targets: MetaCyc:PWY0-521.

Recombinant catalytic and inhibitor observations support the qualified edges. Experimental preparations and analytical limitations are retained separately from native database chemistry.

### Transporter participation inference

evidence: supported. Targets: MetaCyc:PWY0-521.

FrlA enables is supported only as qualified pathway participation from phenotype plus probable annotation; no direct transport measurement, coupling, complementation or polarity exclusion is invented.

### Regulatory context and evidence tiers

graph: supported. Targets: MetaCyc:PWY0-521.

FrlR reporter repression and purified operator binding remain separate; RpoH overexpression supports expression activation. CRP is explicitly inferred from cyaA/glucose/promoter experiments. No direct CRP binding, FrlR autoregulation, native gene-specific transcript or host-adaptation experiment is asserted.

### Source-local evidence and original bindings

provenance: supported. Targets: MetaCyc:PWY0-521.

All cited asserted digests match original bytes; source assertions are local to their exact cited objects. Issue514 was repaired before native inspection and has no fabricated formal predecessor. Authority additions preserve all prior terms and owners.

### Bounded transcriptomic cross-check

scope: supported. Targets: MetaCyc:PWY0-521.

The structured adapter returns the expected five frl genes in precise_mg1655. Zero module hits is a query result, not evidence against regulation or pathway activity.

### Qualified graph export

representation: supported. Targets: MetaCyc:PWY0-521.

The contributor technical audit retains all35 evidence-bearing edges and14 endpoint qualifiers, correct local roles and all prior KGX contexts. This supports static generated representation within the disclosed lack of interactive browser testing.

### Documented technical gates

schema: supported. Targets: MetaCyc:PWY0-521.

Required gates are reported using actual input-bound receipts; scientific support is assessed independently of deterministic validation. All required validation, test, lint and formatting gates passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| initial-inspect | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/initial-inspect.json; Complete retained receipt; exact frozen target3e5b25fc | supports | Actual native inspection preceded assessment on exact3e5b25fc and base4d0546; initial input hashes remain unchanged. |
| authority-inspect | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/supplemental-authority-inspect.json; Complete retained receipt; exact frozen target3e5b25fc | supports | Actual supplemental native inspection binds finalized authority owners and unchanged adjacent GO record; every initial context hash is preserved. |
| edge-assessment | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/edge-assessment.json; Complete retained receipt; exact frozen target3e5b25fc | supports | Every complete edge, endpoint qualifier and evidence locator was assessed against its cited original; no new actionable defect found. |
| reference-hashes | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/reference-hashes.json; Complete retained receipt; exact frozen target3e5b25fc | supports | All29 asserted reference digests match complete retained originals. PMID12147680 intentionally has no original digest; no derived text is mislabelled as PDF bytes. |
| reading-coverage | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/reading-coverage.json; Complete retained receipt; exact frozen target3e5b25fc | supports | Separates personally inspected source text and figure pixels from the full2020 appraisal contributed by the primary-evidence agent. |
| authority-assessment | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/authority-assessment.json; Complete retained receipt; exact frozen target3e5b25fc | supports | All4747 existing authority terms and738 owners retain parsed identity;10new terms and4new owners support the current record. The adjacent GO record remains byte-identical. |
| diff-check | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/diff-check.json; Complete retained receipt; exact frozen target3e5b25fc | supports | Actual focused git diff --check passed on the frozen target. |
| rhea-alternatives | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/rhea-exact-alternative-search.json; Complete retained receipt; exact frozen target3e5b25fc | supports | Complete pinned Rhea142 aggregate scan finds no exact beta-product alternative for the deglycase; broad Rhea28383 is not silently substituted. |
| dedup-bridge | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/post-draft-dedup-bridge.json; Complete retained receipt; exact frozen target3e5b25fc | context_only | Connects the precreation hidden/ignored-inclusive search to the subsequent candidate: all244 prior records unchanged, exactly one newly added pathway. |
| imodulondb | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/imodulondb-check.json; Complete retained receipt; exact frozen target3e5b25fc | context_only | Actual structured adapter datasets and frl search succeeded; five expected gene hits and no module hit in precise_mg1655. No absence-based conclusion. |
| record | data/pathways/fructoselysine-and-psicoselysine-degradation.yaml; Entire record; all35 edges and endpoint qualifiers | supports | Exact three-event native route, qualified primary experiments and process-level regulatory context are supported within stated limitations. |
| identity | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/identity-audit/chemical-identity-closure.json; Whole native27.0 compounds and reactions; complete formal Rhea142 substrate/product/contains1/compound/chebi traversal; ChEBI255 structural fields | supports | All nine core native chemical structures match exact charged ChEBI forms. The first two selected directional Rhea reactions are exact; native beta-G6P makes the third reaction narrower than Rhea28383. |
| dedup | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/identity-audit/fresh-dedup-audit.json; Precreation search including hidden and ignored files and parsed inventory of244 maintained records | context_only | PWY0-521 is absent before creation; the existing GO1901281 record is the explicitly narrower two-step route and excludes upstream FrlC. |
| draft-repair | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/author/issue-514-independent-disposition.json; Bounded pre-formal draft comparison3ff91bc5 to8dcfa98b; six source_assertion fields | supports | The source-local provenance defect tracked in issue514 was independently confirmed repaired before promoted native inspection; every other parsed draft field was unchanged. |
| frlc2004 | https://research.dial.uclouvain.be/bitstreams/d9a57554-ce88-46e1-af66-9d66e5795925/download; Complete printed1047-1052; Figures1-5; cloning and assays; Fig4 reversible conversion; Fig2 metal tests | supports | Direct reversible conversion and bounded metal/phenotype observations support FrlC catalysis and qualified FrlA participation; exact printed275-aa construct differs from current276-aa entry. |
| enzymes2002 | https://www.researchgate.net/profile/Elsa-Wiame/publication/11234416_Wiame_E_Delpierre_G_Collard_F_Van_Schaftingen_E_Identification_of_a_pathway_for_the_utilization_of_the_Amadori_product_fructoselysine_in_Escherichia_coli_J_Biol_Chem_277_42523-42529/links/566962a108aea0892c4992aa/Wiame-E-Delpierre-G-Collard-F-Van-Schaftingen-E-Identification-of-a-pathway-for-the-utilization-of-the-Amadori-product-fructoselysine-in-Escherichia-coli-J-Biol-Chem-277-42523-42529.pdf; Printed42523-42529 complete web-reader text; characterization sections, Figs5-8 and captions | supports | Supports qualified recombinant kinase/deglycase activity and zinc inhibition. The G6P product assay does not establish beta-anomer specificity. |
| regulation2020 | https://edoc.ub.uni-muenchen.de/28034/7/Koller_Franziska.pdf; Thesis PDF85-100 contains article; claim-bearing PDF89-93/97-98, Figs5b-d and7, Methods4.5-4.9 | supports | Reporter and operator-binding evidence support scoped FrlR and RpoH regulation; CRP remains an inference from cAMP manipulation/promoter architecture, not direct CRP perturbation or binding. |
| appraisal2020 | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/reading/2020/claims.json; Complete16-page article appraisal and Figures1-9 by /root/next244_primary_evidence; supplement access exclusions | supports | Independent whole-article appraisal supports the included regulatory claims and identifies explicit construct, glucose-concentration, binding and strain limits. |
| appraisal2002 | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/reading/2002/claims.json; Complete seven-page primary appraisal; original-access limitations | supports | Confirms biochemical and construct scope; figure pixels and original PDF bytes were not retained. |
| frlc-sequence | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/reading/2004/frlc-sequence-comparison.json; Manual Figure1 sequence transcription versus complete current UniProt P45541 | supports | Printed275 residues match current first275; current terminalArg276 is not in the experimental sequence depiction. |
| protein-identities | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/identity-authorities/protein-original-bindings.json; Complete current reviewed UniProt original JSON bindings | supports | Protein labels, entry/sequence versions and evidence scope retain reviewed K12 identity without asserting exact experimental insert equivalence. |
| technical-output | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/identity-authorities/technical-audit.json; Static HTML/SVG, all35 exported edges,14 endpoint qualifiers, existing KGX rows/contexts and authority preservation | supports | Read the separate technical audit by /root/next244_source_coverage, who also prepared authority inputs. It finds no defects and preserves all prior graph context; this reviewer does not claim to have rerun that audit or exercised a browser. |
| integration-bridge | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/integrated-draft-bridge.json; Complete retained receipt; exact frozen target3e5b25fc | supports | The first28 complete edge objects are parsed-identical to the repaired preintegration draft. Seven new edges and their added identities/references received fresh scientific assessment. |
| gate-render | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/validation/20261014T070954Z-render.json; Actual command, start/finish, target SHA and complete compressed stdout binding | supports | Root-run render passed on unchanged3e5b25fc. Receipt, compressed hash and decompressed stdout hash independently verified. |
| gate-kgx | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/validation/20261014T070954Z-kgx.json; Actual command, start/finish, target SHA and complete compressed stdout binding | supports | Root-run kgx passed on unchanged3e5b25fc. Receipt, compressed hash and decompressed stdout hash independently verified. |
| gate-lint | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/validation/20261014T071008Z-lint.json; Actual command, start/finish, target SHA and complete compressed stdout binding | supports | Root-run lint passed on unchanged3e5b25fc. Receipt, compressed hash and decompressed stdout hash independently verified. |
| gate-validate | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/validation/20261014T071452Z-validate.json; Actual command, start/finish, target SHA and complete compressed stdout binding | supports | Root-run validate passed on unchanged3e5b25fc. Receipt, compressed hash and decompressed stdout hash independently verified. |
| gate-test | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/validation/20261014T071452Z-test.json; Actual command, start/finish, target SHA and complete compressed stdout binding | supports | Root-run test passed on unchanged3e5b25fc. Receipt, compressed hash and decompressed stdout hash independently verified. |
| gate-replay | research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/gate-replay.json; Complete retained receipt; exact frozen target3e5b25fc | supports | Independently recomputed all available compressed and decompressed gate log hashes; retained actual completion output and pending status. |

## Limits And Additional Notes

- PMID12147680 was read as complete primary text/captions through a public author-PDF web reader; original PDF bytes were not retained and figure pixels were not inspected. No source_sha256 is asserted for that paper.
- The entire2020 article/Figures1-9 appraisal is attributed to /root/next244_primary_evidence. This reviewer independently checked claim-bearing original text and Figures5/7. Supporting information remained unavailable/unread and exact full experimental insert identities remain unverified.
- Native beta-G6P specificity is a database chemical assertion, not an anomer-specific conclusion of the cited biochemical assay. The broader Rhea deglycase is deliberately not used as an exact mapping.
- FrlA participation and CRP regulation are bounded inferences with explicit experimental limitations. Transcriptomic adapter results are context and cannot establish catalysis or direct regulation.
- Complete raw source originals remain in documented external archives; repository-retained hashes, projections and reading appraisals support auditability but do not embed every original or assure recovery after external archive loss.
- The six source-local draft assertions tracked in GitHub issue514 were independently verified repaired before initial native inspect. This pre-formal repair is not represented as a resolved structured finding and has no invented previous_occurrences.
- The initial pre-assessment inspection is preserved. Supplemental inspection adds final authority files and unchanged adjacent GO context; every initial inspected hash is unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T072939Z-fructoselysine-psicoselysine246-scientific
kind: record
repository: CultureBotAI/PathwayMech
title: Independent scientific review of fructoselysine and psicoselysine degradation
started_at: '2026-10-14T07:08:24.409943Z'
finished_at: '2026-10-14T07:29:39.291194Z'
reviewer:
  identity: Codex /root/ascorbate244_pr_review
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Did not author the maintained pathway, authority owners or generated
    artifacts. Conducted read-only identity research and draft feedback, then independently
    inspected promoted bytes and assessed all claims. Complete2020 primary appraisal
    is attributed to a separate contributor; personal source and figure coverage is
    explicit.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All fields and35 edges of exact3e5b25fc were scientifically assessed. No
  new actionable defect was found. Exact native chemistry, bounded recombinant constructs
  and appropriately qualified regulatory inference are supported. All required gates
  passed on unchanged final record bytes.
source:
  git_revision: 4d0546f17b4a554322a0b38f8d689d5b77a1e3c8
  state: working_tree
  inputs:
  - path: conf/identifier_policy.yaml
    sha256: f2991a22f16f0d14d83226c6ac261bc779b253b2547fae9724474d8596b411c7
    role: context
  - path: conf/identifier_sources.json
    sha256: 44678d183dafb98385d11df4daf9976634d369fda8c2a0c69793b02f991c840f
    role: context
  - path: conf/record_review.yaml
    sha256: a2d6578719a7d080eadc9520695ea7203618b0a7b274ee78fb25dbc17794876b
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: aeb52e13429c4523a0276fea9a3c2ea292a7cd8c7aab822308762d247c26dcd7
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 5ee9513a33dff9975d4faf0366b139ff858638d046ea901d6afe0aa34bec598d
    role: context
  - path: data/pathways/fructoselysine-and-psicoselysine-degradation.yaml
    sha256: 3e5b25fc917a30aca70b1dbdce4c70cb7b2d69f595b1f0f13d391812b7cdcb93
    role: target
  - path: data/pathways/fructoselysine-catabolic-process.yaml
    sha256: e9e80038a8671da109e8453523439ed921fe7810bb96b24f55dc532b4dd6ca5f
    role: context
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
  description: One complete maintained pathway and its source-linked graph.
  selection: Exact final integrated3e5b25fc candidate requested for independent adversarial
    scientific review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY0-521
  exclusions:
  - target: Other maintained pathways, comprehensive repository technical review,
      data licensing and public-release readiness
    reason: Outside this single-record scientific review; adjacent GO record is boundary
      context only.
targets:
- target_id: MetaCyc:PWY0-521
  path: data/pathways/fructoselysine-and-psicoselysine-degradation.yaml
  label: fructoselysine and psicoselysine degradation
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/fructoselysine-and-psicoselysine-degradation.yaml
    role: maintained pathway record
checks:
- check_id: native-inspect
  name: Native pre-assessment inspection
  status: passed
  required: true
  summary: Actual initial native inspect succeeded before assessment.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - initial-inspect
  command: scripts/record_review.py inspect --targets /private/tmp/pathwaymech-next-246-native-review-20261013/targets.json
  exit_code: 0
- check_id: supplemental-inspect
  name: Final authority native inspection
  status: passed
  required: false
  summary: Final authority files were inspected as added context; no existing inspected
    bytes changed.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - authority-inspect
  exit_code: 0
- check_id: all-edges
  name: Complete source-to-graph assessment
  status: passed
  required: false
  summary: All35 edge objects and all remaining record fields independently assessed.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - edge-assessment
  - reading-coverage
- check_id: technical-output
  name: Contributor generated-output audit
  status: passed
  required: false
  summary: Read the separate passing static graph/evidence/export audit; browser interaction
    was not exercised.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - technical-output
- check_id: reference-originals
  name: Reference original digest replay
  status: passed
  required: false
  summary: All29 asserted digests verified; one intentionally unhashed complete-paper
    citation.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - reference-hashes
- check_id: imodulondb
  name: Structured iModulonDB cross-check
  status: passed
  required: false
  summary: Both actual adapter commands succeeded; zero module hits makes summarize
    not applicable.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - imodulondb
  command: kg-microbe-sources imodulondb --timeout 30 datasets; kg-microbe-sources
    imodulondb --timeout 30 search --organism e_coli --dataset precise_mg1655 --query
    frl
  exit_code: 0
- check_id: render
  name: just render-pages
  status: passed
  required: false
  summary: Actual root-run command passed on the unchanged final target; this reviewer
    verified retained receipt/log hashes and read its completion output.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - gate-render
  command: just render-pages
  exit_code: 0
- check_id: kgx
  name: just kgx-export
  status: passed
  required: false
  summary: Actual root-run command passed on the unchanged final target; this reviewer
    verified retained receipt/log hashes and read its completion output.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - gate-kgx
  command: just kgx-export
  exit_code: 0
- check_id: lint
  name: just lint
  status: passed
  required: true
  summary: Actual root-run command passed on the unchanged final target; this reviewer
    verified retained receipt/log hashes and read its completion output.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - gate-lint
  command: just lint
  exit_code: 0
- check_id: validate
  name: just validate
  status: passed
  required: true
  summary: Actual root-run command passed on the unchanged final target; this reviewer
    verified retained receipt/log hashes and read its completion output.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - gate-validate
  command: just validate
  exit_code: 0
- check_id: test
  name: just test
  status: passed
  required: true
  summary: Actual root-run command passed on the unchanged final target; this reviewer
    verified retained receipt/log hashes and read its completion output.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - gate-test
  command: just test
  exit_code: 0
- check_id: diff-check
  name: git diff --check
  status: passed
  required: true
  summary: Actual focused formatting check passed.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - diff-check
  command: git diff --check
  exit_code: 0
evidence:
- evidence_id: initial-inspect
  kind: validation
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/initial-inspect.json
  locator: Complete retained receipt; exact frozen target3e5b25fc
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Actual native inspection preceded assessment on exact3e5b25fc and base4d0546;
    initial input hashes remain unchanged.
  snapshot_sha256: 4e3cce63722a183bb8bf8562488ef9e079f22a9f28e4bbd490940cb4ce5fa3ed
- evidence_id: authority-inspect
  kind: validation
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/supplemental-authority-inspect.json
  locator: Complete retained receipt; exact frozen target3e5b25fc
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Actual supplemental native inspection binds finalized authority owners
    and unchanged adjacent GO record; every initial context hash is preserved.
  snapshot_sha256: d4052742c8eef3e34393c5f1670eff1189f96ce3efc249da72c03067abd79913
- evidence_id: edge-assessment
  kind: record_content
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/edge-assessment.json
  locator: Complete retained receipt; exact frozen target3e5b25fc
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Every complete edge, endpoint qualifier and evidence locator was assessed
    against its cited original; no new actionable defect found.
  snapshot_sha256: cbf22238eb17cba082ca52a2e8bcdae5fd0911932470829ee0d53e94d54ed0ff
- evidence_id: reference-hashes
  kind: validation
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/reference-hashes.json
  locator: Complete retained receipt; exact frozen target3e5b25fc
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: All29 asserted reference digests match complete retained originals. PMID12147680
    intentionally has no original digest; no derived text is mislabelled as PDF bytes.
  snapshot_sha256: 59c0f8066f71bd53ee624d96613991f0aa32c22c59d520e607be00b8649c6c51
- evidence_id: reading-coverage
  kind: validation
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/reading-coverage.json
  locator: Complete retained receipt; exact frozen target3e5b25fc
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Separates personally inspected source text and figure pixels from the full2020
    appraisal contributed by the primary-evidence agent.
  snapshot_sha256: 516d03274c43d1c8d7b3cc613e4e258968235f9216671b926ce6c3356a70f9f7
- evidence_id: authority-assessment
  kind: authority
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/authority-assessment.json
  locator: Complete retained receipt; exact frozen target3e5b25fc
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: All4747 existing authority terms and738 owners retain parsed identity;10new
    terms and4new owners support the current record. The adjacent GO record remains
    byte-identical.
  snapshot_sha256: f776c66866847587084fe7170318de5591332a9261eb25b79ec2711e0660aa83
- evidence_id: diff-check
  kind: validation
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/diff-check.json
  locator: Complete retained receipt; exact frozen target3e5b25fc
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Actual focused git diff --check passed on the frozen target.
  snapshot_sha256: 320aa5383dbe771767cb839256bb8f521a964f0c1b3152e2758d75dfaee63252
- evidence_id: rhea-alternatives
  kind: authority
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/rhea-exact-alternative-search.json
  locator: Complete retained receipt; exact frozen target3e5b25fc
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Complete pinned Rhea142 aggregate scan finds no exact beta-product alternative
    for the deglycase; broad Rhea28383 is not silently substituted.
  snapshot_sha256: 3f07b6db3f955f877dece3a5ab4f19a5f720f47d10044fbf9ab3494ae6f02ddb
- evidence_id: dedup-bridge
  kind: search
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/post-draft-dedup-bridge.json
  locator: Complete retained receipt; exact frozen target3e5b25fc
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: context_only
  summary: 'Connects the precreation hidden/ignored-inclusive search to the subsequent
    candidate: all244 prior records unchanged, exactly one newly added pathway.'
  search_scope: Precreation rg --no-ignore --hidden text search over the entire next246
    worktree for PWY0-521, fructoselysine/fructosyllysine/psicoselysine, RXN0-4841,
    RHEA28390-28393, UPA00784, PMID14641112 and BJ20031527; all244 maintained YAMLs
    parsed. Hidden and ignored files included; no recursive following of symlink directories
    or binary decoding. Post-draft receipt compares the245-record inventory and all
    prior record hashes.
  snapshot_sha256: 0079e4a5c0622a72df4364c559a550c512338627787bf07e658fcca699801262
- evidence_id: imodulondb
  kind: database
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/imodulondb-check.json
  locator: Complete retained receipt; exact frozen target3e5b25fc
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: context_only
  summary: Actual structured adapter datasets and frl search succeeded; five expected
    gene hits and no module hit in precise_mg1655. No absence-based conclusion.
  snapshot_sha256: beca238642dd720fec2fd90ec27f05a25f09d6041398671dccb5e958ca8948f3
- evidence_id: record
  kind: record_content
  reference: data/pathways/fructoselysine-and-psicoselysine-degradation.yaml
  locator: Entire record; all35 edges and endpoint qualifiers
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Exact three-event native route, qualified primary experiments and process-level
    regulatory context are supported within stated limitations.
  snapshot_sha256: 3e5b25fc917a30aca70b1dbdce4c70cb7b2d69f595b1f0f13d391812b7cdcb93
- evidence_id: identity
  kind: authority
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/identity-audit/chemical-identity-closure.json
  locator: Whole native27.0 compounds and reactions; complete formal Rhea142 substrate/product/contains1/compound/chebi
    traversal; ChEBI255 structural fields
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: All nine core native chemical structures match exact charged ChEBI forms.
    The first two selected directional Rhea reactions are exact; native beta-G6P makes
    the third reaction narrower than Rhea28383.
  snapshot_sha256: 1b071d3fc4f2f25047e4f4e1b6b98d8985d7c144384393bf1c120e93afbde18c
- evidence_id: dedup
  kind: search
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/identity-audit/fresh-dedup-audit.json
  locator: Precreation search including hidden and ignored files and parsed inventory
    of244 maintained records
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: context_only
  summary: PWY0-521 is absent before creation; the existing GO1901281 record is the
    explicitly narrower two-step route and excludes upstream FrlC.
  search_scope: Precreation rg --no-ignore --hidden text search over the entire next246
    worktree for PWY0-521, fructoselysine/fructosyllysine/psicoselysine, RXN0-4841,
    RHEA28390-28393, UPA00784, PMID14641112 and BJ20031527; all244 maintained YAMLs
    parsed. Hidden and ignored files included; no recursive following of symlink directories
    or binary decoding. Post-draft receipt compares the245-record inventory and all
    prior record hashes.
  snapshot_sha256: 43e6e68afef53c2115c1af1458c540c2b6715d7c771bf9b39015a05a6b825749
- evidence_id: draft-repair
  kind: prior_review
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/author/issue-514-independent-disposition.json
  locator: Bounded pre-formal draft comparison3ff91bc5 to8dcfa98b; six source_assertion
    fields
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: The source-local provenance defect tracked in issue514 was independently
    confirmed repaired before promoted native inspection; every other parsed draft
    field was unchanged.
  snapshot_sha256: 73f3d3e684269507af64497e86f94b6742f1cd08482c382910692c8a47155083
- evidence_id: frlc2004
  kind: primary_source
  reference: https://research.dial.uclouvain.be/bitstreams/d9a57554-ce88-46e1-af66-9d66e5795925/download
  locator: Complete printed1047-1052; Figures1-5; cloning and assays; Fig4 reversible
    conversion; Fig2 metal tests
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Direct reversible conversion and bounded metal/phenotype observations support
    FrlC catalysis and qualified FrlA participation; exact printed275-aa construct
    differs from current276-aa entry.
  snapshot_sha256: 3ff6bd0c195156ff78fd509723301a3d425d317a6ef9e0f65489faeec579556c
- evidence_id: enzymes2002
  kind: primary_source
  reference: https://www.researchgate.net/profile/Elsa-Wiame/publication/11234416_Wiame_E_Delpierre_G_Collard_F_Van_Schaftingen_E_Identification_of_a_pathway_for_the_utilization_of_the_Amadori_product_fructoselysine_in_Escherichia_coli_J_Biol_Chem_277_42523-42529/links/566962a108aea0892c4992aa/Wiame-E-Delpierre-G-Collard-F-Van-Schaftingen-E-Identification-of-a-pathway-for-the-utilization-of-the-Amadori-product-fructoselysine-in-Escherichia-coli-J-Biol-Chem-277-42523-42529.pdf
  locator: Printed42523-42529 complete web-reader text; characterization sections,
    Figs5-8 and captions
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Supports qualified recombinant kinase/deglycase activity and zinc inhibition.
    The G6P product assay does not establish beta-anomer specificity.
- evidence_id: regulation2020
  kind: primary_source
  reference: https://edoc.ub.uni-muenchen.de/28034/7/Koller_Franziska.pdf
  locator: Thesis PDF85-100 contains article; claim-bearing PDF89-93/97-98, Figs5b-d
    and7, Methods4.5-4.9
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Reporter and operator-binding evidence support scoped FrlR and RpoH regulation;
    CRP remains an inference from cAMP manipulation/promoter architecture, not direct
    CRP perturbation or binding.
  snapshot_sha256: 0da0abe4b59d46041613fef11db65636d5facc75de2b722527b48c67195a0173
- evidence_id: appraisal2020
  kind: primary_source
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/reading/2020/claims.json
  locator: Complete16-page article appraisal and Figures1-9 by /root/next244_primary_evidence;
    supplement access exclusions
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Independent whole-article appraisal supports the included regulatory claims
    and identifies explicit construct, glucose-concentration, binding and strain limits.
  snapshot_sha256: b26740350cbf5bacc656040425be80420fb315032e945aba9c2c44107a017e69
- evidence_id: appraisal2002
  kind: primary_source
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/reading/2002/claims.json
  locator: Complete seven-page primary appraisal; original-access limitations
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Confirms biochemical and construct scope; figure pixels and original PDF
    bytes were not retained.
  snapshot_sha256: 13362bf9ee8775f6af23d925396018464639834c1ebd06dc1ee8426d90c74b10
- evidence_id: frlc-sequence
  kind: primary_source
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/reading/2004/frlc-sequence-comparison.json
  locator: Manual Figure1 sequence transcription versus complete current UniProt P45541
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Printed275 residues match current first275; current terminalArg276 is not
    in the experimental sequence depiction.
  snapshot_sha256: d50397400dd35f51522e6c06e830961287d165d6fd836cfcab2fca4e070dcdef
- evidence_id: protein-identities
  kind: database
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/identity-authorities/protein-original-bindings.json
  locator: Complete current reviewed UniProt original JSON bindings
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Protein labels, entry/sequence versions and evidence scope retain reviewed
    K12 identity without asserting exact experimental insert equivalence.
  snapshot_sha256: e8b86e1ea8b727bb36c426562cc16cf0e938b3f539b29e84b475954def090af9
- evidence_id: technical-output
  kind: validation
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/identity-authorities/technical-audit.json
  locator: Static HTML/SVG, all35 exported edges,14 endpoint qualifiers, existing
    KGX rows/contexts and authority preservation
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Read the separate technical audit by /root/next244_source_coverage, who
    also prepared authority inputs. It finds no defects and preserves all prior graph
    context; this reviewer does not claim to have rerun that audit or exercised a
    browser.
  snapshot_sha256: b54728048aa54544ef96d260fe0d6d1c0c6734f47338fe9cfdd691d990d42437
- evidence_id: integration-bridge
  kind: record_content
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/integrated-draft-bridge.json
  locator: Complete retained receipt; exact frozen target3e5b25fc
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: The first28 complete edge objects are parsed-identical to the repaired
    preintegration draft. Seven new edges and their added identities/references received
    fresh scientific assessment.
  snapshot_sha256: 1b346cfe131e4807acd7378249e3b8f0e7e552ab9fe5c0244a7ee32ab50df963
- evidence_id: gate-render
  kind: validation
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/validation/20261014T070954Z-render.json
  locator: Actual command, start/finish, target SHA and complete compressed stdout
    binding
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Root-run render passed on unchanged3e5b25fc. Receipt, compressed hash and
    decompressed stdout hash independently verified.
  snapshot_sha256: 2b8e46262783e4acfd26063b25a133e1d621d2620cff8459aff50976d51ed2c9
- evidence_id: gate-kgx
  kind: validation
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/validation/20261014T070954Z-kgx.json
  locator: Actual command, start/finish, target SHA and complete compressed stdout
    binding
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Root-run kgx passed on unchanged3e5b25fc. Receipt, compressed hash and
    decompressed stdout hash independently verified.
  snapshot_sha256: a7c8947fc69471ce522458654242382a70839dc4372355cfa9345efaa25d8f4a
- evidence_id: gate-lint
  kind: validation
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/validation/20261014T071008Z-lint.json
  locator: Actual command, start/finish, target SHA and complete compressed stdout
    binding
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Root-run lint passed on unchanged3e5b25fc. Receipt, compressed hash and
    decompressed stdout hash independently verified.
  snapshot_sha256: 93cf6f1e5e0fabf874f6683f42d840141aaaacb1f4080d370f17047a2e13bb99
- evidence_id: gate-validate
  kind: validation
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/validation/20261014T071452Z-validate.json
  locator: Actual command, start/finish, target SHA and complete compressed stdout
    binding
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Root-run validate passed on unchanged3e5b25fc. Receipt, compressed hash
    and decompressed stdout hash independently verified.
  snapshot_sha256: 725f9cc1d8580e42d3fc788b2dee4f946a396694de9c966c994233a1b3d7718a
- evidence_id: gate-test
  kind: validation
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/validation/20261014T071452Z-test.json
  locator: Actual command, start/finish, target SHA and complete compressed stdout
    binding
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Root-run test passed on unchanged3e5b25fc. Receipt, compressed hash and
    decompressed stdout hash independently verified.
  snapshot_sha256: d5b0c549ef202b0f7c26f3568fe4880a85cb6e5c88649c713b9b33ba8a78d657
- evidence_id: gate-replay
  kind: validation
  reference: research/pathway_additions/2026-10-13-next-246/fructoselysine-psicoselysine/independent-scientific-audit/gate-replay.json
  locator: Complete retained receipt; exact frozen target3e5b25fc
  accessed_at: '2026-10-14T07:29:39.291194Z'
  support: supports
  summary: Independently recomputed all available compressed and decompressed gate
    log hashes; retained actual completion output and pending status.
  snapshot_sha256: d5d606a4a3b077eb3b64681b276b24d46f043e5fd3cf4e62bcffc639d0e2cedd
assessments:
- assessment_id: identity
  area: identity
  topic: Native pathway boundary
  outcome: supported
  summary: The three-reaction PWY0-521 adds upstream psicoselysine epimerization to
    the existing explicitly narrower GO1901281 pathway. Identity and graph boundary
    are supported without treating different prefixes as novelty.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - identity
  - dedup
  - dedup-bridge
  - record
- assessment_id: chemistry
  area: grounding
  topic: Exact structures, complete sides and direction
  outcome: supported
  summary: All core structures retain native charge and stereochemistry; first two
    Rhea directional IDs match complete sides, including ATP/ADP/H+. Native RXN0-963
    preserves beta-G6P and source generality is not forced into a broader Rhea identifier.
    Source reversibility and chosen pathway direction remain distinct.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - identity
  - rhea-alternatives
  - edge-assessment
  dimensions:
  - name: source_object
    value: Whole native27.0 XML and aggregated Rhea142 RDF side/contains1 participant
      closure; ChEBI255 identity fields.
    definition: Exact source objects rather than unverified cross-reference equivalence.
    evidence_ids:
    - identity
  - name: component_role
    value: Nine core chemicals, alternative activity-enhancing metals, seven proteins
      and two assemblies have distinct roles.
    definition: Core chemistry, cofactors, assemblies and regulatory context are not
      conflated.
    evidence_ids:
    - record
    - edge-assessment
- assessment_id: frlc
  area: evidence
  topic: FrlC catalysis, constructs and metals
  outcome: supported
  summary: Reversible biochemical conversion supports the epimerization event. The
    printed sequence discrepancy, donor-strain discrepancy, inferred octamer, extract
    metal assay and alternative-metal scope remain explicit; zinc inhibition is not
    generalized to physiology.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - frlc2004
  - frlc-sequence
  - edge-assessment
- assessment_id: frldb
  area: evidence
  topic: FrlD and FrlB primary activity
  outcome: supported
  summary: Recombinant catalytic and inhibitor observations support the qualified
    edges. Experimental preparations and analytical limitations are retained separately
    from native database chemistry.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - enzymes2002
  - appraisal2002
  - edge-assessment
- assessment_id: frla
  area: evidence
  topic: Transporter participation inference
  outcome: supported
  summary: FrlA enables is supported only as qualified pathway participation from
    phenotype plus probable annotation; no direct transport measurement, coupling,
    complementation or polarity exclusion is invented.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - frlc2004
  - protein-identities
  - edge-assessment
- assessment_id: regulation
  area: graph
  topic: Regulatory context and evidence tiers
  outcome: supported
  summary: FrlR reporter repression and purified operator binding remain separate;
    RpoH overexpression supports expression activation. CRP is explicitly inferred
    from cyaA/glucose/promoter experiments. No direct CRP binding, FrlR autoregulation,
    native gene-specific transcript or host-adaptation experiment is asserted.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - regulation2020
  - appraisal2020
  - record
  - edge-assessment
  dimensions:
  - name: evidence_tier
    value: Native assertions, recombinant activity, growth inference, reporters and
      operator binding retain different evidentiary roles.
    definition: An inference is not upgraded to a directly measured causal event.
    evidence_ids:
    - edge-assessment
    - regulation2020
  - name: taxon_condition
    value: K12/MG1655 annotation, BL21 recombinant preparations and BW25113 reporters
      are separately qualified.
    definition: Database strain and actual assay construct/condition remain distinct.
    evidence_ids:
    - record
    - reading-coverage
    - regulation2020
- assessment_id: provenance
  area: provenance
  topic: Source-local evidence and original bindings
  outcome: supported
  summary: All cited asserted digests match original bytes; source assertions are
    local to their exact cited objects. Issue514 was repaired before native inspection
    and has no fabricated formal predecessor. Authority additions preserve all prior
    terms and owners.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - reference-hashes
  - draft-repair
  - authority-assessment
  - reading-coverage
- assessment_id: structured-context
  area: scope
  topic: Bounded transcriptomic cross-check
  outcome: supported
  summary: The structured adapter returns the expected five frl genes in precise_mg1655.
    Zero module hits is a query result, not evidence against regulation or pathway
    activity.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - imodulondb
- assessment_id: representation
  area: representation
  topic: Qualified graph export
  outcome: supported
  summary: The contributor technical audit retains all35 evidence-bearing edges and14
    endpoint qualifiers, correct local roles and all prior KGX contexts. This supports
    static generated representation within the disclosed lack of interactive browser
    testing.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - technical-output
  - record
- assessment_id: technical
  area: schema
  topic: Documented technical gates
  outcome: supported
  summary: Required gates are reported using actual input-bound receipts; scientific
    support is assessed independently of deterministic validation. All required validation,
    test, lint and formatting gates passed.
  target_ids:
  - MetaCyc:PWY0-521
  evidence_ids:
  - gate-replay
  - diff-check
  - authority-inspect
findings: []
actions: []
limitations:
- PMID12147680 was read as complete primary text/captions through a public author-PDF
  web reader; original PDF bytes were not retained and figure pixels were not inspected.
  No source_sha256 is asserted for that paper.
- The entire2020 article/Figures1-9 appraisal is attributed to /root/next244_primary_evidence.
  This reviewer independently checked claim-bearing original text and Figures5/7.
  Supporting information remained unavailable/unread and exact full experimental insert
  identities remain unverified.
- Native beta-G6P specificity is a database chemical assertion, not an anomer-specific
  conclusion of the cited biochemical assay. The broader Rhea deglycase is deliberately
  not used as an exact mapping.
- FrlA participation and CRP regulation are bounded inferences with explicit experimental
  limitations. Transcriptomic adapter results are context and cannot establish catalysis
  or direct regulation.
- Complete raw source originals remain in documented external archives; repository-retained
  hashes, projections and reading appraisals support auditability but do not embed
  every original or assure recovery after external archive loss.
notes:
- The six source-local draft assertions tracked in GitHub issue514 were independently
  verified repaired before initial native inspect. This pre-formal repair is not represented
  as a resolved structured finding and has no invented previous_occurrences.
- The initial pre-assessment inspection is preserved. Supplemental inspection adds
  final authority files and unchanged adjacent GO context; every initial inspected
  hash is unchanged.
links:
- https://github.com/CultureBotAI/PathwayMech/issues/514
tags:
- fructoselysine
- psicoselysine
- scientific-review
```

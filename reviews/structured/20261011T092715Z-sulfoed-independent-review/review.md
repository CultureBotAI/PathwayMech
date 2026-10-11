# Independent review of sulfoquinovose degradation II

- Review: 20261011T092715Z-sulfoed-independent-review
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-11T09:04:51Z
- Finished UTC: 2026-10-11T09:27:15Z
- Reviewer: Codex /root/pathway_literature_candidates (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete five-transformation sulfo-ED pathway is supported, with the final native NAD(P) activity represented by two explicit alternatives. All 48 edges and 86 evidence blocks were independently assessed against original sources. No corrective findings were identified. Exact strain/construct, cofactor evidence tiers, historical stereochemical prose, and later abstract-only evidence remain explicitly qualified. All required final cohort gates passed.

## Scope And Provenance

One complete frozen pathway, every local edge and source tier, exact chemistry, strain/construct and assembly/cofactor limitations.

Selection: Parent-assigned frozen MetaCyc:PWY-7722 at SHA256 20a95c209243399b88a90fbecb0d8d310ebfb3094fc6ee4487352fdc2185c596.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c555ecacc2b2708b246a68dcc9b64444791f526.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| MetaCyc:PWY-7722 | data/pathways/sulfoquinovose-degradation-ii.yaml | maintained | sulfoquinovose degradation II |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical pre-assessment inspection | passed | True | MetaCyc:PWY-7722 | Actual canonical inspect captured target and source context before assessment. |
| Independent original-source and actual KGX replay | passed | False | MetaCyc:PWY-7722 | Actual terminal 0 with original RDF/SQL/XML/JSON/HTML, sequence/primer and exporter checks; local helper failed attempts retained. |
| Final canonical inspection and sealed-input verification | passed | True | MetaCyc:PWY-7722 | All initial scientific inputs remained unchanged. All final log/archive digests, supporting receipts, frozen target and rendered-page hash were rechecked; canonical inspection captured final shared inputs. |
| Final coordinated render | passed | False | MetaCyc:PWY-7722 | Actual terminal exit 0; sealed log and archived copy independently rehashed. |
| Final coordinated validate | passed | True | MetaCyc:PWY-7722 | Actual terminal exit 0; sealed log and archived copy independently rehashed. |
| Final coordinated test | passed | True | MetaCyc:PWY-7722 | 1059 passed, 3 skipped, 3 upstream warnings in 300.19 s. |
| Final coordinated lint | passed | True | MetaCyc:PWY-7722 | Actual terminal exit 0; sealed log and archived copy independently rehashed. |
| Final coordinated identifiers | passed | False | MetaCyc:PWY-7722 | Actual terminal exit 0; sealed log and archived copy independently rehashed. |
| Final coordinated kgx | passed | False | MetaCyc:PWY-7722 | Actual terminal exit 0; sealed log and archived copy independently rehashed. |
| Final coordinated diff | passed | True | MetaCyc:PWY-7722 | Actual terminal exit 0; sealed log and archived copy independently rehashed. |

## Scientific And Domain Assessments

### Complete native sulfo-ED pathway

identity: supported. Targets: MetaCyc:PWY-7722.

The exact MetaCyc identity is retained; broad GO:1902777 and obsolete narrower terms are not substituted. All five transformations and two alternative terminal cofactor activities have bounded direct/native support.

### Charged structures, direction and source disagreement

grounding: supported. Targets: MetaCyc:PWY-7722.

Current chemical identifiers, native exact InChIs and original Figure 1 are consistent. Old R-SLA protein prose is explicitly rejected; original SQ1 HPLC data are not relabeled as an absolute-configuration assay.

### Strain, construct, assembly and cofactor specificity

scope: supported. Targets: MetaCyc:PWY-7722.

Protein functions are represented without claiming monomer sufficiency. Exact measured SQDH tetramer is retained, inferred metal/cluster annotations remain inferred, and altered aldolase start plus cross-strain later studies remain explicit.

### Conditional product inhibition and substrate specificity

evidence: supported. Targets: MetaCyc:PWY-7722.

Exact sequence-matched 2025 SQDH supports purified-enzyme NADH inhibition. New low-level side activities contextualize older negative tests; no false in-vivo regulation, exclusive specificity or surrogate SLA kinetic parameter is asserted.

### Every local edge and nearest source

graph: supported. Targets: MetaCyc:PWY-7722.

All 48 edges / 86 evidence blocks have been read, exact source locators checked, and actual KGX preserves endpoint/predicate/evidence details. No corrective finding remains in this selected record.

### Transcriptomic applicability

scope: supported. Targets: MetaCyc:PWY-7722.

KT2440 expression context is not transferred to SQ1; no absence conclusion is drawn.

### Final applicable corpus and generated-artifact checks

consistency: supported. Targets: MetaCyc:PWY-7722.

All required read-only corpus gates passed on the frozen corrected cohort. Generated artifact checks and unchanged scientific-input hashes support this observation without replacing the independent source assessment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/pathways/sulfoquinovose-degradation-ii.yaml; Complete frozen record: every participant, reaction, all 48 edges, all 86 evidence blocks and 22 references | supports | Complete native scope and all nearest-source assertions independently assessed; no corrective finding identified. |
| native | MetaCyc:PWY-7722 and five original reaction XML objects; reaction-list, reaction-ordering, left/right, dblink and reaction-direction | supports | All five native transformations are retained. Native RXN-17101 uses generic NAD(P) classes; current Rhea / UniProt split the final cofactor alternatives. Five native gene/enzyme objects and their stale protein prose were inspected separately. |
| chemistry | Rhea release142 original RDF and ChEBI255 SemanticSQL; Six directed equations,27 original side occurrences, compounds/formula/charge/InChI; all six native compound XML InChIs | supports | Independent original-RDF extraction confirms all selected directions, coefficients and six atom/charge balances. Exact native/current organic structures agree. The formula and charge conventions are internally consistent, including 2 H+ in both terminal alternatives. |
| primary2015 | PMID:26195800 / PMC4534283; Results s2-s5; Figure1 visually inspected; Figure4; SI8/9/10; Table1/footnote; TableS2; FigureS4 | supports | Original full primary supports SQ1-grown-cell expression, mutant phenotype and reconstitution of five purified proteins. SQ1 chromosomal inserts were sequence-verified and expressed in E. coli. Truncated dehydratase preparation, non-enantiomer-resolved assay, surrogate SLA kinetics and condition-specific negative substrate tests are preserved. |
| primary2025 | PMID:39840830 / PMC12133307; s2-1/p1-p4; s2-2/p1; Figure4; s5-2 complete sequences; s5-3 constructs | supports | Exact untagged published SQ1 SQDH sequence matches P0DOV5. SEC-MALLS supports tetramer; crystals agree. NAD specificity, trace G6P turnover and NADH competitive inhibition are assay-scoped. Independent sequence check grounds the inhibitor relation to the named protein without an intracellular regulation claim. |
| protein | UniProtKB:P0DOV5–P0DOV9 original complete reviewed JSON; Catalytic activity comments, cofactor/subunit comments, genomic and experimental referenceComments, sequences | supports | Five SQ1 identities and ECO0000269 catalytic annotations verified. Divalent-metal and dehydratase Fe4S4/homodimer evidence remains ECO0000250. All exact cited pointers including /comments/2/note/texts/0 exist and support the scoped statements. |
| construct | NCBIProtein:KHL76360.1 and GenBank:JTCJ01000004.1; Original CDS complement(18793..19560); paper primer alignment complement(18793..19596) | supports | Independent original-contig translation reproduces the 36-nt upstream 2015 start: MSTAVTPPTFTP extension, then internal Leu versus annotated initiator Met, with the remaining protein identical. This is the same genomic locus but not an identical construct claim. |
| primary2023 | PMID:37886098 / PMC10599462; abstract1/p1; sec3/p1; sec6/p1 | context_only | The racemic SLA consumption and solution tetramer are explicitly Rhizobium leguminosarum SRDI565 RlGabD. They support a transfer limitation, not exact SQ1 assembly or stereoselectivity. |
| primary2026 | PMID:41830472 / DOI:10.1002/chem.70857; Original Europe PMC CORE resultList.result[0].abstractText | context_only | Inspected primary abstract gives P. putida homohexamer, Co/Mn preferences and modest KDPG cross-reactivity; strain/construct are unspecified. Unavailable full article/SI and structure endpoints are retained as access limits. These observations are not transferred as exact SQ1 experimental evidence. |
| context | iModulonDB official precise321 dataset metadata; Strain,KT2440 in original dataset_meta.csv; root current dataset inventory/applicability and offline replay | context_only | The only P. putida dataset in the inspected inventory has KT2440 metadata, so it is not applied to SQ1. This does not assert module membership or biological absence. |
| audit | research/pathway_additions/2026-10-11-next-203/sulfoed-independent-review-audit.json; Original-source replay plus manual source assessment ledger | supports | Independent actual replay passed 67 source-body hashes,22 reference digests, 27 side occurrences, 6 balances, exact source pointers, construct checks and 28-node / 48-edge / 86-evidence export. Two local helper setup/API mistakes were corrected and their failed attempts are retained honestly. |
| gate-render | research/pathway_additions/2026-10-11-next-203/final-checks/render.txt; Complete command output; started 2026-10-11T09:19:51.110676+00:00; finished 2026-10-11T09:20:18.830217+00:00 | supports | Root-coordinated final full-corpus command; independent log hash and reported terminal-result check. |
| gate-validate | research/pathway_additions/2026-10-11-next-203/final-checks/validate.txt; Complete command output; started 2026-10-11T09:20:18.831588+00:00; finished 2026-10-11T09:21:48.513337+00:00 | supports | Root-coordinated final full-corpus command; independent log hash and reported terminal-result check. |
| gate-test | research/pathway_additions/2026-10-11-next-203/final-checks/test.txt; Complete command output; started 2026-10-11T09:20:18.833541+00:00; finished 2026-10-11T09:25:20.759261+00:00 | supports | Root-coordinated final full-corpus command; independent log hash and reported terminal-result check. |
| gate-lint | research/pathway_additions/2026-10-11-next-203/final-checks/lint.txt; Complete command output; started 2026-10-11T09:20:18.834336+00:00; finished 2026-10-11T09:20:18.991060+00:00 | supports | Root-coordinated final full-corpus command; independent log hash and reported terminal-result check. |
| gate-identifiers | research/pathway_additions/2026-10-11-next-203/final-checks/identifiers.txt; Complete command output; started 2026-10-11T09:20:18.991410+00:00; finished 2026-10-11T09:20:33.726628+00:00 | supports | Root-coordinated final full-corpus command; independent log hash and reported terminal-result check. |
| gate-kgx | research/pathway_additions/2026-10-11-next-203/final-checks/kgx.txt; Complete command output; started 2026-10-11T09:20:33.727072+00:00; finished 2026-10-11T09:20:50.203022+00:00 | supports | Root-coordinated final full-corpus command; independent log hash and reported terminal-result check. |
| gate-diff | research/pathway_additions/2026-10-11-next-203/final-checks/diff.txt; Complete command output; started 2026-10-11T09:20:50.203587+00:00; finished 2026-10-11T09:20:50.806867+00:00 | supports | Root-coordinated final full-corpus command; independent log hash and reported terminal-result check. |
| integration | research/pathway_additions/2026-10-11-next-203/integration-receipt.json; Complete sealed receipt; selected target row and linked original-source or command records | supports | Final post-issue371 shared gates and actual test result were read and rehashed. Initial author-helper lint failure and prior full test pass remain separate historical attempts; neither was relabeled as the final run. |
| generated | research/pathway_additions/2026-10-11-next-203/generated-graph-kgx-audit.json; Complete sealed receipt; selected target row and linked original-source or command records | supports | Final structural audit preserves the sulfoED page with 27 displayed nodes, 48 edges and all 86 evidence blocks; all 28 declared nodes including taxon are retained in KGX. Actual independent CLI downloads agree, with source metadata, directions and evidence links preserved. |
| authority-integration | research/pathway_additions/2026-10-11-next-203/authority-integration.json; Complete sealed receipt; selected target row and linked original-source or command records | supports | Canonical builders retained every baseline term and source. Final original-source authority snapshots are byte-identical to those captured before this scientific assessment. |

## Limits And Additional Notes

- 2026 aldolase full text, original strain and construct were not inspectable; abstract is contextual only.
- The 2015 SQ1 HPLC-MS assay is not an independent absolute-stereochemistry characterization; current explicit native/Rhea/ChEBI structures supply exact identity.
- Cofactors and some assemblies remain reviewed similarity annotations, rather than direct SQ1 occupancy/solution measurements.
- Original 2015 aldolase has a different upstream start from current annotation; exact locus is verified, not whole-construct identity.
- Live PMC web-tool calls returned browser challenges; retained original full HTML bodies were independently inspected.
- The other two cohort records are outside this scientific assessment. The reviewer authored the separate ergothioneine record, which received its own independent reviewer.
- Generated SVG and KGX checks are programmatic; no interactive browser or visual-layout inspection is claimed.
- Full-corpus gates were coordinated by the root agent. Their sealed command, timing, exit status and exact log hashes were independently inspected here; the reviewer did not duplicate the full suite.
- The first review-draft validation rejected the non-enumerated assessment area validation; this was corrected to consistency before canonical save. No pathway or scientific evidence changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T092715Z-sulfoed-independent-review
kind: record
repository: CultureBotAI/PathwayMech
title: Independent review of sulfoquinovose degradation II
started_at: '2026-10-11T09:04:51Z'
finished_at: '2026-10-11T09:27:15Z'
reviewer:
  identity: Codex /root/pathway_literature_candidates
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author sulfoED, its source projections, target
    or validation. Reviewer authored the unrelated ergothioneine record in the same
    cohort; it is excluded from this review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete five-transformation sulfo-ED pathway is supported, with the
  final native NAD(P) activity represented by two explicit alternatives. All 48 edges
  and 86 evidence blocks were independently assessed against original sources. No
  corrective findings were identified. Exact strain/construct, cofactor evidence tiers,
  historical stereochemical prose, and later abstract-only evidence remain explicitly
  qualified. All required final cohort gates passed.
source:
  git_revision: 7c555ecacc2b2708b246a68dcc9b64444791f526
  state: working_tree
  inputs:
  - path: conf/identifier_sources.json
    sha256: 6e00cd9909857e79aed9a99f5f980f65d27d2c762d2e74e4683f719af7875372
    role: context
  - path: data/identifier_authorities/ontology.json
    sha256: 6aa3c04fbb8dfebfba2a774e432764ee578f8951a140298a98c706396a2f690f
    role: context
  - path: data/identifier_authorities/sources.json
    sha256: 8185c5ca95a6c8eadc2e71c072916a85bfdb21d814e253ba65cec5c203f7e764
    role: context
  - path: data/pathways/sulfoquinovose-degradation-ii.yaml
    sha256: 20a95c209243399b88a90fbecb0d8d310ebfb3094fc6ee4487352fdc2185c596
    role: target
  - path: docs/CAUSAL_GRAPHS.md
    sha256: c635a91493a53b519ed2c8e0f825adcca320e1c8d96ef87a69459c8a2cb14937
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
  - path: research/pathway_additions/2026-10-11-next-203/authority-integration.json
    sha256: c491c847fd0df5f9259fc96d893b51850fab71be81ba75c5c6da496918c70e21
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/baseline-preservation.json
    sha256: c0efe8e3da64ddc951dfad096d68349a6bc897dfdc5a00d1d7cb5587efcc0fc8
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/generated-graph-kgx-audit.json
    sha256: 4b51696f051b4f71fdfc0b7e505ff36401d283e7716a96b1f93d7bf7900f9efb
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/imodulondb-applicability.json
    sha256: 57da9dbc37e8048aaf2a226985b1334a92ec6096cdaf8a81333069e3a93fb49f
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/imodulondb-offline-replay.json
    sha256: b043b3a91b5ab2a0b692df464d862be81fd6b026ed2a796df30b5c8d48862194
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/integration-receipt.json
    sha256: c2579bfcfed0e37e7c8d3e5ab6a952cbc15b0fae0463c4ae8c16da28994fa8a5
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/sulfoed-authority-inputs.json
    sha256: 7cab0427ef4a47afe7f47d6f1aeffd1da706efecc7b0fccd6c9c97b943e46ce5
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/sulfoed-curation.md
    sha256: db66f4d363f05e8451a0d49ceffa2d2ecc7661896a3acb263dbe82cca06b4e5a
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/sulfoed-dedup.json
    sha256: b94f789bb235c068fa456c796b9b1444248c4d73d4cfdb517ec65d35ad7f89e0
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/sulfoed-identifiers.json
    sha256: 1ecaf6befcd75c4e187c9658763885d7ece53170afa30a1ab7ee448870da99af
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/sulfoed-independent-review-audit.json
    sha256: 996e33a1eddaec0221cbf25066cf5f174d4cb079a86c50db31aab4cd27097e5c
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/sulfoed-independent-review-audit.md
    sha256: 0c9edec1706d85bb0210383f668e0954e230279376ad0f6935b0f7b79eedf478
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/sulfoed-protein-projection.json
    sha256: 3d29bfb534488463943d4f1c1dbf46e78910b12aca1856e78b25f180b69cdbc0
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/sulfoed-replay.py
    sha256: 95e4f7cbc2b2b4aa9cc4ae13febd6c8bf8a4887275b5d1968576d0eb9100a860
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/sulfoed-source-manifest.json
    sha256: e3f14694fba9923f03bc34b128cc3672ef0afc1b6a7776342e9b056a896b2706
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/sulfoed-source-projection.json
    sha256: ad3208e82f488c3d2cdf773bf76217128a3760a6607b2ee42e42040d8cc1cf63
    role: context
  - path: research/pathway_additions/2026-10-11-next-203/sulfoed-validation.json
    sha256: 2742b79dfb8990ec0f12dac02b0576c6e8d6821c0c6432f6ff9fce7c94b0ccf4
    role: context
  - path: src/pathwaymech/schema.py
    sha256: f006e5b99cedd91b57a2c5fb938315a84b68822586d1602d4df9ccfdc851e98c
    role: context
  - path: src/pathwaymech/schema/pathwaymech.yaml
    sha256: ffa1107da83c8ff173833662e78ba73c779bbab9f2da33cea993b614e99d6345
    role: context
targets:
- target_id: MetaCyc:PWY-7722
  path: data/pathways/sulfoquinovose-degradation-ii.yaml
  label: sulfoquinovose degradation II
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/PathwayMech
    path: data/pathways/sulfoquinovose-degradation-ii.yaml
    role: maintained record
scope:
  description: One complete frozen pathway, every local edge and source tier, exact
    chemistry, strain/construct and assembly/cofactor limitations.
  selection: Parent-assigned frozen MetaCyc:PWY-7722 at SHA256 20a95c209243399b88a90fbecb0d8d310ebfb3094fc6ee4487352fdc2185c596.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - MetaCyc:PWY-7722
  exclusions:
  - target: Other cohort records, full pathway inventory, publication licensing and
      in-vivo universal generalization
    reason: Outside this one-record review; unrelated ergothioneine author work is
      excluded.
checks:
- check_id: inspect
  name: Canonical pre-assessment inspection
  command: PYTHONPATH=src .venv/bin/python scripts/record_review.py inspect --targets
    /private/tmp/pathwaymech-next-203-sulfoed-review-targets.json
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-7722
  summary: Actual canonical inspect captured target and source context before assessment.
- check_id: independent-replay
  name: Independent original-source and actual KGX replay
  command: PYTHONPATH=src .venv/bin/python /private/tmp/pathwaymech-next-203-sulfoed-independent-replay.py
  status: passed
  required: false
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - audit
  summary: Actual terminal 0 with original RDF/SQL/XML/JSON/HTML, sequence/primer
    and exporter checks; local helper failed attempts retained.
- check_id: final-inputs
  name: Final canonical inspection and sealed-input verification
  command: PYTHONPATH=src .venv/bin/python /private/tmp/pathwaymech-next-203-sulfoed-final-input-check.py
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-7722
  summary: All initial scientific inputs remained unchanged. All final log/archive
    digests, supporting receipts, frozen target and rendered-page hash were rechecked;
    canonical inspection captured final shared inputs.
- check_id: gate-render
  name: Final coordinated render
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just render-pages
  status: passed
  required: false
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - gate-render
  summary: Actual terminal exit 0; sealed log and archived copy independently rehashed.
- check_id: gate-validate
  name: Final coordinated validate
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just validate
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - gate-validate
  summary: Actual terminal exit 0; sealed log and archived copy independently rehashed.
- check_id: gate-test
  name: Final coordinated test
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just test
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - gate-test
  summary: 1059 passed, 3 skipped, 3 upstream warnings in 300.19 s.
- check_id: gate-lint
  name: Final coordinated lint
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just lint
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - gate-lint
  summary: Actual terminal exit 0; sealed log and archived copy independently rehashed.
- check_id: gate-identifiers
  name: Final coordinated identifiers
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just check-identifiers
  status: passed
  required: false
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - gate-identifiers
  summary: Actual terminal exit 0; sealed log and archived copy independently rehashed.
- check_id: gate-kgx
  name: Final coordinated kgx
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    just kgx-export --output-dir /private/tmp/pathwaymech-next-203-kgx
  status: passed
  required: false
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - gate-kgx
  summary: Actual terminal exit 0; sealed log and archived copy independently rehashed.
- check_id: gate-diff
  name: Final coordinated diff
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/pathwaymech-curation-uv-cache
    git diff --check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - gate-diff
  summary: Actual terminal exit 0; sealed log and archived copy independently rehashed.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/pathways/sulfoquinovose-degradation-ii.yaml
  locator: 'Complete frozen record: every participant, reaction, all 48 edges, all
    86 evidence blocks and 22 references'
  accessed_at: '2026-10-11T09:13:39Z'
  support: supports
  summary: Complete native scope and all nearest-source assertions independently assessed;
    no corrective finding identified.
  snapshot_sha256: 20a95c209243399b88a90fbecb0d8d310ebfb3094fc6ee4487352fdc2185c596
- evidence_id: native
  kind: database
  reference: MetaCyc:PWY-7722 and five original reaction XML objects
  locator: reaction-list, reaction-ordering, left/right, dblink and reaction-direction
  accessed_at: '2026-10-11T09:13:39Z'
  support: supports
  summary: All five native transformations are retained. Native RXN-17101 uses generic
    NAD(P) classes; current Rhea / UniProt split the final cofactor alternatives.
    Five native gene/enzyme objects and their stale protein prose were inspected separately.
  snapshot_sha256: 99e2817a7fa24b23192f0a765629840443e117d68b20a1d0edac3fd264c2d0f4
- evidence_id: chemistry
  kind: authority
  reference: Rhea release142 original RDF and ChEBI255 SemanticSQL
  locator: Six directed equations,27 original side occurrences, compounds/formula/charge/InChI;
    all six native compound XML InChIs
  accessed_at: '2026-10-11T09:13:39Z'
  support: supports
  summary: Independent original-RDF extraction confirms all selected directions, coefficients
    and six atom/charge balances. Exact native/current organic structures agree. The
    formula and charge conventions are internally consistent, including 2 H+ in both
    terminal alternatives.
  snapshot_sha256: 8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf
- evidence_id: primary2015
  kind: primary_source
  reference: PMID:26195800 / PMC4534283
  locator: Results s2-s5; Figure1 visually inspected; Figure4; SI8/9/10; Table1/footnote;
    TableS2; FigureS4
  accessed_at: '2026-10-11T09:13:39Z'
  support: supports
  summary: Original full primary supports SQ1-grown-cell expression, mutant phenotype
    and reconstitution of five purified proteins. SQ1 chromosomal inserts were sequence-verified
    and expressed in E. coli. Truncated dehydratase preparation, non-enantiomer-resolved
    assay, surrogate SLA kinetics and condition-specific negative substrate tests
    are preserved.
  snapshot_sha256: e82307720415251fbe81a8293ed7078effeb5e268502c5776ce9b30f632e8afc
- evidence_id: primary2025
  kind: primary_source
  reference: PMID:39840830 / PMC12133307
  locator: s2-1/p1-p4; s2-2/p1; Figure4; s5-2 complete sequences; s5-3 constructs
  accessed_at: '2026-10-11T09:13:39Z'
  support: supports
  summary: Exact untagged published SQ1 SQDH sequence matches P0DOV5. SEC-MALLS supports
    tetramer; crystals agree. NAD specificity, trace G6P turnover and NADH competitive
    inhibition are assay-scoped. Independent sequence check grounds the inhibitor
    relation to the named protein without an intracellular regulation claim.
  snapshot_sha256: d3059313116aeac892709ea5a759bc1900fc4f47e8d021ff965a5a3c557f36b3
- evidence_id: protein
  kind: database
  reference: UniProtKB:P0DOV5–P0DOV9 original complete reviewed JSON
  locator: Catalytic activity comments, cofactor/subunit comments, genomic and experimental
    referenceComments, sequences
  accessed_at: '2026-10-11T09:13:39Z'
  support: supports
  summary: Five SQ1 identities and ECO0000269 catalytic annotations verified. Divalent-metal
    and dehydratase Fe4S4/homodimer evidence remains ECO0000250. All exact cited pointers
    including /comments/2/note/texts/0 exist and support the scoped statements.
- evidence_id: construct
  kind: database
  reference: NCBIProtein:KHL76360.1 and GenBank:JTCJ01000004.1
  locator: Original CDS complement(18793..19560); paper primer alignment complement(18793..19596)
  accessed_at: '2026-10-11T09:13:39Z'
  support: supports
  summary: 'Independent original-contig translation reproduces the 36-nt upstream
    2015 start: MSTAVTPPTFTP extension, then internal Leu versus annotated initiator
    Met, with the remaining protein identical. This is the same genomic locus but
    not an identical construct claim.'
  snapshot_sha256: 8736f6a5439a022c10f154cafdeb607f32515739d029ccbfe72020b7bf5165e7
- evidence_id: primary2023
  kind: primary_source
  reference: PMID:37886098 / PMC10599462
  locator: abstract1/p1; sec3/p1; sec6/p1
  accessed_at: '2026-10-11T09:13:39Z'
  support: context_only
  summary: The racemic SLA consumption and solution tetramer are explicitly Rhizobium
    leguminosarum SRDI565 RlGabD. They support a transfer limitation, not exact SQ1
    assembly or stereoselectivity.
  snapshot_sha256: e5e213c79ca6b4b0b5648555bc91d6af4e373f6f7cb2d389a0ded2effcbaa735
- evidence_id: primary2026
  kind: primary_source
  reference: PMID:41830472 / DOI:10.1002/chem.70857
  locator: Original Europe PMC CORE resultList.result[0].abstractText
  accessed_at: '2026-10-11T09:13:39Z'
  support: context_only
  summary: Inspected primary abstract gives P. putida homohexamer, Co/Mn preferences
    and modest KDPG cross-reactivity; strain/construct are unspecified. Unavailable
    full article/SI and structure endpoints are retained as access limits. These observations
    are not transferred as exact SQ1 experimental evidence.
  snapshot_sha256: bfaee9c036939b4db87a8076aacfcebd894569f3f7a31fab54d5a28b49a3c055
- evidence_id: context
  kind: database
  reference: iModulonDB official precise321 dataset metadata
  locator: Strain,KT2440 in original dataset_meta.csv; root current dataset inventory/applicability
    and offline replay
  accessed_at: '2026-10-11T09:13:39Z'
  support: context_only
  summary: The only P. putida dataset in the inspected inventory has KT2440 metadata,
    so it is not applied to SQ1. This does not assert module membership or biological
    absence.
  snapshot_sha256: 137eee274bdd0f331047457aba3854c2d0666d4c1401d07b067fbe1a5129d48c
- evidence_id: audit
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/sulfoed-independent-review-audit.json
  locator: Original-source replay plus manual source assessment ledger
  accessed_at: '2026-10-11T09:13:39Z'
  support: supports
  summary: Independent actual replay passed 67 source-body hashes,22 reference digests,
    27 side occurrences, 6 balances, exact source pointers, construct checks and 28-node
    / 48-edge / 86-evidence export. Two local helper setup/API mistakes were corrected
    and their failed attempts are retained honestly.
  snapshot_sha256: 996e33a1eddaec0221cbf25066cf5f174d4cb079a86c50db31aab4cd27097e5c
- evidence_id: gate-render
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/final-checks/render.txt
  locator: Complete command output; started 2026-10-11T09:19:51.110676+00:00; finished
    2026-10-11T09:20:18.830217+00:00
  accessed_at: '2026-10-11T09:27:15Z'
  support: supports
  summary: Root-coordinated final full-corpus command; independent log hash and reported
    terminal-result check.
  snapshot_sha256: c0abafa086139b1ddf252ff853aaebe2a3c361b8cb2a41b57eba41ab5626ec0c
- evidence_id: gate-validate
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/final-checks/validate.txt
  locator: Complete command output; started 2026-10-11T09:20:18.831588+00:00; finished
    2026-10-11T09:21:48.513337+00:00
  accessed_at: '2026-10-11T09:27:15Z'
  support: supports
  summary: Root-coordinated final full-corpus command; independent log hash and reported
    terminal-result check.
  snapshot_sha256: 7c6bc6e90859f7e5852ee3eb1c2154fdfba0dec3488f3cc14f9bdef4f237d809
- evidence_id: gate-test
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/final-checks/test.txt
  locator: Complete command output; started 2026-10-11T09:20:18.833541+00:00; finished
    2026-10-11T09:25:20.759261+00:00
  accessed_at: '2026-10-11T09:27:15Z'
  support: supports
  summary: Root-coordinated final full-corpus command; independent log hash and reported
    terminal-result check.
  snapshot_sha256: 158e3de6324689d08482f125437bad7f749f6b46364f3b92bd954702788afe3c
- evidence_id: gate-lint
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/final-checks/lint.txt
  locator: Complete command output; started 2026-10-11T09:20:18.834336+00:00; finished
    2026-10-11T09:20:18.991060+00:00
  accessed_at: '2026-10-11T09:27:15Z'
  support: supports
  summary: Root-coordinated final full-corpus command; independent log hash and reported
    terminal-result check.
  snapshot_sha256: df1116f359e834afd6a034defcde34a9a565e53ff21243185301623b334dcb41
- evidence_id: gate-identifiers
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/final-checks/identifiers.txt
  locator: Complete command output; started 2026-10-11T09:20:18.991410+00:00; finished
    2026-10-11T09:20:33.726628+00:00
  accessed_at: '2026-10-11T09:27:15Z'
  support: supports
  summary: Root-coordinated final full-corpus command; independent log hash and reported
    terminal-result check.
  snapshot_sha256: caa41fbc7e49c0fbdfcf6d0c410395136c3cefe70d34ba5d5157bb2de04705b3
- evidence_id: gate-kgx
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/final-checks/kgx.txt
  locator: Complete command output; started 2026-10-11T09:20:33.727072+00:00; finished
    2026-10-11T09:20:50.203022+00:00
  accessed_at: '2026-10-11T09:27:15Z'
  support: supports
  summary: Root-coordinated final full-corpus command; independent log hash and reported
    terminal-result check.
  snapshot_sha256: feea7c3ee89728a991b8d1eaa614e8ffae756ad43e720b9906e767a6f4433435
- evidence_id: gate-diff
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/final-checks/diff.txt
  locator: Complete command output; started 2026-10-11T09:20:50.203587+00:00; finished
    2026-10-11T09:20:50.806867+00:00
  accessed_at: '2026-10-11T09:27:15Z'
  support: supports
  summary: Root-coordinated final full-corpus command; independent log hash and reported
    terminal-result check.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: integration
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/integration-receipt.json
  locator: Complete sealed receipt; selected target row and linked original-source
    or command records
  accessed_at: '2026-10-11T09:27:15Z'
  support: supports
  summary: Final post-issue371 shared gates and actual test result were read and rehashed.
    Initial author-helper lint failure and prior full test pass remain separate historical
    attempts; neither was relabeled as the final run.
  snapshot_sha256: c2579bfcfed0e37e7c8d3e5ab6a952cbc15b0fae0463c4ae8c16da28994fa8a5
- evidence_id: generated
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/generated-graph-kgx-audit.json
  locator: Complete sealed receipt; selected target row and linked original-source
    or command records
  accessed_at: '2026-10-11T09:27:15Z'
  support: supports
  summary: Final structural audit preserves the sulfoED page with 27 displayed nodes,
    48 edges and all 86 evidence blocks; all 28 declared nodes including taxon are
    retained in KGX. Actual independent CLI downloads agree, with source metadata,
    directions and evidence links preserved.
  snapshot_sha256: 4b51696f051b4f71fdfc0b7e505ff36401d283e7716a96b1f93d7bf7900f9efb
- evidence_id: authority-integration
  kind: validation
  reference: research/pathway_additions/2026-10-11-next-203/authority-integration.json
  locator: Complete sealed receipt; selected target row and linked original-source
    or command records
  accessed_at: '2026-10-11T09:27:15Z'
  support: supports
  summary: Canonical builders retained every baseline term and source. Final original-source
    authority snapshots are byte-identical to those captured before this scientific
    assessment.
  snapshot_sha256: c491c847fd0df5f9259fc96d893b51850fab71be81ba75c5c6da496918c70e21
assessments:
- assessment_id: boundary
  area: identity
  topic: Complete native sulfo-ED pathway
  outcome: supported
  summary: The exact MetaCyc identity is retained; broad GO:1902777 and obsolete narrower
    terms are not substituted. All five transformations and two alternative terminal
    cofactor activities have bounded direct/native support.
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - native
  - primary2015
  - chemistry
- assessment_id: chemistry
  area: grounding
  topic: Charged structures, direction and source disagreement
  outcome: supported
  summary: Current chemical identifiers, native exact InChIs and original Figure 1
    are consistent. Old R-SLA protein prose is explicitly rejected; original SQ1 HPLC
    data are not relabeled as an absolute-configuration assay.
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - chemistry
  - primary2015
  - primary2023
- assessment_id: scope
  area: scope
  topic: Strain, construct, assembly and cofactor specificity
  outcome: supported
  summary: Protein functions are represented without claiming monomer sufficiency.
    Exact measured SQDH tetramer is retained, inferred metal/cluster annotations remain
    inferred, and altered aldolase start plus cross-strain later studies remain explicit.
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - protein
  - construct
  - primary2015
  - primary2025
  - primary2026
- assessment_id: evidence
  area: evidence
  topic: Conditional product inhibition and substrate specificity
  outcome: supported
  summary: Exact sequence-matched 2025 SQDH supports purified-enzyme NADH inhibition.
    New low-level side activities contextualize older negative tests; no false in-vivo
    regulation, exclusive specificity or surrogate SLA kinetic parameter is asserted.
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - primary2015
  - primary2025
  - primary2026
- assessment_id: graph
  area: graph
  topic: Every local edge and nearest source
  outcome: supported
  summary: All 48 edges / 86 evidence blocks have been read, exact source locators
    checked, and actual KGX preserves endpoint/predicate/evidence details. No corrective
    finding remains in this selected record.
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - record
  - audit
- assessment_id: context
  area: scope
  topic: Transcriptomic applicability
  outcome: supported
  summary: KT2440 expression context is not transferred to SQ1; no absence conclusion
    is drawn.
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - context
- assessment_id: gates
  area: consistency
  topic: Final applicable corpus and generated-artifact checks
  outcome: supported
  summary: All required read-only corpus gates passed on the frozen corrected cohort.
    Generated artifact checks and unchanged scientific-input hashes support this observation
    without replacing the independent source assessment.
  target_ids:
  - MetaCyc:PWY-7722
  evidence_ids:
  - integration
  - generated
  - authority-integration
  - gate-validate
  - gate-test
  - gate-lint
  - gate-diff
findings: []
actions: []
limitations:
- 2026 aldolase full text, original strain and construct were not inspectable; abstract
  is contextual only.
- The 2015 SQ1 HPLC-MS assay is not an independent absolute-stereochemistry characterization;
  current explicit native/Rhea/ChEBI structures supply exact identity.
- Cofactors and some assemblies remain reviewed similarity annotations, rather than
  direct SQ1 occupancy/solution measurements.
- Original 2015 aldolase has a different upstream start from current annotation; exact
  locus is verified, not whole-construct identity.
- Live PMC web-tool calls returned browser challenges; retained original full HTML
  bodies were independently inspected.
- The other two cohort records are outside this scientific assessment. The reviewer
  authored the separate ergothioneine record, which received its own independent reviewer.
- Generated SVG and KGX checks are programmatic; no interactive browser or visual-layout
  inspection is claimed.
- Full-corpus gates were coordinated by the root agent. Their sealed command, timing,
  exit status and exact log hashes were independently inspected here; the reviewer
  did not duplicate the full suite.
- The first review-draft validation rejected the non-enumerated assessment area validation;
  this was corrected to consistency before canonical save. No pathway or scientific
  evidence changed.
```

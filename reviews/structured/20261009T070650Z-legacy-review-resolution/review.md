# Reconcile 26 legacy pathway review reports with current evidence

- Review: 20261009T070650Z-legacy-review-resolution
- Repository: CultureBotAI/PathwayMech
- Started UTC: 2026-10-09T06:57:09Z
- Finished UTC: 2026-10-09T07:06:50Z
- Reviewer: Codex with delegated record and category reconciliation agents (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Read all 26 selected historical reports, reconciled their findings and conditional followups, and verified 152 current target hashes against the final integrated audit. Nineteen individual reports contain no corrective findings; seven category reports describe already-applied corrections. No current actionable defect was identified, no pathway edits were warranted, and scientific unknowns remain explicit. This new observation preserves old reports and superseding decisions without fabricating structured resolved lineage.

## Scope And Provenance

Bounded reconciliation of legacy report findings, recommendations and later integrated evidence; no fresh scientific or literature review.

Selection: All 19 Markdown files under reports/yaml_record_review and all 7 top-level Markdown files under reports/yaml_category_review present at initial inspection.
Coverage: full; 26 reviewed / 26 in the declared population.
Source: working_tree at Git base e04c41ce28323c8c35954da544bba1b33f86ed1c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| legacy-01 | reports/yaml_category_review/20261005T062048Z-gocam-causal-graphs.md | source | 20261005T062048Z-gocam-causal-graphs |
| legacy-02 | reports/yaml_category_review/20261005T064327Z-metacyc-causal-graphs.md | source | 20261005T064327Z-metacyc-causal-graphs |
| legacy-03 | reports/yaml_category_review/20261005T064715Z-diagram-and-mibig-causal-graphs.md | source | 20261005T064715Z-diagram-and-mibig-causal-graphs |
| legacy-04 | reports/yaml_category_review/20261005T064715Z-gocam-yeast-compartments.md | source | 20261005T064715Z-gocam-yeast-compartments |
| legacy-05 | reports/yaml_category_review/20261005T070225Z-folate-inositol-chemistry.md | source | 20261005T070225Z-folate-inositol-chemistry |
| legacy-06 | reports/yaml_category_review/20261005T071328Z-gocam-chemical-sides.md | source | 20261005T071328Z-gocam-chemical-sides |
| legacy-07 | reports/yaml_category_review/20261005T071959Z-all-causal-graphs.md | source | 20261005T071959Z-all-causal-graphs |
| legacy-08 | reports/yaml_record_review/20260925T102834Z-tetrahydrofolate-biosynthesis.md | source | 20260925T102834Z-tetrahydrofolate-biosynthesis |
| legacy-09 | reports/yaml_record_review/20260925T103456Z-utp-and-ctp-de-novo-biosynthesis.md | source | 20260925T103456Z-utp-and-ctp-de-novo-biosynthesis |
| legacy-10 | reports/yaml_record_review/20260925T104012Z-adenosine-ribonucleotides-de-novo-biosynthesis.md | source | 20260925T104012Z-adenosine-ribonucleotides-de-novo-biosynthesis |
| legacy-11 | reports/yaml_record_review/20260925T104540Z-adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.md | source | 20260925T104540Z-adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii |
| legacy-12 | reports/yaml_record_review/20260925T105222Z-gluconeogenesis-i.md | source | 20260925T105222Z-gluconeogenesis-i |
| legacy-13 | reports/yaml_record_review/20260925T110014Z-glycolysis-i-from-glucose-6-phosphate.md | source | 20260925T110014Z-glycolysis-i-from-glucose-6-phosphate |
| legacy-14 | reports/yaml_record_review/20260925T110624Z-mevalonate-pathway.md | source | 20260925T110624Z-mevalonate-pathway |
| legacy-15 | reports/yaml_record_review/20260925T111145Z-l-lysine-biosynthesis-iv.md | source | 20260925T111145Z-l-lysine-biosynthesis-iv |
| legacy-16 | reports/yaml_record_review/20260925T111814Z-phospholipid-biosynthesis.md | source | 20260925T111814Z-phospholipid-biosynthesis |
| legacy-17 | reports/yaml_record_review/20260925T112308Z-guanosine-ribonucleotides-de-novo-biosynthesis.md | source | 20260925T112308Z-guanosine-ribonucleotides-de-novo-biosynthesis |
| legacy-18 | reports/yaml_record_review/20260925T112914Z-methylglyoxal-catabolism.md | source | 20260925T112914Z-methylglyoxal-catabolism |
| legacy-19 | reports/yaml_record_review/20260925T113418Z-dolichyl-phosphate-d-mannose-biosynthesis.md | source | 20260925T113418Z-dolichyl-phosphate-d-mannose-biosynthesis |
| legacy-20 | reports/yaml_record_review/20260925T114143Z-thiamine-biosynthesis.md | source | 20260925T114143Z-thiamine-biosynthesis |
| legacy-21 | reports/yaml_record_review/20260925T114726Z-phospholipid-biosynthesis-ii-kennedy-pathway.md | source | 20260925T114726Z-phospholipid-biosynthesis-ii-kennedy-pathway |
| legacy-22 | reports/yaml_record_review/20260925T115356Z-valine-degradation.md | source | 20260925T115356Z-valine-degradation |
| legacy-23 | reports/yaml_record_review/20260925T115800Z-phosphatidylcholine-biosynthesis-i.md | source | 20260925T115800Z-phosphatidylcholine-biosynthesis-i |
| legacy-24 | reports/yaml_record_review/20260925T120549Z-trans-trans-farnesyl-diphosphate-biosynthesis.md | source | 20260925T120549Z-trans-trans-farnesyl-diphosphate-biosynthesis |
| legacy-25 | reports/yaml_record_review/20260927T042331Z-very-long-chain-fatty-acid-biosynthesis.md | source | 20260927T042331Z-very-long-chain-fatty-acid-biosynthesis |
| legacy-26 | reports/yaml_record_review/20260927T070312Z-glycogen-catabolism.md | source | 20260927T070312Z-glycogen-catabolism |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Review inventory and prior structured-bundle check | passed | True | legacy-01, legacy-02, legacy-03, legacy-04, legacy-05, legacy-06, legacy-07, legacy-08, legacy-09, legacy-10, legacy-11, legacy-12, legacy-13, legacy-14, legacy-15, legacy-16, legacy-17, legacy-18, legacy-19, legacy-20, legacy-21, legacy-22, legacy-23, legacy-24, legacy-25, legacy-26 | No pre-existing structured reviews; 26 selected legacy reports read in full. No structured lineage to retire. |
| Final integrated target hash verification | passed | True | legacy-01, legacy-02, legacy-03, legacy-04, legacy-05, legacy-06, legacy-07, legacy-08, legacy-09, legacy-10, legacy-11, legacy-12, legacy-13, legacy-14, legacy-15, legacy-16, legacy-17, legacy-18, legacy-19, legacy-20, legacy-21, legacy-22, legacy-23, legacy-24, legacy-25, legacy-26 | All 152 historical category targets match their final integrated reviewed hashes. All 19 individual-review targets are included. |
| Required local gate: validate | passed | True | legacy-01, legacy-02, legacy-03, legacy-04, legacy-05, legacy-06, legacy-07, legacy-08, legacy-09, legacy-10, legacy-11, legacy-12, legacy-13, legacy-14, legacy-15, legacy-16, legacy-17, legacy-18, legacy-19, legacy-20, legacy-21, legacy-22, legacy-23, legacy-24, legacy-25, legacy-26 | Passed skill validation and full QC: 157 pathway records, closed schema, identifiers/labels, 8,263 evidence blocks, 30 sources, documentation, deep-research contract, history, and generated pages current. |
| Required local gate: test | passed | True | legacy-01, legacy-02, legacy-03, legacy-04, legacy-05, legacy-06, legacy-07, legacy-08, legacy-09, legacy-10, legacy-11, legacy-12, legacy-13, legacy-14, legacy-15, legacy-16, legacy-17, legacy-18, legacy-19, legacy-20, legacy-21, legacy-22, legacy-23, legacy-24, legacy-25, legacy-26 | Full repository pytest passed. This is deterministic regression coverage, not a literature reassessment. 981 passed, 3 skipped, 3 warnings in 277.97s (0:04:37) |
| Required local gate: lint | passed | True | legacy-01, legacy-02, legacy-03, legacy-04, legacy-05, legacy-06, legacy-07, legacy-08, legacy-09, legacy-10, legacy-11, legacy-12, legacy-13, legacy-14, legacy-15, legacy-16, legacy-17, legacy-18, legacy-19, legacy-20, legacy-21, legacy-22, legacy-23, legacy-24, legacy-25, legacy-26 | Full repository Ruff check passed. |
| Required local gate: diff | passed | True | legacy-01, legacy-02, legacy-03, legacy-04, legacy-05, legacy-06, legacy-07, legacy-08, legacy-09, legacy-10, legacy-11, legacy-12, legacy-13, legacy-14, legacy-15, legacy-16, legacy-17, legacy-18, legacy-19, legacy-20, legacy-21, legacy-22, legacy-23, legacy-24, legacy-25, legacy-26 | Whitespace/error check passed for the tracked patch at assessment time. Untracked new files were outside that command scope. |
| Required local gate: skill | passed | True | legacy-01, legacy-02, legacy-03, legacy-04, legacy-05, legacy-06, legacy-07, legacy-08, legacy-09, legacy-10, legacy-11, legacy-12, legacy-13, legacy-14, legacy-15, legacy-16, legacy-17, legacy-18, legacy-19, legacy-20, legacy-21, legacy-22, legacy-23, legacy-24, legacy-25, legacy-26 | Skill-creator frontmatter and scaffold validation passed for the new resolver. |

## Scientific And Domain Assessments

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-01.

No concrete unimplemented correction identified within the historical report scope; corrections are represented by current files matching the final integrated review ledger. This is a reconciliation assessment, not a new scientific PASS or fabricated terminal finding lineage.

Historical cohort: 86 targets; each current target hash equals the final integrated ledger.
Prior correction groups: Native assertion locators and relation semantics corrected for all 86 records; source physical individuals preserved rather than collapsed to generic chemical classes. Ten unsupported threonine outline activities excluded; independently sourced GLY1 aldolase route added. Six lipid IV(A) native enablers and independently supported complex composition restored. CPX-1739 location conflict handed to, and subsequently reconciled by, yeast compartment audit.
Followup interpretation: Integration, rendering, export and gate handoffs were completed historically as recorded in main-integration-validation.json. Current full validate/test/lint now passed; actual commands and scope are recorded in checks. Provider-refresh reproduction remains a conditional future task, not an instruction to replay one-time migrations on already curated records.
Preserved scientific limits: Native unknown physical identities remain source-local. Unsupported yeast threonine branches remain excluded. Generic or missing exact enablers and complete physiological/cofactor coverage are not asserted.
Scope limits: Historical reports and ledgers remain byte-identical; no structured previous_occurrences are fabricated for legacy prose. Current byte identity verifies continued representation of prior reviewed decisions; it does not independently validate all biological assertions or establish literature completeness. Counts are an intermediate native stage, superseded by later compartment, chemistry and cofactor stages; they should not be forced onto the final current graph.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-02.

No concrete unimplemented correction identified within the historical report scope; corrections are represented by current files matching the final integrated review ledger. This is a reconciliation assessment, not a new scientific PASS or fabricated terminal finding lineage.

Historical cohort: 50 targets; each current target hash equals the final integrated ledger.
Prior correction groups: Core native leaf reaction coverage and glyoxylate/carbamoyl-phosphate routes completed. Composite-step chemistry exposed and erroneous attribution corrected. Unsupported protein/cofactor specificity excluded or qualified; repaired-mutant IlvG, tentative P00561/P00562 sodium and overly specific P05791 cluster chemistry not reinstated. Structured assertions separated from genuine literature quotations.
Followup interpretation: Integration, rendering, export and gate handoffs were completed historically as recorded in main-integration-validation.json. Current full validate/test/lint now passed; actual commands and scope are recorded in checks. Provider-refresh reproduction remains a conditional future task, not an instruction to replay one-time migrations on already curated records.
Preserved scientific limits: Broad taxon records may retain activity classes without exact named proteins. Cofactor absence is not cofactor independence; general iron-sulfur scope is deliberate. Source-supported specificity/protonation differences and alternative-route boundaries remain explicit.
Scope limits: Historical reports and ledgers remain byte-identical; no structured previous_occurrences are fabricated for legacy prose. Current byte identity verifies continued representation of prior reviewed decisions; it does not independently validate all biological assertions or establish literature completeness.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-03.

No concrete unimplemented correction identified within the historical report scope; corrections are represented by current files matching the final integrated review ledger. This is a reconciliation assessment, not a new scientific PASS or fabricated terminal finding lineage.

Historical cohort: 16 targets; each current target hash equals the final integrated ledger.
Prior correction groups: Misgrounded ATP/CoA/Q6/mycothiol/DAP/inositol identities, directionality, complexes and enzyme/cofactor roles corrected. Native diagram/BioPAX assertions replace manufactured quotations; reusable importers preserve object and direction provenance. TreS physiological direction, MshB/Mca roles and conditional metal dependence corrected; unsupported ImpC and THI3 catalytic assignments removed. LnyI dependence and observed linearmycin products represented while proposed assembly mechanism stays unasserted.
Followup interpretation: Integration, rendering, export and gate handoffs were completed historically as recorded in main-integration-validation.json. Current full validate/test/lint now passed; actual commands and scope are recorded in checks. Provider-refresh reproduction remains a conditional future task, not an instruction to replay one-time migrations on already curated records.
Preserved scientific limits: Mycothiol phosphate-removal catalyst remains unresolved. Three peptidoglycan nodes retain authentic GPML identities without external chemical grounding. Unassigned glutaredoxin partner and ambiguous branches remain omitted. Proposed linearmycin assembly is not established causal chemistry. Cross-provider duplication was outside this bounded review.
Scope limits: Historical reports and ledgers remain byte-identical; no structured previous_occurrences are fabricated for legacy prose. Current byte identity verifies continued representation of prior reviewed decisions; it does not independently validate all biological assertions or establish literature completeness.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-04.

No concrete unimplemented correction identified within the historical report scope; corrections are represented by current files matching the final integrated review ledger. This is a reconciliation assessment, not a new scientific PASS or fabricated terminal finding lineage.

Historical cohort: 85 targets; each current target hash equals the final integrated ledger.
Prior correction groups: Systematic definite-cytosol overstatement corrected conservatively, preserving physical located_in versus activity occurs_in distinction. Exact protein identity joins and source-conditional compartments added; five cytoplasmic actin-patch cases restored after initial overclassification. CPX-1739 activity reconciled to Golgi; CPX-1268 native mitochondrial activity corroborated, not falsely treated as a conflict. ADH4, ADK2, ARG2/ARG7 and DCI1 catalytic handoffs subsequently addressed by function and chemistry audits.
Followup interpretation: Integration, rendering, export and gate handoffs were completed historically as recorded in main-integration-validation.json. Current full validate/test/lint now passed; actual commands and scope are recorded in checks. Provider-refresh reproduction remains a conditional future task, not an instruction to replay one-time migrations on already curated records.
Preserved scientific limits: 108 independent activity-location gaps require activity-specific evidence, not inferred generic cytosol. Protein location does not prove absence of cytosolic activity or establish every catalytic compartment. Conditional molecular forms/topology are retained without simultaneous-location claims.
Scope limits: Historical reports and ledgers remain byte-identical; no structured previous_occurrences are fabricated for legacy prose. Current byte identity verifies continued representation of prior reviewed decisions; it does not independently validate all biological assertions or establish literature completeness.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-05.

No concrete unimplemented correction identified within the historical report scope; corrections are represented by current files matching the final integrated review ledger. This is a reconciliation assessment, not a new scientific PASS or fabricated terminal finding lineage.

Historical cohort: 2 targets; each current target hash equals the final integrated ledger.
Prior correction groups: Methenyl/methylene folate identities separated; MET13 NADPH/NADP specificity corrected while MET12 NADH route retained. Eighteen unsupported directed material-flow assertions quarantined; three actual folate bridges retained. Vip1/Kcs1 positional chemistry and missing Kcs1 enabler corrected; generic PP-InsP4/DDP1 identities preserved. Experimentally supported isolated Vip1 pyrophosphatase-domain activity added with qualified scope; redundant proton canceled.
Followup interpretation: Integration, rendering, export and gate handoffs were completed historically as recorded in main-integration-validation.json. Current full validate/test/lint now passed; actual commands and scope are recorded in checks. Provider-refresh reproduction remains a conditional future task, not an instruction to replay one-time migrations on already curated records.
Preserved scientific limits: Generic PP-InsP4 and DDP1 regioselectivity remain deliberate limits. Vip1 result concerns recombinant yeast domain in vitro; no whole-cell flux or untested IP8 hydrolysis inferred. Broad native folate/polyglutamate classes are not narrowed without evidence.
Scope limits: Historical reports and ledgers remain byte-identical; no structured previous_occurrences are fabricated for legacy prose. Current byte identity verifies continued representation of prior reviewed decisions; it does not independently validate all biological assertions or establish literature completeness.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-06.

No concrete unimplemented correction identified within the historical report scope; corrections are represented by current files matching the final integrated review ledger. This is a reconciliation assessment, not a new scientific PASS or fabricated terminal finding lineage.

Historical cohort: 85 targets; each current target hash equals the final integrated ledger.
Prior correction groups: All 475 original activity occurrences assigned explicit dispositions: 440 retained, 29 changed, six excluded; one Vip1 activity added. PSA1 donor pair, FOX2 stereochemistry, DCI1/ECI1, ARO8 sides, MAE1, ARG2/ARG7, COQ1 labels and yeast dATP scope corrected. Catalytic/function supplements corrected cardiolipin, ADK2, BNA3/LYS4, folate and inositol chemistry and qualified specificity conflicts.
Followup interpretation: Integration, rendering, export and gate handoffs were completed historically as recorded in main-integration-validation.json. Current full validate/test/lint now passed; actual commands and scope are recorded in checks. Provider-refresh reproduction remains a conditional future task, not an instruction to replay one-time migrations on already curated records.
Preserved scientific limits: Five retained activities lack exact enablers; spontaneous steps do not imply unknown enzymes. Seven substrate-specificity contexts lack independently complete catalogs; five tyrosol ADH branches have related-substrate rather than direct tyrosine-assay support. Two redox contexts retain pathway-system NADPH inputs without claiming balanced direct enzyme chemistry. Protein-bound/polymer reactants remain source abstractions.
Scope limits: Historical reports and ledgers remain byte-identical; no structured previous_occurrences are fabricated for legacy prose. Current byte identity verifies continued representation of prior reviewed decisions; it does not independently validate all biological assertions or establish literature completeness.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-07.

No concrete unimplemented correction identified within the historical report scope; corrections are represented by current files matching the final integrated review ledger. This is a reconciliation assessment, not a new scientific PASS or fabricated terminal finding lineage.

Historical cohort: 152 targets; each current target hash equals the final integrated ledger.
Prior correction groups: Complete integration of GO-CAM, MetaCyc, WikiPathways, Reactome and MIBiG corrections across the historical 152-record cohort. BNA3/BNA7, ACO1/ACO2/LYS4, CRD1, THI4/THI13, ADK2, FOX2, folate/MET13, inositol, material flow and compartments corrected. Parent renders, exports, closed schema, identifier and test gates performed during integration. Later PR262 adversarial corrections supersede the first integrated narrative: ARG82 crystal calcium excluded and THI13 exact products/balance quarantined; 7134 edges is the final reviewed ledger count.
Followup interpretation: Integration, rendering, export and gate handoffs were completed historically as recorded in main-integration-validation.json. Current full validate/test/lint now passed; actual commands and scope are recorded in checks. Provider-refresh reproduction remains a conditional future task, not an instruction to replay one-time migrations on already curated records.
Preserved scientific limits: ADP-thiazole hydrolysis and mycothiol phosphate-removal enzyme assignments unresolved. THI13 exact products and net balance remain unresolved; homolog evidence is not a direct THI13 experiment. CMP/STR2 specificity, native tyrosol context and Vip1 domain limitations remain qualified. Broad taxon enzyme classes and missing cofactor annotations do not establish molecular completeness.
Scope limits: Historical reports and ledgers remain byte-identical; no structured previous_occurrences are fabricated for legacy prose. Current byte identity verifies continued representation of prior reviewed decisions; it does not independently validate all biological assertions or establish literature completeness. This legacy narrative predates the final adversarial counts. Historical counts are not current invariant requirements. Five current pathways were added after this 152-record cohort and are outside its prior scientific coverage.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-08.

The old unsupported RO:0002411 omission and BFO omission are historical scope decisions. PR262 now preserves native causality/context with exact source_assertion locators.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/tetrahydrofolate-biosynthesis.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: No fresh experimental assessment of this native model was performed.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-09.

URA6, YNK1 and two CTP-synthase activities remain; later current context and cofactors supersede historical 30-edge count.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: Database assertion support is not proof that every referenced primary paper was read.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-10.

Later catalytic-function curation supersedes the historical ADK2 AMP/ATP assignment; current record has a second curation-history event.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: Preserve the newer species-specific ADK2 adjudication; historical source exactness is not biological correctness.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-11.

The historical instruction to preserve raw-only RXN0-745 has been superseded by PR262: the current description and final history event exclude class III formate-dependent ATP reduction from yeast. Three diphosphate-reduction/kinase activities remain.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: Do not restore the rejected branch merely because the legacy review passed its raw source projection.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-12.

Later PR262 curation removed a spurious nondecarboxylating MAE1 duplicate, documented in curation_history; 15 activities remain instead of the historical 16.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/gluconeogenesis-i.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: Raw source equality alone cannot override the newer independently supported MAE1 disposition.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-13.

The current graph preserves 14 activities and adds source context, complex composition and cofactors under the newer relation rubric.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: The old rule treating BFO/location context as illegal is obsolete; current source-supported context must be preserved.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-14.

The current HMG reaction has two HMG1/HMG2 enablers and one copy of each shared chemical-side triple; no duplicate edge triples are present.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/mevalonate-pathway.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: If importer regeneration is undertaken, preserve separate enablers without duplicating shared substrate/product triples.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-15.

Nine activities remain with later protein assignment/context/cofactor enrichment; current record is exactly the final PR262 reviewed digest.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/l-lysine-biosynthesis-iv.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: Later catalytic assignment corrections take precedence over the legacy raw-only pass.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-16.

Nine activities remain; later catalytic-function curation, including cardiolipin chemistry, supersedes legacy source-equality assertions.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/phospholipid-biosynthesis.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: The current function review/source locators remain necessary evidence; no new literature review was performed.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-17.

Six activities remain with later source context and cofactors; current record is exactly the final PR262 reviewed digest.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: No immediate legacy corrective task; future edits require current gates and evidence.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-18.

The current graph retains distinct GLO2 and GLO4 enables edges to GLYOXII-RXN and the parallel source-local hydrolase activity.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/methylglyoxal-catabolism.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: Preserve the parallel enzyme activities during future importer regeneration.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-19.

Four activities remain; later history explicitly corrects PSA1 guanylyl donor and leaving group while retaining GDP-mannose.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: Do not restore obsolete raw-source chemical sides to satisfy historical input/output counts.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-20.

Later function/adversarial curation retains the THI13 protein-bound core as a similarity inference and quarantines exact iron-redox, balancing and residue-product claims.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/thiamine-biosynthesis.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: THI13 omitted products/balancing species and the ADP-thiazole hydrolysis bridge remain bounded scientific uncertainties, not a license to invent edges.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-21.

The three EKI1/ECT1/EPT1 activities remain with later source context and cofactor enrichment.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: Historical lack of causal associations does not justify inventing ordering edges.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-22.

Eleven activities remain; the historical 24 causal source associations are now 24 provides_input_for assertions under corrected relation semantics.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/valine-degradation.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: The source isozyme fan-out is retained as source context, not new experimental validation.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-23.

The three CPT1/PCT1/CKI1 activities remain with later source context/cofactors.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/phosphatidylcholine-biosynthesis-i.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: This is still the exact GO-CAM pathway and is not merged with the related Kennedy model.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-24.

Three activities remain; old before-merge checks refer to the historical import. Current chemical sides/context are the final PR262 reviewed state.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: Reused upstream steps do not establish duplicate pathway identity.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-25.

Five activities remain. The previously omitted ELO3 output is now edge-037, an explicit native source_assertion at ./YeastPathways_PWY-5080-1.json#/facts/36, reconciled in the later native and chemical review ledgers.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: The native statement is database evidence, not direct experimental support; do not revert it solely because the old projection required an annotation array.

### Historical findings and conditional followups against current state

provenance: supported. Targets: legacy-26.

The current description remains explicitly GPH1/PGM scoped. Phosphate and shortened-glucan product were restored in PR262; GDB1 and SGA1 are not asserted as complete reactions.

Historical disposition: no findings and no recommended edits. Current target: data/pathways/glycogen-catabolism.yaml.
Current structural validation and duplicate-triple checks passed. Current target bytes match the final integrated PR #262 ledger; this is not a fresh scientific attestation.
Preserved limits: Ambiguous peripheral GDB1/SGA1 branches remain outside this record pending reaction-specific evidence; broader identifier support alone is insufficient.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| e001 | reports/yaml_category_review/20261005T062048Z-gocam-causal-graphs.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical category corrections and followup handoffs read in full and reconciled with later integrated audit evidence. |
| e002 | reports/causal_graph_review/all-pathways-summary.json; #/records/*/sha256 | supports | Every one of this report's 86 targets exactly matches the final integrated reviewed bytes; see per_target_hash_verification. |
| e003 | data/pathways/threonine-degradation.yaml; #/participants/7; #/mechanistic_edges/7 | supports | UniProtKB:P37303 is the preserved GLY1 participant and enables GO:0004793; current reviewed graph remains bounded. |
| e004 | data/pathways/sphingolipid-biosynthesis-yeast.yaml; mechanistic_edges[id=location-f1f67fe5b506] (lines 2342-2353) | supports | gomodel:RXN3O-663 occurs_in GO:0005794 with CPX-1739.json#/functions/0 as the independent activity-location source. |
| e005 | reports/causal_graph_review/gocam-location-review.json; #/summary | supports | Subsequent ledger explicitly records 163 quarantined cytosol assertions and 108 independent location gaps; prevents mistaking the early native-stage context for final assertions. |
| e006 | reports/yaml_category_review/20261005T064327Z-metacyc-causal-graphs.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical category corrections and followup handoffs read in full and reconciled with later integrated audit evidence. |
| e007 | reports/causal_graph_review/all-pathways-summary.json; #/records/*/sha256 | supports | Every one of this report's 50 targets exactly matches the final integrated reviewed bytes; see per_target_hash_verification. |
| e008 | reports/causal_graph_review/metacyc-review.json; per-record dispositions | supports | Detailed historical dispositions enumerate the 50-record source cohort; every current target matches the later final integrated hash. |
| e009 | reports/causal_graph_review/main-integration-validation.json; #/checks/render; #/checks/kgx; #/checks/qc; #/download_audit | supports | Parent render/export/QC followups are historically recorded as completed with exit 0, and source evidence/reference arrays were checked exactly. |
| e010 | reports/yaml_category_review/20261005T064715Z-diagram-and-mibig-causal-graphs.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical category corrections and followup handoffs read in full and reconciled with later integrated audit evidence. |
| e011 | reports/causal_graph_review/all-pathways-summary.json; #/records/*/sha256 | supports | Every one of this report's 16 targets exactly matches the final integrated reviewed bytes; see per_target_hash_verification. |
| e012 | data/pathways/mycothiol-biosynthesis.yaml; #/description (lines 3-7) | supports | Explicit unresolved phosphatase and ImpC histidinol-phosphatase reassignment remain in current maintained description. |
| e013 | data/pathways/linearmycin-biosynthetic-gene-cluster.yaml; #/description | supports | The record explicitly says assembly steps remain proposed; its final ledger/current hash matches four supported edges. |
| e014 | data/pathways/glutathione-glutaredoxin-redox-reaction.yaml; #/description (lines 3-6) | supports | Unresolved glutaredoxin redox partner remains explicitly scoped rather than invented. |
| e015 | reports/causal_graph_review/adversarial-scientific-corrections.json; #/records/0 | supports | Later choline classification correction supersedes an intermediate diagram-stage decision; all current files match the later integrated ledger. |
| e016 | reports/yaml_category_review/20261005T064715Z-gocam-yeast-compartments.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical category corrections and followup handoffs read in full and reconciled with later integrated audit evidence. |
| e017 | reports/causal_graph_review/all-pathways-summary.json; #/records/*/sha256 | supports | Every one of this report's 85 targets exactly matches the final integrated reviewed bytes; see per_target_hash_verification. |
| e018 | reports/causal_graph_review/gocam-location-review.json; #/summary/activity_decisions | supports | 204 compatible native assertions, 108 independent gaps, 163 quarantined conflicting cytosol assertions remain an exhaustive historical decision ledger. |
| e019 | reports/causal_graph_review/gocam-function-dispositions.json; #/records[accession=P10127] | supports | ADH4 physiological ethanol-oxidation branch excluded; higher-alcohol source contexts retain bounded specificity. |
| e020 | data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml; #/reactions/3; #/mechanistic_edges/28; #/mechanistic_edges/30 | supports | ADK2 activity is GTP:AMP phosphotransferase, with CHEBI:37565 input and CHEBI:58189 output. |
| e021 | tests/test_gocam_chemical_identities.py; test_arg2_and_arg7_acetyl_glutamate_labels_have_located_independent_evidence; test_fox2_stereochemistry_and_distinct_dci1_eci1_chemistry | supports | Existing regressions inspect the maintained ARG2/ARG7 labels and separate DCI1/ECI1 chemistry; full parent test gate pending this subtask. |
| e022 | reports/yaml_category_review/20261005T070225Z-folate-inositol-chemistry.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical category corrections and followup handoffs read in full and reconciled with later integrated audit evidence. |
| e023 | reports/causal_graph_review/all-pathways-summary.json; #/records/*/sha256 | supports | Every one of this report's 2 targets exactly matches the final integrated reviewed bytes; see per_target_hash_verification. |
| e024 | data/pathways/folate-interconversions.yaml; #/mechanistic_edges/62; #/mechanistic_edges/87 | supports | MET13 output CHEBI:58349 and input CHEBI:57783 retain explicit NADPH/NADP source rationale. |
| e025 | data/pathways/inositol-phosphate-biosynthesis.yaml; #/reactions/14; #/mechanistic_edges/107 through /112 | supports | RHEA:79724 has exact hydrolysis endpoints and enzyme edge explicitly limited to in-vitro recombinant domain activity, without physiological flux or S. pombe phenotype transfer. |
| e026 | tests/test_folate_inositol_chemistry.py; six maintained-record tests | supports | Existing record assertions cover folate identity, distinct cofactor specificity, three shared-intermediate flow edges, inositol isomers, generic identities and qualified domain hydrolysis; execution delegated to parent full suite. |
| e027 | reports/yaml_category_review/20261005T071328Z-gocam-chemical-sides.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical category corrections and followup handoffs read in full and reconciled with later integrated audit evidence. |
| e028 | reports/causal_graph_review/all-pathways-summary.json; #/records/*/sha256 | supports | Every one of this report's 85 targets exactly matches the final integrated reviewed bytes; see per_target_hash_verification. |
| e029 | reports/causal_graph_review/gocam-chemical-dispositions.json; #/activities (475 rows); #/added_activities/0 | supports | Complete historical original-to-final activity dispositions retain exact source pointers and amendment ledger references; current 85-target bytes match the integrated final ledger. |
| e030 | reports/causal_graph_review/gocam-function-dispositions.json; #/records[accession=P15700] | supports | CMP phosphorylation remains explicitly qualified as disputed, preserving opposing source identifiers. |
| e031 | tests/test_gocam_chemical_identities.py; seven maintained-record regression cases | supports | Current acceptance assertions cover named correction groups; parent full test suite supplies execution evidence. |
| e032 | reports/yaml_category_review/20261005T071959Z-all-causal-graphs.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical category corrections and followup handoffs read in full and reconciled with later integrated audit evidence. |
| e033 | reports/causal_graph_review/all-pathways-summary.json; #/records/*/sha256 | supports | Every one of this report's 152 targets exactly matches the final integrated reviewed bytes; see per_target_hash_verification. |
| e034 | reports/causal_graph_review/README.md; Graph and Evidence Patterns; Additional Notes | supports | Later overview explicitly records final 3599 participants, 814 reactions, 7134 edges and THI13/ARG82 adversarial dispositions. |
| e035 | reports/causal_graph_review/adversarial-pr-262.md; issues #263-#270 table | supports | Eight genuine historical issues have explicit correction and acceptance evidence; reports are preserved rather than retroactively rewritten. |
| e036 | data/pathways/thiamine-biosynthesis.yaml; #/mechanistic_edges/75; #/mechanistic_edges/79 through /83 | supports | THI13 keeps only bounded protein-bound histidyl/PLP inputs and HMP-P output, explicitly inferred by similarity; detailed products and balance remain unresolved. |
| e037 | reports/causal_graph_review/main-integration-validation.json; #/checks/tests; #/tests; #/download_audit | supports | Historical whole-suite exit 1 is not misreported: page-generation race was explicitly explained and browser test rechecked successfully. Current parent full-suite run must supply fresh current gate outcome. |
| e038 | reports/yaml_record_review/20260925T102834Z-tetrahydrofolate-biosynthesis.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e039 | data/pathways/tetrahydrofolate-biosynthesis.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e040 | reports/causal_graph_review/all-pathways-summary.json; /records/134 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e041 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e042 | reports/yaml_record_review/20260925T103456Z-utp-and-ctp-de-novo-biosynthesis.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e043 | data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e044 | reports/causal_graph_review/all-pathways-summary.json; /records/147 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e045 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e046 | reports/yaml_record_review/20260925T104012Z-adenosine-ribonucleotides-de-novo-biosynthesis.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e047 | data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e048 | reports/causal_graph_review/all-pathways-summary.json; /records/9 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e049 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e050 | reports/yaml_record_review/20260925T104540Z-adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e051 | data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e052 | reports/causal_graph_review/all-pathways-summary.json; /records/8 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e053 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e054 | reports/causal_graph_review/gocam-chemical-dispositions.json; /activities/9 | supports | Inspected current field content or local relation rubric for the historical followup. |
| e055 | reports/yaml_record_review/20260925T105222Z-gluconeogenesis-i.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e056 | data/pathways/gluconeogenesis-i.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e057 | reports/causal_graph_review/all-pathways-summary.json; /records/37 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e058 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e059 | reports/yaml_record_review/20260925T110014Z-glycolysis-i-from-glucose-6-phosphate.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e060 | data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e061 | reports/causal_graph_review/all-pathways-summary.json; /records/46 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e062 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e063 | reports/yaml_record_review/20260925T110624Z-mevalonate-pathway.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e064 | data/pathways/mevalonate-pathway.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e065 | reports/causal_graph_review/all-pathways-summary.json; /records/93 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e066 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e067 | reports/yaml_record_review/20260925T111145Z-l-lysine-biosynthesis-iv.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e068 | data/pathways/l-lysine-biosynthesis-iv.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e069 | reports/causal_graph_review/all-pathways-summary.json; /records/73 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e070 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e071 | reports/yaml_record_review/20260925T111814Z-phospholipid-biosynthesis.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e072 | data/pathways/phospholipid-biosynthesis.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e073 | reports/causal_graph_review/all-pathways-summary.json; /records/117 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e074 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e075 | reports/yaml_record_review/20260925T112308Z-guanosine-ribonucleotides-de-novo-biosynthesis.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e076 | data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e077 | reports/causal_graph_review/all-pathways-summary.json; /records/48 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e078 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e079 | reports/yaml_record_review/20260925T112914Z-methylglyoxal-catabolism.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e080 | data/pathways/methylglyoxal-catabolism.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e081 | reports/causal_graph_review/all-pathways-summary.json; /records/92 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e082 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e083 | reports/yaml_record_review/20260925T113418Z-dolichyl-phosphate-d-mannose-biosynthesis.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e084 | data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e085 | reports/causal_graph_review/all-pathways-summary.json; /records/26 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e086 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e087 | reports/yaml_record_review/20260925T114143Z-thiamine-biosynthesis.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e088 | data/pathways/thiamine-biosynthesis.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e089 | reports/causal_graph_review/all-pathways-summary.json; /records/136 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e090 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e091 | reports/yaml_category_review/20261005T071959Z-all-causal-graphs.md; remaining thiazole bridge gap; thiamine per-record entry | supports | Inspected current field content or local relation rubric for the historical followup. |
| e092 | reports/yaml_record_review/20260925T114726Z-phospholipid-biosynthesis-ii-kennedy-pathway.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e093 | data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e094 | reports/causal_graph_review/all-pathways-summary.json; /records/116 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e095 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e096 | reports/yaml_record_review/20260925T115356Z-valine-degradation.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e097 | data/pathways/valine-degradation.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e098 | reports/causal_graph_review/all-pathways-summary.json; /records/148 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e099 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e100 | reports/yaml_record_review/20260925T115800Z-phosphatidylcholine-biosynthesis-i.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e101 | data/pathways/phosphatidylcholine-biosynthesis-i.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e102 | reports/causal_graph_review/all-pathways-summary.json; /records/113 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e103 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e104 | reports/yaml_record_review/20260925T120549Z-trans-trans-farnesyl-diphosphate-biosynthesis.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e105 | data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e106 | reports/causal_graph_review/all-pathways-summary.json; /records/138 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e107 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e108 | reports/yaml_record_review/20260927T042331Z-very-long-chain-fatty-acid-biosynthesis.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e109 | data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e110 | reports/causal_graph_review/all-pathways-summary.json; /records/149 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e111 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e112 | reports/yaml_category_review/20261005-gocam-causal-graphs/gocam-causal-review.json; /records/83/facts/36 | supports | Inspected current field content or local relation rubric for the historical followup. |
| e113 | reports/causal_graph_review/gocam-chemical-dispositions.json; /activities/460 | supports | Inspected current field content or local relation rubric for the historical followup. |
| e114 | reports/yaml_record_review/20260927T070312Z-glycogen-catabolism.md; Entire report, including Findings, Recommended Edits, Follow-up Checks and limitations | context_only | Historical pass with no corrective findings; conditional recommendations reassessed. |
| e115 | data/pathways/glycogen-catabolism.yaml; /description; /participants; /reactions; /mechanistic_edges; /references; /curation_history | supports | Inspected current field content or local relation rubric for the historical followup. |
| e116 | reports/causal_graph_review/all-pathways-summary.json; /records/45 | supports | Current maintained bytes and field context inspected; the current target hash matches its later final integrated ledger entry. |
| e117 | docs/CAUSAL_GRAPHS.md; Components and relations; Evidence and provenance | supports | Inspected current field content or local relation rubric for the historical followup. |
| e118 | reports/yaml_category_review/20261005T064715Z-diagram-and-mibig-causal-graphs.md; Exhaustive per-record dispositions: glycogen-catabolism | supports | Inspected current field content or local relation rubric for the historical followup. |
| e119 | Local review inventory; reviews/structured; reports/yaml_record_review; reports/yaml_category_review; supporting reports/causal_graph_review | supports | Gitignore-independent filesystem and rg --no-ignore --hidden inventories found 19 individual and 7 top-level category Markdown reports; no existing structured bundle in the original or task checkout. Raw ledgers were used as context. No claim of absence outside these roots. |
| e120 | reports/causal_graph_review/all-pathways-summary.json; #/records/*/sha256 | supports | Recomputed SHA-256 for all 152 final-ledger targets: 152 match current bytes and initial inspection, zero mismatches. Final ledger cohort contains 7,134 edges; older prose totals are intermediate historical counts, not corrective targets. |
| e121 | just validate; Executed 2026-10-09T06:58:58.921772+00:00 through 2026-10-09T07:00:16.926693+00:00; exit 0 | supports | Passed skill validation and full QC: 157 pathway records, closed schema, identifiers/labels, 8,263 evidence blocks, 30 sources, documentation, deep-research contract, history, and generated pages current. |
| e122 | just test; Executed 2026-10-09T07:00:16.927798+00:00 through 2026-10-09T07:04:57.904577+00:00; exit 0 | supports | Full repository pytest passed. This is deterministic regression coverage, not a literature reassessment. 981 passed, 3 skipped, 3 warnings in 277.97s (0:04:37) |
| e123 | just lint; Executed 2026-10-09T07:04:57.906245+00:00 through 2026-10-09T07:04:59.216107+00:00; exit 0 | supports | Full repository Ruff check passed. |
| e124 | git diff --check; Executed 2026-10-09T07:04:59.216759+00:00 through 2026-10-09T07:04:59.295808+00:00; exit 0 | supports | Whitespace/error check passed for the tracked patch at assessment time. Untracked new files were outside that command scope. |
| e125 | .venv/bin/python /Users/marcin/.codex/skills/.system/skill-creator/scripts/quick_validate.py .claude/skills/pathwaymech-resolve-reviews; Executed 2026-10-09T07:04:59.296577+00:00 through 2026-10-09T07:04:59.400336+00:00; exit 0 | supports | Skill-creator frontmatter and scaffold validation passed for the new resolver. |

## Limits And Additional Notes

- This is reconciliation of 26 historical reports, not a new scientific review. No primary literature or upstream database retrieval was repeated, and no native scientific status was promoted.
- The 19 September individual reports predate the October causal-graph corrections. Their old pass verdicts, source projections, graph counts and schema exclusions are historical; current scope decisions are assessed against later evidence.
- All 152 records in the final integrated category ledger match its hashes. This proves continued representation of those reviewed decisions, not the truth or completeness of every biological claim. Field-level followups were inspected as described in the assessments.
- The current corpus contains 157 records. The five later pathways listed in scope exclusions have no historical scientific coverage from this cohort; current corpus-wide validation is not a substitute for scientific review.
- Legacy Markdown has no structured finding IDs. No previous_occurrences or terminal resolved findings have been fabricated, and no old report was rewritten. Empty findings means no current actionable defect was identified in this reconciliation scope.
- Historical scientific gaps remain: unknown mycothiol phosphate-removal catalyst and ADP-thiazole hydrolysis assignment; THI13 exact products/balance; activity-specific compartment gaps; generic chemical identities and incomplete cofactor, isoform or condition coverage. These limits are not scientifically resolved.
- Local source-ingestion artifacts, raw drafts and GitHub issues #273-277 are outside the selected completed-record-review population. Supporting causal audit ledgers inform this reconciliation but are not represented as new independent scientific reviews.
- Input source.state is working_tree: the retained hashes attest inspected bytes on the stated durable main base. Nineteen legacy reports were copied byte-for-byte from the original checkout and preserved for replayability; the bundle does not claim they were already tracked at that base.
- No biological YAML, generated pages, original legacy report bytes, or native curation statuses changed during this reconciliation.
- All 19 individual reports were previously untracked local artifacts. The new skill, routing, immutable review bundle and preserved historical inputs are the deliverables of this session.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T070650Z-legacy-review-resolution
kind: repository
repository: CultureBotAI/PathwayMech
title: Reconcile 26 legacy pathway review reports with current evidence
started_at: '2026-10-09T06:57:09Z'
finished_at: '2026-10-09T07:06:50Z'
reviewer:
  identity: Codex with delegated record and category reconciliation agents
  kind: agent
  model: gpt-6
  independence: self_review
  independence_basis: The session created the resolver workflow and applied it. Delegated
    readers checked disjoint report populations; this is not an independent new scientific
    review.
skill: pathwaymech-resolve-reviews
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Read all 26 selected historical reports, reconciled their findings and conditional
  followups, and verified 152 current target hashes against the final integrated audit.
  Nineteen individual reports contain no corrective findings; seven category reports
  describe already-applied corrections. No current actionable defect was identified,
  no pathway edits were warranted, and scientific unknowns remain explicit. This new
  observation preserves old reports and superseding decisions without fabricating
  structured resolved lineage.
source:
  git_revision: e04c41ce28323c8c35954da544bba1b33f86ed1c
  state: working_tree
  inputs:
  - path: .claude/skills/pathwaymech-resolve-reviews/SKILL.md
    sha256: 3d3b9d3b9e56cc782cf4ff63d491c5b589e9bdcde71438a695384b228edc4aea
    role: context
  - path: conf/record_review.yaml
    sha256: a2d6578719a7d080eadc9520695ea7203618b0a7b274ee78fb25dbc17794876b
    role: context
  - path: data/pathways/2-phenylethanol-biosynthesis.yaml
    sha256: cf1fc7347b88c2ecb1139564b24bd64018e0fc65793314061f3cf22eed5fd5ef
    role: context
  - path: data/pathways/4-aminobenzoate-biosynthesis-i.yaml
    sha256: b0150b47850d17acbbe560a7d40a82d49a2f976a92ea15ab43c44df1a83c4b91
    role: context
  - path: data/pathways/4-aminobutyrate-degradation.yaml
    sha256: dc220e2a4d394750d7adc8bbaa1a7060082c28daeaa077fb6e9c1f94f2168173
    role: context
  - path: data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml
    sha256: 74516388c180b8832fbaf1f8a24a3e8f71ff737a4812191b8c3807dfd91ec250
    role: context
  - path: data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml
    sha256: 324c587f1e7943d75cc48d6958fdf5f9e8b37d7427e2e132507192e670ba5ec9
    role: context
  - path: data/pathways/6-hydroxymethyl-dihydropterin-diphosphate-biosynthesis-i.yaml
    sha256: e5f0507a6060dab794ffc5b0b11b125f23677a9d54c5b5440a07eb05c48a72a9
    role: context
  - path: data/pathways/acetate-and-atp-formation-from-acetyl-coa-i.yaml
    sha256: 98fa4218caba0e95fbee8fc6ce63d97166499afb3609391db88ab6f82a1f4e22
    role: context
  - path: data/pathways/acetogenesis.yaml
    sha256: 355b97b8d2c45e437b853c2447bfb14900507b40923991d49d0b68e9e7d3d54a
    role: context
  - path: data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml
    sha256: 3cd2f4ba0bdbd27028fad8814a024a16cdca397bc09764ecba2597826bfc0625
    role: context
  - path: data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml
    sha256: 3840e82b7a5d9809e754222ac412b4321f3b99e73e085a3efdb9fbe6b402c9ef
    role: context
  - path: data/pathways/aerobic-glycerol-degradation.yaml
    sha256: 6541509e6b50f5a7f462010541a7953ddcafa82c49959ffcbf7658a00b5e92fb
    role: context
  - path: data/pathways/allantoin-degradation-to-glyoxylate-i.yaml
    sha256: 4d8f1c7aee53baaf61885814f0e6870ae480759cb825037725bfa39395921ac2
    role: context
  - path: data/pathways/allantoin-degradation-to-ureidoglycolate-i.yaml
    sha256: adb71534db0d3300a6757b499b757a2d17f901910cc2417d99ad6f7f510fdc31
    role: context
  - path: data/pathways/aspartate-biosynthesis.yaml
    sha256: 8c26f4bd655f7b13db25c70e817db9cb6b4232ccc941bf890bcbff54b25a180e
    role: context
  - path: data/pathways/assimilatory-sulfate-reduction.yaml
    sha256: 64aa47bf9da9d04d1e53d164f44d2ec4fb42adede455ea5dbbaa351917b398bc
    role: context
  - path: data/pathways/beta-alanine-biosynthesis-iv.yaml
    sha256: f12c8f6ea8a7b774c0e596fec3c141de4a5ae60049aee7caec8018f2827aa2ee
    role: context
  - path: data/pathways/carnitine-shuttle.yaml
    sha256: e7c9ab47f1cb65dd2ab0c467436da840f77e592fa9ca72293014350820cdb6af
    role: context
  - path: data/pathways/chitin-biosynthesis.yaml
    sha256: b7ab2d44d5694a1c1f56d15474c5d59ef66e7a0df36516e3325ea605b6c98c43
    role: context
  - path: data/pathways/chorismate-biosynthesis-i.yaml
    sha256: dc5c2fa8d319b3e1909f59982d6891e0de76eecc00bd3850da469507f0a1875a
    role: context
  - path: data/pathways/chromobacterium-violaceum-violacein-biosynthetic-gene-cluster.yaml
    sha256: a2c389bdea0ba8574ded73b47ae67cc5011105f4579401661197ffcb0e689d0a
    role: context
  - path: data/pathways/citrulline-biosynthesis.yaml
    sha256: bf40044ef709ce95ef9faafef7a724efbdac7764cce18fdd263520f0593f1924
    role: context
  - path: data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml
    sha256: bdca4a5ea4688a5a4f4ab4f18e93dc3501b40e0bfe00eb7fa1621998295f438d
    role: context
  - path: data/pathways/d-arabinose-degradation-i.yaml
    sha256: e4c05a00929557b8cabcdc26f057f7ac788d85ae82de515828806a79dd98f886
    role: context
  - path: data/pathways/d-galacturonate-degradation-i.yaml
    sha256: dafcc96c28d5d1e9c36f38a9b9701217e64b32cebffcb7fd4516bb1557a5d562
    role: context
  - path: data/pathways/d-glucarate-degradation-i.yaml
    sha256: c48cbb09d6b97812ea6d84a3229eae34400a68bccc38192553fff2d376ba4ad1
    role: context
  - path: data/pathways/d-xylose-degradation-i.yaml
    sha256: 4faccd4d9a05d6132f6f24e06d481e0c1be1386f4914cecd8abcab6e23c50ce2
    role: context
  - path: data/pathways/dolichyl-glucosyl-phosphate-biosynthesis.yaml
    sha256: 3d4489e00bc5bc9d7c5160d1ad3e7ed4a8c64e1722ef80b562740a6699febe5b
    role: context
  - path: data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml
    sha256: acc8b361993a1db31e3bf253e05526b2998b7a91c0cf3b0e6628aaf530adb688
    role: context
  - path: data/pathways/ectoine-biosynthesis.yaml
    sha256: 9f9d3c2c3de5ca5a3c59df1c3cb056fdf8cd60c0fb922feb902d5549151478dc
    role: context
  - path: data/pathways/epoxysqualene-biosynthesis.yaml
    sha256: c6bf14ce9e385df8aab07fb667d4aaecffcc53495d4b7372b02ea183f3898ccd
    role: context
  - path: data/pathways/ergosterol-biosynthesis-i.yaml
    sha256: 0439f963e2bcbb3e5e781df1338549c8963929747a721c72171cf533030344c5
    role: context
  - path: data/pathways/ethanol-degradation.yaml
    sha256: d9df81a6d31bb732e2077798277c3b840c71596a482366603a93d22285aa6f84
    role: context
  - path: data/pathways/fatty-acid-elongation.yaml
    sha256: 2da686ea5b62f2e43585967a23b1739d819a42dfcf19d0492cef55c944137120
    role: context
  - path: data/pathways/fatty-acid-oxidation-pathway.yaml
    sha256: 2dcd1db7489ee7695bd99461bbee5c59064e15853b3ab3c413ea6b6118aefe36
    role: context
  - path: data/pathways/flavin-biosynthesis-i.yaml
    sha256: 417d94b49af861613f07f76e2f4dc0d6b4d44123a57547a1c05c2aca91e2a025
    role: context
  - path: data/pathways/folate-interconversions.yaml
    sha256: 6774526812ae134d049d2bd6f36941ff0d4453558aa68259a790e93149278d6a
    role: context
  - path: data/pathways/formaldehyde-oxidation-ii-glutathione-dependent.yaml
    sha256: e100dd411c9dc79be86d86d0b2ee76f9a0c228d673ecb4d4b8343b264cfaa054
    role: context
  - path: data/pathways/galactose-degradation.yaml
    sha256: 3d1cd470853a62a3373ee876e18ba1c49f1aec17b858acb929c49af89c4296ee
    role: context
  - path: data/pathways/gluconeogenesis-i.yaml
    sha256: 365e9c29df8a62dd3dd5d4a3a190e530f6e3beae4a8e159be04ec9e4a9a952ba
    role: context
  - path: data/pathways/glutamate-degradation-i.yaml
    sha256: a518e6f42cee9d981d3a2876da0aa0ba9ed1612b90163f69cbbac1d8b1be28c0
    role: context
  - path: data/pathways/glutathione-biosynthesis.yaml
    sha256: e6b762e025742ca9cf0766d8d2d8b3f15e1c2b0078e7af2ab21bab1a43d8dba7
    role: context
  - path: data/pathways/glutathione-degradation.yaml
    sha256: f8f06c4612ab0c7e38f3b46378454ba449231a013816902262ef6bddcc4cf2e4
    role: context
  - path: data/pathways/glutathione-glutaredoxin-redox-reaction.yaml
    sha256: 670795c76c89c998d015e40536a5aba90acccb1430e7b4649aef2f738bad5e1b
    role: context
  - path: data/pathways/glycerol-biosynthesis.yaml
    sha256: 07b3f629ede35b4c42441295f1a3596a45ecbe776f9667633b3739c19bf742a6
    role: context
  - path: data/pathways/glycerol-degradation-v.yaml
    sha256: 17004e2911d28d42612c2010bf28d3339dc7f5f8a5af1e49b94cb4bae98ab2ba
    role: context
  - path: data/pathways/glycine-cleavage.yaml
    sha256: 14313c0e3e8c3af451b0946c2b7d8d20545af13e8e27c5441cea62648899a524
    role: context
  - path: data/pathways/glycogen-catabolism.yaml
    sha256: fc91636aa102a87bcb65d173ff28b2acbb356ea67beb831e00e7a93d9ae52aa4
    role: context
  - path: data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml
    sha256: ce99470da6b66a527a1a7ffe4e46e059afa4af75496a8fca96f2831049410be6
    role: context
  - path: data/pathways/glyoxylate-cycle.yaml
    sha256: bd5793fee6b8af7da1e67eece20ebfd65004a48bdfe4d4afbbfb3d544c8138b9
    role: context
  - path: data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml
    sha256: 65c619b8dfdd73062ad25ec9757f617da2a1a5739502ea44004be38e20897df0
    role: context
  - path: data/pathways/heme-biosynthesis-i-aerobic.yaml
    sha256: 0b59dea7ec3eb1b01ba4b147d7532f7a395ef1d6d4128eb7f6be7e6a7cf8dcc3
    role: context
  - path: data/pathways/hexaprenyl-diphosphate-biosynthesis.yaml
    sha256: d72784cfaf3d8bf0e30f226b687177eaf269358a3317327aaa2ca12686c7b1ff
    role: context
  - path: data/pathways/homocysteine-and-cysteine-interconversion.yaml
    sha256: 548a2a31db077211819e31504c16f45e3ce711858ef8bafc992d142e50fe095a
    role: context
  - path: data/pathways/inosine-5-phosphate-biosynthesis-i.yaml
    sha256: 74e4cd1621fc270ba365ef411b3079692de075024264f7e8866f6b0d9442938e
    role: context
  - path: data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml
    sha256: d676ccc1740fc538486cc7c9664bd5e3e2c89cc2aadd74bcffd586cce6aa7b97
    role: context
  - path: data/pathways/inositol-phosphate-biosynthesis.yaml
    sha256: add22f805f7a14a195c64a04e8b070f98c68626b30e768898e843213e7809fcc
    role: context
  - path: data/pathways/isoleucine-degradation.yaml
    sha256: 50585e2d8674b369b4aa5271ba78c57c18ea7556138e16e55140d77c42aa935e
    role: context
  - path: data/pathways/l-arabinose-degradation-i.yaml
    sha256: 37cfa161adf3d8ab8b4b01a018d387d60b33817bd5908b0d1dc73c91ee7d001e
    role: context
  - path: data/pathways/l-arginine-biosynthesis-i.yaml
    sha256: bf299cc075fee4f21e6cb76b71cdcddc70c06dbd8db17ab9448144f95dd7535c
    role: context
  - path: data/pathways/l-arginine-biosynthesis-ii-acetyl-cycle.yaml
    sha256: fa54ce93a653642b1fe2e0d9a1a02654ca238723ca6191a113c4f105ee1e07fe
    role: context
  - path: data/pathways/l-arginine-degradation-ii-ast-pathway.yaml
    sha256: fe02deb131bfe53eedb770ed50278885955e7a67d97859184142aea6ae35c86b
    role: context
  - path: data/pathways/l-arginine-degradation-iv.yaml
    sha256: e9769441139f7047c2d2c83338b03deffc61bc3ec7b84990e0487e4f5e8eaa92
    role: context
  - path: data/pathways/l-arginine-degradation-v.yaml
    sha256: 869563ce5c7be07d5d4bd976ff53030082e518f913822b09f2c01033aee801df
    role: context
  - path: data/pathways/l-asparagine-biosynthesis-i.yaml
    sha256: 766ba43c30ea3c6568779592c48aa667dd38880b0023a091979df2705161bb16
    role: context
  - path: data/pathways/l-asparagine-degradation.yaml
    sha256: 7df30c94062629ad64c6ed7d137a637f904a1f7428d2b530fde78b78bc5df5c2
    role: context
  - path: data/pathways/l-cysteine-biosynthesis-i.yaml
    sha256: 54fe6a258f21f5866d4051ad8b756f347191a9fe3a154b3749c8393367157476
    role: context
  - path: data/pathways/l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml
    sha256: acb2ce1d623b40d939a091bdbb3f9ce5d118a00aff3ebb873752ea323722de46
    role: context
  - path: data/pathways/l-fucose-degradation-i.yaml
    sha256: a00b36d76e86e0102822cd1d280e686310aa0ff1603d0f4e53a8ed7286b3dc9a
    role: context
  - path: data/pathways/l-histidine-biosynthesis.yaml
    sha256: d4f67cf6d398a8ed42fcd7a83588f93c0f81ee22ddc94308d8027a9aa39e6c58
    role: context
  - path: data/pathways/l-homocysteine-biosynthesis.yaml
    sha256: 5f4f330c4cee30dfe0ee244331adb501776c4e34c4f34811f428379cc99380e5
    role: context
  - path: data/pathways/l-homoserine-biosynthesis.yaml
    sha256: 2ba55d5db3be34827890a544718c9759c4a606e464b0e46d3c263bf4dcff30d1
    role: context
  - path: data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml
    sha256: 6f478576730ca9224f355d5f04730464a7a7fa4e4dcca9a16c206b21669d8445
    role: context
  - path: data/pathways/l-leucine-biosynthesis.yaml
    sha256: 7c11ab8c3970d6ac699b9a6d55bcfb8e31fa936fd8be9a8cffec49cb0f63bc1d
    role: context
  - path: data/pathways/l-lysine-biosynthesis-i.yaml
    sha256: f9e140eb9a5d886b826e5b77d03b44ad9bbad4b46dac54cdd676ad067e68705e
    role: context
  - path: data/pathways/l-lysine-biosynthesis-iv.yaml
    sha256: 7f6375da56c7c53b27a336f385c71564c46ad7700e397063915bf6d6bdd18530
    role: context
  - path: data/pathways/l-methionine-biosynthesis-i.yaml
    sha256: d3f600b8cf7da3ca2d5027327097c08e11bf562bbdceea90b1c5e9e7faaf2e89
    role: context
  - path: data/pathways/l-ornithine-biosynthesis-i.yaml
    sha256: 922abf2efb71d2ba60e3913a9c0827bdcf419bd8800d900d66d4b8752e075d7f
    role: context
  - path: data/pathways/l-phenylalanine-biosynthesis-i.yaml
    sha256: 9b816a653a709e59bd9cd25b249d0e8e0ad58fcb90d072c981bd8c2748811d88
    role: context
  - path: data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml
    sha256: e812af6b8f5879d39859ff0203088ddb6c298f1df13167d4e76f39f98f4da252
    role: context
  - path: data/pathways/l-proline-degradation.yaml
    sha256: 47625a371cab68efdf3f6e5deda9a982d8c309bda00f74827b03f0ae164ec49d
    role: context
  - path: data/pathways/l-rhamnose-degradation-i.yaml
    sha256: f7afcfa11188882427f316b02209fcb4fe4544c1e45c0290259858a5c28ed970
    role: context
  - path: data/pathways/l-serine-biosynthesis-i.yaml
    sha256: b8fd90eb060911cf62737caa12f9b4899cc89119a2369aa3281bc700a64313a9
    role: context
  - path: data/pathways/l-threonine-biosynthesis.yaml
    sha256: e277951647e3da86c7ad92ac40a3e8d795c36f1550d67825898927540fe5dfa3
    role: context
  - path: data/pathways/l-tryptophan-biosynthesis.yaml
    sha256: 92206dbd7e6e9aba6fee6e9f866e3eb3fe019cd6b832a0ac6586cbcc65ce6dcc
    role: context
  - path: data/pathways/l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde.yaml
    sha256: 435fa7b9e72cb017859159a7eb2ba3c078248638810272043fb23a22e27a67ea
    role: context
  - path: data/pathways/l-tyrosine-biosynthesis-i.yaml
    sha256: e61553cc86414476cc4bc593114c2c0820b01246225450edffdef55910efe376
    role: context
  - path: data/pathways/l-tyrosine-degradation-iii.yaml
    sha256: 2ab3d77be1a21b236beb89a4b6c316c37f37bac708741ca496b552318ee96b7e
    role: context
  - path: data/pathways/l-valine-biosynthesis.yaml
    sha256: 9b58c4c2bdd0b065c6227492dda5c6bc998902739848ab4f2dc1f070e7bd9c19
    role: context
  - path: data/pathways/leucine-degradation.yaml
    sha256: b11427a45a2f33becfda49dee1e4a636844f2c1d8febf8042e0e5daf10892d6d
    role: context
  - path: data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
    sha256: a5a908285f06357add5292777ea7be2226263c1448097361f9b3d87be0001cbe
    role: context
  - path: data/pathways/lipid-iva-biosynthesis.yaml
    sha256: 5fdcc02a40f15844d1ba8a2ca67979afd58bd34781af21d8e2380a46df7faad5
    role: context
  - path: data/pathways/mannose-degradation.yaml
    sha256: dd4237f6d08801e661b2089644fcfb4c46fbbd1f65868d6853d51cae84293251
    role: context
  - path: data/pathways/methionine-salvage-pathway.yaml
    sha256: 2220e5618ddc3f993788bf772fd20c560350c3752885a9d7bb07eb7e297d7b3c
    role: context
  - path: data/pathways/methylglyoxal-catabolism.yaml
    sha256: 4e0655e6c340986dbb79f846b237550d6d793e7ae5781d576df4fbd6fa5f1ba1
    role: context
  - path: data/pathways/mevalonate-pathway.yaml
    sha256: 25a739d9e28a0dfaabc31f59bcaa98179ca4377f501a0f8a8a869039b786afdb
    role: context
  - path: data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml
    sha256: cdbfd2cae9e281dc1a1722f65b2f019841b0a84b6e53e755bce049d495ed7f44
    role: context
  - path: data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml
    sha256: 99b0c6d3e04ab2d3c310bbe8099cd5fa716f251632e5320ba83444bd7ebff82d
    role: context
  - path: data/pathways/mycobacterium-sulfate-assimilation.yaml
    sha256: aecb344e6ec330b48884cafd9bab879f5e3c623f66e315d90ad93910da12f931
    role: context
  - path: data/pathways/mycobacterium-trehalose-biosynthesis.yaml
    sha256: 7c3915665fbbe8cfe1d695354f471a1c832ccf972d2302c0910a96144ec1cd49
    role: context
  - path: data/pathways/mycothiol-biosynthesis.yaml
    sha256: 35dfb77de4fcc447aeb649bb478c6a840e78ab39f5921469a154ec3768c32f4f
    role: context
  - path: data/pathways/mycothiol-catabolism.yaml
    sha256: 9d1f2496015cee969712712da363456ac0cac63dcd5cb46cfa5ace763f8388b1
    role: context
  - path: data/pathways/myo-inositol-biosynthesis.yaml
    sha256: f1131912336cddeb1e79f27e4c0087e7188d97ad775583fbef65b7056086a5e5
    role: context
  - path: data/pathways/n-acetylglucosamine-degradation-i.yaml
    sha256: 1ddbabfa3bad2292e49add564ee94283ff622c5dae55902f78aa5b4b1d6908b8
    role: context
  - path: data/pathways/nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde.yaml
    sha256: d9712d9291fdec2d7188a31d3eabf54dc198b880c996f39be3e5ada28c4684dc
    role: context
  - path: data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml
    sha256: 36b0c2675cf844a236ee4e20a9f89874f137726026b1a713618cb6b4a51a280a
    role: context
  - path: data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml
    sha256: dc3a803eb1890953f16cf92fe012d9f780aa5e376ec30cfa2fc467cd80645885
    role: context
  - path: data/pathways/nad-salvage-pathway-iv-from-nicotinamide-riboside.yaml
    sha256: f41413a4a24571ece2b3e2d93490f778a1e8b9619c948fc4d6d1825db58d579a
    role: context
  - path: data/pathways/nad-salvage-pathway-v.yaml
    sha256: 5714f5fe02a834e4b4836d61524835501f8eeaa6241d7da5be3f6242ca572d5a
    role: context
  - path: data/pathways/oleate-biosynthesis.yaml
    sha256: 3dcf719e913158bb23184d8ac68a8b6bce55f7f7ef0c69bee8c71a997d2cce2e
    role: context
  - path: data/pathways/palmitoleate-biosynthesis.yaml
    sha256: 47ad28d2b5f793ae9916a213e5b9522248d24e1415c32640f35c4908b6383b9e
    role: context
  - path: data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml
    sha256: 4fa7115243982e1fc30e5f492f66ab43225152be9e14cf114d5c67857af6032f
    role: context
  - path: data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml
    sha256: 37f5e7f93e971f867f00890b758411f59e84117ce1f9a76f310e64e82c5393e8
    role: context
  - path: data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml
    sha256: 41137e969f7960cddb59b6452079b9424b87b0bfaa8402172969c230965cb36a
    role: context
  - path: data/pathways/periplasmic-nad-degradation.yaml
    sha256: 0bba116121063c695033713548f5be6e79a09c875c08754785a86da58fdb7741
    role: context
  - path: data/pathways/phenylalanine-biosynthesis.yaml
    sha256: d83bf9681c328942b0da0101d675687d2772f8017e236df3e813272fe59927d7
    role: context
  - path: data/pathways/phosphatidate-biosynthesis-i-the-dihydroxyacetone-pathway.yaml
    sha256: 5d41048d73ffc521a1d8aeaf79f9ff7ecffd80dffb6bd8915a2e7d512342b455
    role: context
  - path: data/pathways/phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway.yaml
    sha256: f0fb3e3b3a323efe8e435ecff37c2e870f208f0e05dae61c4d417e61a8bac720
    role: context
  - path: data/pathways/phosphatidylcholine-biosynthesis-i.yaml
    sha256: 9707f0bd75a5ade7eff2b25d0d8f8b7953b7749e2cdf2878156c09b9eb1d9d63
    role: context
  - path: data/pathways/phosphatidylethanolamine-biosynthesis-i.yaml
    sha256: c1d5c378d7fff51a6ba181570520d299898891226f4f00662d30b4be6313be9c
    role: context
  - path: data/pathways/phosphatidylinositol-phosphate-biosynthesis.yaml
    sha256: 6e81302207f8ac3a9d1eee0a63cf89b4bed0d6813339819ac96a2d44eec6194b
    role: context
  - path: data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml
    sha256: f32a3b1cf37d1ee31de0900901860a17029ffe49f9d97deb4763f22d4fa580c7
    role: context
  - path: data/pathways/phospholipid-biosynthesis.yaml
    sha256: 69eb1a16bb8baa5beccd8d281522534ff29afe828826aae39532063d6d131669
    role: context
  - path: data/pathways/phospholipids-degradation.yaml
    sha256: fb0b58b847d80f1a68aac342f1974cb6f51171da44ffe3285030454221af5c19
    role: context
  - path: data/pathways/phosphopantothenate-biosynthesis-i.yaml
    sha256: 7d16b766666d040ee91d6e4c56415c69312440fa6f7a3db1482c3f807719c6f0
    role: context
  - path: data/pathways/ppgpp-metabolism.yaml
    sha256: 81e8642cd792bbe351a43638303a7232e92679d2b47e8c308170bc6a0ad36a20
    role: context
  - path: data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml
    sha256: 03219ffa92913bcc306f4824c2c72aa39f862b17d14c96a0a9dd6daa9834bc42
    role: context
  - path: data/pathways/pyridoxal-5-phosphate-salvage-i.yaml
    sha256: 4fa125485b95ff8518056a42c7f22764cac006f812e66effbf250261ee7e4c29
    role: context
  - path: data/pathways/pyruvate-decarboxylation-to-acetyl-coa.yaml
    sha256: 308c60f798bdc3dd8d004c3b5c214dcb9ab4f1ed2a174d169ef4d0958300d145
    role: context
  - path: data/pathways/pyruvate-fermentation-to-acetoin-iii.yaml
    sha256: ad122132b9b414dfdf4aff99f6b26b476cd0cdb98d9dacbfa85ea87f0ac269d6
    role: context
  - path: data/pathways/s-adenosyl-l-methionine-cycle-ii.yaml
    sha256: 81526ec7fcedf14ead1ef9be33747b3560e74f4293e08ac6b6653cf6cb85eb1b
    role: context
  - path: data/pathways/salvage-pathways-of-pyrimidine-ribonucleotides.yaml
    sha256: d283eb6065c21162774b7c8267ab48ce82766a20ce93a37b182bf205e5c14bff
    role: context
  - path: data/pathways/siroheme-biosynthesis.yaml
    sha256: 9bb7972608c907fff78104cff4d93a54af3b5cffd6debfd9be9852d460dc297f
    role: context
  - path: data/pathways/spermidine-biosynthesis-i.yaml
    sha256: 7a59a97a06f5624a7c81b7aba90e909454eafbe37128e044b92fbd92bc82165b
    role: context
  - path: data/pathways/spermine-biosynthesis.yaml
    sha256: abc49bff88359eabe59d05ae6ba0c1255e6937f6748d738220253b31d7744d3c
    role: context
  - path: data/pathways/sphingolipid-biosynthesis-yeast.yaml
    sha256: d75f7d359601e9967fc0f47c0bf369b0c2fbf4759014b6839131600cbf46ef22
    role: context
  - path: data/pathways/sporosarcina-pasteurii-ectoine-biosynthetic-gene-cluster.yaml
    sha256: 0c2e4ef99740885129888a71cf927b1ac8af45e7061c3e3b55ac0913d68dc224
    role: context
  - path: data/pathways/sulfate-activation-for-sulfonation.yaml
    sha256: 3e20747a383ef29d995e2eee4b93040423b7d49b27843c0ec1987edcf6d82588
    role: context
  - path: data/pathways/superoxide-radicals-degradation.yaml
    sha256: 4d0224dd2604fa1cce375b2afa12e614f22e304153734504e03da6e83c797585
    role: context
  - path: data/pathways/tca-cycle-detailed.yaml
    sha256: e98639698c8b4f68286adbeb7d68305a2b3aedcbd9a548bc06feccc91eaf2e39
    role: context
  - path: data/pathways/tetrahydrofolate-biosynthesis.yaml
    sha256: ce15c57307f843c5773b7e5515d09077f8c7c4ef1bbc588e1223d26b4e340690
    role: context
  - path: data/pathways/tetrapyrrole-biosynthesis.yaml
    sha256: b9b73976e6a55b8a24abfd22a8e239733d2f7edd2a746e9e774d5df3fe5e5296
    role: context
  - path: data/pathways/thiamine-biosynthesis.yaml
    sha256: b22273bb29300508a8446c84344cbe568a8ec56858c7d983dd951ba3fd04ca1e
    role: context
  - path: data/pathways/threonine-degradation.yaml
    sha256: 23cce07f43a32645d175d779eabcdfa873a8bcb5d2f2c10171b06cd2fd7dd9ae
    role: context
  - path: data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml
    sha256: be0cf90a07906abd1aec303dc0871e33e97510e961d77e4dcd1649f7fb7f1264
    role: context
  - path: data/pathways/trehalose-biosynthesis-i.yaml
    sha256: 2345d073b0ee434ab1a897653441d1bcd431ba0314e2265b9699fc6fd5a8eefb
    role: context
  - path: data/pathways/triglyceride-biosynthesis.yaml
    sha256: 0ab6fcab3fa418433fffcd68cc992090145bf43c16c1132bddd1e9834a1a6a2f
    role: context
  - path: data/pathways/tryptophan-degradation.yaml
    sha256: 08d5c4115a06db36842a5f384fc5d6f9c0a37f1fdf341d23286bc4e34773ebed
    role: context
  - path: data/pathways/tyrosine-biosynthesis.yaml
    sha256: 441df9779bbf64c1fd7919baac3baa4a3c332668848762ac2ae9f35b2217e967
    role: context
  - path: data/pathways/ubiquinol-6-biosynthesis-from-4-hydroxybenzoate.yaml
    sha256: e4debbe20da1e00f8b304bf272d96f676ac3e6e18e82994fce4f799665cb80fd
    role: context
  - path: data/pathways/udp-n-acetylglucosamine-biosynthesis.yaml
    sha256: 03f1712aa87505464ec9d5f21e56adbce65401d3d554504b23c2fb1a8e603abb
    role: context
  - path: data/pathways/ump-biosynthesis-i.yaml
    sha256: 7360c32e29f0aa492c9b6e3c73b28ec1d1c152258e7efcfd540beb1394546f16
    role: context
  - path: data/pathways/urea-degradation-i.yaml
    sha256: 7c1b0c20488b920bff60f3bd07bedbd9e94d0649af2db5464169a4b5c76bb7b3
    role: context
  - path: data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml
    sha256: dc67a0bd30057f3eb9bebebf4498875a1f841f94e98059447b9b584909a8d43e
    role: context
  - path: data/pathways/valine-degradation.yaml
    sha256: fd0e23fb44bf92196391dfa4b8318fd5b8ae8136c8ebefde13a327348531ccc4
    role: context
  - path: data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml
    sha256: a5ebdc354315545ce4863cca5cbbb07880dc1f9629763a89cdaf93214c566434
    role: context
  - path: data/pathways/xylose-metabolism.yaml
    sha256: 61d17766dddacce9131e18c6f9b4678a7cc43fc304c00b151d2644b389e7be03
    role: context
  - path: data/pathways/zymosterol-biosynthesis.yaml
    sha256: 235d39afd5726b326c67763fb1da02075b60931d32b904050e577c7638cfa8a6
    role: context
  - path: docs/CAUSAL_GRAPHS.md
    sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
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
  - path: reports/causal-graph-diagram-review.json
    sha256: 00a8976bff08eb3bc4f832926fc1c265708a955eda1e7315ed3e6362e2e3739d
    role: context
  - path: reports/causal_graph_review/README.md
    sha256: 426e46d57c2bb7cdef1495fcf14cd93bb7c2523f9efece04d51c9f341a60c7a8
    role: context
  - path: reports/causal_graph_review/README.metacyc.md
    sha256: 58c87ac4c18be92b8c58fe066c7ce87b0ade4e679a0d90fe36b5e3391fb6e1d7
    role: context
  - path: reports/causal_graph_review/adversarial-pr-262.md
    sha256: 7c2b372772f077c93294006eddcb1629237ddaccda2810ad4707918a140d5c8e
    role: context
  - path: reports/causal_graph_review/adversarial-scientific-corrections.json
    sha256: 7ac73054c908e646177b568b78af79078aeb820c03a7c5d65980a177d21db1ab
    role: context
  - path: reports/causal_graph_review/adversarial-validation.json
    sha256: 294f48df3faa374ea0284f7bf989e2331fe9c664aa009e01f42e56813a354fb6
    role: context
  - path: reports/causal_graph_review/all-pathways-summary.json
    sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
    role: context
  - path: reports/causal_graph_review/folate-inositol-chemistry-review.json
    sha256: 2bd802256ba88e4c751a2caf6dd84918a7165c5c5ccf8d46975cce0ddf414c45
    role: context
  - path: reports/causal_graph_review/gocam-assignment-conflicts.json
    sha256: ddf1b088400bf0514068c5ed032393aa1bf8ca047e37bb249a729616a01bdb4c
    role: context
  - path: reports/causal_graph_review/gocam-chemical-corrections.json
    sha256: 9fa09df25c820c6499761dac692d0f97945c90696750bcc7bc48e8553c107c17
    role: context
  - path: reports/causal_graph_review/gocam-chemical-dispositions.json
    sha256: 72c571363b45fbf738e02733b8f89f945dcc191584988752723b4f984a31cf14
    role: context
  - path: reports/causal_graph_review/gocam-chemical-final-supplement.json
    sha256: 5ba4e2917bbc51f0a141db85eec8f14eba716fe54eaf8bcdc665d9e68b0ff130
    role: context
  - path: reports/causal_graph_review/gocam-chemical-final.json
    sha256: 89b46aa08731c922ab6b15ebffe9fbd23bec79844b6025f27d3e738b37396976
    role: context
  - path: reports/causal_graph_review/gocam-chemical-review.json
    sha256: 09673ad832210aa10396c2db6558d381f094929e5bf636e05f50e6c76fe299ca
    role: context
  - path: reports/causal_graph_review/gocam-function-dispositions.json
    sha256: 98b620149511df890ba018e619253ffcd6388b4c2bac6aa0e27e60b4a6d1d1cb
    role: context
  - path: reports/causal_graph_review/gocam-function-review.json
    sha256: e3deedf84a504754d613896d6b31e75c439ce64cd174268cf2109efb8cd372df
    role: context
  - path: reports/causal_graph_review/gocam-function-review.md
    sha256: faaea40ee82a2c3fa75c318451e48e5864b9443f42a8c59e267ecc59568928cf
    role: context
  - path: reports/causal_graph_review/gocam-location-review.json
    sha256: 5c5b3a04c54993675cf1dbb81d20f58ddaee9503338b6dbbc553476a8e9c46fd
    role: context
  - path: reports/causal_graph_review/main-integration-validation.json
    sha256: 71872f08223918c7d146e922309b7c867fca777328167c6fb521c43f673995d2
    role: context
  - path: reports/causal_graph_review/metacyc-identifiers.txt
    sha256: 2c87ad19d44a66b24794e50b7021a248d47f41bb5d2ef8ac1a4e598badd63772
    role: context
  - path: reports/causal_graph_review/metacyc-review.json
    sha256: 86eb3b6d167ec9627977a86d8584d2dd4f9122c5c18647a8bbd9ec669ef4bdd9
    role: context
  - path: reports/causal_graph_review/metacyc-sources.json
    sha256: b0b6b6cef94cd3663d918f7d299886f05395b645c8040316c2f15256ece1939e
    role: context
  - path: reports/causal_graph_review/source-digest-verification.json
    sha256: 36739a6b365d8a82d13f764971d78a2a3fb8aa883681a44b94134ed5f8498374
    role: context
  - path: reports/causal_graph_review/uniprot-cofactor-decisions.json
    sha256: 029aa1e7f4b335bf4bec6da4fb159bc7af730b201753bac175a20c19bb283b87
    role: context
  - path: reports/causal_graph_review/uniprot-cofactor-plan.json
    sha256: bf21b1e310f98541d88a7672073386a324bfa5de35f637394ef36ba64ba34740
    role: context
  - path: reports/causal_graph_review/uniprot-cofactor-review.md
    sha256: 793ccb4b7e5ee28ef4a93f149cf364b78fd306130505441bbae4fe30b727e25c
    role: context
  - path: reports/causal_graph_review/uniprot-source-projection.json
    sha256: 9da77a894b7291a387a7e3ff250aaa8ed076542c67566c6ddd489b0cba073983
    role: context
  - path: reports/causal_graph_review/validation-results.json
    sha256: 8472c25d1502fd23e3e7e70c49cd647fa9e740024517b353907b8d7135e1b7ee
    role: context
  - path: reports/yaml_category_review/20261005-gocam-causal-graphs/complex-composition-review.json
    sha256: 2fd1ab90b907c366e86b55849fb09adabb652368c256a7db2f5a2cfc524a4273
    role: context
  - path: reports/yaml_category_review/20261005-gocam-causal-graphs/gocam-causal-review.json
    sha256: 868912bcc536b5c552dd4af19f592ce6d4de844360823aef98485dd4e1e83b82
    role: context
  - path: reports/yaml_category_review/20261005T062048Z-gocam-causal-graphs.md
    sha256: ac51b53f5d59ec7975e262a4cd574e314d2bf031fdc70019e39fc440d54402ba
    role: target
  - path: reports/yaml_category_review/20261005T064327Z-metacyc-causal-graphs.md
    sha256: 74fa117c29fef032a8a4b24e8af3b20e182f18a11261ffa5454b42767c4af71a
    role: target
  - path: reports/yaml_category_review/20261005T064715Z-diagram-and-mibig-causal-graphs.md
    sha256: c56ac6561f6087a22e3306608b8bce7a71f01452387bee509256edbcd1b57dab
    role: target
  - path: reports/yaml_category_review/20261005T064715Z-gocam-yeast-compartments.md
    sha256: 88fa5c3d6e73ca7d11c973426656038234f5b5d6a7a77fd6d265c9589f36790c
    role: target
  - path: reports/yaml_category_review/20261005T070225Z-folate-inositol-chemistry.md
    sha256: 4781470c19cf02c74aa1087fd14a086920fbd519a76b62845e9da88a75b094a1
    role: target
  - path: reports/yaml_category_review/20261005T071328Z-gocam-chemical-sides.md
    sha256: 7bbc6d69ae0487198c8dfbd0ba2aa6955dddd44a9f855517f7d2c64f8cfc084e
    role: target
  - path: reports/yaml_category_review/20261005T071959Z-all-causal-graphs.md
    sha256: edca5162042fc03f829fa27978000d8a086422449974836061c0d63e261ef702
    role: target
  - path: reports/yaml_record_review/20260925T102834Z-tetrahydrofolate-biosynthesis.md
    sha256: 29a294d413a14fe2d8387fdd6f16871149b8577e5f83417f20429f1ddd34c103
    role: target
  - path: reports/yaml_record_review/20260925T103456Z-utp-and-ctp-de-novo-biosynthesis.md
    sha256: d918277e674fe1c74a16f6efebf42a1dfab230112419a7c98236fe8a1a1572ff
    role: target
  - path: reports/yaml_record_review/20260925T104012Z-adenosine-ribonucleotides-de-novo-biosynthesis.md
    sha256: 12c4a90c5d8da6f239bd70c14e3d64f336bb29cc63185e10c618228fec7d1f44
    role: target
  - path: reports/yaml_record_review/20260925T104540Z-adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.md
    sha256: c4737945ed4c572d29e4bdb89924f8923cfb588619fbc8aaf6c11b89e57f1969
    role: target
  - path: reports/yaml_record_review/20260925T105222Z-gluconeogenesis-i.md
    sha256: f3ff1c4d8bbb722ae9587fef4482a9b1850bc832a2d58288772e8f290bab2d57
    role: target
  - path: reports/yaml_record_review/20260925T110014Z-glycolysis-i-from-glucose-6-phosphate.md
    sha256: 654a2d0957b7a4661d30a29311db116e2be788e45671563a30b414f19fdd73e9
    role: target
  - path: reports/yaml_record_review/20260925T110624Z-mevalonate-pathway.md
    sha256: 3a5a77adc0bc9e01e1fce2e06f53a5903c7085ffa0affbbeaeb289a5215d8611
    role: target
  - path: reports/yaml_record_review/20260925T111145Z-l-lysine-biosynthesis-iv.md
    sha256: 110641dac96d4b08ded517efeecb08580cb616d7f2f67552d8ca345883c3f530
    role: target
  - path: reports/yaml_record_review/20260925T111814Z-phospholipid-biosynthesis.md
    sha256: 6482e2d61da6d26f8e7599adbee0bd9c1a42a235fa8f38fe85f1c66c47f31acc
    role: target
  - path: reports/yaml_record_review/20260925T112308Z-guanosine-ribonucleotides-de-novo-biosynthesis.md
    sha256: 9e7138f84139557d2e780b341a8662790cd56ac3f269d01d07ea5349b7721f74
    role: target
  - path: reports/yaml_record_review/20260925T112914Z-methylglyoxal-catabolism.md
    sha256: 2920839fe5f0c0aedc34f0bb96e5639dabf23ee5ee038492f04ea8d8c716b27c
    role: target
  - path: reports/yaml_record_review/20260925T113418Z-dolichyl-phosphate-d-mannose-biosynthesis.md
    sha256: 8626e7508707ef39c67eef25478f2b9a9aedfbaca0b66742c4efccc6a12a629e
    role: target
  - path: reports/yaml_record_review/20260925T114143Z-thiamine-biosynthesis.md
    sha256: 37baccd1bb7a72696413104b9ce4e90ec70862ec987c3f5e4af72e3bd879dc26
    role: target
  - path: reports/yaml_record_review/20260925T114726Z-phospholipid-biosynthesis-ii-kennedy-pathway.md
    sha256: 0a4720f409431275eb0c11df98daa5ce979a2f4a88a83c7aa5502536eb2d8787
    role: target
  - path: reports/yaml_record_review/20260925T115356Z-valine-degradation.md
    sha256: 6667cbbde770738647104965bc756283d3037bb273359354f04c9ba30b8fd4da
    role: target
  - path: reports/yaml_record_review/20260925T115800Z-phosphatidylcholine-biosynthesis-i.md
    sha256: 6d63c331f77c38370474c9746311b44e39555da7839e6d92f67d85426823a596
    role: target
  - path: reports/yaml_record_review/20260925T120549Z-trans-trans-farnesyl-diphosphate-biosynthesis.md
    sha256: 7830ff73054a3433cbc2cebb28f2a712b93a6e1d7a3b7fcc7e2e76866b14b1d5
    role: target
  - path: reports/yaml_record_review/20260927T042331Z-very-long-chain-fatty-acid-biosynthesis.md
    sha256: 00971bf43c43b8d139e60129479d1749aeb59b3346c7a04865265ca535bc19a0
    role: target
  - path: reports/yaml_record_review/20260927T070312Z-glycogen-catabolism.md
    sha256: 31efd1c0b4ed9de936e015c6a288df2a7a845652cdb700c9f978f07365e009b0
    role: target
  - path: tests/test_folate_inositol_chemistry.py
    sha256: c8cc435f2ba54948670dae7366e0f65a616f888919e0c4754f7561197ee76b55
    role: context
  - path: tests/test_gocam_chemical_identities.py
    sha256: 7001faf55760b0352bf592b09f62ac22676daeb9fd2067b71c2f661fb53bad99
    role: context
targets:
- target_id: legacy-01
  path: reports/yaml_category_review/20261005T062048Z-gocam-causal-graphs.md
  label: 20261005T062048Z-gocam-causal-graphs
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-02
  path: reports/yaml_category_review/20261005T064327Z-metacyc-causal-graphs.md
  label: 20261005T064327Z-metacyc-causal-graphs
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-03
  path: reports/yaml_category_review/20261005T064715Z-diagram-and-mibig-causal-graphs.md
  label: 20261005T064715Z-diagram-and-mibig-causal-graphs
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-04
  path: reports/yaml_category_review/20261005T064715Z-gocam-yeast-compartments.md
  label: 20261005T064715Z-gocam-yeast-compartments
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-05
  path: reports/yaml_category_review/20261005T070225Z-folate-inositol-chemistry.md
  label: 20261005T070225Z-folate-inositol-chemistry
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-06
  path: reports/yaml_category_review/20261005T071328Z-gocam-chemical-sides.md
  label: 20261005T071328Z-gocam-chemical-sides
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-07
  path: reports/yaml_category_review/20261005T071959Z-all-causal-graphs.md
  label: 20261005T071959Z-all-causal-graphs
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-08
  path: reports/yaml_record_review/20260925T102834Z-tetrahydrofolate-biosynthesis.md
  label: 20260925T102834Z-tetrahydrofolate-biosynthesis
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-09
  path: reports/yaml_record_review/20260925T103456Z-utp-and-ctp-de-novo-biosynthesis.md
  label: 20260925T103456Z-utp-and-ctp-de-novo-biosynthesis
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-10
  path: reports/yaml_record_review/20260925T104012Z-adenosine-ribonucleotides-de-novo-biosynthesis.md
  label: 20260925T104012Z-adenosine-ribonucleotides-de-novo-biosynthesis
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-11
  path: reports/yaml_record_review/20260925T104540Z-adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.md
  label: 20260925T104540Z-adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-12
  path: reports/yaml_record_review/20260925T105222Z-gluconeogenesis-i.md
  label: 20260925T105222Z-gluconeogenesis-i
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-13
  path: reports/yaml_record_review/20260925T110014Z-glycolysis-i-from-glucose-6-phosphate.md
  label: 20260925T110014Z-glycolysis-i-from-glucose-6-phosphate
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-14
  path: reports/yaml_record_review/20260925T110624Z-mevalonate-pathway.md
  label: 20260925T110624Z-mevalonate-pathway
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-15
  path: reports/yaml_record_review/20260925T111145Z-l-lysine-biosynthesis-iv.md
  label: 20260925T111145Z-l-lysine-biosynthesis-iv
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-16
  path: reports/yaml_record_review/20260925T111814Z-phospholipid-biosynthesis.md
  label: 20260925T111814Z-phospholipid-biosynthesis
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-17
  path: reports/yaml_record_review/20260925T112308Z-guanosine-ribonucleotides-de-novo-biosynthesis.md
  label: 20260925T112308Z-guanosine-ribonucleotides-de-novo-biosynthesis
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-18
  path: reports/yaml_record_review/20260925T112914Z-methylglyoxal-catabolism.md
  label: 20260925T112914Z-methylglyoxal-catabolism
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-19
  path: reports/yaml_record_review/20260925T113418Z-dolichyl-phosphate-d-mannose-biosynthesis.md
  label: 20260925T113418Z-dolichyl-phosphate-d-mannose-biosynthesis
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-20
  path: reports/yaml_record_review/20260925T114143Z-thiamine-biosynthesis.md
  label: 20260925T114143Z-thiamine-biosynthesis
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-21
  path: reports/yaml_record_review/20260925T114726Z-phospholipid-biosynthesis-ii-kennedy-pathway.md
  label: 20260925T114726Z-phospholipid-biosynthesis-ii-kennedy-pathway
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-22
  path: reports/yaml_record_review/20260925T115356Z-valine-degradation.md
  label: 20260925T115356Z-valine-degradation
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-23
  path: reports/yaml_record_review/20260925T115800Z-phosphatidylcholine-biosynthesis-i.md
  label: 20260925T115800Z-phosphatidylcholine-biosynthesis-i
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-24
  path: reports/yaml_record_review/20260925T120549Z-trans-trans-farnesyl-diphosphate-biosynthesis.md
  label: 20260925T120549Z-trans-trans-farnesyl-diphosphate-biosynthesis
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-25
  path: reports/yaml_record_review/20260927T042331Z-very-long-chain-fatty-acid-biosynthesis.md
  label: 20260927T042331Z-very-long-chain-fatty-acid-biosynthesis
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
- target_id: legacy-26
  path: reports/yaml_record_review/20260927T070312Z-glycogen-catabolism.md
  label: 20260927T070312Z-glycogen-catabolism
  kind: source
  ownership_note: Immutable historical review; future fixes belong to the maintained
    pathway or generator named in this report.
scope:
  description: Bounded reconciliation of legacy report findings, recommendations and
    later integrated evidence; no fresh scientific or literature review.
  selection: All 19 Markdown files under reports/yaml_record_review and all 7 top-level
    Markdown files under reports/yaml_category_review present at initial inspection.
  coverage: full
  population_size: 26
  reviewed_target_ids:
  - legacy-01
  - legacy-02
  - legacy-03
  - legacy-04
  - legacy-05
  - legacy-06
  - legacy-07
  - legacy-08
  - legacy-09
  - legacy-10
  - legacy-11
  - legacy-12
  - legacy-13
  - legacy-14
  - legacy-15
  - legacy-16
  - legacy-17
  - legacy-18
  - legacy-19
  - legacy-20
  - legacy-21
  - legacy-22
  - legacy-23
  - legacy-24
  - legacy-25
  - legacy-26
  exclusions:
  - target: data/pathways/chromobacterium-violaceum-violacein-biosynthetic-gene-cluster.yaml
    reason: Later pathway outside the 152-record historical category cohort; current
      deterministic gates only.
  - target: data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml
    reason: Later pathway outside the 152-record historical category cohort; current
      deterministic gates only.
  - target: data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml
    reason: Later pathway outside the 152-record historical category cohort; current
      deterministic gates only.
  - target: data/pathways/mycobacterium-sulfate-assimilation.yaml
    reason: Later pathway outside the 152-record historical category cohort; current
      deterministic gates only.
  - target: data/pathways/sporosarcina-pasteurii-ectoine-biosynthetic-gene-cluster.yaml
    reason: Later pathway outside the 152-record historical category cohort; current
      deterministic gates only.
checks:
- check_id: inventory
  name: Review inventory and prior structured-bundle check
  required: true
  status: passed
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  summary: No pre-existing structured reviews; 26 selected legacy reports read in
    full. No structured lineage to retire.
  target_ids:
  - legacy-01
  - legacy-02
  - legacy-03
  - legacy-04
  - legacy-05
  - legacy-06
  - legacy-07
  - legacy-08
  - legacy-09
  - legacy-10
  - legacy-11
  - legacy-12
  - legacy-13
  - legacy-14
  - legacy-15
  - legacy-16
  - legacy-17
  - legacy-18
  - legacy-19
  - legacy-20
  - legacy-21
  - legacy-22
  - legacy-23
  - legacy-24
  - legacy-25
  - legacy-26
  evidence_ids:
  - e119
- check_id: ledger-currentness
  name: Final integrated target hash verification
  required: true
  status: passed
  summary: All 152 historical category targets match their final integrated reviewed
    hashes. All 19 individual-review targets are included.
  target_ids:
  - legacy-01
  - legacy-02
  - legacy-03
  - legacy-04
  - legacy-05
  - legacy-06
  - legacy-07
  - legacy-08
  - legacy-09
  - legacy-10
  - legacy-11
  - legacy-12
  - legacy-13
  - legacy-14
  - legacy-15
  - legacy-16
  - legacy-17
  - legacy-18
  - legacy-19
  - legacy-20
  - legacy-21
  - legacy-22
  - legacy-23
  - legacy-24
  - legacy-25
  - legacy-26
  evidence_ids:
  - e120
- check_id: validate
  name: 'Required local gate: validate'
  required: true
  status: passed
  command: just validate
  exit_code: 0
  summary: 'Passed skill validation and full QC: 157 pathway records, closed schema,
    identifiers/labels, 8,263 evidence blocks, 30 sources, documentation, deep-research
    contract, history, and generated pages current.'
  target_ids:
  - legacy-01
  - legacy-02
  - legacy-03
  - legacy-04
  - legacy-05
  - legacy-06
  - legacy-07
  - legacy-08
  - legacy-09
  - legacy-10
  - legacy-11
  - legacy-12
  - legacy-13
  - legacy-14
  - legacy-15
  - legacy-16
  - legacy-17
  - legacy-18
  - legacy-19
  - legacy-20
  - legacy-21
  - legacy-22
  - legacy-23
  - legacy-24
  - legacy-25
  - legacy-26
  evidence_ids:
  - e121
- check_id: test
  name: 'Required local gate: test'
  required: true
  status: passed
  command: just test
  exit_code: 0
  summary: Full repository pytest passed. This is deterministic regression coverage,
    not a literature reassessment. 981 passed, 3 skipped, 3 warnings in 277.97s (0:04:37)
  target_ids:
  - legacy-01
  - legacy-02
  - legacy-03
  - legacy-04
  - legacy-05
  - legacy-06
  - legacy-07
  - legacy-08
  - legacy-09
  - legacy-10
  - legacy-11
  - legacy-12
  - legacy-13
  - legacy-14
  - legacy-15
  - legacy-16
  - legacy-17
  - legacy-18
  - legacy-19
  - legacy-20
  - legacy-21
  - legacy-22
  - legacy-23
  - legacy-24
  - legacy-25
  - legacy-26
  evidence_ids:
  - e122
- check_id: lint
  name: 'Required local gate: lint'
  required: true
  status: passed
  command: just lint
  exit_code: 0
  summary: Full repository Ruff check passed.
  target_ids:
  - legacy-01
  - legacy-02
  - legacy-03
  - legacy-04
  - legacy-05
  - legacy-06
  - legacy-07
  - legacy-08
  - legacy-09
  - legacy-10
  - legacy-11
  - legacy-12
  - legacy-13
  - legacy-14
  - legacy-15
  - legacy-16
  - legacy-17
  - legacy-18
  - legacy-19
  - legacy-20
  - legacy-21
  - legacy-22
  - legacy-23
  - legacy-24
  - legacy-25
  - legacy-26
  evidence_ids:
  - e123
- check_id: diff
  name: 'Required local gate: diff'
  required: true
  status: passed
  command: git diff --check
  exit_code: 0
  summary: Whitespace/error check passed for the tracked patch at assessment time.
    Untracked new files were outside that command scope.
  target_ids:
  - legacy-01
  - legacy-02
  - legacy-03
  - legacy-04
  - legacy-05
  - legacy-06
  - legacy-07
  - legacy-08
  - legacy-09
  - legacy-10
  - legacy-11
  - legacy-12
  - legacy-13
  - legacy-14
  - legacy-15
  - legacy-16
  - legacy-17
  - legacy-18
  - legacy-19
  - legacy-20
  - legacy-21
  - legacy-22
  - legacy-23
  - legacy-24
  - legacy-25
  - legacy-26
  evidence_ids:
  - e124
- check_id: skill
  name: 'Required local gate: skill'
  required: true
  status: passed
  command: .venv/bin/python /Users/marcin/.codex/skills/.system/skill-creator/scripts/quick_validate.py
    .claude/skills/pathwaymech-resolve-reviews
  exit_code: 0
  summary: Skill-creator frontmatter and scaffold validation passed for the new resolver.
  target_ids:
  - legacy-01
  - legacy-02
  - legacy-03
  - legacy-04
  - legacy-05
  - legacy-06
  - legacy-07
  - legacy-08
  - legacy-09
  - legacy-10
  - legacy-11
  - legacy-12
  - legacy-13
  - legacy-14
  - legacy-15
  - legacy-16
  - legacy-17
  - legacy-18
  - legacy-19
  - legacy-20
  - legacy-21
  - legacy-22
  - legacy-23
  - legacy-24
  - legacy-25
  - legacy-26
  evidence_ids:
  - e125
evidence:
- evidence_id: e001
  kind: prior_review
  reference: reports/yaml_category_review/20261005T062048Z-gocam-causal-graphs.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical category corrections and followup handoffs read in full and
    reconciled with later integrated audit evidence.
  snapshot_sha256: ac51b53f5d59ec7975e262a4cd574e314d2bf031fdc70019e39fc440d54402ba
- evidence_id: e002
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: '#/records/*/sha256'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Every one of this report's 86 targets exactly matches the final integrated
    reviewed bytes; see per_target_hash_verification.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e003
  kind: record_content
  reference: data/pathways/threonine-degradation.yaml
  locator: '#/participants/7; #/mechanistic_edges/7'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: UniProtKB:P37303 is the preserved GLY1 participant and enables GO:0004793;
    current reviewed graph remains bounded.
  snapshot_sha256: 23cce07f43a32645d175d779eabcdfa873a8bcb5d2f2c10171b06cd2fd7dd9ae
- evidence_id: e004
  kind: record_content
  reference: data/pathways/sphingolipid-biosynthesis-yeast.yaml
  locator: mechanistic_edges[id=location-f1f67fe5b506] (lines 2342-2353)
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: gomodel:RXN3O-663 occurs_in GO:0005794 with CPX-1739.json#/functions/0
    as the independent activity-location source.
  snapshot_sha256: d75f7d359601e9967fc0f47c0bf369b0c2fbf4759014b6839131600cbf46ef22
- evidence_id: e005
  kind: record_content
  reference: reports/causal_graph_review/gocam-location-review.json
  locator: '#/summary'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Subsequent ledger explicitly records 163 quarantined cytosol assertions
    and 108 independent location gaps; prevents mistaking the early native-stage context
    for final assertions.
  snapshot_sha256: 5c5b3a04c54993675cf1dbb81d20f58ddaee9503338b6dbbc553476a8e9c46fd
- evidence_id: e006
  kind: prior_review
  reference: reports/yaml_category_review/20261005T064327Z-metacyc-causal-graphs.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical category corrections and followup handoffs read in full and
    reconciled with later integrated audit evidence.
  snapshot_sha256: 74fa117c29fef032a8a4b24e8af3b20e182f18a11261ffa5454b42767c4af71a
- evidence_id: e007
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: '#/records/*/sha256'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Every one of this report's 50 targets exactly matches the final integrated
    reviewed bytes; see per_target_hash_verification.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e008
  kind: record_content
  reference: reports/causal_graph_review/metacyc-review.json
  locator: per-record dispositions
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Detailed historical dispositions enumerate the 50-record source cohort;
    every current target matches the later final integrated hash.
  snapshot_sha256: 86eb3b6d167ec9627977a86d8584d2dd4f9122c5c18647a8bbd9ec669ef4bdd9
- evidence_id: e009
  kind: record_content
  reference: reports/causal_graph_review/main-integration-validation.json
  locator: '#/checks/render; #/checks/kgx; #/checks/qc; #/download_audit'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Parent render/export/QC followups are historically recorded as completed
    with exit 0, and source evidence/reference arrays were checked exactly.
  snapshot_sha256: 71872f08223918c7d146e922309b7c867fca777328167c6fb521c43f673995d2
- evidence_id: e010
  kind: prior_review
  reference: reports/yaml_category_review/20261005T064715Z-diagram-and-mibig-causal-graphs.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical category corrections and followup handoffs read in full and
    reconciled with later integrated audit evidence.
  snapshot_sha256: c56ac6561f6087a22e3306608b8bce7a71f01452387bee509256edbcd1b57dab
- evidence_id: e011
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: '#/records/*/sha256'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Every one of this report's 16 targets exactly matches the final integrated
    reviewed bytes; see per_target_hash_verification.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e012
  kind: record_content
  reference: data/pathways/mycothiol-biosynthesis.yaml
  locator: '#/description (lines 3-7)'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Explicit unresolved phosphatase and ImpC histidinol-phosphatase reassignment
    remain in current maintained description.
  snapshot_sha256: 35dfb77de4fcc447aeb649bb478c6a840e78ab39f5921469a154ec3768c32f4f
- evidence_id: e013
  kind: record_content
  reference: data/pathways/linearmycin-biosynthetic-gene-cluster.yaml
  locator: '#/description'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: The record explicitly says assembly steps remain proposed; its final ledger/current
    hash matches four supported edges.
  snapshot_sha256: a5a908285f06357add5292777ea7be2226263c1448097361f9b3d87be0001cbe
- evidence_id: e014
  kind: record_content
  reference: data/pathways/glutathione-glutaredoxin-redox-reaction.yaml
  locator: '#/description (lines 3-6)'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Unresolved glutaredoxin redox partner remains explicitly scoped rather
    than invented.
  snapshot_sha256: 670795c76c89c998d015e40536a5aba90acccb1430e7b4649aef2f738bad5e1b
- evidence_id: e015
  kind: record_content
  reference: reports/causal_graph_review/adversarial-scientific-corrections.json
  locator: '#/records/0'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Later choline classification correction supersedes an intermediate diagram-stage
    decision; all current files match the later integrated ledger.
  snapshot_sha256: 7ac73054c908e646177b568b78af79078aeb820c03a7c5d65980a177d21db1ab
- evidence_id: e016
  kind: prior_review
  reference: reports/yaml_category_review/20261005T064715Z-gocam-yeast-compartments.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical category corrections and followup handoffs read in full and
    reconciled with later integrated audit evidence.
  snapshot_sha256: 88fa5c3d6e73ca7d11c973426656038234f5b5d6a7a77fd6d265c9589f36790c
- evidence_id: e017
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: '#/records/*/sha256'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Every one of this report's 85 targets exactly matches the final integrated
    reviewed bytes; see per_target_hash_verification.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e018
  kind: record_content
  reference: reports/causal_graph_review/gocam-location-review.json
  locator: '#/summary/activity_decisions'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: 204 compatible native assertions, 108 independent gaps, 163 quarantined
    conflicting cytosol assertions remain an exhaustive historical decision ledger.
  snapshot_sha256: 5c5b3a04c54993675cf1dbb81d20f58ddaee9503338b6dbbc553476a8e9c46fd
- evidence_id: e019
  kind: record_content
  reference: reports/causal_graph_review/gocam-function-dispositions.json
  locator: '#/records[accession=P10127]'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: ADH4 physiological ethanol-oxidation branch excluded; higher-alcohol source
    contexts retain bounded specificity.
  snapshot_sha256: 98b620149511df890ba018e619253ffcd6388b4c2bac6aa0e27e60b4a6d1d1cb
- evidence_id: e020
  kind: record_content
  reference: data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml
  locator: '#/reactions/3; #/mechanistic_edges/28; #/mechanistic_edges/30'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: ADK2 activity is GTP:AMP phosphotransferase, with CHEBI:37565 input and
    CHEBI:58189 output.
  snapshot_sha256: 3840e82b7a5d9809e754222ac412b4321f3b99e73e085a3efdb9fbe6b402c9ef
- evidence_id: e021
  kind: record_content
  reference: tests/test_gocam_chemical_identities.py
  locator: test_arg2_and_arg7_acetyl_glutamate_labels_have_located_independent_evidence;
    test_fox2_stereochemistry_and_distinct_dci1_eci1_chemistry
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Existing regressions inspect the maintained ARG2/ARG7 labels and separate
    DCI1/ECI1 chemistry; full parent test gate pending this subtask.
  snapshot_sha256: 7001faf55760b0352bf592b09f62ac22676daeb9fd2067b71c2f661fb53bad99
- evidence_id: e022
  kind: prior_review
  reference: reports/yaml_category_review/20261005T070225Z-folate-inositol-chemistry.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical category corrections and followup handoffs read in full and
    reconciled with later integrated audit evidence.
  snapshot_sha256: 4781470c19cf02c74aa1087fd14a086920fbd519a76b62845e9da88a75b094a1
- evidence_id: e023
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: '#/records/*/sha256'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Every one of this report's 2 targets exactly matches the final integrated
    reviewed bytes; see per_target_hash_verification.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e024
  kind: record_content
  reference: data/pathways/folate-interconversions.yaml
  locator: '#/mechanistic_edges/62; #/mechanistic_edges/87'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: MET13 output CHEBI:58349 and input CHEBI:57783 retain explicit NADPH/NADP
    source rationale.
  snapshot_sha256: 6774526812ae134d049d2bd6f36941ff0d4453558aa68259a790e93149278d6a
- evidence_id: e025
  kind: record_content
  reference: data/pathways/inositol-phosphate-biosynthesis.yaml
  locator: '#/reactions/14; #/mechanistic_edges/107 through /112'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: RHEA:79724 has exact hydrolysis endpoints and enzyme edge explicitly limited
    to in-vitro recombinant domain activity, without physiological flux or S. pombe
    phenotype transfer.
  snapshot_sha256: add22f805f7a14a195c64a04e8b070f98c68626b30e768898e843213e7809fcc
- evidence_id: e026
  kind: record_content
  reference: tests/test_folate_inositol_chemistry.py
  locator: six maintained-record tests
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Existing record assertions cover folate identity, distinct cofactor specificity,
    three shared-intermediate flow edges, inositol isomers, generic identities and
    qualified domain hydrolysis; execution delegated to parent full suite.
  snapshot_sha256: c8cc435f2ba54948670dae7366e0f65a616f888919e0c4754f7561197ee76b55
- evidence_id: e027
  kind: prior_review
  reference: reports/yaml_category_review/20261005T071328Z-gocam-chemical-sides.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical category corrections and followup handoffs read in full and
    reconciled with later integrated audit evidence.
  snapshot_sha256: 7bbc6d69ae0487198c8dfbd0ba2aa6955dddd44a9f855517f7d2c64f8cfc084e
- evidence_id: e028
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: '#/records/*/sha256'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Every one of this report's 85 targets exactly matches the final integrated
    reviewed bytes; see per_target_hash_verification.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e029
  kind: record_content
  reference: reports/causal_graph_review/gocam-chemical-dispositions.json
  locator: '#/activities (475 rows); #/added_activities/0'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Complete historical original-to-final activity dispositions retain exact
    source pointers and amendment ledger references; current 85-target bytes match
    the integrated final ledger.
  snapshot_sha256: 72c571363b45fbf738e02733b8f89f945dcc191584988752723b4f984a31cf14
- evidence_id: e030
  kind: record_content
  reference: reports/causal_graph_review/gocam-function-dispositions.json
  locator: '#/records[accession=P15700]'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: CMP phosphorylation remains explicitly qualified as disputed, preserving
    opposing source identifiers.
  snapshot_sha256: 98b620149511df890ba018e619253ffcd6388b4c2bac6aa0e27e60b4a6d1d1cb
- evidence_id: e031
  kind: record_content
  reference: tests/test_gocam_chemical_identities.py
  locator: seven maintained-record regression cases
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current acceptance assertions cover named correction groups; parent full
    test suite supplies execution evidence.
  snapshot_sha256: 7001faf55760b0352bf592b09f62ac22676daeb9fd2067b71c2f661fb53bad99
- evidence_id: e032
  kind: prior_review
  reference: reports/yaml_category_review/20261005T071959Z-all-causal-graphs.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical category corrections and followup handoffs read in full and
    reconciled with later integrated audit evidence.
  snapshot_sha256: edca5162042fc03f829fa27978000d8a086422449974836061c0d63e261ef702
- evidence_id: e033
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: '#/records/*/sha256'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Every one of this report's 152 targets exactly matches the final integrated
    reviewed bytes; see per_target_hash_verification.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e034
  kind: record_content
  reference: reports/causal_graph_review/README.md
  locator: Graph and Evidence Patterns; Additional Notes
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Later overview explicitly records final 3599 participants, 814 reactions,
    7134 edges and THI13/ARG82 adversarial dispositions.
  snapshot_sha256: 426e46d57c2bb7cdef1495fcf14cd93bb7c2523f9efece04d51c9f341a60c7a8
- evidence_id: e035
  kind: record_content
  reference: reports/causal_graph_review/adversarial-pr-262.md
  locator: 'issues #263-#270 table'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Eight genuine historical issues have explicit correction and acceptance
    evidence; reports are preserved rather than retroactively rewritten.
  snapshot_sha256: 7c2b372772f077c93294006eddcb1629237ddaccda2810ad4707918a140d5c8e
- evidence_id: e036
  kind: record_content
  reference: data/pathways/thiamine-biosynthesis.yaml
  locator: '#/mechanistic_edges/75; #/mechanistic_edges/79 through /83'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: THI13 keeps only bounded protein-bound histidyl/PLP inputs and HMP-P output,
    explicitly inferred by similarity; detailed products and balance remain unresolved.
  snapshot_sha256: b22273bb29300508a8446c84344cbe568a8ec56858c7d983dd951ba3fd04ca1e
- evidence_id: e037
  kind: record_content
  reference: reports/causal_graph_review/main-integration-validation.json
  locator: '#/checks/tests; #/tests; #/download_audit'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: 'Historical whole-suite exit 1 is not misreported: page-generation race
    was explicitly explained and browser test rechecked successfully. Current parent
    full-suite run must supply fresh current gate outcome.'
  snapshot_sha256: 71872f08223918c7d146e922309b7c867fca777328167c6fb521c43f673995d2
- evidence_id: e038
  kind: prior_review
  reference: reports/yaml_record_review/20260925T102834Z-tetrahydrofolate-biosynthesis.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 29a294d413a14fe2d8387fdd6f16871149b8577e5f83417f20429f1ddd34c103
- evidence_id: e039
  kind: record_content
  reference: data/pathways/tetrahydrofolate-biosynthesis.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: ce15c57307f843c5773b7e5515d09077f8c7c4ef1bbc588e1223d26b4e340690
- evidence_id: e040
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/134
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e041
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e042
  kind: prior_review
  reference: reports/yaml_record_review/20260925T103456Z-utp-and-ctp-de-novo-biosynthesis.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: d918277e674fe1c74a16f6efebf42a1dfab230112419a7c98236fe8a1a1572ff
- evidence_id: e043
  kind: record_content
  reference: data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: dc67a0bd30057f3eb9bebebf4498875a1f841f94e98059447b9b584909a8d43e
- evidence_id: e044
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/147
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e045
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e046
  kind: prior_review
  reference: reports/yaml_record_review/20260925T104012Z-adenosine-ribonucleotides-de-novo-biosynthesis.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 12c4a90c5d8da6f239bd70c14e3d64f336bb29cc63185e10c618228fec7d1f44
- evidence_id: e047
  kind: record_content
  reference: data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: 3840e82b7a5d9809e754222ac412b4321f3b99e73e085a3efdb9fbe6b402c9ef
- evidence_id: e048
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/9
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e049
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e050
  kind: prior_review
  reference: reports/yaml_record_review/20260925T104540Z-adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: c4737945ed4c572d29e4bdb89924f8923cfb588619fbc8aaf6c11b89e57f1969
- evidence_id: e051
  kind: record_content
  reference: data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: 3cd2f4ba0bdbd27028fad8814a024a16cdca397bc09764ecba2597826bfc0625
- evidence_id: e052
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/8
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e053
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e054
  kind: record_content
  reference: reports/causal_graph_review/gocam-chemical-dispositions.json
  locator: /activities/9
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: 72c571363b45fbf738e02733b8f89f945dcc191584988752723b4f984a31cf14
- evidence_id: e055
  kind: prior_review
  reference: reports/yaml_record_review/20260925T105222Z-gluconeogenesis-i.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: f3ff1c4d8bbb722ae9587fef4482a9b1850bc832a2d58288772e8f290bab2d57
- evidence_id: e056
  kind: record_content
  reference: data/pathways/gluconeogenesis-i.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: 365e9c29df8a62dd3dd5d4a3a190e530f6e3beae4a8e159be04ec9e4a9a952ba
- evidence_id: e057
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/37
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e058
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e059
  kind: prior_review
  reference: reports/yaml_record_review/20260925T110014Z-glycolysis-i-from-glucose-6-phosphate.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 654a2d0957b7a4661d30a29311db116e2be788e45671563a30b414f19fdd73e9
- evidence_id: e060
  kind: record_content
  reference: data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: ce99470da6b66a527a1a7ffe4e46e059afa4af75496a8fca96f2831049410be6
- evidence_id: e061
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/46
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e062
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e063
  kind: prior_review
  reference: reports/yaml_record_review/20260925T110624Z-mevalonate-pathway.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 3a5a77adc0bc9e01e1fce2e06f53a5903c7085ffa0affbbeaeb289a5215d8611
- evidence_id: e064
  kind: record_content
  reference: data/pathways/mevalonate-pathway.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: 25a739d9e28a0dfaabc31f59bcaa98179ca4377f501a0f8a8a869039b786afdb
- evidence_id: e065
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/93
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e066
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e067
  kind: prior_review
  reference: reports/yaml_record_review/20260925T111145Z-l-lysine-biosynthesis-iv.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 110641dac96d4b08ded517efeecb08580cb616d7f2f67552d8ca345883c3f530
- evidence_id: e068
  kind: record_content
  reference: data/pathways/l-lysine-biosynthesis-iv.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: 7f6375da56c7c53b27a336f385c71564c46ad7700e397063915bf6d6bdd18530
- evidence_id: e069
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/73
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e070
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e071
  kind: prior_review
  reference: reports/yaml_record_review/20260925T111814Z-phospholipid-biosynthesis.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 6482e2d61da6d26f8e7599adbee0bd9c1a42a235fa8f38fe85f1c66c47f31acc
- evidence_id: e072
  kind: record_content
  reference: data/pathways/phospholipid-biosynthesis.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: 69eb1a16bb8baa5beccd8d281522534ff29afe828826aae39532063d6d131669
- evidence_id: e073
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/117
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e074
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e075
  kind: prior_review
  reference: reports/yaml_record_review/20260925T112308Z-guanosine-ribonucleotides-de-novo-biosynthesis.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 9e7138f84139557d2e780b341a8662790cd56ac3f269d01d07ea5349b7721f74
- evidence_id: e076
  kind: record_content
  reference: data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: 65c619b8dfdd73062ad25ec9757f617da2a1a5739502ea44004be38e20897df0
- evidence_id: e077
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/48
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e078
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e079
  kind: prior_review
  reference: reports/yaml_record_review/20260925T112914Z-methylglyoxal-catabolism.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 2920839fe5f0c0aedc34f0bb96e5639dabf23ee5ee038492f04ea8d8c716b27c
- evidence_id: e080
  kind: record_content
  reference: data/pathways/methylglyoxal-catabolism.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: 4e0655e6c340986dbb79f846b237550d6d793e7ae5781d576df4fbd6fa5f1ba1
- evidence_id: e081
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/92
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e082
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e083
  kind: prior_review
  reference: reports/yaml_record_review/20260925T113418Z-dolichyl-phosphate-d-mannose-biosynthesis.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 8626e7508707ef39c67eef25478f2b9a9aedfbaca0b66742c4efccc6a12a629e
- evidence_id: e084
  kind: record_content
  reference: data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: acc8b361993a1db31e3bf253e05526b2998b7a91c0cf3b0e6628aaf530adb688
- evidence_id: e085
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/26
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e086
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e087
  kind: prior_review
  reference: reports/yaml_record_review/20260925T114143Z-thiamine-biosynthesis.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 37baccd1bb7a72696413104b9ce4e90ec70862ec987c3f5e4af72e3bd879dc26
- evidence_id: e088
  kind: record_content
  reference: data/pathways/thiamine-biosynthesis.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: b22273bb29300508a8446c84344cbe568a8ec56858c7d983dd951ba3fd04ca1e
- evidence_id: e089
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/136
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e090
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e091
  kind: record_content
  reference: reports/yaml_category_review/20261005T071959Z-all-causal-graphs.md
  locator: remaining thiazole bridge gap; thiamine per-record entry
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: edca5162042fc03f829fa27978000d8a086422449974836061c0d63e261ef702
- evidence_id: e092
  kind: prior_review
  reference: reports/yaml_record_review/20260925T114726Z-phospholipid-biosynthesis-ii-kennedy-pathway.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 0a4720f409431275eb0c11df98daa5ce979a2f4a88a83c7aa5502536eb2d8787
- evidence_id: e093
  kind: record_content
  reference: data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: f32a3b1cf37d1ee31de0900901860a17029ffe49f9d97deb4763f22d4fa580c7
- evidence_id: e094
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/116
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e095
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e096
  kind: prior_review
  reference: reports/yaml_record_review/20260925T115356Z-valine-degradation.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 6667cbbde770738647104965bc756283d3037bb273359354f04c9ba30b8fd4da
- evidence_id: e097
  kind: record_content
  reference: data/pathways/valine-degradation.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: fd0e23fb44bf92196391dfa4b8318fd5b8ae8136c8ebefde13a327348531ccc4
- evidence_id: e098
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/148
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e099
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e100
  kind: prior_review
  reference: reports/yaml_record_review/20260925T115800Z-phosphatidylcholine-biosynthesis-i.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 6d63c331f77c38370474c9746311b44e39555da7839e6d92f67d85426823a596
- evidence_id: e101
  kind: record_content
  reference: data/pathways/phosphatidylcholine-biosynthesis-i.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: 9707f0bd75a5ade7eff2b25d0d8f8b7953b7749e2cdf2878156c09b9eb1d9d63
- evidence_id: e102
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/113
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e103
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e104
  kind: prior_review
  reference: reports/yaml_record_review/20260925T120549Z-trans-trans-farnesyl-diphosphate-biosynthesis.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 7830ff73054a3433cbc2cebb28f2a712b93a6e1d7a3b7fcc7e2e76866b14b1d5
- evidence_id: e105
  kind: record_content
  reference: data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: be0cf90a07906abd1aec303dc0871e33e97510e961d77e4dcd1649f7fb7f1264
- evidence_id: e106
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/138
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e107
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e108
  kind: prior_review
  reference: reports/yaml_record_review/20260927T042331Z-very-long-chain-fatty-acid-biosynthesis.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 00971bf43c43b8d139e60129479d1749aeb59b3346c7a04865265ca535bc19a0
- evidence_id: e109
  kind: record_content
  reference: data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: a5ebdc354315545ce4863cca5cbbb07880dc1f9629763a89cdaf93214c566434
- evidence_id: e110
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/149
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e111
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e112
  kind: record_content
  reference: reports/yaml_category_review/20261005-gocam-causal-graphs/gocam-causal-review.json
  locator: /records/83/facts/36
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: 868912bcc536b5c552dd4af19f592ce6d4de844360823aef98485dd4e1e83b82
- evidence_id: e113
  kind: record_content
  reference: reports/causal_graph_review/gocam-chemical-dispositions.json
  locator: /activities/460
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: 72c571363b45fbf738e02733b8f89f945dcc191584988752723b4f984a31cf14
- evidence_id: e114
  kind: prior_review
  reference: reports/yaml_record_review/20260927T070312Z-glycogen-catabolism.md
  locator: Entire report, including Findings, Recommended Edits, Follow-up Checks
    and limitations
  accessed_at: '2026-10-09T07:06:50Z'
  support: context_only
  summary: Historical pass with no corrective findings; conditional recommendations
    reassessed.
  snapshot_sha256: 31efd1c0b4ed9de936e015c6a288df2a7a845652cdb700c9f978f07365e009b0
- evidence_id: e115
  kind: record_content
  reference: data/pathways/glycogen-catabolism.yaml
  locator: /description; /participants; /reactions; /mechanistic_edges; /references;
    /curation_history
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: fc91636aa102a87bcb65d173ff28b2acbb356ea67beb831e00e7a93d9ae52aa4
- evidence_id: e116
  kind: record_content
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: /records/45
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Current maintained bytes and field context inspected; the current target
    hash matches its later final integrated ledger entry.
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e117
  kind: record_content
  reference: docs/CAUSAL_GRAPHS.md
  locator: Components and relations; Evidence and provenance
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: aff52358f7a8abee85f488da1f0d88b669caa48ccb153d7b0467f5f1637c610e
- evidence_id: e118
  kind: record_content
  reference: reports/yaml_category_review/20261005T064715Z-diagram-and-mibig-causal-graphs.md
  locator: 'Exhaustive per-record dispositions: glycogen-catabolism'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Inspected current field content or local relation rubric for the historical
    followup.
  snapshot_sha256: c56ac6561f6087a22e3306608b8bce7a71f01452387bee509256edbcd1b57dab
- evidence_id: e119
  kind: search
  reference: Local review inventory
  locator: reviews/structured; reports/yaml_record_review; reports/yaml_category_review;
    supporting reports/causal_graph_review
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Gitignore-independent filesystem and rg --no-ignore --hidden inventories
    found 19 individual and 7 top-level category Markdown reports; no existing structured
    bundle in the original or task checkout. Raw ledgers were used as context. No
    claim of absence outside these roots.
  search_scope: Original PathwayMech checkout and isolated worktree review roots;
    ignored, hidden and untracked entries included; .git internals, virtualenvs and
    unrelated worktrees excluded.
- evidence_id: e120
  kind: validation
  reference: reports/causal_graph_review/all-pathways-summary.json
  locator: '#/records/*/sha256'
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: 'Recomputed SHA-256 for all 152 final-ledger targets: 152 match current
    bytes and initial inspection, zero mismatches. Final ledger cohort contains 7,134
    edges; older prose totals are intermediate historical counts, not corrective targets.'
  snapshot_sha256: 0e1c8ca98325ac199dd5be9060d08978c268b332e86b1f4d611a8c55cd29f917
- evidence_id: e121
  kind: validation
  reference: just validate
  locator: Executed 2026-10-09T06:58:58.921772+00:00 through 2026-10-09T07:00:16.926693+00:00;
    exit 0
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: 'Passed skill validation and full QC: 157 pathway records, closed schema,
    identifiers/labels, 8,263 evidence blocks, 30 sources, documentation, deep-research
    contract, history, and generated pages current.'
- evidence_id: e122
  kind: validation
  reference: just test
  locator: Executed 2026-10-09T07:00:16.927798+00:00 through 2026-10-09T07:04:57.904577+00:00;
    exit 0
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Full repository pytest passed. This is deterministic regression coverage,
    not a literature reassessment. 981 passed, 3 skipped, 3 warnings in 277.97s (0:04:37)
- evidence_id: e123
  kind: validation
  reference: just lint
  locator: Executed 2026-10-09T07:04:57.906245+00:00 through 2026-10-09T07:04:59.216107+00:00;
    exit 0
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Full repository Ruff check passed.
- evidence_id: e124
  kind: validation
  reference: git diff --check
  locator: Executed 2026-10-09T07:04:59.216759+00:00 through 2026-10-09T07:04:59.295808+00:00;
    exit 0
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Whitespace/error check passed for the tracked patch at assessment time.
    Untracked new files were outside that command scope.
- evidence_id: e125
  kind: validation
  reference: .venv/bin/python /Users/marcin/.codex/skills/.system/skill-creator/scripts/quick_validate.py
    .claude/skills/pathwaymech-resolve-reviews
  locator: Executed 2026-10-09T07:04:59.296577+00:00 through 2026-10-09T07:04:59.400336+00:00;
    exit 0
  accessed_at: '2026-10-09T07:06:50Z'
  support: supports
  summary: Skill-creator frontmatter and scaffold validation passed for the new resolver.
assessments:
- assessment_id: reconcile-legacy-01
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: No concrete unimplemented correction identified within the historical report
    scope; corrections are represented by current files matching the final integrated
    review ledger. This is a reconciliation assessment, not a new scientific PASS
    or fabricated terminal finding lineage.
  details: 'Historical cohort: 86 targets; each current target hash equals the final
    integrated ledger.

    Prior correction groups: Native assertion locators and relation semantics corrected
    for all 86 records; source physical individuals preserved rather than collapsed
    to generic chemical classes. Ten unsupported threonine outline activities excluded;
    independently sourced GLY1 aldolase route added. Six lipid IV(A) native enablers
    and independently supported complex composition restored. CPX-1739 location conflict
    handed to, and subsequently reconciled by, yeast compartment audit.

    Followup interpretation: Integration, rendering, export and gate handoffs were
    completed historically as recorded in main-integration-validation.json. Current
    full validate/test/lint now passed; actual commands and scope are recorded in
    checks. Provider-refresh reproduction remains a conditional future task, not an
    instruction to replay one-time migrations on already curated records.

    Preserved scientific limits: Native unknown physical identities remain source-local.
    Unsupported yeast threonine branches remain excluded. Generic or missing exact
    enablers and complete physiological/cofactor coverage are not asserted.

    Scope limits: Historical reports and ledgers remain byte-identical; no structured
    previous_occurrences are fabricated for legacy prose. Current byte identity verifies
    continued representation of prior reviewed decisions; it does not independently
    validate all biological assertions or establish literature completeness. Counts
    are an intermediate native stage, superseded by later compartment, chemistry and
    cofactor stages; they should not be forced onto the final current graph.'
  target_ids:
  - legacy-01
  evidence_ids:
  - e001
  - e002
  - e003
  - e004
  - e005
- assessment_id: reconcile-legacy-02
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: No concrete unimplemented correction identified within the historical report
    scope; corrections are represented by current files matching the final integrated
    review ledger. This is a reconciliation assessment, not a new scientific PASS
    or fabricated terminal finding lineage.
  details: 'Historical cohort: 50 targets; each current target hash equals the final
    integrated ledger.

    Prior correction groups: Core native leaf reaction coverage and glyoxylate/carbamoyl-phosphate
    routes completed. Composite-step chemistry exposed and erroneous attribution corrected.
    Unsupported protein/cofactor specificity excluded or qualified; repaired-mutant
    IlvG, tentative P00561/P00562 sodium and overly specific P05791 cluster chemistry
    not reinstated. Structured assertions separated from genuine literature quotations.

    Followup interpretation: Integration, rendering, export and gate handoffs were
    completed historically as recorded in main-integration-validation.json. Current
    full validate/test/lint now passed; actual commands and scope are recorded in
    checks. Provider-refresh reproduction remains a conditional future task, not an
    instruction to replay one-time migrations on already curated records.

    Preserved scientific limits: Broad taxon records may retain activity classes without
    exact named proteins. Cofactor absence is not cofactor independence; general iron-sulfur
    scope is deliberate. Source-supported specificity/protonation differences and
    alternative-route boundaries remain explicit.

    Scope limits: Historical reports and ledgers remain byte-identical; no structured
    previous_occurrences are fabricated for legacy prose. Current byte identity verifies
    continued representation of prior reviewed decisions; it does not independently
    validate all biological assertions or establish literature completeness.'
  target_ids:
  - legacy-02
  evidence_ids:
  - e006
  - e007
  - e008
  - e009
- assessment_id: reconcile-legacy-03
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: No concrete unimplemented correction identified within the historical report
    scope; corrections are represented by current files matching the final integrated
    review ledger. This is a reconciliation assessment, not a new scientific PASS
    or fabricated terminal finding lineage.
  details: 'Historical cohort: 16 targets; each current target hash equals the final
    integrated ledger.

    Prior correction groups: Misgrounded ATP/CoA/Q6/mycothiol/DAP/inositol identities,
    directionality, complexes and enzyme/cofactor roles corrected. Native diagram/BioPAX
    assertions replace manufactured quotations; reusable importers preserve object
    and direction provenance. TreS physiological direction, MshB/Mca roles and conditional
    metal dependence corrected; unsupported ImpC and THI3 catalytic assignments removed.
    LnyI dependence and observed linearmycin products represented while proposed assembly
    mechanism stays unasserted.

    Followup interpretation: Integration, rendering, export and gate handoffs were
    completed historically as recorded in main-integration-validation.json. Current
    full validate/test/lint now passed; actual commands and scope are recorded in
    checks. Provider-refresh reproduction remains a conditional future task, not an
    instruction to replay one-time migrations on already curated records.

    Preserved scientific limits: Mycothiol phosphate-removal catalyst remains unresolved.
    Three peptidoglycan nodes retain authentic GPML identities without external chemical
    grounding. Unassigned glutaredoxin partner and ambiguous branches remain omitted.
    Proposed linearmycin assembly is not established causal chemistry. Cross-provider
    duplication was outside this bounded review.

    Scope limits: Historical reports and ledgers remain byte-identical; no structured
    previous_occurrences are fabricated for legacy prose. Current byte identity verifies
    continued representation of prior reviewed decisions; it does not independently
    validate all biological assertions or establish literature completeness.'
  target_ids:
  - legacy-03
  evidence_ids:
  - e010
  - e011
  - e012
  - e013
  - e014
  - e015
- assessment_id: reconcile-legacy-04
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: No concrete unimplemented correction identified within the historical report
    scope; corrections are represented by current files matching the final integrated
    review ledger. This is a reconciliation assessment, not a new scientific PASS
    or fabricated terminal finding lineage.
  details: 'Historical cohort: 85 targets; each current target hash equals the final
    integrated ledger.

    Prior correction groups: Systematic definite-cytosol overstatement corrected conservatively,
    preserving physical located_in versus activity occurs_in distinction. Exact protein
    identity joins and source-conditional compartments added; five cytoplasmic actin-patch
    cases restored after initial overclassification. CPX-1739 activity reconciled
    to Golgi; CPX-1268 native mitochondrial activity corroborated, not falsely treated
    as a conflict. ADH4, ADK2, ARG2/ARG7 and DCI1 catalytic handoffs subsequently
    addressed by function and chemistry audits.

    Followup interpretation: Integration, rendering, export and gate handoffs were
    completed historically as recorded in main-integration-validation.json. Current
    full validate/test/lint now passed; actual commands and scope are recorded in
    checks. Provider-refresh reproduction remains a conditional future task, not an
    instruction to replay one-time migrations on already curated records.

    Preserved scientific limits: 108 independent activity-location gaps require activity-specific
    evidence, not inferred generic cytosol. Protein location does not prove absence
    of cytosolic activity or establish every catalytic compartment. Conditional molecular
    forms/topology are retained without simultaneous-location claims.

    Scope limits: Historical reports and ledgers remain byte-identical; no structured
    previous_occurrences are fabricated for legacy prose. Current byte identity verifies
    continued representation of prior reviewed decisions; it does not independently
    validate all biological assertions or establish literature completeness.'
  target_ids:
  - legacy-04
  evidence_ids:
  - e016
  - e017
  - e018
  - e019
  - e020
  - e021
- assessment_id: reconcile-legacy-05
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: No concrete unimplemented correction identified within the historical report
    scope; corrections are represented by current files matching the final integrated
    review ledger. This is a reconciliation assessment, not a new scientific PASS
    or fabricated terminal finding lineage.
  details: 'Historical cohort: 2 targets; each current target hash equals the final
    integrated ledger.

    Prior correction groups: Methenyl/methylene folate identities separated; MET13
    NADPH/NADP specificity corrected while MET12 NADH route retained. Eighteen unsupported
    directed material-flow assertions quarantined; three actual folate bridges retained.
    Vip1/Kcs1 positional chemistry and missing Kcs1 enabler corrected; generic PP-InsP4/DDP1
    identities preserved. Experimentally supported isolated Vip1 pyrophosphatase-domain
    activity added with qualified scope; redundant proton canceled.

    Followup interpretation: Integration, rendering, export and gate handoffs were
    completed historically as recorded in main-integration-validation.json. Current
    full validate/test/lint now passed; actual commands and scope are recorded in
    checks. Provider-refresh reproduction remains a conditional future task, not an
    instruction to replay one-time migrations on already curated records.

    Preserved scientific limits: Generic PP-InsP4 and DDP1 regioselectivity remain
    deliberate limits. Vip1 result concerns recombinant yeast domain in vitro; no
    whole-cell flux or untested IP8 hydrolysis inferred. Broad native folate/polyglutamate
    classes are not narrowed without evidence.

    Scope limits: Historical reports and ledgers remain byte-identical; no structured
    previous_occurrences are fabricated for legacy prose. Current byte identity verifies
    continued representation of prior reviewed decisions; it does not independently
    validate all biological assertions or establish literature completeness.'
  target_ids:
  - legacy-05
  evidence_ids:
  - e022
  - e023
  - e024
  - e025
  - e026
- assessment_id: reconcile-legacy-06
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: No concrete unimplemented correction identified within the historical report
    scope; corrections are represented by current files matching the final integrated
    review ledger. This is a reconciliation assessment, not a new scientific PASS
    or fabricated terminal finding lineage.
  details: 'Historical cohort: 85 targets; each current target hash equals the final
    integrated ledger.

    Prior correction groups: All 475 original activity occurrences assigned explicit
    dispositions: 440 retained, 29 changed, six excluded; one Vip1 activity added.
    PSA1 donor pair, FOX2 stereochemistry, DCI1/ECI1, ARO8 sides, MAE1, ARG2/ARG7,
    COQ1 labels and yeast dATP scope corrected. Catalytic/function supplements corrected
    cardiolipin, ADK2, BNA3/LYS4, folate and inositol chemistry and qualified specificity
    conflicts.

    Followup interpretation: Integration, rendering, export and gate handoffs were
    completed historically as recorded in main-integration-validation.json. Current
    full validate/test/lint now passed; actual commands and scope are recorded in
    checks. Provider-refresh reproduction remains a conditional future task, not an
    instruction to replay one-time migrations on already curated records.

    Preserved scientific limits: Five retained activities lack exact enablers; spontaneous
    steps do not imply unknown enzymes. Seven substrate-specificity contexts lack
    independently complete catalogs; five tyrosol ADH branches have related-substrate
    rather than direct tyrosine-assay support. Two redox contexts retain pathway-system
    NADPH inputs without claiming balanced direct enzyme chemistry. Protein-bound/polymer
    reactants remain source abstractions.

    Scope limits: Historical reports and ledgers remain byte-identical; no structured
    previous_occurrences are fabricated for legacy prose. Current byte identity verifies
    continued representation of prior reviewed decisions; it does not independently
    validate all biological assertions or establish literature completeness.'
  target_ids:
  - legacy-06
  evidence_ids:
  - e027
  - e028
  - e029
  - e030
  - e031
- assessment_id: reconcile-legacy-07
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: No concrete unimplemented correction identified within the historical report
    scope; corrections are represented by current files matching the final integrated
    review ledger. This is a reconciliation assessment, not a new scientific PASS
    or fabricated terminal finding lineage.
  details: 'Historical cohort: 152 targets; each current target hash equals the final
    integrated ledger.

    Prior correction groups: Complete integration of GO-CAM, MetaCyc, WikiPathways,
    Reactome and MIBiG corrections across the historical 152-record cohort. BNA3/BNA7,
    ACO1/ACO2/LYS4, CRD1, THI4/THI13, ADK2, FOX2, folate/MET13, inositol, material
    flow and compartments corrected. Parent renders, exports, closed schema, identifier
    and test gates performed during integration. Later PR262 adversarial corrections
    supersede the first integrated narrative: ARG82 crystal calcium excluded and THI13
    exact products/balance quarantined; 7134 edges is the final reviewed ledger count.

    Followup interpretation: Integration, rendering, export and gate handoffs were
    completed historically as recorded in main-integration-validation.json. Current
    full validate/test/lint now passed; actual commands and scope are recorded in
    checks. Provider-refresh reproduction remains a conditional future task, not an
    instruction to replay one-time migrations on already curated records.

    Preserved scientific limits: ADP-thiazole hydrolysis and mycothiol phosphate-removal
    enzyme assignments unresolved. THI13 exact products and net balance remain unresolved;
    homolog evidence is not a direct THI13 experiment. CMP/STR2 specificity, native
    tyrosol context and Vip1 domain limitations remain qualified. Broad taxon enzyme
    classes and missing cofactor annotations do not establish molecular completeness.

    Scope limits: Historical reports and ledgers remain byte-identical; no structured
    previous_occurrences are fabricated for legacy prose. Current byte identity verifies
    continued representation of prior reviewed decisions; it does not independently
    validate all biological assertions or establish literature completeness. This
    legacy narrative predates the final adversarial counts. Historical counts are
    not current invariant requirements. Five current pathways were added after this
    152-record cohort and are outside its prior scientific coverage.'
  target_ids:
  - legacy-07
  evidence_ids:
  - e032
  - e033
  - e034
  - e035
  - e036
  - e037
- assessment_id: reconcile-legacy-08
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: The old unsupported RO:0002411 omission and BFO omission are historical
    scope decisions. PR262 now preserves native causality/context with exact source_assertion
    locators.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/tetrahydrofolate-biosynthesis.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: No fresh experimental assessment of this native model was performed.'
  target_ids:
  - legacy-08
  evidence_ids:
  - e038
  - e039
  - e040
  - e041
- assessment_id: reconcile-legacy-09
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: URA6, YNK1 and two CTP-synthase activities remain; later current context
    and cofactors supersede historical 30-edge count.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: Database assertion support is not proof that every referenced
    primary paper was read.'
  target_ids:
  - legacy-09
  evidence_ids:
  - e042
  - e043
  - e044
  - e045
- assessment_id: reconcile-legacy-10
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: Later catalytic-function curation supersedes the historical ADK2 AMP/ATP
    assignment; current record has a second curation-history event.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: Preserve the newer species-specific ADK2 adjudication; historical
    source exactness is not biological correctness.'
  target_ids:
  - legacy-10
  evidence_ids:
  - e046
  - e047
  - e048
  - e049
- assessment_id: reconcile-legacy-11
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: 'The historical instruction to preserve raw-only RXN0-745 has been superseded
    by PR262: the current description and final history event exclude class III formate-dependent
    ATP reduction from yeast. Three diphosphate-reduction/kinase activities remain.'
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: Do not restore the rejected branch merely because the legacy
    review passed its raw source projection.'
  target_ids:
  - legacy-11
  evidence_ids:
  - e050
  - e051
  - e052
  - e053
  - e054
- assessment_id: reconcile-legacy-12
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: Later PR262 curation removed a spurious nondecarboxylating MAE1 duplicate,
    documented in curation_history; 15 activities remain instead of the historical
    16.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/gluconeogenesis-i.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: Raw source equality alone cannot override the newer independently
    supported MAE1 disposition.'
  target_ids:
  - legacy-12
  evidence_ids:
  - e055
  - e056
  - e057
  - e058
- assessment_id: reconcile-legacy-13
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: The current graph preserves 14 activities and adds source context, complex
    composition and cofactors under the newer relation rubric.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: The old rule treating BFO/location context as illegal is obsolete;
    current source-supported context must be preserved.'
  target_ids:
  - legacy-13
  evidence_ids:
  - e059
  - e060
  - e061
  - e062
- assessment_id: reconcile-legacy-14
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: The current HMG reaction has two HMG1/HMG2 enablers and one copy of each
    shared chemical-side triple; no duplicate edge triples are present.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/mevalonate-pathway.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: If importer regeneration is undertaken, preserve separate enablers
    without duplicating shared substrate/product triples.'
  target_ids:
  - legacy-14
  evidence_ids:
  - e063
  - e064
  - e065
  - e066
- assessment_id: reconcile-legacy-15
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: Nine activities remain with later protein assignment/context/cofactor enrichment;
    current record is exactly the final PR262 reviewed digest.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/l-lysine-biosynthesis-iv.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: Later catalytic assignment corrections take precedence over
    the legacy raw-only pass.'
  target_ids:
  - legacy-15
  evidence_ids:
  - e067
  - e068
  - e069
  - e070
- assessment_id: reconcile-legacy-16
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: Nine activities remain; later catalytic-function curation, including cardiolipin
    chemistry, supersedes legacy source-equality assertions.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/phospholipid-biosynthesis.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: The current function review/source locators remain necessary
    evidence; no new literature review was performed.'
  target_ids:
  - legacy-16
  evidence_ids:
  - e071
  - e072
  - e073
  - e074
- assessment_id: reconcile-legacy-17
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: Six activities remain with later source context and cofactors; current
    record is exactly the final PR262 reviewed digest.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: No immediate legacy corrective task; future edits require current
    gates and evidence.'
  target_ids:
  - legacy-17
  evidence_ids:
  - e075
  - e076
  - e077
  - e078
- assessment_id: reconcile-legacy-18
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: The current graph retains distinct GLO2 and GLO4 enables edges to GLYOXII-RXN
    and the parallel source-local hydrolase activity.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/methylglyoxal-catabolism.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: Preserve the parallel enzyme activities during future importer
    regeneration.'
  target_ids:
  - legacy-18
  evidence_ids:
  - e079
  - e080
  - e081
  - e082
- assessment_id: reconcile-legacy-19
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: Four activities remain; later history explicitly corrects PSA1 guanylyl
    donor and leaving group while retaining GDP-mannose.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: Do not restore obsolete raw-source chemical sides to satisfy
    historical input/output counts.'
  target_ids:
  - legacy-19
  evidence_ids:
  - e083
  - e084
  - e085
  - e086
- assessment_id: reconcile-legacy-20
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: Later function/adversarial curation retains the THI13 protein-bound core
    as a similarity inference and quarantines exact iron-redox, balancing and residue-product
    claims.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/thiamine-biosynthesis.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: THI13 omitted products/balancing species and the ADP-thiazole
    hydrolysis bridge remain bounded scientific uncertainties, not a license to invent
    edges.'
  target_ids:
  - legacy-20
  evidence_ids:
  - e087
  - e088
  - e089
  - e090
  - e091
- assessment_id: reconcile-legacy-21
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: The three EKI1/ECT1/EPT1 activities remain with later source context and
    cofactor enrichment.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: Historical lack of causal associations does not justify inventing
    ordering edges.'
  target_ids:
  - legacy-21
  evidence_ids:
  - e092
  - e093
  - e094
  - e095
- assessment_id: reconcile-legacy-22
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: Eleven activities remain; the historical 24 causal source associations
    are now 24 provides_input_for assertions under corrected relation semantics.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/valine-degradation.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: The source isozyme fan-out is retained as source context, not
    new experimental validation.'
  target_ids:
  - legacy-22
  evidence_ids:
  - e096
  - e097
  - e098
  - e099
- assessment_id: reconcile-legacy-23
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: The three CPT1/PCT1/CKI1 activities remain with later source context/cofactors.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/phosphatidylcholine-biosynthesis-i.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: This is still the exact GO-CAM pathway and is not merged with
    the related Kennedy model.'
  target_ids:
  - legacy-23
  evidence_ids:
  - e100
  - e101
  - e102
  - e103
- assessment_id: reconcile-legacy-24
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: Three activities remain; old before-merge checks refer to the historical
    import. Current chemical sides/context are the final PR262 reviewed state.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: Reused upstream steps do not establish duplicate pathway identity.'
  target_ids:
  - legacy-24
  evidence_ids:
  - e104
  - e105
  - e106
  - e107
- assessment_id: reconcile-legacy-25
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: Five activities remain. The previously omitted ELO3 output is now edge-037,
    an explicit native source_assertion at ./YeastPathways_PWY-5080-1.json#/facts/36,
    reconciled in the later native and chemical review ledgers.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: The native statement is database evidence, not direct experimental
    support; do not revert it solely because the old projection required an annotation
    array.'
  target_ids:
  - legacy-25
  evidence_ids:
  - e108
  - e109
  - e110
  - e111
  - e112
  - e113
- assessment_id: reconcile-legacy-26
  area: provenance
  topic: Historical findings and conditional followups against current state
  outcome: supported
  summary: The current description remains explicitly GPH1/PGM scoped. Phosphate and
    shortened-glucan product were restored in PR262; GDB1 and SGA1 are not asserted
    as complete reactions.
  details: 'Historical disposition: no findings and no recommended edits. Current
    target: data/pathways/glycogen-catabolism.yaml.

    Current structural validation and duplicate-triple checks passed. Current target
    bytes match the final integrated PR #262 ledger; this is not a fresh scientific
    attestation.

    Preserved limits: Ambiguous peripheral GDB1/SGA1 branches remain outside this
    record pending reaction-specific evidence; broader identifier support alone is
    insufficient.'
  target_ids:
  - legacy-26
  evidence_ids:
  - e114
  - e115
  - e116
  - e117
  - e118
findings: []
actions: []
limitations:
- This is reconciliation of 26 historical reports, not a new scientific review. No
  primary literature or upstream database retrieval was repeated, and no native scientific
  status was promoted.
- The 19 September individual reports predate the October causal-graph corrections.
  Their old pass verdicts, source projections, graph counts and schema exclusions
  are historical; current scope decisions are assessed against later evidence.
- All 152 records in the final integrated category ledger match its hashes. This proves
  continued representation of those reviewed decisions, not the truth or completeness
  of every biological claim. Field-level followups were inspected as described in
  the assessments.
- The current corpus contains 157 records. The five later pathways listed in scope
  exclusions have no historical scientific coverage from this cohort; current corpus-wide
  validation is not a substitute for scientific review.
- Legacy Markdown has no structured finding IDs. No previous_occurrences or terminal
  resolved findings have been fabricated, and no old report was rewritten. Empty findings
  means no current actionable defect was identified in this reconciliation scope.
- 'Historical scientific gaps remain: unknown mycothiol phosphate-removal catalyst
  and ADP-thiazole hydrolysis assignment; THI13 exact products/balance; activity-specific
  compartment gaps; generic chemical identities and incomplete cofactor, isoform or
  condition coverage. These limits are not scientifically resolved.'
- 'Local source-ingestion artifacts, raw drafts and GitHub issues #273-277 are outside
  the selected completed-record-review population. Supporting causal audit ledgers
  inform this reconciliation but are not represented as new independent scientific
  reviews.'
- 'Input source.state is working_tree: the retained hashes attest inspected bytes
  on the stated durable main base. Nineteen legacy reports were copied byte-for-byte
  from the original checkout and preserved for replayability; the bundle does not
  claim they were already tracked at that base.'
notes:
- No biological YAML, generated pages, original legacy report bytes, or native curation
  statuses changed during this reconciliation.
- All 19 individual reports were previously untracked local artifacts. The new skill,
  routing, immutable review bundle and preserved historical inputs are the deliverables
  of this session.
links:
- https://github.com/CultureBotAI/PathwayMech/pull/262
```

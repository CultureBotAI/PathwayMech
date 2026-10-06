# YAML Category Review: Folate and inositol phosphate chemistry

- Repository: CultureBotAI/PathwayMech
- Category: Two yeast GO-CAM records with source-identity conflicts
- Selection Rule: Exact folate-interconversions.yaml and inositol-phosphate-biosynthesis.yaml; all activities, chemical roles and connecting material-flow assertions.
- Started UTC: 2026-10-05 (exact first inspection time not retained; catalytic source retrieved at 06:42:27Z)
- Finished UTC: 2026-10-05T07:07:00Z
- Verdict: Complete review and authorized corrections; six major scientific error classes and one minor net-equation defect corrected. Generic chemical specificity remains explicit where experiments do not resolve an isomer.

## Target Category

The bounded chemical follow-up covers all 28 original activities. A primary experiment supports one additional Vip1 domain activity, bringing this cohort to 29. This report supplements the complete 475-activity chemical audit, the 85-record compartment audit and the full native graph audit; it does not claim all cellular pathway chemistry is experimentally resolved.

## Selection and Membership

Both existing pathway boundaries are retained. All activities are listed below; the machine-readable ledger contains every inspected protein FUNCTION/CATALYTIC ACTIVITY annotation, current chemical side, changed edge and complete excluded native assertion.

| Record | Reviewed activity | Independent enzyme source |
|---|---|---|
| folate-interconversions | `gomodel:1.5.1.15-RXN` | Q02046 |
| folate-interconversions | `gomodel:1.5.1.20-RXN` | P46151 |
| folate-interconversions | `gomodel:DIHYDROFOLATEREDUCT-RXN` | P07807 |
| folate-interconversions | `gomodel:FORMATETHFLIG-RXN` | P07245 |
| folate-interconversions | `gomodel:GCVMULTI-RXN` | ComplexPortal:CPX-1268 |
| folate-interconversions | `gomodel:GLYOHMETRANS-RXN` | P37292 |
| folate-interconversions | `gomodel:METHENYLTHFCYCLOHYDRO-RXN` | P07245 |
| folate-interconversions | `gomodel:METHYLENETHFDEHYDROG-NADP-RXN` | P07245 |
| folate-interconversions | `gomodel:THYMIDYLATESYN-RXN` | P06785 |
| folate-interconversions | `gomodel:YeastPathways_PWY3O-697/6a4c244800005448` | P09440 |
| folate-interconversions | `gomodel:YeastPathways_PWY3O-697/6a4c244800005468` | P09440 |
| folate-interconversions | `gomodel:YeastPathways_PWY3O-697/6a4c244800005484` | P09440 |
| folate-interconversions | `gomodel:YeastPathways_PWY3O-697/6a4c244800005502` | P37291 |
| folate-interconversions | `gomodel:YeastPathways_PWY3O-697/6a4c244800005519` | P53128 |
| inositol-phosphate-biosynthesis | `gomodel:2.7.1.127-RXN` | P07250 |
| inositol-phosphate-biosynthesis | `gomodel:2.7.1.151-RXN` | P07250 |
| inositol-phosphate-biosynthesis | `gomodel:2.7.1.152-RXN` | Q12494 |
| inositol-phosphate-biosynthesis | `gomodel:3.1.4.11-RXN` | P32383 |
| inositol-phosphate-biosynthesis | `gomodel:RXN-4941` | P07250 |
| inositol-phosphate-biosynthesis | `gomodel:RXN-7162` | P07250 |
| inositol-phosphate-biosynthesis | `gomodel:RXN-7163` | Q06667 |
| inositol-phosphate-biosynthesis | `gomodel:RXN-7184` | P07250 |
| inositol-phosphate-biosynthesis | `gomodel:RXN3O-143` | Q06685 |
| inositol-phosphate-biosynthesis | `gomodel:RXN3O-258` | Q06685 |
| inositol-phosphate-biosynthesis | `gomodel:RXN3O-785` | Q99321 |
| inositol-phosphate-biosynthesis | `gomodel:RXN3O-786` | Q99321 |
| inositol-phosphate-biosynthesis | `gomodel:RXN3O-9819` | Q12494 |
| inositol-phosphate-biosynthesis | `gomodel:YeastPathways_PWY3O-402/6a4c244800000690` | Q12494 |
| inositol-phosphate-biosynthesis | `RHEA:79724` | Q06685 |

## Validation

Both corrected records passed semantic validation before handoff. Six independent chemistry regression tests cover folate-state separation, MET13 versus MET12 specificity, actual folate material flow, inositol regioisomers, generic pyrophosphate count and qualified domain hydrolysis. Combined importer, support importer, compartment and chemistry suites: 42 passed. Scoped Ruff and git diff --check passed. Full repository schema/identifier/cofactor/history/render gates are owned by the integrating agent and were not redundantly run during this handoff.

## Lump and Split Review

No pathway merge or split warranted. Multiple folate activities of ADE3/MIS1 remain distinct; they are not collapsed into one reaction. Different inositol kinase routes and intermediate IPMK steps remain distinct. The new Vip1 hydrolysis activity is separate from its kinase activity and is qualified as an isolated-domain in-vitro result.

## Identity and Grounding

Five methenyl endpoints formerly typed as methylene CHEBI:20502 now use independently grounded CHEBI:57455. Methylene inputs retain their distinct identity. Vip1/Kcs1 regioisomers use CHEBI:74946 (1-IP7) and CHEBI:77983 (1,5-IP8), supported by current UniProt/Rhea and primary product crystallography.

Generic PP-InsP4 products retain authentic native entity gomodel:CHEBI_14178_RXN-4941, whose native display label is correct but CHEBI:14178 type had two diphosphates. Generic DDP1 PP-InsP5 uses authentic gomodel:CHEBI_62919_RXN3O-786; no unsupported positional isomer is imposed. Native locations are recorded exactly in the ledger. CHEBI:187038 was rejected: despite its appealing display label, its ChEBI255 SMILES/InChI encode six monophosphates. No new structure was guessed.

## Graph and Evidence Patterns

MET13 uses NADPH/NADP, directly supported by PMID:11729203, while MET12's independently annotated NADH branch remains. Eighteen native folate provides_input_for assertions cannot supply the required folate intermediate in their displayed chemical direction after state correction; these are quarantined with full original evidence. Three supported material-flow assertions remain. Reversible catalytic capacity alone is not evidence for an unmodeled reverse material flow, nor for unobserved transport between compartments.

Kcs1 now enables the supported 1-IP7-to-1,5-IP8 route; its missing proton inputs are represented for the charged species. The isolated S. cerevisiae Vip1 pyrophosphatase domain hydrolyzes 1-IP7 but not 3-IP7 in vitro (PMID:32303658, Fig3A and Table2). This supersedes UniProt's older no-phosphatase CAUTION only for the tested activity. RHEA:79724 supplies the independently grounded chemical equation. No S. pombe cellular phenotype, physiological yeast flux or untested yeast IP8 hydrolysis is asserted.

All new facts are source_assertion values with exact source locators. Structured facts are not presented as verbatim quotations. The pinned UniProt source SHA256 is 9600fe7f1e55a4f51554b244607a706b1604904dc71de8960b2f399bf75b0c7c; primary full XML SHA256 is 3e4daf11de27f7571fd524187c26585c63365169c80143be547437354180a0c9. Source comments remain attached to their canonical protein accession while representation-specific URL, checksum and JSON pointer appear in the locator.

## Completeness Patterns

Retained all original activities and supported chemical roles. Added the missing experimentally demonstrated Vip1 domain hydrolysis. Retained DDP1 despite absence of a specific Rhea cross-reference, because independent protein FUNCTION and primary citations support the generic pyrophosphate hydrolysis. Retained IPMK intermediate reactions rather than replacing them with its aggregate net equation. Broad native folate/polyglutamate classes were not silently narrowed to a specific chain length. Generic PP-InsP4 and DDP1 regioselectivity remain deliberate evidence limits.

## Findings

1. Major, fixed: distinct methenyl and methylene folates merged under one identifier.
2. Major, fixed: MET13 assigned the wrong pyridine-nucleotide pair.
3. Major, fixed: native directed folate-flow assertions incompatible with displayed corrected chemical sides.
4. Major, fixed: outdated Vip1/Kcs1 phosphate positions and an absent Kcs1 enabler.
5. Major, fixed: PP-InsP4 assigned a bisdiphosphate class; DDP1 narrowed to unsupported positional identities.
6. Major, fixed: the existing graph omitted experimentally demonstrated yeast Vip1 domain pyrophosphatase activity and an older source CAUTION contradicted the later experiment.
7. Minor, fixed: redundant proton on both sides of the native Kcs1 IP6-kinase equation; canceled for the net reaction.

## Recommended Edits

Applied to the two maintained YAMLs. The bounded migration scripts/curate_folate_inositol_chemistry.py checks exact source bytes and original endpoints before publishing either record. It is a one-time migration and fails against already curated inputs rather than overwriting subsequent work. History records were scaffolded for both records. Regenerate pages through the integrating agent's full-corpus render workflow.

## Follow-up Checks

Run full identifier, schema, history, cofactor and rendered-page gates after integration. Preserve scoped generic inositol entities until an independently authoritative structure/class resolves the source ambiguity. Do not replay the native importer over these reviewed records without reapplying source exclusions.

## Additional Notes

[Machine-readable review ledger](../causal_graph_review/folate-inositol-chemistry-review.json). Primary sources: [MET13 cofactor experiment](https://pubmed.ncbi.nlm.nih.gov/11729203/), [Arg82 kinase experiment](https://pubmed.ncbi.nlm.nih.gov/11311242/), [yeast IP6 kinase substrate study](https://pubmed.ncbi.nlm.nih.gov/10827188/), [Vip1 kinase/domain phosphatase experiment](https://pmc.ncbi.nlm.nih.gov/articles/PMC7196807/). Source inspection used explicit file enumeration, which includes ignored files; no absence finding relies on gitignore-filtered searches. User authorization permitted edits beyond the review skills' default read-only scope.

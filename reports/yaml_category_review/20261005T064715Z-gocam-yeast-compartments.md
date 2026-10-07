# YAML Category Review: Yeast GO-CAM compartments

- Repository: CultureBotAI/PathwayMech
- Category: All 85 S288C GO-CAM pathway records
- Selection Rule: Root `gomodel:` plus taxon `NCBITaxon:559292`, recursively selected from maintained pathway YAMLs; exact85 count enforced.
- Started UTC: 2026-10-05T06:31:56Z (pinned source retrieval)
- Finished UTC: 2026-10-05T06:47:15Z
- Verdict: Complete compartment audit; source conflicts corrected or quarantined, independent gaps explicit.

## Target Category

Reviewed all475 activities in the85-record yeast cohort, including activities with no original location assertion. The pinned reviewed S288C UniProt batch contains6,733 entries and exact SGD cross-references, location annotations, functions and cautions. Source SHA256: `95f72dcc644358c480e0e59f996cf88533558b5fa4256460a030e0a1eaf9678d`. The complete per-protein annotations, per-activity decisions and original excluded facts are in [the location ledger](../causal_graph_review/gocam-location-review.json).

## Selection and Membership

Every selected record appears in the table below. This was a complete audit, not a sample. The one E. coli GO-CAM record was outside this yeast compartment cohort.

| Record | Activities audited | Cytosol facts quarantined | Location edges added |
|---|---:|---:|---:|
| 4-aminobutyrate-degradation | 2 | 0 | 2 |
| 6-hydroxymethyl-dihydropterin-diphosphate-biosynthesis-i | 5 | 2 | 1 |
| adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii | 4 | 0 | 6 |
| adenosine-ribonucleotides-de-novo-biosynthesis | 4 | 1 | 4 |
| aerobic-glycerol-degradation | 2 | 0 | 2 |
| allantoin-degradation-to-glyoxylate-i | 3 | 0 | 0 |
| allantoin-degradation-to-ureidoglycolate-i | 2 | 0 | 0 |
| aspartate-biosynthesis | 4 | 1 | 5 |
| assimilatory-sulfate-reduction | 4 | 0 | 2 |
| beta-alanine-biosynthesis-iv | 3 | 0 | 2 |
| carnitine-shuttle | 4 | 2 | 4 |
| chitin-biosynthesis | 3 | 3 | 5 |
| citrulline-biosynthesis | 2 | 0 | 3 |
| dolichyl-glucosyl-phosphate-biosynthesis | 5 | 1 | 4 |
| dolichyl-phosphate-d-mannose-biosynthesis | 4 | 1 | 4 |
| epoxysqualene-biosynthesis | 3 | 3 | 3 |
| ergosterol-biosynthesis-i | 5 | 5 | 5 |
| ethanol-degradation | 8 | 2 | 12 |
| fatty-acid-elongation | 8 | 3 | 4 |
| fatty-acid-oxidation-pathway | 11 | 10 | 17 |
| folate-interconversions | 14 | 3 | 15 |
| formaldehyde-oxidation-ii-glutathione-dependent | 4 | 0 | 4 |
| galactose-degradation | 6 | 0 | 2 |
| gluconeogenesis-i | 16 | 0 | 16 |
| glutathione-degradation | 2 | 1 | 4 |
| glycerol-biosynthesis | 4 | 0 | 8 |
| glycine-cleavage | 3 | 3 | 3 |
| glycolysis-i-from-glucose-6-phosphate | 14 | 0 | 16 |
| guanosine-ribonucleotides-de-novo-biosynthesis | 6 | 0 | 6 |
| heme-biosynthesis-i-aerobic | 4 | 0 | 5 |
| hexaprenyl-diphosphate-biosynthesis | 5 | 0 | 2 |
| homocysteine-and-cysteine-interconversion | 4 | 0 | 5 |
| inositol-phosphate-biosynthesis | 14 | 6 | 7 |
| l-arginine-biosynthesis-ii-acetyl-cycle | 10 | 6 | 8 |
| l-asparagine-biosynthesis-i | 4 | 1 | 3 |
| l-asparagine-degradation | 7 | 5 | 12 |
| l-cysteine-biosynthesis-iii-from-l-homocysteine | 2 | 0 | 1 |
| l-homocysteine-biosynthesis | 2 | 0 | 2 |
| l-lysine-biosynthesis-iv | 9 | 5 | 6 |
| l-proline-degradation | 3 | 2 | 2 |
| l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde | 6 | 1 | 7 |
| l-tyrosine-degradation-iii | 10 | 2 | 13 |
| leucine-degradation | 9 | 3 | 11 |
| mannose-degradation | 4 | 0 | 1 |
| methionine-salvage-pathway | 9 | 1 | 13 |
| methylglyoxal-catabolism | 3 | 1 | 2 |
| mevalonate-pathway | 7 | 1 | 8 |
| myo-inositol-biosynthesis | 3 | 0 | 3 |
| nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde | 5 | 1 | 5 |
| nad-salvage-pathway-iv-from-nicotinamide-riboside | 3 | 1 | 3 |
| oleate-biosynthesis | 2 | 2 | 2 |
| palmitoleate-biosynthesis | 2 | 2 | 2 |
| periplasmic-nad-degradation | 2 | 2 | 3 |
| phenylalanine-biosynthesis | 4 | 0 | 4 |
| phosphatidate-biosynthesis-i-the-dihydroxyacetone-pathway | 4 | 4 | 8 |
| phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway | 5 | 3 | 9 |
| phosphatidylcholine-biosynthesis-i | 3 | 2 | 4 |
| phosphatidylethanolamine-biosynthesis-i | 3 | 3 | 10 |
| phosphatidylinositol-phosphate-biosynthesis | 21 | 10 | 18 |
| phospholipid-biosynthesis-ii-kennedy-pathway | 3 | 1 | 4 |
| phospholipid-biosynthesis | 9 | 9 | 16 |
| pyruvate-decarboxylation-to-acetyl-coa | 4 | 4 | 4 |
| pyruvate-fermentation-to-acetoin-iii | 9 | 0 | 5 |
| s-adenosyl-l-methionine-cycle-ii | 5 | 0 | 0 |
| salvage-pathways-of-pyrimidine-ribonucleotides | 9 | 0 | 10 |
| siroheme-biosynthesis | 3 | 0 | 0 |
| spermidine-biosynthesis-i | 2 | 0 | 0 |
| spermine-biosynthesis | 2 | 0 | 0 |
| sphingolipid-biosynthesis-yeast | 20 | 17 | 26 |
| sulfate-activation-for-sulfonation | 2 | 0 | 1 |
| superoxide-radicals-degradation | 4 | 2 | 5 |
| tetrahydrofolate-biosynthesis | 3 | 1 | 2 |
| tetrapyrrole-biosynthesis | 4 | 1 | 1 |
| thiamine-biosynthesis | 10 | 0 | 2 |
| threonine-degradation | 3 | 1 | 2 |
| trans-trans-farnesyl-diphosphate-biosynthesis | 3 | 0 | 1 |
| tryptophan-degradation | 12 | 2 | 16 |
| tyrosine-biosynthesis | 4 | 0 | 3 |
| udp-n-acetylglucosamine-biosynthesis | 4 | 0 | 3 |
| urea-degradation-i | 2 | 0 | 0 |
| utp-and-ctp-de-novo-biosynthesis | 4 | 0 | 5 |
| valine-degradation | 11 | 3 | 15 |
| very-long-chain-fatty-acid-biosynthesis | 5 | 5 | 8 |
| xylose-metabolism | 2 | 0 | 2 |
| zymosterol-biosynthesis | 12 | 12 | 6 |

## Validation

All85 candidate outputs passed semantic validation before write. Five independently authored acceptance tests passed, covering physical-versus-activity location, cytoplasmic isoenzymes, conditional evidence, ambiguous identities, per-representation provenance, and cytoplasmic actin patches. Location script and tests passed lint. Root owns final full corpus gates after other agents' catalytic and cofactor updates.

## Lump and Split Review

No pathways were merged or split. Native source activity identities and catalyst-specific branches were preserved. Location evidence never equates separate enzymes or moves every isoenzyme into the same compartment.

## Identity and Grounding

Location facts join exact reviewed UniProt accessions and exact SGD cross-references. An ambiguous SGD cross-reference in the complete source batch is excluded from identity joins; no label matching is used. UniProt SL vocabulary was manually mapped to current GO cellular components after checking canonical labels and relevant definitions in the independent GO database. Cytoplasm is preserved as cytoplasm; it is not narrowed to cytosol. Microsomes are experimental fractions and the GO class is obsolete, so these annotations are retained only in the ledger. Source representation URL, SHA and exact JSON paths are carried in each evidence locator, including when an existing canonical UniProt reference describes another pinned representation.

## Graph and Evidence Patterns

The pass added475 location edges and quarantined163 generic cytosol activity assertions whose complete resolved catalyst set had only nuclear, organellar, membrane or extracellular source locations. This is withholding an unsupported definite activity assignment, not claiming that protein localization proves absence of all cytosolic activity; membrane-associated enzymes can have cytosolic catalytic faces. Such cases require activity-specific evidence before a replacement location is asserted. The initial implementation overclassified five cytoplasmic actin-patch cases; those native assertions were restored and a regression test added.

Physical `located_in` facts retain source ECO grades, conditions, topology, orientation and processed molecular-form notes. Only twelve manually inspected UniProt FUNCTION entries and two explicit Complex Portal function entries generate additional activity `occurs_in` edges. This avoids promoting each observed protein location or generic sterol-module boilerplate into a pathway activity location.

The CPX-1739 mannosylinositol phosphorylceramide synthesis activity is now in the Golgi, matching the explicit Complex Portal functional statement. The cited PMID12954640 abstract supports complex formation and activity, but does not itself establish the Golgi location; location provenance is correctly the inspected Complex Portal record. Contrary to an earlier narrative report, CPX-1268 GCVMULTI activity already had a native mitochondrial location, so it was corroborated rather than falsely reported as a corrected cytosolic activity. PMID10871621 independently supports mitochondrial glycine-derived one-carbon production.

## Completeness Patterns

204 activity decisions retain compatible native locations,108 retain native assertions with an explicit independent-evidence gap, and163 quarantine conflicting/insufficient cytosol assignments. Protein-level organelle coverage now includes mitochondria and their membranes/matrix/intermembrane space, ER, Golgi, peroxisomes, vacuoles, nuclei, lipid droplets, plasma membrane, vesicles and extracellular/periplasmic regions where present in the source. These are source-conditional protein facts; they do not imply all sites are simultaneous or all are catalytic compartments.

## Findings

The systemic definite-cytosol overstatement has been corrected conservatively. Remaining independent location gaps are exhaustively enumerated in the ledger, including native generic protein individuals and entries lacking location comments. No experiment or absent annotation is invented to fill these gaps. Additional catalyst/substrate specificity conflicts noticed during this audit—ADH4, ADK2, ARG2/ARG7 and DCI1—were handed to the catalytic-review owner for separate scientific correction.

## Recommended Edits

Completed within compartment scope. Preserve the source-exclusion ledger on future regeneration, and rerun the bounded audit after a verified provider refresh. Do not automatically convert physical protein locations into activity locations.

## Follow-up Checks

Root should refresh independent GO authority snapshots for the new cellular-component IDs and run final identifier, schema, test, lint and history gates after the catalytic-review and cofactor stages. Follow up the108 independent location gaps through activity-specific experimental evidence rather than replacing uncertainty with generic cytosol.

## Additional Notes

The user explicitly authorized curation beyond the normally read-only skill. No paid source, GitHub mutation or iModulonDB expression inference was used. This audit establishes positive annotations and bounded conflicts in the pinned6,733-entry source, not general claims of biological absence. The complete source and record selection use direct filesystem reads and recursive Path enumeration, which include gitignored files.

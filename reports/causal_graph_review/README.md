# PathwayMech causal graph review

Reviewed and updated all **152 maintained pathway records**, with complete source-cohort
coverage: 86 GO-CAM, 50 MetaCyc, 12 WikiPathways, 3 Reactome and 1 MIBiG.
Review completed 2026-10-05T07:19:59.219761+00:00. Base commit: `88744403c934a84828d373cfccb8cdaa7507ad77`.

## Target Category

The complete maintained corpus, recursively enumerated under `data/pathways/`
including ignored and hidden files. The user explicitly authorized evidence-backed
edits and updates, extending the local review skills' normal read-only scope.

## Selection and Membership

Every record appears in the inventory below and in
[all-pathways-summary.json](all-pathways-summary.json), including its final SHA-256
and before/after graph counts. The cohort ledgers cover the full corpus without
sampling. No pathway record was added, deleted or merged.

## Validation

- `just validate`: passed, including native and closed LinkML schemas, independent
  identifier/label resolution, history links, provenance, sources, documentation,
  research-contract checks and generated-page consistency.
- `just test`: **531 passed, 3 skipped**.
- `just lint` and `git diff --check`: passed.
- All 18 governed files match the pinned canonical revision.
- Pages, KGX and SSSOM were regenerated from the final records.
- All **93** distinct byte hashes cited in final references or source locators
  match retained raw artifacts: [digest audit](source-digest-verification.json).

## Lump and Split Review

Alternative reaction routes, source-specific pathway scopes and taxon variants
remain separate where their biology differs. Shared names or reactions did not
justify merging records. Native activity and physical-state instances are retained
when a shared broad class would erase mechanistic distinctions.

## Identity and Grounding

Names and identifiers were checked against independently acquired ChEBI 255,
GO 2026-07-26, Rhea 139, NCBI Taxonomy 2026-05-13 and pinned primary provider
artifacts. Source-local identifiers retain the provider's exact asserted identity
and context; they are not an exemption from identifier existence checks.

## Graph and Evidence Patterns

The final corpus contains **3604 participant occurrences,
814 reaction occurrences and 7142 edges** (previously
4690 edges). These are per-record counts, not unique entities.
It includes 521 enzyme/cofactor links,
585 physical-location links,
342 activity/process-location links and
42 complex-composition links.

The final cofactor pass checked all152 records and added 371 source-backed
links across 93 records. Exact matches, source cautions, alternative metals,
covalent groups and inference grades are preserved. Source assertions have precise
locators and are rendered separately from verbatim quotations. KGX retains full
evidence, qualifications, provenance and each record's label/category/direction.

## Completeness Patterns

All native source reactions/facts have a represented or documented disposition
within the reviewed scope. Later chemistry and compartment ledgers explicitly
supersede affected native-import assertions; their counts must not be mistaken
for disjoint additions to the final graph.

The yeast chemical audit accounts for all 475 original activities: 440 retained,
29 corrected and 6 excluded, with one independently supported Vip1 activity added.
The final yeast cohort therefore contains 470 activities in 85 records.

Proteins, complexes, small molecules, lipids, cofactors and cellular components
were added where the inspected evidence supports them. The current metabolic
corpus did not establish additional DNA or RNA molecular participants; gene names
and references to transcription alone were not used to invent such nodes.

## Findings

Corrections include BNA3/BNA7 formamidase identity, ACO1/ACO2 versus LYS4 roles,
yeast cardiolipin chemistry, THI4/THI13 protein-residue chemistry, ADK2 nucleotide
specificity, FOX2 stereochemistry, folate oxidation states and MET13 co-substrate,
inositol regioisomers, incorrect directed material transfers and unsupported
compartment assignments. Full removed assertions remain in the ledgers.

Evidence limits remain explicit. Some broad taxon records support enzyme classes
without exact proteins; missing cofactor annotation is not cofactor independence.
Physical protein location is not automatically an activity location. The ADP-thiazole
hydrolysis bridge and mycothiol phosphate-removal step retain unresolved enzyme
assignments. Disputed CMP specificity and STR2 substrate annotations are qualified.
Native tyrosol isoenzyme assertions retain their source attribution; the inspected
related-substrate study is not presented as a direct tyrosine assay.
Vip1 hydrolysis is limited to the experimentally assayed recombinant domain; no
unmeasured in-vivo phenotype is asserted.

## Recommended Edits

The supported edits are applied. Preserve the source exclusions, activity scope,
conditional annotations and reviewed overrides during future source refreshes.
No additional current-corpus edit is blocked on user input.

## Follow-up Checks

Future provider updates should repeat source hash checks and resolve changed
scientific assertions before replaying migrations. Use `docs/CAUSAL_GRAPHS.md`
for the review contract. Migration scripts intentionally refuse unreviewed source
representations; their pinned raw inputs are cached outside the repository.

## Additional Notes

No paid research, GitHub changes or remote publication was performed. Expression
modules were not used as substitutes for direct biochemical evidence. The native
and cohort reports describe intermediate review stages; this report records the
final integrated result.

## Evidence ledgers

- [Native GO-CAM facts](../yaml_category_review/20261005-gocam-causal-graphs/gocam-causal-review.json)
  and [complex composition](../yaml_category_review/20261005-gocam-causal-graphs/complex-composition-review.json).
- [MetaCyc coverage and reproduction](README.metacyc.md) and [full ledger](metacyc-review.json).
- [Diagrams and MIBiG](../causal-graph-diagram-review.json).
- [Yeast compartments](gocam-location-review.json).
- [All yeast chemical-side dispositions](gocam-chemical-dispositions.json),
  [final independent comparisons](gocam-chemical-final.json),
  [initial detailed comparisons](gocam-chemical-review.json),
  [bounded corrections](gocam-chemical-corrections.json),
  [final supplement](gocam-chemical-final-supplement.json),
  [function corrections](gocam-function-review.json),
  [assignment conflicts](gocam-assignment-conflicts.json) and
  [folate/inositol chemistry](folate-inositol-chemistry-review.json).
- [Applied cofactors](uniprot-cofactor-plan.json), [reviewed caution decisions](uniprot-cofactor-decisions.json)
  and [selected unchanged UniProt source fields](uniprot-source-projection.json).

## Per-record inventory

| Record | Cohort | Participants | Reactions | Edges |
|---|---|---:|---:|---:|
| [2-phenylethanol-biosynthesis](../../data/pathways/2-phenylethanol-biosynthesis.yaml) | Diagrams and MIBiG | 26 | 11 | 38 |
| [4-aminobenzoate-biosynthesis-i](../../data/pathways/4-aminobenzoate-biosynthesis-i.yaml) | MetaCyc | 14 | 2 | 16 |
| [4-aminobutyrate-degradation](../../data/pathways/4-aminobutyrate-degradation.yaml) | GO-CAM native | 15 | 2 | 19 |
| [5-aminoimidazole-ribonucleotide-biosynthesis-i](../../data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-i.yaml) | MetaCyc | 30 | 5 | 52 |
| [5-aminoimidazole-ribonucleotide-biosynthesis-ii](../../data/pathways/5-aminoimidazole-ribonucleotide-biosynthesis-ii.yaml) | MetaCyc | 29 | 5 | 54 |
| [6-hydroxymethyl-dihydropterin-diphosphate-biosynthesis-i](../../data/pathways/6-hydroxymethyl-dihydropterin-diphosphate-biosynthesis-i.yaml) | GO-CAM native | 22 | 5 | 41 |
| [acetate-and-atp-formation-from-acetyl-coa-i](../../data/pathways/acetate-and-atp-formation-from-acetyl-coa-i.yaml) | MetaCyc | 14 | 2 | 17 |
| [acetogenesis](../../data/pathways/acetogenesis.yaml) | Diagrams and MIBiG | 43 | 12 | 60 |
| [adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii](../../data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml) | GO-CAM native | 21 | 3 | 42 |
| [adenosine-ribonucleotides-de-novo-biosynthesis](../../data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml) | GO-CAM native | 21 | 4 | 33 |
| [aerobic-glycerol-degradation](../../data/pathways/aerobic-glycerol-degradation.yaml) | GO-CAM native | 16 | 2 | 19 |
| [allantoin-degradation-to-glyoxylate-i](../../data/pathways/allantoin-degradation-to-glyoxylate-i.yaml) | GO-CAM native | 13 | 3 | 21 |
| [allantoin-degradation-to-ureidoglycolate-i](../../data/pathways/allantoin-degradation-to-ureidoglycolate-i.yaml) | GO-CAM native | 11 | 2 | 16 |
| [aspartate-biosynthesis](../../data/pathways/aspartate-biosynthesis.yaml) | GO-CAM native | 22 | 4 | 44 |
| [assimilatory-sulfate-reduction](../../data/pathways/assimilatory-sulfate-reduction.yaml) | GO-CAM native | 29 | 4 | 50 |
| [beta-alanine-biosynthesis-iv](../../data/pathways/beta-alanine-biosynthesis-iv.yaml) | GO-CAM native | 16 | 3 | 28 |
| [carnitine-shuttle](../../data/pathways/carnitine-shuttle.yaml) | GO-CAM native | 12 | 4 | 32 |
| [chitin-biosynthesis](../../data/pathways/chitin-biosynthesis.yaml) | GO-CAM native | 12 | 3 | 29 |
| [chorismate-biosynthesis-i](../../data/pathways/chorismate-biosynthesis-i.yaml) | MetaCyc | 41 | 7 | 66 |
| [citrulline-biosynthesis](../../data/pathways/citrulline-biosynthesis.yaml) | GO-CAM native | 20 | 2 | 28 |
| [coenzyme-a-biosynthesis-i-prokaryotic](../../data/pathways/coenzyme-a-biosynthesis-i-prokaryotic.yaml) | MetaCyc | 23 | 4 | 38 |
| [d-arabinose-degradation-i](../../data/pathways/d-arabinose-degradation-i.yaml) | MetaCyc | 8 | 2 | 10 |
| [d-galacturonate-degradation-i](../../data/pathways/d-galacturonate-degradation-i.yaml) | MetaCyc | 18 | 5 | 27 |
| [d-glucarate-degradation-i](../../data/pathways/d-glucarate-degradation-i.yaml) | MetaCyc | 17 | 5 | 30 |
| [d-xylose-degradation-i](../../data/pathways/d-xylose-degradation-i.yaml) | MetaCyc | 13 | 2 | 14 |
| [dolichyl-glucosyl-phosphate-biosynthesis](../../data/pathways/dolichyl-glucosyl-phosphate-biosynthesis.yaml) | GO-CAM native | 20 | 5 | 45 |
| [dolichyl-phosphate-d-mannose-biosynthesis](../../data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml) | GO-CAM native | 22 | 4 | 35 |
| [ectoine-biosynthesis](../../data/pathways/ectoine-biosynthesis.yaml) | MetaCyc | 28 | 5 | 38 |
| [epoxysqualene-biosynthesis](../../data/pathways/epoxysqualene-biosynthesis.yaml) | GO-CAM native | 20 | 3 | 26 |
| [ergosterol-biosynthesis-i](../../data/pathways/ergosterol-biosynthesis-i.yaml) | GO-CAM native | 24 | 5 | 47 |
| [ethanol-degradation](../../data/pathways/ethanol-degradation.yaml) | GO-CAM native | 26 | 6 | 68 |
| [fatty-acid-elongation](../../data/pathways/fatty-acid-elongation.yaml) | GO-CAM native | 22 | 8 | 70 |
| [fatty-acid-oxidation-pathway](../../data/pathways/fatty-acid-oxidation-pathway.yaml) | GO-CAM native | 39 | 11 | 109 |
| [flavin-biosynthesis-i](../../data/pathways/flavin-biosynthesis-i.yaml) | MetaCyc | 43 | 9 | 84 |
| [folate-interconversions](../../data/pathways/folate-interconversions.yaml) | GO-CAM native | 45 | 14 | 138 |
| [formaldehyde-oxidation-ii-glutathione-dependent](../../data/pathways/formaldehyde-oxidation-ii-glutathione-dependent.yaml) | GO-CAM native | 21 | 4 | 37 |
| [galactose-degradation](../../data/pathways/galactose-degradation.yaml) | GO-CAM native | 21 | 6 | 42 |
| [gluconeogenesis-i](../../data/pathways/gluconeogenesis-i.yaml) | GO-CAM native | 47 | 15 | 158 |
| [glutamate-degradation-i](../../data/pathways/glutamate-degradation-i.yaml) | Diagrams and MIBiG | 14 | 3 | 19 |
| [glutathione-biosynthesis](../../data/pathways/glutathione-biosynthesis.yaml) | MetaCyc | 16 | 2 | 22 |
| [glutathione-degradation](../../data/pathways/glutathione-degradation.yaml) | GO-CAM native | 17 | 2 | 20 |
| [glutathione-glutaredoxin-redox-reaction](../../data/pathways/glutathione-glutaredoxin-redox-reaction.yaml) | Diagrams and MIBiG | 15 | 3 | 18 |
| [glycerol-biosynthesis](../../data/pathways/glycerol-biosynthesis.yaml) | GO-CAM native | 20 | 4 | 44 |
| [glycerol-degradation-v](../../data/pathways/glycerol-degradation-v.yaml) | MetaCyc | 10 | 2 | 12 |
| [glycine-cleavage](../../data/pathways/glycine-cleavage.yaml) | GO-CAM native | 20 | 3 | 26 |
| [glycogen-catabolism](../../data/pathways/glycogen-catabolism.yaml) | Diagrams and MIBiG | 11 | 2 | 13 |
| [glycolysis-i-from-glucose-6-phosphate](../../data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml) | GO-CAM native | 42 | 14 | 148 |
| [glyoxylate-cycle](../../data/pathways/glyoxylate-cycle.yaml) | MetaCyc | 26 | 6 | 50 |
| [guanosine-ribonucleotides-de-novo-biosynthesis](../../data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml) | GO-CAM native | 27 | 6 | 64 |
| [heme-biosynthesis-i-aerobic](../../data/pathways/heme-biosynthesis-i-aerobic.yaml) | GO-CAM native | 21 | 4 | 36 |
| [hexaprenyl-diphosphate-biosynthesis](../../data/pathways/hexaprenyl-diphosphate-biosynthesis.yaml) | GO-CAM native | 18 | 5 | 44 |
| [homocysteine-and-cysteine-interconversion](../../data/pathways/homocysteine-and-cysteine-interconversion.yaml) | GO-CAM native | 20 | 4 | 39 |
| [inosine-5-phosphate-biosynthesis-i](../../data/pathways/inosine-5-phosphate-biosynthesis-i.yaml) | MetaCyc | 28 | 6 | 44 |
| [inosine-5-phosphate-biosynthesis-ii](../../data/pathways/inosine-5-phosphate-biosynthesis-ii.yaml) | MetaCyc | 22 | 5 | 31 |
| [inositol-phosphate-biosynthesis](../../data/pathways/inositol-phosphate-biosynthesis.yaml) | GO-CAM native | 33 | 15 | 118 |
| [isoleucine-degradation](../../data/pathways/isoleucine-degradation.yaml) | Diagrams and MIBiG | 24 | 3 | 35 |
| [l-arabinose-degradation-i](../../data/pathways/l-arabinose-degradation-i.yaml) | MetaCyc | 17 | 3 | 23 |
| [l-arginine-biosynthesis-i](../../data/pathways/l-arginine-biosynthesis-i.yaml) | MetaCyc | 54 | 9 | 91 |
| [l-arginine-biosynthesis-ii-acetyl-cycle](../../data/pathways/l-arginine-biosynthesis-ii-acetyl-cycle.yaml) | GO-CAM native | 44 | 10 | 91 |
| [l-arginine-degradation-ii-ast-pathway](../../data/pathways/l-arginine-degradation-ii-ast-pathway.yaml) | MetaCyc | 30 | 5 | 43 |
| [l-arginine-degradation-iv](../../data/pathways/l-arginine-degradation-iv.yaml) | MetaCyc | 15 | 3 | 23 |
| [l-arginine-degradation-v](../../data/pathways/l-arginine-degradation-v.yaml) | MetaCyc | 19 | 4 | 28 |
| [l-asparagine-biosynthesis-i](../../data/pathways/l-asparagine-biosynthesis-i.yaml) | GO-CAM native | 21 | 4 | 46 |
| [l-asparagine-degradation](../../data/pathways/l-asparagine-degradation.yaml) | GO-CAM native | 22 | 7 | 58 |
| [l-cysteine-biosynthesis-i](../../data/pathways/l-cysteine-biosynthesis-i.yaml) | MetaCyc | 14 | 2 | 18 |
| [l-cysteine-biosynthesis-iii-from-l-homocysteine](../../data/pathways/l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml) | GO-CAM native | 13 | 2 | 19 |
| [l-fucose-degradation-i](../../data/pathways/l-fucose-degradation-i.yaml) | MetaCyc | 14 | 4 | 19 |
| [l-histidine-biosynthesis](../../data/pathways/l-histidine-biosynthesis.yaml) | MetaCyc | 44 | 10 | 85 |
| [l-homocysteine-biosynthesis](../../data/pathways/l-homocysteine-biosynthesis.yaml) | GO-CAM native | 14 | 2 | 19 |
| [l-homoserine-biosynthesis](../../data/pathways/l-homoserine-biosynthesis.yaml) | MetaCyc | 19 | 3 | 28 |
| [l-isoleucine-biosynthesis-i-from-threonine](../../data/pathways/l-isoleucine-biosynthesis-i-from-threonine.yaml) | MetaCyc | 35 | 7 | 57 |
| [l-leucine-biosynthesis](../../data/pathways/l-leucine-biosynthesis.yaml) | MetaCyc | 30 | 6 | 49 |
| [l-lysine-biosynthesis-i](../../data/pathways/l-lysine-biosynthesis-i.yaml) | MetaCyc | 51 | 10 | 90 |
| [l-lysine-biosynthesis-iv](../../data/pathways/l-lysine-biosynthesis-iv.yaml) | GO-CAM native | 39 | 9 | 89 |
| [l-methionine-biosynthesis-i](../../data/pathways/l-methionine-biosynthesis-i.yaml) | MetaCyc | 33 | 7 | 50 |
| [l-ornithine-biosynthesis-i](../../data/pathways/l-ornithine-biosynthesis-i.yaml) | MetaCyc | 33 | 5 | 47 |
| [l-phenylalanine-biosynthesis-i](../../data/pathways/l-phenylalanine-biosynthesis-i.yaml) | MetaCyc | 15 | 3 | 22 |
| [l-proline-biosynthesis-i-from-l-glutamate](../../data/pathways/l-proline-biosynthesis-i-from-l-glutamate.yaml) | MetaCyc | 19 | 4 | 33 |
| [l-proline-degradation](../../data/pathways/l-proline-degradation.yaml) | GO-CAM native | 17 | 3 | 25 |
| [l-rhamnose-degradation-i](../../data/pathways/l-rhamnose-degradation-i.yaml) | MetaCyc | 15 | 5 | 22 |
| [l-serine-biosynthesis-i](../../data/pathways/l-serine-biosynthesis-i.yaml) | MetaCyc | 23 | 3 | 28 |
| [l-threonine-biosynthesis](../../data/pathways/l-threonine-biosynthesis.yaml) | MetaCyc | 14 | 2 | 16 |
| [l-tryptophan-biosynthesis](../../data/pathways/l-tryptophan-biosynthesis.yaml) | MetaCyc | 29 | 6 | 48 |
| [l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde](../../data/pathways/l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde.yaml) | GO-CAM native | 28 | 5 | 47 |
| [l-tyrosine-biosynthesis-i](../../data/pathways/l-tyrosine-biosynthesis-i.yaml) | MetaCyc | 16 | 3 | 22 |
| [l-tyrosine-degradation-iii](../../data/pathways/l-tyrosine-degradation-iii.yaml) | GO-CAM native | 34 | 10 | 121 |
| [l-valine-biosynthesis](../../data/pathways/l-valine-biosynthesis.yaml) | MetaCyc | 29 | 4 | 44 |
| [leucine-degradation](../../data/pathways/leucine-degradation.yaml) | GO-CAM native | 29 | 9 | 81 |
| [linearmycin-biosynthetic-gene-cluster](../../data/pathways/linearmycin-biosynthetic-gene-cluster.yaml) | Diagrams and MIBiG | 4 | 0 | 4 |
| [lipid-iva-biosynthesis](../../data/pathways/lipid-iva-biosynthesis.yaml) | GO-CAM native | 20 | 6 | 33 |
| [mannose-degradation](../../data/pathways/mannose-degradation.yaml) | GO-CAM native | 14 | 4 | 31 |
| [methionine-salvage-pathway](../../data/pathways/methionine-salvage-pathway.yaml) | GO-CAM native | 34 | 9 | 82 |
| [methylglyoxal-catabolism](../../data/pathways/methylglyoxal-catabolism.yaml) | GO-CAM native | 14 | 3 | 26 |
| [mevalonate-pathway](../../data/pathways/mevalonate-pathway.yaml) | GO-CAM native | 31 | 7 | 63 |
| [mycobacterium-trehalose-biosynthesis](../../data/pathways/mycobacterium-trehalose-biosynthesis.yaml) | Diagrams and MIBiG | 21 | 5 | 50 |
| [mycothiol-biosynthesis](../../data/pathways/mycothiol-biosynthesis.yaml) | Diagrams and MIBiG | 32 | 7 | 78 |
| [mycothiol-catabolism](../../data/pathways/mycothiol-catabolism.yaml) | Diagrams and MIBiG | 9 | 1 | 14 |
| [myo-inositol-biosynthesis](../../data/pathways/myo-inositol-biosynthesis.yaml) | GO-CAM native | 14 | 3 | 25 |
| [n-acetylglucosamine-degradation-i](../../data/pathways/n-acetylglucosamine-degradation-i.yaml) | MetaCyc | 17 | 2 | 22 |
| [nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde](../../data/pathways/nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde.yaml) | GO-CAM native | 24 | 5 | 48 |
| [nad-de-novo-biosynthesis-i-from-aspartate](../../data/pathways/nad-de-novo-biosynthesis-i-from-aspartate.yaml) | MetaCyc | 26 | 6 | 48 |
| [nad-salvage-pathway-i-pnc-vi-cycle](../../data/pathways/nad-salvage-pathway-i-pnc-vi-cycle.yaml) | MetaCyc | 24 | 6 | 48 |
| [nad-salvage-pathway-iv-from-nicotinamide-riboside](../../data/pathways/nad-salvage-pathway-iv-from-nicotinamide-riboside.yaml) | GO-CAM native | 16 | 3 | 28 |
| [nad-salvage-pathway-v](../../data/pathways/nad-salvage-pathway-v.yaml) | Diagrams and MIBiG | 28 | 5 | 41 |
| [oleate-biosynthesis](../../data/pathways/oleate-biosynthesis.yaml) | GO-CAM native | 16 | 2 | 19 |
| [palmitoleate-biosynthesis](../../data/pathways/palmitoleate-biosynthesis.yaml) | GO-CAM native | 16 | 2 | 20 |
| [pentose-phosphate-pathway-non-oxidative-branch-i](../../data/pathways/pentose-phosphate-pathway-non-oxidative-branch-i.yaml) | MetaCyc | 26 | 5 | 49 |
| [pentose-phosphate-pathway-oxidative-branch-i](../../data/pathways/pentose-phosphate-pathway-oxidative-branch-i.yaml) | MetaCyc | 15 | 3 | 22 |
| [peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways](../../data/pathways/peptidoglycan-cytoplasmic-synthesis-and-recycling-pathways.yaml) | Diagrams and MIBiG | 80 | 29 | 127 |
| [periplasmic-nad-degradation](../../data/pathways/periplasmic-nad-degradation.yaml) | GO-CAM native | 16 | 2 | 19 |
| [phenylalanine-biosynthesis](../../data/pathways/phenylalanine-biosynthesis.yaml) | GO-CAM native | 19 | 4 | 33 |
| [phosphatidate-biosynthesis-i-the-dihydroxyacetone-pathway](../../data/pathways/phosphatidate-biosynthesis-i-the-dihydroxyacetone-pathway.yaml) | GO-CAM native | 20 | 4 | 33 |
| [phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway](../../data/pathways/phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway.yaml) | GO-CAM native | 22 | 5 | 43 |
| [phosphatidylcholine-biosynthesis-i](../../data/pathways/phosphatidylcholine-biosynthesis-i.yaml) | GO-CAM native | 21 | 3 | 28 |
| [phosphatidylethanolamine-biosynthesis-i](../../data/pathways/phosphatidylethanolamine-biosynthesis-i.yaml) | GO-CAM native | 23 | 3 | 34 |
| [phosphatidylinositol-phosphate-biosynthesis](../../data/pathways/phosphatidylinositol-phosphate-biosynthesis.yaml) | GO-CAM native | 37 | 21 | 239 |
| [phospholipid-biosynthesis-ii-kennedy-pathway](../../data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml) | GO-CAM native | 20 | 3 | 28 |
| [phospholipid-biosynthesis](../../data/pathways/phospholipid-biosynthesis.yaml) | GO-CAM native | 41 | 9 | 89 |
| [phospholipids-degradation](../../data/pathways/phospholipids-degradation.yaml) | Diagrams and MIBiG | 6 | 1 | 6 |
| [phosphopantothenate-biosynthesis-i](../../data/pathways/phosphopantothenate-biosynthesis-i.yaml) | MetaCyc | 30 | 4 | 42 |
| [ppgpp-metabolism](../../data/pathways/ppgpp-metabolism.yaml) | MetaCyc | 15 | 6 | 41 |
| [pyridoxal-5-phosphate-biosynthesis-i](../../data/pathways/pyridoxal-5-phosphate-biosynthesis-i.yaml) | MetaCyc | 40 | 7 | 67 |
| [pyridoxal-5-phosphate-salvage-i](../../data/pathways/pyridoxal-5-phosphate-salvage-i.yaml) | MetaCyc | 21 | 5 | 42 |
| [pyruvate-decarboxylation-to-acetyl-coa](../../data/pathways/pyruvate-decarboxylation-to-acetyl-coa.yaml) | GO-CAM native | 21 | 4 | 36 |
| [pyruvate-fermentation-to-acetoin-iii](../../data/pathways/pyruvate-fermentation-to-acetoin-iii.yaml) | GO-CAM native | 14 | 9 | 80 |
| [s-adenosyl-l-methionine-cycle-ii](../../data/pathways/s-adenosyl-l-methionine-cycle-ii.yaml) | GO-CAM native | 24 | 5 | 45 |
| [salvage-pathways-of-pyrimidine-ribonucleotides](../../data/pathways/salvage-pathways-of-pyrimidine-ribonucleotides.yaml) | GO-CAM native | 32 | 9 | 82 |
| [siroheme-biosynthesis](../../data/pathways/siroheme-biosynthesis.yaml) | GO-CAM native | 14 | 3 | 25 |
| [spermidine-biosynthesis-i](../../data/pathways/spermidine-biosynthesis-i.yaml) | GO-CAM native | 12 | 2 | 17 |
| [spermine-biosynthesis](../../data/pathways/spermine-biosynthesis.yaml) | GO-CAM native | 12 | 2 | 16 |
| [sphingolipid-biosynthesis-yeast](../../data/pathways/sphingolipid-biosynthesis-yeast.yaml) | GO-CAM native | 65 | 20 | 207 |
| [sulfate-activation-for-sulfonation](../../data/pathways/sulfate-activation-for-sulfonation.yaml) | GO-CAM native | 12 | 2 | 18 |
| [superoxide-radicals-degradation](../../data/pathways/superoxide-radicals-degradation.yaml) | GO-CAM native | 19 | 4 | 34 |
| [tca-cycle-detailed](../../data/pathways/tca-cycle-detailed.yaml) | Diagrams and MIBiG | 49 | 9 | 75 |
| [tetrahydrofolate-biosynthesis](../../data/pathways/tetrahydrofolate-biosynthesis.yaml) | GO-CAM native | 21 | 3 | 29 |
| [tetrapyrrole-biosynthesis](../../data/pathways/tetrapyrrole-biosynthesis.yaml) | GO-CAM native | 21 | 4 | 32 |
| [thiamine-biosynthesis](../../data/pathways/thiamine-biosynthesis.yaml) | GO-CAM native | 41 | 10 | 102 |
| [threonine-degradation](../../data/pathways/threonine-degradation.yaml) | GO-CAM native | 12 | 2 | 16 |
| [trans-trans-farnesyl-diphosphate-biosynthesis](../../data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml) | GO-CAM native | 11 | 3 | 24 |
| [trehalose-biosynthesis-i](../../data/pathways/trehalose-biosynthesis-i.yaml) | MetaCyc | 16 | 2 | 18 |
| [triglyceride-biosynthesis](../../data/pathways/triglyceride-biosynthesis.yaml) | Diagrams and MIBiG | 20 | 5 | 29 |
| [tryptophan-degradation](../../data/pathways/tryptophan-degradation.yaml) | GO-CAM native | 36 | 12 | 121 |
| [tyrosine-biosynthesis](../../data/pathways/tyrosine-biosynthesis.yaml) | GO-CAM native | 19 | 4 | 32 |
| [ubiquinol-6-biosynthesis-from-4-hydroxybenzoate](../../data/pathways/ubiquinol-6-biosynthesis-from-4-hydroxybenzoate.yaml) | Diagrams and MIBiG | 29 | 8 | 52 |
| [udp-n-acetylglucosamine-biosynthesis](../../data/pathways/udp-n-acetylglucosamine-biosynthesis.yaml) | GO-CAM native | 21 | 4 | 35 |
| [ump-biosynthesis-i](../../data/pathways/ump-biosynthesis-i.yaml) | MetaCyc | 38 | 6 | 54 |
| [urea-degradation-i](../../data/pathways/urea-degradation-i.yaml) | GO-CAM native | 13 | 2 | 21 |
| [utp-and-ctp-de-novo-biosynthesis](../../data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml) | GO-CAM native | 21 | 4 | 46 |
| [valine-degradation](../../data/pathways/valine-degradation.yaml) | GO-CAM native | 32 | 11 | 125 |
| [very-long-chain-fatty-acid-biosynthesis](../../data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml) | GO-CAM native | 21 | 5 | 42 |
| [xylose-metabolism](../../data/pathways/xylose-metabolism.yaml) | GO-CAM native | 15 | 2 | 19 |
| [zymosterol-biosynthesis](../../data/pathways/zymosterol-biosynthesis.yaml) | GO-CAM native | 34 | 12 | 102 |

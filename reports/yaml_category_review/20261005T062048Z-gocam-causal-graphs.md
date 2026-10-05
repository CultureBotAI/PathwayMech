# YAML Category Review: All GO-CAM causal graphs

Repository: CultureBotAI/PathwayMech. Category: root namespace `gomodel`. Selection: all recursive `data/pathways/**/*.yaml` records with that root. Review started 2026-10-05 UTC; this stage finished 2026-10-05T06:20:35Z. Verdict: all 86 reviewed and updated; explicit source limitations retained. User authorized curation in addition to the category/record review skills.

## Target Category

The cohort contains 85 Saccharomyces cerevisiae S288C records and one Escherichia coli K-12 lipid IV(A) record. This review covers every record and every native source fact, not a sample. Counts below describe the native reconstruction, independent GLY1 route, and complex-composition stage. Subsequent compartment, catalytic-function, and chemical-side reviews supersede specific imported assertions using independent sources; their ledgers under `reports/causal_graph_review/` preserve the exact replaced facts. The counts here precede those reconciliations and corpus-wide UniProt cofactor enrichment.

## Selection and Membership

All 86 root identifiers matched independently cached members of the [official Noctua JSON archive](https://current.geneontology.org/products/json/noctua-models-json.tgz). The exact archive SHA-256 is `7a6999245e9265f2167d6e47c7565adb17433ad26611f1a877dc79564279523b`. Every member filename and SHA-256, all 4,038 source triples, and each triple disposition are recorded in `20261005-gocam-causal-graphs/gocam-causal-review.json`. Archive membership was enumerated directly; filesystem searches used ignored/hidden-inclusive discovery.

## Validation

All 86 final candidates passed `validate_record`. The native converter regression suite passed 5 tests, covering direction, precise causality, physical-instance separation, unknown facts, and explicit scope exclusions. There were 2,953 original edges; all matched native assertions after relation/orientation normalization. The reviewed stage contains 3,989 edges, 481 reaction/activity nodes, and 1,594 participant entries. The parent workflow runs corpus-wide identifier, LinkML, evidence, renderer, and integration gates after combining all cohorts.

## Lump and Split Review

The 86 primary model identities are distinct. Shared reactions and enzyme classes across adjacent biosynthetic, salvage, and catabolic routes do not establish duplicate pathway identities. Existing source pathway boundaries and taxa were preserved. The threonine record required a narrower enzyme-supported scope than its broader imported reaction outline; no record was merged merely because it shared intermediates or enzymes.

## Identity and Grounding

Existing grounded class IDs were checked against native individual types. A class projection is explicit in each edge locator. Generic physical individuals retain native gomodel IDs, preventing ferro-/ferricytochrome b5 redox partners from collapsing into CHEBI:33695, and keeping unspecified proteins and chemicals separate. Six previously omitted lipid IV(A) enablers retain native model IDs because the source types are EcoCyc IDs; the source supplies LpxA, LpxC, LpxD, LpxH, LpxB, and LpxK. One source input in very-long-chain fatty-acid biosynthesis has no type or label at all; its native ID is preserved without inventing a chemical identity.

ChEBI release 255 `is_a` ancestry supplies physical categories (SHA-256 `6cd3c7f18d8b22c577e110e00008fb288d8f5b34424bbe5011858747062f9dd9`). Lipid/protein/DNA/RNA classes are used only when supported by that ancestry; macromolecules and generic chemical entities can remain unclassified. No DNA or RNA molecular participant is asserted by the inspected cohort source facts. Biological-process descriptions mentioning transcription or DNA repair do not establish DNA/RNA reactants.

## Graph and Evidence Patterns

Native RO:0002233/RO:0002234 remain activity→participant `has_input`/`has_output`; they do not assert that every input is chemically consumed. RO:0002411 becomes `causally_upstream_of` and RO:0002413 becomes `provides_input_for`, preserving the [Relation Ontology definitions](https://raw.githubusercontent.com/oborel/obo-relations/master/ro.obo). Their former labels `regulates` and `precedes` respectively overstated regulation and lost material flow. Native enabled_by is inverted to protein→activity `enables`.

Activity `occurs_in`, process `part_of`, and complex `has_part` facts are retained as distinct relations. Physical locations are not inferred from reaction locations. The native model supplied 489 activity-location assertions and 491 membership assertions; 10 of each belong to explicitly excluded threonine outline activities. All included location/membership facts are represented. Duplicate projected triples retain all their exact fact locators as separate evidence items.

Every native edge now cites a faithful `source_assertion` and an exact archive-member JSON fact index plus endpoint type indexes. The source reference carries the archive URL, model date/member, and archive SHA-256. These assertions do not masquerade as article quotations or claim that every cited PMID was read. SGD [documents the YeastPathways conversion](https://geneontology.org/GO_REF/0000123.html) as curator-maintained imported pathway data with combinatorial evidence; this limitation remains relevant even when a model is in production.

## Completeness Patterns

3,973 of 4,038 native facts are represented, as 3,949 distinct projected edges. The other 65 facts are not silently dropped: they concern ten out-of-scope, unassigned threonine-outline activities. Source-supported SAM methyl transfer and diphosphoinositol pentakisphosphate phosphorylation steps were restored without inventing enablers. Five included native activities have no assigned enabling protein: RXN0-745, RXN3O-9819, SPONTPRO-RXN, RXN-5721, and RXN-7605. Some are spontaneous or generic steps; absence of an enabler is not evidence of an unknown enzyme.

Independent [reviewed UniProt GLY1](https://www.uniprot.org/uniprotkb/P37303/entry) supplies the missing yeast threonine aldolase route: L-threonine input, glycine and acetaldehyde outputs, enzyme, pathway membership, and protein cytosol annotation. The exact JSON source, SHA-256, version 198, native chemical cross-references, and experimental evidence attribution are retained. The original assay article is [PMID:9151955](https://pubmed.ncbi.nlm.nih.gov/9151955/); the graph cites inspected UniProt structured annotations rather than fabricating article quotations.

All eight SGD enzyme complexes were checked against exact [Complex Portal API](https://www.ebi.ac.uk/intact/complex-ws/complex/) records. Their protein and small-molecule components were restored in seven pathway records; exact UniProt SGD cross-references avoid duplicate protein aliases. The native CPA1/CPA2 composition and original model provenance were also propagated to the same complex in citrulline biosynthesis. Evidence grades remain explicit: CPX-1103 is inferred by paralogy; CPX-3163 and CPX-1268 are inferred by curator; the other five have physical-interaction evidence. Stoichiometry is preserved in descriptions, not converted into unsupported reaction coefficients. Complex small-molecule constituents include iron cation, Fe4S4, FAD, FMN, and siroheme.

## Findings

1. **Corrected systematic omissions and relation semantics:** all 86 records gained accurate source assertion provenance and preserved relevant source component/context facts. Generic physical identities and six lipid IV(A) enablers were restored.
2. **Preserved species scope:** the [SGD threonine summary](https://pathway.yeastgenome.org/YEAST/NEW-IMAGE?object=THREOCAT2-PWY) explicitly says yeast lacks KBL and that TDH existence is uncertain. AKBLIG-RXN, THREODEHYD-RXN, and presumed downstream THREOSPON-RXN cannot become established yeast reactions solely from archive membership. Seven additional unassigned side-branch reactions lack independent species support in the inspected summary. All ten exclusions have individual reasons in the ledger. GLY1 provides an independently supported omitted route.
3. **Location reconciliation:** Complex Portal places CPX-1739 at the Golgi, conflicting with its imported activity cytosol assertion; the subsequent compartment review reconciles that activity to the supported Golgi context. CPX-1268 and its native glycine-cleavage activity both specify the mitochondrion, so they do not constitute a source conflict. Physical complex location and activity location remain distinct assertions.
4. **Source-limited identities:** unspecified proteins/chemicals and one untyped native input remain source-local. No particular cofactor, gene, RNA, DNA, membrane structure, or enzyme was invented to fill those placeholders.

## Recommended Edits

The scientifically supported edits above are applied. Additional enzyme/cofactor enrichment must use exact reviewed protein identities and retain source cautions, conditions, and evidence grades. Reconcile the explicit cytosol/organelle disagreements with species-specific experiments before asserting exclusive physical locations. Native-source refreshes must preserve independently cited enrichment edges and cofactor categories.

## Follow-up Checks

Reproduce the native stage from the exact external artifacts (hashes are checked; changed source releases require a new review):

```bash
PYTHONPATH=src .venv/bin/python scripts/review_gocam_graphs.py \
  --archive "$CACHE/noctua-models-json.tgz" \
  --chebi "$CACHE/chebi.obo" \
  --gly1-uniprot "$CACHE/gly1-uniprot.json" \
  --records data/pathways \
  --report-dir reports/yaml_category_review/20261005-gocam-causal-graphs \
  --write

PYTHONPATH=src:scripts .venv/bin/python scripts/review_gocam_complexes.py \
  --complex-dir "$CACHE/complexportal" \
  --uniprot-json "$CACHE/uniprot-yeast-reviewed-cofactors.json" \
  --uniprot-provenance "$CACHE/uniprot-yeast-reviewed-cofactors.provenance.json" \
  --chebi "$CACHE/chebi.obo" \
  --records data/pathways \
  --report reports/yaml_category_review/20261005-gocam-causal-graphs/complex-composition-review.json \
  --write
```

Without `--write` both commands validate candidate records and write only a report. No partial record publication occurs before every candidate validates. `CACHE` is a user-supplied external source directory. Obtain raw artifacts from the URLs in the ledger and source constants, preserving exact bytes; the current URL may later serve different bytes. The reviewed UniProt proteome provenance must match the supplied raw JSON SHA-256.

## Additional Notes

iModulonDB expression modules were not causal evidence for these exact native metabolic facts and were not used to infer regulation. Source curation history and evidence strengths are preserved. No GitHub mutation or paid research call was made.

### Exhaustive per-record status

Every row below is reviewed and updated. “Native facts” is represented/total; excluded facts are explained above. Counts include GLY1 and complex composition but precede the separate UniProt cofactor pass.

| Record | Native facts | Activities | Edges | Specific scope/source note |
|---|---:|---:|---:|---|
| [4-aminobutyrate-degradation.yaml](../../data/pathways/4-aminobutyrate-degradation.yaml) | 16/16 | 2 | 16 | all native facts represented |
| [6-hydroxymethyl-dihydropterin-diphosphate-biosynthesis-i.yaml](../../data/pathways/6-hydroxymethyl-dihydropterin-diphosphate-biosynthesis-i.yaml) | 41/41 | 5 | 41 | all native facts represented |
| [adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml](../../data/pathways/adenosine-deoxyribonucleotides-de-novo-biosynthesis-ii.yaml) | 32/32 | 4 | 43 | unassigned/spontaneous activity retained; complex composition reviewed |
| [adenosine-ribonucleotides-de-novo-biosynthesis.yaml](../../data/pathways/adenosine-ribonucleotides-de-novo-biosynthesis.yaml) | 28/28 | 4 | 28 | all native facts represented |
| [aerobic-glycerol-degradation.yaml](../../data/pathways/aerobic-glycerol-degradation.yaml) | 16/16 | 2 | 16 | all native facts represented |
| [allantoin-degradation-to-glyoxylate-i.yaml](../../data/pathways/allantoin-degradation-to-glyoxylate-i.yaml) | 20/20 | 3 | 20 | all native facts represented |
| [allantoin-degradation-to-ureidoglycolate-i.yaml](../../data/pathways/allantoin-degradation-to-ureidoglycolate-i.yaml) | 15/15 | 2 | 15 | all native facts represented |
| [aspartate-biosynthesis.yaml](../../data/pathways/aspartate-biosynthesis.yaml) | 34/34 | 4 | 34 | all native facts represented |
| [assimilatory-sulfate-reduction.yaml](../../data/pathways/assimilatory-sulfate-reduction.yaml) | 39/39 | 4 | 44 | complex composition reviewed |
| [beta-alanine-biosynthesis-iv.yaml](../../data/pathways/beta-alanine-biosynthesis-iv.yaml) | 26/26 | 3 | 25 | all native facts represented |
| [carnitine-shuttle.yaml](../../data/pathways/carnitine-shuttle.yaml) | 30/30 | 4 | 30 | all native facts represented |
| [chitin-biosynthesis.yaml](../../data/pathways/chitin-biosynthesis.yaml) | 27/27 | 3 | 27 | all native facts represented |
| [citrulline-biosynthesis.yaml](../../data/pathways/citrulline-biosynthesis.yaml) | 20/20 | 2 | 23 | complex composition reviewed |
| [dolichyl-glucosyl-phosphate-biosynthesis.yaml](../../data/pathways/dolichyl-glucosyl-phosphate-biosynthesis.yaml) | 39/39 | 5 | 39 | all native facts represented |
| [dolichyl-phosphate-d-mannose-biosynthesis.yaml](../../data/pathways/dolichyl-phosphate-d-mannose-biosynthesis.yaml) | 28/28 | 4 | 28 | all native facts represented |
| [epoxysqualene-biosynthesis.yaml](../../data/pathways/epoxysqualene-biosynthesis.yaml) | 24/24 | 3 | 24 | all native facts represented |
| [ergosterol-biosynthesis-i.yaml](../../data/pathways/ergosterol-biosynthesis-i.yaml) | 47/47 | 5 | 45 | all native facts represented |
| [ethanol-degradation.yaml](../../data/pathways/ethanol-degradation.yaml) | 74/74 | 8 | 74 | all native facts represented |
| [fatty-acid-elongation.yaml](../../data/pathways/fatty-acid-elongation.yaml) | 70/70 | 8 | 69 | all native facts represented |
| [fatty-acid-oxidation-pathway.yaml](../../data/pathways/fatty-acid-oxidation-pathway.yaml) | 98/98 | 11 | 98 | all native facts represented |
| [folate-interconversions.yaml](../../data/pathways/folate-interconversions.yaml) | 131/131 | 14 | 137 | complex composition reviewed |
| [formaldehyde-oxidation-ii-glutathione-dependent.yaml](../../data/pathways/formaldehyde-oxidation-ii-glutathione-dependent.yaml) | 32/32 | 4 | 32 | all native facts represented |
| [galactose-degradation.yaml](../../data/pathways/galactose-degradation.yaml) | 35/35 | 6 | 35 | all native facts represented |
| [gluconeogenesis-i.yaml](../../data/pathways/gluconeogenesis-i.yaml) | 140/140 | 16 | 140 | all native facts represented |
| [glutathione-degradation.yaml](../../data/pathways/glutathione-degradation.yaml) | 15/15 | 2 | 15 | all native facts represented |
| [glycerol-biosynthesis.yaml](../../data/pathways/glycerol-biosynthesis.yaml) | 34/34 | 4 | 34 | all native facts represented |
| [glycine-cleavage.yaml](../../data/pathways/glycine-cleavage.yaml) | 24/24 | 3 | 24 | all native facts represented |
| [glycolysis-i-from-glucose-6-phosphate.yaml](../../data/pathways/glycolysis-i-from-glucose-6-phosphate.yaml) | 119/119 | 14 | 121 | complex composition reviewed |
| [guanosine-ribonucleotides-de-novo-biosynthesis.yaml](../../data/pathways/guanosine-ribonucleotides-de-novo-biosynthesis.yaml) | 53/53 | 6 | 53 | all native facts represented |
| [heme-biosynthesis-i-aerobic.yaml](../../data/pathways/heme-biosynthesis-i-aerobic.yaml) | 45/45 | 4 | 30 | all native facts represented |
| [hexaprenyl-diphosphate-biosynthesis.yaml](../../data/pathways/hexaprenyl-diphosphate-biosynthesis.yaml) | 39/39 | 5 | 39 | all native facts represented |
| [homocysteine-and-cysteine-interconversion.yaml](../../data/pathways/homocysteine-and-cysteine-interconversion.yaml) | 30/30 | 4 | 30 | all native facts represented |
| [inositol-phosphate-biosynthesis.yaml](../../data/pathways/inositol-phosphate-biosynthesis.yaml) | 105/105 | 14 | 105 | native activity restored; unassigned/spontaneous activity retained |
| [l-arginine-biosynthesis-ii-acetyl-cycle.yaml](../../data/pathways/l-arginine-biosynthesis-ii-acetyl-cycle.yaml) | 85/85 | 10 | 86 | complex composition reviewed |
| [l-asparagine-biosynthesis-i.yaml](../../data/pathways/l-asparagine-biosynthesis-i.yaml) | 42/42 | 4 | 42 | all native facts represented |
| [l-asparagine-degradation.yaml](../../data/pathways/l-asparagine-degradation.yaml) | 49/49 | 7 | 49 | all native facts represented |
| [l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml](../../data/pathways/l-cysteine-biosynthesis-iii-from-l-homocysteine.yaml) | 16/16 | 2 | 16 | all native facts represented |
| [l-homocysteine-biosynthesis.yaml](../../data/pathways/l-homocysteine-biosynthesis.yaml) | 16/16 | 2 | 16 | all native facts represented |
| [l-lysine-biosynthesis-iv.yaml](../../data/pathways/l-lysine-biosynthesis-iv.yaml) | 74/74 | 9 | 74 | all native facts represented |
| [l-proline-degradation.yaml](../../data/pathways/l-proline-degradation.yaml) | 24/24 | 3 | 24 | unassigned/spontaneous activity retained |
| [l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde.yaml](../../data/pathways/l-tryptophan-degradation-to-2-amino-3-carboxymuconate-semialdehyde.yaml) | 47/47 | 6 | 47 | all native facts represented |
| [l-tyrosine-degradation-iii.yaml](../../data/pathways/l-tyrosine-degradation-iii.yaml) | 96/96 | 10 | 96 | all native facts represented |
| [leucine-degradation.yaml](../../data/pathways/leucine-degradation.yaml) | 62/62 | 9 | 62 | all native facts represented |
| [lipid-iva-biosynthesis.yaml](../../data/pathways/lipid-iva-biosynthesis.yaml) | 30/30 | 6 | 30 | all native facts represented |
| [mannose-degradation.yaml](../../data/pathways/mannose-degradation.yaml) | 29/29 | 4 | 29 | all native facts represented |
| [methionine-salvage-pathway.yaml](../../data/pathways/methionine-salvage-pathway.yaml) | 62/62 | 9 | 62 | all native facts represented |
| [methylglyoxal-catabolism.yaml](../../data/pathways/methylglyoxal-catabolism.yaml) | 22/22 | 3 | 22 | all native facts represented |
| [mevalonate-pathway.yaml](../../data/pathways/mevalonate-pathway.yaml) | 54/54 | 7 | 54 | all native facts represented |
| [myo-inositol-biosynthesis.yaml](../../data/pathways/myo-inositol-biosynthesis.yaml) | 19/19 | 3 | 19 | all native facts represented |
| [nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde.yaml](../../data/pathways/nad-biosynthesis-from-2-amino-3-carboxymuconate-semialdehyde.yaml) | 42/42 | 5 | 42 | unassigned/spontaneous activity retained |
| [nad-salvage-pathway-iv-from-nicotinamide-riboside.yaml](../../data/pathways/nad-salvage-pathway-iv-from-nicotinamide-riboside.yaml) | 24/24 | 3 | 24 | all native facts represented |
| [oleate-biosynthesis.yaml](../../data/pathways/oleate-biosynthesis.yaml) | 18/18 | 2 | 18 | all native facts represented |
| [palmitoleate-biosynthesis.yaml](../../data/pathways/palmitoleate-biosynthesis.yaml) | 19/19 | 2 | 19 | all native facts represented |
| [periplasmic-nad-degradation.yaml](../../data/pathways/periplasmic-nad-degradation.yaml) | 15/15 | 2 | 15 | all native facts represented |
| [phenylalanine-biosynthesis.yaml](../../data/pathways/phenylalanine-biosynthesis.yaml) | 27/27 | 4 | 27 | all native facts represented |
| [phosphatidate-biosynthesis-i-the-dihydroxyacetone-pathway.yaml](../../data/pathways/phosphatidate-biosynthesis-i-the-dihydroxyacetone-pathway.yaml) | 29/29 | 4 | 29 | all native facts represented |
| [phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway.yaml](../../data/pathways/phosphatidate-biosynthesis-ii-the-glycerol-3-phosphate-pathway.yaml) | 37/37 | 5 | 37 | all native facts represented |
| [phosphatidylcholine-biosynthesis-i.yaml](../../data/pathways/phosphatidylcholine-biosynthesis-i.yaml) | 24/24 | 3 | 24 | all native facts represented |
| [phosphatidylethanolamine-biosynthesis-i.yaml](../../data/pathways/phosphatidylethanolamine-biosynthesis-i.yaml) | 22/22 | 3 | 22 | all native facts represented |
| [phosphatidylinositol-phosphate-biosynthesis.yaml](../../data/pathways/phosphatidylinositol-phosphate-biosynthesis.yaml) | 222/222 | 21 | 222 | all native facts represented |
| [phospholipid-biosynthesis-ii-kennedy-pathway.yaml](../../data/pathways/phospholipid-biosynthesis-ii-kennedy-pathway.yaml) | 24/24 | 3 | 24 | all native facts represented |
| [phospholipid-biosynthesis.yaml](../../data/pathways/phospholipid-biosynthesis.yaml) | 74/74 | 9 | 74 | all native facts represented |
| [pyruvate-decarboxylation-to-acetyl-coa.yaml](../../data/pathways/pyruvate-decarboxylation-to-acetyl-coa.yaml) | 31/31 | 4 | 31 | all native facts represented |
| [pyruvate-fermentation-to-acetoin-iii.yaml](../../data/pathways/pyruvate-fermentation-to-acetoin-iii.yaml) | 69/69 | 9 | 69 | all native facts represented |
| [s-adenosyl-l-methionine-cycle-ii.yaml](../../data/pathways/s-adenosyl-l-methionine-cycle-ii.yaml) | 39/39 | 5 | 39 | native activity restored; unassigned/spontaneous activity retained |
| [salvage-pathways-of-pyrimidine-ribonucleotides.yaml](../../data/pathways/salvage-pathways-of-pyrimidine-ribonucleotides.yaml) | 67/67 | 9 | 67 | all native facts represented |
| [siroheme-biosynthesis.yaml](../../data/pathways/siroheme-biosynthesis.yaml) | 25/25 | 3 | 25 | all native facts represented |
| [spermidine-biosynthesis-i.yaml](../../data/pathways/spermidine-biosynthesis-i.yaml) | 16/16 | 2 | 16 | all native facts represented |
| [spermine-biosynthesis.yaml](../../data/pathways/spermine-biosynthesis.yaml) | 15/15 | 2 | 15 | all native facts represented |
| [sphingolipid-biosynthesis-yeast.yaml](../../data/pathways/sphingolipid-biosynthesis-yeast.yaml) | 188/188 | 20 | 194 | complex composition reviewed |
| [sulfate-activation-for-sulfonation.yaml](../../data/pathways/sulfate-activation-for-sulfonation.yaml) | 17/17 | 2 | 17 | all native facts represented |
| [superoxide-radicals-degradation.yaml](../../data/pathways/superoxide-radicals-degradation.yaml) | 26/26 | 4 | 26 | all native facts represented |
| [tetrahydrofolate-biosynthesis.yaml](../../data/pathways/tetrahydrofolate-biosynthesis.yaml) | 27/27 | 3 | 27 | all native facts represented |
| [tetrapyrrole-biosynthesis.yaml](../../data/pathways/tetrapyrrole-biosynthesis.yaml) | 29/29 | 4 | 29 | all native facts represented |
| [thiamine-biosynthesis.yaml](../../data/pathways/thiamine-biosynthesis.yaml) | 87/87 | 10 | 87 | all native facts represented |
| [threonine-degradation.yaml](../../data/pathways/threonine-degradation.yaml) | 16/81 | 3 | 22 | 10 outline activities excluded; GLY1 independently added |
| [trans-trans-farnesyl-diphosphate-biosynthesis.yaml](../../data/pathways/trans-trans-farnesyl-diphosphate-biosynthesis.yaml) | 21/21 | 3 | 21 | all native facts represented |
| [tryptophan-degradation.yaml](../../data/pathways/tryptophan-degradation.yaml) | 90/90 | 12 | 90 | all native facts represented |
| [tyrosine-biosynthesis.yaml](../../data/pathways/tyrosine-biosynthesis.yaml) | 27/27 | 4 | 27 | all native facts represented |
| [udp-n-acetylglucosamine-biosynthesis.yaml](../../data/pathways/udp-n-acetylglucosamine-biosynthesis.yaml) | 31/31 | 4 | 31 | all native facts represented |
| [urea-degradation-i.yaml](../../data/pathways/urea-degradation-i.yaml) | 25/25 | 2 | 20 | all native facts represented |
| [utp-and-ctp-de-novo-biosynthesis.yaml](../../data/pathways/utp-and-ctp-de-novo-biosynthesis.yaml) | 38/38 | 4 | 38 | all native facts represented |
| [valine-degradation.yaml](../../data/pathways/valine-degradation.yaml) | 98/98 | 11 | 98 | all native facts represented |
| [very-long-chain-fatty-acid-biosynthesis.yaml](../../data/pathways/very-long-chain-fatty-acid-biosynthesis.yaml) | 39/39 | 5 | 39 | all native facts represented |
| [xylose-metabolism.yaml](../../data/pathways/xylose-metabolism.yaml) | 16/16 | 2 | 16 | all native facts represented |
| [zymosterol-biosynthesis.yaml](../../data/pathways/zymosterol-biosynthesis.yaml) | 106/106 | 12 | 106 | all native facts represented |

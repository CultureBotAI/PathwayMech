# Bounded GO-CAM catalytic-function review

All 40 flagged source entries were read against the actual input/output edges. Exact source pointers, SHA256 digests and per-accession dispositions are in `gocam-function-dispositions.json`; removed and replacement facts are in `gocam-function-review.json`. These files supersede affected native-import assertions without erasing their provenance.

The corrections distinguish physiological pathway roles from in-vitro capacity, protein-bound residues from free metabolites, and explicit source uncertainty from established chemistry. ADH4/ADH5 higher-alcohol branches remain supported by [the primary isozyme-mutant study](https://pubmed.ncbi.nlm.nih.gov/12499363/), despite exclusion of their unsupported ethanol-oxidation branches. The inspected abstract does not directly test tyrosine-to-tyrosol; that native context remains qualified in the final chemical disposition ledger. ARO9 was a false alarm: its actual represented co-substrates comply with its specificity.

THI4 was additionally checked after the complete Rhea audit raised its downstream hydrolysis assignment: reviewed THI4 makes ADP-thiazole by sacrificing its own cysteine residue. The separate ADP-thiazole-to-thiazole-phosphate bridge remains a source-model reaction with unresolved physiological enzyme; THI4 is no longer asserted as its catalyst.

| Accession | Disposition | Reason |
|---|---|---|
| P06106 | retain | The native MET17 branch uses O-acetylhomoserine, not the disputed O-acetylserine route to cysteine. |
| P10127 | correct_scope | Exclude the physiological ethanol-oxidation branch. Retain native higher-alcohol contexts with bounded evidence: PMID12499363 supports isozyme redundancy for the tested higher alcohols, but its inspected abstract does not directly establish tyrosine-to-tyrosol. The final chemical disposition ledger preserves that specificity limitation; dominant wild-type flux is not inferred. |
| P10614 | retain | Lanosterol demethylation matches the reviewed endogenous sterol reaction; no non-intrinsic substrate is introduced. |
| P15700 | qualify | UMP phosphorylation is established; CMP phosphorylation in pyrimidine salvage is retained with an explicit disputed-substrate qualifier and the opposing source literature identifiers. |
| P22140 | retain | The represented EPT1 reaction is CDP-ethanolamine to phosphatidylethanolamine, not the weak phosphatidylcholine route. |
| P25340 | retain | The current graph has sterol reductase chemistry; the historical transport-protein misassignment is not represented. |
| P26364 | correct_chemistry | Replace ATP input with GTP and add GDP output for the ADK2 native instance; update its activity label. Retain ADK1 ATP chemistry separately. |
| P29465 | retain | Membrane-terminal topology caution does not contradict chitin synthase chemistry. Topology is not asserted by these catalytic edges. |
| P30624 | retain | The graph represents ATP-dependent fatty-acid activation, not the separate ATP-independent sphingoid-base uptake process. |
| P31373 | correct_scope | Preserve cystathionine cleavage in the two cysteine-route records. Remove the unrelated reverse condensation branch from threonine degradation; exact physiological direction is RHEA14006. |
| P32368 | retain | Alternative initiation-site caution does not contradict represented phosphoinositide phosphatase reactions. |
| P32784 | retain | Both native glycerol-3-phosphate and dihydroxyacetone-phosphate acylations are supported. Substrate preference is not an absolute specificity exclusion. |
| P36148 | retain | Both native glycerol-3-phosphate and dihydroxyacetone-phosphate acylations are explicitly supported. |
| P38298 | retain | Phytoceramide hydrolysis is a supported substrate class; the excluded unsaturated-ceramide substrate is not explicitly asserted. |
| P38840 | retain_false_alarm | Five actual ARO9 activities use pyruvate/alanine, phenylpyruvate/phenylalanine, or a generic proteinogenic amino donor. No glutamate/2-oxoglutarate pair is asserted for this protein; do not remove correct ARO9 branches based on the generic EC name. |
| P38891 | retain | Contradictory growth phenotypes concern cell-cycle consequences, not the represented amino-acid transaminations. |
| P38994 | retain | PtdIns4P to PtdIns(4,5)P2 phosphorylation agrees with the reviewed function; no PKC1 dependency is asserted. |
| P38998 | retain_catalysis_location_reviewed | Retracted peroxisomal localization affects compartment evidence, handled by the separate location audit; saccharopine cleavage remains supported. |
| P39006 | retain_catalysis_location_reviewed | ER localization is disputed and handled separately; phosphatidylserine decarboxylation remains supported. |
| P39518 | retain | Fatty-acid activation is supported; the source preference for medium-chain substrates does not exclude tolerated long-chain substrates. Compartment review identifies the peroxisomal context. |
| P40106 | retain | Non-stereospecific glycerol-phosphate hydrolysis supports the native glycerol-1-phosphate route. |
| P40559 | retain | Actual substrate is PtdIns(4,5)P2, not the explicitly excluded PtdIns(3,5)P2, PtdIns3P or PtdIns4P. |
| P41277 | retain | Non-stereospecific glycerol-phosphate hydrolysis supports the native glycerol-1-phosphate route. |
| P41911 | retain | Alternative initiation-site caution does not affect NADH-dependent glycerol-3-phosphate formation. |
| P47912 | retain | The graph represents ATP-dependent fatty-acid activation, not the separate ATP-independent sphingoid-base uptake process. |
| Q00055 | retain | Current graph is NADH-dependent glycerol-3-phosphate formation; historical FAD-dependent GUT2 misidentification is not propagated. |
| Q01574 | retain | Alternative initiation-site caution does not affect acetate-CoA ligation. |
| Q02896 | retain | The native saturated phytoceramide class is among the reported hydrolyzed substrates. The stronger dihydroceramide preference is not an absolute exclusion; no unsaturated-ceramide breakdown is asserted. |
| Q03677 | qualify_cofactor_branch | The displayed methionine-salvage chemistry matches Fe-ARD. The cofactor review explicitly distinguishes the inferred nickel-bound off-route product branch; nickel is not presented as a required cofactor for the shown salvage reaction. |
| Q05584 | retain | Caution distinguishes historical degraded preparations and supports current GLO2/GLO4 identity; no third glyoxalase-II protein is inferred. |
| Q06685 | qualified_by_later_primary_review | The two original VIP1 activities are ATP-dependent kinases and are not contradicted by the old phosphatase-negative caution. The later primary review in folate-inositol-chemistry-review.json supersedes that caution for the experimentally tested recombinant S. cerevisiae Vip1 pyrophosphatase domain (PMID:32303658, Fig.3A and Table2), adding qualified 1-IP7 hydrolysis. It does not infer a yeast in-vivo phenotype or untested IP8 hydrolysis. |
| Q07560 | correct_chemistry | Although its CAUTION only concerns historical taxon attribution, the full FUNCTION/catalytic record exposes bacterial glycerol-forming chemistry in the native graph. Replace it with yeast CDP-DAG+PG to cardiolipin+CMP+H+. |
| Q12320 | retain | Caution distinguishes historical degraded preparations and supports current GLO2/GLO4 identity; no third glyoxalase-II protein is inferred. |
| Q99321 | retain | Native reactions hydrolyze diphosphoinositol phosphate groups, a separately supported activity. Excluded nucleotide substrates are not represented; precise positional chemistry is in the independent Rhea audit. |
| P32459 | retain | Native products are glyoxylate and urea, consistent with the lyase and distinct from the ammonia-producing hydrolase cautioned against. |
| P38113 | correct_scope | Exclude the physiological ethanol-oxidation branch. Retain native higher-alcohol contexts with bounded evidence: PMID12499363 supports isozyme redundancy for the tested higher alcohols, but its inspected abstract does not directly establish tyrosine-to-tyrosol. The final chemical disposition ledger preserves that specificity limitation; dominant wild-type flux is not inferred. |
| P53128 | retain | Current methylenetetrahydrofolate reductase chemistry does not propagate the historical mitochondrial-ribosomal-protein classification. |
| Q08227 | retain | Actual substrate is PtdIns(4,5)P2, not the explicitly excluded PtdIns(3,5)P2, PtdIns3P or PtdIns4P. |
| P06174 | retain | Uroporphyrinogen-III formation does not propagate the historical mitochondrial-import role. |
| Q07748 | correct_chemistry | Represent phosphorylated HMP product and protein-bound histidine/PLP-lysine chemistry, including modified residues and redox species. Preserve inference by similarity to THI5 and single-turnover scope; route product directly to HMP-phosphate kinase. |

Reproduce after native and compartment curation (dry run unless `--apply` is supplied):

```bash
PYTHONPATH=src .venv/bin/python scripts/review_gocam_functions.py \
  --source-dir /external/cache/function-review \
  --chebi-db /external/cache/chebi.db \
  --records data/pathways \
  --report reports/causal_graph_review/gocam-function-review.json
```

Obtain the exact UniProt accession JSON endpoints and `.provenance.json` files listed in the source projection. The script pins the reviewed byte hashes and refuses changed representations. ChEBI labels come from the independent release-255 authority database. All record candidates validate before publication; the default writes only the report.

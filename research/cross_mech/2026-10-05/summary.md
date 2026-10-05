# Cross-Mech protein inventory

| Mech | Protein slot values | Distinct accessions | In a PathwayMech pathway | Record-pathway pairs | Unlinked pairs | PathwayMech links | Broken links |
|---|---:|---:|---:|---:|---:|---:|---:|
| AntibioticMech | 278 | 88 | 0 | 0 | 0 | 0 | 0 |
| CellStructureMech | 413 | 329 | 0 | 0 | 0 | 0 | 0 |
| NaturalProductMech | 1093 | 445 | 1 | 1 | 1 | 0 | 0 |
| ProteinTraitsMech | 10056 | 3256 | 351 | 2468 | 2468 | 0 | 0 |
| TraitMech | 143 | 112 | 0 | 0 | 0 | 0 | 0 |

## Unlinked record-pathway pairs

A sibling record holds a protein of a PathwayMech pathway but does not link that pathway. Whether it should depends on what the record is: a pathway or activity trait usually should, a domain or family trait usually should not. At most 25 pairs per Mech are listed; `pairs.tsv` has all of them.

- NaturalProductMech `naturalproductmech:mibig-01731d46ec` (feglymycin) -> `WikiPathways:WP5060` via P0A749
- ProteinTraitsMech `EC:1.1.1.101` (acylglycerone-phosphate reductase) -> `gomodel:YeastPathways_PWY3O-6407` via P40471
- ProteinTraitsMech `EC:1.1.1.170` (3beta-hydroxysteroid-4alpha-carboxylate 3-dehydrogenase (decarboxylating)) -> `gomodel:YeastPathways_PWY-6074-1` via P53199
- ProteinTraitsMech `EC:1.1.1.430` (D-xylose reductase (NADH)) -> `gomodel:YeastPathways_PWY3O-8` via P38715
- ProteinTraitsMech `EC:1.1.1.431` (D-xylose reductase (NADPH)) -> `gomodel:YeastPathways_PWY3O-8` via P38715
- ProteinTraitsMech `EC:1.1.1.54` (allyl-alcohol dehydrogenase) -> `gomodel:YeastPathways_PWY3O-214` via P00330
- ProteinTraitsMech `EC:1.1.1.54` (allyl-alcohol dehydrogenase) -> `gomodel:YeastPathways_PWY3O-4105` via P00330
- ProteinTraitsMech `EC:1.1.1.54` (allyl-alcohol dehydrogenase) -> `gomodel:YeastPathways_PWY3O-4108` via P00330
- ProteinTraitsMech `EC:1.1.1.54` (allyl-alcohol dehydrogenase) -> `gomodel:YeastPathways_PWY3O-4112` via P00330
- ProteinTraitsMech `EC:1.1.1.54` (allyl-alcohol dehydrogenase) -> `gomodel:YeastPathways_PWY3O-4300` via P00330
- ProteinTraitsMech `EC:1.1.1.78` (methylglyoxal reductase (NADH)) -> `gomodel:YeastPathways_PWY3O-214` via P00330
- ProteinTraitsMech `EC:1.1.1.78` (methylglyoxal reductase (NADH)) -> `gomodel:YeastPathways_PWY3O-4105` via P00330
- ProteinTraitsMech `EC:1.1.1.78` (methylglyoxal reductase (NADH)) -> `gomodel:YeastPathways_PWY3O-4108` via P00330
- ProteinTraitsMech `EC:1.1.1.78` (methylglyoxal reductase (NADH)) -> `gomodel:YeastPathways_PWY3O-4112` via P00330
- ProteinTraitsMech `EC:1.1.1.78` (methylglyoxal reductase (NADH)) -> `gomodel:YeastPathways_PWY3O-4300` via P00330
- ProteinTraitsMech `EC:1.1.1.87` (homoisocitrate dehydrogenase) -> `gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2` via P40495
- ProteinTraitsMech `EC:1.14.18.6` (4-hydroxysphinganine ceramide fatty acyl 2-hydroxylase) -> `gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1` via Q03529
- ProteinTraitsMech `EC:1.14.18.7` (dihydroceramide fatty acyl 2-hydroxylase) -> `gomodel:YeastPathways_SPHINGOLIPID-SYN-PWY-1` via Q03529
- ProteinTraitsMech `EC:1.14.18.-` (With another compound as one donor, and incorporation of one atom of oxygen) -> `gomodel:YeastPathways_PWY-6074-1` via P53045
- ProteinTraitsMech `EC:1.14.19.1` (stearoyl-CoA 9-desaturase) -> `gomodel:YeastPathways_PWY3O-1801` via P21147
- ProteinTraitsMech `EC:1.14.19.1` (stearoyl-CoA 9-desaturase) -> `gomodel:YeastPathways_PWY3O-5268` via P21147
- ProteinTraitsMech `EC:1.3.1.13` (prephenate dehydrogenase (NADP(+))) -> `gomodel:YeastPathways_PWY3O-4120` via P20049
- ProteinTraitsMech `EC:1.5.1.10` (saccharopine dehydrogenase (NADP(+), L-glutamate-forming)) -> `gomodel:YeastPathways_LYSINE-AMINOAD-PWY-2` via P38999
- ProteinTraitsMech `EC:1.5.1.15` (methylenetetrahydrofolate dehydrogenase (NAD(+))) -> `gomodel:YeastPathways_PWY3O-697` via Q02046
- ProteinTraitsMech `EC:1.5.1.20` (methylenetetrahydrofolate reductase [NAD(P)H]) -> `gomodel:YeastPathways_PWY3O-697` via P46151
- ProteinTraitsMech `EC:1.5.1.53` (methylenetetrahydrofolate reductase (NADPH)) -> `gomodel:YeastPathways_PWY3O-697` via P53128
- ProteinTraitsMech: 2443 more pairs not listed here

SGD participants without a UniProtKB mapping: SGD:S000217821, SGD:S000217863, SGD:S000217933, SGD:S000217934, SGD:S000218025, SGD:S000218096, SGD:S000218158, SGD:S000218211.

Every row is a curation lead. A shared accession shows pathway participation, not that the sibling record's claim concerns that pathway.

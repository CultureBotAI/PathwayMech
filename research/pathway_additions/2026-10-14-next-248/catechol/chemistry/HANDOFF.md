# Next248 exact chemical and reaction authority closure

All four reactions in **MetaCyc:CATECHOL-ORTHO-CLEAVAGE-PWY** close with exact native chemical identities and complete Rhea142 stoichiometry. The selected module ends at 3-oxoadipate; downstream CoA transfer and thiolysis remain outside this boundary. This assessment does not establish a catalyst, strain, experimental sample identity, or primary-paper claim.

| Order | Recommended reaction | Rhea/native equation orientation | Complete pathway-flow equation |
|---|---|---|---|
| 1 | RHEA:23853 | left_to_right | CHEBI:18135 + CHEBI:15379 → CHEBI:32379 + 2 CHEBI:15378 |
| 2 | RHEA:30033 | right_to_left | CHEBI:32379 + CHEBI:15378 → CHEBI:58736 |
| 3 | RHEA:12349 | left_to_right | CHEBI:58736 → CHEBI:58425 |
| 4 | RHEA:10185 | left_to_right | CHEBI:58425 + CHEBI:15377 → CHEBI:15775 + CHEBI:15378 |

The second reaction is formally right-to-left relative to its native/Rhea master written sides. The table's displayed pathway-flow equation follows its actual substrate/product traversal. Rhea30032 is the opposite directional event and must not replace 30033 merely to make all direction fields alike. In Rhea RDF, coefficients are encoded by the side predicates `rh:contains1` and, for the first reaction's two hydrons, `rh:contains2`; they are not properties invented on the reaction participant.

The eight native27.0 compound complete InChIs, formal charges and elemental formulas match pinned ChEBI255 exactly. Full native CML element/bond connectivity also matches, with stereochemistry deliberately excluded from that graph-only comparison. Current issuing ChEBI JSON independently confirms each full InChI, charge and formula; its SMILES interprets to the same complete InChI. Native CPD-15124 is the specified S muconolactone monoanion CHEBI:58736, with a five-membered lactone ring. Both its native SMILES and full InChI independently agree with the ChEBI structure. The next reaction moves the ring double bond and removes the stereogenic center; its product is the same five-membered enol lactone CHEBI:58425 used by the hydrolase. Every step is element- and charge-balanced, and all three intermediate joins use the identical full structure.

## Representation limits retained

- Native CIS-CIS-MUCONATE and 3-KETO-ADIPATE XML contain a generic `C([R])(=O)[O-]` SMILES field. That field is not a usable complete structure. The native complete InChI, CML graph, formula/charge, and issuing ChEBI structures support the exact identities.
- Pinned ChEBI255 CHEBI:32379 SMILES omits the stereochemical bond assignments. Its complete InChI specifies cis,cis, and current issuing ChEBI SMILES also specifies both Z bonds. Do not claim all source SMILES fields agree, or use the deficient pinned SMILES alone as stereochemical proof.
- Native CML atom/bond data was checked for connectivity and charge, not treated as an independent absolute stereochemical assignment from coordinates. The explicit native InChI and specified SMILES provide that assignment for CPD-15124.

## KEGG discrepancy resolved within scope

Whole issuing [R03959](https://rest.kegg.jp/get/R03959), [R06989](https://rest.kegg.jp/get/R06989), and C04105/C14610/C02480 flatfiles and MOL originals were retained. RDKit2025.03.6 interpretation shows:

- R03959 uses neutral stereounspecified muconolactone C04105. It is broader than the native CPD-15124 reaction, despite native27.0's unification cross-reference.
- R06989 uses neutral S-muconolactone C14610 and is explicitly a member of M00568. Its S-specific route is consistent with the retained DRAM lead. Its structures remain neutral, so it is not protonation- or charge-identical to the native/Rhea anionic equation.
- Controlled computational deprotonation of the issuing C14610 and C02480 structures gives the exact complete InChIs of native CPD-15124/CHEBI:58736 and cis,cis-muconate/CHEBI:32379, respectively. This is a comparison calculation, not a claim that the issuing KEGG structures themselves are charged or that an experimental sample was identified.

## Deliverables and provenance

`author-handoff.json` contains the recommended identifiers, complete native and RDF sides, exact source locators, source URLs/hashes, full chemical identity fields, baseline snapshot availability, and caveats. `chemical-identity-closure.json` additionally retains parsed molecule interpretations, issuing ChEBI objects' relevant fields, and KEGG MOL comparisons. `rhea-original-projection.json` retains all selected Rhea142 reaction/direction/side/participant/compound nodes. Acquisition manifests bind the unmodified originals under `originals/`; the failed sandbox acquisition is explicitly separate and is not evidence of source absence.

Pinned Rhea139 SQL labels agree exactly with the selected Rhea142 equations. The full retained Rhea142 gzip and directions file were freshly hashed. Existing ChEBI255/Rhea139 semantic SQL digest metadata was inspected; these multi-GB databases were opened read-only and not freshly rehashed in this bounded task. The issuing ChEBI fetches are a separate dated verification, not a claimed upgrade of pinned authorities.

At baseline main `22f4279d66ab39cf153a9a1f7333150671d1b17b`, the complete parsed ontology/source authority snapshots lack ten required core terms: the pathway, all four selected Rhea reactions, and CHEBI:18135, CHEBI:32379, CHEBI:58736, CHEBI:58425 and CHEBI:15775. O2, hydron and water are already present. This is a statement about those exact snapshot files, not a global absence claim. All selected chemical/reaction identifiers exist in the issuing/pinned originals audited here. Source agent owns protein/taxon identity and any authority build.

No maintained records, canonical snapshots or GitHub objects were changed. External temporary paths are session evidence storage, not durable archives. Whole native reaction originals and complete chemical identity fields were inspected; unrelated common-compound reaction listings were not used as mechanistic evidence. Primary-paper appraisal remains with the primary-evidence agent.

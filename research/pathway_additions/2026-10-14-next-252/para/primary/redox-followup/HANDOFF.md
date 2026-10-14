# Successor author payload for issue #531

The proposed payload adds four edges: hydrogen peroxide and potassium ferricyanide inhibit the historical native protocatechuate 2,3-dioxygenase preparation; ascorbate restores activity in two distinct oxidant-treated molecular states. Both recovery edges qualify the **object** as inactive enzyme. Neither claims activation of untreated enzyme, physiological regulation, a damaged residue, a dose, iron-state occupancy, or identity of the historical purified material with the complete 2009 sequence.

`proposed-redox-payload.json` contains the three participant rows, new primary reference, four edges, two object qualifiers, and explicit quotation accounting. All repeated primary quotations, including qualifier evidence, total **22 words** from PMID:8392511. Every quoted string was checked against the exact retrieved PubMed XML. Native MetaCyc evidence supports the historical-preparation mapping only; it is not presented as encoding the redox states.

The same primary abstract sentence identifies H2O2 and K3FE(CN)6 as oxidizing agents that inactivate the enzyme, followed by full activity restoration through ascorbate reduction. This supports the qualitative recovery association with both named treatments. It does not provide independently resolved treatment-specific dose, time course, recovery protocol or metal-state occupancy, and the proposed qualifiers explicitly preserve that limitation.

| Selected identity | Reason |
|---|---|
| CHEBI:16240, hydrogen peroxide | Exact neutral H2O2 reagent. |
| CHEBI:30060, potassium hexacyanoferrate(3-) | Exact potassium salt named in the abstract. Three K+ counterions and a ferricyanide complex give neutral overall composition. |
| CHEBI:22651, ascorbate; category chemical_entity | The abstract does not specify stereochemistry. This issuing class deliberately retains that breadth. |

CHEBI:5020 is the ferricyanide anion, not the stated neutral potassium salt; it was inspected but not substituted. CHEBI:38290 is L-ascorbate, a narrower child of the generic ascorbate class; its exact stereo-resolved structure was inspected but not claimed for this experiment. Generic ascorbate has no single structure in either the current issuing record or pinned ChEBI255. No structure, salt or enantiomer has been invented to fill that source limitation.

`chemical-identity-projection.json` binds the current ChEBI responses to pinned ChEBI255 rows. `structure-checks.json` independently parses the four exact compounds with RDKit2025.03.6 and verifies graph equivalence, full InChI/InChIKey, element counts and total charge. Potassium ferricyanide additionally passes the three-potassium-counterion check. The central iron's negative formal charge in ChEBI's connected SMILES is an encoding of the complex charge, not a claim of a negative iron oxidation state. All applicable checks passed.

The reference is bound to `originals/PMID8392511-pubmed.xml`, SHA256 `cf039adc4ce83fd8aef5b6d651c9a5b88ae695140c4d8e956389b76cecfa0bd1`. The entire abstract was inspected; the full article's redox protocols were not retrieved. Metadata identifies DOI:10.1128/jb.175.14.4414-4426.1993. Raw downloads and exact URLs/digests remain in this external directory.

This is author remediation support, not an independent scientific review. No maintained repository files or earlier handoff/ledger files were modified. The earlier omission remains traceable; this successor is linked to https://github.com/CultureBotAI/PathwayMech/issues/531.

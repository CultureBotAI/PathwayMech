# Next260 formal chemistry author handoff

Exact candidate: **MetaCyc:GALLATE-DEGRADATION-I-PWY**, displayed **gallate degradation II**. This is external root-author research. It changes no maintained record, authority, Git state or GitHub object and is not independent scientific approval.

All five complete native reaction objects and eleven complete native compound objects (ten formal compounds plus the distinct Z,Z comparator) were inspected computationally. Full native CML connectivity, bond orders, charge and 2D double-bond geometry agree with complete native InChI/InChIKey, issuing ChEBI structures and the pinned ChEBI 255 full identity fields. The full 4,137,340,928-byte pinned Semantic SQL database was hashed before read-only queries. Exact source hashes and calculated representations are retained. This is formal chemistry closure, not a complete survey of enzyme-specific substrates, cofactors or assay reagents.

| Native member | Selected identifier | Selected formal equation | Native direction |
|---|---|---|---|
| RXN-11861 | MetaCyc:RXN-11861 | Gallate + O2 → PDC + H2O + H+ | Physiological L2R |
| RXN-2462 | RHEA:10645 | PDC + H2O → keto OMA + H+ | Physiological L2R |
| RXN-9983 | RHEA:28932 | Keto OMA → E,E enol CHM | Reversible; spontaneous; selected L2R |
| RXN-2463 | RHEA:17403 | E,E enol CHM + H2O → CHA | Reversible; selected R2L relative to native sides |
| RXN-2464 | RHEA:28936 | CHA → pyruvate + oxaloacetate | Reversible; selected L2R |

All native pathway members and layout directions were replayed. The four exact Rhea directional equations were traversed through their complete side, participant, coefficient and compound nodes from the full original RDF, including repeated subject fragments. The entry reaction keeps its exact native identifier. The complete decompressed Rhea original contains neither the exact R03549 nor RXN-11861 cross-reference; that bounded result does not prove absence of every chemically equivalent reaction under other annotations.

The calculated overall equation is **gallate(−1) + O2 + H2O → pyruvate(−1) + oxaloacetate(−2) + 2 H+**. Both sides have C7 H7 O8 and charge −1. The entry-produced water cancels the PDC hydrolysis water in the summed first two steps. This sum is a calculation, not an additional elementary reaction, evidence of flux, or a reason to merge the distinct five-member route with the four-member gallate I route. `material-facts.json` contains all 17 native input/output facts, coefficients and exact XML locators with structured statements of at most 400 characters; no paper quotation is allocated here.

The PDC identity is **CHEBI:58304**, C7H2O6, charge −2, full key `VRMXCPVFSJVVCA-UHFFFAOYSA-L`. The other formal identities are CHEBI:16918 (gallate), 57471 (keto OMA), 58142 (E,E enol CHM), 58075 (CHA with unspecified absolute configuration), 15361 (pyruvate), 16452 (oxaloacetate), 15377 (water), 15379 (dioxygen) and 15378 (proton). The distinct Z,Z comparator is CHEBI:57732.

Fresh ordinary public retrieval obtained the exact ChEBI:58304 JSON, KEGG:R03549 reaction, and complete records plus MOL structures for KEGG:C01424 and C03671. KEGG's compound structures are neutral acids, C7H6O5 and C7H4O6; its reaction uses a reversible arrow and omits an explicit proton. Their complete molecular graphs match the selected ChEBI ions only after explicitly adding one and two carboxyl protons for comparison. Native RXN-11861 uses gallate monoanion and PDC dianion, so its explicit H+ is required for balance. Keep these source conventions distinct; the KEGG cross-reference does not establish exact charge-normalized directional equivalence. Selected forward graph edges do not imply physical irreversibility. Primary evidence for reversible PDC hydrolase catalysis remains a separate preparation-scoped observation.

Three source limitations remain explicit:

- The native pathway narrative's CPD-185 is Z,Z, while its formal RXN-9983/RXN-2463 sides use CPD-12849, E,E. Their full stereochemical keys differ. ChEBI:58142's historical cis,cis label does not override its E,E structure. Pinned SMILES for keto OMA and both enol comparators omit some stereo; all complete pinned InChI/key fields, source CML geometry and issuing structures agree. No authority file was altered to hide that limitation.
- CHEBI:58075 has an unassigned stereocenter. It does not mean a racemic experimental product. The earlier inspected primary packages distinguish the negative CHA enantiomer from an unresolved absolute assignment; no S configuration is transferred from a different LigJ preparation. The primary authors' historical uncharacterized open-chain intermediates do not independently establish every modern E,E mapping.
- This handoff covers formal pathway material chemistry only. Native source closure and primary-source preparation/assay interpretation remain owned by the separate next260-native and next260-primary packages. Salt constituents such as CUSO4/SULFATE, metal-treatment identities, other regulators, alternate substrates and enzyme-specific reaction boundaries require their own participant-selection assessment. No universal reagent or cofactor closure is claimed.

The first calculation helper incorrectly compared RDKit's charge-suffixed formula string with ChEBI's separate elemental-formula field. All full structure/key/charge and five reaction balances passed in that attempt; nine charged string comparisons failed. The entire failed helper, output and log remain preserved. Version 2 correctly compares complete atom counts and checks formal charge separately; all checks pass. RDKit's explicit warnings about proton normalization and unspecified stereo remain in the logs.

No new primary-paper visual reading is claimed by this chemistry subtask. The frozen next260-primary dossier owns the complete 1982 and 1975 readings and their exact preparation limitations. This package supplies source-native chemical structure and equation checks; a future record still needs a fresh post-merge duplicate check, native/primary claim reconciliation, participant authorities, complete record-to-source/source-to-record dispositions, and independent scientific review.

# Purine deoxyribonucleosides degradation

The new record is the complete six-reaction native pathway **PathBank:SMP0002089**, member **PW002077.owl**. Its record is `data/pathways/purine-deoxyribonucleosides-degradation.yaml`. The adjacent source definitions are not interchangeable: MetaCyc PWY0-1297 is a superpathway of PWY-7179 and PWY-7180 and includes an additional acetaldehyde-to-acetyl-CoA reaction. The PathBank definition ends at acetaldehyde and D-glyceraldehyde 3-phosphate. GO:0046124 denotes generic purine deoxyribonucleoside catabolism without that exact boundary. The native PathBank identity therefore best preserves this assignment; no exactMatch to the larger MetaCyc route is asserted.

Fresh hidden- and ignored-inclusive searches found the candidate in prior archive screening and taxonomy-audit ledgers, where it awaited scientific review and semantic deduplication. Those were leads, not rejections. No existing exact record was found in the accessible 174-record baseline. The existing pyrimidine deoxyribonucleoside route uses Cdd/DeoA and different substrates, despite a shared sugar-phosphate product. Purine biosynthesis, salvage and yeast ribonucleoside context are also distinct. A separate attempt to search the original Documents repository returned an OS access denial. The search ledger preserves this limit and does not claim absence throughout the computer.

## Exact mechanism and boundary

| Native reaction | Selected directed Rhea | Catalyst or functional role | Native direction |
|---|---|---|---|
| 6068 | 28191 | Add, P22333 | Right-to-left deamination of deoxyadenosine |
| 6069 | 27743 | DeoD homohexamer | Deoxyadenosine phosphorolysis |
| 6067 | 27751 | DeoD homohexamer | Reversible deoxyinosine phosphorolysis; degradation selected |
| 6070 | 27739 | DeoD homohexamer | Reversible deoxyguanosine phosphorolysis; degradation selected |
| 6071 | 27659 | DeoB, P0A6K6 | Deoxyribose 1-phosphate to 5-phosphate |
| 6072 | 12822 | DeoC, P0A6L0 | Sugar-phosphate cleavage to acetaldehyde and D-GAP |

All six native reactions, all four protein identities, the six-subunit DeoD assembly, and all 22 chemical side occurrences are retained. Every native side coefficient is one. Independent replay of the complete Rhea 142 RDF checks each directed family, side URI, `contains1` relation, participant-to-compound link and exact ChEBI species. All six reactions balance by atoms and charge against the complete ChEBI database. Five material-transfer edges link identical intermediates. The parallel DeoD branches are not chained according to arbitrary XML array order.

PathBank's phosphate(3-), uncharged deoxyribose phosphates and generic glyceraldehyde phosphate cross-references differ from the precise Rhea/UniProt species. The projection preserves both representations. Rhea selects hydrogenphosphate, alpha-D deoxyribose 1-phosphate(2-), D-ribofuranose 5-phosphate(2-) and D-glyceraldehyde 3-phosphate(2-). These are justified by the exact enzyme reaction annotations, rather than by an assertion that different charges or underspecified stereochemistry are identical. Native 6068 is explicitly reversed before comparison with the Rhea left-to-right deamination.

## Assemblies, cofactors and evidence grades

MetaCyc DEOD-CPLX independently specifies six DEOD-MONOMER copies; the monomer explicitly cross-references P0ABP8. PathBank complex 4056 also has six copies. The [1975 primary abstract](https://pubmed.ncbi.nlm.nih.gov/235429/) reports physical subunit characterization and association experiments suggesting that only hexamers are active. The [2018 primary full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6193948/fullTextXML) corroborates the trimer-of-dimers architecture and its catalytic significance. The three exact deoxyribonucleoside specificities are attributed to the inspected current UniProt comments and native reactions; the 2018 paper's ribonucleoside/analogue experiments are not relabeled as direct assays of every deoxy substrate. Only the complex catalyzes these branches; its subunit has a membership edge.

DeoB's monomeric form is supported by the [1975 physical-characterization abstract](https://pubmed.ncbi.nlm.nih.gov/1089430/), which reports single polypeptide chains for four purified forms. Current UniProt attributes Mn(2+) and Co(2+) activation, and less efficient Ni(2+) substitution, to PMID:4992818. The graph preserves these as alternative metal-supported activities. It does not claim simultaneous occupancy, establish the physiological metal, or turn the source's by-similarity two-Mn annotation into a measured stoichiometry.

Add's exact deoxyadenosine activity is annotated with experimental attribution in reviewed UniProt and the native ADDALT-ENZRXN purified-protein evidence slot. Its zinc assignment is separately **ECO:0000255 / HAMAP MF_00540**, not directly inspected E. coli metal-binding evidence. The native discussion of murine monomeric zinc-dependent ADA is not transferred as an E. coli experiment. Add is represented by a qualified functional `enables` edge.

DeoC also uses a qualified functional edge. The [K-12 primary abstract](https://pubmed.ncbi.nlm.nih.gov/6749498/) and current UniProt preserve both monomer and homodimer states; the native annotation distinguishes monomer in Tris/HCl with EDTA from dimer in phosphate buffer. The [1995 primary abstract](https://pubmed.ncbi.nlm.nih.gov/7675789/) states the exact reversible cleavage. No unregistered physical complex is invented, and crystal asymmetric-unit membership alone is not interpreted as physiological assembly. Hyperthermophilic DERA properties and tentative Salmonella residue inferences are excluded.

## Organism, location and context

PathBank uses E. coli taxon 562. All four fresh reviewed UniProt entries use K-12 taxon 83333; each selected native MetaCyc protein frame explicitly uses MG1655 taxon 511145. The record's MG1655 scope follows those component annotations. The older E. coli enzyme studies do not demonstrate complete pathway flux in MG1655. Each protein's cytosol edge uses an explicit current GO:0005829 cross-reference with IDA:EcoCyc attribution; the complex location follows its native CCO-CYTOSOL slot.

Root's independent iModulonDB context includes add/deoB in component k43 and deoC in k33. These expression-context memberships are not catalytic or whole-route flux evidence. The maintained shared `imodulondb-*` receipts preserve the queries, component contents, acquisition details and client availability limitation.

## Source completeness and exclusions

All native reaction and catalyst roles are accounted for in `purine-deoxy-source-projection.json`. Uptake, free-base salvage, purine-ring catabolism, acetaldehyde oxidation, ribonucleoside activities, modified nucleosides, enzyme inhibitors and a general regulatory network lie outside this six-reaction boundary. Native phosphomutase sugar-bisphosphate activators and assay inhibitors remain in the retained source and disposition ledger; they are not mistaken for consumed pathway intermediates or metal occupancy counts.

Public publisher retrievals for PMID:235429, 4992818, 357905 and 1089430 returned 403. The first and last have inspected substantive abstracts; 4992818 and 357905 have indexed metadata without abstracts. Their detailed catalytic claims are therefore explicitly attributed to the inspected native and reviewed annotations, not inaccessible paper text. PMC2168217 returned an HTTP-200 challenge page and its alternate endpoint returned 500; neither is claimed as inspected full text. PMC6193948 was retrieved as genuine complete primary XML. Acquisition manifests retain failures and use a strict metadata allowlist. Every maintained reference digest names its actual hash scope, including the uncompressed PathBank member and complete Rhea gzip.

## Validation and handoff

`purine-deoxy-replay.py` performs read-only independent parsing of externally retained source bodies, native and closed-schema validation, all 22 side/coefficient checks, six balances, six native Rhea-family bridges, four protein/MG1655 crosswalks, ChEBI labels, all 29 reference hashes, and actual KGX export/readback. The final receipt and target digest are in `purine-deoxy-validation.json`. The graph has 24 participants, six reactions, 49 edges and 80 evidence blocks; actual KGX has 32 nodes. Full corpus gates and the independent scientific review belong to the integration workflow, not this author receipt.

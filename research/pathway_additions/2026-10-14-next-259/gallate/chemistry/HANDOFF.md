# Next259 independent chemistry author handoff

Candidate: **MetaCyc:GALLATE-DEGRADATION-II-PWY**, issuing display **gallate degradation I**. This is external author research, not an independent review or approval. No maintained file, authority snapshot, Git object or GitHub object was changed. Frozen `gal2014/` and `gal2016/` packages remain unchanged.

The four formal native equations are chemically coherent and match the selected Rhea directions. Ten complete native CML graphs, including their 2D double-bond geometry, match the issuing ChEBI structures after explicit/implicit hydrogen normalization. Full InChI, InChIKey, formula and charge match independently. All ten pinned ChEBI 255 rows were independently reread from the whole hash-bound SQL original. All 45 Rhea reaction/side/participant/compound subjects were reconstructed from the full original RDF and match the native agent’s projection; the four equations and direction quartets were independently traversed again.

| Native member | Selected Rhea | Selected equation | Native metadata |
|---|---|---|---|
| GALLATE-DIOXYGENASE-RXN | RHEA:28928 | Gallate + O2 → keto OMA + 2 H+ | Physiological L2R |
| RXN-9983 | RHEA:28932 | Keto OMA → E,E enol CHM | Reversible; spontaneous=true; selected L2R |
| RXN-2463 | RHEA:17403 | E,E CHM + water → CHA | Reversible; selected **R2L** relative to native sides |
| RXN-2464 | RHEA:28936 | CHA → pyruvate + oxaloacetate | Reversible; selected L2R |

The calculated sum is **gallate(−1) + O2 + H2O → pyruvate(−1) + oxaloacetate(−2) + 2 H+**. Both sides contain C7 H7 O8 and net charge −1. This sum is a calculation, not an additional elementary reaction. Selected forward material edges do not erase native reversibility or establish thermodynamic irreversibility.

| Chemical | Exact source-normalized ID | Formula; charge |
|---|---|---|
| Gallate | CHEBI:16918 | C7H5O5; −1 |
| Keto OMA | CHEBI:57471 | C7H3O7; −3 |
| Formal E,E enol CHM | CHEBI:58142 | C7H3O7; −3 |
| Distinct native-prose Z,Z enol | CHEBI:57732 | C7H3O7; −3 |
| CHA with unspecified absolute configuration | CHEBI:58075 | C7H5O8; −3 |
| Oxaloacetate | CHEBI:16452 | C4H2O5; −2 |
| Pyruvate | CHEBI:15361 | C3H3O3; −1 |
| Water / dioxygen / proton | CHEBI:15377 / 15379 / 15378 | H2O; 0 / O2; 0 / H; +1 |

The principal dispositions are:

- **Preserve the native narrative conflict.** The pathway comment links `CPD-185` (Z,Z, CHEBI:57732), but RXN-9983 and RXN-2463 use `CPD-12849` (E,E, CHEBI:58142). They have different complete stereochemical structures and keys. They are not interchangeable synonyms. ChEBI’s historical `cis,cis` label for CHEBI:58142 coexists with its explicit E,E IUPAC name and structure; the label alone does not imply Z,Z.
- **Keep primary geometry source-bound.** The 2011 publisher text reports GalA’s immediate keto OMA product and assigns GalD’s product as E-OMAenol using the 6.73 ppm versus absent 7.38 ppm signal. The 2016 paper interprets this as (2E,4E)-CHM and freshly compares utilization by GalB and E6 LigJ. It does not newly determine every double-bond geometry by NMR. The separate (2Z,4E) LigI drawing discussed in 2016 is neither E,E nor the native narrative’s Z,Z isomer.
- **Keep CHA generic with an explicit optical qualifier.** The 2016 experiment yields and consumes the negative CHA enantiomer. Figure 9 models S-CHA but explicitly leaves the negative product’s absolute configuration unknown. CHEBI:58075 preserves the unspecified center; it does not assert a racemic product. Modern SYK-6 LigJ S-CHA cannot be transferred to KT2440 GalB.
- **Distinguish enol from the proposed enolate state.** CHEBI:58142 is the trianionic enol. Figure 9A’s proposed bound enolate has an additional deprotonated oxygen, calculated C7H2O7 and charge −4. Preserve this catalytic interpretation in evidence, without inventing an exact enolate identifier or silently changing normalized equation coefficients.
- **Do not substitute KCH.** The inspected 2018 SYK-6 LigJ and 2019 KA1 LigU abstracts concern (3Z)-KCH and a distinct allylic isomerization. They do not rename GalD’s measured product or resolve GalB absolute stereochemistry. Their main papers remain outside the obtained full-text access.
- **Retain schematic limitations.** A manual transcription of the 2014 DesB Figure 1A product yields neutral E,E enol, matching CHEBI:58142 only after explicitly removing the three carboxyl protons. It is a background drawing, not a new solution-product assignment. The 2023 Figure 1 is also a pathway summary. The 2021 DesB Figure 1 labels both the unsaturated keto LigU product and the saturated hydroxy LigJ product as CHA; the former has KCH-like topology. Preserve that apparent label error rather than silently correcting the source or importing it into GalD chemistry.
- **Keep the GalB kinetic substrate conflict visible.** The 2011 primary text assigns Km 85 µM and Vmax 76 µmol/min/mg to OMAenol. Native activity metadata labels CHA. Use the primary assay substrate for that kinetic claim.

`chemistry-claim-ledger.json` contains 19 bounded claims and all 12 material edge proposals, with exact native/Rhea and primary locators and no verbatim quotes. `independent-chemistry-check.json`, `independent-rhea-equation-check.json`, `pinned-recheck.json` and `primary-drawing-interpretation.json` preserve reproducible calculations. `source-coverage-ledger.json` records what was read and the access limits. `P184-precedent-check.json` verifies its three shared native downstream members without making P184 authority for this whole route.

The main remaining access gap is the **2011 figures and supplement**: publisher-indexed text and captions were read, but neither this task nor the parent’s failed raw download attempts supplied a usable figure image. Fresh PDF screenshot calls returned text-only references or timeout, so no visual 2011 figure read is claimed. Current issuing JSON originals and Rhea RDF are reused with hashes and acquisition dates; the public MetaCyc mirror is version 27.0, not a claim of current upstream release. All original copies and completed artifact files are bound in `reuse-receipts.json`, `verification.json` and `artifact-manifest.json`.

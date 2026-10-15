# PWY-5420 formal chemistry — frozen author handoff

The exact seven-step oxidative catechol route is chemically closed. It comprises PWY-5419 (four reactions) followed by PWY-5162 (three reactions), as one PWY-5420 candidate. All seven equations, 28 material entries and six exact intermediate joins pass independent atom/charge calculations from native CML graphs and complete issuing ChEBI structures.

| Step | Native reaction | Native source direction / route traversal | Exact forward chemistry proposal |
| --- | --- | --- | --- |
| 1 | CATECHOL-23-DIOXYGENASE-RXN | Physiological L2R / L2R | RHEA:17338 |
| 2 | RXN-8527 | L2R / L2R | RHEA:34220 |
| 3 | RXN-8529 | Reversible / L2R | RHEA:33432 |
| 4 | 4.1.1.77-RXN | Physiological L2R / L2R | Keep exact native enol reaction |
| 5 | 2-OXOPENT-4-ENOATE-HYDRATASE-RXN | Physiological R2L / R2L | RHEA:22582 (Rhea RL) |
| 6 | MHPELY-RXN | Reversible / L2R | RHEA:22625 |
| 7 | ACETALD-DEHYDROG-RXN | Reversible / L2R | RHEA:23289 |

These proposals follow a fresh exact participant/coefficient search across all 18,611 direction families (37,222 LR/RL equations) in the independently acquired, hash-verified Rhea 142 originals. Nine complete families / 36 members and their 110 selected source subjects are retained. All 36 labels agree with pinned Rhea 139 SQL; newer equations and older production labels remain separately attributed. A directional identifier does not establish physiological irreversibility.

The net reaction is:

`catechol + O2 + 2 H2O + CoA(4−) + 2 NAD(1−) → CO2 + pyruvate(1−) + acetyl-CoA(4−) + 2 NADH(2−) + 3 H+`

Both sides contain **C69 H94 N21 O50 P7 S**, charge **−6**. NAD(1−) and NADH(2−) denote the complete charged ChEBI species, not informal redox-center names. Pyruvate is an aldolase branch product; acetaldehyde alone continues into step 7.

The critical distinctions are explicit:

- RXN-8527 preserves the exact 2Z,4E geometry through aldehyde oxidation. RXN-8529 matches 28080 → 64908. Its native RHEA:32214 cross-reference instead joins 16967 and 64016, with different keto bond position and enol stereochemistry; the entire 32211 family is rejected as an exact equivalent.
- Native decarboxylation produces the **2Z dienol** 67152. Linked RHEA:24261 produces the distinct **keto** species 11641. No exact finite-species enol counterpart was found in the complete pinned Rhea 142 directions. The hydrolytic alternative has the same enol-versus-linked-keto problem and is excluded from this seven-step route.
- The parent pathway's 2E prose is preserved as a conflict. Its child modules, formal reaction sides and independent structures join through 2Z 67152. Five C6 and four C5 alternatives are resolved into actual bond/stereo patterns, with 16 pairwise comparisons; names and formulas are insufficient for substitution.
- Native-only CPD-13337 and CPD-14441 remain distinct comparators. Whole pinned ChEBI 255 exact InChI/InChIKey searches returned no match; this is not a global/current absence claim. Historical spontaneous-product, PraC and Bordetella assay interpretations remain primary-evidence work.

The complete input inventory binds **40 native META 27.0 objects**, **21 complete issuing ChEBI API originals** (13 exact reused, eight newly retrieved), and four external whole Rhea/ChEBI source artifacts. Eleven native generic/unparseable SMILES and six stereo-incomplete pinned ChEBI SMILES are preserved as representation limitations; complete native CML/full InChI plus independent issuing structures supply the exact checks. Native CML reconstruction alone does not prove stereochemistry.

Start with `formal-chemistry-proof.json`, `chemical-dispositions.json`, `structural-alternative-comparisons.json`, `complete-input-inventory.json` and `scope-and-limitations.json`. Full objects, every retained direct slot, exact RDF fragments, complete ChEBI bodies, source versions, locators, acquisition/reuse receipts and reproducible helpers are retained externally. Compact selection is a lossless retention proposal, not a maintained edit.

This is a verified **author** dossier, not an independent scientific review or proof that one organism experimentally executes every step. No primary full text was newly read for this chemistry task. The six-step 1971 endpoint does not independently establish the seventh CoA-acylating reaction or exact modern stereochemistry. Targeted primary work follows in a separate directory. Final baseline/dedup rebind, biological claims, maintained authority selection and independent review belong to root. Frozen discovery/native packages and all maintained/Git/GitHub state remain unchanged.

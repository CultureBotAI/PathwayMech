# Next264 formal chemistry preparation

The complete two-step chemistry of **MetaCyc:PWY-2503, benzoate degradation I (aerobic)** is supported by exact native structures and issuing ChEBI/Rhea originals. This package prepares sources; it does not author a maintained pathway, independently approve a final record, resolve organism/preparation claims, or establish source exhaustion. Rebind discovery to the verified post263 merged baseline before authoring.

## Exact formal route

1. **RHEA:12634**, left-to-right member of family 12633–12636: benzoate + NADH(2−) + H+ + O2 → (1R,6S)-1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate + NAD(1−).
2. **RHEA:11561**, left-to-right member of family 11560–11563: that dihydrodiol carboxylate + NAD(1−) → catechol + CO2 + NADH(2−).

All coefficients are one. Both complete reactions have C28 H33 N7 O18 P2 and charge −2 on each side. Native pathway order joins the steps through CPD-290. NAD also appears on the shared adjacent sides; it is a cofactor cycle, while CPD-290 is the primary material join. The net calculated equation is **benzoate + H+ + O2 → catechol + CO2**, C7 H6 O4 and charge zero per side. NAD/NADH cancel. This sum is bookkeeping, not a new elementary reaction or empirical flux claim.

The complete issuing Rhea142 RDF, directions table, exact eight family descriptions and participant closure were inspected. All eight family records are Approved and marked chemically balanced; the RDF master/LR/RL/bidirectional side links agree with the issuing directions table. Rhea139 pinned SQL labels for the two selected directional equations also agree. The complete fixed-coefficient comparison examined 37,216 directional equations and found only the two respective families as exact whole-side equivalents. Six equations have unresolved fixed material sides and were excluded; their exact IDs and complete side descriptions are retained in `rhea-equivalence-search-exclusions.json`. Do not interpret that finite comparison as a generic/polymer equivalence or global pathway-exhaustion result.

## Exact core compounds

| Native frame | Selected identifier | Issuing label | Formula | Charge |
|---|---|---|---|---:|
| BENZOATE | CHEBI:16150 | benzoate | C7H5O2 | −1 |
| CPD-290 | CHEBI:60129 | (1R,6S)-1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate | C7H7O4 | −1 |
| CATECHOL | CHEBI:18135 | catechol | C6H6O2 | 0 |
| NAD | CHEBI:57540 | NAD(1−) | C21H26N7O14P2 | −1 |
| NADH | CHEBI:57945 | NADH(2−) | C21H27N7O14P2 | −2 |
| PROTON | CHEBI:15378 | hydron | H | +1 |
| OXYGEN-MOLECULE | CHEBI:15379 | dioxygen | O2 | 0 |
| CARBON-DIOXIDE | CHEBI:16526 | carbon dioxide | CO2 | 0 |

Each row has exact full native/issuing/pinned InChI, InChIKey, formula and charge agreement. Complete native CML connectivity agrees with issuing and pinned ChEBI SMILES graphs. CPD-290 has two specified chiral centers, R and S; its exact native and issuing InChI ends `/p-1/t5-,7+/m0/s1`, key `PUCYIVFXTPWJDD-CAHLUQPWSA-M`. The full source InChI/issuing stereochemical structure supplies stereochemistry; it is not inferred from the native CML drawing or from the generic word “cis”. No primary-paper absolute-configuration experiment is asserted here.

Native BENZOATE, NAD and NADH SMILES are incomplete/generic and fail exact parsing. They are retained as source defects, not silently repaired. NAD and NADH standard-InChI reconstruction can normalize proton/bond microstates differently from the explicit CML/SMILES representations; full standard-InChI identity and explicit graph comparisons are separately recorded. These reconstruction microstates are not evidence of assay atom positions. Native monoisotopic-mass fields were not used to identify ion forms.

The native parent prose says the dihydrodiol is “reduced” to catechol. Its reaction instead describes substrate oxidation/decarboxylation while NAD+ is reduced. Preserve this disagreement. Formal NAD(1−)/NADH(2−) normalization does not establish preparation-specific NAD/NADP selectivity or assay protonation conditions; the primary/preparation task owns those claims.

## Context cofactors

The native activity source task supplied two additional complete compound originals, copied at its declared hashes and then checked against its completed frozen manifest in `native-cofactor-frozen-binding.json`:

- **FAD → CHEBI:57692, FAD(3−)**: exact full InChI/key, C27H30N9O15P2, charge −3 and complete native CML/issuing graph agreement. Native generic SMILES is incomplete. This is the normalized native molecular form; it does not assert the protein-bound or assay microstate.
- **MetaCyc:CPD-6** is a class with two Fe, two bridging S, four protein-ligating S and four R groups in its native CML, empty molecular formula and no InChI. Its CHEBI:33739 cross-reference describes a specific neutral Fe2S2 core, `di-mu-sulfido-diiron(0)`, and does not establish exact identity for the complete protein-ligated class. The `(0)` is net charge notation; the issuing IUPAC synonym uses diiron(II), so do not describe the irons as zero-valent. **CHEBI:49601** is the generic Fe2S2 iron-sulfur cluster class with no fixed formula/charge/InChI; it contains both tetracysteinyl and Cys/His-ligated subclasses. It can ground only that generic class concept. Retaining MetaCyc:CPD-6 preserves the more specific native representation. Neither mapping supports a Rieske ligand assignment, oxidation state, or ligand protonation for a preparation.

The native activity cofactor citation/preparation mismatch is recorded by the native and primary tasks. This package does not transfer a C-1 cofactor result onto JMP222 or resolve that mismatch by chemical identity alone.

## Evidence and reproduction

- `chemical-identity-closure.json`: all eight core structures, CML fragments, exact InChI/keys, charges, formulas and representation caveats.
- `whole-route-chemistry-replay.json`: every native and Rhea side/participant/coefficient, 11 material-side entries, element/charge totals, exact family matches and net equation.
- `rhea-family-orientation-verification.json`: issuing family links and direction conventions, all eight approved statuses, pinned-label compatibility.
- `context-cofactor-identity-assessment.json`: FAD exact closure and the explicit cluster identity/class distinction.
- `input-manifest.json`: frozen discovery/263 source bindings and full SHA256 checks of the 4,137,340,928-byte pinned ChEBI255 and 1,025,437,696-byte pinned Rhea139 SQL databases. Complete selected outgoing subject rows are retained. Those multi-GB databases remain external; a projection is not represented as an original structure source.
- `acquisition.json` and `context-cofactor-acquisition.json`: all 14 fresh source requests, complete response bodies, URLs, headers, timestamps and hashes. All returned HTTP 200.
- `execution-receipts.json`: actual preparation/replay commands and observed outcomes. Helpers are retained as inert `.py.txt` files. RDKit 2026.03.5 was verified in its independent environment; the shared195 and root's fresh263 environments were not used or modified.
- `attempts/`: the first replay helper, partial successful structure result and complete failure log. Its full-Rhea pass initially assumed all directional sides had fixed material entries and raised KeyError for 22452_R. The corrected helper excludes unresolved sides explicitly. A separate audit enumerates all six exclusions. No selected family is unresolved.

The full original Rhea RDF remains in this external package and is hash-bound; the compact handoff may omit that bulk duplicate while retaining selected complete descriptions and the full-source locator/hash. Compact gzip copies are lossless and have original/stored hashes. Do not mutate this package after its artifact manifest is written; append any later correction separately.

# PWY-5417 primary-source preparation

This is a finite **source-authoring** handoff for catechol degradation III. It is not an independent scientific review, a maintained record, an identifier-authority promotion, or a claim of absence against a post-262 baseline. No maintained files, Git, or GitHub were changed.

The frozen native input is `/private/tmp/pathwaymech-next-263-native/artifact-manifest.json`, SHA256 `302c4e494f3bfc92f4062e223f5bf7316451e29bc1e4ca52e97b32d70671abcc`. Integrity verification rechecked all 394 native files without changes. Native provenance and activity/conflict ledgers were copied into `predecessor-bindings/`.

## Coverage and access

- All **42 direct native literature leads** are individually accounted for, plus six bounded historical, regulatory, or conflict follows.
- **48 source access records**, **63 source-supported claim dispositions**, **18 native conflict dispositions**, **20 formal activity associations**, and **19 formal catalysts** are covered.
- Twenty papers have some retained article text or page scans; 21 are abstract-only and seven metadata-only. These counts do not imply complete reading of every acquired body. `source-access-and-reading-ledger.json` names the actual sections read and the missing material for each paper.
- Sixty-six full-text/scan candidates were copied only after exact predecessor artifact and source-manifest binding. The predecessor source audit covers 142 artifacts. Earlier reviewer/author prose is retained only as a lead, never substituted for primary reading.
- Thirty-nine page scans were freshly OCRed. Eight listed original pages were visually inspected. Other publisher or ResearchGate article transformations are **text access**, not visual PDF or figure inspection. ResearchGate reproductions are labeled as such even where a convenience filename says `publisher-transformed`.
- HTTP 200 redirect shells and challenge pages are not accepted as scientific bodies. No search-result snippet supports a claim. The unrelated human amniotic-fluid PMID761399 remains explicitly rejected.

## Material findings for the next author

1. **MT1 CatA/SalD:** PMID17172348 supports native preparations and opposite substrate preferences. CatA and SalD purity was approximately 41% and 57%, respectively. The CatA native paragraph's heterologous/4-methylcatechol tail cannot support these assays. CatC remains a sequence-based assignment.
2. **B13 inhibitor target:** PMID11741862 assigns the three uncompetitive analog inhibitors to the **CoA transferase**. Native REG-5831, REG-5832, and REG-5833 instead target thiolase. `regulator-target-and-reagent-assessment.json` binds every native XML element and the exact primary paragraph. The separate thiolase experiments tested CuSO4, NaCN, and ZnCl2 at 1 mM. Mercury reagent effects were indeterminate because the substrate decomposed.
3. **B13 preparations:** transferase assembly was inferred as A2B2; thiolase as A4. The latter preparation retained two minor impurity bands despite later homogeneous wording. B13 biology cannot inherit P. putida induction through the parent hyperlink to MONOMER-12813.
4. **H16:** Table 2 assigns pcaI/pcaJ to transferase subunits and pcaF/H16_B0200 to the thiolase candidate. Protein abundance and mutant phenotypes are narrower than purified catalysis. The separate recombinant purification experiments concern dehydrogenases.
5. **Historical identity:** the PcaD preparation used PRS2260, a phage-resistant isolate from strain 2178; its mass-inferred 33 kDa trimer/11 kDa subunit is not three modern Q88N36 molecules. Historical PcaIJ A2B2 evidence remains separate from the 1992 gene/construct study and current issuing annotations. PRS2000 is a derivative of PRS1 (ATCC12633), not an alias.
6. **CatA and constructs:** the exact Q9AEQ0 issuer response is inactive/deleted and points to UniParc UPI00000B8127. No replacement was guessed. C1 alpha/beta isozymes and the 98%-similar mt-2 enzyme are distinct. PMID8083169 also contains an internal K38-versus-DH5α host conflict for the pHS104 binding preparation.
7. **Reaction versus pathway scope:** Y2 PMID9495743 directly assays PaaK, not terminal PaaJ. The captured PNAS PaaJ Results are partial and omit preparation Methods. Phenylacetate assays and engineered reverse adipate pathways do not demonstrate a native complete catechol route. Eleven native parent-organism rows are not eleven complete-route experiments.

All findings have claim IDs, source artifact hashes, locators, preparation limits, and acceptance checks in the JSON ledgers. The claim summaries are **author paraphrases**, not ready-made `source_assertion` evidence. A record author must use a short exact excerpt or an actually structured table/database fact at the appropriate edge. Scientific review must be performed by someone who did not author these contributions.

## Reproduction and remaining work

`helpers/build_dossier.py` reconstructs the authored ledgers offline; `helpers/regulator_assessment.py` replays the six native regulation objects. `helpers/verify.py` checks exact source bindings, all native preservation, finite coverage, and compact decoded bytes. Acquisition scripts and every original response remain retained, including errors. The historical intake script records its actual predecessor paths; no live 262 worktree is needed for the active offline verification.

`package-verification.json` records successful source and coverage checks. `compact-retention-manifest.json` describes deterministic archives and every member's decoded hash; `artifact-manifest.json` binds the complete frozen package. Run `python3 helpers/verify.py` read-only after freezing. Do not run acquisition or rebuilding helpers in the frozen directory; use a new successor directory.

`finite-closure-and-gaps.json` explicitly retains unread historical miniprint, body-only access gaps, the PaaJ preparation gap, unresolved issuing identities and chemical mappings, and the need for a post-262 baseline rebind and independent review. The separate identity and chemistry authors own their exact source packages; their messages are coordination leads until their frozen originals are independently bound. Public-release licensing review remains deferred as instructed.

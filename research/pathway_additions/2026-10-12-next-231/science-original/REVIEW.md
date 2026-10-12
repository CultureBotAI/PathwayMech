# Independent scientific review: MetaCyc:PWY-8178

The complete six-event PPi-dependent branch is scientifically supported at the stated evidence levels. Five minor preparation, assay-provenance, bibliography and direction-metadata findings require bounded correction. No blocker or major defect found; no reduction of the six events, 20 sides, 51 edges, 53 references, 14 qualifiers or negative/conflicting controls is recommended.

Target SHA256: `a5fb4208601109e5939577f84276a0fbe6ff28a324fa40a4b057b7bfe338e35a`. The review covers every edge, qualifier, description paragraph and inherited preflight disposition. It is an external review packet; native save/integration remains root-owned.

## Findings

### Minor: Correct the CDQ83_07225 coupling-enzyme preparation and its evidence

Stable key: `pwy8178-ammonium-assay-preparation`.

The qualifier says auxiliary-enzyme ammonium sulfate was removed by ultrafiltration. The 2020 Methods instead specify lyophilized rabbit aldolase/GPDH and explain that the earlier ammonium-sulfate suspensions could not be used with S7P barium salt. Ultrafiltration in the neighboring paragraph applies to the purified PFK buffer exchange. The qualifier cites 2019 preparation paragraphs, which do not establish the 2020 added-ammonium condition.

**Correction:** State that the 2020 assay used lyophilized auxiliary enzymes in place of the earlier ammonium-sulfate suspensions, retaining BaSO4 precipitation and the source NH4Cl2 inconsistency. Cite the actual 2020 Methods in the qualifier; preserve the separate 2019 His6/TEV construct evidence.

**Acceptance:** No claim that auxiliary enzymes were ultrafiltered remains. The qualifier includes the 2020 assay paragraph and keeps CDQ83_07225/F6P/ATP scope; no PPi-S7P catalytic edge is added.

### Minor: Separate the Pfp mixed-substrate activity assay from the MS identity experiment

Stable key: `pwy8178-competition-assay-modality`.

The draft calls the mixed F6P/S7P competition measurement an MS assay. The primary Results say that the competition assay monitored FBP production, and the Pfp Methods describe the coupled activity assays. The separate MS Methods contain S7P alone for product identification. The inaccessible supplementary Table S3 is not a basis for asserting an MS competition readout.

**Correction:** Replace mixed-substrate MS assay with mixed-substrate FBP activity assay; add the Pfp assay Methods locator if specifying the coupled readout. Keep the observed decrease and the explicitly interpretive competition explanation.

**Acceptance:** The S7P inhibition edge still refers only to reduced F6P-to-FBP activity with mixed substrates; it does not assert binding affinity or suppression of S7P catalysis.

### Minor: Use the actual titles of the 1982 and 2022 primary articles

Stable key: `pwy8178-reference-titles`.

Both title fields contain descriptive substitutes. The 1982 original first-page scan is titled A pathway for the interconversion of hexose and pentose in the parasitic amoeba Entamoeba histolytica. The retained 2022 publisher rendering is titled Increasing the Thermodynamic Driving Force of the Phosphofructokinase Reaction in Clostridium thermocellum.

**Correction:** Replace the two title strings with the inspected original titles; retain the existing identifiers, URLs, artifact bindings and access limitations.

**Acceptance:** Both titles match the originals after whitespace normalization; no reference identity or source hash is silently replaced.

### Minor: Carry the six known reversible directions into reaction metadata

Stable key: `pwy8178-reaction-direction-metadata`.

Every original Reaction has reaction-direction REVERSIBLE, and the prose and side evidence correctly retain it. All six record reaction nodes omit direction, so the native node/graph/export direction field is unavailable despite known source support.

**Correction:** Set direction: reversible on each of the six existing reaction nodes. Keep the selected pathway-layout side orientations and all twenty side occurrences exactly as authored.

**Acceptance:** All six node directions are reversible; the 51 edge triples and 20 side triples remain unchanged. Standalone/native page and KGX node metadata expose the direction after regeneration.

### Minor: Bind construct features to the exact tested enzyme and nearest primary passage

Stable key: `pwy8178-construct-evidence-scope`.

ppi-034 asserts the His6/TEV construct but cites only the 2020 Methods and issuing native sequence; the retained 2019 Methods directly establish that feature. Aldoa linker wording is supported by the 2023 Results, but those Results are omitted from the qualifier locators. For Pfp, the inspected 2023 Methods explicitly call PfkA, PfkB and Aldoa codon optimized, then refer Pfp to an earlier study; the Pfp-specific text and thesis establish His6 but do not explicitly establish its linker or codon optimization. Those features should not be transferred from neighboring proteins.

**Correction:** Add the retained 2019 direct construct citation to ppi-034. Add the actual Aldoa linker Results locator to the four Aldoa qualifiers. For Pfp, keep the supported pAHCT0347/pRSET-A, His6, host, strain and assay distinctions, while making the linker/codon-optimization uncertainty explicit or supplying an inspected Pfp-specific construct source before retaining those extra features.

**Acceptance:** Every retained construct feature is entailed by its cited exact passage for that enzyme. No unsupported Pfp linker/codon-optimization assertion remains; all biological endpoints, catalytic activities, signs, strains and negative controls are preserved.

## Biological boundaries retained

The native pathway identity, all six reversible events, twenty sides, exact strain-specific enzyme identities and fourteen construct qualifiers remain. The historical amoebal activity evidence has no fabricated modern sequence. Rabbit coupling does not prove native clostridial SBP aldolase. The 2023 FBP Aldoa work, DSM1313 versus ATCC27405 kinetics, thesis F6P inhibition and negative controls, paired TktAB genetics, unsigned Rex binding, 2022 loss counterexample, native class/charge conflicts and wrong B8I4R1 bridge are preserved.

## Evidence and checks

All 345 scientific artifacts and 57 external originals match their hashes. The closed hidden/ignored/followed inventory also accounts for 107 excluded runtime files. All 102 XML evidence selectors replay exactly; the remaining 14 PDF/EC/JSON/PDB observations were independently assessed. Fresh native probes cover six events, twenty sides, twelve chemicals, thirteen NCBI proteins, sixteen native associations and the 149-residue RpiB join. Twenty original thesis pages were independently re-extracted through PDFKit; first-page and kinetic source scans/figures were visually read.

## Limits

- This is an independent external full-record scientific review of the sealed author draft. Root owns issue creation, curation, maintained native review persistence and publication; no maintained or sealed files were edited.
- No full canonical builder, corpus test/validate/lint suite, maintained page consistency gate or Git/GitHub action was run by this reviewer. Author bounded checks are retained evidence, not relabeled as reviewer or maintained checks.
- Authority proposals use EG outputs. ATP baseline bridge and independent full canonical acceptance are pending and are not inferred here. Multi-GB SQL originals were not rehashed during this scientific review.
- All 345 scientific artifacts and 57 external original bindings were freshly hash-verified ; 107 compiler/uv runtime files are excluded by the author and were checked only for closed inventory and sizes.
- Original 1982 six-page scans and WUR five supplement page images were visually inspected. Twenty selected Taillefer PDF pages were independently extracted; only the stated PFK/preparation passages and selected tables/figures were scientifically assessed, not the entire 475-page thesis.
- The 2022 source is an archived publisher web rendering, not a newly acquired original HTML body. The 2011 RpiB full body and relevant supplementary bodies remain unavailable; no unseen kinetic data are claimed.
- Fresh PubMed browser attempts encountered reCAPTCHA and HTTP 429; title findings rely on the inspected original 1982 scan and retained 2022 publisher rendering. Other issuing source identities are evaluated against hash-bound originals, not a claim of live re-fetching.
- The initial pypdf import failed because the module is absent; independent PDFKit extraction succeeded. Probe construction errors and over-broad debug projections are retained and do not count as scientific failures or absence findings.
- iModulonDB applicability and broad novelty inventories are inherited from the exact author packet. Their original-bound results and relevant biological comparisons were inspected; no fresh full-source exhaustion claim or new adapter query was made.

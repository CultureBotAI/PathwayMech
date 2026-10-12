# Independent external scientific review

**Verdict: request changes.** Two major finding groups and two minor provenance groups. Target `MetaCyc:THRDLCTCAT-PWY`, external draft-v6 SHA256 `ce63781482b002348cdedede3c2d2155385df99ba371a7e1abc2d7c11d4d9317`.

This review covers the complete three-event route, two transport contexts, LIV-I activity, three opaque pathway interfaces, 111 edges, 84 named identities and 83 references. The formal chemistry and full native boundary are supported; reducing scope is not the remedy.

## Findings

### Major: L-serine competition is assigned to alanine

Key: `threonine-iii-tdcc-serine-endpoint`. Edges: thr-iii-106.

The edge subject CHEBI:16449 is alanine, while its assertion and original experiment concern excess L-serine. Table 1 reports normalized uptake 0.23 with L-serine, 0.81 with L-alanine, and 0.20 in the tdc-deleted control; the source text says alanine did not significantly affect uptake. Thus the graph asserts the wrong chemical interaction despite correct narrative.

Parent-created issue: https://github.com/CultureBotAI/PathwayMech/issues/432

Replace the erroneous subject and corresponding participant with authority-backed CHEBI:17115 L-serine. CHEBI:33384 may be used only with explicit source-neutral-to-zwitterion normalization. Remove the alanine inhibition assertion; retain whole-cell competition rather than allosteric inhibition, and preserve all other graph scope.


Acceptance: Re-read the original assay table and exact ChEBI definition for the selected L-serine endpoint. Add a source-backed negative control which restores CHEBI:16449 and must fail independently of narrative labels. Refresh source/edge/identity ledgers, authority artifacts, render and KGX after correction; preserve all 111 edges unless a separately supported correction is made.

### Major: Three source assertions cite native objects that do not contain the stated support

Key: `threonine-iii-native-source-misattribution`. Edges: thr-iii-066, thr-iii-069, thr-iii-100.

The biology is supportable from existing bound originals, but the nearest cited objects are wrong. MetaCyc pathway comments do not contain the claimed SstT/TdcC uptake paragraph; EcoCyc pathway comments do. EcoCyc TU0-42552 contains FeaR/NsrR commentary, not the FNR anaerobic-profiling paragraph; the bound MetaCyc AMINEOXID-CPLX comment contains it.

Parent-created issue: https://github.com/CultureBotAI/PathwayMech/issues/433

- thr-iii-066, thr-iii-069: Cite the EcoCyc pathway comment, optionally together with exact transporter physiologicalReaction annotations. Preserve conditional substrate supply without concurrent expression or full-route flux. Source: EcoCyc:THRDLCTCAT-PWY; /ptools-xml/Pathway/comment, first paragraph naming SstT, LIV-I, TdcC and threonine use; native XML line28.
- thr-iii-100: Reference MetaCyc:AMINEOXID-CPLX and say native complex comment reports, rather than native TU reports. Preserve direct-versus-indirect uncertainty, the conflicting 2013 reporter conditions, and no inference of anaerobic oxidase flux. Source: MetaCyc:AMINEOXID-CPLX; /ptools-xml/Protein/comment, final paragraph citing PMID12754220; native XML line66.

Acceptance: Resolve each source locator inside the newly cited hash-bound original, not an adjacent database object. Reject negative controls that restore the wrong MetaCyc pathway or EcoCyc TU reference even though nearby sources support the biology. Re-review all three revised edges and maintain their uncertainty and source-versus-primary distinctions.

### Minor: Supported assertions need precise locators or additional existing references

Key: `threonine-iii-evidence-locator-closure`. Edges: thr-iii-024, thr-iii-025, thr-iii-026, thr-iii-030, thr-iii-033, thr-iii-034, thr-iii-049, thr-iii-059, thr-iii-060.

The underlying claims checked here are supported. These corrections improve exact replay and distinguish composite assertions from their individual source objects.

- thr-iii-024, thr-iii-025, thr-iii-026: Retain pathway reaction-list/layout membership evidence and add the alreadydeclared matching MetaCyc reaction reference (THREODEHYD-RXN, THREOSPON-RXN, AMACETOXID-RXN) for its native RHEA dblink.
- thr-iii-030: Correct Pathway/pathway-links to singular Pathway/pathway-link[Compound/@frameid="METHYL-GLYOXAL"]/link-target/Pathway[@frameid="PWY-5386"].
- thr-iii-033: Add the bound EcoCyc:RXN-14249 reaction-list reference for composite membership; THREODEHYD-ENZRXN only points to the composite.
- thr-iii-034: Remove nonexistent Table 2. The complete eight-page paper has Table 1 (CD/secondary structure) only. Use p750 Enzymatic Activity Assays, p752 Fig3 and substrate text, and p753 cofactor text as appropriate.
- thr-iii-049: Add PMID:22411989 Results initial metal-activity paragraph/Table1 for the no-Cd-activity half of the retained conflict; UniProt P07913 supports the older Cd-exchange annotation.
- thr-iii-059: Add existing EcoCyc:CPLX0-7797 Protein/comment for oxygen-dependent dimer/cluster state, separately from the UniProt cofactor count.
- thr-iii-060: Add existing EcoCyc:CPLX0-7756 Protein/comment for the S. coelicolor physical-state study caveat, separately from UniProt E. coli curator-inferred cofactor assignment.

Acceptance: Every revised locator resolves to inspected supporting content in its own cited original. Preserve all biological endpoints, directions, condition limitations and conflicts.

### Minor: Optional explicit disclosure of historical TdcC sequence provenance

Key: `threonine-iii-tdcc-historical-sequence-provenance`. Edges: thr-iii-104, thr-iii-105, thr-iii-106, thr-iii-107, thr-iii-108.

The original p4292 Discussion/Fig5 describes 431 residues; current P0AAD8 is 443 residues and annotates historical sequence conflicts at 70 and 431–443. The draft makes no explicit full-sequence/material-equivalence assertion and already bounds these edges to whole-cell competition/energetic assays. This is not evidence that the assayed transporter was an engineered truncation or a distinct physical variant.

A concise shared note may disclose the historical 431-aa report versus the current 443-aa reference and that the complete assayed sequence is not established. Keep MC4100/TH16(pEC61) assay scope and do not conflate separate PhoA/LacZ topology fusions with the transport preparation. Do not add an invented variant node.


Acceptance: Any added sequence/material note states the uncertainty rather than equating a reporting discrepancy with a proven assayed variant. Retain the existing cell-assay and no-purified-binding qualifiers.

## Scientific assessment

- **Pathway identity and complete boundary:** Exact MetaCyc THRDLCTCAT-PWY identity and full three-event native boundary match the target. Oxidation, spontaneous decarboxylation and terminal aminoacetone oxidation are all retained; RXN-14249 is a composite and not a fourth elementary event. Source-defined completeness does not establish an experimentally reconstructed E. coli route.
- **Formal chemistry, direction and chemical identity:** Independent chemistry reviewer parsed original Rhea RDF, checked all 23 formal sides, contains/contains1 coefficients, master/directional links, transport In/Out context, and all five atom/charge balances. All 37 draft ChEBI labels match pinned authority terms/synonyms; identity of a term does not make its use in thr106 correct. All three core and two transport equations are retained.
- **Stable identities and components:** All 83 bound reference originals rehashed against YAML and bindings. Read-only GO/NCBITaxon SQL confirms four GO terms and two taxa; eight native Entrez IDs match exact genes, MG1655 taxon and protein products. Fifteen current UniProt entries, versioned AAB18566.1, exact native complex and monomer mappings, Tdh tetramer, TynA dimer, five LIV-I components, Dps dodecamer, NsrR/FNR dimers, and Lrp-leucine complex are supported. PubChem original CID78645 property object identifies 2-hydrazinopyridine; a pending production adapter is not a false chemical identity.
- **Terminal oxidation and experimental taxon scope:** TynA terminal assignment is native hypothetical EV-AS-NAS, not experimentally established aminoacetone catalysis in E. coli. The 1968 unnamed sewage isolate was described as closely related to Arthrobacter globiformis, not a resolved modern strain accession. Washed-cell methylglyoxal/O2 data and the proposed peroxide/catalase equation do not establish measured H2O2 or an identified oxidase. E. coli W1485/SBD76 aminoacetone non-growth/non-consumption and Serratia Sr41 unresolved further metabolism remain assay/strain bounded. Cytoplasmic Tdh and periplasmic TynA do not establish an intervening aminoacetone transport mechanism.
- **YiaY assay and construct identity:** Entire eight-page publisher PDF inspected. MG1655-derived orf382 was expressed as N-terminal six-His protein in BL21(DE3); the exact construct sequence was not supplied. Original AAB18566.1 is 382 aa; current P37686 is 383 aa with C-terminal differences independently compared. NADH340nm supports oxidation activity without directly measured intermediate/product or whole-route reconstruction. Metal assay/EDTA/CD evidence and Keio-versus-paper glycine phenotype conflict retain their stated limits. Table2 locator is erroneous.
- **Tdh cofactors, assays and redox protection:** Older one-Zn experimental abstract versus reviewed two-Zn annotation, Co/Cd exchange and 2012 no-Cd activity conflict are retained. Full 2012 main article was inspected. Fe/Mn activity, inferred intracellular occupancy, peroxide damage, conditional DTT/TCEP plus metal rescue, and Dps/MntH/Mn protection are bounded to preparations and measured enzyme activity. No supplement access, universal metal occupancy, isolated Mn occupancy proof, or complete pathway flux is claimed.
- **Transport and interfaces:** SstT sodium/threonine and TdcC proton/threonine directions and annotations, LIV-I ATP-dependent activity without invented complete stoichiometry, and three opaque pathway interfaces are supported. Original SstT1998 Thr301 versus current Ala301 and separate 2002 eight-His serine-transport preparation remain distinct. TdcC cell competition has the wrong L-serine endpoint in thr106; two uptake-supply edges cite the wrong native pathway object. Attached PathBank child identity/title and output interface do not establish complete child chemistry.
- **Regulation and context conflicts:** Primary Lrp repression of tdh with leucine induction is preserved against contrary native TU polarity. LIV transcription and transport responses remain condition dependent; ilvIH DNA-binding assays are not promoted to tdh/liv promoter binding. FeaR reporter effects and C-terminal six-His DNA-binding domain are distinct from full-length ligand-binding. FNR profiling versus 2013 no-anaerobic-induction conflict is preserved, but thr100 needs the correct complex comment source. NsrR native annotation, altered start-codon expression, and species/strain qualifications remain explicit; no supported tynA metal occupancy or direct allosteric flux claim is invented.
- **Expression-module and source-discovery context:** Author iModulonDB assessment and exact identifiers were inspected; target audit finds no iModulon membership promoted to catalysis or causal route proof. Reviewer did not independently replay all 32 author adapter bodies. Search absence is not negative biological evidence or source exhaustion.
- **Graph closure and validation:** 84 unique named IDs, 72 participants, nine reaction/activity/interface nodes, two taxa, 111 unique edges, 83 references and local endpoint/reference closure pass. Native target schema and closed strict checks passed; author render/KGX and 62 replay controls were inspected as receipts, not independent scientific acceptance. Passing automation did not detect the wrong alanine endpoint or wrong cited objects.

## Checks and source scope

- **Independent source hash and closure script — pass:** 83/83 source bodies match source bindings and YAML source_sha256; 84 unique IDs,111 edges,83 reference IDs; target and edge/qualifier reference closure. All three final ledgers parsed in full.
- **Native target-only schema and strict validation — pass:** validate_record returned MetaCyc:THRDLCTCAT-PWY; strict_errors([external_target],224root) returned []. Explicit pinned interpreter/PYTHONPATH; no whole-corpus rerun.
- **Independent chemistry and native boundary probes — pass:** 23/23 formal sides; all five balanced equations; exact native directions, membership, composite exclusion, opaque interfaces; 37 ChEBI labels.
- **Independent semantic probes of problematic source/endpoint bindings — fail:** Four failing edges: thr066,069,100 wrong source object; thr106 wrong chemical. Two sequence-distinction probes pass; TdcC historical provenance is minor.
- **GO/taxon exact authority readback — pass:** Four GO labels and two taxon labels/lineage queried read-only from pinned originals. These large DBs were not rehashed again by this reviewer; parent pins retained.
- **Author 62 controls, render, KGX and handoff — author_report_inspected_not_reexecuted:** Author receipts reviewed; root independently verified383artifacts and18handoffbindings. Reviewer additionally rehashed83reference originals and report inputs. These receipts do not override science findings.
- **Whole-corpus tests/lint/build/generated gates — not_rerun_by_instruction:** Parent owns already-authorized final gates and adoption; no duplicate whole-corpus gates for this external review.
- **Canonical maintained record review saver — not_applicable_yet:** Target remains external and unadopted. Parent explicitly requested external JSON/MD only; use maintained canonical lifecycle after adoption, retaining this review and its open findings.
- **Inspection helper initial run — recovered_local_tool_failure:** Initial helper named inspect.py shadowed the Python standard-library module during lxml import. Renamed to independent_inspection.py and reran successfully. No source/target inputs changed.

- PMID:24651643: Complete original eight-page publisher PDF (pp748–755), independently text-extracted using PDFKit and read; exact native versioned protein sequence inspected.
- PMID:22411989, PMID:24013633, PMID:9852024: Original full HTML main Methods, Results, Discussion and figure/table captions inspected. No claim to have inspected unavailable supplements.
- PMID:2115866: Original scanned article OCR read; original p4291 Table1/transport text and p4292 sequence/topology discussion visually inspected.
- PMID:5721463: Four original scanned-page OCR texts read; original p270 visually inspected for unnamed-isolate, washed-cell and proposed-oxidation scope.
- PMID:6413491: Critical original p277 negative aminoacetone-growth and cell-extract assay visually inspected, with original OCR context. Not represented as a newly exhaustive full-paper reanalysis.
- PMID:355220: Original scanned abstract, methods and critical discussion sections inspected through OCR for Sr41 lineage and unresolved later aminoacetone route.
- PMID:1917830: Original p5944 and p5948–5950 critical reporter/regulation text and tables through OCR; original p5948 Table2 visually inspected.
- PMID:1729203: Original scanned Methods and Results pp109/112, Fig4/5 and p113 Fig6/Discussion opening inspected through OCR, along with abstract. Reporter and transport context supported; no claim of a new full-paper review of every remaining paragraph.
- PMID:6780553, PMID:2007567, PMID:12097162, PMID:9048544, PMID:8647101, PMID:12754220, PMID:26239124, PMID:19656291, PMID:34767760, PMID:8521047: Bound EuropePMC abstract/metadata originals inspected. Native UniProt/EcoCyc source assertions inspected separately. No claim that corresponding complete papers or experimental tables were directly inspected.

## Limitations and follow-up

- This review judges the source-defined complete record; it does not demonstrate full physiological route flux or establish the hypothetical E. coli terminal catalyst.
- Full paper inspections versus critical sections versus abstract/native-annotation evidence are explicitly separated. Tdh2012 supplement remains unavailable; YiaY and historical transporter full assay sequences remain unreported/unestablished.
- No independent replay of all author iModulon adapter calls, render/KGX generation, or duplicate whole-corpus gates.
- PathBank whole PWML is malformed; the original unchanged, hash-bound intact fragments support the interface only. Native attached child identity is not full child pathway chemistry.
- Source adapter implementation/adoption for PubChem78645 and attached PathBank child is parent-owned; exact issuing originals exist and pending adapter coverage is not classified as scientific false identity.
- Licensing assessment was explicitly deferred by parent/user scope. No source-exhaustion claim.
- No maintained files, shared caches, package installations, Git or GitHub mutations by reviewer. Issues #432 and #433 were created by parent under parent authorization.
- Absence claims used exact complete native objects and gitignore-independent searches; ordinary ignored-aware search absence was not used as exhaustive evidence.

Parent should track issues #432/#433, coordinate all supported author corrections in a successor external draft, then obtain independent re-review before maintained adoption. Preserve v6 and this immutable review; successful schema/replay alone cannot close the findings.

The JSON is the authoritative external review and contains exact input/source hashes, all111edge dispositions, remedies and acceptance checks. This bundle is not a maintained canonical review.

First captured audit checkpoint: 2026-10-12T00:50:56.517808+00:00; finished: 2026-10-12T00:59:24.005324+00:00. Earlier preliminary reading was not timestamped. Git base: `83acb13ef388fa854ce5d67e1cb275da70e3c870`.

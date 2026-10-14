# Next254 construct and supplement handoff

Author support only; no maintained edits or independent review verdict. All three official ACS supplements were read in full extracted text. All 24 non-title pages were visually inspected, including every figure, scheme, table and reference page. Title pages were text-inspected. Exact per-page scope and source hashes are in supplement-evidence-ledger.json. Raw PDFs, figures, article HTML and PDB files stay external.

## Decisive modern identity and exclusions

- The 2018 LigU supplement explicitly uses Q0KJL4. Its displayed 357-residue reference is KA1, despite SYK-6 in the article title. PDB 6P3J independently records the KA1 gene source, E. coli BL21(DE3) expression, and full Q0KJL4 sequence plus C-terminal LEHHHHHH. The PDB difference table explicitly calls these eight residues an expression tag. 6P3H has the same tag plus K66M.
- LigU reference sequence, deposited sample sequence and crystal-ordered residues are different quantities. In 6P3J, chain A has ordered residues 8–360; chain B has gaps. The 2019 supplement's omission of beta strand 16 from an alignment is not an expressed truncation. See pdb-construct-projection.json for exact ranges and hashes.
- LigJ Table S2 identifies the studied reference as SYK-6 Q9KWL6, now G2IQQ5. PDB 6DWV's 341-residue entity exactly matches that issuing native sequence. 6DXQ matches native residues 2–341. 6DXS has those residues with E284Q and terminal LE. These deposited differences do not prove the tag state of all kinetic assays.
- Modern LigU/LigJ chemistry uses KCH. Do not attach those enzymes' modern catalytic evidence to legacy CHM tautomerase/hydratase reactions. The LigJ supplement supports reversible KCH hydration under its stated assay conditions. Its Scheme S1d has no stereochemical wedge; absolute S is a product-bound structural assignment, not an independent NMR determination.
- The nonenzymatic OMA-to-KCH observation is restricted to approximately six hours, pH 9.7 and the reported LigI-containing mixture. It does not establish generally spontaneous physiological flux.
- LigJ supplement Figure S6's caption calls the ligand-free illustration 6DXQ, while Figure S1 connects the relevant ligand-free view to 6DWV. This source discrepancy is preserved rather than silently repaired.

These facts support explicit exclusions and source boundaries for a legacy native P184-PWY graph. They do not force a single-strain graph or authorize replacing native reaction identities.

## Additional primary construct progress

The complete PMC article bytes for PMID22475079 (LigI), PMID23977959 (LigAB), and PMID12486039 (LigK) were legitimately recovered. I inspected their relevant expression and purification methods; the component ledger reports the precise narrower read bounds and does not claim full visual review.

- LigI 2012: codon-optimized O87170, pSGX3(BC), encoded MSL–PCR product–EGHis6. Purified unlabeled material lacked the initial methionine by mass spectrometry. Separate SeMet crystallography must not be generalized to the kinetic preparation.
- LigAB 2013: synthetic native-reference ligAB in pET15b; LigA initially N-His tagged and LigB untagged. Anaerobic preparation includes thrombin tag removal; aerobic preparation retains the tag. Exact cleavage scar is not established by the inspected prose.
- LigK 2003: native ligK fragment in pETK/pET21(+), expressed in BL21(DE3), with chromatographic purification. Measured N-terminus matches native LigK except initial methionine. This paper explicitly measures both CHA aldolysis and OAA decarboxylation and subtracts spontaneous OAA background. Its statement about the physiological l-CHA substrate is tentative. The AB073227 full-CDS/current-protein comparison was sent to the native-evidence agent and remains outside this handoff's completed work.

All proposed verbatim quote budgets are zero. No graph edges are proposed here because attaching them requires the route author's explicit source and endpoint choice. Suggested construct descriptions in component-construct-ledger.json are paraphrases for descriptions, not fabricated source_assertion evidence from prose.

## Access bounds

All three main modern ACS paper routes returned 403. The official OAKTrust item is fe380330-64dd-4b04-8ac7-edc5a89bf1aa, with public PDF bitstream 4debd50c-d6c5-49b7-b712-d21ea08e3971. Web retrieval reached the PDF but rejected its 32,253,519-byte size. Local standard retrieval returned a Cloudflare challenge, and no browser is available. I did not solve or bypass a challenge, pay for access, or attribute main-method claims to these failures.

An initial unverified trial item UUID in acquire.py was unsuccessful and is not an authoritative source. Likewise trial PMCID151511 proved unrelated to LigK and is explicitly excluded. The correct LigK accession was recovered from issuing PMID metadata as PMC141877 before its article was used. A GenScript page with a brief methods excerpt and a chemical-vendor mirror were search leads only, not scientific evidence.

## Compact retention

Retain HANDOFF.md, supplement-evidence-ledger.json, component-construct-ledger.json, pdb-construct-projection.json, original-bindings.json, and acquisition JSONs as useful. Helpers may be retained exactly as .py.txt, not active research Python. Do not commit originals/, rendered/, extracted article text or the full raw papers. The retention candidate manifest binds all compact outputs and explicitly records source read limits.

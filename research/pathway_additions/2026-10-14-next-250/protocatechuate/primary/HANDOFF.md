# Next250 primary evidence handoff

Author support only. No maintained files edited and no independent scientific review performed.

The 14-edge candidate `native-protein-edge-draft.json` has four native catalysts, five assembly memberships, one ferric cofactor edge, and four expression-induction edges. Chemical native IDs are handoff keys: the chemistry agent has closed protocatechuate as CHEBI:36241, 3-oxoadipate is CHEBI:15775, and ferric iron is CHEBI:29034. All referenced native XML byte hashes were checked before constructing the draft. Do not import the generic PcaB Rhea mapping: its chemical stereochemistry is broader than the native R-lactone route.

The catalysis evidence pointers were checked separately from each object's general citations. ENZRXN3343 evidence cites PMID 6273403; ENZRXN3366 cites PMID 4199895; ENZRXN3367 cites PMID 4199896; ENZRXN3368 cites PMID 7391022. The first draft mistakenly assigned ENZRXN3368's general older citation to its evidence slot; root caught this, and the external draft is corrected. This was an author error, not a native-data defect.

`claim-ledger.json` contains optional short exact quotations, actual source locators and access limits. Do not duplicate its quoted text into several maintained artifacts. `reading-coverage.json` distinguishes full original-scan readings from abstracts, partial rendered primary prose, metadata-only sources and failed downloads. `source-manifest.json` binds 42 artifacts, including all 18 original-page scans examined and every failed download. HTTP 403 payloads with a `.pdf` filename are HTML failures, not original PDFs. All originals and OCR remain external.

## Protein identities and assemblies

- Native CPLX2721 is the historical PHK four-alpha/four-beta/four-Fe model, supported by PMID 6273403's author abstract and inspected portions of original prose. It is not the ATCC 23975 enzyme. Native MONOMER3185 is beta; MONOMER3186 is alpha. Preserve these source-native identities.
- PMID 8407791 was fully read from nine original scans. Its ATCC 23975 preparation (formerly called P.aeruginosa) has an alpha12 beta12 structural model. The 12 iron sites do not establish 12 occupied sites: recombinant protein measured 8.4 Fe/enzyme, older native values 6–8. DNA accession L14836 differs from older chemical protein sequences at three residues. None of these sequences or measurements identify PHK monomers.
- CPLX2762 has four MONOMER3222 PcaB subunits. PMID 4199895 is metadata-only in this retrieval; use the inspected native component/evidence slots rather than imply its full original paper was read. PMID 1390752's author abstract establishes cloned pcaB, E. coli N4830 expression and membership in the class II fumarase family; it does not by itself prove all pcaBDC cluster details.
- CPLX2745 has six MONOMER3206 PcaC subunits. PMID 7391024's inspected author abstract supports a historical hexamer inference from 13.3 kDa equivalent chains; the 1973 source is metadata-only here. Do not transfer the related catechol-branch decamer or infer identical regulation in Acinetobacter.
- CPLX2761 has three MONOMER3221 PcaD subunits. PMID 7391022's author abstract and original rendered p 6336 discussion support the historical 11 kDa/30–33 kDa inference. Its complete miniprint/figure pixels were not inspected; prior 248 inspected selected preparation/mass-method prose. No exact sequence join to modern 263 aa KT2440 Q88N36 is established. Use source-scoped historical language.

## Regulation and cofactors

Native chemical induction edges mean expression induction in curated P.putida pathway context. They do not establish direct binding to the purified enzyme, acute catalytic activation, or measured regulation of every strain preparation. Native PcaHG is induced by protocatechuate; B/C/D by 3-oxoadipate.

PMID 8083169 was freshly read from all nine original scans. It supports PcaR-dependent pcaBDC expression in PRS2000. Table 2 directly measures PcaB, with activity 120→1850 mU/mg on glucose→glucose+20 mM adipate; two pcaR mutants fail induction. The gelshift assays use recombinant crude extracts and the pcaIJ promoter, not the pcaBDC promoter. The ligand-PcaR interaction is proposed, not measured: added 3-oxoadipate did not alter mobility(data not shown). PcaR stays research context because exact pairwise identity with the native purified B/C/D preparations is not established.

Salicylate induction in PMID 8407791 is an engineered nahG promoter effect, not natural PcaHG regulation. Ferrous ammonium sulfate in culture does not establish a catalytic Fe2+ cofactor. The native PHK cofactor is Fe3+; oxygen is a consumed substrate.

Native inhibitor slots are assay observations: PHK PcaHG chloride/fluoride/iodide/acetate; PcaB Cu2+/Ni2+/Co2+/KCl. Partial original 1966 text identifies 0.1 mM Ni/Co/Cu chloride inhibition of PcaB and distinguishes it from Mg/Mn stimulation of the catechol-branch enzyme. Those metals are not PcaB cofactors. No physiological inhibitory regulation is inferred. PcaC accelerates decarboxylation that can also occur spontaneously; spontaneous turnover is not evidence against its enzyme.

## Source defects and gaps

PMID 916393 is an unrelated prostaglandin/norepinephrine paper. Embedded PMID 761399 is the already-rejected human amniotic-fluid polyamine paper. Neither is graph evidence; no replacement PMID was guessed. The historical enzymes remain supported by their inspected native activity and composition assertions despite blocked full original ACS/JBC PDFs. This handoff makes no full-reading claim for those blocked papers.

Chari 1987 DOI 10.1021/ja00252a034 full 5514–5519 PDF remains inaccessible; only its first-page indexed abstract/start was read. The chemistry agent's exact native/authority molecular identity closure is the graph basis, rather than an invented full-primary stereochemistry appraisal. Its disjoint generic Rhea/KEGG map must remain excluded.

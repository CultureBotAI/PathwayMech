# Next264 biological issuing identity source preparation

This is a bounded source-author package for MetaCyc PWY-2503, not an independent scientific review or a pathway draft. All 13 selected native organism objects, 13 protein/complex contexts, and 8 genes have explicit identity decisions. Forty-seven public issuing requests preserved complete response bytes, final URLs, status, dates, headers, SHA256 hashes and byte counts. Sixty-three source-context files were reused from the frozen native and primary packages with original and manifest bindings.

The selected sequence proof covers 25 complete issuing protein sequences and 25 complete coding regions, including every one of the 17 protein/locus pairs explicitly listed in the 2025 primary article. Original nucleotide sequence was translated using the indicated genetic code and codon start, with strand and bacterial initiation handled explicitly. Every selected translation matches both the feature translation and the issuing protein. An isolated replay reproduces the result; `receipts/reproduction-and-preservation.json` gives the exact scope and hashes. Issuing sequences do not directly verify an absent native-frame sequence, physical complex composition, an assay construct, or a functional observation.

## Native decisions

`native-organism-identity-decisions.json` covers all 13 selected native organism objects. Nine native NCBI Taxonomy links resolve to their issuing identities and current ranks. The four native ORG contexts remain qualified:

- mt-2 retains native strain/preparation scope and a verified species-level Pseudomonas putida parent, NCBITaxon:303. A finite exact-name search did not establish a unique strain taxon.
- TW3 has the issuing candidate NCBITaxon:72271, Pseudomonas sp. TW3, under unclassified Pseudomonas. This conflicts with the native P. putida assignment; no automatic replacement is selected.
- Native NT4 remains distinct from the primary paper's printed 4NT. No identity is inferred from the transposed name.
- JMP222 retains MetaCyc:ORG-6075 and its unresolved lineage conflict: the native C. necator parent versus the comment describing a plasmid-cured C. pinatubonensis JMP134 derivative. JMP134, H16, historical 335, and B9 are separate contexts.

`native-protein-gene-identity-decisions.json` covers all 13 proteins/complexes, all 9 native component links, and all 8 linked genes. The four native mt-2 monomers have supported curated unification links to UniProtKB:P23099, P23100, P23101 and P23102. Their complete issuing sequences agree with the linked INSDC proteins and the original M64747 coding regions. The native gene identifiers remain selected; no unique active Entrez gene is inferred from a protein accession. Five native complexes remain native identities, and a subunit accession is never used as the identity of a whole complex. Embedded component-ledger `source_file` paths are relative to `source-context/native/`.

The JMP222 BenABC monomers and genes remain native-only identities. BenD's Q0KAB0 and Gene 4248800 links are explicitly Ortholog, not exact unification. Issuing Q0KAB0/CAJ93061.1 and its coding region belong to C. necator H16, NCBITaxon:381666. Gene 4248800 is discontinued; no successor is inferred. None of these establishes the identity of JMP222 BenD, the historical 335 purified enzyme, or B9.

## Sequence and source conflicts retained

`issuing-conflicts-and-exclusions.json` preserves six finite conflicts/exclusions, with exact original bytes:

- O85961 and O85988 are deleted/inactive UniProt entries. Their UniParc archives retain historical sequences; they do not reactivate the accessions or establish a replacement.
- The ADP1 related protein P07770 is BenB. P07771 is a 348-aa BenC sequence matching CAG68302.1; the older linked AAC46438.1 is 338 aa. Both versions match their own complete coding regions. Their equality is explicitly rejected. ADP1 is not historical A. calcoaceticus 73 or JMP222.
- P23099/M64747/AAA26047.1 is 454 aa. The current pWW0 RefSeq annotation WP_181408537.1 is 450 aa and matches residues 5–454 of P23099, lacking its initial MTMT. It is not silently substituted. The NC_003350.1 response is a contig annotation with feature translations, not an assembled DNA original. Three other current pWW0 feature translations match the other curated Xyl sequences. The 25 selected CDS checks all use actual original nucleotide sequence.
- The 1971 paper prints P. testosteroni 16 / ATCC 15668; current issuing taxonomy's exact collection-name match is Delftia acidovorans, NCBITaxon:80866. The modern assignment is held rather than silently renaming the historical preparation.
- The H16 ortholog and discontinued gene are excluded as exact JMP222 or 335 identities.

Additional native taxon conflicts and native reaction/activity preparation conflicts remain in their respective decision tables and the unchanged frozen native/primary handoffs. They are not repaired by sequence similarity or modern taxonomy names.

## Primary preparation boundaries

`primary2025-protein-identity-decisions.json` binds all 17 printed accession/locus pairs to complete issuing proteins and coding regions: 12 RW1 entries, three KT2440 control entries, and two B1 comparison entries. Accession verification does not turn the putative RW1 BenD into experimentally purified BenD, establish a unique physiological electron partner, or broaden heterologous complementation results. RW1, KT2440 and B1 retain separate organism and experimental scopes.

`preparation-scope-decisions.json` retains 14 preparation groups, including historical 335, B9, C-1, Acinetobacter 73, the other 1971 controls, mt-2, JMP222, H16, ADP1, TW3, NT4, RW1, KT2440 and B1. Species-level collection aliases are not unique strain sequence identities. Finite exact-name queries returning zero results are not global taxonomy absence claims.

This author read the complete frozen handoffs and ledgers, the identity-specific 1971 methods passage, the 2025 accession/locus paragraph, and the original 1972 first-page preview. The preview visibly identifies 335 for growth/purification and B9 separately as substrate donor. Full-paper scientific reading and its access limitations remain those of the primary source author: full 1971 PDF; full 2025 PDF and figures; 1972 transformed full text plus original first-page image, without a full raw PDF; 1971 PMID 4326771 title/metadata only. This stage does not claim a repeat independent full-paper review.

## Retention and remaining gates

Complete originals, request/response provenance, source-context bindings, decision tables, inert `.py.txt` helpers, and replay/preservation evidence are retained. `compact-retention-manifest.json` binds every pre-manifest artifact to its exact or lossless-gzip storage copy with original/stored hashes and byte counts. `artifact-manifest.json` binds every regular file except itself. Runtime caches are not part of this package. The earlier finite sequence helper failure on the annotation-only contig was preserved, then corrected without relaxing the requirement for DNA in all selected CDS proofs.

No maintained files, Git or GitHub state, frozen predecessor package, shared environment, or pathway draft was modified. This package does not assert candidate absence or source exhaustion. Root intake, the post263 merged baseline/corpus rebind, final source selection and independent review remain required before authoring and acceptance. Native-only and unresolved identity decisions are deliberate limits, not evidence that no issuing identifier exists.

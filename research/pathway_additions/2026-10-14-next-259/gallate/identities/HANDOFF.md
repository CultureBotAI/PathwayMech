# next259 primary-endpoint identity supplement

This is a bounded source-author supplement. It does not change or supersede the frozen native, primary, chemistry, or GalA packages. No maintained file, source authority, adapter, worktree, or GitHub object was changed. It supplies exact issuing evidence, candidate endpoints, exclusions, and remaining owner prerequisites; it is not an independent review or authority promotion.

## Results

**GalR and GalP identity is closed at the deposited-source level.** Fresh issuing UniProt, complete NCBI protein XML, and KEGG CDS entries agree exactly with independently translated ENA AE015451.2 CDS sequences:

| Component | Gene endpoint | Protein endpoints | Length |
|---|---|---|---|
| GalR | KEGG:ppu:PP_2516 | UniProtKB:Q88JX7; NCBIProtein:AAN68128.1 | 397 aa |
| GalP | KEGG:ppu:PP_2517 | UniProtKB:Q88JX6; NCBIProtein:AAN68129.1 | 410 aa |
| Deposited full GalB | KEGG:ppu:PP_2515 | UniProtKB:Q88JX8; NCBIProtein:AAN68127.1 | 258 aa |

The exact KEGG genes and their protein products are separate entities. In particular, GalR's reporter-supported transcriptional effect targets the **galB or galT gene/promoter context**, not GalB/GalT protein activity. Promoter-reporter evidence does not establish direct GalR binding at a predicted site. The primary author's mechanistic and preparation qualifications remain controlling.

Fresh complete KEGG CDS entries were acquired for all six coding loci PP_2513 through PP_2518. All six pass the strict `kegg-gene-flatfile` parser in the next258 code, which treats these IDs as genes. Existing `uniprot` and `ncbi-protein-xml` parsers also pass the exact newly acquired proteins. All three full GalB/GalR/GalP comparisons verify both KEGG nucleotide identity and amino-acid identity against the deposited chromosome; GalR/GalP also agree with the lengths in 2011 Table 1.

This deposited-reference agreement does not prove the sequence of every historical assay insert or every 2023 reporter construct. The 2023 paper's stated genomic template and strain remain source-specific; do not infer a sequenced plasmid insert merely from a reference-protein match.

## GalT gene endpoint remains an owner-shape prerequisite

Fresh `KEGG:ppu:PP_2519` is an issuing **gene/pseudogene** entry with symbol `gllT`, location 2867058..2867060, three nucleotides `ccg`, and no protein sequence. It agrees with the minimal current ENA pseudo-gene annotation. It is not a complete CDS or a reconstruction of the 2011 inactive 522-aa allele. The current strict CDS adapter correctly rejects it for missing required CDS fields; do not weaken that adapter or manufacture coding sequence.

The exact current query for `PP_RS13170` returned **Entrez:44144364**, explicitly discontinued, pseudo, and frameshifted. It fails the existing current-gene authority parser. Historical `PP_RS13150`, `PP_RS13155`, and `PP_RS13160` records (1045763, 1045766, 1045767) are likewise explicitly discontinued. Their retained locus annotations are historical evidence, not current authority approvals.

Fresh UniProt-linked GeneIDs **83680896 and 83680898** are a separate trap: the issuing NCBI records identify *Pseudomonas alloputida* strain **NMI24_14**, with LU682 loci, not KT2440. They are excluded as KT2440 gene endpoints even though one passes the generic source parser. Cross-references and shared WP protein accessions cannot transfer a strain-specific gene identity.

The requested native candidate lookup `G1G01-2703` returned a META 27.0 mirror HTTP 404 explicitly saying that object was not found in that KB. The canonical BioCyc page returned a challenge/non-authority document; the existing parser rejects it for lacking native META identity/title. Both originals are retained. This is a bounded failed lookup, not a claim that no GalT gene record exists anywhere.

For a maintained **GalR → galT transcription** edge, either a separately reviewed, bounded non-CDS gene/pseudogene owner profile is needed for the exact KEGG record, or the edge must remain in research until a supported exact gene endpoint is available. Such a profile must preserve gene versus CDS class, organism/locus identity, source provenance, and absence of an inferred translation. No implementation was authorized here. Never substitute the repaired GalT protein as a transcription target. The earlier repaired FN669140.1/CBJ94499.1/E8ZB61 proof is unchanged and does not solve the 2023 allele uncertainty.

## GalB: exact construct evidence and remaining inference

The inspected 2011 Table 1 row (publisher transcript line 204) states PP2515 GalB is **244 aa / 27.4 kDa**. Current AAN68127.1 and Q88JX8 are **258 aa**. The UniSave entry-version-1 original from 2003 has exactly the current 258-aa sequence, and all 105 retrieved history rows report sequence version 1. This is not explained by an observed UniProt sequence-version change.

Fresh PDB **5CGZ** complete mmCIF and polymer-entity JSON give a **240-aa crystal construct**. Its exact sequence is:

`initiating M + Q88JX8 residues 20–258`

The mmCIF explicitly calls the fragment `UNP residues 20-258`, aligns entity positions 2–240 to reference 20–258 and author positions 6–244, and separately labels entity residue 1 / author residue 5 as an initiating methionine. The raw CIF resolves an artifact hidden by the coarser SIFTS alignment beginning at reference position 19.

Current full residues 15–258 form a 244-aa sequence beginning `MNTPQ...`. This is a plausible short-form start. Removing its first four residues (full positions 15–18) exposes **Q19**; the crystal instead begins **M** followed by full positions 20–258. Thus the crystal involves an initiating-M junction as well as the reported truncation. Net length minus four does not prove a literal unchanged four-residue deletion or the exact 2011 plasmid sequence.

All eight 2016 primary mutant positions independently match the short-form numbering with a **+14 offset** in the deposited full sequence: A16→A30, R21→R35, E48→E62, R67→R81, H127→H141, Y123→Y137, H164→H178, R216→R230. These matches and the PDB author numbering support the proposed indexing relationship. They do not establish every residue of the 2011 assay insert. Preserve assay-specific native endpoints and distinguish 244-aa reported assay protein, 258-aa deposited reference, and 240-aa crystal construct. A complete original 2011 insert/primer sequence or exact deposited plasmid remains needed for definitive assayed-sequence identity. The 2016 methods state that relevant primers are available upon request; no contact was made.

`projections/GalB-construct-reconciliation.json` contains full sequences/hashes, exact comparisons, the historical original binding, all eight residue checks, and CIF locators. This supersedes no frozen artifact; it adds evidence to the previously unresolved discrepancy.

## All seven DesB2021 inhibitors retained

Every red inhibitor structure in supplementary Figure S1 was visually inspected and independently transcribed into a molecular graph. Full graph InChI/InChIKey, elemental formula, and total charge agree with both fresh issuing ChEBI JSON and pinned ChEBI data. Issuing SMILES also round-trip to the same full InChI.

| Primary compound | Exact chemical endpoint | Drawn charge |
|---|---|---|
| Protocatechuate | CHEBI:36241, 3,4-dihydroxybenzoate | −1 |
| 4-Nitrocatechol | CHEBI:16318 | 0 |
| Vanillate | CHEBI:16632 | −1 |
| 2-Methoxy-4-methylphenol | CHEBI:89886 | 0 |
| Syringate | CHEBI:132111 | −1 |
| Vanillin | CHEBI:18346 | 0 |
| Syringaldehyde | CHEBI:67380 | 0 |

The carboxylate forms follow the actual drawing, including its charge, rather than substituting acids or salts. Phenolic and nitro forms likewise follow the drawing. These identities do not assert a unique solution microspecies at assay pH or a common binding mechanism. The primary inhibition observations use **5 mM compound with 1 mM gallate and the synthetic DesB–MBP fusion**; they must not become unqualified claims about a natural unmodified DesB preparation. The exact synthetic fusion sequence is still unsupplied. High-gallate substrate inhibition uses the already-closed CHEBI:16918 endpoint separately.

The exact Figure S1 PNG was extracted from `word/media/image1.png` in the rehashed original DOCX. It was not edited. `projections/DesB-inhibitor-identity-closure.json` retains the independent drawing transcriptions, structural features, source hashes, pinned/current properties, and all checks. No inhibitor was dropped because it needed a new authority term.

## SYK-6 LigAB and DesZ addition

The later bounded request is also covered. The native SYK-6 complex is **MetaCyc:CPLX-7916**, distinct from historical Comamonas CPLX-2701. Its two native component slots name MONOMER-15116 (LigA) and MONOMER-15117 (LigB), with **no coefficients**. No stoichiometry is invented. Fresh issuing protein and original deposited nucleotide sequences independently agree:

| Protein | Native identity | Exact issuing identities | Length |
|---|---|---|---|
| SYK-6 LigA | MetaCyc:MONOMER-15116 | UniProtKB:P22635; NCBIProtein:AAA17727.1; M34835.1 CDS 78..497 | 139 aa |
| SYK-6 LigB | MetaCyc:MONOMER-15117 | UniProtKB:P22636; NCBIProtein:AAA17728.1; M34835.1 CDS 499..1407 | 302 aa |
| SYK-6 DesZ | MetaCyc:MONOMER-15115 | UniProtKB:Q7WYU8; NCBIProtein:BAC79261.1; AB110976.1 | 330 aa |

Native genes G-11551, G-11552, and G-11550 explicitly name ligA, ligB, and desZ and point to these respective products. Original ENA deposits retain the historical S. paucimobilis taxonomy and explicitly name strain SYK6/SYK-6. Current LigA/B UniProt records use modern Sphingobium SYK-6 taxon 627192; current DesZ retains 13689. Native META27 uses 502559. These issuing contexts are preserved, without asserting equivalence of every taxon identifier.

`projections/SYK6-LigAB-DesZ-identities.json` contains complete annotation/sequence bindings and independently translated CDS equality. `projections/SYK6-native-direct-slots.json` accounts for all **71 direct slots of seven supplemental native objects**, including alternative activities and full narrative locations. Previously acquired three native originals were independently rehashed against the next253 acquisition manifest before copying; DesZ and the three gene objects were freshly acquired from the same META27 mirror.

These exact reference-protein identities do not reconstruct all historical or later assay tags/vector residues. Kasai2005 pELAB and DesZ preparation contexts stay with that paper; the assigned 2013/2015 LigAB author owns the newly inspected preparations. Do not equate SYK-6 LigAB with Comamonas LigAB, transfer LigAB effects to DesB, or infer a specific gallate-to-OMA product equation solely from substrate-dependent oxygen consumption. The assigned primary author determines which activity/product claims the papers establish.

## Scope, provenance, and retention

`projections/authority-parser-inventory.json` inventories 36 candidate identifiers, including explicitly excluded candidates, against both point-in-time authority snapshots. Among the seven chemicals, only CHEBI:36241 is currently in those snapshots. The supported new CDS genes and new protein IDs also require selected source entries/terms. This inventory is not authority promotion.

Authority-directory enumeration used `rg --files --hidden --no-ignore`; all found JSON snapshots were fully parsed and hash-bound. This establishes exact-key coverage only. It is not a whole-repository absence search; binaries and archive contents were not searched and symlinks were not traversed. Root must refresh the inventory after next258 merge and final identifier choices.

`reuse-receipts.json` binds independently rehashed frozen native/primary originals before reuse. Fresh issuing originals remain under this supplement's `originals/`, including the initial NCBI 429 response, successful retry, failed native lookup, and challenge page. Initial sandbox DNS failures are retained in the acquisition receipt. No successful response overwrote a failure. All raw originals remain external; the compact manifest retains projections, ledgers, helper copies, and an original-file manifest.

Standard-library work used `/usr/local/bin/python3.11 -B`; parser checks used the requested project Python with next258 source on `PYTHONPATH`. Chemistry used the already existing next253 read-only RDKit environment because the project environment lacks RDKit. No environment installation occurred. An initial formula comparison detected RDKit's charge suffix convention; the corrected comparison removes only that suffix and tests charge separately, with every structural test then passing.

The outstanding list is bounded: exact 2011 GalB assay insert; supported galT gene/pseudogene owner shape; 2023 GalT allele; exact DesB–MBP fusion sequence; final authority extraction and record integration; and independent scientific review. Primary mechanistic evidence, activity-process endpoint identities, unrelated GalA reagent identities, and later LigAB assay-construct evidence remain with their assigned authors. No full-source-exhaustion claim is made here.

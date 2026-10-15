# Next260 biological identity and source-authority handoff

Candidate: **MetaCyc:GALLATE-DEGRADATION-I-PWY — gallate degradation II**. The accession suffix I and displayed numeral II are deliberately different. This is external source-author work, not an independent review, maintained authority update, record draft, or post-merge duplicate check.

The declared native identity scope is covered: **51 non-organism objects** comprising two pathways (the candidate and TCA interface), nine reactions (five formal and four adjacent), 25 proteins/complexes, and 15 genes. All six standalone native organism objects and the inline PDC isolate remain inventoried separately. Twelve pinned taxon identities cover native, reference, historical preparation, and expression-host contexts; they are not twelve whole-route occurrence assertions.

`projections/native-biological-identity-summary.json` provides every native identity, issuing-source option, direct gene/product/component/species references, source hashes and slot locators. `projections/component-reference-and-gene-dispositions.json` separates the 16 monomers, nine assemblies, 15 genes and their reference/preparation boundaries. All 21 native activity/preparation summaries and 26 native fact groups were read; their unresolved chemistry and experimental questions are not approved by this identity inventory.

## Authority candidates

Twenty-three native IDs already have maintained authorities and their owners are preserved exactly. Twenty-eight missing native IDs have concrete source descriptors in `source-config-proposals.json`. Including optional reference-sequence counterparts, that file contains **43 candidate source entries supplying 58 currently unretained identifiers**. These are options for the parent's eventual exact selection, not instructions to add every candidate. The 30 optional sequence identifiers must not replace source-scoped native components merely to obtain a resolvable accession.

Every proposal points to an exact external cache original with a SHA-256 binding. `source-cache/` holds symlinks to those verified originals. The base manifest and both authority snapshots are bound to the exact reviewed next259 commit **baf1f16f109dbdf6c2571e9c2ab70078ab4382ea**. A separate runtime copy contains 116 exact Git-blob-matched parser/schema/context files so subsequent branch cleanup does not change the research inputs. No maintained owner was written and no final union builder was run before record selection.

The actual strict parser replay covers **122 source profiles**. It preserves 28 rejected profiles and one inactive accession with no emitted authority term:

- The real candidate pathway HTML verifies its exact ID and title. `metacyc-pathway-xml` is mentioned in the copied builder's header, but its actual `source_terms` dispatch rejects that kind; this is recorded rather than claimed supported. No extension is needed because the genuine issuing HTML works.
- All 15 native genes have real `/gene?orgid=META&id=...` pages reached through their observed same-origin JavaScript redirects. Those complete issuing pages pass the existing HTML parser. The original short redirect bodies correctly fail and remain preserved; no synthetic HTML was created.
- MONOMER-3183's real gene page supplies its native name. Named MONOMER-3468 and unnamed homodimer CPLX-2864 pass their existing XML profiles. The latter's HTML redirect points to its monomer and is not accepted as complex identity.
- Named heteromer CPLX-2721 passes the direct-name XML profile; its four beta and four alpha components remain exact. Its identity is not collapsed to either sequence, and another strain's twelve-unit assembly is not substituted.
- Five native reaction XML objects pass the existing constrained identity profile. RXN-11861 has a common-name; three adjacent reactions have unsupported side shapes. Their exact rejections are recorded, and all nine real issuing reaction HTML pages independently identify the requested native frames. These identity options do not change the parent's five closed Rhea equations or add formal pathway members.

## Reference sequences and preparation limits

Sixteen complete original INSDC CDSs were translated independently using their exact coordinates and annotated bacterial code. Every translation agrees with its original `/translation`; every available selected UniProt/NCBI counterpart also agrees. Four additional native RefSeq/original GalD-GalC protein accessions were checked separately. Compact results are in `projections/reference-sequence-summary.json` and `projections/supplemental-reference-identities.json`; full sequence comparisons remain external.

| Native/reference group | Exact reference result | Boundary |
|---|---|---|
| BR6020 PmdE/PmdF/PmdD | AF305325.1 gives AAK73569.1 (342 aa), AAK73570.1 (227 aa), AAK73571.1 (305 aa); matching Q93PS9/Q93PS8/Q93PS7 sequences | This does not identify historical purified samples or turn PmdE sequence inference into direct catalytic evidence. |
| PmdF | The original BR6020 sequence equals current Q93PS8 | Current Q93PS8 names NCTC10698 `proA_3`. Sequence equality does not transfer strain-specific gene identity. |
| E6 PmdE | BAI50711.1 is explicitly Comamonas sp. E6, taxon364029; 342 aa | It differs from BR6020 PmdE at two positions. The 2016 E6 assay cannot be assigned to BR6020; tags/scars remain separate. |
| LigJ | Native Q9KWL6 is a secondary accession of G2IQQ5. AB035121.1/BAA97116.1 and AB073227.1/BAB88741.1 give the same 341-aa reference | Identity closure does not establish formal E,E-substrate hydration, nor the full 2018 tagged construct. |
| LigK | Native Q8RQW0 is a secondary accession of G2IQQ8; BAB88738.1 gives the matching 228-aa reference | Assembly and adjacent OAA activity remain source-specific. |
| LigI | AB015964.1/BAA33799.1 and AB073227.1/BAB88736.1 agree with O87170 (293 aa) | Native or recombinant preparation provenance still controls assays. |
| NGJ1 ProH/ProA | AB050935.2 gives BAB21455.1 (342 aa) and BAB21456.3 (227 aa), matching Q9AQI1/Q9AQI0 | The deposit names NGJ1 and records the historical P. ochraceae name; this does not identify an older unnumbered preparation. |
| ProL | Complete NGJ1 AB127969.2/BAD04056.1 gives 305 aa | Q75T30 is currently deleted and emits no authority term. The partial AB050935 ProL CDS is not substituted. Native historical ProL remains separate from its later cloned reference. |
| Entry alpha/beta components | L14836.1/AAB41025.1 and AAB41024.1 match P00436 (201 aa) and P00437 (239 aa) | L14836 names ATCC23975 in `tissue_lib`. This does not identify the anonymous 1975 enzyme gift or the separate 1982 B. fuscum/P. aeruginosa preparations. |
| KT2440 GalD/GalC/GalB | Exact AE015451.2 translations match Q88JY0 (361 aa), Q88JX9 (238 aa), Q88JX8 (258 aa). Native NP_744662.1/NP_744663.1 agree with the corresponding full references | The 244-aa reported GalB assay, 258-aa reference and 240-aa crystal remain distinct. The two native GalC-associated frames are not merged because they link the same modern sequence. |
| PDC-isolate hydrolase MONOMER-10723 | Native object and inline ORG-5956 PDC-isolate context are exact | No exact sequence is attached in the declared native object. Do not substitute purified PmdD, LigI or ProL or invent a strain-level NCBI accession. |

The Q93PS7 issuing recommended name literally contains `dicarbaxylate`. Its source label is not silently corrected. Native G-2284 and other gene frames remain usable exact native identities without promoting their historical crossreferences to current NCBI gene or strain equivalences.

## Taxonomy and source boundaries

The entire **14,115,225,600-byte pinned NCBI Taxonomy semantic SQL database** was independently hashed, with digest `89998447813e3151d1116222a3ec4b74959ccfb492114db134acee753f63548d`, matching the maintained 2026-07-12 owner. Twelve selected native term extractions and direct statements are retained in the taxon and supplemental projections. The historical SQL version/digest remains distinct from present-day navigation or taxonomy changes.

Native SYK6 taxon502559, historical S. paucimobilis taxon13689, and current reference strain taxon627192 remain separate source assertions. The pinned canonical name for taxon47882 is **Phytopseudomonas straminea**; P. ochraceae is a related synonym, not an exact canonical-label replacement. Native PDC has no direct NCBI strain xref in the inspected object. B. fuscum47914 and P. aeruginosa287 are preparation context options; E. coli562 is an expression-host option. None supplies whole-route occurrence by itself.

The 1975/1982, LigJ/ProH isomer, later tagged construct, native GalB kinetic-substrate/tag, and ProA preparation-code conflicts remain with the primary/native/chemistry authors. This package closes reference identity where evidence allows and preserves the remaining preparation gaps. It does not reinterpret primary chemistry, create experimental-sequence claims, or certify the pathway.

## Verification and retention

`verification.json` and its actual command receipt report success: 605 frozen/context bindings rehashed, 116 runtime files checked, all 122 parser outcomes replayed, all candidate cache hashes and selections checked, 15 native gene/product mappings accounted for, nine assemblies retained, sequence comparisons checked, and 57 public HTTP responses bound. HTTP 200 is never treated alone as authority acceptance. Initial sandbox DNS failures and the later ordinary public-network responses remain separate. An initial overbroad request selector was corrected before any request ran; its checkpoint explicitly preserves that scope correction.

`compact-retention-manifest.json` is a proposed allowlist of compact projections, receipts and inert helper copies. Full native XML/HTML, issuing JSON/XML/EMBL, full sequence projections, and runtime copies remain external. No transport cookie or authentication/session header is serialized in the public HTTP receipts. `artifact-manifest.json` binds the external package, while the originals manifest distinguishes raw external responses from successful semantic authority records.

Before drafting, the parent must perform a fresh ignored/hidden-inclusive whole-record duplicate check after next259 merges, select exact native/reference endpoints and preparation qualifiers, integrate the separate chemistry and primary dossiers, extract only selected authority terms, and obtain independent scientific and technical review. This author package supplies no approval, source-exhaustion claim, or license-release decision.

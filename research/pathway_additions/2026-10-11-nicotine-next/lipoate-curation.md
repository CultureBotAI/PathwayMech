# Lipoate biosynthesis and incorporation I

`MetaCyc:PWY0-501` is the complete native LipB–LipA route, retained as two reactions in `data/pathways/lipoate-biosynthesis-and-incorporation-i.yaml`. It begins with octanoyl-ACP and an unmodified target-protein lysine, and ends at protein-bound dihydrolipoyl state. Fatty-acid synthesis, LplA salvage, Fe-S cluster regeneration and downstream cofactor cycling are adjacent processes, not extra members of this native pathway.

## Identity and source disposition

The ignored- and hidden-inclusive pre-write search found 16 matches. Every match was inspected: previous screening/triage, this cohort's research, and two incidental numeric substrings. The prior thiamine handoff specifically identified the donor-label and carrier-state questions now resolved here. No maintained route record was found in the accessible worktree. This does not cover the original Documents checkout, which the OS denied access to. The Pseudomonas PathBank document names the same route in a different organism; it is not separately curated or represented as a second exact identity.

The full GO Semantic SQL label/synonym search and candidate definitions are retained. GO:0009107 denotes general formation of lipoate, while GO:0009249 denotes protein lipoylation without specifying this two-enzyme route. MetaCyc gives the exact named variant and does not collapse LipB transfer with LplA salvage or the Bacillus/yeast variants.

The raw PathBank member `PW002107.owl` was extracted from the independently rehashed archive. Its SHA-256 is `3207224ddd5d8c53293a0f827d63f03356fe49024c8afb2b416396ba9c142c86`. The primary member `SMP0002119` contains two biochemical reactions, 6136 and 6138. Its linked palmitate and SAM pathways are precursor context. Reaction 6136 labels its acyl donor acetyl-ACP, inconsistent with its octanoyl-transfer title and product; current LipB, primary experiments and native RXN0-947 all support octanoyl-ACP. The mistaken donor is rejected. Reaction 6138 uses old generic sulfur-carrier and ferredoxin bookkeeping, which is retained in the source projection rather than promoted as current chemistry.

## Chemistry and source versions

Native RXN0-947 explicitly unifies RHEA:17666; RXN0-949 explicitly unifies RHEA:16586. Both native pathway layouts select left-to-right, and RXN0-949 has RXN0-947 as its explicit predecessor. Rhea masters 17665 and 16585 explicitly link these directed members. All 17 chemical-side occurrences, their coefficients and whole carrier identities are retained.

The current LipA net reaction and the native 22.5 equation disagree in their formal redox convention. Rhea 142 releases four Fe(III), consumes two oxidized ferredoxins, produces two reduced ferredoxins and consumes four hydrons. MetaCyc releases four Fe(II), consumes reduced ferredoxin, produces oxidized ferredoxin and consumes six hydrons. Both retain octanoyl-protein to dihydrolipoyl-protein sulfur insertion and two SAM molecules. The record selects current Rhea's exact formal equation, documents the native disagreement on every affected chemical edge, and does not claim the selected electron balance has been measured physiologically. It does not silently flip a ferredoxin direction or merge the equations.

RHEA-COMP identifiers denote whole protein states, not their ChEBI reactive moieties. Carrier 14568 has **two** `rh:reactivePart` entries. An initial temporary audit that counted only the first showed a false residual of four Fe, four S and charge +2. Summing both retained native reactive parts gives zero atom and charge residual for both complete equations. The fixed audit checks every reactive part; no chemical coefficient was changed to force balance. The generic scaffold states are not asserted to identify an independently added IscU or NfuA enzyme.

## Proteins and evidence limits

Current reviewed UniProt P60720 and P60716 are E. coli K-12 proteins. Primary indexed abstracts generally describe E. coli; this is not relabeled as an independent measurement in every K-12 substrain. LipB's experimental FUNCTION and SUBUNIT assertions are distinguished from its HAMAP-only catalytic annotation. Active monomer and homotrimer alternatives are retained; the protein can catalyze transfer without inventing a stable complex accession. PMID:12591875 establishes direct transfer and corrects the historical truncated initiation assignment. PMID:16342964 supports a competent C169 acyl-enzyme intermediate and in-vitro reverse transfer.

Native CPLX0-782 contains two EG11306-MONOMER subunits, with explicit P60716 unification. The dimer is retained alongside the current UniProt monomer/dimer alternative. It is not claimed to be the uniquely required active assembly. The 2004 abstract's two-polypeptide mechanistic interpretation is qualified by the 2005 finding that both sulfurs derive from one LipA polypeptide. PMID:15362861 supports two distinct [4Fe-4S] clusters per subunit. CHEBI:49883 is a cofactor class; the formal oxidation states remain in the whole-carrier reaction nodes.

The two cytoplasm edges are explicitly HAMAP-inferred, not experimental fractionation. No direct LipA–LipB complex, obligate protein-protein transfer complex, or exclusive localization is invented. No inhibitor edge is copied from the LipA annotation without inspecting the relevant primary claim: PMID:15911379 is titled around biotin synthase, and was not used as direct LipA inhibition evidence. Omission does not establish the absence of regulation.

## Access and verification

Complete native XML, current full UniProt bodies, full Rhea 142 RDF and the original PathBank member remain outside the repository. The committed source manifests retain actual URLs, retrieval times, releases and body hashes. Changing Europe PMC response bodies were preserved under separate digest-suffixed filenames. PMID:15112987 was inspected and recognized as a commentary, not primary experimental evidence; it is not a record reference.

Primary articles were inspected as indexed abstracts. The attempted PMC148080 full-text endpoints returned HTTP 500 (Europe PMC) and HTTP 429 (NCBI BioC); no full-text result is claimed. The selected assertions are restricted to the inspected abstracts and authoritative structured records. Current iModulonDB gene searches returned lipA/lipB hits but no module-name hits; those results prove neither biological membership nor absence, and support no chemical edge.

The author replay checks the maintained YAML, every reference digest, native pathway membership/order, reaction cross-references, assembly crosswalks, source-family membership, all Rhea sides/coefficients and both full reactive-part balances. It is deterministic author validation, not independent scientific review. Shared authority integration, full gates, generated SVG/KGX audits and the saved independent review are tracked separately.

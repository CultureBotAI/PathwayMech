# next259 GalA and GalR evidence successor

This external author supplement resolves the previously staged evidence grammar for GalA2005 treatment/assembly findings and two GalR transcriptional targets. It changes no frozen source package, maintained record, authority, schema, worktree or GitHub object. It is not independent scientific approval.

There are **13 complete edge proposals**: eleven GalA edges and two GalR edges. **Twelve are insertion-ready author proposals** with exact issuing endpoint choices; the GalR→galT proposal still requires the separately reviewed gene/pseudogene authority owner. All thirteen pass the current repository's edge/evidence/qualifier shape checks. “Insertion-ready” does not mean authority promotion, a complete validated pathway record, or scientific acceptance.

## How to integrate

Use `author/gala-replacement-proposals.json` **instead of** the frozen GalA child P01–P12 selection. The old native-composition P03 and experimental-assembly P12 are merged into one qualified assembly edge. Appending the old selection would duplicate claims and exceed the paper-wide quotation allowance.

The proposed GalA set includes catalysis, native iron cofactor, predominant trimeric assembly, EDTA/dipyridyl/peroxide inhibition, Fe/Mn/Cu/Co rescue after chelator treatment, and sodium-ascorbate rescue after peroxide treatment. The conditional weak metal results are all retained. No individual numerical result is invented for ferric citrate, magnesium, zinc or nickel merely because the methods list them.

The actual purification **Table 1 title and row** support the narrow recombinant-preparation qualifier. The table does not assert processing, pretreatment effects, rescue or assembly. Full source-specific conditions and apparent Met processing remain in the corresponding edge descriptions, with exact result/protocol locators; short verbatim result excerpts supply effect evidence. No prose is relabeled as a structured source assertion. `author/evidence-allocation.json` states these boundaries explicitly. The native iron-cofactor annotation remains native-scope; it does not acquire an unnecessary assay-specific qualifier.

GalA's source-native complex/monomer remain `MetaCyc:CPLX-8177` and `MetaCyc:G1G01-2702-MONOMER`. They are not replaced by obsolete 340-aa Q88JX5. ENA's 420-aa encoded chain, apparent 419-aa processed protein, unknown complete recombinant terminal sequence, and predominantly rather than exclusively trimeric preparation remain explicit. The 2005 late product analysis does not independently resolve the immediate keto/enol reaction product.

## Exact endpoint choices and remaining prerequisite

The fresh issuing records support hydrogen peroxide `CHEBI:16240`, copper(II) `CHEBI:29036`, exact 2,2′-dipyridyl `CHEBI:30351`, and the sodium ascorbate salt `CHEBI:113451`. Native `MetaCyc:CO+2` explicitly gives cobalt(II) InChI/SMILES; its uppercase CML atom label is not silently treated as a conventional element symbol. Existing native chemistry supplies iron(II) `CHEBI:29033` and manganese(II) `CHEBI:29035`. Salt delivery in the methods is retained separately from metal-ion identity. Named-reagent mapping does not claim that the paper analytically measured purity or stereochemistry.

**EDTA uses `CHEBI:4735` as a proposed canonical named-parent normalization**, at root's explicit direction. Its issuing synonyms include EDTA and the chelating-agent name, but its structure is the neutral parent acid. The edge therefore says that the assay salt and protonation form were unspecified and that this normalization establishes neither a neutral-acid assay microspecies nor salt, charge or stoichiometry. Independent scientific review must judge this documented choice. Form-specific `CHEBI:64755`, `CHEBI:42191` and `CHEBI:64734` remain rejected as unsupported assignments for the assay. The full pinned-graph lexical scan and four live options are retained in `projections/EDTA-authority-options.json`; broader chemical-class substitution is not proposed.

`author/galr-proposals.json` keeps protein-to-gene transcriptional control distinct from protein activation. The exact regulator is `UniProtKB:Q88JX7`; galB is `KEGG:ppu:PP_2515`. The positive sign is inferred from the promoter–RFP reporter comparison, including the extra plasmid galR copy, endogenous GalR in promoter-only controls, 1.25 mM inducer, 6 h and LB/MM conditions. This is not a direct measurement of native target RNA, GalR occupancy or ligand binding.

The galT target is exactly **`KEGG:ppu:PP_2519`**, a current three-nucleotide gene/pseudogene entry. Its transcriptional evidence is ready, but the existing single-CDS authority correctly rejects that owner shape. Root is independently handling a bounded gene-only profile. This supplement does not approve that implementation or substitute repaired GalT protein, a discontinued Entrez gene, or a gene from another strain. Full 2023 GalT insert identity remains unresolved.

## Corrections to frozen research locators

`author/frozen-primary-errata.json` is append-only:

- Main 2023 Table 1 contains biosensor response parameters, not construct components. SI S3 has only host-strain rows; S4 has primers. This corrects G23-01 and G23-12.
- The 1.25 mM KT2440 GalR/promoter comparison uses **SI Figure S2**, not S4; this corrects G23-02/G23-03 locators. S4 concerns a broader 5 mM construct comparison with important replicate/transformation limits.
- G23-04/G23-05's broad S3–S5 locator is refined: main Figure 4 supplies the E. coli reconstruction; S3 is C. necator, S4 is KT2440, and S5 is specificity. The prior mechanistic inference and allele limitations remain.

The original PDF member was checked against the saved supplement archive, and SI pages 3, 5 and 7 were visually reread against the frozen image hashes. No frozen ledger was edited.

## Quotation budget, validation and retention

`quotation-audit.json` counts every selected placement, including repetitions: **25 words for GalA2005 and 20 for the 2023 biosensor paper**. Exact excerpts were replayed against retained source text. The audit stores quote hashes rather than another copy of the quotations. Short numerical excerpts remain dependent on the specified ordered metal list and source context. Root must audit the eventual combined record across all author packages; this selected set replaces prior GalA quotations and adds no words to other papers.

`verification.json` binds the exact current main schema/skill bytes and records all thirteen successful edge-shape checks. It also rehashes every file listed by the frozen primary, GalA child, native and primary-identity compact manifests, and rechecks direct native slots, the actual purification-table row and quote exactness. Whole-record gates, final authority extraction, independent review and lifecycle actions are outside this author task.

`source-bindings.json` retains exact source paths, hashes and frozen-manifest links. Reused originals remain in their original frozen external packages. Eight new issuing ChEBI originals and the authority-discovery web transcript are retained here, with acquisition timestamps and the initial sandbox DNS failure receipt. No successful original was overwritten. The GalA complete raw PDF and complete figure set remain unavailable; the table/main-text evidence is the retained author-uploaded web transcription, not purported publisher-PDF bytes. The frozen parent package's earlier overwritten-HTML integrity limitation remains unchanged; stable PMC XML, SI and relevant images are still reproducible.

`artifact-manifest.json` is the compact retention allowlist. Helpers are retained as inert `.py.txt`; raw source responses remain external and are hash-bound by `external-originals-manifest.json`. No claim is made that all possible source identities or public literature have been exhausted. The EDTA query covers every matching label/synonym row in the pinned SQLite graph, independent of gitignore; it is not a whole-repository absence assertion.

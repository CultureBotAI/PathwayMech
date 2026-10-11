# Adenine and adenosine salvage III

The target is `data/pathways/adenine-and-adenosine-salvage-iii.yaml`, with exact native identity **MetaCyc:PWY-6609**. It represents the complete four-reaction adenine → adenosine → inosine → hypoxanthine → IMP route in *Escherichia coli* K-12. It includes every reaction and material dependency in this native definition, not just the final phosphoribosyltransferase reaction. Native/source facts, including nonselected facts, are preserved in `adenine-salvage-source-projection.json`.

## Identity, novelty and boundary

PathBank:SMP0002081 (`PW002069.owl`) is the discovery lead. Its legacy label “Adenine and Adenosine Salvage I” cannot be transferred literally to current MetaCyc: native PWY-6609 calls this four-step chemistry salvage III. Fresh P121-PWY XML instead defines current salvage I as a different adenosine/adenine/AMP route. PWY-6611 includes an inosine-kinase alternative. The nearby legacy PathBank salvage III graph also differs; labels alone do not identify equivalent pathways. The chosen identity is grounded in the exact native reaction membership and ordering and independently retrieved canonical native HTML.

GO:0006166 describes purine ribonucleoside salvage broadly; GO:0006168 and GO:0006169 describe production of adenine and adenosine, respectively. None defines this entire adenine-to-IMP variant exactly. GO:0010140 is obsolete. The exact current native pathway identifier therefore remains the record identity.

Hidden and ignored files were searched in both the owned worktree and original Documents checkout, with only `.git` administrative and `.venv` runtime directories excluded. Exact identifiers, names, reaction names, proteins, papers, GO candidates and native KEGG cross-references were searched. All 189 baseline YAML identities were inspected programmatically. Inventories and source bundles contain this lead; no baseline record covers the exact four-reaction route. Existing guanine salvage and purine deoxyribonucleoside degradation share enzymes and some chemistry but differ in starting compounds, ribose/deoxyribose scope and endpoint. Their prior dossiers were examined; no existing rejection of the selected exact pathway was found. This conclusion is bounded to the documented repositories and sources, not a whole-computer or all-pathways absence claim. The reproducible search ledger records outputs and dispositions.

## Complete chemistry

| Native reaction | Exact selected direction | Material transformation |
| --- | --- | --- |
| ADENPHOSPHOR-RXN | RHEA:27644, right to left in family 27642 | Adenine + alpha-D-ribose 1-phosphate → adenosine + phosphate |
| ADENODEAMIN-RXN | RHEA:24409, left to right in family 24408 | Adenosine + water + hydron → inosine + ammonium |
| INOPHOSPHOR-RXN | RHEA:27647, left to right in family 27646 | Inosine + phosphate → hypoxanthine + alpha-D-ribose 1-phosphate |
| HYPOXANPRIBOSYLTRAN-RXN | RHEA:17975, right to left in family 17973 | Hypoxanthine + PRPP → IMP + diphosphate |

Native xrefs 27645 and 27649 are bidirectional members, not directionalReaction objects. The graph explicitly bridges those native identifiers through their Rhea masters to 27644 and 27647. Every directed side is independently extracted from the original release-142 RDF, including its side URI, participant, compound and `contains1` coefficient. Seventeen sides and four individual elemental/charge balances pass. ChEBI formulas and charges independently agree. Phosphate and ribose 1-phosphate cancel over the complete route, as do the three internal purines; the retained net is adenine + water + hydron + PRPP → IMP + diphosphate + ammonium. This algebraic net does not replace the four reactions.

The full native PathBank document independently corroborates the four transformations (6047, 6049, 6050, 6052). Its generic/older chemical protonation descriptions are not asserted to be exact chemical matches to every Rhea charged species. The projection retains those original objects. PathBank's additional PurP transport event is context outside the selected MetaCyc metabolic boundary. Reviewed P31466 now names this transporter AdeP; no transporter absence or unsupported membrane-crossing edge is asserted.

## Catalysts, assembly and evidence scope

DeoD (P0ABP8; b4384) catalyzes the first and third reactions in the opposite orientations required by this route. Native DEOD-CPLX contains six DEOD-MONOMER copies, whose identity explicitly bridges to this accession. Reviewed reversible activities and the 2018 full primary structural study support the homohexamer. The native six-subunit complex, rather than an isolated monomer, is the catalyst. These directions do not establish dominant flux under every condition.

Add (P22333; b1623) supplies adenosine deamination. Its reviewed activity, native enzyme-reaction object and historical K-12 genetics agree. The native apparent mass from gel filtration does not establish a multimeric assembly, and the record makes no measured assembly or monomer-sufficiency claim. Its one-zinc-per-subunit annotation is explicitly **HAMAP ECO:0000255 inference**, not a direct E. coli metal-binding result. Calcium in an old dialysis buffer is not a cofactor edge.

Hpt (P0A9M2; b0125), native CPLX0-7685, is the hypoxanthine-preferring homotetramer. Gpt (P0A9M5; b0238), GPT-CPLX, also catalyzes IMP formation with lower affinity for hypoxanthine than guanine. Both native four-copy compositions and monomer-to-accession bridges are retained. The graph does not claim equal flux through these alternatives. Hpt magnesium is a curated ECO:0000305 assignment with primary abstract structural support; Gpt magnesium has ECO:0000269 attribution and an explicit Mg/Asp89 structural observation. Neither is assigned an invented per-complex metal count. Hpt inhibition by its local product IMP is retained from reviewed experimentally attributed annotation, without extrapolating a cellular effect size.

Gpt's older gel-filtration apparent trimer (PMID:6305942) differs from later structural tetramer evidence (PMID:9100006) and current reviewed annotation. The record selects the tetramer and explicitly preserves the historical discrepancy; no unobserved condition-dependent explanation is invented. Native alternative PpnP/XapA and cross-species enzyme listings are retained in the source projection. This is the complete supported DeoD/Add/Hpt-Gpt route, not an exhaustive catalogue of all enzymes that can accept the same compounds. Additional substrate activities, synthetic inhibitors and broad transcriptional regulation do not become extra pathway steps.

Each of the four protein records supplies a cytosol annotation with IDA:EcoCyc attribution. DeoD membrane annotation is HDA:UniProtKB; Gpt plasma-membrane annotation is IEA:UniProtKB-SubCell. Their original tiers remain explicit. These annotations establish neither exclusive localization nor whole-pathway placement in a membrane.

## Primary inspection and organism limits

The original seven-page 1975 article (PMID:765747, DOI:10.1007/BF00269424) was obtained as a real PDF, extracted, read and rendered. Figure 1 and Table 1 were visually inspected. The route is shown in a broader purine map; genetic comparisons and the Figure 3 caption link the phosphorylase/deaminase route to adenine utilization in specified mutants. Table 1 identifies K-12 derivatives, not MG1655. The reviewed proteins also have taxon 83333, whereas native MetaCyc points to MG1655. Accordingly the record uses **K-12**, without representing those older experiments as MG1655-specific results or transferring all branches in that figure into this pathway.

The 2018 full BioC body (PMID:30337572, PMC6193948) independently supports the DeoD hexamer and recombinant enzyme scope. Exact locators are zero-based passages 40 and 63, with the actual subsection names. Author finalization corrected an initially imprecise Methods subsection label before independent review; the mechanism did not change.

Primary abstracts were inspected for Hpt structure (PMID:12070315), Gpt structure (PMID:9100006), historical Gpt preparation (PMID:6305942), Gpt kinetics (PMID:3886014), DeoD preparation (PMID:235429) and Add characterization (PMID:1998686). Hpt full text was **not** obtained: the BioC HTTP-200 body was an error document and was rejected; the official PDF endpoint returned 403. PMID:357905 has indexed metadata but no retained abstract, and its publisher endpoint returned 403. Claims attributed to these reviewed UniProt comments are not presented as direct readings of unavailable full papers. Exact metadata, body hashes and unsuccessful access dispositions are in the manifest.

Raw PDF extraction/rendering used the external cached runtime `uv run --offline --no-project --with pypdfium2 --with pillow python`; no repository dependency was added. The source PDF, extracted text and page images remain under the external raw directory.

## Expression context and completion

The shared current iModulonDB adapter queried the E. coli `precise_mg1655` dataset. Exact deoD, add, hpt and gpt gene hits were checked. Component 43, Purine, contains add/b1623/P22333 (weight −0.167619077, threshold 0.065168134). This is computational expression context only, not direct catalysis or regulation. Alias/subsequence results such as gpp or unrelated add/hpt substrings are not protein identity. The shared context, source manifest and successful parser replay are separate cohort artifacts; none is used to manufacture a mechanistic edge.

The complete author replay reads the original source bodies, full Rhea RDF and SemanticSQL authorities, verifies native/closed schemas, all named canonical labels, assemblies, source hashes and exact chemical sides, and serializes the actual KGX output. It checks all 30 nodes, 42 edges and 73 evidence blocks, including reference metadata and locators. The validation receipt preserves actual command outcomes, including initial helper-formatting failures corrected before final replay. Root performs integrated authority/gate/publication work; a different agent performs the scientific review. No unresolved scientific gap requires truncating this route.

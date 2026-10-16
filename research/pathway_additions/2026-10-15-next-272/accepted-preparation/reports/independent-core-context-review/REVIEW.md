# Independent next272 core identity and transcriptomic context review

**Qualified acceptance for finite source preparation. No actionable defect was found in either frozen packet.** This review accepts the supported identity, chemical-equation and bounded expression-context conclusions described below. It does not approve a maintained pathway record, authority adapter, whole-route strain flux, primary-paper interpretation, or completed biological component graph.

Reviewer: `/root/next272_core_and_context_review`, independent of the core-packet author and the root-authored iModulonDB packet. Only this new scratch owner was written. Source owners, maintained files, Git/GitHub, installed adapters and runtimes were unchanged. No background processes were launched; all calls are terminal.

## Inputs and integrity

- Core packet: `/private/tmp/pathwaymech-next-272-core-identity-preparation`, manifest SHA256 `67f29b62064d86886bfc0767a42c2ee08a8b444045242ed7e4d1b4e398dc8e57`; 399 listed files and 401 physical files.
- Context packet: `/private/tmp/pathwaymech-next-272-imodulondb-preparation`, manifest SHA256 `faeb80b7709f36e6544b059f10700f22e545aa87e58b2cfc371a0be474a2e4dd`; 67 listed files and 69 physical files.

`packet-intake.json` verifies both complete physical inventories, including hidden and ignored files, and every listed size/hash. The final input recheck establishes that both frozen owners stayed unchanged. The 1,525 successful checks comprise 470 intake checks, 301 core checks, 368 Rhea checks, 134 context checks and 252 provenance/secondary-alias checks. These counts describe finite checks; they are not a claim that every biological statement in the source bodies was scientifically reviewed.

## Native pathway identity and chemical boundary

The direct full META object is `PWY0-1477`, named ethanolamine utilization. All 23 native direct objects and their 583 own slots reproduce the author projection exactly. The root itself has 21 own slots; “core 20” means 20 identities, not 20 root slots. The five member Reactions, all four order relations and all five pathway layout directions were extracted from the original root. Both the acetyl-CoA/acetate branch and the ethanol branch remain present. The direct source taxa are MG1655 and LT2; the separate bacterial taxonomic-range statement does not demonstrate complete-pathway activity throughout bacteria.

The independently acquired ECOLI counterpart has the same five-member list, ordering and traversal directions, but belongs to its MG1655-specific PGDB. That supports shared source topology, not unconditional equivalence of the whole cross-species pathway. The inspected GO:0046336 definition is broad ethanolamine catabolism. The returned KEGG M00092/M00093 definitions concern phosphatidylethanolamine biosynthesis. Withholding those as exact aliases is justified.

Each full native Reaction lacks its own common-name slot. The fallback to the native frame ID preserves issued identity; a nested activity name must not be presented as an issued Reaction common name. This finding is bounded to the five complete originals, independently parsed with all hidden/ignored packet files included in the inventory.

The selected equations are:

| Reaction | Pathway direction | Selected species and coefficients | Directed Rhea |
|---|---|---|---|
| ETHAMLY-RXN | L2R | ethanolaminium → ammonium + acetaldehyde | 15314 |
| ACETALD-DEHYDROG-RXN | L2R | acetaldehyde + CoA(4−) + NAD(1−) → acetyl-CoA(4−) + NADH(2−) + H+ | 23289 |
| PHOSACETYLTRANS-RXN | L2R | hydrogenphosphate + acetyl-CoA(4−) → acetyl phosphate(2−) + CoA(4−) | 19522 |
| ACETATEKIN-RXN | R2L | ADP(3−) + acetyl phosphate(2−) → ATP(4−) + acetate | 11354 |
| ALCOHOL-DEHYDROG-RXN | R2L | acetaldehyde + NADH(2−) + H+ → ethanol + NAD(1−) | 25292 |

All 22 material occurrences are unit coefficient and unlocated in the source Reaction objects. Independent atom and charge sums balance for every equation. ETHAMLY alone has an own LEFT-TO-RIGHT assertion; the other four own assertions are REVERSIBLE. The pathway layout selects a traversal, not a measured flux or thermodynamic proof. Adding one copy of each branch equation is not a justified whole-pathway physiological net.

## Concrete species and source conflicts

All 14 native material identities independently agree with the selected ChEBI issuer response on complete InChI, InChIKey, molecular formula and formal charge. The ChEBI structures are concrete, not R-group structures. The selected molecular fields in the corresponding 14 MetaNetX pages agree as well. Equality of formula alone was never used to establish molecular identity; the exact InChI includes constitutional and stereo information.

Native CML SMILES have five real representation conflicts: ACETALD, ETHANOL-AMINE, NAD and NADH contain `[R]`; ATP contains `[a purine base]` and a shortened phosphate representation. The CML atom arrays inspected for those five have the expected nonhydrogen atom counts; the contradictory SMILES still must not become structure authority. The accepted molecular comparison rests on the explicit native InChI/key and formula/charge corroborated by ChEBI. Native monoisotopic mass, arbitrary unselected cross-references and all incidental chemical metadata were not accepted by this review.

MetaNetX also exposes standardized molecular representations that can neutralize species, and its cross-reference lists may combine protonation states. For example, the ethanolamine page lists both CHEBI:16000 and CHEBI:57603 while its selected original InChI represents the +1 species and its normalized SMILES represents neutral ethanolamine. This packet appropriately limits acceptance to specified concrete fields. Do not convert MetaNetX’s broad link collection, normalized strings or names into universal exact chemical mappings.

Native ETHANOL-AMINE is **CHEBI:57603 ethanolaminium(1+)**, C2H8NO. **CHEBI:16000 neutral ethanolamine**, C2H7NO, is its separately issued conjugate base. Both identities and the issuer acid/base relationship were checked directly. A primary EutH claim about uncharged ethanolamine cannot silently be attached to movement of the native +1 molecule. This review does not infer an acid-base step, a transporter substrate, or a physiological transport mechanism.

## Reaction comparisons and EC annotation

The selected Rhea source was independently decompressed from the hash-bound original compressed corpus. All 326,097 RDF descriptions in its 206,616,941 decoded bytes were scanned for the finite 66 selected subjects. All 88 selected fragments equal the original byte ranges, including their trailing newlines. Every repeated description of those selected subjects is retained. The incomplete first-description author projection remains superseded, and was not used as chemistry authority.

An independent graph join from selected directional reaction to reaction side, participant, unit coefficient and concrete ChEBI compound reconstructs all five equations exactly. It preserves the source bidirectional family IDs separately from selected direction members. Rhea’s own Approved status and chemical balance statements do not supply enzyme, compartment, strain or in-vivo flux evidence.

The five MetaNetX equations independently agree in concrete species and coefficients. ACETALD-DEHYDROG-RXN and ALCOHOL-DEHYDROG-RXN print opposite native left/right orientations; the other three agree. MNXD1 remains a generic model compartment. Two requested accessions are deprecated: MNXR95210 resolves through MNXR190510 to served MNXR190509; MNXR103319 resolves through MNXR188715 to served MNXR188714. The author’s detailed property ledgers preserve these chains. Future curation must preserve requested versus served identity rather than claiming an old accession is the current entry.

All five KEGG Reaction identities and the complete equation-compound files were inspected. Their named transformations correspond, but several chemical formula conventions differ. In particular, R00749 names neutral ethanolamine and ammonia where the native source uses ethanolaminium and ammonium. KEGG orthophosphate is represented as H3PO4, rather than native HO4P(2−). Withholding exact charged-equation mappings is justified; matching labels are insufficient.

The native ACETATEKIN-RXN annotation really is EC-2.7.2.15. The retained IUBMB originals distinguish propionate kinase EC2.7.2.15 from acetate kinase EC2.7.2.1 and explicitly allow acetate as a substrate for the former. Therefore the source acetate equation is not invalidated merely by that annotation. Preserve the specificity/annotation distinction; do not silently rewrite EC-2.7.2.15, introduce propionate as a route participant, or infer the identity of a particular catalyst from its EC class.

## Taxon and provenance limits

The exact NCBI objects establish MG1655 taxid 511145, parent K12 taxid 83333, rank `no rank`, and LT2 taxid 99287, parent 90371, rank `strain`. Native BioCyc calls both strain. Preserve exact strain names and the rank-model difference; shortening either node to a broad species identity would lose scope.

The copied UniProt P0AEJ6 response has K12 taxid 83333. Its CPZ-55 CAUTION is qualified with “may,” carries ECO:0000305 and cites PMID9278503; it is a curated inference about potential MG1655 operon expression interference, not a proof that all MG1655 flux is impossible. Conversely, the native MG1655 pathway association is not an experiment proving complete-route flux. K12 protein identity, LT2 experimental observations, reference annotation and exact experimental strain must remain separate.

Every retained receipt with a body hash has a matching exact body and size in the finite core packet. The six HTTP403 bodies and network-error receipts remain failures. The empty Rhea accession TSV response is not invalid-identifier evidence. The two older full XML objects ACETALD and Pi were separately compared byte-for-byte with their existing repository owner paths. The entire packet receipt directory, including physical hidden/ignored inventory, supplies no matching original HTTP receipt for those two bodies. Their documented repository reuse is valid; a new acquisition timestamp must not be invented. This is a packet-bounded provenance observation, not a claim that no historical receipt exists anywhere.

## iModulonDB context

The exact dataset response has 20 organism entries and 28 distinct dataset keys. Five E. coli keys and s_enterica/core match the prospective route’s organism context. Both `eut` and `ethanolamine` were actually searched in each, giving 12 command receipts. Eleven succeeded and each returned ten gene rows with zero component rows. Those finite tables do not establish complete gene inventories or absence of other matching components.

The remaining E. coli modulome/ethanolamine search failed with exit 2. Its exact API response contains component 76, named Fermentation, with a null regulator. The unmodified copied installed parser reproduces the same error when given that response. No adapter repair, null-to-empty conversion or network call was needed for this replay. Null does not mean biologically unregulated.

The installed summary command succeeded for `e_coli/modulome/76`. Its raw component response contains 13 rows marked members and threshold 0.105120952. The unchanged parser accepts those rows. Every rendered signed weight was compared with the original numeric value at the displayed precision. Relevant exact weights are eutJ 0.205927273, eutG 0.20032519, eutH 0.156945327, eutA 0.155496541 and ackA −0.171109794. The other returned functions include hydrogenase, fumarate, lactate and other metabolism; this is a mixed expression module, not an exact ethanolamine pathway definition.

Both signs are meaningful component weights, not reaction directions or evidence of activation/inhibition. The summary’s phrase “total genes scored: 13” is safely narrowed by the packet assessment to the complete **returned** table. No total underlying transcriptomic population was verified. STRING keys beginning 511145 and a dataset named precise_mg1655 establish reference-annotation context, not each culture’s genetic background or conditions. STM locus strings do not independently establish LT2 experimental conditions. The historical Salmonella EutG “putative transport protein” annotation is real and must not override current enzyme or primary evidence. In the raw component-gene response, `/genes/4/uniprot_function` for EutH/P76552 specifically describes protonated ethanolamine diffusion at low pH. Preserve that annotation conflict against any separately supported neutral-ethanolamine transport interpretation; the embedded string is not a newly inspected transport experiment. No mechanistic edge follows from this packet.

## Review operations, failures and remaining requirements

The final four independent review helpers replay successfully; their results remain in `core-results.json`, `alias-results.json`, `imodulon-results.json` and `provenance-and-alias-results.json`. All four helpers pass Ruff. The initial lint failure and formatting successor are retained.

Reviewer harness mistakes are preserved rather than converted into packet findings: the first MetaNetX parser expected `charge` rather than `global charge`; the early placeholder detector omitted ATP’s explicit `[a purine base]`; the first Rhea regex omitted the trailing newline while exact offset comparisons already agreed; the initial iModulon check expected a prose zero-result marker rather than the actual empty table and transcribed eutA’s exact decimal incorrectly; the first secondary-alias parser joined HTML sections across `<br>`. Corrected checks inspect the actual source representation and all pass. These errors affected reviewer checks, not frozen source bytes. Historical scripts/results are retained as `.py.txt`/versioned JSON and logs.

Reading included both complete packet assessments/handoffs, core provenance operations, exact selected native identity/equation sections, ChEBI structure and acid/base relations, MetaNetX molecular/equation/deprecation sections, complete selected Rhea graph statements, KEGG equation/compound fields, IUBMB identity/equation/specificity sections, direct taxon fields, the exact UniProt caution/evidence scope, all eleven rendered successful search tables, the failed-search raw response, all 13 raw summary rows and installed parser logic. No primary-paper main text, figure, supplementary experiment, enzyme/complex closure or transport experiment was reviewed here. No fresh network acquisition, whole-repository novelty search or unrelated archive search was performed. Physical inventories include hidden/ignored files. The Rhea scan is exhaustive only for the finite selected subjects in that exact corpus.

The review-yaml-record skill’s scientific rubric was used, but there is no maintained next272 YAML target in this task. Accordingly this is a source-preparation handoff, not a falsely completed canonical kind:record review. Full record gates, rendering/KGX, a governed record review and biological mechanism assessment remain required after curation. Actual verified PR #633 merged-baseline rebind remains a prerequisite before maintained curation or adapter work. Candidate/source exhaustion remains unproved.

**Actionable packet findings: 0.** The explicit scientific and provenance qualifications above must travel with any use of these packets. Native biological closure and primary evidence are separate ongoing preparations, and are neither accepted nor replaced by this review.

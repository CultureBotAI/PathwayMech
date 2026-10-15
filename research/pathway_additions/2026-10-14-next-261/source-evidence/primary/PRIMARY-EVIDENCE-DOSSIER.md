# PWY-5415 primary-evidence dossier

This dossier supports authoring **one connected five-step catechol degradation I record**, with its hydrolytic branch and shared terminal reactions kept together. It is an author research product, not an independent scientific review and not permission to infer one organism or preparation across different papers. All work was confined to this external temporary package; no maintained record, Git object or GitHub object was changed.

## Pathway scope

The native boundary is catechol ring cleavage → semialdehyde hydrolysis → dienol hydration → aldol cleavage → CoA-acylating acetaldehyde oxidation. Primary studies support individual enzymes, related genetic systems, substrate preferences and terminal enzyme association. They do not together demonstrate all five steps in one uniformly tested strain. The oxidative 4-oxalocrotonate branch is retained as experimental context; its tautomerase and decarboxylase are not extra reactions in this candidate.

The parent chemistry dossier owns exact chemical identifiers, reaction directions, stoichiometry and authority comparisons. The formal native intermediate is CPD-14447/CHEBI:67152 (2Z enol). Native prose also mentions the distinct 2E enol and keto compound; Rhea's hydrolase family describes the keto product. The primary preparations below do not erase those distinctions. An enol absorbance assay, a historical compound name, a racemic precursor, or E/Z labels on fluorinated inhibitors do not establish the stereochemistry of the native formal substrate.

## Mechanistic summary

The strongest direct terminal evidence is the native CF600 DmpFG preparation. Acyl-CoA product identification, copurification and subunit sequencing support associated aldolase and acylating dehydrogenase activities. The full 1993 methods and delayed-addition controls support **NADH stimulation**, with weaker NAD+ stimulation. They contradict the accepted biological reading of native REG-5876's negative sign. Mn2+ stimulates and Zn2+ inhibits this preparation, but unchanged basal activity after EDTA dialysis prevents an obligatory removable manganese claim from this experiment alone. The regulator target is complex-associated aldolase activity; direct NADH binding to DmpG was not demonstrated. Claims F01–F15 preserve the quantitative and negative observations. [Original publisher paper](https://journals.asm.org/doi/pdf/10.1128/jb.175.2.377-385.1993?download=true).

Assembly terms describe different levels. The 1993 apparent native mass supports two copies of each subunit. The inspected first two pages of the 2003 structure paper explicitly distinguish a biological tetramer of two DmpFG heterodimers from its catalytic pairs and the two tetramers in the crystal asymmetric unit. Later pages were not obtained, so the package does not claim a complete structural-paper reading. Claims S01–S03 retain this limit and identify introduction kinetics attributed to unpublished data. [Original structural paper](https://www.pnas.org/doi/pdf/10.1073/pnas.1236794100).

The 1989 XylIJ study distinguishes the hydratase-active dienol from the accumulating keto pool and unidentified chemical decay. It also reports XylJ activity without XylI, while isolated decarboxylase was unstable. The 2004 engineered-complex abstract therefore cannot justify universal dependence of hydratase on decarboxylase. The 1989 authors could not determine whether the hydratase's initial product was keto or enol; their hydrolysis-to-dienol statement cites Duggleby/Williams 1986 rather than reporting a new hydrolase product experiment. Claims H01–H12 retain preparation, rate, metal, tautomer and citation-layer distinctions. [Original XylIJ paper](https://journals.asm.org/doi/pdf/10.1128/jb.171.11.6251-6258.1989?download=true).

PKO1 tbu genetics supports the ring-cleavage and lower-pathway activities and conditional induction in specified clones. Most measurements used PKO1 DNA in a P. aeruginosa catA host. Noninduction by catechol or certain cresols is not inhibition or lack of enzyme substrate activity. The mapped seven-gene operon does not identify the terminal acylating dehydrogenase. Claims K01–K08 retain the donor/host distinction, extract activities and promoter controls. [Original tbu paper](https://journals.asm.org/doi/pdf/10.1128/jb.173.15.4587-4594.1991?download=true).

## Evidence table

| Source | Inspected material | Accepted use and boundary |
|---|---|---|
| PMID1856161, Kukor/Olsen 1991 | Complete 8-page publisher PDF transformed text | tbu genetics, extract activities, induction and promoter controls; donor DNA and expression host remain distinct. |
| PMID8419288, Powlowski et al. 1993 | Complete 9-page publisher PDF transformed text | Native CF600 terminal preparation, activities, metal/nucleotide effects, assembly evidence and assay limitations. |
| PMID2681159, Harayama et al. 1989 | Complete 8-page publisher PDF transformed text | Native XylIJ association, recombinant single-component experiments, tautomer preference and instability; no measured E/Z conclusion. |
| PMID12764229, Manjasetty et al. 2003 | Main pages 6992–6993 only,153 extracted lines | Biological 2+2 versus heterodimer distinction; later active-site/structure discussion unread. |
| PMID7890778, Díaz/Timmis 1995 | Complete indexed abstract only | XylF catalytic-triad evidence and F108M change; no full assay details or initial-product geometry. |
| PMID15301547, Johnson et al. 2004 | Complete indexed abstract only | Engineered E109Q/E111Q complexes and fluorinated-inhibitor experiments; no native inhibition extrapolation. |
| PMID17902707, Wang et al. 2007 | Complete indexed abstract only | YwhB in-vitro tautomerization and mutant effects; biological role unknown, no B. subtilis route assertion. |
| PMID2183008, Harayama/Rekik 1990 | Complete indexed abstract only | Historical pWW0 gene order/product sizes; xylT/xylQ unknown in that paper, not a present-day functional absence. |
| DOI10.1099/00221287-132-3-717, Duggleby/Williams 1986 | Publisher abstract and reference list | Hydrolase preparation properties; early dienol product experiment remains unread. This is not PMID3481421. |
| PMID3481421, Harayama et al. 1987 | Complete indexed abstract and publisher preview | Evolutionary gene-order context; no inspected enol-versus-keto experiment. |
| PMID4325686, Sala-Trepat/Evans 1971 | Bibliographic metadata only | Unread Rhea-cited historical lead; no experiment promoted to evidence. |
| PMID23237860, Fischer et al. 2013 | Complete PubMed indexed abstract only | MhpF monomer activity; native acetaldehyde Ki/mode not verified in primary detail. |

All three complete PDF text sets include methods, results, discussion, references, legible tables and figure captions. No figure was visually inspected: screenshot attempts supplied no usable page image. No raw PDF bytes were acquired. Hashes bind the exact web-transformed receipts or their reproducibly merged line text, never an imagined raw PDF. Each source's read scope and byte binding is in [reference-metadata.json](reference-metadata.json).

## Material evidence and dispositions

[material-claim-ledger.json](material-claim-ledger.json) contains 50 source-located assertions, including numerical assay conditions, negative observations, construct limits and explicit hypotheses. It is the detailed evidence owner. [material-conflicts-and-dispositions.json](material-conflicts-and-dispositions.json) provides cross-source decisions; no omitted contradictory native assertion is silently overwritten.

| Five-step route position | Primary claim anchors | What remains qualified |
|---|---|---|
| Catechol2,3-dioxygenation | K02, K03, K07 | Clone/extract evidence; no entire-route host inference. |
| Semialdehyde hydrolysis | K02, X01, X02, D01, H10 | Hydrolysis supported; exact initial-enol geometry unresolved in inspected preparation evidence. |
| Dienol hydration | H02, H05–H10, E01–E02 | Enol/keto preference supported; historical E/Z and initial-product tautomer not automatically resolved. |
| Hydroxyketovalerate aldol cleavage | F01, F04–F15 | S substrate stated for the CF600 preparation; linked-assay controls and substrate degradation matter. |
| Acetaldehyde→acetyl-CoA | F02, F13–F14, M01–M02 | CF600 DmpF and E. coli MhpF are distinct preparations; native MhpF Ki remains primary-unverified. |

Additional dispositions retain the 1993 propionaldehyde precursor inconsistency, reversed 1989 function/mass labels, the 2004 weaker-inhibition/lower-Ki discrepancy, and the uncertain small-subunit apparent mass in the isomerase experiment. Hypotheses about channeling, protective benefit, direct allostery and native YwhB substrate remain hypotheses. The full route is not expanded to include the oxidative sibling or these side activities.

The native-author boundaries remain applicable: Mag2 is scoped to Bordetella sp. 10d, and the native terminal child excludes E. coli ADHE-CPLX despite a global reaction listing. This dossier supplies no primary evidence overriding those boundaries.

## Gaps and access closure

The package followed the seven frozen intake leads and five justified additional primary sources. Existing originals were inspected first. The named prior PMC2531070 BioC file is an error/help response; the prior PMC210496 HTML is reCAPTCHA. Exact copies and rejection hashes are retained. Three main-text retrievals succeeded through actual publisher PDF links despite direct-request403 responses. No new BioC request was made after the known429.

Remaining source limits are explicit: four intake papers remain abstract-only; the structural paper is partial; the 1986 hydrolase source is abstract-only; the 1971 paper is metadata-only; the 1987 and 2013 sources are abstract-level. Publisher, PMC, EuropePMC, public repository and supporting-information attempts are bound in [source-acquisition-and-read-coverage.json](source-acquisition-and-read-coverage.json). The advertised YwhB supplement was not obtained, and a zero-byte202 HTML response with a.pdf filename is explicitly rejected. Access failures are endpoint/time observations, not assertions of global unavailability. No purchase, credential bypass or author contact was attempted.

## Candidate YAML integration

[graph-ready-suggestions.json](graph-ready-suggestions.json) offers source-scoped provisional activity edges and the supported CF600 assembly distinction. Its seven edges use declared local endpoints and repository-supported predicate/category names. It is not a complete record or a schema-valid standalone YAML document; the parent author must ground and qualify endpoints within the one full-route record. No whole-route taxon edge is generated from mixed sources.

[quote-ledger.json](quote-ledger.json) contains the only authored verbatim excerpts:16 whitespace-delimited words from PMID8419288 and 8 from PMID2681159, each shorter than 400 characters. Other assertions use exact locators and paraphrases. The original/extraction bodies are evidence retention, not authored extended quotations. Follow [HANDOFF.md](HANDOFF.md) and the frozen manifest for compact retention.

# Independent scientific review: adenosine nucleotides degradation II

**Request changes: one major finding.** Reviewed the complete external draft `MetaCyc:SALVADEHYPOX-PWY`, SHA `b2e32140bbdc4a242e89166c1090db8d6eac84aa6c55abc8b030d80ff82bd528`: 74 named IDs, 101 edges, 129 evidence items, 48 references. I did not author this record, its evidence package, preflight or supporting implementation. This external review does not substitute for the later canonical maintained review.

## Material completeness finding

The graph omits the measured MG1655 adenine-induced **add** transcription response. It retains induction for xapA, umpH and deoD, while its Add note mentions only historical E. coli B evidence. Independently inspected original [PMID21572102](https://pmc.ncbi.nlm.nih.gov/articles/PMC3159470/), Methods sec3 and Results sec9, explicitly uses MG1655 and reports 17.61-fold add transcript induction by adenine. Methods specify M9 with 2g/L glucose, ±100µg/mL adenine, 37°C and mid-log sampling. Results sec13 explicitly says add is not directly regulated by PurR.

Add an evidence-backed gene-expression edge from CHEBI:16708 adenine to Entrez:945851 add, with the exact issuing gene/protein/strain identity and measured conditions. Retain the E. coli B observation separately; do not turn this into protein allostery, direct ligand binding or PurR repression. The full finding, stable issue key and acceptance checks are in `add-induction-finding.json`. Root owns issue creation and author correction.

## Supported current content

All present edges were examined in `edge-review.json`. The native complete five-reaction route, four orderings and all 25 substrate/product edges match independently read Rhea142/META originals. Formula and formal charge balance match issuing ChEBI identities. The neutral uric-acid structure used by the urate-labelled native reaction is preserved without a physiological protonation claim.

The current eight-step PathBank definition remains distinct; its mixed UshA/PhoA/AphA complex and HIU trimer conflicts were independently confirmed in native BioPAX. The META-only urate-to-allantoin interface is opaque and does not assign downstream oxidative flux to MG1655.

Native/reviewed identities support the alternative nucleotidases and phosphorylases, five specified homomeric assemblies, variable UmpG and inferred XdhABC complex. The 2000 W3110 and 2025 MG1655 results do not become purified NAD specificity evidence. Mo-MPT annotation and the 2009 MCD phenotype interpretation remain separate. The 2020 and 2025 PgeF assays remain construct-qualified, with weak later PNP and failed-growth-rescue limits. Reagent identities and conditional DTT restoration are preserved. Native XapR–xanthosine state, promoter-to-transcription-unit-to-gene projection, and remaining gene-expression edges have traceable local scope.

Rhea139 original SQL independently supports the five exact accession/name pairs. Rhea142 original RDF independently supports the chemical evidence. Matching names do not establish complete chemistry or release equivalence.

## Verification and limits

All 369 preflight artifacts and 100 sealed author artifacts rehashed successfully. Independent identity/chemistry replay passed 246 assertions. Closed schema, evidence locators, native assembly/regulatory bridges, full KGX evidence/qualifier preservation and four meaningful mutation controls passed 525 assertions. These checks do not establish scientific completeness: the Add omission remains a real finding despite deterministic success.

Five original primary articles were independently read in relevant Methods/Results/Discussion sections, plus the newly identified sixth article for Add. The XapR primary source remained abstract-only; historical inhibitor details and uninspected supplements were not invented. Fresh iModulonDB native fallback queries produced expression context only. Console-runner and first extraction-helper failures are retained in `review.json`, with their corrected outcomes.

No maintained files, authority caches, Git or GitHub state were changed. Full canonical authority build, corpus gates/preservation, reviewed successor, canonical review saving and publication remain pending.

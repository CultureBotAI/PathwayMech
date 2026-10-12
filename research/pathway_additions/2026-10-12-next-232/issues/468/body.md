Stable finding key: `nad-construct-ledger-specificity`

Independent scientific review found a minor defect in the NAD phosphorylation/dephosphorylation candidate (`MetaCyc:NADPHOS-DEPHOS-PWY`, target SHA-256 `c2fec44e8c4f9a10f3ba96148a88afd7f3a16c25ac075167286bb81ef975f503`).

The preparation-to-qualifier ledger joins only by publication ID, so distinct preparations within a paper inherit every qualifier using that paper. The ledger presents these as applicable endpoint qualifiers without distinguishing related-source context from the actual preparation. CsiR17 includes FLAG-Nac edges094/095; Archaea07 includes E.coli CysQ047–049; C45A/T50C include WT His10 edges055/058–062; recombinant NadK includes endogenous-native qualifiers. K87 also lists paragraph6, which describes2001 metal replacement. The record YAML itself correctly separates these preparations; this is a misleading audit/capture ledger, not a demonstrated incorrect graph endpoint.

Root read the exact generator and all eight demonstrated preparation/qualifier mismatches. The YAML preparation descriptions remain correctly separated; this defect is in the external audit ledger.

Acceptance criteria:

- Replace publication-only association with explicit exact-context mapping or separately typed contextual/comparator links. Exact endpoint-qualifier mapping must not identify Nac as CsiR, E.coli CysQ as an archaeal preparation, mutant proteins as wild type, or endogenous NadK as its recombinant preparation.
- Keep all28 original context rows and corrected PhoB lineage. Preserve variant, control, and archaea observations as narrative/comparator contexts where no exact graph endpoint exists; do not manufacture new graph edges solely for this ledger.
- Correct K87 paragraph association by removing2001-only paragraph6 or explicitly marking it as a cross-study comparator.
- Add bounded negative checks showing the above mismatched endpoint qualifications are absent from exact preparation links; retained related links must be visibly typed.
- Retain original sealed packet and produce a successor; preserve all102 edge triples,48 qualifiers,19 exact reaction sides and the scientific description except supported citation/ledger repairs.

Original finding SHA-256: `ccca24d919bb085c3953a65e391508cb9362b88214e4f4da7a503ad086c706fa`. Retain the sealed original author packet and record the fixes in a bounded successor with independent review. No maintained NAD record, full canonical build, or resolved issue is claimed.

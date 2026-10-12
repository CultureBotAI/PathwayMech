# Independent scientific review: L-lyxose degradation

**Changes requested: one major and one minor completeness finding.** The existing 109 edges are supported with their stated limits. The separate two native authority adapter gaps are not passing identifier gates and are not counted as these scientific findings.

Reviewed the entire final 2,407-line, 144,531-byte target `/private/tmp/pathwaymech-next-227-author-20261012/draft/l-lyxose-degradation.yaml`; SHA256 `fa77f6b451b49863552a7bcc9543ba94cd408f2886e8477d53e3a2464eb9583b`. This reviewer did not author the L-lyxose preflight or target. All 400 sealed author artifacts were freshly verified. No maintained record, core code, shared cache, canonical review, Git or GitHub object was changed.

## Findings

### 1. Major: Retain reciprocal PlaR–KdgR expression regulation

Stable issue key: `lyxose-plar-kdgr-reciprocal-expression-omission`.

The record includes PlaR autoregulation and external control of plaR expression but omits the cited 2019 reciprocal regulator-expression observations. This is an evidence-backed omission in the represented regulatory context, not proof of direct promoter binding. Material incompleteness: a characterized regulator of the included pathway repressor, and its reciprocal response, are missing despite inclusion of other PlaR expression controls and the same primary source.

**Source proof:** Northern blots show increased plaR mRNA after kdgR deletion and increased kdgR mRNA after plaR deletion. The supported basal wild-type influences are negative in both directions. Conditions: BW25113 and deletion derivatives JW3546 (plaR) and JW1816 (kdgR), M9 plus 0.5% casamino acids, 37 C, aerobic shaking, mid-exponential cells. Indirect regulation remains possible. Original `/private/tmp/pathwaymech-next-227-preflight-20261012/raw/PMC6958661.xml`, SHA256 `3aeebd5caace657ea43d72cbe4a23d41d1a445e2b38062316e667affab29d046`, XPath `/article/body/sec[2]/sec[5]/p[3]`. `finding-methods-context.json` binds the preparation and strain details.

Affected locations: mechanistic_edges (missing relations adjacent to PlaR expression edges lyxose-075 through lyxose-077 and lyxose-099); participants (missing grounded KdgR protein and kdgR gene); conflict-and-scope-ledger.json (missing disposition).

Acceptance:

- Independently ground exact KdgR protein and kdgR gene identities, including reference versus assay-strain scope; do not invent accession strings.
- Represent KdgR inhibiting plaR gene expression and PlaR inhibiting kdgR gene expression, with exact gene endpoints and the source conditions.
- Attach the original 2019 results paragraph and Fig. 5 support at the narrow edges; preserve negative signs and potential indirectness.
- Do not infer direct DNA binding, a KdgR effector, or ordinary wild-type whole-pathway flux from these deletion data.
- Replay source locators and identity/strict gates; reject flipped signs, direct-binding upgrades and gene/protein endpoint substitution.

### 2. Minor: Preserve chemically unresolved pectin-digest reporter context

Stable issue key: `lyxose-pectin-digest-reporter-context-omission`.

The 2000 source reports a plaR/yiaJ reporter effect from pectinase-digested pectin, but neither the complete record nor its scope ledger records that supported, chemically unresolved context. Bounded completeness/documentation gap: the source does not identify a single chemical effector, so the result must not become an invented molecular graph edge. The four-event core is unaffected.

**Source proof:** Pectinase-hydrolyzed citrus or apple pectin produced 10–20-fold yiaJ-lacZ induction in ECL1 but not JA134. Structural-gene expression was unaffected even without repressor. The authors left the significance unknown. Preparation: 0.14% pectin in sodium acetate pH 4.0, overnight 25 C treatment with 400 U Aspergillus niger pectinase, then 10-fold dilution into medium. Original `/private/tmp/pathwaymech-next-227-preflight-20261012/raw/PMC94634.html`, SHA256 `0cc0161545c2db712a9faf395cc5f811d4a864e043132c7e9d7a12d75903376b`, XPath `/html/body/div[2]/div[2]/div/div[1]/div/div[2]/main/article/section[2]/section/section[3]/section[6]/p[4]`. `finding-methods-context.json` binds the preparation and strain details.

Affected locations: description or other supported maintained contextual prose; conflict-and-scope-ledger.json (missing explicit unresolved-mixture disposition); PMID:10913096 evidence context.

Acceptance:

- Preserve the exact direction, 10–20-fold range, ECL1-versus-JA134 contrast, and lack of structural-gene induction.
- Retain the undefined pectinase digest and preparation as mixture/condition context with exact original source locators; record unknown significance.
- Do not equate the digest to galacturonate, invent a molecular identity, add a direct effector edge, or expand the four-event core.
- Make the disposition visible in the successor record/context and corresponding scope dossier; verify the cited source selectors.

## Complete-record assessment

The source-defined core is retained in full: LYXISOM, LYXK, LXULRU5P and RIBULPEPIM, with native selected directions L2R, L2R, R2L and L2R. All 11 core chemical sides and four transport sides are present. The original Rhea RDF supplies reaction-side participant identities, coefficients, formulas and charges; all tested balances hold. Native beta-L-lyxopyranose has the same complete InChI as original CHEBI:147210. The first native reaction is reversible metadata, while the native pathway layout selects forward flux. Generic RhaT pyranose transport is bounded separately; neither exact beta uptake nor a new anomerization is asserted.

Native RhaA tetramer, LyxK dimer and AraD tetramer are distinct from assay chains. The qualified RhaA JA121 preparation, retained 10-His LyxK construct, cleaved-tag SgbE preparation and B/r AraD metal experiments preserve reference-chain versus experimental scope. Magnesium in the coupled LyxK assay is not a measured occupancy; the SgbE zinc assignment is marked by similarity. Native ATP inhibition and glutathionate activation remain annotation-level claims with the unavailable 1994 body explicitly limited. The chemically unresolved AraD glycolohydroxamate inhibitor remains a disclosed source gap; substituting phosphoglycolohydroxamate would be unsound.

SgbU remains tentative, with both the failed 2000 GST-based experiment and failed 2002 assay retained. The graph does not upgrade this to demonstrated catalysis or universal inactivity. Primary genetics distinguish alternative terminal AraD and SgbE activities and the yiaQ insertion-polarity effect. No YiaQ decarboxylation or separate 1991 mutant-rhaB 1-phosphate pathway is inserted into the core. Whole-route support is bounded to adapted strains such as JA134; ordinary wild-type MG1655 complete flux is not asserted.

The independent regulatory reconstruction joined exact native regulators, signs, promoter objects, transcription-unit membership, UniProt native-chain/GeneID cross-references and NCBI Gene originals. Eight assemblies were checked; 23 neighboring-promoter assertions were excluded. ArcA-P is a qualified molecular state; its rhaT expression evidence does not establish direct binding. Motif-only site evidence stays distinct. PlaR gel-shift and reporter observations retain their different preparations, strains, concentrations and endpoints. No lyxose-bound RhaS or signed CRP site-2 function is invented. The two findings concern omitted additional context, not incorrect signs on the existing edges.

The frozen PathBank parent and child were freshly extracted from the full archive and byte-matched. Its UlaF assignment and incorrect formula do not override native exclusions and original chemical identities. The Pentose Phosphate child stays opaque and source-specific. The NONOXIPENT and PWY-5257 interfaces likewise remain bounded.

## Evidence and checks

All 64 declared references were checked against original whole-body SHA256 and byte bindings. All 222 actual target evidence-locator uses resolved, including qualifier evidence. The author's 235-entry observation ledger is broader than this target-use count; no missing target selector was detected. `source-locator-observations.json` retains every replayed use, and `edge-assessments.json` accounts for every one of the 109 edges.

All 64 named identities were examined scientifically: 28 original ontology identities, 12 UniProt proteins, seven NCBI genes, 12 top-level native MetaCyc/EcoCyc objects, four original Rhea events and the frozen PathBank child. UniProt uses K-12 taxon 83333; the NCBI Gene/native ECOLI objects use MG1655 taxon 511145. The record retains both scopes. This is not a substitute for the still-failing native adapter gates.

Single-target native schema and closed strict validation passed. Nine deliberate corruptions were rejected by independent checks: wrong Rhea orientation, wrong substrate anomer, missing ATP, SgbU upgraded to catalysis, lost ArcA state, misplaced PlaR construct qualifier, flipped IHF regulation, wrong PlaR target and missing complex component. Test-harness mistakes and exploratory command failures remain documented in `execution-receipts.json`; they are not relabeled passing runs.

The 1991 original PDF was freshly extracted through PDFKit; the text agrees after removal of preflight-added page markers. Printed page 5147 was visually checked against the transport competition and kinetic interpretation. Full relevant 2000/2002 primary mechanisms and 2019 methods/results were read. The retained 1994/1998 abstract-only access and later source-specific full-body access limits are not promoted to original-body evidence.

The iModulon replay verified 26 retained original responses, 14 searches and 11 components. It remains computational expression context, with zero causal graph edges. Actual baseline inventory is 227 record files at observed HEAD 9dc303d33d7f798904edf82993211dc53312903d, comprising the merged 226 plus uncommitted adopted ribose. Hidden, ignored and followed files were included in the record inventory and relevant absence searches. Only the terminal AraD activity overlaps L-arabinose degradation I; no 228-file baseline or exhaustion claim is made.

## Remaining gates and handoff

Create issues for the two stable findings and produce an immutable successor with evidence-backed corrections. Reassess the exact successor before adoption. Independently complete and review the guarded LYXISOM class=true and archive-aware PathBank child adapters; neither missing identifier validation nor an unsupported node may be waived. Root owns canonical authority construction, maintained adoption, full-corpus gates, saved review/history, issue/PR lifecycle, merge and branch cleanup.

This external scientific review does not claim a whole-corpus validation, export, build or browser-layout pass. Licensing remains deferred under the user instruction. The earlier mannosylglycerate preflight was left unchanged.

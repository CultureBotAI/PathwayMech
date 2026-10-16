# Ethanolamine utilization: finite core issuer assessment

The native **MetaCyc:PWY0-1477** identity, five source Reaction identities, 14 concrete material identities and two direct strain identities are supported within this packet. This is source preparation, not a maintained-record verdict or approval of biological flux, a source adapter, or an exact pathway mapping to every cross-reference. Actual next271 merged-baseline binding remains a prerequisite for maintained work.

## Native route and names

The reused full META 27.0 root is `PWY0-1477`, label `ethanolamine utilization`. Its original hash is `a65eb455ccb8459b73754834f354231c576fe4805e2ba32df568dd9ac6fec25d`. Independent ECOLI 27.0 acquisition confirms the same five native member IDs, four ordering relations and five selected layout directions. Its PGDB is E. coli K-12 MG1655; the META definition directly names both MG1655 and Salmonella LT2. The ECOLI counterpart therefore supports shared route structure, while unconditional cross-species pathway equivalence is not proposed. Retain the MetaCyc root.

All five full Reaction originals omit their **own** common-name slot. Nested enzymatic-reaction names are names of activities and must not be substituted as issued Reaction names. Native frame IDs are legitimate source-context fallback labels. The existing acetate adapter explicitly implements this at its `_projection` function, lines 2047–2054 in the copied context; it does not authorize extending that finite adapter to new identities. No authority adapter or schema has been changed here.

| Native Reaction | Pathway traversal | Selected concrete equation | Matching directed Rhea |
| --- | --- | --- | --- |
| ETHAMLY-RXN | L2R | ethanolaminium → ammonium + acetaldehyde | 15314 |
| ACETALD-DEHYDROG-RXN | L2R | acetaldehyde + CoA + NAD → acetyl-CoA + NADH + H+ | 23289 |
| PHOSACETYLTRANS-RXN | L2R | phosphate + acetyl-CoA → acetyl phosphate + CoA | 19522 |
| ACETATEKIN-RXN | R2L | ADP + acetyl phosphate → ATP + acetate | 11354 |
| ALCOHOL-DEHYDROG-RXN | R2L | acetaldehyde + NADH + H+ → ethanol + NAD | 25292 |

All 22 native material occurrences have omitted coefficients, effective multiplicity one, and no explicit compartment. All five equations balance in atoms and charge under the source's concrete molecular species. Only ETHAMLY has native own direction LEFT-TO-RIGHT; the other four are REVERSIBLE. Their source Rhea cross-references are respectively 15314, 23291, 19524, 11355 and 25293; four are bidirectional family members. A selected directional quartet member above is a scoped chemical comparison, not a silent replacement of the native direction assertion or a measured flux claim. Both acetaldehyde branches remain necessary; adding one copy of each does not establish a physiological net.

## Concrete chemical identities

Each row was independently checked against a freshly acquired complete ChEBI issuer response. Native InChI, InChIKey, CML formula and formal charge all match. Stereo encoded in the exact InChI matches; no broader family or neutral compound is substituted. The 14 independently acquired MetaNetX compound pages match the same InChI, key, formula and charge. Their selected IDs and all source links are recorded in `results/material-identity-assessment.json`; unselected native xrefs are preserved as leads, not approved en masse.

| Native material | Exact ChEBI species | Formula | Charge |
| --- | --- | --- | ---: |
| ACET | 30089 acetate | C2H3O2 | −1 |
| ACETALD | 15343 acetaldehyde | C2H4O | 0 |
| ACETYL-COA | 57288 acetyl-CoA(4−) | C23H34N7O17P3S | −4 |
| ACETYL-P | 22191 acetyl phosphate(2−) | C2H3O5P | −2 |
| ADP | 456216 ADP(3−) | C10H12N5O10P2 | −3 |
| AMMONIUM | 28938 ammonium | H4N | +1 |
| ATP | 30616 ATP(4−) | C10H12N5O13P3 | −4 |
| CO-A | 57287 coenzyme A(4−) | C21H32N7O16P3S | −4 |
| ETHANOL-AMINE | 57603 ethanolaminium(1+) | C2H8NO | +1 |
| ETOH | 16236 ethanol | C2H6O | 0 |
| NAD | 57540 NAD(1−) | C21H26N7O14P2 | −1 |
| NADH | 57945 NADH(2−) | C21H27N7O14P2 | −2 |
| PROTON | 15378 hydron | H | +1 |
| Pi | 43474 hydrogenphosphate | HO4P | −2 |

**Source representation conflicts remain visible.** Native CML SMILES contain generic placeholders for ACETALD, ATP, ETHANOL-AMINE, NAD and NADH. Those strings cannot independently certify these concrete structures and were not used as equivalence premises. Exact native InChI, InChIKey, formula and formal charge agree with the ChEBI concrete species. Similarly, the display name NAD+ refers to the oxidized nicotinamide form; the full represented molecule has net charge −1. Native phosphate is hydrogenphosphate, not phosphate(3−).

The fresh neutral ethanolamine record **CHEBI:16000**, formula C2H7NO and charge 0, is explicitly conjugate base of CHEBI:57603. It is not an exact alias of native ETHANOL-AMINE(+1). A transport claim about uncharged ethanolamine cannot be attached to transport of the native +1 material by name alone. No acid-base reaction or measured mechanism is invented to bridge them. Primary EutH evidence and the source neutral/protonated conflict are separately owned; this agent has not read that paper.

## Reaction alias limits and the kinase EC annotation

The reused frozen Rhea release 142 (2026-09-02) resolves all five complete direction families. All repeated RDF descriptions for 66 selected subjects are preserved as 88 exact original fragments with decoded byte offsets and hashes; five fresh Rhea master TSV rows corroborate current master equations and identifiers. The selected Rhea material species and unit coefficients exactly equal the native equations. Rhea citations were not treated as newly read primary papers.

All five independently acquired MetaNetX equations agree on the concrete species and coefficients after their chemical issuers are resolved. Two print the opposite orientation from native left/right; the exact orientation is recorded in `results/alias-crosschecks.json`. Their MNXD1 generic compartment is not a biological lumen or cell compartment. The reversible display does not replace a native or pathway-selected direction. Native old compound xrefs such as MNXM7 or MNXM21 are not silently promoted to the current selected MNX equation identifiers.

KEGG R00749, R00228, R00230, R00315 and R00754 were acquired along with all 14 equation compounds. They describe the corresponding named transformations, but several formulas represent different protonation: R00749 uses neutral ethanolamine and ammonia, while the native source uses ethanolaminium and ammonium. ATP, ADP, CoA, acetyl-CoA, acetate, acetyl phosphate, NAD/NADH and phosphate also use different hydrogen conventions. No exact charged-equation alias or chemical exact mapping to KEGG is approved from these names/formulas. The complete native equations remain intact.

Native ACETATEKIN-RXN reports **EC-2.7.2.15**, despite its ATP/acetate equation. Fresh IUBMB entries distinguish EC2.7.2.1 acetate kinase from EC2.7.2.15 propionate kinase. The latter explicitly allows acetate as a substrate; its principal issued equation is ATP + propanoate → ADP + propanoyl phosphate. Thus the discrepancy is retained as an annotation/specificity distinction, not evidence that the native acetate equation is invalid. Do not silently rewrite the source EC, transfer propionate into the pathway, or equate an EC class with a particular protein.

## Taxon and evidence scope

Fresh NCBI responses establish 511145 as *Escherichia coli* str. K-12 substr. MG1655, parent 83333, and 99287 as *Salmonella enterica* subsp. enterica serovar Typhimurium str. LT2, parent 90371. MetaCyc calls both strain; NCBI currently gives MG1655 rank `no rank` and LT2 rank `strain`. This rank-model distinction does not change the exact identifiers. Native short common names must retain their strain/subspecies context.

The separately acquired native-agent UniProt P0AEJ6 original is copied exactly for `/organism/taxonId` and `/comments/10/texts/0`. Its protein scope is K-12 taxid83333. The CAUTION, annotated ECO:0000305 with PMID9278503, says the CPZ-55 interruption between eutA and eutB **may** prevent MG1655 operon expression and contrasts W3110. This is a curator inference, not demonstrated complete-route flux or a universal impossibility. Keep the native direct MG1655 association, broad K12 protein identity and actual experimental strains distinct. Neither LT2 experiments nor K12 protein entries silently become MG1655 experiments.

GO:0046336 remains a broader ethanolamine-catabolic process. Returned KEGG M00092/M00093 concern phosphatidylethanolamine biosynthesis. Neither is an accepted exact pathway alias. This packet makes no global novelty or exhaustion claim.

## Reading and remaining work

The identity, structure, equation, direction, organism, EC and cross-reference sections described above were inspected. `native-own-slot-projections.json` accounts for 583 own slots in 23 complete native objects (core20, two taxa, one EcoCyc counterpart); the projection preserves biological, regulatory and thermodynamic context without claiming those assertions were scientifically reviewed here. Native biological closure and primary experiments are owned by separate agents. In particular, a material backlink does not establish a route enzyme or regulatory edge.

395 reproducible structural/alias checks passed. They are author checks, not independent scientific review. The old Rhea first-description-only projection is superseded; all repeated descriptions are included in the complete successor and independently replayed against exact decoded source slices. No maintained YAML, generated page, schema, source adapter, Git/GitHub state, runtime or frozen source owner was changed. Independent source acceptance, actual merged-baseline rebind, complete biological graph assessment and governed corpus/review gates remain necessary.

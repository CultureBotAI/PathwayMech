# Propanoyl route assessment: two distinct candidates remain deferred

The exact five-reaction **MetaCyc:PWY0-42, 2-methylcitrate cycle I**, is a distinct microbial pathway with strong biochemical support. No pathway YAML was added because its central methylcitrate stereochemistry remains disputed in primary literature and explicitly cautioned by current UniProt. This is a chemical-identity gap, not evidence that the biological pathway does not exist.

The initially supplied **PathBank:SMP0002069 / PW002057.owl** is a different, broader methylmalonyl-CoA map. It remains deferred for separate reasons. Neither candidate is closed as an exact duplicate. The assessment does not claim that pathway sources are exhausted.

## Native scope and deduplication

PW002057 contains five biochemical reactions. Reactions6006,6008 and6009 are the Sbm/ScpABC transformations already represented by `data/pathways/succinate-to-propanoate.yaml` (MetaCyc:PWY0-43). Reactions 6005 and 6007 add propionyl-CoA carboxylation and methylmalonyl-CoA epimerization; no catalytic controller is supplied for either native object. Their absence does not authorize invented catalysts or establish that these transformations cannot occur biologically. The full PathBank map cannot be marked covered by the existing three-reaction record.

PWY0-42 contains all five reactions below. Its native description distinguishes this depiction from external TCA regeneration of oxaloacetate; the latter should not be added merely because the native title says cycle. Alternative AcnD/PrpF routes are separate native pathways.

| Native MetaCyc reaction | Native Rhea link | Physiological directed Rhea |
|---|---|---|
| PROPIONATE--COA-LIGASE-RXN | 20373 master | 20374, left to right |
| 2-METHYLCITRATE-SYNTHASE-RXN | 23783 bidirectional | 23781, left to right |
| 2-METHYLCITRATE-DEHYDRATASE-RXN | 17728 bidirectional | 17726, left to right |
| 4.2.1.99-RXN | 17944 bidirectional | 17943, right to left |
| METHYLISOCITRATE-LYASE-RXN | 16812 bidirectional | 16810, left to right |

All five native membership objects, native Rhea links, independent Rhea 142 master/direction families and 21 coefficient-bearing side occurrences were inspected. Replaying atom and charge totals passed for all five source equations. This verifies the source projection, **not the disputed biological stereochemistry**.

Ignored- and hidden-inclusive searches covered identifiers, labels, reaction names, gene/protein names, references and prior research in the accessible worktree. No matching maintained methylcitrate pathway was found. The original Documents checkout returned an operating-system access error, preserved in `propanoyl-duplicate-searches.json`; no absence claim is made for that inaccessible tree. The prior Sbm and candidate-screening handoffs were inspected. GO:0019629 and GO:0019679 are obsolete and replaced by the broader GO:0019543, so none is an exact current identity for the five-reaction route.

## Why the stereochemical disagreement is material

The 2002 E. coli paper, [PMID 12473114](https://doi.org/10.1046/j.1432-1033.2002.03336.x), provides the reconstituted downstream mechanism and the historical (2S,3S) assignment. Its publisher-rendered Methods, Results and Discussion were inspected; the retained section artifacts are serialized web-tool text rather than original publisher HTML.

The 2017 study, [PMID 28956599](https://doi.org/10.1021/acs.biochem.7b00778), directly includes E. coli PrpC and PrpD. Its main article was accessible at abstract level; the **complete authentic 14-page supplement** was retrieved from [ACS Figshare](https://acs.figshare.com/articles/journal_contribution/5479564), DOI 10.1021/acs.biochem.7b00778.s001. All pages were read, and rendered S7 and S13 were independently inspected. Table S-1 contains the E. coli cloning primers. S4–S6 and S10–S13 describe comparisons with commercial methylcitrate and historical NMR assignments; they do not assign an absolute configuration. S7 explicitly contrasts the two relative stereochemical classes using the same molecular skeleton. The authors retain the alternatives (2R,3S) and (2S,3R), acknowledge the disagreement with the older assignment and reserve definitive stereoisomer-standard work for later investigation. The supplement states, “either our assignment, or the one previously reported in the literature, is incorrect” (S13).

Current UniProt 2026_03 **P31660 and P77243 both contain an explicit CAUTION** about this unresolved assignment, citing the 2002 and 2017 papers with ECO:0000305. Their catalytic annotations still link the historical stereospecific Rhea equations. The primary 2017 supplement therefore cannot be dismissed as irrelevant Bacillus evidence, and current catalytic annotation alone cannot settle the conflict.

| Structure | Issuing identifier and exact stereochemical distinction |
|---|---|
| Historical (2S,3S) trianion | CHEBI:58853; InChI stereolayer `/t3-,7+/m1/s1` |
| One of the two 2017 alternatives, (2R,3S) trianion | CHEBI:10860; stereolayer `/t3-,7-/m1/s1`; **not selected as the enzyme product** |
| Other 2017 alternative, (2S,3R) | Absolute assignment unresolved; no identifier was selected |
| Unspecified methylcitrate trianion | CHEBI:15598; no stereolayer; **not substituted into specific Rhea reactions** |

ChEBI 255 distinguishes the first two structures at the same formula and charge. Neutral acid counterparts CHEBI:50948 and CHEBI:30836 retain the corresponding stereolayers. Native MetaCyc:CPD-622 has an InChI exactly matching CHEBI:58853, as well as the explicit ChEBI cross-reference. Its CML SMILES lacks stereomarkers, so that field alone must not override the specified native InChI. These inspected structures and the supplement's comparison rule out treating the disagreement simply as protonation or harmless label renumbering. They do not justify choosing either unresolved alternative.

A bounded later-literature search found no inspected E. coli absolute-configuration resolution. The 2024 paper PMID 38704976, a newer Rhea citation, was checked at abstract level and concerns Eimeria tenella enzyme kinetics. It does not settle this E. coli assignment. This is not an exhaustive claim about all later literature.

## Enzyme and assembly handoff

Fresh complete UniProt bodies and response release metadata are retained for PrpE/P77495/b0335, Acs/P27550/b4069, PrpC/P31660/b0333, PrpD/P77243/b0334, AcnB/P36683/b0118 and PrpB/P77541/b0331. Native enzyme and assembly frames were also retrieved.

- **Activation:** the 2002 E. coli K-12 W3350 expression evidence favors Acs physiologically, but that inference is not an isolated Acs propionate assay. PrpE's current function evidence includes ECO:0000250. Preserve the difference between native annotation, homology support and experimental physiology.
- **PrpC:** MetaCyc:CPLX0-251 explicitly contains two G6198-MONOMER components; UniProt independently annotates a homodimer with experimental evidence. The native complex does not resolve product configuration.
- **PrpD:** UniProt annotates a monomer. PMID 11782506 describes an unstable [2Fe-2S] association and metal-dependent maximal activity; the inspected 2002 study reports contrasting metal/reconstitution results. Do not silently make a universal cofactor or metal-independence assertion.
- **AcnB:** the iron-sulfur catalytic enzyme and regulatory oligomer states require separation. MetaCyc:CPLX0-7761 lists one component without an explicit coefficient while also carrying a 180 kDa molecular-weight citation. Current UniProt distinguishes monomer and condition-dependent dimer. Do not turn this source ambiguity into an invented fixed catalytic dimer.
- **PrpB:** MetaCyc:CPLX0-1021 explicitly contains four G6196-MONOMER components. UniProt and primary abstract evidence support tetrameric enzyme and Mg-dependent catalysis. Mutant substrate/product structures in PMID 15723538 need their experimental scope retained.

The native pathway/complex taxonomy is MG1655; current UniProt proteins are K-12 scoped, while the 2002 primary uses W3350 and recombinant preparations. A future record must describe those evidence scopes without pretending every experiment used MG1655. No compartment, transport, regulatory edge or alternative TCA branch was added from inference. The batch's shared iModulonDB receipt provides expression context only and does not resolve catalysis or stereochemistry.

## Acceptance checks before a future record

1. Obtain an inspectable primary absolute-configuration assignment for the E. coli PrpC product using authenticated stereoisomer standards, or an upstream reviewed resolution grounded in such evidence. Alternatively, assess a source-supported uncertainty representation explicitly; do not silently replace the exact species in a specific reaction.
2. Reconcile both PrpC and PrpD chemistry against exact Rhea, ChEBI and native structures. A generic parent, a balanced equation or the existence of CHEBI:10860 alone is insufficient.
3. Keep the complete native five-reaction route. Resolve activation evidence grades, PrpD metal conflict and AcnB assembly state without narrowing away difficult biology.
4. Repeat semantic/ignored-inclusive dedup, issuer resolution, native membership and direction replay, full chemistry/evidence checks and independent scientific review before adding YAML.

[Follow-up issue #332](https://github.com/CultureBotAI/PathwayMech/issues/332) tracks the unresolved acceptance checks. The six adjacent `propanoyl-*.json` artifacts preserve source URLs, dates, full-body or artifact hash scopes, native projections, competing identities, dedup results and the actual narrow replay. Raw bodies and scratch remain under `/private/tmp/pathwaymech-next-routes-evidence/propanoyl`. No full-corpus gate or completed record review is claimed by this research handoff.

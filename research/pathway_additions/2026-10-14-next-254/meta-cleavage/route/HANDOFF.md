# P184-PWY whole-boundary curation decision

Author support, 2026-10-14. No maintained files or authority snapshots changed. No independent review verdict.

The entire eight-member MetaCyc 27.0 definition is curatable as a source-defined composite. Each native chemical equation is explicit, balanced and exactly grounded. The inspected Rhea 142 release retains the historical enol tautomerase/hydratase equations and the modern LigU/LigJ equations as distinct approved reactions. These facts support preserving the native definition, not substituting the later reactions under the old IDs. A source-defined composite must not be presented as an experimentally reconstituted route in one strain. Unsupported or chemically contradicted catalyst-to-reaction assignments are excluded explicitly; complete same-strain assay closure is not a prerequisite for the source-defined chemical pathway.

`protocatechuate-meta-cleavage.yaml` is the concrete scratch record. The assembled record has six contextual taxa, sixty-two participants, all eight reactions, one hundred twenty-seven edges, and eighty-four references. The exact frozen native biological fragment is merged without changing its assertions; the single integration category adjustment marks CHEBI:48828 as a cofactor because its two accepted has_cofactor edges establish that role. The assembled record passes `pathwaymech.schema.validate_record`; this is not the full repository gate suite. Canonical authority extension, history, generated pages and independent review remain the root agent's work.

## Exact identities

- Native oxalomesaconate is CHEBI:57471. It has the E double bond in the position represented by Rhea's `(1E)-4-oxobut-1-ene-1,2,4-tricarboxylate`; modern descriptions using `(4E)-OMA` number the same structure differently.
- Native CPD-12849 is CHEBI:58142, the E,E enol. The issuing historical `cis,cis` display name does not override its full stereochemical structure. It differs from the Z,Z enol CHEBI:57732, linked in some native GalD/GalB narrative.
- Modern LigU produces CHEBI:142690, KCH. Its current ChEBI label is `(2Z)-4-oxobut-2-ene-1,2,4-tricarboxylate`; Rhea calls the same structure `(3Z)-2-oxo-4-carboxy-3-hexenedioate`. This is a keto tautomer with a shifted double bond, distinct from native CHEBI:58142. Formula and charge match but full InChI and bond-order connectivity do not.
- Native CHA CHEBI:58075 leaves absolute configuration unspecified. Modern LigJ product CHEBI:142706 is explicitly S and is a direct ChEBI subclass of CHEBI:58075. Do not turn the unspecified structure into a racemate or silently replace it with the S-specific compound.

The new `exact-chemistry-comparison.json` compares six freshly retrieved official ChEBI records against pinned ChEBI 255, independently interprets full SMILES and InChI using RDKit 2024.03.5, and verifies four Rhea equations from the pinned original RDF. All six live/pinned full InChI, key, formula and charge comparisons match. Current SMILES round-trips match their issuing InChIs. Known incomplete stereo in the older pinned SMILES is not used to override full InChI/current SMILES.

## Complete native boundary

| Native reaction | Selected exact equation | Direction metadata |
|---|---|---|
| PROTOCATECHUATE-45-DIOXYGENASE-RXN | RHEA:24045 | native physiological L2R |
| R107-RXN | MetaCyc:R107-RXN | L2R; spontaneous=true |
| 1.2.1.45-RXN | RHEA:29588 | L2R; obsolete native RHEA:10889 xref replaced by complete equation comparison |
| RXN-2462 | RHEA:10645 | native physiological L2R |
| RXN-9983 | RHEA:28932 | native reversible, selected L2R; spontaneous=true |
| RXN-2463 | RHEA:17403 | native reversible, selected R2L relative to native written dehydration |
| RXN-2464 | RHEA:28936 | native reversible, selected L2R |
| OXALODECARB-RXN | RHEA:15642 | native physiological L2R |

The terminal oxaloacetate decarboxylation remains internal. GO:0019617 stops at oxaloacetate plus pyruvate and cannot replace this entire eight-member pathway identifier. The graph describes selected pathway flux while retaining source reversibility; a Rhea master or bidirectional identifier alone is not evidence for physiological reversibility. Native spontaneous flags assert possible uncatalyzed conversion without a rate or universal physiological condition.

## Source-to-graph dispositions

Every native member, coefficient-one reactant/product and selected layout orientation is represented in `complete-native-graph-proposal.json` and the scratch YAML. All seven native reaction-ordering assertions are represented as provides_input_for edges, each independently tied to an exact shared selected product/substrate; no causal-regulation edge is inferred. Exact native/Rhea mapping is additional chemical evidence, not a protein-specific activity claim. The four direct native species slots are retained as contextual taxa, using issuing taxonomy labels; they do not imply universal occurrence in every member or eight-step experimental closure. Native NCBITaxon:502559 is retained as its own source identity and is not asserted equivalent to the distinct modern NCBITaxon:627192 used by some protein records. The broader source taxonomic-range phylum is not turned into a new pathway occurrence assertion. Narrative upstream aromatic substrates and three alternative ring-fission pathways are background, outside this exact native route.

Modern LigU/LigJ data are retained as contrasts in the research dossier, with their exact proteins/constructs separately reviewed by the constructs author. They do not support LigU→native RXN-9983 or LigJ→native RXN-2463 edges. Linked GalD/GalB narrative uses a different enol stereoisomer. The separately inspected 2016 GalB study explicitly uses the E,E substrate generated with GalA/GalD, supporting the native structured E,E reaction assignment while rejecting the conflicting Z,Z narrative link. GalD/GalB experimental preparation qualifications remain necessary on their assay-based claims. This preserves every native chemical step while avoiding false catalyst assignments. Generic source aldolase activity may support unspecified CHA without claiming either enantiomer specificity.

Route-author read bounds for the 2016 GalB paper are the targeted Introduction/substrate-preparation/assay sections and visual inspection of Figure 1; full biological source coverage is owned by the native-evidence author. Figure 1 explicitly separates the GalD-produced (2E,4E)-CHM from an alternative proposed CHM geometry. No new paper quotations are proposed. No source biological IDs are invented. No authority snapshot was hand-built. The old next253 source/review bytes remain unchanged.

## Reproduction

Run `extract_rhea.py` with the existing Rhea 142 RDF/directions files, then `compare_chemistry.py` with RDKit 2024.03.5 and the six newly retrieved issuing ChEBI JSON files. Run `propose_graph.py` and `assemble_record.py` with the current project venv and explicit current-worktree PYTHONPATH. All full originals stay external. Retain compact projections/manifests plus helpers renamed `.py.txt`; do not retain full raw downloads or an active research `.py` file.

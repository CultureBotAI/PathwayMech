# Homogentisate catabolic process

## Pathway scope

`GO:1902000`, **homogentisate catabolic process**, is represented for *Pseudomonas putida* strain U under the canonical species identifier `NCBITaxon:303`. The experimentally studied strain is explicit; this is not an assertion of pathway presence in every strain assigned to that species. The target is `data/pathways/homogentisate-degradation.yaml`.

The complete selected central pathway has three reactions: HmgA ring cleavage, HmgC cis/trans isomerization, and HmgB hydrolysis, ending in fumarate and acetoacetate. The exact GO term and its three exact synonyms were inspected in QuickGO and the pinned GO authority. The primary study separately boxes this central pathway in Figure 1B. The broader native `MetaCyc:TYRFUMCAT-PWY` contains five reactions, starting with tyrosine aminotransferase and hydroxyphenylpyruvate dioxygenase; its identifier is therefore not used for this smaller, independently named complete pathway.

## Mechanistic summary

| Step | Directed reaction | Functional strain U protein | Evidence limit |
| --- | --- | --- | --- |
| Ring cleavage | `RHEA:15450` | HmgA, `UniProtKB:Q6EMI9` | Reviewed function and primary genetics; catalytic-family and hexamer annotations retain HAMAP inference. |
| Isomerization | `RHEA:14818` | HmgC, `UniProtKB:Q6EMI7` | Primary genetic/homology assignment and exact deposited sequence; current UniProt entry is unreviewed. |
| Hydrolysis | `RHEA:10245` | HmgB, `UniProtKB:Q6EMI8` | Primary genetic/homology assignment and exact deposited sequence; current UniProt entry is unreviewed. |

The [2004 primary study](https://doi.org/10.1128/JB.186.15.5062-5077.2004) supplies the named pathway and strain U genetic evidence. Its deposited sequence `AY168855.1` independently links the three CDS translations to `AAO12527.1`, `AAO12528.1`, and `AAO12529.1`, respectively. All three translations are replayed against the corresponding current UniProt sequences. KT2440-specific enzyme assays and later structural work remain comparative evidence.

All eleven reaction-side relations come from the full Rhea 142 RDF. Every master-to-directed-member bridge cites the explicit `rh:directionalReaction` triple: `15449→15450`, `14817→14818`, and `10244→10245`. The forward orientations also agree with the three inspected native MetaCyc reaction objects. Atom and charge balance retain two net hydrons, dioxygen consumption and hydrolytic water. No extra net reaction is added.

## Evidence table

| Maintained relation | Inspected source | Scope |
| --- | --- | --- |
| Eleven chemical sides | Rhea native side, coefficient, participant, compound and ChEBI triples | Exact directed reactions and charge-normalized species. |
| Three protein/activity assignments | Primary Fig. 1B and central-pathway Results; current UniProt; ENA deposited CDS | `enables` retains functional identity without asserting an isolated monomer as the catalytic assembly. |
| Three process memberships | Primary boxed central pathway; exact GO definition | Complete selected core. |
| Two material-transfer edges | Shared Rhea intermediate plus primary Fig. 1B order | Chemical order A→C→B; operon order is A→B→C. |
| Three cofactor edges | Current protein-specific UniProt annotations | HmgA iron cation is HAMAP inference; HmgB Ca/Mg are ARBA/PIRSR automatic annotations with no occupancy or simultaneous-requirement claim. |
| Two protein localizations | Current UniProt GO cross-references | Electronic cytoplasm annotations, not localization measurements. |

The primary PDF was retrieved intact from [Europe PMC](https://europepmc.org/articles/PMC451635?pdf=render); Figure 1 and relevant Methods/Results were inspected as text and rendered pages. Failed publisher/PMC attempts and page shells are explicitly classified as unavailable or rejected. Their hashes never stand in for an inspected paper. Complete raw bodies stay outside the repository.

## Gaps and exclusions

- HmgA's strain U hexamer is annotated by HAMAP. The inspected MetaCyc complex frames belong to humans; fungal and other bacterial enzyme frames likewise do not establish the U assembly. No foreign complex is imported, and no monomeric catalytic unit is asserted.
- Strain U HmgB and HmgC were not individually characterized as purified enzymes in the inspected study. Gene disruption and cluster rescue are recorded with sequence-based functional interpretation. Current TrEMBL identities are not described as reviewed protein records.
- No strain U-specific glutathione requirement was established in the inspected primary study or the exact current HmgC annotation. This omission does not assert glutathione independence. Human/fungal glutathione-dependent assays are not transferred to U.
- Upstream Phe/Tyr/3-hydroxyphenylacetate entry reactions, HmgR promoter regulation, downstream central metabolism, transport and pigment formation lie outside the selected three-step biochemical pathway. No unsupported transporter or generic DNA node is introduced.
- The parent's iModulonDB `p_putida/precise321` module 78 receipt concerns KT2440. It is retained as comparative expression context only; no biochemical or regulatory edge, strain U membership, or missing-membership claim follows from it.
- Hidden and ignored files were included in both accessible-repository searches. The clean 177-record anchor has no matching pathway/reaction/protein/source identity. Current-worktree hits are only this batch's baseline/context receipts. The inaccessible original Documents checkout was not searched.

## Verification

The owned replay checks native and closed schemas, source-body hashes, a fresh streaming Rhea projection, exact side sets and family directions, atom/charge balances and net stoichiometry, all three U CDS translations, evidence attachment, cofactor/location annotations, and canonical labels. The final author validation receipt reports the actual command outcomes and target hash. Whole-repository gates, generated pages/KGX and independent review are delegated to the parent and are not claimed by this author dossier.

## Further exact source lead

`MetaCyc:PWY-6993`, nicotine degradation II (pyrrolidine pathway), remains a distinct full eleven-reaction lead in *P. putida* S16. The [2013 route study](https://doi.org/10.1371/journal.pgen.1003923) and [2022 Pnao correction](https://doi.org/10.1016/j.jbc.2022.102251) require reconciliation with the older native route. NicA2/Pnao use the physiological cytochrome partner CycN; older oxidase/O2 assignments and the historical NicA1 shortcut require explicit correction. Native spontaneous hydration, ring opening, fumarate formation and the succinate-semialdehyde branch must all be accounted for. This is a separate future candidate, not a second record or an exhaustion claim in this dossier. Raw native XML and primary fulltext paths were handed to the parent, who owns its separate assessment.

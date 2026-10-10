# Pathway mechanism research: methylerythritol phosphate pathway I

## Pathway scope

The new record is `MetaCyc:NONMEVIPP-PWY`, methylerythritol phosphate pathway I,
at `data/pathways/methylerythritol-phosphate-pathway-i.yaml`. It represents the
*Escherichia coli* K-12 enzyme set, `NCBITaxon:83333`, resolved by eight reviewed
UniProt entries. The independent MetaCyc 22.5 definition lists K-12 MG1655
(`NCBITaxon:511145`) and *Brucella abortus*; these are not silently equated with
all eight K-12 protein annotations. The record does not assert those proteins
for the additional species or assign an experimentally established reaction to
every K-12 substrain.

This is the flavodoxin-associated MEP I variant. It is separate from the existing
mevalonate pathway and from MEP II's ferredoxin-associated IspG step. The record
keeps all nine native reaction frames, mapped to nine reviewed Rhea directions,
including both terminal IspH products and the additional Idi interconversion.

## Mechanistic summary

Dxs condenses pyruvate and D-glyceraldehyde 3-phosphate to DXP. Dxr rearranges
and reduces DXP to MEP. IspD, IspE and IspF perform cytidylylation,
phosphorylation and cyclodiphosphate formation. IspG forms HMBPP, and IspH
branches directly to IPP and DMAPP. Idi interconverts IPP and DMAPP but is not
required to make the IspH-derived DMAPP branch.

The native definition's reaction-layout and current UniProt/Rhea annotations
establish the retained directions. MetaCyc's closing prose describes the IspG
conversion in reverse, despite its own `R2L` reaction-layout and the forward
biosynthetic account elsewhere; the explicit layout and independent enzyme
annotations take precedence. Direction metadata records source orientation;
it does not state thermodynamic irreversibility.

The primary [IspH study](https://pubmed.ncbi.nlm.nih.gov/11818558/)
(DOI `10.1073/pnas.032658999`) reports an IPP/DMAPP mixture from an engineered
*E. coli* strain supplied with labelled deoxyxylulose. Its measured 5:1 ratio
is an experimental result, not a fixed physiological stoichiometry. The
[enzyme-mechanism study](https://pubmed.ncbi.nlm.nih.gov/12571359/)
(DOI `10.1073/pnas.0337742100`) reports auxiliary-factor dependence for IspG,
photoreduced-dye activation of purified IspG/IspH, and IspH activation by
flavodoxin, flavodoxin reductase and NADPH. Its 6:1 product ratio under dye
activation is kept distinct from the earlier engineered-cell result. Both
primary abstracts were directly inspected and preserved outside the repository.

## Evidence table

The machine-readable [source projection](mep-source-projection.json) identifies
every source reaction side, retained edge, omitted carrier state, native ordering
relation, catalytic-activity annotation and cofactor assertion. It preserves
source evidence codes and reaction coefficients. The
[source manifest](mep-sources.json) gives exact acquisition URLs and byte hashes.

| Native step | Curated reaction | Catalyst | Disposition |
| --- | --- | --- | --- |
| DXS-RXN | RHEA:12606 | UniProtKB:P77488 | All five chemical-side assertions retained |
| DXPREDISOM-RXN | RHEA:13719 | UniProtKB:P45568 | Biosynthetic right-to-left orientation retained |
| 2.7.7.60-RXN | RHEA:13430 | UniProtKB:Q46893 | Source catalytic annotation retained without inventing an evidence code |
| 2.7.1.148-RXN | RHEA:18438 | UniProtKB:P62615 | Native substrate phosphorylation retained |
| RXN0-302 | RHEA:23865 | UniProtKB:P62617 | Core IspF route retained; side activity RHEA:68364 excluded |
| RXN-15878 | RHEA:43606 | UniProtKB:P62620 | Chemical sides retained; generic flavodoxin states omitted |
| ISPH2-RXN | RHEA:24490 | UniProtKB:P62623 | Direct IPP branch retained; generic ferredoxin states omitted |
| RXN0-884 | RHEA:24827 | UniProtKB:P62623 | Direct DMAPP branch retained; generic ferredoxin states omitted |
| IPPISOM-RXN | RHEA:23285 | UniProtKB:Q46822 | Source-selected IPP-to-DMAPP orientation; additional interconversion |

Cofactor edges preserve the annotated thiamine diphosphate, divalent-metal and
iron-sulfur requirements and their qualification. Metal lists do not imply
simultaneous occupancy or a requirement for all listed alternatives. IspG's
mixed HAMAP/experimental evidence remains distinct from IspH's experimental
annotation. IspH's note about oxygen-associated [4Fe-4S] degradation to [3Fe-4S]
is retained, without promoting the damaged cluster to an equivalent catalytic
cofactor. No missing IspE cofactor comment is interpreted as cofactor absence.

Idi's cytoplasmic location is the only localization edge: UniProt explicitly
cross-references `GO:0005737` with `IEA:UniProtKB-SubCell`. This does not assign
that evidence or location to the other proteins. No unsupported protein-complex
identifier or protein redox state is invented.

## Gaps

Six source carrier-state links are deliberately omitted: reduced/oxidized
flavodoxin for IspG and reduced/oxidized generic ferredoxin for each IspH branch.
The `RHEA-COMP` generic entities are whole redox carriers; their ChEBI
prosthetic-group cross-references are not interchangeable participant IDs.
Moreover, current IspH Rhea/UniProt equations use generic ferredoxin, while the
inspected *E. coli* assay supports flavodoxin-dependent activation. The retained
reaction nodes and edges explicitly describe a partial chemical projection;
they do not select an exclusive physiological donor or claim full balancing.

The graph records presence of reaction participants, not their stoichiometric
multiplicity. Coefficients remain in the source projection. Whole-pathway
compartment, complete complex composition, in vivo flux and universal product
ratios remain outside the evidence-backed record.

Duplicate searches included hidden and ignored files in the entire task
worktree and the original checkout's ignored reports, excluding only Git
internals and virtual environments. Exact native IDs, names/synonyms, reaction
IDs, new protein IDs and PMID identifiers were searched. Prior research listed
this exact pathway as an uncurated cross-Mech candidate (rank 9). The
`DXS-RXN` mention in the prior MetaCyc review belongs to the pyridoxal
5'-phosphate biosynthesis record: sharing the DXP precursor reaction does not
make the downstream MEP pathway a duplicate. The ignored SEED subsystem menu
is a support lead, not a maintained record. No existing exact maintained MEP I
record was found before this addition.

## Candidate YAML

The curated YAML is
[`methylerythritol-phosphate-pathway-i.yaml`](../../../data/pathways/methylerythritol-phosphate-pathway-i.yaml).
It contains 35 participants, nine reactions and 68 edges. Identifier authority
refresh, integrated site generation and repository-wide gates are handled by
the integration task; they are not claimed complete by this research note.

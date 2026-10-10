# Methylphosphonate degradation I — source and scope decisions

Record: [PathBank:SMP0002077](../../../data/pathways/methylphosphonate-degradation-i.yaml).
The native title is **Methylphosphonate Degradation I**, from `PW002065.owl` in
PathBank's public primary BioPAX archive. The member contains one pathway,
four explicitly linked biochemical reactions, four catalysis objects and a
four-protein assembly. The `PW` filename is a PathWhiz identifier; the `SMP`
xref supplies the maintained pathway identifier. The archive was retrieved
2026-10-08 and inspected again for this addition on 2026-10-10. Its server
Last-Modified date is 2019-08-16; no equivalence to a current portal rendering is
assumed.

## Identity and duplicate review

Ignored and hidden files were included in exact-ID, label, synonym, accession,
reaction and PMID/DOI searches in both the original checkout and this worktree,
excluding Git internals and virtual environments. Earlier mentions are the
2026-10-10 research inventory and README, which identify this as a pending
candidate, plus the current batch screening report. No maintained pathway
record matched before this addition. The archived member is source material,
not a pre-existing maintained record. This bounded search does not establish
that all pathway sources have been exhausted.

The native BioSource is **Escherichia coli, NCBITaxon:562**. The maintained
record narrows enzyme provenance to **E. coli K-12, NCBITaxon:83333**, matching
all seven inspected reviewed UniProt records. It does not assert that all
K-12 cells can grow on methylphosphonate. The primary phnE phase-variation
study (PMID:15342581, DOI:10.1128/JB.186.18.6118-6123.2004) shows how transporter
switching can block utilization. Taxon scope is enzyme provenance, not a growth
phenotype or proof of a transport-competent genotype.

## Four reactions and their grounding

| Native member | Directed Rhea | Catalyst represented | Disposition |
| --- | --- | --- | --- |
| `Reactions/6035`, EC:2.7.8.37 | RHEA:34680 | Native PhnG/H/I/L assembly | ATP donates the ribose-triphosphate moiety; adenine is released. |
| `Reactions/6036`, EC:3.6.1.63 | RHEA:34684 | PhnM, UniProtKB:P16689 | Hydrolysis releases diphosphate and ribosyl methylphosphonate monophosphate. |
| `Reactions/6037`, EC:4.7.1.1 | RHEA:34708 | PhnJ, UniProtKB:P16688 | Methane and cyclic ribose-phosphate form; Rhea also records radical-activation reagents and products. |
| `Reactions/6038`, EC:3.1.4.55 | RHEA:34796 | PhnP, UniProtKB:P16692 | Hydrolysis opens the cyclic phosphate to alpha-D-ribose 1,5-bisphosphate. |

PathBank supplies **no Rhea xrefs** in this member. Membership edges therefore
cite native membership separately from the corresponding protein's UniProt
catalytic assignment and the Rhea direction. Correspondence was manually
checked from chemical transformation, stereochemistry, EC and protein evidence;
it is not represented as a source-native crosswalk. All four Rhea directions
are left-to-right. All 22 Rhea side-participant occurrences have coefficient 1,
verified from `rh:contains1` on the source reaction sides.

The older PathBank member mixes neutral and ionic forms. The selected Rhea
forms are CHEBI:68684 methylphosphonate(1-), CHEBI:30616 ATP(4-), CHEBI:68823
RPnTP(5-), CHEBI:68686 PRPn(3-), CHEBI:68687 cyclic PRcP(3-), CHEBI:68688
ribose 1,5-bisphosphate(4-), and CHEBI:33019 diphosphate(3-). Native/selected
labels, formulas, charges, InChI and SMILES are retained in the source projection.
ChEBI definitions independently establish the conjugate forms and alpha-D
stereochemistry. These are **not exact-match mappings between differently
protonated chemical species**. No unsupported `skos:exactMatch` rows are added.

The native `pathwayOrder` property links four step objects but contains no
`nextStep` relation. Array order is not interpreted as biological ordering.
Three `provides_input_for` edges instead connect the shared, identified Rhea
intermediates across the experimentally established sequence.

## Proteins, cofactors and experimental conditions

The first native controller is `ProteinComplex/4049`, preserved as
`PathBank:SMP0002077/ProteinComplex/4049`. It has PhnG (P16685), PhnH (P16686),
PhnI (P16687), and PhnL (P16679). All component xrefs were inspected and
independently resolved at UniProt. No copy numbers are supplied by this native
assembly. Membership does not establish four independent catalysts.
PMID:22089136 directly reconstituted the first reaction with these four proteins
and MgATP after removal of fusion tags; PhnI alone's ATP/GTP nucleosidase
activity is a different reaction and is excluded. The catalytic-edge description and primary evidence retain this MgATP assay
condition. The wording alone does not establish an assembly-level magnesium
cofactor relation or a binding site; no magnesium independence is asserted.

PhnM was assayed with MgCl2 and ZnCl2 in the 2011 study. That condition remains
in its catalytic-edge description; presence in an assay is not converted into
two claims of obligatory cofactors. For PhnJ, the graph includes the independently
annotated [4Fe-4S] cluster and explicitly requires the reduced state and anaerobic
reconstitution. The class CHEBI:49883 does not encode oxidation state. Dithionite
was the experimental reductant; neither CHEBI:17499 (generic hydrogen donor,
Rhea AH2) nor CHEBI:13193 (generic hydrogen acceptor, Rhea A) is assigned an
unestablished physiological molecular identity. They are typed as cofactors,
preserving their generic chemical-entity status in KGX.

Rhea:34708 includes one SAM, one generic AH2, and the associated
5'-deoxyadenosine, methionine and A products. Those exact source coefficients are
retained. They describe the activation-associated reference equation, **not a
proven SAM-to-substrate ratio for repeated physiological turnover**. The later
primary structural study (PMID:26280334, full-text passage offset 8408) discusses
a persistent glycyl radical supporting turnovers without further SAM consumption.
The 2011 primary experiment observed the activation products, but did not
establish the in vivo turnover ratio. A coefficient-free edge schema cannot
model activation and repeated catalytic cycles separately; this limitation is
visible in the record description and affected chemical edges.

PhnP's physiological substrate/product assignment comes from PMID:21341651
(DOI:10.1021/ja1102713), whose indexed primary abstract was inspected. The earlier
PMID:19366688 (DOI:10.1074/jbc.M808392200) characterized structure and
metal-dependent activity on other substrates. Its bis(p-nitrophenyl)phosphate
assay favored Mn2+ and Ni2+ and gave poor activity with catalytic Zn2+ substitution.
The separate, remote Zn2+ site was assigned a structural role. Accordingly,
Mn2+ and structural Zn2+ have separately qualified edges; exclusive manganese
usage and equivalent catalytic zinc usage are not asserted. Full-text attempts
for these two older PhnP studies were unavailable; the evidence ledger identifies
abstract-only review explicitly and does not treat HTML error bodies as papers.

## Later machinery and deliberate exclusions

The native four-protein assembly is not equated to the later Phn(GHIJ)2 core or
the Phn(GHIJKL)2 complex. The full 2015 and 2023 primary articles were inspected.
PMID:36813778 (DOI:10.1038/s41467-023-36604-y) identifies PhnK/PhnL double-dimer
ATPase remodeling and shows that ATPase-disrupting mutations prevent growth on
phosphonates. PhnK resolves to UniProtKB:P16678; its current UniProt text still
contains an older unknown-function statement. That text is not adopted as the
current state of knowledge. The newer whole-utilization phenotype does not by
itself establish a PhnK `enables` edge to a particular reaction of this bounded
four-step record. PhnK and the larger complex therefore remain explicit context,
without a fabricated controller, reaction or composition edge.

Other deliberate exclusions are transport by PhnCDE, regulation by PhnF,
aminoalkylphosphonate acetylation by PhnO, alternative phosphonate substrates,
the PhnI-only nucleosidase side reaction, experimental tags/proteases and
auxiliary assay reagents, and downstream PhnN conversion to PRPP. The endpoint
is ribose 1,5-bisphosphate and methane; the graph does **not** claim release of
free inorganic phosphate. No localization or growth edge is inferred from
sequence annotation or pathway naming.

The current-session canonical iModulonDB search of `e_coli/precise_mg1655` returned
10 `phn` gene matches and zero iModulon matches. It is computational gene context,
not evidence of catalysis, regulation, growth or absence of unreturned genes.
The raw root-managed adapter output is
`/private/tmp/pathwaymech-frl-phn-imodulondb-phn.md`.

## Evidence artifacts and validation

The identifier handoff lists every target node and reference ID. The source
projection retains native objects, independent Rhea side/coefficients,
protein assignments, chemical-form decisions and bounded primary-source
assessments. The source manifest records URLs, dates, versions and hashes,
including exact artifact scope and rejected retrievals. Complete source
downloads remain outside the repository. Public-release data licensing remains
separately tracked under the user's authorized local-ingestion scope.

Native and closed LinkML validation pass for this record. The final narrow
validation receipt records source-side coverage and quotes. Root owns authority
snapshot integration, rendering, history, whole-corpus gates and the independent
scientific/adversarial review before publication.

## Adversarial correction #317

[Issue #317](https://github.com/CultureBotAI/PathwayMech/issues/317) identified
that the MgATP assay condition did not by itself support the previously asserted
assembly-to-Mg2+ `has_cofactor` edge. Edge 031 and its otherwise-unused magnesium
participant were removed; edge 027 retains the exact source evidence and assay
condition. Remaining edge IDs are stable. The corrected record contains
27 participants, four reactions and 40 edges, with all 22 reaction-side
occurrences unchanged. The final validation receipt was rerun on these bytes.

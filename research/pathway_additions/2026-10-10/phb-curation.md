# Pathway mechanism research: polyhydroxybutanoate biosynthesis

## Pathway scope

- Record: `MetaCyc:PWY1-3`, `data/pathways/polyhydroxybutanoate-biosynthesis.yaml`.
- Organism: `NCBITaxon:381666`, Cupriavidus necator H16. The primary papers use
  the older names Alcaligenes eutrophus H16 and Ralstonia eutropha H16.
- Scope: the core PhaA-PhaB-PhaC biosynthetic route from acetyl-CoA to PHB,
  represented by three reactions and twenty evidence-backed edges.
- This is a follow-up to the missing-pathway lead in
  `research/cross_mech/2026-10-05-uniprot-protein-links.md`. Searches included
  ignored and hidden files in the original checkout and the task worktree;
  the prior cross-Mech protein inventory and ignored support data are leads,
  not duplicate maintained pathway records. Exact searched terms and all
  record identifiers are in `phb-source-manifest.json`.

## Mechanistic summary

PhaA (`UniProtKB:P14611`) condenses two acetyl-CoA molecules to
acetoacetyl-CoA, releasing CoA. PhaB (`UniProtKB:P14697`) reduces that product
using NADPH and a proton, yielding the R-configured hydroxybutanoyl-CoA and
NADP. PhaC (`UniProtKB:P23608`) incorporates the monomer into a PHB chain and
releases CoA. The three biosynthetic directions were inspected in Rhea 142;
the pathway sequence was independently inspected in MetaCyc 22.5 XML.

The exact H16 proteins resolve at UniProt, with strain identity preserved.
The original gene-characterization experiment supports the thiolase and
reductase identities ([PMID:2670935](https://pubmed.ncbi.nlm.nih.gov/2670935/)).
PhaB biochemical and structural experiments establish the participation of
NADPH and acetoacetyl-CoA ([PMID:23913421](https://pubmed.ncbi.nlm.nih.gov/23913421/)).
Native-organism purification and polymerization assays support PhaC function;
the paper distinguishes initiation from elongation and studies tagged H16
derivatives ([PMID:22369488](https://pubmed.ncbi.nlm.nih.gov/22369488/)). Its
full text and strain-construction passage were inspected in the NCBI BioC
artifact. Statements are not attributed to wild-type-only experiments.

## Evidence table

| Subject | Predicate | Object | Source and boundary |
| --- | --- | --- | --- |
| Acetyl-CoA | consumes | `RHEA:21037` | Directed Rhea equation explicitly has coefficient 2; the graph does not encode coefficients as edge multiplicity. |
| `RHEA:21037` | produces | Acetoacetyl-CoA and CoA | Rhea substrates/products; MetaCyc reaction layout selects condensation although the native reaction family is reversible. |
| Acetoacetyl-CoA, NADPH and hydron | consumes | `RHEA:45798` | The right-to-left member of the Rhea master equation matches MetaCyc's biosynthetic layout. |
| `RHEA:45798` | produces | R-hydroxybutanoyl-CoA and NADP | Explicit R stereochemistry and chemical charge identities retained. |
| R-hydroxybutanoyl-CoA and PHB(n) | consumes | `RHEA:15406` | Polymer substrate is native `POLYMER:14464`, underlying `CHEBI:8298`. |
| `RHEA:15406` | produces | PHB(n+1) and CoA | Polymer product is native `POLYMER:14465`, also underlying `CHEBI:8298`. |
| PhaA, PhaB and PhaC | catalyzes | Their respective reaction | Exact UniProt activity/function fields plus inspected short primary excerpts; individual annotation evidence codes are preserved. |
| Each reaction | part_of | `MetaCyc:PWY1-3` | Native three-member reaction list and crosswalks. |
| Condensation then reduction | precedes | Reduction then polymer extension | Native predecessor statements; shared metabolites independently match Rhea. |

`phb-source-projection.json` retains all three source equations and each
participant/coefficient, native polymer states, pathway layouts, selected
protein assertions, and the disposition of every maintained edge.
`phb-source-manifest.json` gives fetched URLs, dates, raw hashes and introduced
identifiers. Raw downloads remain outside the repository. The Rhea digest is
for the compressed source artifact at its recorded FTP URL.

## Gaps

The schema has no polymer-instance or coefficient slots. Both chain states
therefore use the generic chemical class `CHEBI:8298`; the input/output edge
descriptions and evidence retain n versus n+1. This is a class-level graph,
not an atom-mapped or stoichiometric model. The explicit `polymer` category
exports PHB as `biolink:ChemicalEntity`, retaining `source_category: polymer`,
and gives it chemical styling in the record diagram. This fixes the CHEBI
prefix fallback to small molecule identified in
[#315](https://github.com/CultureBotAI/PathwayMech/issues/315). No unsupported
polymer CURIE was minted.

PhaC's UniProt catalytic-activity evidence is `ECO:0000250` (similarity),
whereas its function annotation includes `ECO:0000269`. The record preserves
that distinction and adds independently inspected experimental evidence.
Rhea chemistry alone does not establish activity in H16.

The selected core route is not an exhaustive H16 isoenzyme inventory.
PhaB paralog experiments show condition-dependent contributions beyond the
core operon ([PMID:20729355](https://pubmed.ncbi.nlm.nih.gov/20729355/)); neither
PhaB2 nor PhaB3 is asserted absent. Their mapping and contextual activity are
reserved for a later extension. Granule assembly, PhaP/PhaM interactions,
regulation, degradation, copolymers, catalytic intermediates, and a definitive
initiation mechanism are outside this record. NADPH is represented as a
consumed cosubstrate, not as an inferred permanently bound cofactor.

## Verification

Native `validate_record` and closed-LinkML `strict_errors` validation passed
on this one record. Source-to-graph chemical coverage and the exact primary
excerpts were checked locally. Shared identifier snapshot regeneration,
generated pages, whole-corpus gates, and independent review belong to the
parent task and remain required before publication. No biological tests,
page render or whole-corpus gate was run by this subtask.

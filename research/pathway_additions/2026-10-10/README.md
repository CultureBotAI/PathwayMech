# Pathway additions and remaining candidates — 2026-10-10

This batch follows the repository's add-pathway workflow for two exact microbial
routes. It is an incremental addition, not a claim that the sources are exhausted.
The starting corpus contains 157 records; these two additions bring it to 159.

| Pathway | Maintained record | Scope and retained limitation |
| --- | --- | --- |
| `MetaCyc:PWY1-3` — polyhydroxybutanoate biosynthesis | [PHB YAML](../../../data/pathways/polyhydroxybutanoate-biosynthesis.yaml) | Core PhaA/PhaB/PhaC route of Cupriavidus necator H16; polymer n and n+1 remain explicit in evidence and descriptions of a shared chemical-class node. |
| `MetaCyc:NONMEVIPP-PWY` — methylerythritol phosphate pathway I | [MEP YAML](../../../data/pathways/methylerythritol-phosphate-pathway-i.yaml) | E. coli K-12 route, including both direct IspH product branches and Idi interconversion; unresolved carrier-state nodes and differences between generic reaction chemistry and organism-specific donor evidence remain explicit. |

The pathway-specific curation notes, source projections and manifests in this
directory record exact identifiers, edge dispositions, primary literature,
source URLs, versions and raw artifact hashes.
[record-identifiers.json](record-identifiers.json) lists every identifier in the
two additions and the 31 node IDs newly introduced to the maintained corpus. The complete downloads remain
outside the repository. The generated record pages include the network diagrams
introduced in PR #310.

## Source coverage and next work

[candidate-inventory.json](candidate-inventory.json) freezes the starting corpus,
30-source inventory, inspected PathBank archive counts and exact duplicate-search
scope. All OWL members of the 2,687-member archive were parsed. Of 528 files with
explicit microbial BioSources, 205 contain exactly one Pathway object and at
least two biochemical reactions. These are screening candidates, not 205 unique
approved pathways. The 265 multiple-pathway files require native membership
selection before their graphs can be evaluated.

The strongest next leads are:

- `GO:1901281`, fructoselysine catabolism in E. coli: purified two-enzyme evidence
  in PMID:12147680; optional psicoselysine extension needs separate scope review.
- `PathBank:SMP0002077`, methylphosphonate degradation I: four-step source route,
  with primary support in PMID:22089136 and PMID:19366688. First maintained
  PathBank use also needs an independently sourced authority extractor/policy.
- `MetaCyc:DENITRIFICATION-PWY`: choose a single experimentally grounded organism
  and nitrate/nitrite reductase route; do not merge alternative enzyme systems.
- `MetaCyc:DISSULFRED-PWY`: retain the DsrC trisulfide intermediate and inspect
  PMID:26680199; older support tables collapse this mechanistic distinction.
- `MetaCyc:CALVIN-PWY`: a bounded cyanobacterial cycle is a candidate, with
  Synechocystis evidence in PMID:31470115; separate adjacent carbon reactions.

Other PathBank leads and source defects are retained in the inventory. In
particular, the archived tetrahydromonapterin candidate contains an apparent
wrong chemical cross-reference and must not be promoted unchanged. Curcumin's
two reactions are catalyzed by one enzyme and require scope adjudication under
the add-pathway skill. Prior radicicol (`MIBiG:BGC0002887`) and kotanin
(`MIBiG:BGC0003126`) leads still need evidence/strain reconciliation.

Duplicate searches included hidden and ignored files in the original checkout
and task worktree, excluding Git internals and virtual environments. Existing
research and ignored support-table mentions were inspected as prior leads. An
unavailable source or unreviewed archive member is not evidence of absence.

## Authority inputs and review corrections

All four preserved Semantic SQL authority databases match their committed
SHA-256 values: GO 2026-07-26, ChEBI 255, NCBITaxon 2026-07-12 and Rhea 139.
The new mechanistic equations come from independently downloaded Rhea 142 RDF;
its source manifest identifies those bytes separately from the Rhea 139 label
snapshot. The selected directed reaction identities agree across these inputs.

Of the original 90 source-manifest inputs, 34 were recovered byte-for-byte and
56 official downloads had changed bytes. The source parsers found all 81 selected
terms from those 56 inputs with unchanged labels and synonyms. A full rebuild
before new-record integration also reproduced all 1,560 existing source terms
exactly. [authority-refresh.json](authority-refresh.json) records old/new hashes
and versions. This is an identifier-provenance refresh, not a new scientific
review of the existing pathways. Six new authority inputs cover the two exact
MetaCyc pathway titles and eleven UniProt proteins.

The adversarial review identified and corrected four defects:

- [#312](https://github.com/CultureBotAI/PathwayMech/issues/312): refresh the
  Reactome hash-scope descriptions to identify successful live downloads.
- [#313](https://github.com/CultureBotAI/PathwayMech/issues/313): distinguish native
  PHB pathway membership from its Rhea crosswalk evidence, and identify the
  direction-table hash as plain TSV.
- [#314](https://github.com/CultureBotAI/PathwayMech/issues/314): preserve coefficients
  from Rhea side-level `containsN` assertions in the MEP evidence and source ledger.
- [#315](https://github.com/CultureBotAI/PathwayMech/issues/315): add explicit polymer
  typing so PHB exports as a chemical entity instead of inheriting the small-molecule
  prefix fallback. The node category does not encode individual chain lengths.

The integrated [verification receipt](verification.json) records passing whole-corpus
validation, 1,008 passing tests (3 skipped), lint, vendored sync, and the 88-edge
export/SVG audit. The pathway notes preserve the authors' earlier narrow checks
separately. Independent scientific reviews are saved under `reviews/structured/`.

The completed independent reviews both pass with explicit scientific limitations
and no remaining findings:

- PHB: [Markdown](../../../reviews/structured/20261010T210052Z-phb-independent-review/review.md) · [YAML](../../../reviews/structured/20261010T210052Z-phb-independent-review/review.yaml).
- MEP I: [Markdown](../../../reviews/structured/20261010T210026Z-mep-i-independent-review/review.md) · [YAML](../../../reviews/structured/20261010T210026Z-mep-i-independent-review/review.yaml).

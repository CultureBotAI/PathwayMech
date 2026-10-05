---
name: cross-mech-protein-links
description: Inventory the UniProt proteins that sibling Mechs (TraitMech, ProteinTraitsMech, NaturalProductMech, AntibioticMech, CellStructureMech) hold, join them to PathwayMech pathway participants, find pathways PathwayMech is missing, check that sibling records link back to PathwayMech, and propose PathwayMech proteins as sibling examples where each Mech's rules allow. Use for cross-Mech protein and pathway-link audits and their follow-up curation plans, not for adding one pathway (use add-pathway).
allowed-tools: Bash, Read, Grep, Glob, WebFetch, Edit, Write
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Cross-Mech Protein Links

Use inside the PathwayMech repository. The goal has three parts:

1. every pathway that a sibling Mech's proteins belong to has a PathwayMech
   record, or is listed as a ranked gap;
2. sibling records that concern a PathwayMech pathway link to that record;
3. PathwayMech proteins become sibling examples where they fill a real gap
   and the sibling's own evidence rules are met.

The deterministic part is `just cross-mech-proteins`. Everything it emits is a
curation lead. A shared accession shows that a protein participates in a
pathway, not that a sibling record's claim is about that pathway.

## Read First

- `CLAUDE.md` and `docs/IDENTIFIERS.md`. A new PathwayMech record needs
  authority-snapshot coverage for every new identifier, not only a valid prefix.
- `conf/sibling_mechs.yaml`: the slots each sibling uses for proteins and
  PathwayMech links. Update it when a sibling adds or moves a slot.
- The newest report under `research/cross_mech/`. The first one,
  `research/cross_mech/2026-10-05-uniprot-protein-links.md`, maps each sibling's
  schema, validators, and rules in detail.
- Each sibling's `CLAUDE.md`, schema, and curation docs before proposing an
  edit there. Sibling rules win inside sibling repositories.

## Boundaries

- Read sibling records at a pinned commit (`--ref origin/main`) or from a clean
  checkout of their default branch. A sibling checkout may sit on a feature
  branch with someone else's work: never edit, stash, or switch it. Make your
  own branch or worktree in that repository for any change.
- One pull request per repository. Each follows the user's git workflow:
  branch first, PR, separate adversarial review, findings filed as issues, no
  merge without explicit approval.
- Never invent an accession, a PathwayMech record id, or a label. Resolve
  UniProt entries (reviewed status, organism node, recommended name, gene
  names) before writing them anywhere. Call UniProt anonymously.
- PathwayMech pathway membership is not evidence for a sibling claim. Cite the
  primary source each sibling requires.
- Organism scope matters. Most PathwayMech yeast records are S. cerevisiae
  S288C (NCBITaxon:559292) and the E. coli records are species level
  (NCBITaxon:562). A yeast pathway is a fair link for a fungal ergosterol
  target and an overclaim for a bacterial folate target.
- Do not edit claw-governed files in any Mech.

### Sibling rules that decide what is allowed

| Mech | Protein examples | PathwayMech link |
|---|---|---|
| TraitMech | `causal_graphs[].nodes[].protein_examples[]` on GENE_OR_PROTEIN nodes only. Needs the UniProt organism taxon (usually strain level), entry status, role, and primary evidence with reference, verbatim snippet, and notes. Append, never prepend. Respect `DO_NOT_WORK.md`. | No slot today. Proposed: node-level CrossCorpusLink `related_records` (schema change, rendering, tests, docs, history record). Record-level `xrefs` are exact equivalences only. |
| CellStructureMech | `components[].protein_examples[]`: membership of a component in the structure, evidenced by UniProt localisation PMIDs, the UniProt entry, or a primary paper. Taxon must be one the record names. Never `complex_compositions` (source import). | No slot today. A link slot needs schema, checker, page-coverage probe, template, source-queue row, and docs. |
| AntibioticMech | Only on curator-owned targets (`source` PRIMARY_LITERATURE or CURATOR). BindingDB, CARD, and PHI-base items are source-owned and are reverted by re-seed. The parent target's citation must concern that protein and organism. | No slot today. A curator-owned `related_records` must be added to the seeder's `CURATOR_FIELDS`, or the next seed drops it. |
| NaturalProductMech | Curated `biosynthetic_pathway` steps or causal-graph nodes only, for the producer's own protein of this compound's pathway. Bioactivity targets of compounds with an AntibioticMech record belong there. | `related_records` (CrossCorpusLink) exists but is seeder-computed from a pinned sibling inventory. Never hand-add; add an extractor, a `conf/sibling_pins.yaml` pin, and a relation value. |
| ProteinTraitsMech | Only through its release-pinned candidate, resolve, review, and promote workflow, with explicit human authorization for `--apply`. Hand-added examples are forbidden. Hand over candidates instead. | `trait_relations` on unbound records through a registered in-place editor. Never touch records bound in `data/grounding` receipts. |

## Workflow

### 1. Inventory

```bash
just cross-mech-proteins --mechs-root /path/to/Mechs --ref origin/main \
  --sgd-map <dir>/inputs/sgd_uniprot.json --fetch-sgd-map \
  --annotations <dir>/inputs/uniprot_annotations.json --fetch-annotations \
  --out <dir>
```

`<dir>` is `research/cross_mech/<YYYY-MM-DD>/`. The command writes:

- `sibling_proteins.tsv`: every accession in a configured sibling slot;
- `overlaps.tsv`: sibling proteins that are PathwayMech participants, and
  whether the sibling record already links that pathway;
- `reaction_matches.tsv`: sibling proteins that share a Rhea reaction or a
  complete EC number with a pathway;
- `link_checks.tsv`: every sibling PathwayMech link and whether it resolves;
- `example_candidates.tsv`: PathwayMech proteins of linked or overlapping
  pathways that the sibling does not hold;
- `summary.md`.

Keep the SGD map limited to the SGD ids the corpus uses, and record each
sibling's commit (the command prints them) in the report. With `--ref`, the
command reads git objects and never the working tree.

### 2. Judge the leads

Rank match bases from strongest to weakest: a shared accession, a Rhea
reaction stated in the record (`record_rhea`), a Rhea reaction of a pathway
participant (`participant_rhea`), then complete EC numbers (`record_ec`,
`participant_ec`). Reject:

- matches through promiscuous or side-activity annotations;
- mammalian or plant proteins matched to a microbial pathway (PathwayMech is
  microbial);
- upstream artifacts, such as a target mislabelled with another organism or
  a reporter protein listed as a drug target;
- links that name a related but different route, such as urease against
  yeast urea amidolyase or dissimilatory against assimilatory sulfate
  reduction.

Then group the surviving leads by pathway.

### 3. Corresponding pathways in PathwayMech

For each sibling protein or record whose pathway has no PathwayMech record,
add the pathway to a ranked gap list. Rank by sibling demand (records and
Mechs that need it), microbial scope, and source availability. Add a pathway
only with `.claude/skills/add-pathway/SKILL.md`, one record per pathway. Every
new identifier must already be covered by `data/identifier_authorities/`, or
the snapshot must be refreshed under `docs/IDENTIFIERS.md`. If the refresh is
blocked, file an issue that names the blocker. Never weaken the gate to land a
record.

### 4. PathwayMech links in sibling Mechs

Link value: the PathwayMech record `id`, verbatim (for example
`WikiPathways:WP5060`), with `corpus: PathwayMech` and the PathwayMech commit
it was read from. The page is
`https://culturebotai.github.io/PathwayMech/pages/records/<id with ':' and '/' replaced by '_'>.html`.
Sibling checks can verify links against the published
`pages/pathway_index.json`, which lists every record's id, label, page, taxa,
protein participants, and reactions. Choose the PathwayMech record by
organism as well as by name: one pathway family can have separate yeast and
E. coli records.

### 5. Examples

Propose an example only where it fills a gap the sibling cares about. Typical
gaps are no microbial example, a deleted or unreviewed accession, or no
example on a mechanistic node. The example must also satisfy the table above.
For ProteinTraitsMech, write candidate rows for its own review workflow
instead of editing records.

### 6. Verify

Re-run step 1 against the sibling branches (`--mech NAME=PATH` or
`--ref <branch>`) with `--check-links`. Confirm that the new links resolve and
that the overlap and link counts moved. Then run each sibling's own gates and
PathwayMech's `just validate`, `just test`, `just lint`, and `git diff --check`.

## Report

Name the report folder and its sibling commits. Give per-Mech counts (slot
values, distinct accessions, overlaps, links, broken links). List:

- the links added or proposed, with relation and evidence;
- the examples added or proposed;
- the ranked pathway gaps, and which ones were added;
- the leads rejected, and why;
- every PR and issue opened, with the checks that passed or could not run.

## Related

- `.claude/skills/add-pathway/SKILL.md` adds a gap pathway.
- `.claude/skills/review-yaml-record/SKILL.md` reviews a linked record.
- `.claude/skills/review-open-issues/SKILL.md` triages the follow-up issues.

# PathwayMech Curation Notes

## Scope

PathwayMech records describe mechanistic microbial pathways. A record should
cover one pathway, its molecular or physiological participants, ordered or
causal reactions, and the evidence supporting each causal edge.

Use stable CURIEs whenever possible:

- `GO` for biological processes.
- `gomodel` for GO-CAM activity nodes in imported drafts.
- `MetaCyc` and `KEGG` for pathway and reaction references.
- `MIBiG` for biosynthetic gene cluster drafts and seed rows.
- `ModelSEED`, `BiGG`, and `BV-BRC` for support seed rows.
- `CHEBI` and `LIPIDMAPS` for metabolites, lipids, and cofactors; `CAS`,
  `ChemSpider`, `HMDB`, and `PubChem` for imported pathway-diagram chemical
  xrefs that still need ChEBI review.
- `EC`, `Ensembl`, `Entrez`, `NCBIProtein`, `SGD`, `TubercuList`, and
  `UniProtKB` for enzymes, genes, and proteins.
- `GO_REF` and `ECO` for GO-CAM evidence references and evidence codes.
- `Reactome` and `PathBank` for BioPAX fixture draft IDs.
- `WikiPathways` for GPML pathway and interaction draft IDs.
- `NCBITaxon` or `GTDB` for organism scope.
- `PMID` and `DOI` for primary evidence.

## Local Skills

- `.claude/skills/add-pathway/SKILL.md` - add one named microbial pathway as a
  `data/pathways/` YAML record with edge-level evidence.
- `.claude/skills/source-triage/SKILL.md` - evaluate reusable pathway sources
  and keep `conf/sources.yaml` aligned with source-discovery research.
- `.claude/skills/review-yaml-record/SKILL.md` - review one pathway YAML
  record without editing it.
- `.claude/skills/review-yaml-category/SKILL.md` - review a coherent cohort of
  pathway records without editing them.
- `.claude/skills/review-open-issues/SKILL.md` - triage the full open-issue
  queue without mutating GitHub unless explicitly asked.

## Record Contract

Keep each YAML record in `data/pathways/`.

Each `mechanistic_edges` entry must:

- use a predicate from the local schema;
- connect nodes declared in the same record;
- cite at least one `references` entry by `reference_id`;
- quote only short supporting snippets.

Records must fit the closed LinkML schema in
`src/pathwaymech/schema/pathwaymech.yaml`: a key it does not declare is an
error, not an extension. Adding a field means changing that schema (and, where
it has a rule, `src/pathwaymech/schema.py`), in the same pull request. Do not
add an `__init__.py` to `src/pathwaymech/schema/`: it would shadow the module
`schema.py`.

The strict validator is the source of truth:

```bash
just validate
```

A record may carry an optional `curation_history`: a list of `CurationEvent`
entries (the same shape TaxonMech uses), each with a quoted RFC 3339
`timestamp` that has a timezone, such as `'2026-09-28T12:00:00Z'`, and starts
`20YY-` (the fleet's shared year guard), plus optional `curator`, `action`,
`changes` and `llm_assisted`. No recipe appends events yet.

## Governed files

These 14 files are vendored byte-identical from
[culturebotai-claw](https://github.com/CultureBotAI/culturebotai-claw) at the
full commit pinned in `scripts/.vendored_canon_ref` (itself governed):

- `scripts/check_vendored_sync.py`, `scripts/check_vendored_sync.sh`
- `scripts/validate_id_label_correspondence.py`, `scripts/chem_formula.py`
- `scripts/deep_research_contract.py`: claw's research-provider contract. It
  is not PathwayMech's report-heading checker, which is the
  `pathwaymech-deep-research-contract` command (`just validate` runs it).
- `tests/test_skill_frontmatter.py`, `tests/test_curation_timestamp_schema.py`,
  `tests/test_id_label_empty_adapter.py`,
  `tests/test_id_label_unknown_prefix.py`, `tests/test_id_label_plausibility.py`
- `src/pathwaymech/schema/history.yaml`, `src/pathwaymech/schema/mech_shared.yaml`
- `prompts/backlog-loop-goal.md`
- `.github/workflows/pr-shepherd.yml`

Never edit one here. Change it in claw and re-pin. `just vendored-check` (the
`vendored-sync` workflow) fails on any local drift. PathwayMech's own gates and
data rules for the backlog loop are in `prompts/backlog-loop-local.md`.

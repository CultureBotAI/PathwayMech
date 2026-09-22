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
- `CHEBI` for metabolites and cofactors.
- `SGD` for Saccharomyces Genome Database gene products from GO-CAM.
- `EC` and `UniProtKB` for enzymes.
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

The strict validator is the source of truth:

```bash
just validate
```

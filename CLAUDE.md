# PathwayMech Curation Notes

## Scope

PathwayMech records describe mechanistic microbial pathways. A record should
cover one pathway, its molecular or physiological participants, ordered or
causal reactions, and the evidence supporting each causal edge.

Use stable CURIEs whenever possible:

- `GO` for biological processes.
- `MetaCyc` and `KEGG` for pathway and reaction references.
- `CHEBI` for metabolites and cofactors.
- `EC` and `UniProtKB` for enzymes.
- `NCBITaxon` or `GTDB` for organism scope.
- `PMID` and `DOI` for primary evidence.

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

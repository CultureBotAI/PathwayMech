# PathwayMech record review checklist

Use this checklist to make claim-level review and curation decisions for one
PathwayMech record (`data/pathways/*.yaml`). It is not a requirement to populate
every optional slot.

## Field-by-field audit

| Area | Verify | Complete enough when |
|---|---|---|
| Identity | Primary identifier, label/name, and upstream groundings agree with `src/pathwaymech/schema/pathwaymech.yaml`. | The record denotes one unambiguous entity and satisfies `manage-identifiers`. |
| Ontology & CURIEs | Every CURIE resolves and carries its canonical ontology label. | Verified against `id-label-correspondence` and `just validate-strict`. |
| Evidence | Every scientific assertion cites an inspected primary source (`PMID`, `DOI`, or authoritative database accession) with accurate scope. | Snippets are verbatim, notes hold interpretation, and no claim is inflated beyond the studied system. |
| Provenance & History | Maintained vs generated ownership is respected and history is recorded through repository tooling. | `just validate` passes with zero errors. |

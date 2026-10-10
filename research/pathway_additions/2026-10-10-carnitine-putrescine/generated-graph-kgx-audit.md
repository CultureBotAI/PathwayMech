# Generated SVG and KGX integration audit

Result: **passed**, with no artifact defects found. The audit compared both frozen YAML records against actual rendered HTML/SVG and KGX artifacts. It did not render pages or change records.

| Record | Local named nodes | SVG nodes | Assertions | Evidence blocks |
| --- | ---: | ---: | ---: | ---: |
| PathBank:SMP0002051, L-Carnitine Degradation I | 25 | 24 | 32 | 53 |
| PathBank:SMP0002067, Putrescine Degradation II | 30 | 29 | 38 | 59 |
| Total | 55 | 53 | 70 | 112 |

All 70 assertions retain their subject, predicate, object, description, complete evidence and complete reference metadata. SVG edge links resolve to the corresponding evidence rows; each evidence reference resolves to its citation. Node links, labels, categories and source reaction directions match the records. Every checked node box, path and label coordinate lies within SVG bounds, and paths connect the corresponding source/target boxes. The two scope-only taxon declarations remain in component tables and KGX; neither is an asserted graph endpoint.

The 55 local declarations resolve to 51 distinct KGX nodes. Their complete source contexts were compared against declarations throughout the corpus, preserving any shared-node category unions. The generated download manifest hashes and row counts match the files. Both `nodes.tsv` and `edges.tsv` are **byte-identical** to the separately completed CLI export at `/private/tmp/pathwaymech-carnitine-putrescine-kgx`.

Whole carrier states remain separate: RHEA-COMP10686 is the reduced protein input and RHEA-COMP10685 the oxidized protein output of RHEA51586. They are distinct `biolink:Protein` nodes and protein SVG nodes. CaiA-bound FAD/CHEBI57692 retains its separate cofactor context.

The [JSON receipt](generated-graph-kgx-audit.json) preserves the exact invocation, exit0 result, audit-script hash, target record/page hashes, KGX hashes and coverage. The command ran with the repository environment and returned exit0.

**No visual browser preview or interaction testing was performed:** CUA reported no available apps or browsers. This programmatic structural audit does not establish scientific correctness of the underlying source assertions; scientific reviews and repository-wide gates are separate.

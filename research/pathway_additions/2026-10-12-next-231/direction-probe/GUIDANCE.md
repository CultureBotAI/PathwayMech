# Six reaction directions: verified native contract

The six original MetaCyc Reaction objects each have exactly one `/ptools-xml/Reaction/reaction-direction`, whose value is `REVERSIBLE`. Their full original file hashes, source-local frame joins and all twenty native side occurrences were rechecked in `result.json`. Set the existing six YAML `reactions[*].direction` fields to the native supported value **`reversible`**. No graph or renderer implementation change is needed.

| Reaction | Native reaction direction | Native pathway layout |
|---|---|---|
| MetaCyc:RXN-21730 | REVERSIBLE | L2R |
| MetaCyc:SEDOBISALDOL-RXN | REVERSIBLE | L2R |
| MetaCyc:RIB5PISOM-RXN | REVERSIBLE | R2L |
| MetaCyc:RIBULP3EPIM-RXN | REVERSIBLE | L2R |
| MetaCyc:1TRANSKETO-RXN | REVERSIBLE | R2L |
| MetaCyc:2TRANSKETO-RXN | REVERSIBLE | L2R |

Pathway layout orientation and reaction reversibility are separate fields. Preserve the existing pathway-oriented chemical-side assertions, including the two R2L layouts. Do not add reverse edges or change arrows to depict reversibility.

## Precise successor assertions

1. The reaction-ID set is exactly these six IDs, with exactly six nodes, each `direction == "reversible"`. Native `validate_record(raw)` and `validator().validate(raw, TARGET_CLASS)` both pass. Native code permits direction only on reactions; the allowed values are `left_to_right`, `right_to_left`, `reversible`.
2. Compare the old and successor `(subject, predicate, object)` triples as lists or multiplicity-preserving counters: all 51 graph assertions remain. The subset with `predicate in {"consumes", "produces"}` has exactly 20 occurrences and remains exact.
3. Generate the native page using `cli._record_page(validate_record(raw))`. For every reaction, select `a[@data-node-id=<exact ID>]`: its direct SVG `title` and its `aria-label` must contain `Source reaction direction: reversible`. Follow its `href` to the component-table row and assert the third `td` is exactly `reversible`.
4. Generate the standalone graph using `graph_view.graph_html(checked, {}, {})`; assert the same six node title/ARIA values. There is no new `data-direction` attribute. Direction is node metadata, not replacement edge polarity. For SVG edge comparisons, use `data-subject-id` / `data-object-id` when present, falling back to `data-subject` / `data-object`: qualified display instances otherwise differ from biological IDs.
5. Generate standalone export with `kgx.render_kgx([checked])`. Parse `nodes.tsv`; each six-node row has `direction == "reversible"`. Parse its `source_contexts` JSON and select the entry with `record_id == "MetaCyc:PWY-8178"`, `collection == "reactions"`, and the exact node `id`; that entry also has `direction == "reversible"`.
6. For a merged-corpus KGX export, the target-specific `source_contexts` assertion is essential. If another record gives the shared reaction a conflicting source direction, the aggregate node `direction` is deliberately blank while both record-local values survive. The bounded collision fixture demonstrates this behavior.

The isolated direction-only overlay leaves `edges.tsv` byte-identical. This is **not** an expected comparison for the whole scientific successor, which also changes evidence and construct descriptions. For the complete successor use the exact triple-preservation checks; if desired isolate the direction effect by comparing it against an in-memory clone differing only by removal of the six direction fields.

## Evidence and limits

`probe.py` replayed the immutable original target SHA `a5fb4208601109e5939577f84276a0fbe6ff28a324fa40a4b057b7bfe338e35a`, then added the six fields in memory. It did not author or alter a successor. Native/LinkML, native page, standalone graph, KGX and source-context checks passed. Three semantic negative controls reject missing metadata, one wrong-but-schema-valid direction and an altered side orientation.

Inspected native contracts: `schema.py` lines 246–251; `schema/pathwaymech.yaml` NamedNode.direction and ReactionDirectionEnum; `cli.py` lines 1094–1123; `graph_view.py` lines 57–58, 312–339; `kgx.py` lines 133–160 and 220–256. The exact code bodies are bound in `bindings.json`. No full suite, full render, maintained files, cache, Git or sealed inputs were changed. Actual successor review remains parent/root-owned.

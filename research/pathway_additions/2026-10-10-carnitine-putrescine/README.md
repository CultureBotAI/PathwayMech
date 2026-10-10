# Carnitine and putrescine pathway curation

This batch adds two bounded E. coli K-12 pathway networks to the 161-record
baseline at `5766cf2fe227afc248a72e455f74f4c5ddda9d97`:

| Record | Scope | Reactions | Edges |
| --- | --- | ---: | ---: |
| `PathBank:SMP0002051`, L-Carnitine Degradation I | Initial CoA activation and anaerobic CaiD/CaiA/CaiB recycling; distinct whole ETF redox states | 4 | 32 |
| `PathBank:SMP0002067`, Putrescine Degradation II | PuuA/B/C/D glutamylation core from putrescine to GABA | 4 | 38 |

[The complete identifier ledger](record-identifiers.json) lists all named nodes,
reference IDs, source URLs and record hashes. The carnitine and putrescine
curation notes, source projections, manifests and validation receipts preserve
every retained assertion, source conflict, exclusion and authority version.
Exact duplicate searches included ignored and hidden files in both the original
repository and the isolated worktree; Git internals, virtual environments and
bytecode were excluded. Earlier mentions were pending research or support rows,
not maintained records of these exact routes.

Native PathBank BioPAX members establish pathway and complex identities. Current
reviewed UniProt annotations, primary literature and exact Rhea/ChEBI objects
supply catalytic assignments, chemical forms, direction, stoichiometry and
cofactor evidence. Incorrect native chemical structures and cross-references are
explicitly rejected. Rhea142 reaction evidence and Rhea139 label authority are
versioned separately. The three older putrescine papers and several carnitine
papers were inspected through indexed primary abstracts; broader claims are
bounded by that access limit.

[Authority integration](authority-integration.json) preserves every existing
term and source assertion. The source manifest grows from 97 to 100 inputs:
two native PathBank members and pinned Rhea142 RDF for whole generic protein
components. Eight historical ChEBI authority terms no longer selected by current
record fields were queried afresh and retained byte-equivalent. Reproduce the
ontology build with the documented GO include IDs and the eight additional
`retained_include_ids` in that receipt. No authority label was copied from a
curated record. [Issue320](https://github.com/CultureBotAI/PathwayMech/issues/320)
tracks the RHEA-COMP representation gap; the new adapter excludes reactive-part
objects, and canonical policy keeps whole carrier states distinct from free FAD.

The [technical review](rhea-components-technical-review.md) independently checks
that adapter against pinned Rhea and current UniProt. Separate immutable
scientific reviews assess each complete pathway. Batch verification and the
SVG/KGX audit record the actual gate results and generated evidence preservation.
No browser surface was available, so there is no claim of a visual preview.
Expression-module71 is computational context, not catalytic or regulatory proof.

[The three-candidate handoff](triage-handoff.md) identifies cyanate as the next
bounded lead, a hypothetical step and wrong compound in tetrahydromonapterin,
and valid curcumin chemistry outside the current single-enzyme scope. It leaves
the earlier frozen528-row screening ledger unchanged. More candidates remain;
this is not source exhaustion. Data licensing for public release remains deferred
under the user's standing instruction.

The external implementation adds one bounded native naming case to the existing
MetaCyc Protein XML authority adapter. It changes only the source builder,
`tests/test_metacyc_complex_naming.py`, and `docs/IDENTIFIERS.md`. No participant
policy, schema, importer, maintained authority snapshot or pathway is changed.

Identity validation is now a separate helper that returns the validated direct
Protein and exact META frame. Both name paths share one safe decoder. Any direct
`common-name` slot retains precedence, and an empty, duplicate, malformed or
unresolved direct name fails. Only complete absence invokes the new relation.
There is no matching on exception messages.

The new relation requires native `Protein-Complexes` membership, exactly one
component with a distinct coherent META reference and integer coefficient at
least two, one resolved direct enzymatic-reaction, one empty enzyme reference
back to the exact complex, one coherent empty native reaction reference, and
one native string activity name. References cannot contain nested names or
nonempty text. Multiple components or activities, even duplicate activity names,
remain unsupported. The exact complex ID is retained; no activity aliases or
assembly suffixes are imported. Existing XML/HTML canonical conflict checks
remain unchanged.

This is the deliberately narrow single-activity homomer interpretation accepted
by root from SRI's native protein naming documentation. The copied proposal
contains the full rationale and issuing documentation, including SRI's loader
manual and `full-enzyme-name` description. The documentation change cites those
primary sources and explains unsupported cases. It does not assert assembly,
strain, taxon, reaction chemistry or experimental equivalence from a name.

The baseline is the actual working state of
`/private/tmp/pathwaymech-next-222-20261011`, whose HEAD was
`d8e3888528088e7bba468df57056f9f0e588b463`. HEAD alone does not describe these
inputs: the accepted five Salvage II files and its 629-entry manifest,
2265-term/476-source authority snapshot and 223 records were pending working
changes. `baseline-binding.json` records 1075 original/copy pairs and the actual
status. `accepted-working-baseline-five-files.json` verifies all five expected
accepted hashes. A later bridge to the actual merged 223 baseline is required;
this package does not claim that bridge or authorize adoption.

All 629 original cache bodies were copied into an isolated external cache after
hash verification. Their original bytes, metadata and full retained-ID selection
are used for the source snapshot replay. The source selection includes every
retained ID rather than dropping historical terms absent from current records;
it supplies no labels to the builder. The authentic four new originals have
their acquisition receipts bound separately and are tested as a four-term
external fixture, not adopted into a candidate canonical snapshot.

The first focused run passed 288 tests. Its initial lint run reported seven
line-length violations; that exact code and test state and both terminal
receipts are preserved under `initial-attempt/`. Only line wrapping was changed.
The final captured run and native CLI outputs are under `validation-run-1/`.
`result.json` and `retained-reproduction.json` must be read for their actual
completed statuses; a launch or intermediate log alone is not success evidence.

Focused tests exercise exact identity/back-reference failures, homomer bounds,
missing and duplicate required fields, safe name decoding, direct-name
precedence, cross-source conflict behavior and real CLI success/failure output
preservation. The original-source probes separately exercise all four authentic
originals and 22 preserved mutations. Existing protein, encoding and source
snapshot builder suites are included; no duplicate broad repository run was
started. The validation runner rehashes all copied and original bound inputs
after the full retained-ID source replay.

All work is external to the active worktree and shared cache. No Git metadata,
GitHub state or maintained input is written by this implementation. Independent
review and explicit parent-owned adoption remain separate steps.

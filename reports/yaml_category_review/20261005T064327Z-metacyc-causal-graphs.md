# YAML Category Review: MetaCyc causal graphs

- Repository: CultureBotAI/PathwayMech
- Category: All maintained MetaCyc pathway records
- Selection Rule: Recursively enumerate `data/pathways/**/*.yaml` and select records whose top-level `id` starts with `MetaCyc:`; all 50 members reviewed.
- Started UTC: 2026-10-05T06:40:53Z (final reporting and verification pass)
- Finished UTC: 20261005T064327Z
- Verdict: Full cohort reviewed and curated under explicit user authorization. No unresolved cohort blocker found; source limitations and final repository-wide checks remain explicit below.

## Target Category

The 50 MetaCyc records form a source cohort, not one biological pathway class.
The user authorized reviewing and editing all causal graphs, including supported
participants, enzymes, cofactors, locations, and evidence. That authorization
supersedes the review skill's default prohibition on record edits.

## Selection and Membership

Every member was compared with the complete native MetaCyc pathway definition,
including nested pathways, independent Rhea reaction sides, and relevant protein
annotations. The [per-record inventory](../causal_graph_review/README.metacyc.md#per-record-coverage)
and [detailed ledger](../causal_graph_review/metacyc-review.json) enumerate all 50;
this is not a sample. Filesystem recursion includes ignored files. A final
`rg --no-ignore --hidden` search across `data/pathways` and `conf` checked purine,
arginine, and glyoxylate identifiers and aliases outside this cohort.

## Validation

- All 152 maintained records, including all 50 MetaCyc members, pass native
  schema validation, endpoint semantics, and duplicate-record-ID checks.
- The focused graph-context, KGX, MetaCyc, and LinkML suites passed: 167 tests.
  These include cycle closure, exposed intermediates, spontaneous steps,
  mutant/cofactor exclusions, feedback direction, bacterial AIR carboxylation,
  and lossless qualified evidence export.
- The independently reviewed generic UniProt cofactor importer passes 11 tests;
  note-level evidence is preserved separately from cofactor-row evidence.
- The history validator passed 75 current history records with no invalid links
  at the cohort handoff, including 50 scaffolded MetaCyc history records.
- Ruff passed the cohort scripts/tests and shared schema/KGX edits. The final
  repository-wide `just validate`, `just test`, and `just lint`, including
  regenerated-product drift checks, are coordinated by the parent review after
  all source cohorts and authority snapshots settle. They are not claimed as
  completed by this cohort report.

## Lump and Split Review

Keep the alternative AIR/IMP biosynthesis routes separate: native reaction
chemistry and taxon-specific evidence distinguish them. The unusual
*Treponema denticola* class-II AIR-carboxylase route is independently supported
by PMID:21548610. Keep arginine biosynthesis I, the yeast acetyl-cycle route,
and their adjacent ornithine/citrulline modules within their intended scopes.
Shared reactions alone do not establish duplicate pathway identity. No record
merge or deletion is proposed by this cohort review.

## Identity and Grounding

Independent Rhea RDF and directed-reaction types were used rather than labels
or numeric heuristics. Twenty reaction occurrences now use source-supported
directional IDs. Existing chemically meaningful protonation conventions were
preserved; consecutive anomer-specific versus broader substrate classes remain
explicit ordering bridges. EC nodes denote molecular activities; named proteins
require independent reaction or reviewed component evidence and compatible taxon
scope. ChEBI and GO labels come from independent authorities, never corpus text.

## Graph and Evidence Patterns

Generated descriptions of structured facts now use `source_assertion` with an
exact source locator. Genuine literature quotations were checked against fetched
titles/abstracts and remain distinct; a missing abstract match was not treated as
proof of absence from full text. Source versions, URLs, and byte identities are
in the [source manifest](../causal_graph_review/metacyc-sources.json).

Specific dispositions preserve evidence limits: repaired-mutant IlvG P0DP90 is
excluded; disputed IlvD cluster nuclearity remains a general iron–sulfur-cluster
assertion; tentative crystal sodium for P00561/P00562 is excluded; and the outdated
ProB–ProA interaction requirement is not propagated. The ledger records these
choices. Protein-level feedback and location assertions remain separately sourced.

## Completeness Patterns

All native leaf reactions have a mapped step or a documented disposition. The
curation adds 13 net reaction occurrences, completes glyoxylate cycling and
carbamoyl-phosphate synthesis in the arginine route, and exposes supported
intermediates in isoleucine, leucine, methionine, tryptophan, and arginine
degradation. The cohort-specific pass records 190 protein, 150 cofactor, and
77 location annotation occurrences; later generic enrichment may increase counts.

The optional generic NAD(P)-dependent quinate/shikimate alternative in the nested
chorismate source is explicitly outside the selected E. coli NADPH/AroE route.
No unannotated protein is assumed cofactor-independent. Broad taxon records retain
activity classes when exact named-protein evidence is unavailable. DNA/RNA elements
and organelles are added only when independently grounded and mechanistically
supported; generic placeholders were not invented.

## Findings

Four major patterns were resolved: incomplete core reaction coverage; hidden
intermediates and erroneous enzyme attribution across composite steps; unsupported
protein/cofactor specificity; and structured-source prose presented as quotation.
The detailed ledger contains exact per-record dispositions rather than treating
these pattern counts as the number of changed edges.

Unresolved blockers: none identified in this cohort. Remaining source limitations
are bounded protein/cofactor coverage and specificity differences described above;
these are not claims that the biology is exhaustively known.

## Recommended Edits

The supported cohort edits and provenance/history entries are already applied.
Regenerate all affected pages and exports from maintained YAML as part of the
parent's final corpus pass. Preserve existing reviewed cofactor overrides when
applying generic enrichment. Do not reinstate P00561/P00562 metal edges or a
specific P05791 cluster nuclearity without stronger evidence.

## Follow-up Checks

Complete repository-wide closed-schema, independent identifier, history,
render/export drift, test, lint, and `git diff --check` gates after all parallel
curation work is incorporated. Inspect generated scientific labels and qualified
cofactor descriptions. Reproduction instructions and the exact migration baseline
are in the [cohort README](../causal_graph_review/README.metacyc.md#reproduction).

## Additional Notes

Structured MetaCyc, Rhea, UniProt, ChEBI, GO, and ENZYME sources were inspected;
48 PubMed records support the literature checks. Source snapshots are retained
outside the repository and described by the checked-in manifest.

Not checked: iModulonDB expression modules. This cohort pass evaluates reaction
identity and direct protein chemistry; no transcriptomic membership claim was
added. Expression-module absence would not establish negative biochemical evidence.

This report and the detailed ledgers live under an ignored report directory and
must be explicitly included in the final change. No GitHub mutation or paid
research call was performed by this cohort agent.

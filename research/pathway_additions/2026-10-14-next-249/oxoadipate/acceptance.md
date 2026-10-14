# 3-oxoadipate degradation and graph label repair

The change adds the complete `MetaCyc:PWY-2361` terminal degradation module:
two reactions, 13 participants, 22 evidence-backed edges and 18 references.
The corpus grows from 246 to 247 pathways. `identifiers.json` enumerates every
record, component, reaction and reference identifier. Ten independently sourced
authority terms and six source owners are added; all earlier record bytes,
authority objects and ordered manifest entries remain unchanged.

Exact charged chemistry is supported by the native META 27.0 objects, Rhea and
ChEBI. PRS2000 expression evidence is distinguished from direct catalytic
activation. Native assembly annotations, current UniProt disagreements,
uncertain PcaR initiation, the deposited PRS1/PRS2000 lineage context, partial
1981 access and abstract-only 1995 support remain explicit. No physiological
magnesium cofactor, direct inducer binding or modern-strain substitution is
inferred. Hidden and ignored files were included in the bounded duplicate
search; archive interiors and unfollowed symlink directories were not searched.
Raw scientific source bodies remain external, bound by URL and digest.

## Adversarial finding and repair

Independent integration review found a presentation defect, tracked as
[issue 521](https://github.com/CultureBotAI/PathwayMech/issues/521): distinct
predicate labels occupied identical SVG coordinates. The complete corpus audit
found duplicate positions on 235 pages. The shared renderer now reserves separate
label positions in each gutter and attaches substantially displaced labels to
their own arrows with unarrowed dotted leaders. Arrow paths, node geometry,
scientific data and evidence links are preserved.

Independent post-fix review checked all 247 SVGs and 12,329 graph edges. It found
no overlapping label boxes, label/node overlaps or clipped labels. It verified
4,519 moved labels, 3,674 correct leader attachments and unchanged page content
outside the diagrams. Ten canvases grow downward, by at most 5.04%. The added
regression tests cover coincident predicates and dense graph bounds. Root and
reviewer inspected the final styled static preview. Browser surfaces were
unavailable; no interactive preview is claimed.

The graph repair does not change KGX exports. Compared with the baseline corpus,
the added record supplies two more precise canonical aggregate display names:
acetyl-CoA(4-) and 3-oxoadipate(2-). All prior per-record node contexts and all
12,307 earlier edge rows are preserved.

## Verification

The initial validation cycle passed before the renderer repair was fully
integrated. Its full-test process had already loaded the previous renderer;
that cycle is not final verification of issue 521. The focused post-fix graph
suite passed 56 tests. The final cycle passes `just render-pages`, `just validate`,
`just test` (4,868 passed, three skipped), `just lint`, `just vendored-check` and
`git diff --check`. Commands, elapsed times, exit codes and log hashes are retained
in `validation/final/receipts.json`; `validation/index.json` binds lossless JSON
log wrappers to their original execution paths and exact decoded-byte hashes.
The independent scientific bundle is
`reviews/structured/20261014T103546Z-oxoadipate249-independent-scientific`:
pass with limitations, zero findings. Its validate/save/check commands pass;
the native corpus check reports 136 valid reviews with declared-scope coverage.

Scientific review covers the exact pathway YAML and evidence independently of
the author. Integration review covers canonical authority reproduction, prior
corpus preservation, KGX evidence fidelity, renderer changes and the complete
diagram audit. The saved reports preserve their different scopes and access
limitations. Exact committed-head review and GitHub checks follow publication;
this precommit acceptance note does not claim a merge or successful remote CI.

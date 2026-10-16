# Aerobic phenylacetate degradation: source preservation and primary detail

This increment adds `MetaCyc:PWY0-321`, phenylacetate degradation I (aerobic),
after the 264-record baseline at `2c27fc819bac17ef05e191830346d7a32248c97c`.
The maintained record is
[`phenylacetate-degradation-i-aerobic.yaml`](../../../data/pathways/phenylacetate-degradation-i-aerobic.yaml).
The generated page shows the source graph and eleven separate mechanism graphs.

The complete native pathway has nine reaction members, 22 material identities,
40 material occurrences and 68 source edges. These remain explicit. Primary
evidence supplies twelve additional top-level edges and eleven nested mechanism
objects, containing twelve local step claims. Two contextual reactions describe
cyclic dead-end formation and PaaY salvage; neither is asserted to be a native
member of PWY0-321. The record has 48 participants, seven taxa, eleven reaction
nodes and 50 source references.

## Inspecting the retained evidence

- [Accepted preparation](accepted-preparation/README.md) retains eight selected
  native, design, correction and independent implementation-review packets.
  Its [inventory](accepted-preparation/inventory.json) binds every archive and
  member, including original relative paths, lengths and SHA-256 values.
- [Integration preparation](integration-preparation/README.md) retains the
  immutable primary-fragment author packet, original authority implementation
  packet and 41 additional path-bound supporting artifacts. These include
  original source bodies and derived identity projections; they are not all
  primary publications. Its [inventory](integration-preparation/inventory.json)
  records the exact finite retention scope.
- [Authority originals](authority-source-originals/source-provenance.json)
  map 65 complete MetaCyc/EcoCyc XML bodies and their acquisition receipts to
  the maintained identifier manifest. The source snapshot adds 65 terms and
  owners while preserving all previous entries and ordering. Three taxon terms
  and CHEBI:63252 are added from the existing pinned read-only authority caches.
- [Reference retention](reference-original-retention.json) maps all 50 record
  reference hashes to retained archive members. This establishes availability
  of the original bytes, independently of the scientific review disposition.
- [Review preparation](review-preparation/README.md) preserves the original
  independent authority and primary-science reviews, the A01 correction and
  its independent acceptance, and the S01 contextual-locator correction.
- [Authority correction acceptance](authority-correction-acceptance/README.md)
  retains the A02 correction and independent acceptance, including the final
  formatting-only test successor. Original findings remain historical;
  acceptance applies to the exact corrected hashes recorded in those packets.
- [Implementation integration review](implementation-integration-review/README.md)
  verifies the peer-authored closed schema, graph transport and controls, and
  KGX context. All 264 prior records retain byte-identical KGX output. The
  review preserves exact source/detail relationships and evidence, and explicitly
  excludes the reviewer's own primary curation and authority corrections.
- [Rendering regression reviews](rendering-regression-reviews/README.md)
  retain the independently reproduced empty-rendering, optional-KGX and
  graph-test failures, including their exact original inputs and baseline
  comparisons. Corrected successor acceptance is a separate observation.
- [Rendering correction acceptance](rendering-correction-acceptance/README.md)
  binds the corrected rendering, export and test owners. Independent replay
  passed ten focused tests and 68 assertions; all 273 generated outputs,
  including 265 pathway pages, are byte-identical before and after the fixes.
- [Identifier increment](record-identifier-increment.json) lists the record's
  93 unique declared identifiers, including the 69 newly represented in the
  maintained pathway corpus. It distinguishes this record increment from the
  separately checked authority snapshot increment.
- [Final verification](final-verification/README.md) retains terminal root
  checks, original failed attempts, static visual QA and the complete frozen
  canonical-review working packet. Its inventory binds both archives and all
  193 members to their original bytes.
- The saved successor review is available as
  [YAML](../../../reviews/structured/20261015T235901Z-phenylacetate-primary-s01-successor/review.yaml)
  and [Markdown](../../../reviews/structured/20261015T235901Z-phenylacetate-primary-s01-successor/review.md).
  It records a completed pass with limitations within its declared scope and
  explicitly identifies mixed authorship and separately accepted independent
  evidence. The full suite passed 6,528 tests with three skipped; the canonical
  consistency check validated all 193 saved reviews. Counts describe the
  checks' scope, not scientific certainty.

The archives use standard `tar.gz`; extract a selected archive into a fresh
scratch directory to inspect its files. Original byte content and relative
paths are preserved, while filesystem metadata is not evidence identity.
The directory-local `.gitattributes` in `authority-source-originals/` preserves
the XML bytes and permits their original end-of-line spaces. It retains normal
text diffs and does not change whitespace checking for code or curated data.
The [source-byte preservation review](source-byte-preservation/README.md)
records the original staging diagnostics, exact source hashes and scoped checks.
Archived scripts are historical artifacts and need not be executed. Every
retained archive member was decoded and rehashed after packing. This directory
does not claim to contain every earlier discovery artifact or every possible
pathway source.

## Scientific boundaries

The source RXN0-6512 equation combines the C8 thiolysis and C6 isomerization
interpretation. Its source identity and equation remain intact; local PaaJ and
PaaG claims do not invent an issued identifier for isolated PaaJ chemistry.
The cis-3,4 intermediate is explicitly limited to the detailed interpretation.
Native oxepin and ChEBI:63252 differences remain visible as source conflicts,
without an unsupported identity equivalence. Reaction-equation reconciliation
does not establish physiological flux.

The record distinguishes purified preparations, fusion tags, mutants,
organisms, assay conditions and inferred or proposed mechanisms. It includes
the corrected PaaI mutant interpretation, the PaaX Table II/Table III distinction
and the negative direct IHF-binding result with an indirect physiological role.
The 688-residue PaaZ structural construct is tied to the retained 6JQL sequence,
not inferred from a general architecture statement. The Nature 2012 main/SI
NADPH versus NADP+ discrepancy is explicit.

Remaining source gaps include the complete PaaG 2019 main article, PaaFG 2012
supplement and PaaX 2014/2024 main articles. Four regulator endpoint originals
remain unverified for positive graph assertions. Their bounded literature
observations and the unmerged proposals are retained without adding unsupported
regulatory edges. The isolated PaaJ issuer-identity question remains unresolved.
These gaps do not imply that pathway discovery is exhausted.

## Review corrections

Issues [609](https://github.com/CultureBotAI/PathwayMech/issues/609),
[610](https://github.com/CultureBotAI/PathwayMech/issues/610) and
[611](https://github.com/CultureBotAI/PathwayMech/issues/611) track the primary
evidence corrections. Issues
[612](https://github.com/CultureBotAI/PathwayMech/issues/612),
[613](https://github.com/CultureBotAI/PathwayMech/issues/613) and
[614](https://github.com/CultureBotAI/PathwayMech/issues/614) track explicit
compartments, exact source-side quantities and detail-only participant scope.
The original authority review requires complete embedded identities
([615](https://github.com/CultureBotAI/PathwayMech/issues/615)) and recognition of
native bare-query request assertions
([616](https://github.com/CultureBotAI/PathwayMech/issues/616)). The independent
scientific review identified eight contextual reaction source locators to
correct ([617](https://github.com/CultureBotAI/PathwayMech/issues/617)).
The first full suite exposed optional-field compatibility defects in empty-page
rendering ([618](https://github.com/CultureBotAI/PathwayMech/issues/618)) and KGX
record-like inputs ([619](https://github.com/CultureBotAI/PathwayMech/issues/619)).
The graph integration test also needed to distinguish the source graph from
separate detail graphs
([620](https://github.com/CultureBotAI/PathwayMech/issues/620)). The correction
keeps the original minimal fixtures and checks every source graph, with added
corpus checks for the detailed graphs' directed edges and evidence targets.
Staging also exposed original end-of-line spaces in the retained native XML
([621](https://github.com/CultureBotAI/PathwayMech/issues/621)). The scoped
packaging rule preserves those exact source bytes and normal text diffs while
keeping whitespace and conflict checks active elsewhere.
Frozen predecessors remain available; corrections and independent acceptance
are separate successor records. Issue closure requires the verified merged
tree, not merely a passing author check.

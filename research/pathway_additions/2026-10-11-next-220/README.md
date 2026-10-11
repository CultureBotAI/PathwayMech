# Complete Calvin-Benson-Bassham cycle

This addition represents the complete native **MetaCyc:CALVIN-PWY** definition:
13 reactions, 51 participants, 118 mechanistic edges, 216 evidence blocks and
106 references. Both transketolase activities, both aldolase activities and both
bifunctional phosphatase transformations are retained. The graph distinguishes
native pathway assertions from current Synechocystis protein annotations and
condition-specific primary experiments.

The formal carbon-reduction/regeneration net uses three CO2, nine ATP and six
NADPH per net glyceraldehyde 3-phosphate. Formal atom/charge balance does not
establish culture flux or an energetic yield under every condition. Light
reactions, carbon uptake and concentration, photorespiration and downstream
sugar metabolism are outside this exact native definition.

## Evidence and scope

`identifiers.json` inventories the exact identifiers; `curation.md` explains
source and representation decisions. The compact source, chemistry, protein
and coverage projections retain assertion-specific locators and original-body
hashes. Full article bodies, broad paragraph extracts, original database dumps
and the full source projection remain in the external research cache.

Material limits are explicit in the record and review:

- The PCC 6803 parent taxon, Kazusa genome and GT experimental culture are
  distinct scopes. No exact culture identity is inferred from a shared strain
  name.
- The native TPI-to-mouse accession error is rejected. Current Q59994 is grounded
  in its own annotation; no native complex is transferred to it. Native TKT and
  current P73282 are not asserted to be identical constructs.
- Native ribose 5-phosphate and sedoheptulose 7-phosphate classes are broader
  than the displayed exact structures; no class-wide exact match is asserted.
- Historical protein preparations, short N-terminal peptides, engineered
  crystal constructs, assay metals and ligand-dependent assemblies retain
  their observed scope. Annotation evidence is not relabelled as experiment.
- CP12 GT complementation supports conditional pathway-level regulation. It
  does not establish purified inhibition, a fixed ternary complex, or Kazusa
  culture equivalence.
- Two primary articles were inspected through original full-text web renderings
  without a retained local full-text digest. Gap2 and RPE access is abstract
  limited. These limits are distinct from the replayable local source bodies.
- The inspected iModulonDB inventory has no selectable Synechocystis dataset.
  This limits applicability; it is not negative biological evidence.

## Review and correction

The full independent external review read every edge and evidence block and
checked the complete native reaction membership, directions, chemistry,
identities, assemblies, cofactors and source scope. Its initial observations
are preserved separately from the corrected successor and later maintained
review.

[Issue #413](https://github.com/CultureBotAI/PathwayMech/issues/413) identifies two
aldolase evidence locators that assign supporting paragraphs to printed p.328
instead of p.327. Their biological claims remain supported.
[Issue #414](https://github.com/CultureBotAI/PathwayMech/issues/414) identifies a
replay receipt defect: a formal input could change during the final slow
whole-database scan after its earlier final check. The successor fixes both findings. Independent full replay passes and the exact
late-manifest mutation now fails without a success receipt; selected actual
receipts are retained under `author-correction/` and `successor-review/`. An earlier reversed Rubisco sentence in the author curation prose
was corrected before the initial handoff; the graph hierarchy was already
correct.

The external source replay and its declared original inputs remain external.
Archived helpers are inert text, and the dossier does not claim that those
copies are independently portable. Reproduction requires the exact pinned
external inputs and runtime identified in the source manifest and execution
receipt. Deterministic replay is distinct from scientific review and maintained
repository gates.

## Integration status

The corrected target is integrated byte-for-byte after independent external
reassessment. Canonical authority builds added 10 original source inputs,
22 source terms and 12 ontology terms, preserving all prior entries and policy.
Scientific Rhea 142 inputs remain separate from production's pinned Rhea 139
SQL and existing update manifest. The baseline is actual merged denitrification
commit `32e97a948fc8e691692d5f105047a9f68b641a6f` with 220 pathways.

The maintained history and rendered pages are present. Rendering, full validation,
tests (1,256 passed, 3 skipped), lint, standalone KGX export and whitespace checks
passed, as did the 22-artifact vendored check. The CLI KGX files exactly match
the generated downloads. Static SVG verification preserves all 65 displayed
nodes, 118 edges and 216 evidence blocks; it is not browser visual testing.
See `validation/acceptance.json` and the separate `integration-review/` evidence.
Canonical maintained review bundles under `reviews/structured/` and the PR
record subsequent scientific-review and publication state.

`record-integration.json` identifies selected exact copies and external-only
inputs. Historical author prose retains its original preintegration status;
this README and successor assessments distinguish later acceptance. The source
manifest binds 105 original bodies; the historical correction summary's 104 is
a stale count, explicitly qualified by the independent successor.

Duplicate searches include ignored and hidden files and follow relevant
symlinks. Existing source menus, DRAM leads and shared carbohydrate reactions
do not constitute an existing complete Calvin record. This scoped result does
not establish source exhaustion.

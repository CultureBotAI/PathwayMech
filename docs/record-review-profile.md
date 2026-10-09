# PathwayMech Review Profile

Use the native `.claude/skills/review-yaml-record/SKILL.md` or
`.claude/skills/review-yaml-category/SKILL.md` scientific workflow. Both persist
through [record-reviews.md](record-reviews.md) and `schema/record_review.yaml`.
`conf/record_review.yaml` lists the CI-checked routes and local rubrics.
The `cross-mech-protein-links` route saves its final adjudicated assessment as
a repository-scoped review of exact local frozen audit inputs and local pathway
targets. Its TSVs remain leads. Sibling pins/locators belong in evidence and
dimensions, not external target paths; a sibling record needs its own native
review handoff before scientific status can change.

The scientific-review targets are maintained `data/pathways/*.yaml`. Read the entire pathway,
`docs/CURATION.md`, `docs/HARMONIZATION.md`, `docs/CAUSAL_GRAPHS.md`, and the
`add-pathway` skill. Review exact pathway identity, taxa, participants, reactions,
cofactors, compartments, direction, edge-local endpoints/predicates and evidence.
Preserve structured database assertions with their exact source locators rather
than relabelling them as quotations from a cited paper. Transcriptomic module
membership is context, not direct catalysis or pathway membership evidence.

Use assessment dimensions for evidence tier, taxon/condition, source object and
component role; preserve edge/field paths on findings and claim-specific sources.
Category reviews retain selection, full/sample denominator, and evidence-backed
lump/split/retain/defer decisions. Similar pathway names are not equivalence.

Run the documented read-only gates: `just validate`, `just test`, `just lint`,
and `git diff --check`. Report their actual scope; do not invent a one-record
validator when the route is corpus-wide. `just validate` includes the closed
schema and identifier/label gates. Curation-history and record-promotion APIs
must not be inferred from review support.

Future fixes belong to the target YAML, `conf/sources.yaml`,
`templates/pathway_mechanism_research.md`, or the source extractor as applicable.
`pages/` is generated and must not be hand-patched. Research drafts and migration
decision ledgers are not completed scientific record reviews; review them against
actual targets and save the common bundle before claiming a completed review.

`just review-check` validates the saved YAML/Markdown pairs and append-only
history under `reviews/structured/`. PR/merge-group CI uses the trusted event
base in `RECORD_REVIEW_BASE`. Existing `reports/yaml_record_review/` and
`reports/yaml_category_review/` prose stays historical and is not migrated.
No scientific record, native curation status or history event changes on save.

The `.claude/skills/pathwaymech-resolve-reviews/SKILL.md` route interprets saved
reviews and applies supported corrections. A bounded reconciliation may use
legacy reports as `source` targets with current maintained YAML and audit ledgers
as inspected context inputs; declare `scientific_review: false` and explicitly
exclude fresh literature review. Include any record requiring a correction as
an assessed maintained target. Legacy prose is not converted into fabricated
structured predecessors: already-applied changes belong in evidence-linked
assessments, while structured dispositions retain exact finding lineage.

# Reviewing pathway graphs

Review the entire named pathway and its biological scope against independently
retrieved source statements. A valid graph is not necessarily a complete or
correct mechanism. Source maps can contain neighboring pathways, hypothetical
steps, incorrect cross-references, and annotations superseded by experiments.

Use the local record and cohort review skills for the review rubric. Explicit
curation requests authorize applying the verified findings. Record a disposition
for every source fact and every maintained record when reviewing the corpus;
sampling cannot establish a full-corpus result.

## Components and relations

Participants may include proteins, complexes, cofactors, metabolites, lipids,
DNA, RNA, and cellular components. Add each when it participates in the supported
mechanism. Do not add a generic DNA or RNA node simply because a pathway's
enzymes have genes. Native instance identifiers preserve physical distinctions
such as redox states when the source only supplies a broad shared chemical class.

An optional `category` records the source-supported biological kind or cofactor
role. A chemical may be both a reaction participant and an enzyme cofactor;
the incident edges distinguish those roles. Cellular components and biological
processes are context nodes, not metabolites to consume.

Use `category: pathway` for an identified child pathway or downstream pathway
interface in the `reactions` collection. Its native identifier and evidence must
establish the pathway scope. This explicit type renders and exports as a pathway;
the identifier prefix alone does not distinguish it from an individual reaction.
Pathway nodes cannot serve as consumed metabolites or physical-location subjects.

Use `chemical_entity` when the source establishes a chemical entity or generic
chemical class without restricting it to a narrower molecular kind. For example,
the generic methyl acceptors in the SAM cycle can include small molecules and
macromolecules. This category exports as `biolink:ChemicalEntity` and renders as
a chemical node. It does not establish a specific structure, molecular size or
cofactor role; retain the source-native identity and edge evidence.

Use `polymer` for a supported chemical polymer class. It exports as
`biolink:ChemicalEntity` and renders as a chemical node, avoiding the default
small-molecule classification for an uncategorized ChEBI participant. This
category does not distinguish individual chain lengths; preserve those source
states explicitly in the incident edge evidence and descriptions.

- `has_input` and `has_output` preserve an activity model's assertions without
  claiming chemical destruction or synthesis. Both point from activity to
  participant. `consumes` points from participant to reaction or pathway;
  `produces` points from reaction or pathway to participant.
  A `has_input` or `has_output` subject may also be an explicitly typed
  `molecular_activity` in `participants`. This admission requires a participant-only
  identity and that every declaration of that participant has the activity type;
  conflicting declarations cannot turn a physical entity or taxon into an activity.
  Preserve conditional or alternative input/output scope on the affected edge.
  These assertions do not add terms to the issued reaction's canonical equation
  or extend the endpoint rules for other predicates.
- `enables` preserves a source's gene-product/activity assertion. `catalyzes`
  requires support for catalysis. Membership in a protein complex does not mean
  every subunit independently catalyzes its overall reaction.
- `has_cofactor` connects an enzyme or complex to a supported cofactor.
  Keep notes about alternative metals, binding, conditions, and evidence codes.
  A curated similarity annotation must not be described as direct experimental
  evidence; lack of an annotation does not demonstrate cofactor independence.
- `occurs_in` connects an activity or process to its cellular component.
  `located_in` describes a physical entity. An activity's location does not
  establish exclusive localization of every instance of its protein class.
- `part_of` and `has_part` preserve process membership or complex composition.
  These context relations are not themselves claims of causal regulation.
- `causally_upstream_of` leaves the influence and its sign unspecified;
  `provides_input_for` preserves direct material transfer between activities.
  Neither is interchangeable with `regulates` or temporal `precedes`.

Reaction `direction` records source orientation (`left_to_right`,
`right_to_left`, or `reversible`). Distinguish a pathway's selected physiological
flux from thermodynamic reversibility, and describe source disagreements.

## Experimental constructs and molecular states

Prefer an exact issuing identifier for a modified protein or assembly when one
exists. If evidence tests a construct that differs from the named native protein,
qualify the affected edge endpoint. Do not mint a biological CURIE for the assay
material or let an unqualified base-protein edge imply that the native molecule
was tested. A qualifier describes the source-limited change; it does not assert
sequence identity elsewhere or an assembly's modification occupancy.

An optional `endpoint_qualifiers` list contains at most two objects, one per
`subject` or `object`. Each requires `endpoint`, `kind` (`experimental_construct`
or `molecular_state`), a nonempty `description` of at most 400 characters, and a
nonempty `evidence` list using the same Evidence grammar and locally declared
references as the edge. Only endpoints explicitly declared as protein or complex
participants may be qualified. Unknown kinds or fields, repeated endpoint roles,
and taxon, reaction, pathway or untyped participant endpoints are rejected.

The endpoint plus its qualification forms the complete edge claim. For example,
an activation assay on Ser1-NagB must retain the NagB construct qualification
beside its object ID; moving it to a regulator subject changes the assertion.
Keep phosphorylation, ligand dependence, preparation and assay conditions where
the inspected source establishes them. Absence of measured activation does not
establish inhibition. Generic validation checks shape, endpoint kind and local
evidence references; scientific review and source-specific replay must detect a
missing qualification, a plausible but wrong role, or changed construct wording.

## Evidence and provenance

Each evidence item cites a declared reference and contains exactly one of:

- `quote`: a short, verbatim source excerpt, at most 400 characters;
- `source_assertion`: a faithful description of an inspected structured source
  statement, at most 400 characters, with a mandatory `source_locator` locating
  the native triple, object, JSON path, or XML element.

A generated sentence is not a quotation. A database's citation of a PMID does
not mean its comment occurs in that paper. Cite the inspected database for its
structured statements, preserve its evidence limitations, and inspect a paper
before attributing a specific claim to its text. References may carry `url`,
`source_version`, and `source_sha256`; a digest must identify the actual artifact
and be explained in the accompanying source manifest when the artifact is a
batch export. Keep complete raw downloads outside the repository and retain
the reproducible source projection, manifest, and review ledger.

## Record-page diagrams

### Detailed mechanisms under an issued reaction

An optional `reaction_mechanisms` list describes evidence-backed substeps under
an existing reaction with `category: molecular_activity`. Each mechanism has
`version: 1`, a record-local `key`, `source_reaction_id`, `relation_to_source`,
description, evidence, a source equation, steps and edges. Local step keys are
curatorial claim coordinates, not biological identifiers. All public endpoints
must be uniquely declared, authority-checked participants. Do not relabel a net
reaction accession as an isolated enzymatic step.

A step has a key, label, description, evidence and `assertion_status` of
`supported`, `inferred` or `proposed`. Nested edges have their own status and
evidence. Their typed endpoints contain exactly one `node_id` or `step_key`.
Material edges use `consumes` (chemical to step) or `produces` (step to chemical)
with a positive integer coefficient. `catalyzes`/`enables` connect a declared
protein or complex to a step; `provides_input_for`/`precedes` connect distinct
steps; `occurs_in` connects a step to a cellular component. A local key cannot
escape into a top-level biological edge or an identifier mapping. Construct
qualifiers retain the existing protein/complex-only, endpoint-specific rules.

The source equation contains `inputs` and `outputs`, each with exact
`participant_id` and `coefficient`, and an `orientation` of `as_reported` or
`reversed`. Store the original equation; orientation selects its inverse for
comparison without rewriting the reaction's source direction. This first
profile accepts net equations without the same material on both sides and
exact positive integer coefficients. Each step must have inputs and outputs.
Cancellation uses identical participant IDs only. A `decomposition` must sum
exactly to the selected source equation. Formula or charge balance alone never
establishes chemical identity or the truth of the source equation.

Every step must either be unlocated, meaning location unspecified, or have one
explicit `occurs_in` in the same component as every other step. Mixed,
ambiguous or different step locations are rejected; transport is not inferred.
Source-specific scientific review must still reject unrepresented transport
and verify every source term, coefficient, material identity and assay scope.

An `alternative_interpretation` preserves a distinct mechanistic equation and
requires `source_conflicts`. Each conflict identifies a whole unmatched
`source_participant_id` and `interpreted_participant_id`, the same `side`
(`inputs` or `outputs`), their equal positive integer `coefficient`, `kind`
(`stereo`, `constitution` or `microstate`), `status` (`unresolved`,
`proposed_revision` or `supported_revision`), rationale and evidence. Compare
input and output boundaries separately. Every difference must be covered
exactly once. Shared-ID coefficient changes, additions, deletions, partial
coverage and invented counterparts are rejected. This is a statement of
disagreement, not chemical equivalence or an exact mapping. A supported
revision still needs independent primary/issuer evidence, not just a valid enum.

Unobserved states without verified identities belong in optional step
`hypotheses`: description, `status: proposed` and evidence. These are visibly
proposed prose callouts, not invented chemical nodes or material-flow edges.

`detail_only_participant_ids` explicitly identifies declared participants used
only in mechanistic detail. These must be used by nested endpoints and must not
occur in top-level edges, source equations or source-side conflict terms. Only
these explicit IDs are excluded from the first graph. Other isolated source
components remain visible. Source coverage review must prove that no native
source component was incorrectly marked detail-only. Component tables and KGX
retain every declaration and show this scope; no implicit filtering by label,
isolation or nested usage is permitted.

The first graph and its source assertions remain available beside the detailed
graphs. Each detail states its parent reaction, relation, statuses, equations,
conflicts, hypotheses and complete evidence without JavaScript. Display keys
only control navigation. Layout never asserts reaction order or channeling.

The static record pages render every maintained mechanistic edge as a directed
SVG link to its corresponding evidence-table row. Labels and arrowheads retain
the declared subject, predicate and object; reaction `direction` remains node
metadata. In particular, `has_input` still points from activity to participant.
The layout is a browsing aid, not an inferred sequence or a metabolic flux model.
Context and cofactor relationships use dashed lines; their exact predicates
remain visible. Declared isolated participants and reactions are retained without
inventing connections, and shared labels never merge different identifiers.

SVG diagrams are generated at build time and remain available without JavaScript.
Local progressive controls add zoom, fit-to-width and node-neighborhood
highlighting. Highlighting keeps every relationship in the diagram. The complete
component, edge and evidence tables remain available below it; records with no
mechanistic edges display an explicit empty state.

Qualified endpoints have distinct graph display instances bearing a visible
construct/state label. Their complete description and evidence appear in
accessible graph details and in the adjacent subject/object table cell, without
JavaScript. Display-instance keys serve navigation only; the table and exports
retain the native biological ID. A qualifier applies to its specific edge, so
another edge using the base protein does not inherit it.

The renderer owns `pages/assets/pathway-network.css` and
`pages/assets/pathway-network.js` as well as each record page. Edit their sources
under `src/pathwaymech/assets/` and the graph renderer in
`src/pathwaymech/graph_view.py`, then regenerate through `just render-pages`.
The page consistency gate checks these assets too.

## Verification

For each changed record, retain append-only curation history and verify the
new identifiers against independent authorities. Review source-to-graph and
graph-to-source coverage, endpoint direction, biological identity, cofactors,
compartments, evidence placement, and legitimate exclusions. New namespace or
source-instance support must not waive identifier existence.

After the final records and authority snapshots are ready, run `just render-pages`,
`just validate`, `just test`, `just lint`, and `git diff --check`. Check the KGX
export as well as generated pages: molecular activities, cellular components,
and biological processes must retain their distinct categories, and structured
assertions must not render as block quotations.

KGX edges preserve the complete evidence array and cited reference metadata as
JSON, alongside the edge description. This retains alternative-cofactor notes,
evidence codes, source locations, versions, and artifact hashes. KGX nodes retain
their declared source categories and per-record `source_contexts` JSON, including
local labels and reaction directions. A global direction is left blank when
different records assign different directions to a shared identifier; the
per-record contexts retain both assertions. Explicit biological kinds override
prefix-based category guesses regardless of record order.

KGX adds an `endpoint_qualifiers` JSON column preserving every role, kind,
description and Evidence object. Its reference metadata includes qualifier-only
citations. Complete qualifier payloads participate in edge identity and
deduplication, so a qualified claim cannot collapse into an unqualified edge.
Consumers that cannot preserve this column must explicitly reject or omit the
qualified claim. Empty or absent qualifiers retain previous edge IDs and field
values; the added TSV column and header still change export bytes and checksums.

KGX stores each complete versioned detail under the parent reaction's
record-specific `source_contexts[].reaction_mechanisms`. Each entry has the
unchanged `mechanism` object and `references` containing complete metadata for
every cited source, including qualifier-, hypothesis- and conflict-only
citations. Participant context marks `graph_scope: mechanism_detail_only` when
declared. Local steps do not become biological KGX nodes, and their material or
catalyst edges are never flattened onto the issued parent reaction. Consumers
must parse this context to obtain the detailed graph; ordinary KGX endpoint
rows alone do not contain it. Consumers unable to preserve the extension must
explicitly reject or omit detailed claims. Existing records without mechanisms
retain their KGX row values and edge identities.

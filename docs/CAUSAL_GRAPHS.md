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

- `has_input` and `has_output` preserve an activity model's assertions without
  claiming chemical destruction or synthesis. Both point from activity to
  participant. `consumes` points from participant to reaction or pathway;
  `produces` points from reaction or pathway to participant.
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

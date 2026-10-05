# Identifier and label verification

`just check-identifiers` resolves every named record, taxon, participant, and
reaction in the recursive `data/pathways/` corpus against independently sourced
authority snapshots. `just validate` runs the same enforcing command through
`pathwaymech-run-qc`. The existing PR and merge-group workflows run that QC
entry point, so this is a blocking check rather than an advisory report.

## What is asserted

`conf/identifier_policy.yaml` declares supported namespaces and label policy.
An identifier must be present in its configured authority snapshot under every
policy. A syntactically valid CURIE, a citation in a pathway record, or a label
copied from that record is not proof of identifier existence.

- `canonical` compares a label with the authority's preferred label.
- `canonical_or_synonym` additionally accepts synonyms supplied by that
  authority snapshot. Ontology extraction uses exact synonyms only.
- `contextual_labels` lists explicit namespace, record-prefix, and section
  combinations where the label is display text from a pathway or diagram.
  Each rule has a reason. These rules preserve display text while still
  requiring the identifier to resolve. They do not create identifier exceptions.

Comparison normalizes Unicode compatibility forms, whitespace, and letter case.
It does not remove words, charges, stereochemistry, or punctuation. There is no
fuzzy matching and no rule that accepts a missing identifier because its label
looks plausible.

The current policy distinguishes diagram abbreviations, organism-qualified
gene symbols, and functional reaction-step names from canonical assertions.
Rules apply only to their declared surfaces. For example, a contextual reaction
label does not make a taxon label contextual, and a WikiPathways display rule
does not cover a newly introduced GO record. Read the policy file for the exact
scope; adding a broader rule requires a semantic justification, not merely a
list of current failures.

Schema-supported prefixes without a configured authority remain unsupported by
this gate and fail explicitly. Adding an importer or new prefix therefore
requires authority evidence as well as schema support. Local activity or
interaction IDs are checked against the independently obtained source graph
that defines them, rather than treated as externally resolvable ontology terms.

## Authority snapshots

`data/identifier_authorities/` holds small JSON projections of independent
ontology or primary-source artifacts. These are offline resolver data, not an
allowlist produced from pathway labels. The corpus may select which IDs to
extract, but only the external authority supplies existence, labels, and
synonyms. Missing IDs stop extraction and need investigation.

Each snapshot contains:

- `version`: the snapshot format version;
- `sources`: original source URLs, source versions, licenses, and SHA-256
  digests of the input bytes;
- `terms`: a mapping from exact CURIE to authority label, synonyms, and a
  source key from `sources`.

A term with `label_kind: source_context` is an identifier assertion in an
independent source's cross-reference or local graph, not a canonical name
assertion by the target namespace. Such a term can only satisfy an explicitly
contextual slot. It cannot satisfy canonical-label verification even if the
strings happen to match. This records the evidence boundary for native IDs
whose independently available source supplies membership but no canonical name.

The optional `sha256_scope` says precisely which artifact was hashed when its
bytes differ from the representation at the public source URL. For example,
an OAK Semantic SQL database digest covers the uncompressed SQLite database,
while its source URL identifies the ontology release. Without this field the
digest denotes the unmodified bytes returned by the source URL. These are
provenance digests of the inputs, not checksums of the derived JSON file.

The gate does not download or silently refresh authority data. A term absent
from the selected snapshot fails with `ID_NOT_FOUND`; this means it is
unverified against that snapshot, not necessarily absent from today's upstream
database. Resolve it against the primary source, refresh the relevant snapshot,
and review that evidence before adding it. Similarly, a source's current state
may have changed since a pinned version; the gate asserts verification against
the recorded version, not continual live verification.

The extraction scripts are `scripts/build_ontology_identifier_snapshot.py` and
`scripts/build_source_identifier_snapshot.py`. Their `--help` describes the
explicit input artifacts and output paths. Keep downloaded full authorities
outside the repository; commit the small extracted snapshots and provenance.
Do not use importer test fixtures or the curated YAML as production authorities.

For a source snapshot refresh, obtain the exact artifacts described by
`conf/identifier_sources.json` from its source URLs or a preserved cache. Put
each artifact at its manifest `path` beneath an external cache directory:

```bash
uv run python scripts/build_source_identifier_snapshot.py \
  --manifest conf/identifier_sources.json \
  --cache-dir /path/to/identifier-sources \
  --records data/pathways \
  --output data/identifier_authorities/sources.json
```

Every input must match its manifest SHA-256. Read `sha256_scope` when the
artifact is a cached export rather than the source URL's current response.
Upstream changes require an explicit source/version/hash review and manifest
update. A missing artifact, hash mismatch, or unresolved named identifier in
a supported source namespace stops the refresh before replacing the existing
snapshot; partial results are not published.

For ontology snapshots, supply the independently downloaded, uncompressed OAK
Semantic SQL databases. The explicit GO IDs retain coverage for that configured
namespace even when the current corpus has no GO named nodes:

```bash
uv run python scripts/build_ontology_identifier_snapshot.py \
  --source GO=/path/to/go.db --source CHEBI=/path/to/chebi.db \
  --source NCBITaxon=/path/to/ncbitaxon.db --source RHEA=/path/to/rhea.db \
  --corpus data/pathways \
  --include-id GO:0008150 --include-id GO:0006096 --include-id GO:0005975 \
  --output data/identifier_authorities/ontology.json
```

Review the resulting provenance and label differences, then run
`just check-identifiers` and `just validate` before committing either refresh.

## Failures and acceptance tests

The command returns nonzero for unknown namespaces, IDs absent from authority
data, wrong canonical labels, an empty corpus, malformed named surfaces,
missing or empty snapshots, and incomplete provenance or policy. A configured
namespace with zero authority terms also fails even if other namespaces work.
There is no report mode, warning downgrade, implicit adapter fallback, or
identifier-existence exception.

`tests/test_identifiers.py` exercises the same checker and CLI used by QC with
independently authored offline fixtures. It covers all four named surfaces,
nested records, contextual scope, synonyms, missing IDs, label mismatch,
unknown namespaces, empty selection, and unavailable authority data. The QC
integration test checks that a wrong label makes the QC entry point fail.

The native checker is deliberately separate from the shared vendored
`scripts/validate_id_label_correspondence.py`. That utility supports advisory
and optional-target workflows which do not provide this gate's strict coverage
contract. Its governed files remain byte-identical to the pinned claw revision.

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

For `metacyc-html`, original bytes are hashed without rewriting or transcoding.
The parser uses UTF-8 with lossless `surrogateescape` to tolerate invalid bytes
only outside the native identity and title fields. Every native object metadata
and title field must itself be valid UTF-8 before any term is emitted, including
title markup that will later be removed. There is no Latin-1/Windows-code-page
guess, replacement-character repair, or ignored-byte decoding. This source kind
emits the native canonical title and no synonyms; unrelated page prose is not an
authority label. Other source kinds retain their existing decoders.

The `metacyc-protein-xml` source kind accepts a single native Pathway Tools
`getxml` response containing one direct, full META `Protein` instance. The
manifest request, XML base, metadata query and top-level ID/frame/orgid must
agree. The META PGDB version in the XML must equal the manifest's `version`
exactly (for example, `27.0`); the separate `ptools-version` software attribute
does not establish the database release. Original bytes are hashed unchanged
and parsed according to their declared XML encoding. DTDs and custom entities,
HTML/login responses, duplicate top-level objects and unresolved names fail.

Only the direct `common-name` supplies the canonical label. Native inline
presentation markup and character entities are decoded, with no curated-label
fallback or imported synonyms. Malformed or still-escaped numeric references
and decoded characters outside the supported XML character ranges are rejected;
references are not recursively unescaped to guess a label. Nested enzyme,
component, organism and curator names are not emitted as authority terms.
Nested unresolved protein references
do not imply unresolved identity of the full top-level object. This extraction
establishes identifier/name provenance, not species/strain equivalence,
assembly, sequence, reaction or experimental function. Conflicting canonical
names involving an XML source fail before corpus selection, including conflicts
with a MetaCyc HTML source; existing HTML-only selection behavior is unchanged.

A term with `label_kind: source_context` is an identifier assertion in an
independent source's cross-reference or local graph, not a canonical name
assertion by the target namespace. Such a term can only satisfy an explicitly
contextual slot. It cannot satisfy canonical-label verification even if the
strings happen to match. This records the evidence boundary for native IDs
whose independently available source supplies membership but no canonical name.

The ontology builder also accepts `--rhea-updates conf/rhea_identifier_updates.json
--cache-dir <original-source-cache>`. This explicit manifest selects equations
whose current Rhea release corrects the older Semantic SQL source. It contains
identifiers and source provenance only. The builder hashes the complete original
gzip RDF and requires matching native URI, accession, numeric ID, approved reaction
class/status, and agreeing equation and label. Missing, duplicate or inconsistent
objects fail before the snapshot is written. Updated terms cite that RDF source;
obsolete equations are not retained as synonyms. Other terms continue to use
their pinned sources. The current selection adds two preQ₀ reactions absent from
the prior corpus; the cohort audit verifies that all earlier terms are unchanged.

The `pathbank-biopax` source kind reads a native PathBank BioPAX Level 3
primary pathway per artifact. Its linked SMPDB unification accession establishes the
`PathBank:SMP...` identity; an identifiers.org SMPDB pathway URI must agree.
A PathWhiz `PW...` filename never establishes an SMPDB accession. The native
pathway title remains a canonical label assertion. Declared local reactions, transport events and
physical entities use `PathBank:SMP.../<native-local-id>` and are marked
`source_context`, including objects without a biological label. Their existence
does not itself establish pathway membership or catalytic function.

An exact official per-pathway download URL
(`https://pathbank.org/view/SMP.../download?type=owl_markup`) can select the
primary definition from an export that also contains attached `SubPathway`
interface stubs. The request must agree with the native SMPDB assertion; neither
the first XML object nor the filename selects the pathway. Extra Pathway objects
must be explicitly attached stubs containing native Interaction objects, not
unrelated or expanded definitions. Only the selected primary pathway supplies a
canonical pathway term. An interface's independently downloaded definition can
provide its own canonical title. Legacy archive inputs still require exactly
one Pathway. Native Interaction objects are not emitted as reaction authorities.
Compartment-scoped physical objects keep distinct local IDs even when they share
a chemical reference; identity alone does not assert material transfer or exact
chemical equivalence between those objects.

PathBank's external chemical and protein cross-reference labels are not emitted
as ChEBI or UniProt authority terms: those identifiers still require their own
independent authority inputs. Scoped PathBank participant rules permit native
BioPAX display names, and reaction rules permit curated Rhea step descriptions.
The rules do not relax pathway titles, taxon labels or missing identifiers.
MetaCyc records can also use verified PathBank physical participants when the
native object preserves an assembly or molecular state. This participant-only
contextual rule does not establish pathway membership, catalytic function, or
sequence equivalence; those claims need independent edge evidence. It does not
extend to PathBank reaction labels or pathway titles in a MetaCyc record.
Archive members must be extracted without rewriting bytes, with the exact member
path and archive digest recorded in `sha256_scope` when the public URL is a ZIP.

`ncbi-entrezgene-xml` supplies `Entrez` gene symbols from a single original NCBI
EFetch XML response. Its official HTTPS URL must request one positive numeric
ID with `db=gene` and `rettype=xml`; the direct Gene-track ID must agree. A single
direct Gene-ref supplies the canonical locus symbol, explicit native synonyms
and locus tag. Nested homologs, protein products and external database links do
not become gene aliases or independent authorities. A formal nomenclature symbol,
when present, must agree with the locus. Entrez labels use canonical-or-synonym
comparison without a contextual exemption.

Gene sources must have one unambiguous native taxon and organism name. Repeated
sources for an ID must agree on the locus, aliases and taxon before corpus
selection. Native status omission is permitted as omission, not an observed
explicit live-status assertion. Explicit secondary/discontinued status,
contradictory status, current-ID redirects and discontinue dates are unsupported
and fail. The standard external NCBI Entrezgene DOCTYPE is accepted without
loading a DTD or resolving external entities; internal subsets and entity
declarations fail in every supported XML encoding. Original bytes and their
acquisition/update-date provenance are retained. No status or strain equivalence
is added to the source. Missing Entrez authority terms fail the snapshot builder
and identifier gate.

`RHEA-COMP` identifies whole generic protein participants, including distinct
oxidized and reduced carrier states. This is the namespace used by UniProt's
catalytic-activity cross-references for Rhea `Compound_<id>` objects. The
`rhea-components-rdf-gz` source kind extracts only explicit `GenericPolypeptide`
objects from native Rhea RDF, requiring matching numeric IDs and `GENERIC:<id>`
accessions. It preserves the Rhea name under canonical-label policy. Reactive
parts such as bound FAD and FADH2 are separate objects and cannot substitute for
the whole carrier. These generic protein states do not identify a particular
organism's protein sequence. Declare their participant category explicitly;
the namespace alone does not establish an organism-specific protein identity.

The optional `sha256_scope` says precisely which artifact was hashed when its
bytes differ from the representation at the public source URL. For example,
an OAK Semantic SQL database digest covers the uncompressed SQLite database,
while its source URL identifies the ontology release. Without this field the
digest denotes the unmodified bytes returned by the source URL. These are
provenance digests of the inputs, not checksums of the derived JSON file.

KEGG authority extraction accepts three explicit native REST flatfile kinds:
`kegg-module-flatfile` for `M` plus five digits with ENTRY type `Pathway Module`,
`kegg-reaction-flatfile` for `R` plus five digits with type `Reaction`, and
`kegg-compound-flatfile` for `C` plus five digits with type `Compound`. The
manifest URL must be an official `https://rest.kegg.jp/get/` request for one to
ten unique identifiers of that same class. Every requested ENTRY must occur
exactly once in the complete, terminated response; extra, missing, duplicate,
mixed-class or malformed entries fail before snapshot publication.

Only native ENTRY/NAME fields establish KEGG identity and names. The first
semicolon-delimited NAME is canonical and subsequent native names are retained
as synonyms; the KEGG gate requires the canonical label. Conflicting names
across source inputs fail even for IDs outside the selected corpus. Matching
duplicate assertions retain the first source's provenance. Module reaction and
compound lists, KGML display names, filenames and curated labels are not
authorities for separately issued entries. Other KEGG entry classes remain
unsupported. These rules follow the native
[API](https://www.kegg.jp/kegg/rest/keggapi.html) and
[entry format](https://www.kegg.jp/kegg/docs/dbentry.html).

Hash the complete original HTTP body, including all entries of a batch. Record
the actual retrieval snapshot when an entry has no native release designation;
do not invent release or license metadata. Add the policy and independently
built KEGG snapshot together: an empty namespace or missing identifier remains
blocking. Identity support does not establish organism, pathway membership,
reaction direction or chemical equivalence. In particular, generic carrier
entries need explicit participant categories and evidence; a KEGG Compound
entry does not necessarily describe a small molecule. KEGG `Rxxxxx` reaction
nodes export as BiochemicalReaction unless an explicit category overrides it.

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
  --rhea-updates conf/rhea_identifier_updates.json --cache-dir /path/to/source-cache \
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

## Native MetaNetX chemical authority

The `metanetx.chemical` namespace preserves MetaNetX's own issued spelling.
`metanetx-chemical-html` accepts only a production
`https://www.metanetx.org/chem_info/MNXM<digits>` original, bound to the manifest
SHA-256. It requires one native `MolecularEntity` JSON-LD object whose identifier,
`@id`, URL and name agree with the request and visible MNX_ID/H1. Missing,
duplicate, unresolved or conflicting identities/names fail before output is
written. Beta endpoints, account/error pages and other MNX entry classes do not
establish this authority.

Only the native canonical name is admitted. `alternateName`, `sameAs` and
upstream reference labels do not become accepted synonyms, mappings or other
namespaces' authority terms. No contextual-label exception is granted; an
unselected or unknown MNXM entry remains unresolved. The schema admits the
namespace, while the source parser and identifier gate establish exact identity.
Integrate this policy with an independently built native snapshot and its source
manifest; a configured namespace with no authority terms remains an error, even
when no current record uses it. The empty-namespace guard is not relaxed.

A production entry can describe a generic chemical class or carrier state, not
necessarily a small molecule. Its default KGX category is `biolink:ChemicalEntity`;
more specific participant categories require separate source evidence. The
canonical name does not establish reaction membership, protein sequence, charge
normalization or equivalence to a historical MetaCyc/ModelSEED entry. Inspect
original structures separately, retaining conflicts rather than relabeling them.

For production-page acquisition, record the entry bytes, URL and retrieval time,
and retain the original [MNXref release documentation](https://www.metanetx.org/mnxdoc/mnxref.html)
with its own digest when assigning the observed release. This records a production
observation; it does not claim acquisition of a versioned bulk dump. Upstream
licenses still apply as described by the issuing source.

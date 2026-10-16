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

A contextual rule may additionally set `authority_entity_types: [reaction]`.
This selector matches the verified authority term, not the record's category;
`reaction` is its only supported value. The native-reaction placement check
still requires `reactions` with `category: molecular_activity`. GO records can
therefore describe an independently verified native reaction without extending
the waiver to a pathway interface in the same collection, even if that
interface is incorrectly recategorized. Rules without this optional selector
keep their previous scope. Empty, malformed, or unsupported selectors fail.

Schema-supported prefixes without a configured authority remain unsupported by
this gate and fail explicitly. Adding an importer or new prefix therefore
requires authority evidence as well as schema support. Local activity or
interaction IDs are checked against the independently obtained source graph
that defines them, rather than treated as externally resolvable ontology terms.

## Authority snapshots

Nested `reaction_mechanisms` do not introduce an identifier namespace. Their
`key` and `step_key` fields identify local evidence-bearing statements and
cannot serve as NamedNode IDs, top-level biological endpoints, authority terms
or SSSOM mappings. The parent reaction and every nested public participant
remain existing declarations checked by this gate. An unresolved source
conflict does not grant a synonym, exact-match mapping or label override.
See [the graph contract](CAUSAL_GRAPHS.md) for exact decomposition and scoped
alternative-interpretation rules.

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

The direct `common-name` supplies the canonical label whenever that slot exists;
an empty, duplicate or malformed direct name fails instead of triggering another
name search. When the slot is entirely absent, a bounded native enzyme-name
rule supports a `Protein-Complexes` member with one component at integer
coefficient two or greater and exactly one resolved `catalyzes/Enzymatic-Reaction`.
That activity must have a coherent META identity, exactly one enzyme reference
back to the same complex, one coherent native reaction reference and one string
`common-name`. The resulting authority retains the exact complex ID. SRI's
[BioCyc loader manual](https://bioinformatics.ai.sri.com/biowarehouse/repos/biocyc-loader/flatfile/doc/biocyc-manual.html)
documents linked activity names for proteins lacking `COMMON-NAME`, and its
[`full-enzyme-name` function](https://bioinformatics.ai.sri.com/ptools/ptools-fns.html)
describes native protein naming from those slots. Unnamed monomers, heteromers,
absent or noninteger coefficients, and unresolved or mismatched back-references
remain unsupported. It does not concatenate activity names or add assembly
words to a label.

An additional bounded case supports an unnamed homomer with multiple activities
only when exactly one direct native protein `synonym` matches a direct
`common-name` or `synonym` of exactly one independently validated activity.
Every activity must have a unique coherent META identity and the same exact
enzyme back-reference, an exact native reaction reference, and a valid name.
Every direct protein and activity alias is safely decoded, including unmatched
aliases; duplicate aliases and ambiguous matches fail. The matching protein
alias supplies the label and remaining direct protein aliases supply synonyms.
This is an explicit native alias, not an inferred preferred name encompassing
all functions. Activity aliases are not otherwise imported. For example, the
native CPLX-2865 alias `4-carboxy-4-hydroxy-2-oxoadipate aldolase` matches one
activity alias while its separate decarboxylase activity retains its own identity.
The complex remains CPLX-2865; the six-subunit assembly is not collapsed to its
monomer.

All name paths decode native inline presentation markup and character entities,
with no curated-label fallback. The direct-name and sole-activity paths retain
their existing output, including no imported synonyms.
Malformed or still-escaped numeric references and decoded characters outside the
supported XML character ranges are rejected; references are not recursively
unescaped to guess a label. Component, organism and curator names are not
emitted as authority terms. Apart from the explicitly validated enzyme-name
relation, nested names are not used. Nested unresolved protein references do
not imply unresolved identity of a directly named full top-level object. This extraction
establishes identifier/name provenance, not species/strain equivalence,
assembly, sequence, reaction or experimental function. Conflicting canonical
names involving an XML source fail before corpus selection, including conflicts
with a MetaCyc HTML source; existing HTML-only selection behavior is unchanged.
When the multi-activity alias case is present, competing sources for that same
body-derived ID must have compatible validated native scope: component,
coefficient, activity/reaction identities, names, aliases, and PGDB version.
Conflicting assertions fail even with identical labels and unselected IDs, in
either manifest order. A direct-name, sole-activity, or HTML source for the same
ID is conservatively rejected as mixed scope. IDs without this new case keep
their previous behavior. Native activity order does not change the signature.

A term with `label_kind: source_context` is an identifier assertion in an
independent source's cross-reference or local graph, not a canonical name
assertion by the target namespace. Such a term can only satisfy an explicitly
contextual slot. It cannot satisfy canonical-label verification even if the
strings happen to match. This records the evidence boundary for native IDs
whose independently available source supplies membership but no canonical name.

The `metacyc-reaction-xml` source kind supports bounded unnamed native
small-molecule and whole-carrier protein-modification reactions. It accepts only an exact HTTPS request
`https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=META:<frame>` and one original
full META `Reaction` with matching metadata query, PGDB version, species
`MetaCyc`, and identity attributes. The root software-version field must also
match this supported serialization; it does not replace the explicit PGDB
version check. The exact HTTPS base/service or the observed mirror's literal
HTTP-with-port-443 base/service are supported. Alternate requests, ports,
duplicate metadata/entities, top-level reaction class instances, HTML, DTDs and entities fail.
Original declared XML encoding and bytes are retained unchanged.

The original small-molecule mode requires exactly both native
`Chemical-Reactions` and `Small-Molecule-Reactions` parents and exact empty META
Compound side references. A separate mode requires exactly one
`Protein-Modification-Reactions` parent, with at least one direct whole
`Protein class="true"` on each side; its other direct sides may be Compound
references. Neither unions of the parent modes nor arbitrary Protein instances
are supported. Both modes retain native direction and nonempty left/right
sides. Explicit coefficients/compartments remain unsupported; omitted native
coefficients remain omitted in the source assertion. The optional literal
Compound `class="true"` marker is retained. Other markers, unresolved/cross-PGDB
references, duplicate frames per side, or malformed wrappers fail. New-mode
conflict signatures retain XML participant type as well as frame/class marker;
old-mode signatures are unchanged. A direct `common-name` slot of any shape also fails: named
reaction support is not an implicit fallback. Nested evidence/curator names,
equations and curated labels never supply a canonical reaction name.

The emitted label is only the exact native frame token, with no synonyms,
`label_kind: source_context` and `entity_type: reaction`. Its source metadata
carries `kind: metacyc-reaction-xml`. These optional fields have closed validation:
the type and source kind must occur together, with a coherent MetaCyc identifier,
frame-token label and source-context scope. The loader also requires the exact
META frame requested by its source URL at the HTTPS endpoint
above, with no extra query fields or fragment and with a dotted numeric native
version. Each term must match its source's requested frame; one source cannot
establish a different typed identity. These offline checks establish internal
snapshot consistency. The builder checks the original XML bytes, including
their agreement with the request and version. This typed authority can satisfy
only a `reactions` node explicitly categorized `molecular_activity`. The checker
enforces this restriction **before** contextual-label bypass, so the same ID
cannot pass as a record title, pathway interface, protein, complex or chemical.
An explicit contextual policy is still required; native identity is not a
canonical name authority. Existing authority objects without these fields keep
their prior behavior and bytes. Builder and checker support must be adopted
together; older checkers correctly reject the unfamiliar fields.

Conflicting same-frame reaction versions, parents, directions, sides or native
flags fail before corpus selection. A same-frame assertion from a different
source kind also fails rather than dropping the reaction type or inventing a
canonical name. This identity support does not establish pathway membership,
selected physiological flux, catalytic machinery, or chemical equivalence;
those claims still require separate mechanistic evidence.

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
primary definition from an export that also contains attached pathway
interface stubs. The request must agree with the native SMPDB assertion; neither
the first XML object nor the filename selects the pathway. Extra Pathway objects
must be explicitly attached stubs in a supported native format, not unrelated
or expanded definitions. The original `SubPathway` format contains native
Interaction objects and attaches directly through the primary pathway
components or ordered steps. The selected primary pathway supplies its
canonical pathway term. A directly attached, validated interface also supplies
its exact SMPDB identity and one direct, nonempty biological `displayName` as a
canonical title. Duplicate, empty, nested, or generic `SubPathway` display names
fail; the generic `SubPathway` marker is not a synonym. Conflicting native pathway
names across inputs fail before corpus selection, including a child versus a
separately supplied primary definition. Matching names retain the first source's
provenance. This is issuing-source identity/name support, not a claim to have
retrieved the interface's complete definition or established its chemistry.
Only the primary pathway scopes local graph identifiers; no child chemistry or
local graph expansion is inferred. Legacy archive inputs still require exactly
one Pathway. Native Interaction objects are not emitted as reaction authorities.
Compartment-scoped physical objects keep distinct local IDs even when they share
a chemical reference; identity alone does not assert material transfer or exact
chemical equivalence between those objects.

A second closed format has an empty `InhibitorySubPathway` interface attached
through an Interaction owned by the primary pathway. A direct component pointer
or an exact `PathwayStep`/`stepProcess` chain must reach that Interaction. The
Interaction has the native `InhibitorySubPathwayControl` marker and exactly two
participants: one resolved local SmallMolecule and one independently accessioned
Pathway. The compound retains its `SubPathwayInhibitor` marker and resolved native
SmallMoleculeReference; the child has a single biological displayName and matching
SMPDB unification identity, with no expanded pathway content. Duplicate, dangling,
extra or unsupported participants, fields, markers and ownership paths fail.
Generic marker names are not biological title synonyms. Neither these names nor
this attachment authorizes an inhibition edge, chemical equivalence, directed
pathway dependency or child reaction membership. This branch supplies only the
issuing pathway identity; it does not scan arbitrary descendant interactions.

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
Legacy extracted-member inputs must preserve unmodified bytes, with the exact
member path and archive digest recorded in `sha256_scope` when the public URL
is a ZIP. The typed ZIP source below binds both the whole archive and member
directly instead of using that legacy free-text scope.

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

`bigg-universal-metabolite-json` and `bigg-universal-reaction-json` read one
original BiGG universal API object. An exact HTTPS request under
`https://bigg.ucsd.edu/api/v2/universal/metabolites/<id>` or
`https://bigg.ucsd.edu/api/v2/universal/reactions/<id>` must agree with the source
kind, native `bigg_id` and object shape. Model-specific endpoints, lists,
HTML/error bodies, non-UTF-8 JSON, duplicate JSON keys and missing or ambiguous names fail.
Only the universal native name supplies the canonical `BiGG` label; there is
no contextual-label exemption. `old_identifiers` are not name synonyms, and
cross-database links do not emit other authority terms.

Each BiGG manifest entry requires a `version_source` object containing a
relative cache `path`, `sha256`, and the exact URL
`https://bigg.ucsd.edu/api/v2/database_version`. Its original JSON must state
API `v2`, a `bigg_models_version` matching the manifest's
`BiGG Models <version>; retrieved YYYY-MM-DD`, and a valid `last_updated`.
This companion remains explicitly hash-bound in the manifest; the existing
snapshot source metadata shape is unchanged. Conflicting names, object kinds
or releases for the same BiGG identity fail before corpus selection. Observations
of one native release must also agree on its unaltered update timestamp; no
timezone is inferred from that timestamp.

Universal metabolite and reaction objects remain distinct. Their names do not
establish chemical equivalence, compartments, model reaction bounds, gene
rules or physiological direction. In particular, acmana's source InChIKey
discrepancy and the universal ACMANAptspp arrow versus iML1515 bounds remain
separate evidence assertions, never silently repaired by label extraction.

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

The `pubchem-compound-property-json` source kind accepts one original PubChem
PUG REST property response. Its request must be exactly
`https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/<CID>/property/Title,IUPACName,MolecularFormula,InChIKey/JSON`,
with one positive numeric CID. The single native `PropertyTable.Properties`
object must carry that same integer CID and all four requested properties.
Only its nonempty `Title` supplies the canonical `PubChem` name. The adapter
rejects malformed or non-UTF-8 JSON, duplicate keys, nonfinite numbers, error
objects, multiple compounds, missing/empty/malformed fields and mismatched IDs.
Conflicting titles for a CID fail before corpus selection. Original bytes must
match the manifest digest; missing required PubChem terms remain blocking.

PubChem uses canonical-label policy with no contextual exemption. The adapter
does not promote `IUPACName`, cross-database identifiers or separately downloaded
synonym lists to accepted names. Formula and InChIKey validate the response
shape and do not establish equality with another chemical source. A provenance
version such as `PubChem PUG REST CID 78645 property snapshot retrieved 2026-10-12`
records an acquisition snapshot; this response supplies neither a native entry
version nor a global release. Hash the complete unmodified response and retain
its actual acquisition receipt externally. Optional synonym evidence needs its
own original digest. Keep the issuing source's terms and license-review scope;
do not infer a new release or license from a successful HTTP response.

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
unsupported by these three profiles. These rules follow the native
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

`kegg-gene-flatfile` is a separate, typed complete-CDS profile. It requires one
exact official HTTPS `/get/<organism>:<locus>` request. The ENTRY locus, CDS type,
native genome identifier and ORGANISM code are checked and retained; the locus
and organism must match the request. The canonical gene label is the exact
ENTRY locus. NAME remains functional annotation in the source metadata and
does not become a gene symbol, protein label or accepted synonym.

The complete UTF-8 flatfile is retained in `native_gene`, alongside all ordered
fields, the native genome/organism scope, position, amino-acid sequence and
nucleotide sequence. One terminated object, unique required fields, fixed field
columns, declared sequence counts and alphabets, a simple forward or complement
genomic span, complete-CDS length relationship and terminal stop are required.
The span must equal the nucleotide length. This profile does not validate the
translation or independently resolve the genome-ID/organism-code crosswalk;
those are separately grounded scientific identity checks. It does not accept
joined, partial or ambiguous sequences by guessing missing source context.

`kegg-pseudogene-flatfile` is a distinct, explicitly selected annotation profile.
It requires the same exact organism:locus request, complete fixed-column object,
identity fields and genomic-span/count checks, but ENTRY must have native type
`gene`, NAME must be exactly `(GenBank) pseudogene`, and AASEQ must be absent.
NTSEQ is retained as the issuing annotation only: it does not establish the
complete biological gene, a translated product or a functional protein. A short
native annotation such as the three-base PP_2519 object is not expanded or
translated. The profile records `native_type: gene`,
`annotation_class: pseudogene` and `sequence_scope: native_annotation_only` in
`native_gene`; it does not manufacture an `aaseq` projection. SYMBOL remains
source annotation, not an accepted alias. The original `project(raw, url)` and
`kegg-gene-flatfile` default remain the strict complete-CDS profile and never
fall back to pseudogene handling. Pseudogenes require `project_pseudogene` or the
explicit distinct source kind. Conflicting CDS/pseudogene owners for one locus
fail before term selection in either order, including unselected owners.

The consumer rehashes and reparses the entire retained original and requires
its derived projection to agree exactly, including every field and sequence.
Conflicting whole originals or versions fail across all supplied owners before
corpus selection. A gene request or KEGG organism:locus identity cannot be
laundered through another source kind. Typed gene terms are accepted only in
`participants` with `category: gene`, under the existing canonical label policy;
contextual labels cannot supply a curated gene alias. This support establishes
issuing identity, not expression, transport, regulation or assay-construct scope.

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


### Native EcoCyc complex and RNA identities

The `ecocyc-protein-xml` and `ecocyc-rna-xml` source kinds establish exact
`EcoCyc` authority from native ECOLI objects. The current bounded protein
classes are `Protein-Complexes` and `Protein-Small-Molecule-Complexes`; the RNA
class is `Regulatory-RNAs`. The adapter requires one direct full entity, one
direct resolved string common-name, and matching native parent identity.
Only direct native string synonyms become aliases. Names and aliases share
safe markup/character checks; malformed or duplicated names fail. Nested
genes, proteins, activities and cross-references are never promoted. There is
no enzyme-name fallback and no contextual-label exception. The namespace uses
`canonical_or_synonym` solely for these independently sourced names.

The issuing URL must be exactly
`https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=ECOLI:FRAME`.
The request, XML base, metadata service/query, PGDB/version, species, strain
and NCBITaxon 511145 must agree. The native originals serialize their XML base
as `http://bf2i-artsymbiocyc.insa-lyon.fr:443/getxml?ECOLI:FRAME` and service as
`http://bf2i-artsymbiocyc.insa-lyon.fr:443/`; only those literal legacy forms
are accepted alongside the exact HTTPS forms. This serialization exception
does not permit HTTP issuing requests, arbitrary mirrors or alternate ports.
DTD/entity declarations are rejected during XML parsing, including UTF-16.
Duplicate identities must agree on type, parent, name, aliases and version;
conflicting ECOLI releases fail before corpus filtering. Unsupported upstream
serialization changes require a reviewed adapter change.

`EcoCyc:CPLX0-226` names the CRP–cAMP complex, `EcoCyc:PC00004` the CRP
complex, and `EcoCyc:RNA0-241` SgrS RNA. Identifier authority does not infer
component coefficients, sequence equivalence or regulatory effects. Preserve
explicit `complex` and `rna` categories in curated records; graph labels and
KGX retain them without a prefix-wide reaction classification. Public citations
use `https://ecocyc.org/gene?id=LOCAL_ID`. Acquisition receipts and full original
bytes remain outside curated records, and public-release licensing is deferred.

### Exact PathBank archive selection

`pathbank-biopax-zip` reads the independently acquired official primary ZIP at
`https://pathbank.org/downloads/pathbank_primary_biopax.zip`. Its manifest `path`
points to the original ZIP, and `sha256` hashes that whole ZIP. A required closed
`archive` object contains `bytes` (positive integer archive byte count), `member`
(an exact `PW` plus digits and `.owl` filename), `member_bytes` (positive integer),
`member_sha256` (the exact unmodified member digest), and `root` (the selected
native `SMP` accession). Neither a filename nor a curated label supplies the
root identity. The ZIP and selected member hashes and byte counts are verified
before XML parsing. Missing or duplicate selected member names fail.

This separate source kind applies the existing exact primary-pathway and
attached-interface checks to that verified member. The selected root must match
its native SMPDB assertion; unrelated or expanded extra pathways still fail.
The builder preserves the closed archive object, typed `kind`, real archive URL
and whole-archive digest in source metadata. It also emits `pathway_accessions`
from the verified primary and attached objects, with the selected root first.
The snapshot consumer validates those typed fields and restricts associated
terms to those pathway accessions or the selected root's local graph IDs.
Canonical pathway titles and contextual local labels retain their prior rules.
Typed fields cannot be attached to an untyped or different source kind.

A frozen archive member is never attributed to a live per-pathway URL. This
kind does not accept `sha256_scope` as a substitute for typed byte bindings.
Legacy `pathbank-biopax` extracted single-pathway members retain their earlier
`sha256_scope` behavior, and actual per-pathway downloads keep their existing
selection contract. Existing authority entries need no format migration.

### Native Compound class references

An unnamed `metacyc-reaction-xml` small-molecule reaction may have the optional
literal `class="true"` on a direct Compound side reference. The exact native
resource, organism and frame guards still apply; other class values, extra
attributes, class markers on side wrappers and duplicate side frames fail.
The class marker is retained in same-frame conflict comparisons, so a class
reference cannot silently overwrite an unmarked assertion. This does not alter
the unnamed frame-token authority label or establish chemical/anomer identity.


## Native carrier classes and protein state instances

`metacyc-carrier-class-xml` owns explicitly typed, directly named META classes.
It accepts a whole Protein class with direct `Thioredoxin` parent, optionally
also `Modified-Proteins`, and the corresponding single native modified/unmodified
state link. It separately accepts a Compound class with the exact direct parent
`Hydride-Acceptors`. Both cases require literal top-level `class="true"`, one full
native object, exact HTTPS issuing request/query/PGDB/release identity and safe
direct common-name/synonym slots. There is no nested-name or xref fallback.

The source contains closed `native_carrier_class` metadata with native type,
class marker, parents, names and the explicit Protein state link. Terms have
`entity_type: protein_class` or `chemical_class` and source-native names.
The loader permits only `participants/category: protein` or
`participants/category: chemical_entity`, respectively, and checks canonical or
authorized synonym names before any contextual-label exemption. Generic electron
carrier classes do not establish exact homogeneous client chemicals, formulas,
charges, sequence identities or reactive-part/whole-protein equivalences.

`ecocyc-protein-state-xml` is separate from the named-protein and complex adapters.
It supports exact ECOLI thioredoxin state **instances**, with the native
`Red-Thioredoxin` parent or `Modified-Proteins` plus `Ox-Thioredoxin` parents.
It retains direct source names, a single state link and a direct gene reference.
The source entry requires `counterpart_source`, a separate whole original with
closed `path`, `url`, `version`, `sha256` and `license` provenance. Both objects
must carry the exact ECOLI species/strain/taxon and same release, reciprocal state
links, opposite states and matching native gene identities. Each original is
hashed independently; counterpart assertions participate in conflict checks
even if only the other member is selected by the corpus.

The state source includes closed `native_protein_state` and `counterpart`
metadata. Its term has `entity_type: protein_state`, restricted to
`participants/category: protein` with source-native canonical/synonym names.
A reduced state whose direct common-name is `thioredoxin 1` keeps that name;
state assertions do not authorize rewriting it or identifying an engineered
mutant/construct. All selected state counterparts must remain explicit originals
in source inventories, copy plans and archives; a top-level-path-only collector
is insufficient. This is independent of the accepted complex adapter's separate
`class_source` requirement, which remains unchanged.

Class/state conflicts, issuing identity mismatches and malformed originals fail
before corpus filtering. Typed identities cannot be overwritten by legacy
untyped sources or used as pathways, reactions, small molecules or complexes to
bypass placement checks. Whole Rhea components 10698/10700 remain whole generic
protein redox states; ChEBI reactive parts do not replace those proteins. Native
Protein and Compound class references preserve both events of a carrier cycle,
including the generic-client reaction when it lacks an exact Rhea mapping.

## Bounded anaerobic benzoyl source shapes

Five separate MetaCyc 27.0 source kinds retain complete native objects that do
not fit the older homomer, carrier, acyl-transfer or unnamed-reaction profiles.
Their manifest fields are `key`, `kind`, `path`, `url`, `version`, `license` and
`sha256`; URLs are literal HTTPS `getxml?id=META:<frame>` requests to the pinned
issuing mirror. The existing profiles and their restrictions remain unchanged.

| Source kind | Accepted native scope | Term scope |
| --- | --- | --- |
| `metacyc-heteromer-activity-xml` | Unnamed CPLX-1341, four distinct Bcr components with coefficient one, exact ENZRXN-1821 enzyme/reaction links, full species and ancillary context | `protein_complex`, canonical linked activity name; participants/category complex |
| `metacyc-ferredoxin-reaction-xml` | 1.3.99.15-RXN, PHYSIOL-R2L native direction, exact Compound/Protein equation and coefficients, both activities and EC-1.3.7.8 context | `reaction`, frame-token contextual display; reactions/category molecular_activity |
| `metacyc-ferredoxin-class-xml` | Both complete Reduced-/Oxidized-ferredoxins classes, exact Ferredoxins parent sets, generic cluster-unit names, state links, members and all equation/context slots | `protein_class`, native canonical/synonym names; participants/category protein |
| `metacyc-hydrolytic-composite-xml` | Reversible OAHTHAUERA-RXN, EC-3.7.1.21, two-water net equation and two complete constituent originals | `reaction`, frame-token contextual display; reactions/category molecular_activity |
| `metacyc-named-reaction-xml` | RXN-8032 with its direct native common-name, complete reversible equation and embedded PimB activity context | `reaction`, direct canonical name; reactions/category molecular_activity |

Closed `native_benzoyl` metadata retains each exact original UTF-8 XML body,
including envelope and every native slot, together with its independently
computed typed projection. The offline consumer hashes the full original body
against source provenance and re-parses/re-projects it before accepting terms.
Malformed envelopes, release/identity mismatches, incomplete slot inventories,
wrong component or material types, altered coefficients, activity back-reference
errors and metadata edits fail closed. This does not establish authenticity of
an arbitrary replacement response: acquisition receipts and pinned source hashes
remain the provenance evidence. No source body is generated from curated labels.

The hydrolytic composite additionally requires `constituent_sources`, an ordered
list of two closed `path`, `url`, `version`, `license`, `sha256` descriptors for
RXN-15012 and RXN-15013. Each full original is hashed independently and retained
in `native_benzoyl.companions`. Exact member identities/order, both native
composite backlinks and the signed sum of both equations are checked. CPD-15900
must cancel, and the resulting net must equal the original two-water composite.
Separate ordinary constituent owners remain valid only with identical original
URL/release/hash provenance. The first selected owner remains unchanged.

All six top-level identities are protected from a downgrade to legacy source
kinds even when no typed owner or term is selected. Complete-owner conflicts,
request-only competing claims and companion provenance conflicts fail before
corpus filtering, in either source order. Selected terms must exactly equal their
complete owner projection. Canonical native reaction names are checked before
namespace contextual-label exemptions, as are complex and carrier names.

These authorities do not add pathway membership or catalytic evidence. Oah is
an auxiliary net activity without an eighth selected route membership; formal
constituents do not prove a free released intermediate or separate assays.
Ferredoxin coefficient two denotes two native generic cluster redox units, not
two whole two-cluster proteins. The direct RXN-8032 name does not turn predicted
PimB annotation or operon-level evidence into purified individual-enzyme proof.
Full original context, preparation limitations and conflicting scientific claims
remain separately assessed when curating a record.

## Native electron transfer, named complexes and chemical classes

Four explicit source kinds support complete electron-transfer route identities.
Their manifest entries have closed `key`, `kind`, `path`, `url`, `version`,
`license` and `sha256` fields. Original paths must resolve to regular files;
whole original bytes, issuing request identity and native release are checked
before corpus filtering. Existing source precedence remains unchanged.

`metacyc-electron-transfer-reaction-xml` accepts an unnamed full META Reaction
instance with exactly `Electron-Transfer-Reactions` and
`Small-Molecule-Reactions` parents. It retains direction, every ordered Compound
side, explicit coefficient versus implicit one, and exact optional native
CCO-IN/CCO-OUT compartment references. Composite reaction lists and their
ordering must be complete, member-consistent and acyclic. The term keeps the
frame token, `entity_type: reaction` and `label_kind: source_context`. Only
`reactions/category: molecular_activity` can use the existing contextual-label
rule. Opposite-side hydrons remain separate entries; native compartments do not
automatically assert a taxon's anatomy. Constituent half-event originals are
scientific evidence, including literal electrons, rather than invented CURIEs.
The existing `metacyc-reaction-xml` reader retains its own contract.

`ecocyc-named-protein-complex-xml` requires one directly named ECOLI Protein
instance with the sole `Protein-Complexes` parent and complete explicit Protein
components and positive integer coefficients. A one-component complex requires
at least two copies. Its canonical name and direct synonyms are retained in
`native_named_complex`; the term is `protein_complex`, with a canonical label.
Only `participants/category: complex` is allowed. The namespace's normal label
policy governs real synonyms; contextual labels cannot bypass placement or name
checks. This mode shares whole ECOLI conflict and release guards with proteins,
states and unnamed complexes without changing their accepted parsers. Native
reference composition does not identify a purified or engineered construct.

`metacyc-chemical-class-xml` requires a whole directly named META Compound with
explicit `class="true"`. Exact structural parent sets determine the profile:
`ETR-Quinones`; `ETR-Quinols` plus `Methoxybenzenes`; `Cofactors`, `Hemes` and
`Organometallics`; `Organometallics`; or `Glycerolipids`. These profiles allow
`chemical_entity`, with `cofactor` additionally allowed for the two cofactor
profiles and `lipid` for glycerolipids. Cofactor profiles require complete native
activity annotations. Direct parent, subclass and instance lists remain ordered,
distinct and class/instance-consistent. `native_chemical_class` metadata derives
the new `native_chemical_class` term type and allowed participant categories.
This does not broaden the existing carrier-class mode or equate a class drawing,
xref, heme stereoisomer or mixed lipid preparation with an exact chemical species.

All three XML modes preserve complete ordered source slots, native attributes and
ancillary context. The closed slot grammar checks direct structures and xrefs;
scientific comments and embedded activity context remain source assertions rather
than aliases or independently verified biological claims. Consumer validation
reconstructs the typed projection from the retained safe XML subtrees and checks
all projected fields. Incompatible native facts or cross-kind assertions fail
in either manifest order, including when the identifier is not selected.

## Whole Rhea Polymer components

`rhea-polymer-rdf` reads the whole pinned gzip at the issuing Rhea RDF URL. It
uses `RHEA-COMP` for complete Polymer objects while retaining their native
`POLYMER` accessions; it introduces no new prefix or exact-chain-length claim.
The existing `rhea-components-rdf-gz` GenericPolypeptide reader remains separate.
Whole subjects aggregate all original RDF fragments before selection. Conflicting
ID, accession, type, name, index or underlying-ChEBI assertions fail. Compatible
split descriptions and exact repeated triples retain every original fragment.

Closed `native_polymers` metadata retains plain and HTML names, formula, charge,
variable index, underlying ChEBI resource and complete original fragments for
emitted terms. The required index grammar is `n` or `n` plus/minus a positive
integer. The exact native plain name is canonical, with no manufactured aliases.
Terms have `entity_type: rhea_polymer` and are restricted to
`participants/category: polymer` under the existing canonical label policy.

HTML/plain comparison validates balanced lowercase `i`, `small`, `sub` and `sup`
without attributes. Only alpha, beta, gamma, omega, right/bidirectional arrows and
Unicode minus receive explicit comparison-only typography substitutions. Subscript
text is preserved; positive integer or minus superscripts become parenthesized
text. Numeric references must decode to permitted safe characters. Case, spacing,
stereochemical letters, punctuation, indices and arrow direction are otherwise
exact. Formula and charge remain validated source strings rather than evaluated
expressions. Comparison projections are never emitted aliases. Unsupported
upstream shapes require a separately reviewed adapter change.


## Typed native pathway and nitrate source contexts

`metacyc-pathway-xml` requires one whole META Pathway instance and matching
request, PGDB, release, direct identity, source hash and envelope. Compound-page
HTML with the same title cannot establish typed Pathway identity or share its
selected identity with this mode. Existing legacy HTML records retain their
existing authority contract. The direct common name and synonyms, parent
classes, complete reaction list, acyclic ordering, exact layout membership and
class-marked organism annotations are retained in `native_pathway`. Layout
primaries are source layout context, not complete biochemical equations.
Complete source slots preserve comments, credits, species and taxonomic scope.
The `native_pathway` term is accepted only as the canonical record node; a
contextual label policy cannot make it a participant, reaction or taxon.

The native electron-transfer annotation reader also retains a three-level
numeric EC context such as `EC-7.1.1` verbatim. This does not create a selected
EC identifier, infer a fourth level or extend the existing four-level EC grammar
to new partial forms with unassigned markers.

Named complexes retain typed GO class references and evidence codes,
instance publications, optional evidence `with` text, reverse `component-of`
references, native location references, and the experimentally reported mass
with its citation. The consumer compares each named complex's complete reconstructed native
assertion, source kind and release across every owner before term selection.
Identical duplicates are allowed; differences in coefficients, retained
annotations or release fail even when an owner has no selected term.
Forward component cycles among supplied whole assemblies
fail; reverse context does not create an assembly cycle. Native nested
composition and coefficients are not flattened or normalized to match a
protein count, construct, or a different source's oligomerization claim.

Chemical-class profiles additionally recognize these exact parent sets:
`CPD-11501` plus `ETR-Quinones` (chemical entity); `ETR-Quinols` (chemical entity);
`FeS-Centers` and `Metal-sulfur-Clusters` (each chemical entity or cofactor).
Cofactor authorization continues to require whole native activity context.
The literal charged Compound-class subclass references `4Fe-4S+1`, `4Fe-4S+2`
and `4Fe-4S+3`, and the cofactor-activity Reaction reference
`PYRUVATE-DEHYDROGENASE-NADP+-RXN`, use an exact, closed context-only identity
check. Literal plus signs and resource bytes remain unchanged. Encoded, doubly
encoded, space-decoded, wrong-type, wrong-class, truncated or extra-query
variants fail. This does not change carrier, state, selected-ID or request
syntax. Consumer validation reconstructs all these typed metadata projections
from complete retained native source slots.

The aceto authority profiles retain complete native envelopes and direct source
slots under `native_aceto`; their consumer reconstructs and validates those
objects before checking selected terms. The producer hashes complete original
responses. Offline reconstruction verifies internal coherence, not upstream
reacquisition or cryptographic authentication of XML through its serialization.

- `metacyc-sgd-pathway-xml` admits the exact SGD HTTPS META request and observed
  22.5 envelope. It retains whole experimental evidence and pathway interfaces,
  including native reverse layouts, without treating layout primaries as full
  equations or linked pathways as selected nodes.
- `ecocyc-nested-complex-xml` admits an unnamed two-child assembly with explicit
  coefficient-one children. Its ordered `component_sources` descriptors bind
  complete, named, same-release homomers with distinct leaves and reciprocal
  parent references. Native experimental mass and activity context remain
  attached to the original assembly; the display is the derived unnamed label.
- `metacyc-acyl-transfer-composite-xml` admits the reversible two-constituent
  composite profile without inventing reaction ordering. Ordered
  `constituent_sources` preserve the whole constituent equations and Reaction
  backlinks. Signed identity/type/class/coefficient cancellation must reproduce
  the native composite. Source direction remains separate from pathway traversal.
- `metacyc-protein-residue-class-xml` admits the two explicit protein-bound
  residue profiles with a whole reciprocal `parent_source`. Mixed Compound and
  Protein class context remains typed. Complete CML is checked as serialization,
  with generic protein/R endpoints and unspecified formulas retained, not as a
  newly reconciled exact molecule. Selected placement is `chemical_entity` only.

Each companion descriptor has exactly `path`, `url`, `version`, `license`, and
`sha256`. Original paths are relative to the supplied cache, without traversal;
explicitly staged links retain the established regular-file/hash contract.
Companion fields are rejected on unrelated kinds. Complete companion assertions
and matching URL/version/digest are compared with separate source owners before
corpus selection, including unselected owners and both source orders. Forward
assembly cycles are checked separately from reciprocal parent context. Existing
ordinary-reaction owners supply typed identity plus matching original provenance;
they cannot replace the composite's complete constituent proof.

The four profiles preserve earlier modes, source owners, and selection rules.
Rhea labels remain selected from the pinned production SQL release; newer RDF
reaction evidence is separate. A valid PubChem property original supplies its
label, and existing first UniProt owners remain authoritative. Native source
licensing remains attached; no public-release clearance follows from parsing.

## Complete P321 native identities

The P321 source extension preserves all earlier authority owners and their
serialized metadata. The new `P321-PWY` pathway owner additionally retains the
complete original response as `original_base64` within `native_pathway`. Its
consumer hashes those decoded bytes, reparses the declared XML encoding, checks
the complete request/envelope and reconstructs every projected field. The eight
citations, direct experimental evidence and three compound-to-pathway links
remain source context; none adds a reaction or proves each lower-pathway enzyme.
The nine-member reaction list, layouts and acyclic ordering remain mandatory.

Four bounded 27.0 native profiles use the same complete-original check:

- `metacyc-etf-reaction-xml` preserves R265-RXN's reversible mixed Compound and
  whole Protein-class equation, Chemical-Reactions/Small-Molecule-Reactions
  parents, Gibbs evidence (including its publication URL), activity backlink,
  memberships and other native slots. Omitted reaction coefficients have native
  arithmetic value one; explicit versus omitted presence remains distinct.
- `metacyc-etf-class-xml` preserves ETF-Reduced and ETF-Oxidized as whole protein
  classes, with their complete, unequal parent and state-link shapes. Reduced
  ETF retains its semiquinone reference as context. Supplied paired owners must
  have reciprocal reaction context. No fixed FAD/AMP occupancy or exact protein
  sequence follows from these class identities.
- `metacyc-singleton-activity-xml` preserves CPLX-926's one native component and
  its coherent ENZRXN-1144/R266-RXN naming chain. The assembly coefficient is
  absent: `coefficient: null`, `coefficient_explicit: false`. This is not an
  inferred coefficient one or an oligomer measurement; the existing unnamed
  homomer coefficient-at-least-two contract is unchanged.
- `metacyc-gene-xml` preserves G-545/badD and G-550/badH with exact product
  companions, reciprocal native gene links, species and issuing crosslinks.
  Each `product_source` descriptor has exactly `path`, `url`, `version`,
  `license` and `sha256`. Its original must be a regular file at a relative
  cache path without traversal. Separate `native_metacyc_gene` metadata keeps
  this grammar distinct from KEGG gene metadata; canonical placement remains
  participants/category gene. Native identity does not replace a strain-specific
  sequence or establish promoter regulation.

The three non-gene profiles use `native_p321`. Each new kind has closed manifest
and metadata fields. Both builder and consumer compare the entire reconstructed
projection with the saved projection, check the exact selected term, and reject
conflicting releases, alternate scopes and request-only downgrade owners before
selection, including owners whose identifiers are not wanted. Protected prior
benzoyl identities keep their existing checks. Canonical pathway, gene, complex
and carrier names and native category checks precede contextual-label exemptions.
UniProt contextual labels retain their existing policy and original authority
names, including obsolete annotations.

An exact standalone ordinary gene-product owner can coexist with its complete
native gene and companion in either order, even when one owner has no selected
term. The builder retains the actual manifest kind in temporary assertions only.
Ordinary serialized metadata remains exactly `url`, `version`, `license` and
`sha256`, without an added kind. The consumer accepts that legacy shape only
against the complete reconstructed companion's exact URL, release and raw hash.
Wrong kinds, additional provenance fields, alternate request-only URLs and
changed originals or releases remain conflicts; dropping the kind from a
manifest does not gain this consumer-only compatibility.

Original-byte base64 retains encoding declarations, non-ASCII text and whitespace
without normalizing source XML. DTDs and entities are rejected. The test fixture
uses separately hashed, deterministic gzip storage and recovers exactly the
issuing originals before parsing. These are identity/integrity checks, not an
upstream signature, scientific activity proof or redistribution-license decision.

## Complete phenylacetate native authority originals

The bounded `metacyc-phenylacetate-xml` and `ecocyc-phenylacetate-xml` source kinds
cover the independently inspected PWY0-321 native identities and explicitly
reviewed Paa chemistry/regulation context. They do not widen the P321-PWY profile.
The profile contains reviewed frame identities, native object types and direct
slot multiplicities; labels and synonyms are read from the issuing original XML,
never from curated record labels or a preferred-name table.

Both producer and consumer verify the entire response body's SHA-256, the exact
request/frame/PGDB/release envelope, one complete instance object, direct slot
inventory, every embedded native frame/resource identity, and exact original to
projection correspondence. Original bytes remain in `original_base64`; source
metadata and all native direct slot XML remain in the projection. META and ECOLI
cannot be interchanged. The ECOLI envelope names E. coli K-12 MG1655 and its taxon;
that catalog scope does not establish an E. coli W experimental construct sequence.

Native compounds, monomeric proteins, complexes, molecular activities, DNA
promoters/transcription units, reactions and pathway identity are distinct types.
Their required node section/category and source labels are enforced even if a
namespace permits other contextual labels. A source lacking a direct common name
uses its exact native frame ID with `label_kind: source_context`; this is not
permission to replace the label with a guessed biological name. Labels such as
AMP that equal the frame are valid when supplied by the source common-name slot.

Reaction sides and direction, activity enzyme/reaction links, complete pathway
membership, and complex component rows are projected separately. Omitted source
coefficients remain omitted (`null` in the projection); only explicit integers
are emitted. Complete source scope includes the nine PWY0-321 native reactions;
the separately reviewed salvage/lower-chemistry objects are context, not added
native pathway members. Authority identity does not assign an isolated catalyst
to a source net equation, reconcile chemical alternatives, or settle physiological
flux. In particular, the native C8-to-trans-2,3-C6 net reaction remains distinct
from the requested isolated PaaJ C8-to-cis-3,4-C6 thiolysis.

Originals and acquisition receipts for this increment are retained in
`research/pathway_additions/2026-10-15-next-268/authority-source-originals/`.
`source-provenance.json` maps all 65 identities to the exact retained body,
acquisition receipt, canonical authority request and pinned body hash. A separate
compressed fixture copy is checksum-verified before test decompression. Wrong
frames, wrong requests/releases/native types, missing or surplus slots, altered
body/projection/labels, source-owner substitution and unselected typed-source
downgrades fail closed before selection or at consumer load.

The increment preserves every existing authority term and owner, including the
six pre-existing MetaCyc terms used by the native draft. Three required taxa and
CHEBI:63252 were extracted with the existing ontology builder from read-only
semantic SQL caches that exactly match the already-pinned source hashes and
versions (NCBI Taxonomy 2026-07-12 and ChEBI 255). No source pin or release changed.
The former 264-record corpus and an isolated complete native-draft copy pass the
identifier gate; intermediate reaction nodes require explicit
`category: molecular_activity`.

This is an additive source replay. All 65 new bodies reproduce through the normal
source builder. Existing snapshot terms/metadata are reused unchanged and passed
through the full consumer; this does not claim that all historical source bodies
were newly downloaded or regenerated.

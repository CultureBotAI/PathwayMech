# L-ascorbate degradation I author dossier

This dossier supports `MetaCyc:PWY0-301` in
`data/pathways/l-ascorbate-degradation-i.yaml`. It preserves the complete native
MetaCyc 27.0 five-event boundary and the distinctions from the older 22.5
four-event definition and the existing L-lyxose route.

The stable author candidate passed the record schema with 35 participants,
five core reactions, one downstream pathway interface, 55 edges and 36
references. Its SHA256 was
`b729f7688c5eccf6db7372f7878d68284cfad0c384d5b6e9d5fe39be63ac4d60`.
This is an authoring checkpoint, not a claim that later maintained bytes are
identical or that scientific review is complete.

Start with `reading/SCIENTIFIC-READING.md` for findings and access limits and
`HANDOFF.md` for the full scope. `author/edge-source-matrix.json` binds each
edge and qualifier to its source locator and original bytes.
`author/node-identity-matrix.json` lists every graph identity and exact native
labels. `author/dedup-receipt.json` records a fresh search including hidden and
ignored files without directory exclusions; the exact maintained record check
found 242 records and no `MetaCyc:PWY0-301` duplicate. Prior lyxose dispositions
are retained in their existing repository dossier.

Complete source bodies remain outside the repository, as required by
`docs/CAUSAL_GRAPHS.md`. They were preserved without modification in three
deterministic archives under the external author workspace. The maintained
`evidence/external-archive-manifest.json` records each archive filename, byte
hash and size, member name/hash/size, original public URL and version where
available, plus its retained external location. Every member was read back and
hash-verified. This is an acquisition receipt, not a claim that a temporary
filesystem path is a public or permanent source.

The original URLs, explicit versions, complete original hashes, exact source
locators and bounded source projections identify the evidence independently of
that temporary path. Acquisition failures and metadata-only responses remain
distinguished from usable scientific sources. No complete raw download or
source archive is committed in this dossier.

- `author-originals.tar.gz` preserves primary papers, figure images,
  metadata-only responses, access observations and acquisition receipts.
- `authority-originals.tar.gz` preserves native XML, exact identity HTML,
  UniProt and NCBI Gene responses, including failures and redirect bodies.
- `reused-reference-originals.tar.gz` preserves the whole Rhea RDF and the two
  CRP/IHF native complex originals cited by this candidate.

Archive metadata uses zero mtime, uid and gid, empty owner names, fixed
permissions and sorted paths; gzip metadata has zero mtime and no filename.
The external archives are evidence retention artifacts. Maintained JSON uses
`original_locator` objects combining public provenance with archive member
bindings, while external paths survive only as acquisition history.

`authority/provenance-manifest.json` and the per-batch receipts preserve request
and final URLs, times, versions, body hashes and acquisition outcomes. The
canonical source staging and adapter probes are documented in
`authority/INTEGRATION.md`. Canonical ontology/source term projections are
maintained separately in `data/identifier_authorities/ontology.json` and
`data/identifier_authorities/sources.json`, with ontology issuing provenance in the snapshot `sources` section and
source-object provenance in `conf/identifier_sources.json`; the per-node
SQL projections here are inspection aids, not new issuing sources.

Material limits remain explicit: the UlaG 2010 and UlaR 2008 papers were read
as primary abstracts, not unseen full bodies; UlaF zinc is a similarity
annotation; reporter conditions are strain-specific; the HPr-fed net transport
is not equated with the current generic Rhea donor reaction; and proposed
looping or inducer exclusion is not presented as directly measured chemistry.
Parent integration owns the native scientific review, curation history,
generated pages, gates and publication.

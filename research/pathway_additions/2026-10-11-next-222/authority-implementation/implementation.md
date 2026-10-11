# External authority implementation: full Adenine and Adenosine Salvage II

This is an independently reviewable external implementation against a read-only
git archive of commit `0227eb43e306d989240369c083b717230ef2ede1`. Only five files
in `repo/` differ from that baseline. `change.patch` contains those changes;
`checks/file-scope.json` checks all 5,315 archived files against the
original archive and verifies that all unrelated files are byte-identical. No maintained worktree, source cache, Git metadata, or GitHub
state was written. No dependency synchronization or environment installation was
performed. All Python commands use the retained next-195 runtime with bytecode
disabled.

The implementation supports the accepted full target
`11ceb3fe99f2ed2966bb8a68faf8fa836a6a4a9e94b2bc0c499bb1119fd3cddd`: three chemical
reactions, native adenine/proton transport, and the opaque Aspartate Metabolism
interface, with separately grounded gene-regulatory participants. It does not
substitute the shorter MetaCyc chemical core or rewrite any issuing source.

## Files and behavior

- `scripts/build_source_identifier_snapshot.py`: exact official PathBank
  per-pathway requests select a verified primary SMPDB accession independently
  of object order. All Pathway URIs in such an export must agree with their
  native xrefs. Extra Pathway objects must be explicitly attached native
  SubPathway stubs containing Interaction objects. A requested stub, unrelated
  definition, duplicate accession, unresolved link, or ambiguous identity fails.
  Legacy archive selection still requires a single Pathway. Native Transport
  joins the existing local graph object kinds; native Interaction does not.
  Local objects preserve source graph identity, not asserted elementary
  membership or chemical equivalence. Only the selected primary root yields a
  canonical pathway term.
- The same builder adds `ncbi-entrezgene-xml`: one exact official Gene EFetch
  request, matching direct Gene-track ID, direct locus symbol/formal-symbol
  agreement, native synonyms/locus tag, and unambiguous native source taxon.
  It rejects duplicate or redirected identities, deprecated/contradictory
  explicit status, placeholder names and internal XML subsets/entities.
  Native external NCBI DOCTYPE declarations are accepted with DTD loading and
  external entity resolution disabled. The same buffered original bytes are
  checked and parsed. Cross-source name/alias/taxon conflicts fail before corpus
  selection and independently of source ordering.
- `conf/identifier_policy.yaml`: Entrez uses the existing source snapshot and
  canonical-or-synonym comparison; there is no contextual exemption. Entrez is
  also in the builder's required-source namespace set.
- `tests/test_pathbank_identifier_authority.py` and
  `tests/test_ncbi_gene_identifier_authority.py`: positive source shapes plus
  adversarial request, URI, accession, stub, scoped-object, gene identity,
  status, taxon, alias, XML encoding/entity, conflict-order, identifier-gate
  and output-preservation cases.
- `docs/IDENTIFIERS.md`: documents the exact source boundaries, source-context
  meanings, compartment distinction, gene aliases/status semantics, and failure
  cases. The general BioPAX draft importer, LinkML/schema, predicate vocabulary
  and MetaCyc XML parser are unchanged.

## Verification evidence

The final relevant suite passed **579 tests** in 12.27 seconds (live session 73578,
terminal `f5039a`, exit 0). This covers both changed suites and existing MetaCyc,
KEGG, MetaNetX, Rhea-component, snapshot-builder, identifier-policy and PathBank
importer regressions. Final Ruff passed (`007b9b`, exit 0). The all-file scope and
whitespace audit passed (`8c708b`, exit 0). No full repository test suite or
candidate production snapshot is claimed by this external implementation.

`verify-originals.py` reads both authentic current PathBank exports, both Gene
XML originals, and all three relevant MetaCyc complex originals. All **14**
selected PathBank/Entrez/MetaCyc IDs and canonical labels match the stable author
target. This includes selecting SMP0000809 from the third Pathway object in its
four-Pathway export, without emitting the NAD, beta-alanine or TCA stubs as
canonical terms. All six compartment-scoped molecule objects and Transport505
are retained. Native aliases are intentionally preserved even though the author
proposal omitted alias lists. MetaCyc version normalization is explicit: native
`27.0`, with original bodies untouched. The historical PathBank archive member
still parses and now declares Transport505 as well.

The unchanged 222-record corpus selects **2,230** source authority terms. Its
in-memory rebuild exactly matches the current-corpus projection of the existing
authority terms and metadata, and it contains no Entrez IDs. The baseline also
retains 21 historical authority IDs that are not selected by those records.
`checks/current-corpus-projection.json` lists them explicitly. A second in-memory
run uses all existing authority IDs as an explicit selection to verify complete
preservation of the 2,251-term baseline. That selection has IDs only; its labels
still come exclusively from the issuing originals. The final reproduction
passed byte-for-byte with the existing snapshot SHA
`bb462c5cc88cce38a85a557b190c01a96b3a6b113f4d18333d360192714fea6a`
(session 72027, terminal `51d335`, exit 0). All 859 bound inputs were rehashed
unchanged at completion.

No output snapshot file is written by either original-source/baseline helper
run. The candidate's later whole canonical build, two new ontology authorities,
record integration, full gates and independent review remain root-owned work.

## Preserved attempts and source semantics

The first focused run passed 151 tests and failed one incomplete identifier-gate
fixture because it omitted the required taxa list. After adding that list, the
relevant run passed 575 tests and exposed that the same fixture also needed the
participants/reactions lists. These fixture defects, original code and complete
logs remain in `attempts/initial` and `attempts/second`. The corrected Gene suite
passed 96 tests, followed by the final 579-test relevant suite. Initial lint
findings were line lengths; their log and original files remain preserved.

The first baseline reproduction helper incorrectly expected the current-record
selection to include all historically retained authority terms. It failed with
exactly the 21 unselected historical IDs and no added/changed selected terms.
The failed helper and log remain in `attempts/baseline-selection`. Its successor
checks the exact current selection, then independently reproduces the full
retained-ID baseline; no production parser change was made for this harness
correction. An initial documentation patch was rejected atomically for a stale
context line and made no file change. It was applied successfully afterward.

Both authentic Gene XML originals omit Gene-track_status. The issuing NCBI DTD
read during preflight marks that field optional. The independently retained
[NCBI ASN specification](https://raw.githubusercontent.com/ncbi/ncbi-cxx-toolkit-public/main/src/objects/entrezgene/entrezgene.asn)
(`ebdce22e97e7aae562b6a769762ef8af0a53a1c1fc94a7e58d65bdc139e8d6da`) defines
live/secondary/discontinued as 0/1/2 and uses live as the schema default. The
implementation accepts the source omission but does not fabricate an observed
explicit status element. `ncbi-asn-acquisition.json` preserves its issuing URL,
HTTP 200 original body hash and acquisition metadata. Unsupported redirects and
deprecated records remain explicit failures rather than silent ID remapping.

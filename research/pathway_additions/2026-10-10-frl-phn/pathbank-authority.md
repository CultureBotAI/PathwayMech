# Native PathBank identifier authority

The first maintained PathBank target is `PathBank:SMP0002077`, **Methylphosphonate
Degradation I**. The authority input is the unchanged `PW002065.owl` member of the
public primary BioPAX archive. Its PathWhiz filename and SMPDB pathway accession
are distinct identifiers. The native pathway's linked SMPDB `UnificationXref`
and `http://identifiers.org/smpdb/SMP0002077` URI agree.

## Preserved source bytes

| Artifact | SHA-256 | Bytes |
| --- | --- | ---: |
| `pathbank_primary_biopax.zip` | `b3a9b9557d4147fac0159d178a27c13cc1180729eae9ccb4fb32abebb1656f44` | 27782843 |
| Unmodified member `PW002065.owl` | `66e835939e82188e3c976f0eda7ab68fa3d6fd8064bb18b1c4df439abec4cc62` | 45470 |

The archive URL is
[PathBank primary BioPAX](https://pathbank.org/downloads/pathbank_primary_biopax.zip).
The preserved acquisition receipt records retrieval on 2026-10-08 at
06:29:19 UTC and HTTP Last-Modified `2019-08-16 16:46:40 GMT`. The selected
member's ZIP timestamp is `2019-08-15 22:29:20` without a supplied timezone;
its ZIP CRC32 is `c843177f`. Neither date establishes identity with the current
public pathway page. The archive is retained at
`/private/tmp/pathwaymech-pathbank-dbcan-evidence/pathbank/pathbank_primary_biopax.zip`,
with its original `acquisition.json` and response headers alongside it.

The exact member was read with Python `zipfile.ZipFile.read('PW002065.owl')`
and written without XML serialization or text rewriting to:

```text
/private/tmp/pathwaymech-curation-authorities/sources/pathbank-PW002065.owl
```

Both archive and member digests were recomputed during this task. The member
bytes also match the independently extracted curation input. Existing 96-source
cache artifacts and their manifest provenance were preserved.

## Proposed source manifest entry

The integration task adds this entry to `conf/identifier_sources.json` and runs
the normal source snapshot builder. This receipt is not a manually patched
identifier snapshot.

```json
{
  "key": "PathBank-SMP0002077-PW002065-2019",
  "kind": "pathbank-biopax",
  "path": "pathbank-PW002065.owl",
  "url": "https://pathbank.org/downloads/pathbank_primary_biopax.zip",
  "version": "2019-08-16 primary BioPAX archive; member PW002065.owl; retrieved 2026-10-08",
  "license": "PathBank terms; archive-specific grant unresolved (public-release review deferred)",
  "sha256": "66e835939e82188e3c976f0eda7ab68fa3d6fd8064bb18b1c4df439abec4cc62",
  "sha256_scope": "Unmodified uncompressed PW002065.owl member bytes from pathbank_primary_biopax.zip, archive SHA-256 b3a9b9557d4147fac0159d178a27c13cc1180729eae9ccb4fb32abebb1656f44; not the compressed ZIP bytes or current pathway page."
}
```

The license field preserves uncertainty about this older artifact. It does not
assert an unrestricted grant or equate the archive with current PathBank data;
the source-specific distinctions remain in the existing
[terms assessment](../../source_discovery/2026-10-08-pathbank-dbcan-rights.md).
The user's authorized local curation continues while public-release licensing
is deferred.

## Extraction and policy boundary

`scripts/build_source_identifier_snapshot.py` adds the dedicated
`pathbank-biopax` kind and includes PathBank among the namespaces whose missing
selected identifiers stop the build. The parser reads flat native BioPAX typed
objects directly, independently of the maintained YAML and the pathway importer.

- Exactly one native `Pathway` and an unambiguous linked SMPDB unification
  accession are required. A PathWhiz-only source cannot establish an SMP ID.
- A native identifiers.org SMPDB URI must agree with the accession. Conflicting
  xref values/databases, duplicate normalized RDF subjects, dual `rdf:ID` and
  `rdf:about`, unsupported nested XML bases and ambiguous local identities fail.
- The pathway's native display/standard/name values supply its canonical label
  and synonyms. `PathBank:SMP0002077` resolves to **Methylphosphonate Degradation I**.
- Declared local reaction and physical-entity objects are scoped as
  `PathBank:SMP0002077/<native-local-id>`. Their native labels are retained as
  `source_context`; an unlabeled object retains its local ID as display text.
  Referenced-but-undeclared objects, xref metadata and external chemical/protein
  identifiers are not manufactured into native authority terms.
- Local graph existence does not prove membership, catalysis, composition or
  an external identity. Those claims still require edge-level review.
- `PathBank:SMP0002077/ProteinComplex/4049` resolves to the native
  **methylphosphonate degradation complex**. The planned record uses Rhea IDs
  for reactions, so the expected retained PathBank subset is these two IDs.

The raw member yields 24 native terms: one pathway, four reactions and 19
physical entities (11 chemicals, seven proteins and one complex). Extraction of
all 24 is a native inventory; the corpus selects only the IDs it actually uses.
No PathBank xref label becomes canonical ChEBI or UniProt authority evidence.

`conf/identifier_policy.yaml` supplies PathBank's source snapshot and narrow
contextual rules. Native PathBank participant/reaction descriptions are allowed
only in PathBank records; the pathway title remains canonical. Existing BioPAX
chemical display-name and UniProt protein-description rules now include
PathBank participant slots. Curated Rhea step labels are allowed in PathBank
reaction slots. Taxon labels and identifier existence are never waived.

## Verification

The synthetic parsing/gate regressions are independent test inputs, not
production authorities. They cover exact source labels; local RDF ID/about
normalization; PathWhiz-only refusal; conflicting or missing SMPDB identity;
URI disagreement; repeated subjects; unsupported local identities; undeclared
objects; scoped contextual labels; canonical-slot rejection; and failure to
replace an existing snapshot when a PathBank ID is unresolved.

```sh
.venv/bin/python -m pytest tests/test_pathbank_identifier_authority.py tests/test_source_identifier_snapshot.py tests/test_identifiers.py -q
.venv/bin/ruff check scripts/build_source_identifier_snapshot.py tests/test_pathbank_identifier_authority.py
git diff --check
```

The focused run passed **94 tests in 3.53 seconds**. Ruff and whitespace checks
also passed. Direct extraction of the preserved production member succeeded;
its bytes match the separately extracted curation input.

The complete baseline source snapshot was independently rebuilt with the new
code using the 96 manifest entries and maintained corpus from `d83a2f0`, the
preserved external cache, and an external output. All 1,572 terms, 88 selected
source provenance blocks and snapshot metadata were byte-value equivalent to
the existing parsed snapshot; no baseline term or provenance change resulted.
The reproducible comparison artifacts remain under
`/private/tmp/pathwaymech-pathbank-authority-regression/`.

The integration task must rebuild the final source snapshot after both records
are present, then run the identifier gate and full repository checks. This
parser receipt does not claim those final integrated gates have already run.

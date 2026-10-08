# PathBank local ingestion — 2026-10-08 UTC

One real microbial BioPAX export now produces a schema-valid local draft.
The original archive, selected XML and generated YAML remain outside the
repository at `/private/tmp/pathwaymech-pathbank-dbcan-evidence/pathbank`.
This is a source-based draft for local review, not a complete source graph or
an experimentally demonstrated whole-pathway mechanism. Data-release terms
remain recorded in the [prior rights assessment](2026-10-08-pathbank-dbcan-rights.md);
local processing proceeded under the user's explicit instruction to handle
public-release licensing later.

## Acquired source and exact native identity

The public [primary BioPAX archive](https://pathbank.org/downloads/pathbank_primary_biopax.zip)
returned HTTP 200 through ordinary `curl`, requiring no login, agreement or
access-control bypass. It contains 2,687 members and is 27,782,843 bytes.
The response's Last-Modified is 2019-08-16; this is archive metadata, not a
claim about the current website's release. Acquisition time, original-byte
hashes and measured counts are in the
[local ingest manifest](2026-10-08-pathbank-local/local-ingest-manifest.json).

The selected member is `PW000967.owl`, 74,091 bytes. It contains one Pathway
with native URI `http://identifiers.org/smpdb/SMP0000983`, the SMPDB accession
`SMP0000983`, and the distinct PathWhiz accession `PW000967`. Its named pathway
is [Secondary Metabolites: Glyoxylate Cycle](https://pathbank.org/view/SMP0000983)
for *Escherichia coli*. The BioSource uses database `TAXONOMY`, identifier
`562`, and `displayName`; the draft preserves `NCBITaxon:562` and that label.
The ZIP member's PW filename is not rewritten into an SMP accession. No claim
is made that these 2019 bytes match the current public-page contents.

## Importer corrections exercised by the real file

The original importer stopped before emitting output because five source
reactions spell the direction `LEFT_TO_RIGHT`; two other reactions use
`REVERSIBLE`. PathBank imports now normalize the two recognized underscored
direction values while retaining the original spelling in structured evidence.
Other source adapters keep their strict BioPAX direction rules.

The importer now selects the attached native SMPDB pathway accession and
checks agreement with an identifiers.org SMPDB URI. It keeps PathWhiz identity
separate and rejects files containing multiple Pathway objects rather than
silently combining their graphs. PathBank's `TAXONOMY` alias and BioSource
`displayName` are recognized.
Independent review [#300](https://github.com/CultureBotAI/PathwayMech/issues/300)
also required unambiguous taxon xrefs and explicit reaction membership through
the pathway's components or attached steps. Orphan reactions are refused, and
unattached steps cannot supply or change a reaction's contextual direction.
These safeguards preserve the real canary unchanged; independent re-review
found no remaining actionable issue.

The real source also showed that inspecting only the first entity-reference
xref loses valid chemical mappings: all 15 SmallMoleculeReference objects have
a ChEBI xref, but only three list it first. Entity-reference selection now
inspects all direct xrefs, prefers ChEBI for small molecules and UniProtKB for
proteins, and rejects conflicting supported accessions. Source labels remain
unchanged. These are source-supplied mappings; authority, currency and chemical
identity have not yet been independently approved for maintained records.

## Measured coverage and omissions

The source contains seven BiochemicalReaction and seven Catalysis objects.
The local draft contains seven reactions, 27 participants and 43 structured
evidence edges: 13 consumes, 15 produces, seven catalyzes and eight has_part.
These exactly match the source's 13 left-side links, 15 right-side links,
seven catalytic controllers and eight complex-component links. Participants
comprise 14 source-mapped ChEBI entities, seven UniProtKB entities and six
source-native complexes. Catalysis remains attached to the specified physical
assembly; subunits are not independently promoted into catalysts.

The source's 19 Stoichiometry objects contain coefficients 1, 2, 4 and 6.
Those coefficients are not represented by the current edge model. Eight
BiochemicalPathwayStep objects and one PathwayStep provide source membership,
but there are no nextStep links; no physiological ordering is inferred.
One MolecularInteraction, `Interactions/33`, names an inhibitory relationship
between hydroxypropanedioic acid and isocitrate lyase. That interaction and its
otherwise unused chemical participant are omitted, so the draft is not a
complete rendering of the source graph. Its interaction name alone is not
converted into an experimentally supported inhibitory edge.

There are no PublicationXref objects in this file. The draft's single reference
is the pinned source pathway, and its evidence consists of structured BioPAX
assertions with native locators. No paper quotation or experimental claim is
invented from the current pathway's narrative bibliography.

## Reproduce the local draft

Check the ZIP against SHA-256
`b3a9b9557d4147fac0159d178a27c13cc1180729eae9ccb4fb32abebb1656f44`,
extract exactly `PW000967.owl`, then run from the repository root:

```bash
.venv/bin/python scripts/import_biopax.py PathBank /path/to/PW000967.owl \
  --sha256 1a037aaf80b3cc99f6e6a2c45d60cebea0909cd7b5ee7c15e4f2acf885a8b611 \
  --source-url https://pathbank.org/downloads/pathbank_primary_biopax.zip \
  --source-version 'primary archive Last-Modified 2019-08-16; member PW000967.owl' \
  > /path/to/local/SMP0000983-draft.yaml
```

The command succeeded and validates the closed draft schema. The independent
identifier authority gate was not run against this external draft. The final
focused BioPAX, PathBank and local CLI suite passed 77 tests, along with Ruff.
No source file or draft was added to `data/pathways` or published
as a maintained record.

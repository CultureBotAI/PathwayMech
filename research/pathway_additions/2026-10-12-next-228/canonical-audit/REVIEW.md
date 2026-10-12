# Independent MG canonical-output audit

**Accepted, no canonical-output findings.** This audit covers the actual native
source and ontology outputs, their selected original sources, source metadata,
manifest/Rhea selector changes, closed consumers, and root's post-build recovery.
It does not replace the separate independent scientific review of the record.
The reviewer authored the MG preflight and first scientific draft, but did not
execute or implement this native canonical build; this acceptance is confined to
an independently replayed canonical identity/provenance audit.

The accepted target is SHA256
`b73c407b4315efc45a30ed7121cb3797945cf0a4e86ab010bf5554b276b0e0a6`.
The accepted source output is
`811ebc7681c60a8a82ce9a50f10bef32a7d4f34b9b25eeb8803f1d6f38c5631c`,
and ontology output is
`5c67851f07d6c35ba75fa0e7455367dc634ed7bc751a6f2d71797066b43267ab`.
Actual counts remain **2433 source terms/575 metadata and1951 ontology terms/5
metadata**. The captured baseline is the real accepted228-record lyxose worktree
on ribose commit6435622/tree428c9; it is not described as a committed or merged
lyxose baseline. The staged corpus has229 records including MG.

## All additions and their sources

Every one of the21 new source terms was independently extracted from issuing
identity/name fields and compared as a complete object, then replayed through the
actual production parser. `all-21-source-assessments.json` retains the exact
original binding, manifest row, native facts and comparison for each:

- Nine UniProt proteins: P0A8M6, P0A9A9, P0AA04, P0ACF8, P13669, P23524, P37047,
  P54745 andP54746. Primary accession, taxon83333 and all native label/synonym
  fields match both the selected earlier bulk body and nine later individual
  originals. The actual first-source provenance and unused fresh metadata
  decisions are unchanged from the separately sealed diagnosis. Fresh scientific
  originals remain available and are not equated to the bulk release.
- Five NCBI Gene records:944860/cdaR/b0162,945355/mngA/b0731,945359/mngB/b0732,
  945371/mngR/b0730 and947632/garK/b3124. Exact gene IDs, native locus symbols,
  locus tags, synonyms, formal symbols and taxon511145 match. Native status
  omission remains an omission, not an invented explicit live assertion.
- EcoCyc PC00103 andCPLX0-7639: exact top-level ECOLI complex identities,
  PGDB27.0/MG1655 metadata, parent classes, names and synonyms match. The originals
  retain the MngR dimer and Fur/Fe2+ component coefficients; this identity audit
  does not invent additional assembly biology from compact labels.
- MetaCyc PWY0-1300, MANNCAT-PWY andCOLANSYN-PWY: exact native META frame and
  HTML title pairs match. Separate retained exact-frame XMLs independently show
  MetaCyc PGDB27.0. The HTML footer's Pathway Tools software version was not used
  alone to infer a database release (`metacyc-release-joins.json`).
- MetaCyc RXN0-5216: the full native reaction is preserved as a typed
  `source_context` identity, with no direct common-name. The nested enzyme name
  is not substituted for a reaction name. Native left/right slots retain the
  CPD-15979 class=true assertion without converting it to a resolved anomer.
- PathBank SMP0000839: the complete original ZIP/member hashes, native root and
  child SMPDB identities, root-owned Interaction bridge and adjacent empty child
  stub match. The child title is an issuing identity assertion. Its marker does
  not establish biological inhibition or an expanded child pathway mechanism.
  The original member is retained as `native-PW002096.owl` for exact replay.

A bounded source build using22 actual originals and only the21 new IDs exactly
reproduces all21 terms and their13 selected source metadata objects (12 new plus
the existing selected bulk source). No authored label seeds the extraction.
The root's21 appended manifest entries and unchanged first717 entries are exact.

All six new ontology objects are individually assessed in
`all-6-ontology-assessments.json`. Indexed read-only SQL queries reproduce all
labels and exact synonyms for CHEBI:16537,57541,58735,60331 and60332. Generic
D-mannopyranose6-phosphate and its alpha-specific form remain distinct exact
identities. The complete Rhea142 gzip original was freshly hashed, the actual
production selector parser reproduced all20 selected equations, and independent
streaming extraction verified RHEA:33308's unique approved directional identity,
label/equation, transport assertion, and substrate/product references. Its donor
is protein phosphohistidine; its equation is not rewritten as an overall PEP
shortcut. The prior19 selectors are unchanged and33308 is the only addition.

All four SQL sources were reopened read-only to inspect their native versionIRI,
versionInfo, license and prefix declarations. Exact source keys and metadata
match. Fresh size/mtime checks match the pinned originals; full database hashes
are inherited from the exact successful native builder command, not represented
as freshly recomputed multi-gigabyte hashes by this audit.

## Preservation, recovery, and adversarial checks

All2412 old source terms/563 metadata and1945 old ontology terms/5 metadata are
object-identical. Both actual builder receipts, exact commands/environment and
complete output logs are verified as successful. The root recovery handoff
`ba16915d…` and all477 bound build artifacts are freshly verified. Its concrete
script is read in full and its738-original rehash receipt is accepted with that
explicit scope. This audit freshly hashes the22 source originals used here, the
full Rhea gzip, and the three exact-frame XML release companions; it does not
claim to freshly rehash every unrelated old source or rerun full SQL builds.

The exact ten term/nine metadata proposal differences remain accepted under
`mg-canonical-proposal-selection-expectation`, inherited from the sealed prior
diagnosis. The reference-only PathBank root remains legitimately unselected from
the compact named-node authority, while root/child/archive provenance is retained
by the declared child. No extra identity, selector, source reorder or label edit
was introduced to force the original proposal counts.

The actual target passes record-schema and identifier-consumer validation using
external copies of the exact actual snapshots. Thirteen controls pass across
`negative-controls.json` and `supplemental-negative-controls.json`: wrong NCBI
request identity, EcoCyc version mismatch, unsupported reaction class=false,
PathBank member hash mismatch, unselected Rhea update, exact-source alpha/generic
object drift, missing alpha-specific chemical identity, missing gene metadata,
missing typed reaction provenance, missing Rhea identity, detached PathBank child,
child URI/xref disagreement and obsolete Rhea status. Consumer snapshots are
restored byte-for-byte and pass again.

The MetaCyc/CHEBI participant label policy permits contextual display labels.
Consequently, the anomer label-drift test uses the independently queried native
object equality rather than claiming the identifier consumer enforces such
labels. An initial negative control exposed this expected policy exception and
is retained with its correction. Two other local audit harness failures (handoff
manifest-key assumption and absolute-IRI bracket normalization) are retained and
explained; none was hidden or reclassified as a canonical output defect.

Final `audit.py` exited0; `audit-execution.json` binds its exact code and streams.
`supplement.py` exited0 (toolc75f25/0), with three additional identity controls and
three XML release joins. Initial broad source output was truncated; this report
claims complete machine parsing and exact selected-field reads, not a human
reading of every unrelated paragraph in the expanded EcoCyc bodies. No full
scientific literature rereview is claimed.

No maintained/source-cache/Git/build/preparation mutation occurred. Source
exhaustion remains false. Maintained integration and its gates remain root-owned.

# Glutaryl-CoA degradation

This increment adds `MetaCyc:PWY-5177`, glutaryl-CoA degradation, after the
265-record baseline at `7dcc4e6586a7c2b8a9c0a3d733e0399e7ba68105`.
The curated record is
[`glutaryl-coa-degradation.yaml`](../../../data/pathways/glutaryl-coa-degradation.yaml).
It retains five native pathway members and their order, plus an auxiliary
composite reaction that is not a sixth member.

The record has eight microbial taxa, 53 participants, six reactions, 80 edges
and 59 references. The source diagram contains 60 native biochemical nodes;
the component tables and KGX include all 68 declarations. The graph preserves
20 pathway material occurrences, six composite material occurrences, integer
coefficients and source direction. Composite GcdH catalyst annotations are not
transferred to the two isolated half-reactions. Eight inhibition assertions
target four exact enzyme-specific activities, with four enzyme enables links.

## Evidence and prior research

[Accepted preparation](accepted-preparation/README.md) preserves sixteen frozen
source, design, diagnostic and review packets. Its
[inventory](accepted-preparation/inventory.json) binds every archive member to
the original file bytes, including hidden and ignored files. Historical findings
and failed attempts remain separate from corrected successor observations.
All archives were decoded and checked after packing.

The complete native pathway original was already retained in next266 research;
this is a new maintained record using that source, not a claim to have newly
discovered the source. Existing benzoyl-CoA II/III records explicitly end before
this route. The earlier YeastPathways PWY-5177 GO-CAM lead omits the defining
glutaryl-CoA steps and remains insufficient by itself. Duplicate searches include
hidden and ignored files and first-level compressed text; unread binary and
nested-container interiors do not support a global absence claim.

The primary evidence includes the 2009 decarboxylating/nondecarboxylating GcdH
study (PMID:19395484) and the 2018 KT2440 glutarate-catabolism study
(PMID:29844506). Their experimental scope remains narrower than the source
graph: artificial ferrocenium acceptor and distinct protein preparations;
condition-specific growth and expression; larger complementing inserts; and
purified CsiD/LhgO assays for an alternative route. These do not establish all
five native members, physiological ETF coupling or whole-route flux in every
associated taxon. The 1993 article is represented by an inspected publisher
abstract/preview; its full main was not acquired.

## Preserved qualifications

All nine direct native taxon associations are accounted for: eight microbial
declarations and an explicitly excluded human context. K172 remains at issuing
strain rank, separate from Thauera aromatica species. KB740 is reconciled only
to Aromatoleum evansii species/type material. These are source pathway
associations, not complete-route experimental demonstrations.

RXN-11667 keeps its canonical dehydrogenase label while visible prose states
the actual hydration equation and naming conflict. Taxon and hydration scope
also appear in incident-edge descriptions/evidence because current KGX does
not export the root description. No unsupported NamedNode fields or invented
taxon edges are used.

Generic ETF prevents a complete elemental-balance or physiological-partner
claim. Native ionic identities remain distinct from differing KEGG forms;
normalized ChEBI agreement does not supply unencoded CML stereochemistry.
Located sodium transport in an external Rhea reaction is not added to the native
equation. Opposing thiolase directions, the selenium annotation conflict and
native strain/gene/sequence discrepancies remain explicit.

The authentic 2010 supplement (DOI:10.1021/bi100317m.s001) contains primer and
sequence information, not kinetic reconciliation. Its full main remains
unacquired. IP08's UniProt/paper kinetic discrepancy remains unresolved; no
global numerical correction is asserted. Source-only catalyst, cofactor and
regulation annotations are not promoted to independently verified experiments.

Issues [623](https://github.com/CultureBotAI/PathwayMech/issues/623) and
[624](https://github.com/CultureBotAI/PathwayMech/issues/624) preserve the original
direct-taxon and canonical-label findings. Their accepted design corrections
are separate successor packets. Closure requires corrected maintained content
and verification of its actual merged tree.

## Record and implementation review

[Integration preparation](integration-preparation/README.md) preserves the
authority implementation, original record and actual merged-baseline rebind.
[Review preparation](review-preparation/README.md) retains the independent
authority and original record reviews, the root URL correction and its
independent acceptance. The original record remains historical; the maintained
record uses the accepted URL-only successor.

[Issue 625](https://github.com/CultureBotAI/PathwayMech/issues/625) records
46 native reference links copied from an unsuitable XML base. Each navigable
link now matches an actual successful acquisition receipt. Native XML, its
literal base, body hashes and all scientific content are unchanged. One
representative live HTTP/HTTPS pair was tested; the other replacements use
retained acquisition receipts, not 46 new requests.

The [reference retention ledger](reference-original-retention.json) accounts
for 51 archived reference bodies and eight taxonomy references to the external
pinned full SQLite database. Complete selected taxonomy statements and whole
database verification receipts are retained; the 14 GB database is external.
The [identifier increment](record-identifier-increment.json) enumerates all
68 declarations, including 52 new to this maintained corpus.

## Maintained review and checks

[Authority integration review](integration-review/README.md) verifies the reviewed implementation, documentation and exact source XML bytes. [Maintained scientific review](maintained-record-review/README.md) binds the actual record, page and export, including the bounded structured-source cross-check. [Supporting integration review](supporting-integration-review/README.md) checks reference retention, identifier accounting, immutable histories and preservation of existing records and graph contexts. Each review retains its authorship disclosures and limits.

The full test suite completed with `6827 passed, 3 skipped, 7 warnings in 1287.86s (0:21:27)`. `just render-pages`, `just validate`, `just lint`, `just vendored-check`, `git diff --check` and the complete staged diff check also passed. [Terminal check receipts](final-verification/gates.json) retain exact commands, results and raw log hashes. Passing checks do not remove the scientific limitations documented above.

Immutable canonical observations use the [structured review archive](../../../reviews/structured/). Preparation reviews, canonical assessments and actual merged-tree verification remain distinct evidence.

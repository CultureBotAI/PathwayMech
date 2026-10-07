# BRENDA Entner-Doudoroff export canary

Checked: **2026-10-07 UTC**. This bounded follow-up to the
[October 3 discovery scan](2026-10-03-additional-sources-and-updates.md#brenda)
demonstrated a real public pathway export. It did **not** implement an importer
or adopt a maintained pathway record. BRENDA remains disabled with
`ingest_status: next`; only its inventory note changed.

## What now works

The [Entner-Doudoroff page](https://brenda-enzymes.org/pathway.php?pathway=Entner+Doudoroff+pathway)
has web ID `pw_Entner-Doudoroff-pathway` and directly links downloadable
[enzyme](https://brenda-enzymes.org/pathways/php/pathway_download.php?type=enzymes&pathway=Entner+Doudoroff+pathway)
and [compound](https://brenda-enzymes.org/pathways/php/pathway_download.php?type=compounds&pathway=Entner+Doudoroff+pathway)
CSVs. Its [SPARQL prototype](https://sparql.dsmz.de/brenda/) documents backend
`https://sparql.dsmz.de/api/brenda`, which accepted bounded GET queries with
`Accept: application/sparql-results+json`.

| Observed artifact | Result |
| --- | --- |
| Enzyme CSV | 22 rows; EC number and recommended name |
| Compound CSV | 23 rows; native CompoundID, formula, InChI and InChIKey |
| RDF pathway `https://purl.dsmz.de/brenda/pathway/76` | 15 reactions; 21 distinct EC classes |
| RDF reaction-side projection | 62 substrate/product rows; 28 compound identities |
| Linked SVG | 38,548 bytes; native IDs appear in node classes, but connecting paths use coordinates |

The [acquisition manifest](2026-10-07-brenda-canary/acquisition-manifest.json)
preserves exact query/export URLs, retrieval timestamps, response byte counts,
SHA256 hashes and query hashes. Seven small original responses are retained
alongside all query texts; other successful requests retain acquisition
metadata, and failed requests have no invented content hash. The retained
response hashes were verified against the retained bytes.

The [native canary](2026-10-07-brenda-canary/two-reaction-native-canary.json)
contains six source-backed role assertions for reactions `reaction/I/3385`
and `reaction/I/345`: phosphogluconate dehydration and KDPG cleavage, using
five compound identities. This is an inspectable evidence fixture, not a
PathwayMech record. The [complete role response](2026-10-07-brenda-canary/roles.json)
allows every selected assertion to be checked independently.

## Remaining semantic and identifier gaps

**Assertion-specific enzyme context is missing from the inspected projection.**
Reaction `I/345` links to `enzyme/16699`. The
[direct subject query](2026-10-07-brenda-canary/suspect-enzyme.rq) asks only
`<enzyme/16699> ?predicate ?object`, with no EC/organism/reference joins. Its
[complete response](2026-10-07-brenda-canary/suspect-enzyme.json) contains
455 distinct triples: 171 EC classifications, 12 organism links, 269 reference
links and three type triples. There is no `hasIdentifier` triple on that
subject. These are exact direct triples, not counts inflated by a Cartesian
join. They do not identify which organism and reference support a particular
EC/reaction assertion. A downstream multivalue join would invent combinations;
production curation must first establish that context. This is a limitation of
the inspected representation, not a confirmed defect in the provider's source
curation.

**Web and RDF contents need reconciliation.** The
[inspection summary](2026-10-07-brenda-canary/inspection.json) enumerates four
CSV-only and three RDF-only EC classes. The different compound populations may
reflect map display, reaction content, or snapshots; the cause was not
established. The website advertises release 2026.1, but the
[RDF pathway metadata](2026-10-07-brenda-canary/pathway-metadata.json) provides no
release identifier. Do not assign that website version to the RDF snapshot.

**Native identifiers are not interchangeable.** CSV `CompoundID` values join
RDF structure/ligand identities rather than matching RDF compound-group
numbers. For example, CSV `8212` is `structure/8212`, linked from
`compound/1101` for KDPG. The
[exact selected source triples](2026-10-07-brenda-canary/compound-identity-example.json)
preserve that relationship and the original acquisition hash. EC strings can
map to `EC:`; nonempty verified taxon and PMID values can map to their respective
namespaces. No UniProt identity was established for the inspected enzyme.
Compound grounding needs checked structure mappings; four generic
acceptor/ferredoxin compounds have no nonempty InChIKey. Native BRENDA pathway,
reaction and compound identifiers also need explicit authority-resolution
support: the current local schema does not allow a `BRENDA` CURIE prefix.

**Reaction sides are not a complete pathway-direction model.** Role URIs are
reused across reactions, so provenance must retain the reaction + role +
compound tuple. IUBMB substrate/product orientation is recoverable; the
inspected projections do not establish pathway-specific physiological
orientation, reversibility or stoichiometric coefficients. The canary adds no
precedence, taxon, catalyst, stoichiometry or irreversibility assertions.

## Access, attribution and next step

The [current BRENDA license](https://brenda-enzymes.org/license.php) states
CC BY 4.0 and requests citation of
[BRENDA 2026](https://doi.org/10.1093/nar/gkaf1113), PMID 41206471. The bulk-download
page separately requires active license acceptance. This pilot used only
public documentation, a single pathway's small linked exports and bounded
SPARQL results; no bulk archive, account action or acceptance submission was
used.

The broad enzyme/taxon/reference query returned HTTP 500. A subsequent
23-enzyme subject projection reached its 3,000-row limit and is explicitly
marked truncated in the manifest. The decisive single-enzyme query completed
at 455 rows, below its 1,000-row limit. No absence claim or complete count uses
the truncated result. The [SBML entry page](https://brenda-enzymes.org/search_result.php?a=200)
was inspected as organism/reaction-oriented documentation; a pathway-specific
SBML export was not demonstrated.

Next, resolve one reaction–enzyme–organism–reference assertion using a scoped
official response or primary enzyme page, reconcile web/RDF identifiers, and
verify direction semantics. If that assertion cannot be recovered, retain
BRENDA components as grounding leads and curate a small route from independent
primary evidence. Enzyme-centric bulk JSON should not substitute for verified
pathway topology and context.

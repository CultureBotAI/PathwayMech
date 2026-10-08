# PathBank and bounded dbCAN-PUL license recheck

Assessed 2026-10-08 UTC against PathwayMech `f81b916`.

## PathBank decision

Keep the implemented BioPAX adapter as an enabled **fixture**. Do not promote
current PathBank data into the permissively redistributed pathway corpus.
The [PathBank 2.0 primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767802/)
(DOI `10.1093/nar/gkad1041`, PMID `37962386`), **Data availability**, explicitly
assigns the database data to CC BY-NC 4.0. This is a data-specific statement,
not an inference from the article's separately printed CC BY-NC license.
The [current homepage](https://pathbank.org/) also requires permission for
commercial use or redistribution of data. Thus the current-version blocker
is more specific than the earlier report's unresolved redistribution question.
The [About page](https://pathbank.org/about/) still states ODbL alongside its
commercial-permission reservation. Treat this as conflicting/stale wording,
not as an affirmative unrestricted grant for the current version or a basis
for relicensing older snapshots.

Suggested inventory note: "Local BioPAX/SBML fixtures; PathBank 2.0 data are
CC BY-NC 4.0 and current commercial redistribution requires permission."

## Bounded public-page canary

[PathBank:SMP0000983](https://pathbank.org/view/SMP0000983),
**Secondary Metabolites: Glyoxylate Cycle**, is reported for *Escherichia coli*.
The public indexed source page reports created `2015-07-03`, updated
`2026-07-30`, and references including PMIDs `2512996` and `6389540`.
This establishes an in-scope named candidate only. No export was obtained,
no strain taxon or protein/reaction IDs were independently verified, and no
reaction topology or evidence quotation was ingested. The narrative references
do not automatically establish experimental support for every database edge.

The [download catalog](https://pathbank.org/downloads) still advertises
BioPAX, SBGN, SBML, PWML, RXN, CSV and sequence archives generated in 2019,
with primary-pathway images dated 2020. The primary BioPAX archive lists
2,687 files/26.5 MB; its catalog date is 2019-08-16. These dates establish the
advertised archive metadata only, not its byte identity or equivalence to the
2026 public page. No archive was fetched.

## Retrieval evidence and limits

Assessment used official pages through the web tool and the primary PMC
article. The official About page and candidate were available as indexed
primary-source search results, but direct page opens timed out. Direct
Python GETs to the PathBank homepage, About, Downloads and Browse endpoints
returned HTTP 403. Those failures are recorded in the accompanying
[retrieval manifest](2026-10-08-pathbank-dbcan-rights/pathbank_manifest.json);
no file hashes are invented for inaccessible bytes. No account was created,
no agreement accepted, no request sent to a person, and no bulk data acquired.
The paper, homepage and download catalog were successfully read through the
web tool; [assessment metadata](2026-10-08-pathbank-dbcan-rights/assessment_metadata.json)
identifies these surfaces and outcomes.

## dbCAN-PUL limited rights/update check

This secondary check did not find a new explicit data-redistribution license
on the inspected official Home, About, Help, download index or README pages.
That is a bounded-page finding, not a claim that no license exists anywhere.
The [Home page](https://pro.unl.edu/dbCAN_PUL/dbCAN_PUL/home) and
[download README](https://pro.unl.edu/static/DBCAN-PUL/README.txt) describe
633 loci based on February 2025 searches, including removal of repeated and
capsule-synthesis entries and splitting PUL0460. The
[download index](https://pro.unl.edu/static/DBCAN-PUL/) lists the February
2025 workbook and a change log dated May 2026. No workbook or locus bundle
was downloaded during this check. Do not infer a data release date merely
from filesystem modification times.

The [dbCAN-PUL paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC7778981/)
(DOI `10.1093/nar/gkaa742`, PMID `32941621`) has an article CC BY-NC license;
that alone does not grant a license to the separately hosted database.
Likewise, the [linked run_dbcan software repository](https://github.com/linnabrown/run_dbcan)
is GPL-3.0, but its software license was not established to govern dbCAN-PUL's
external database files. Keep `dbcan-pul` enabled with `license-gated` status.
The source remains useful for primary-paper discovery and local authorized
support parsing, without treating a characterized gene locus as an ordered
small-molecule pathway graph.

## Local audit scope

Existing notes, inventory and fixtures were searched with
`rg --no-ignore --hidden` over `research`, `docs`, `conf`, `tests/fixtures`,
and `.claude/skills`, including ignored files within those explicit roots.
No absence claim was made about other filesystem roots or private credentials.
The inventory note now states the PathBank data restriction; neither source
is promoted and no source export is ingested by this rights assessment.

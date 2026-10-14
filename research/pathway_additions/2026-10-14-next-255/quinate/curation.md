# Quinate degradation I curation

## Pathway scope

The maintained record is `MetaCyc:QUINATEDEG-PWY`, quinate degradation I:
`data/pathways/quinate-degradation-i.yaml`. It preserves the complete three-step
MetaCyc 27.0 boundary from L-quinate to protocatechuate. Organism and enzyme
claims retain their individual evidence scopes for Acinetobacter baylyi ADP1
and Gluconobacter oxydans, including IFO3244 preparations. This is not a claim
of purified three-enzyme reconstitution in one strain.

GO:0019631 is broader: the pinned GO source explicitly narrow-matches both
quinate I and II. The exact native pathway ID therefore remains the record ID.
The preflight read all 251 baseline records from their actual Git blobs and
searched both current roots with ignored and hidden files included. Its 501
distinct patterns, bounded search exclusions, prior research, incidental
matches and shared-reaction dispositions are retained under `preflight/`.

## Mechanistic summary

The initial oxidation uses `MetaCyc:1.1.99.25-RXN`, retaining the native broad
quinone and quinol classes. Native class representatives do not prove identity
to the narrower Rhea 1,4-benzoquinone/hydroquinone classes or acceptance of every
class member. PQQ (`CHEBI:58442`) is a separate protein cofactor. The middle
reaction uses reversible `RHEA:21099`, with forward catabolic pathway ordering;
the final dehydration uses `RHEA:24849`.

The record has 37 evidence-bearing edges, including six enzyme assignments,
native complex composition, source organism contexts and qualified cofactor and
location claims. The 51-object native biological neighborhood was dispositioned
individually: 23 activities, 21 proteins/subunits and seven regulations. Shared
biosynthetic enzymes, alternate NAD(P) routes and petrobactin context are not
silently treated as quinate I components.

Six concrete chemical structures were compared across native MetaCyc 27.0,
current ChEBI and pinned ChEBI 255; all full InChI, charge and formula checks
passed. The three Rhea comparison equations balance. Exact results, source
hashes and helpers are in `chemistry/`.

## Evidence table

| Claim | Inspected support | Retained limit |
| --- | --- | --- |
| Complete three-step route and ordering | Complete native META27 pathway/reaction XML | Downstream protocatechuate degradation and superpathways lie outside this boundary |
| ADP1 QuiA, QuiB and QuiC roles | Native activity joins; 1994 primary scans and 1995 full author-rendered text | Old QuiB start annotation and recombinant QuiC assay material are distinguished |
| IFO3244 DHS dehydration | 2003 primary fractionation and qualitative product assay | Partially purified fraction; no sequence or homogeneous protein inferred |
| IFO3244 membrane-associated DQD | 2008 full text and decisive figures | Dodecamer suggested by mass comparison; precise periplasmic topology remains inference |
| IFO3244 QDH and PQQ | Native annotations and 2004 primary abstract | Full 2004 body and acceptor panel unread; processing state unresolved |

## Gaps

The native narrative overgeneralizes type-I DHQase function; catabolic QuiB is
retained with the primary evidence instead. Native QuiC activity naming and
units, DQD mass, and inferred localization are not copied uncritically.
Q5FTS6 is from strain 621H and is not asserted to be the full IFO3244 protein.
The 1995 figure images and the 1988/2004 full bodies were unavailable; the
primary reading ledger states the exact access bounds.

Independent review corrected an author-session attribution of the 2003
purification experiments: SA1 and AC3 are Acinetobacter, distinct from ADP1 and
Gluconobacter IFO3244. [Issue #540](https://github.com/CultureBotAI/PathwayMech/issues/540)
tracks that provenance correction. No erroneous maintained pathway record had
been written when it was identified. The final ledgers explicitly name both
Acinetobacter preparations and the graph does not import their assay results
as direct measurements of another strain.

Shikimate I, quinate II and shikimate II remain real candidates. New engineered
secretion and extracellular protocatechuate leads remain research leads, not
native enzyme evidence. No source-exhaustion claim is made.

## Candidate YAML

The authoritative YAML is `data/pathways/quinate-degradation-i.yaml`; its
generated page and KGX exports are committed with it. All 4,891 prior authority
terms and 821 owners are preserved. Sixteen new terms produce 4,907 total terms;
the 997-entry manifest prefix is unchanged within the new 1,008-entry manifest.
Both production builders are unchanged and reproducible from bound originals.
Raw papers, figures, XML, HTML, JSON API responses and SQL/RDF snapshots remain
outside the repository. Retention manifests bind compact artifacts to their
exact external originals. Validation and independent review results are saved
separately and are not implied by these author assessments.

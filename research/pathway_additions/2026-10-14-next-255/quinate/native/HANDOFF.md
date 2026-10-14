# Quinate degradation I native source author handoff

This is author support, not a scientific approval. No maintained files were edited.

The freshly acquired native MetaCyc 27.0 pathway XML exactly matches the retained
next251 original SHA256 `51d1f25faf0545dfdf14baf69f8f3647ab33ed564ef4e6117146c06f98e5153b`.
It defines three selected L2R steps. The shared DHQ dehydration reaction is natively
reversible; selected physiological route orientation does not change that fact.

The biological coverage ledger has 51 exact source objects: 16 pathway-reaction
activities, 16 enzymes, 5 recursive complex subunits, 7 regulator objects, and
7 auxiliary activities of the inspected proteins. Thirteen objects are proposed
for retention with scope and 38 excluded with individual reasons. This is a
bounded source-neighborhood denominator, not a claim to have enumerated every
enzyme in nature. Four gene XML originals and two localization originals provide
additional identity/context support. Raw payloads stay in `originals/` outside
the repository.

Retain the compact `biological-coverage.json`, `biological-coverage-replay.json`,
`biological-edge-proposal.json`, `biological-node-identities.json`, acquisition
receipts, `original-bindings.json`, this handoff, and helpers as `.py.txt` if useful.
The larger `source-projection.json` is an external working projection; do not
confuse it with an authority export or independently reviewed final record.

## Source defects and limits requiring final primary reconciliation

- `ENZRXN-29`/ADP1 QuiA links PMID14586098 purification experiments from SA1/AC3,
  not ADP1. Do not transfer assay conditions or purification to ADP1. Independently
  retrieved UniProt Q59086 supports its PQQ role and curated membrane context.
- QuiB Q59087 is currently 272 residues with explicit erroneous extended-start
  cautions for AAC37158.1 and CAG68555.1. The old native leader-to-membrane inference
  is not retained. Broad native prose that type-I DHQases are only biosynthetic
  conflicts with its own catabolic QuiB account and must not be repeated.
- `MONOMER-37` QuiC prose says DHQ rather than DHS activity and has suspect mmol
  units. Its exact enzyme-activity/reaction joins say DHS, and the primary agent
  is inspecting the original assay. UniProt Q43922 is separately verified.
- `MONOMER-0` is a protein-complex object despite its name. It contains twelve
  `MONOMER-15328` subunits. The source's Q5FTS6 cross-reference is strain 621H;
  the native purification was IFO3244 and only a short N-terminal match was
  established. Retain native identifiers and qualify the measured processing;
  do not replace the assayed molecule with the entire 621H sequence.
- `MONOMER-67` is the native IFO3244 QDH preparation with 108-kDa native mass
  and 65/21-kDa SDS bands suggested to be proteolysis. Do not invent a heteromer
  or sequence-equivalent intact construct. Its PQQ and detergent context require
  the primary source's bounded qualification.
- `MONOMER-1` represents partially purified G. oxydans cytoplasmic DHS activity,
  not a sequenced, homogeneous protein. Fraction evidence is not exclusive
  localization of every instance.
- The Gram-positive/fungal NAD-dependent route, unrelated biosynthetic enzymes,
  and petrobactin AsbF remain explicitly excluded. A. methanolica's dual-use
  enzyme is a useful alternate-variant lead, not evidence of PQQ initiation.
- Root owns the quinone/quinol class correspondence decision. Do not assume
  native broad `Quinones`/`Reduced-Quinones` are exact matches to the narrower
  Rhea 23672 family participants without that review.

## Naming authorities

The current bounded protein XML adapter does not name unnamed polypeptides from
their sole activity. Existing native HTML parsing succeeds without code changes
for `MONOMER-1` and `MONOMER-67`; their raw pages and exact parsed identity/title
bindings are recorded in `html-name-acceptance.json`. `MONOMER-37` HTML returned
an interstitial without native identity, explicitly rejected; use the separately
verified UniProt Q43922 name. Named native complex `MONOMER-0` and subunit
`MONOMER-15328` have direct XML names. The QUINATEDEG-PWY HTML object page also
resolved its exact pathway identity and title (even though the request used
the generic ENZYME page type); canonical PATHWAY retrieval is optional for the
final authority manifest, and the actual request remains recorded honestly.

An initial direct websvc.biocyc.org request failed first under restricted DNS
and then with connection reset after network escalation; it yielded no source
payload. Successful acquisitions use the existing public MetaCyc 27.0 mirror.

# Galactitol degradation: deferred chemical identity preflight

`MetaCyc:GALACTITOLCAT-PWY` remains a candidate for a complete pathway record.
This dossier records a stereochemical conflict in its substrate/product mapping.
No pathway YAML or identifier authority is added. The baseline is
`ca9a6940b8ebc125c858e26e594aff37aaf0797e`, with 245 maintained records.
This is a bounded deferral, not a finding that pathway sources are exhausted.
The unresolved chemistry is tracked in
[issue #516](https://github.com/CultureBotAI/PathwayMech/issues/516);
merging this evidence dossier does not close that issue.

## Pathway scope

The MetaCyc 27.0 definition contains five reactions, retained in
[native-boundary.json](native-boundary.json). Its HEXITOLDEGSUPER-PWY parent and
downstream glycolysis links are outside this boundary.

| Native reaction | Direction within the pathway | Source-defined step |
| --- | --- | --- |
| TRANS-RXN-161 | Left to right | Galactitol uptake/phosphorylation with distinct phosphorylated and unphosphorylated HPr classes |
| 1.1.1.251-RXN | Left to right; formally reversible | NAD-dependent oxidation to open-chain D-tagatose 6-phosphate; chemical mapping disputed |
| RXN-16992 | **Right to left**; formally reversible | Open-chain to cyclic D-tagatose 6-phosphate; annotated spontaneous |
| TAGAKIN-RXN | Left to right | ATP-dependent phosphorylation to cyclic D-tagatose 1,6-bisphosphate |
| TAGAALDOL-RXN | Left to right | Cleavage to glyceraldehyde 3-phosphate and dihydroxyacetone phosphate |

The full route is retained for future curation. Omitting transport or the
separate ring conversion would change the selected pathway boundary.

## Mechanistic summary

The native GALACTITOL-1-PHOSPHATE structure matches `CHEBI:60083`, including
stereochemistry and charge −2. Native CPD-15826 matches `CHEBI:134283`, the
open-chain D product. However, oxidizing C5 of that substrate while preserving
the three surviving stereocenters produces `CHEBI:134284`, the **L** product.
The mirror substrate gives the D product. This is a structural inconsistency
under the stated C5 oxidation, not a conclusion drawn from D/L labels alone.

[RHEA:28107](https://www.rhea-db.org/rhea/28107) uses the same disputed substrate
and D product. [RHEA:15138](https://www.rhea-db.org/rhea/15138) uses the same
substrate and the L product; it is consistent with this calculation but describes
a different product route. Neither is accepted here as an exact replacement for
the experimentally reported L-substrate/D-product chemistry.

The 2015 paper reports oxidation of its LG1P sample and inhibition by DG1P.
Its methods and modeled ligand poses do not establish a complete, independently
traceable structure for the vendor's physical samples. The computational result
therefore diagnoses the database structures; it does not identify those samples.

## Evidence table

| Evidence | Observation and limit | Retained support |
| --- | --- | --- |
| MetaCyc 27.0 whole pathway and reaction XML | Five native members, compartments, formal and pathway directions; native equations are source facts, not accepted corrected chemistry | [Native boundary](native-boundary.json), [source hashes and URLs](native-source-manifest.json) |
| Native compound XML and current ChEBI structures | Exact native substrate/D-product identities; atom-preserving C5 oxidation yields the L product | [Portable calculation inputs](stereo-inputs.json), [replay](replay_stereochemistry.py), [root replay result](stereo-result.json) |
| Current issuing authorities and pinned Rhea 142 | Alternate neutral substrate and reaction leads exist, but complete exact route closure remains unfinished | [Authority assessment](authority-assessment.json) |
| PMID:26143925, §§2.3 and 3.6; FigS1 | LG1P oxidation and DG1P inhibition; NADH absorbance endpoint, not new direct product structure analysis | [Primary reading assessment](primary-reading.json) |
| PMID:8955298, pp.6791–6794 | Construct-dependent transport/aldolase assays; GatZ not established as kinase; strain scope must be retained | [Primary reading assessment](primary-reading.json) |
| Fresh corpus and prior-source search | Candidate absence is bounded by the enumerated search; prior combined PathBank and SEED mentions exist | [Deduplication assessment](dedup.json) |

## Gaps

Before adding the complete pathway:

1. Resolve exact substrate stereochemistry, charge and experimental assignment.
   Neutral `PubChem:53827506` is a useful mirror-substrate lead; its identifier
   must not be assigned to a computed dianion. KEGG:C06311/R05571 also needs
   complete substrate/product, ring-state and charge verification.
2. Establish exact reaction identities for the intended complete route and
   preserve the conflicting native/Rhea cross-references. A corrected label
   cannot repair an incompatible structure.
3. Retain both HPr molecular states and compartments. Rhea reactive-part
   histidine identifiers do not identify the whole HPr carriers.
4. Resolve experimental donor/construct and organism scope, kinase assignment,
   GatY/GatZ assembly and activity evidence. Native CPLX0-240 is KbaY, not GatY.
   The 1996 paper's K-12/EC3132 assays do not establish every MG1655 protein join.
   [Catalyst source projections](catalyst-scope.json) preserve these distinctions.
5. Revisit the unread 2012 GatD, 2002 GatY/GatZ, kinase and Salmonella primary
   leads listed in the reading assessment, then perform full record review,
   independent identifier validation and rendering after curation.

## Reproduction and retention

With RDKit 2025.03.6 available, run from any directory:

```sh
python /path/to/galactitol/replay_stereochemistry.py \
  /path/to/galactitol/stereo-inputs.json \
  --output /tmp/galactitol-stereo-result.json
```

The replay uses committed structural projections and needs no network or local
database cache. It verifies structural consistency, not acquisition authenticity
or the experimental sample assignment. Its input contains source URLs, locators
and whole-original hashes for that separate audit.

Original XML, article figures, supplement and failed-download bodies remain in
external working storage. The recorded temporary paths are session locations,
not a durable archive. Whole 1996/2015 main-paper bytes were not retained:
web-rendered text reading and separately retained figure/supplement hashes do
not constitute whole-paper digests. Rejected HTML/error responses are not
scientific evidence. This PR makes no public-release licensing determination.

The [reading coverage](primary-reading-coverage.json) and
[acquisition summary](primary-acquisition-summary.json) distinguish inspected
text, inspected images and unavailable material. They also distinguish the
successful web-reading URL from the failed local filename variant.

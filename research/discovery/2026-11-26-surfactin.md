# Bounded FZB42 surfactin cluster discovery — 2026-11-26

This round adds one native PathwayMech record, `MIBiG:BGC0000433`, after the
AIMech canary passed local gates and its draft PR checks. It does not establish
source saturation. The comparison baseline is PathwayMech
`d2f73822d650851193ce541d68c8ebd8ffac4907` and the retained November 16 MIBiG
source report. No source inventory, importer, schema or workflow changes.

## Candidate dispositions

| Candidate | Disposition | Evidence |
| --- | --- | --- |
| Ethylmalonyl-CoA pathway | Already present | `data/pathways/ethylmalonyl-coa-pathway.yaml` |
| Acetoin biosynthesis | Already represented | `data/pathways/pyruvate-fermentation-to-acetoin-iii.yaml`; a broader GO name is not a new route |
| Spermine biosynthesis | Already present | `data/pathways/spermine-biosynthesis.yaml` |
| Allantoin degradation | Already represented | Separate glyoxylate and ureidoglycolate route records; no umbrella duplicate added |
| Glutathione degradation | Already present | `data/pathways/glutathione-degradation.yaml` |
| FZB42 surfactin cluster, BGC0000433 | Added | One new bounded cluster record with three source-annotated NRPS components |

Duplicate searches included hidden and ignored files in the canonical checkout,
excluding Git internals, virtual environments and dotenv files. Exact cluster,
protein, nucleotide and PMID identifiers, and the surfactin name produced no
matches. The retained external MIBiG archive contains this member; that raw
source inventory is not a maintained pathway record. Other external caches
were not searched. Further source families were not surveyed in this round.

## Inspected sources and limits

The retained [official MIBiG 4.0 archive](https://dl.secondarymetabolites.org/mibig/mibig_json_4.0.tar.gz)
was rehashed as `986f1a69fb5eeb84fd7c0175ae921304c22fd5f8ed04c96d8c1c0c95a145837b`.
Member `mibig_json_4.0/BGC0000433.json` is entry version 5. The freshly retrieved
[live JSON](https://mibig.secondarymetabolites.org/repository/BGC0000433.5/annotations.json)
has the same biological content except for seven explicit `reviewed: false`
module flags. This is a bounded entry comparison, not a release-wide update.
MIBiG data attribution and CC BY 4.0 provenance remain in the additive native
source manifest. No new terms acceptance or bulk download occurred.

The record retains active/questionable/complete source assessments and all nine
native gene annotations. Only three independently verified synthetases become
graph nodes. Module substrate assignments are structure-based inferences, so
they do not become experimentally measured reactions. The source locus
`AJ575642.1` has `0..0` coordinates; the record retains the accession and omits
unspecified bounds. It does not infer a single exact chemical structure from
the product name or assert that these three proteins exhaust the pathway.

[GenBank CAE02630.1, CAE02631.1 and CAE02633.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=CAE02630.1,CAE02631.1,CAE02633.1&rettype=gb&retmode=xml)
independently establish the srfAA/srfAB/srfAC identities and their FZB42 coding
locations. The full batch digest is
`a242df8b52e4f1ba0b8890ab504c44dd3a607557528e7be54adda3aa0a00560d`.
The native authority builder projects their product names. The native ontology
builder resolves NCBITaxon:326423 against the local Semantic SQL authority;
its release, complete database digest and term are retained separately.

The [primary paper's abstract and Figure 2F caption](https://pubmed.ncbi.nlm.nih.gov/14762003/)
support the srf cluster's role through cassette disruption and loss of detected
surfactin. Full text was not inspected. This does not show that each synthetase
alone is sufficient, or exclude polar effects. The B/C component edges retain
their database-annotation basis and empty function-evidence lists. The source's
historical organism name and current FZB42 taxonomy are explicitly distinguished.

Raw source bytes and retrieval receipts are retained under the fleet-ops run's
`pathwaymech/` evidence directory. The native closed-schema and identifier
staging checks passed before installation. Full repository quality gates,
tests, lint, vendored checks and generated-page verification are recorded in
that run's validation receipts before publication.

Next: inspect primary full text and exact module chemistry in a separately
scoped enrichment task before extending this partial graph. This round has
not exhausted MIBiG or other pathway sources; no goal was resumed.

# Next-source ingestion — 2026-10-07

This bounded continuation adds four maintained records: three Reactome pathways
and one MIBiG cluster. The corpus grows from 152 to **156 records**: 86 GO-CAM,
50 MetaCyc, 12 WikiPathways, six Reactome and two MIBiG records. It adds
11 reaction occurrences and 173 mechanistic edges. These are reviewed canaries,
not a complete import of either database.

| Record | Scope | Reactions | Edges |
| --- | --- | ---: | ---: |
| [Reactome:R-MTU-936654](../../data/pathways/mycobacterium-cysteine-synthesis-from-o-phosphoserine.yaml) | CysM–CysO route, beginning at charged CysO | 2 | 28 |
| [Reactome:R-MTU-936721](../../data/pathways/mycobacterium-cysteine-synthesis-from-o-acetylserine.yaml) | CysH/Sir, CysE and CysK1 OAS route | 4 | 69 |
| [Reactome:R-MTU-936635](../../data/pathways/mycobacterium-sulfate-assimilation.yaml) | Sulfate uptake and APS/PAPS activation | 5 | 72 |
| [MIBiG:BGC0000852](../../data/pathways/sporosarcina-pasteurii-ectoine-biosynthetic-gene-cluster.yaml) | Sporosarcina pasteurii ectABC operon | 0 | 4 |

The [Reactome source projection and ledger](2026-10-07-reactome/README.md)
disposition all 177 source edges, preserve physical protein states and source
compartments, exclude the unresolved CysO charging and contradicted CysK2/OAS
reactions, and correct GTP coupling to APS synthesis. Chemical protonation,
ferredoxin composition and source inference limits are explicit. The record
labels do not turn source forms into a fully balanced physiological model.

The [MIBiG review](2026-10-07-mibig-ectoine-canary.md) preserves upstream
questionable/completeness-unknown status. Independent primary experiments
support whole-operon ectoine production; individual functions remain
sequence-based assignments. Three alternative clusters remain deferred with
specific evidence gaps. Exact identity checks and deduplication included ignored
and hidden repository files.

The [BRENDA pilot](2026-10-07-brenda-canary.md) now retrieves public CSV/RDF
pathway content, but does not support an unambiguous reaction–enzyme–organism–
reference projection. Its six-assertion native fixture is research evidence,
not a maintained pathway. BRENDA remains disabled with status `next`.

## Importer review and independent authorities

Review identified and fixed [#278](https://github.com/CultureBotAI/PathwayMech/issues/278),
[#279](https://github.com/CultureBotAI/PathwayMech/issues/279) and
[#280](https://github.com/CultureBotAI/PathwayMech/issues/280): featured catalysts
and cleavage fragments retain native physical identities, and context-edge IDs
are reproducible across fresh processes. Regressions failed before the fixes;
the 35-test BioPAX suite passes. In this cohort, Mec residues 26–146 are a concrete
cleaved state, not the complete UniProt protein.

An independent audit checked all 11 FragmentFeature intervals in the three
previously maintained Reactome exports against pinned UniProt sequence bytes.
Every interval starts at 1 and ends at the complete sequence length:
P9WN11/500, P9WFZ5/391, P9WQ21/765, P9WQ23/580, P9WKI1/367, P9WMY7/480,
P95189/260, P9WJN1/288 (in two exports), P9WJM9/414 and P9WJM7/315.
The exact authority artifact is `uniprot-2026-10-05` in
`conf/identifier_sources.json`; its SHA256 is
`31676bae7e800c5c801d514a75d19174e1ecb92f9afe504b3585c2ccabc01360`.
No existing record required a cleavage correction.

[#281](https://github.com/CultureBotAI/PathwayMech/issues/281) corrects the new
MIBiG evidence serialization: native GenBank XML and MIBiG JSON assertions
support the annotated genes, while a short verbatim primary excerpt supports
observed operon output. A separate reviewer verified the biological claims,
strain identity, source hashes and excerpt.

Five independent source artifacts were added to the authority manifest: three
Reactome release 97 BioPAX documents, a UniProt batch and the exact NCBI protein
batch. The MIBiG identifier is independently resolved from its pinned 4.0 archive;
the current entry is byte-identical. Eight ontology identities were extracted
from independently acquired OAK databases whose complete byte hashes and release
metadata match the prior snapshot. Existing verified ontology terms remain
available. No resolver exception or broader label policy was introduced. The
[identifier inventory](2026-10-07-next-source-identifiers.json) lists every
identifier in the four records and all 81 new-to-corpus identifiers, including
primary reference IDs.

## Remaining source work

HADEG remains a candidate support adapter, and a PMN/ChlamyCyc pilot remains
available. BRENDA needs scoped enzyme context and checked native identifier
resolution before adoption. The MIBiG deferred candidates need their documented
protein or primary-evidence gaps resolved. PathBank's redistribution question
remains outside this batch. An active source flag does not imply exhaustive
pathway coverage.

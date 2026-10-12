Recommend a narrowly validated native enzyme-name derivation for the three
unnamed META27 complex frames. This is a proposal supported by issuing naming
documentation and external controls; it is not a production change or an
adopted authority snapshot. Keep every exact assembly and the full pathway.

The missing direct `Protein/common-name` does not alone establish absence of a
native enzyme name. SRI documents an explicit naming convention for proteins
without that slot: the linked enzymatic-reaction names can supply their names.
The older loader manual explains this convention, and SRI's function reference
and Lisp API describe `full-enzyme-name` using the protein and linked activity
names. Restricting the fallback to a single exact linked activity avoids
inventing a name or implementing a general concatenation algorithm. Treating
that result as a canonical native enzyme name is the recommendation here,
based on those documented semantics; the source does not prescribe PathwayMech
authority policy. Sources: [SRI loader manual](https://bioinformatics.ai.sri.com/biowarehouse/repos/biocyc-loader/flatfile/doc/biocyc-manual.html),
[SRI function reference](https://bioinformatics.ai.sri.com/ptools/ptools-fns.html),
[SRI Lisp API](https://bioinformatics.ai.sri.com/ptools/api/).

The schema guide defines each enzymatic-reaction as an enzyme/reaction pairing;
its enzyme slot points to the particular polypeptide or complex. This supports
requiring an exact same-frame back-reference, rather than borrowing a name
from an arbitrary descendant, related monomer, citation, organism or curator.
Source: [Pathway Tools schema guide](https://pathway.yeastgenome.org/schema.shtml).

| Exact native complex | Proposed native authority label | Native component coefficient |
| --- | --- | --- |
| MetaCyc:ACNEULY-CPLX | N-acetylneuraminate lyase | 4 |
| MetaCyc:NAG6PDEACET-CPLX | N-acetylglucosamine-6-phosphate deacetylase | 4 |
| MetaCyc:GLUCOSAMINE-6-P-DEAMIN-CPLX | glucosamine-6-phosphate deaminase | 6 |
| MetaCyc:CPLX0-8588 | N-acetylmannosamine kinase | 2 |

The first three labels derive from each complex's sole native
`catalyzes/Enzymatic-Reaction/common-name` with an `enzyme/Protein` reference to
that same complex. The fourth remains the unchanged direct-name case. The
original activity synonyms are not silently imported as complex synonyms.
Assembly words such as tetramer or hexamer are not appended to authority names;
the native component coefficients and independently supported assembly edges
carry those facts. Native species data remain source annotations, not expanded
experimental or strain equivalence claims.

Alternative sources were investigated. The preflight's exact ENZYME HTML
responses contain monomer-page redirects, so their identity cannot establish a
canonical complex name. Three new direct requests to BioCyc return HTTP200
account-required HTML after redirection, not usable protein XML. All response
bodies and HTTP receipts are retained. This is a bounded access result, not a
claim that every native endpoint lacks a name. The original mirror XMLs remain
unchanged and bound to their original HTTP200 acquisition receipts. Four issuing
naming/schema documents were downloaded successfully with byte hashes. The
initial sandbox DNS failures are also retained.

The approved adapter currently rejects each unnamed complex after its existing
URL, service, PGDB, version, full-object and frame-identity checks. That behavior
matches its deliberately narrow direct-name contract. The current MetaCyc
participant policy requires canonical names or synonyms; its contextual rules
cover record/reaction labels only. A generic participant contextual exemption
would weaken that contract. None is needed for this recommended native-name
derivation, and no policy change is proposed.

The bounded production proposal is:

1. Factor the existing XML identity validation and name decoding into shared
   internal helpers without weakening their guards or changing direct-name
   precedence. Fall back only when the direct name slot is completely absent;
   malformed, empty or duplicate direct names remain errors.
2. Initially support only a native Protein-Complexes member with one explicit
   homomer component and an integer coefficient at least two, one resolved
   direct enzymatic-reaction, one exact same-complex enzyme back-reference,
   one coherent native reaction reference and one nonempty string activity name.
   Reject multiple activities even if their names happen to match. This narrow
   scope covers the three actual originals; broader naming cases remain out of
   scope until separately justified.
3. Decode the activity name with the same safe markup/entity rules as direct
   names and emit the exact complex ID with that native name and no borrowed
   aliases. Keep the existing canonical cross-source conflict checks. Do not
   derive assembly, chemistry, taxa or experimental function from name extraction.
4. Update the ProteinXML documentation and focused tests. No importer, schema,
   participant-policy or generic nested-name extraction change is proposed.
   Later production implementation must run its focused regressions, meaningful
   CLI output-preservation checks and a full retained-ID canonical build before
   any maintained authority adoption.

`prototype.py` is an external proof of these guard conditions. It deliberately
calls the accepted adapter first and recognizes its missing-name exception;
that exception-message technique is not recommended as production architecture.
`check-proposal-v3.py` passed four original-source positives, 22 identity and
name negative controls, and four identifier-policy cases. The unchanged policy
accepts the exact proposed names, rejects an added assembly suffix, rejects
source_context-only authority assertions even with matching labels, and rejects
a missing complex ID. The gate fixtures use full existing authority sets plus
explicit external proposal terms; they are not full scientific pathway records
or candidate canonical snapshots. Thirty-one exact inputs were rehashed before
the successful result.

Two initial check-harness errors are preserved: selecting the wrong acquisition
receipt and constructing an incomplete authority fixture under the full policy.
The prototype, production adapter and original source bytes were unchanged while
correcting those harness setups. Successful terminal execution is `402bbb/0`;
the failed attempts remain `3a6618/1` and `ad64f1/1`.

No maintained files, bound Salvage II inputs, shared-cache bytes, Git metadata,
or GitHub state were written. Root must review and authorize any later bounded
implementation. The author should preserve exact IDs, native assemblies and
all entry/regulatory context while authority support is finalized.

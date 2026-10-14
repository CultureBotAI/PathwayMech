# Quinate degradation II curation

The maintained target is `MetaCyc:PWY-6416`,
`data/pathways/quinate-degradation-ii.yaml`. It describes quinate oxidation,
dehydroquinate dehydration and dehydroshikimate dehydration to protocatechuate.
The broad native NAD(P) first reaction and its exact NAD-specific realization
remain separate graph nodes; they do not form four sequential steps.

The baseline is commit `11afa1984bbb0d41c34dc82361bd0f0e1c0b9f37`, with 253
maintained pathway records and 4,913 authority terms. Duplicate searches cover
both the main and task working trees, including ignored and hidden files.
The preflight package records prior mentions, source closure and the continuing
queue. Shikimate degradation II remains a separate candidate; this addition does
not establish source exhaustion.

## Evidence packages

- `preflight/`: baseline records, complete search passes, prior-hit dispositions
  and continuing leads.
- `chemistry/`: independently checked native compound structures, complete Rhea
  sides and directions, and the initial three-reaction core.
- `native/`: 73 native objects, 18 enzyme activities, 998 dispositioned slots,
  closed protein/gene references, issuing identities and construct checks.
- `primary/`: inspected primary sources, access limitations, short quotation
  replay, construct and claim ledgers, and the biological author proposal.
- `assembly/`: the initial integrated author record and reproducible assembly
  helpers. These are retained inputs, not independent scientific approval.
- `authorities/`: canonical build commands, original bindings and checks that
  previous authority terms, source objects and manifest entries are preserved.

Complete downloads remain outside the repository at the hash-bound paths in
these manifests. Compact projections retain the biological statements and
locators needed for review. A local external path is a replay location, not a
claim that the original bytes are distributed in this repository. The Rhea
reference digest identifies its complete pinned RDF release; edge locators name
the specific reaction-side and participant triples within that release.

## Scope decisions

The graph distinguishes C. glutamicum R genetic evidence, ATCC 13032 QsuD
structural/kinetic evidence and ATCC 13869 QsuB construct evidence. It retains
experimental tags, inferred enzyme assignments and alternative assay metals.
The QsuB gene identity is supported by strain metadata, its issuing CDS and all
three published primer boundaries; that is not a complete resequencing of the
assayed clone. Historical fungal experiments are not relabeled as experiments
in modern reference strains.

The QutB preparation has conflicting descriptions in the primary Methods and
Table 2. QsuB inhibition concentrations also differ between Methods and the
figure caption. Those disagreements are retained. Shared PQQ-route citations,
adjacent biosynthetic activities, downstream protocatechuate degradation and
unsupported direct regulator-binding claims are not used to expand this route.

Scientific review observations and their successors are stored separately under
`reviews/structured/`. The five initial findings are tracked in issues
[#545](https://github.com/CultureBotAI/PathwayMech/issues/545) and
[#546](https://github.com/CultureBotAI/PathwayMech/issues/546), plus the identifier-label
gate correction in [#547](https://github.com/CultureBotAI/PathwayMech/issues/547). Final acceptance
must cite the resolved observations and checks against the final inputs.

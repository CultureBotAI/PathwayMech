# External representation proposal — pending schema-owner decision

No maintained schema, graph, KGX, authority, or record is changed by this document.

## Concrete gap

PMID:29229699, full original PMC5809692, Materials and Methods section `sec4-2`, describes PCR from E. coli BW25113, removal of the first nagB codon in a SUMO fusion, and Ulp1 cleavage yielding Ser1-NagB instead of native Met1-NagB. Results `sec2-1` through `sec2-4` measure this construct. An ordinary activation edge ending at UniProtKB:P0A759 or the native MetaCyc NagB hexamer would hide that distinction in graph and KGX endpoints even if the evidence text explains it. Source-scoped state investigation has not yielded an issuing Ser1-NagB protein frame; the acquired native NagB frame and its linked regulators do not identify this construct. This is a bounded negative finding, not proof that no identifier exists anywhere.

Native issuing identifiers do cover uridylylated PII (`MetaCyc:URIDYLYL-PII`, polypeptide) and HPr phosphohistidine (`MetaCyc:PTSH-PHOSPHORYLATED`, with unmodified-form PTSH-MONOMER). The modified PII assembly `MetaCyc:CPLX0-8568` has a direct name and unmodified-form PIIPROTEIN-CPLX but no component coefficient or occupancy assertion. Do not infer three uridylylated subunits from the unmodified trimer. Do not treat Mutagenesis-Variants feature annotations as the identity of a protein carrying all listed mutations.

## Minimal proposed contract

Add one optional edge field `endpoint_qualifiers`, containing zero, one, or two objects with:

- `endpoint`: `subject` or `object`; each appears at most once.
- `kind`: `experimental_construct` or `molecular_state`.
- `description`: nonempty text, maximum 400 characters, describing the exact source-limited alteration/state. This is an assertion, not a new identifier.
- `evidence`: one or more existing Evidence objects with local reference IDs and locators, under the existing quote/assertion length rules.

The referenced endpoint remains a native authority identifier denoting the base protein or assembly. The complete edge claim is the endpoint plus its qualifier. It must never be flattened into an unqualified biological edge. Qualifiers are permitted only for protein/complex participants; reaction or taxon qualification would require a separate design. A curation rule prefers exact issuing state identifiers when available and requires a qualifier when a tested experimental construct differs from the base endpoint. This does not assert that the entire experimental sequence equals the base sequence except at the named site.

Example proposal, deliberately not an accepted current-schema record:

```yaml
- id: nagb-uridylylated-pii-assay
  subject: MetaCyc:URIDYLYL-PII
  predicate: activates
  object: UniProtKB:P0A759
  endpoint_qualifiers:
    - endpoint: subject
      kind: experimental_construct
      description: His-tagged recombinant ASKA GlnB preparation, refolded and uridylylated by GlnD; exact uridylylation occupancy is assay-dependent.
      evidence:
        - reference_id: PMID:29229699
          source_assertion: Recombinant His-tagged PII was purified, refolded and subjected to GlnD-dependent uridylylation; modified PII was not repurified from that reaction mixture.
          source_locator: PMC5809692, Materials and Methods, sec4-3 and sec4-6.
    - endpoint: object
      kind: experimental_construct
      description: Ser1-NagB assay construct from E. coli BW25113; first nagB codon omitted in SUMO fusion and Ulp1 cleavage yields N-terminal Ser instead of Met. No claim of sequence identity elsewhere.
      evidence:
        - reference_id: PMID:29229699
          source_assertion: The BW25113 nagB SUMO fusion omits the first codon; Ulp1 cleavage produces Ser1-NagB rather than native Met1-NagB.
          source_locator: PMC5809692, Materials and Methods, sec4-2, Cloning nagB into pMST3.
  evidence:
    - reference_id: PMID:29229699
      source_assertion: PII-dependent Ser1-NagB activation depended on uridylylation and GlcNAc6P under the reported conditions. The GlnD uridylylation mixture was not repurified before assay; matching mixture controls were tested.
      source_locator: PMC5809692, Results sec2-1/sec2-2 and Materials and Methods sec4-6.
```

Final author evidence must retain the GlcNAc6P dependence and HPr phosphorylation conditions as well as the construct qualifier. This example establishes representation only; final assertions will be checked against the full results again.

His-tagged ASKA NanE and HPr preparations likewise need a subject construct qualifier when an edge is grounded only in those assays. Native database-corroborated protein function and assembly assertions retain their own independent scope.

For an HPr activation edge, use exact native `MetaCyc:PTSH-MONOMER` as subject and qualify the NagB object as above; the evidence records nonphosphorylated HPr, concentration and GlcNAc6P/pH context. Do not emit an activating edge from `MetaCyc:PTSH-PHOSPHORYLATED`, and do not turn an absence of measured activation into an inhibitory edge. For GlnB, use its exact uridylylated state; native unmodified PII assembly may have a separately supported assembly edge but is not interchangeable with the assay's U-PII state.

## Required visibility and preservation

1. YAML stores qualifiers beside the exact edge, including their evidence. Schema.py and closed LinkML declare the same class and checks; ordinary existing records remain unchanged.
2. The graph must visibly badge a qualified endpoint on every incident qualified edge (e.g. `NagB [Ser1-NagB assay construct]`) and show the complete description and evidence in its accessible detail view. A shared base-protein node must not visually erase the qualifier; a scoped display instance, if used, is a UI key only and never a minted biological CURIE.
3. The text edge list must display the qualifier adjacent to the subject/object label, so the scientific meaning survives without JavaScript.
4. KGX edge export must add a non-lossy `endpoint_qualifiers` JSON column with role, kind, description and evidence. Export and dedup identity must include the qualifier payload, preventing qualified and unqualified edges from being merged. If a consumer cannot preserve the qualifier, it must omit/reject the qualified claim explicitly rather than silently export an unqualified edge.
5. Source replay and input/output guards bind qualifier bytes and evidence just like other semantic fields. Restoring Met1 wording, deleting the qualifier, exchanging subject/object qualifier roles, dropping its evidence, or exporting only base endpoints must fail the relevant controls.

This bounded extension retains the complete supported biological scope without inventing a construct CURIE or asserting that engineered assays establish the behavior of the unmodified native protein. It requires independent code/science review before maintained adoption; the external candidate remains pending meanwhile.

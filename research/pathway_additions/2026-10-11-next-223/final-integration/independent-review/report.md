# Independent adversarial integration review

**Disposition: no actionable findings.** Reviewed the uncommitted integration against base `24c91a1b232f2879281003c4abfab70a624b9016`. The reviewer did not author the feature, pathway record, prior reviews, or integration dossier and made no maintained-file, Git, cache, or GitHub changes.

## Scope

Read the complete changed source-parser and product-code diffs, new shared claim-identity helper, endpoint qualification tests, BiGG native authority tests, MetaCyc fallback tests, and EcoCyc native authority tests. Checked the LinkML/native schema split, explicit namespace policy, qualification placement, graph instance isolation, HTML evidence rendering, KGX payload/citation preservation and deduplication identity. Reviewed the integrated record's declarations, three qualified assay edges, CRP/SgrS correction, and the saved successor scientific report. This is an integration/code review, not a claim to have independently repeated the complete 114-edge primary-literature review.

Adversarial attention included wrong native source kind/identity, scope crossing between META and ECOLI, strain/version provenance, nested names versus direct authority, model-specific versus universal BiGG identities, ambiguous JSON/XML, direct-name fallback precedence, missing qualification evidence, endpoint type ambiguity, role changes, and accidental promotion of source cross-references. Existing prior source-body and science reviews remain separately attributable.

## Independent checks

`probes.py` completed successfully (terminal `0e7468`, exit 0): **49 checks**, recorded in `probe-results.json`.

- The actual record renders 114 edges and 85 display nodes. Its six qualified endpoint instances are distinct from shared native nodes and retain native identifiers, full descriptions, and the correct edge/role anchors.
- Every actual KGX edge retains the exact qualifier payload and the complete edge-plus-qualifier citation set. Changing qualification presence, role, wording, kind or evidence changes the qualified claim ID; reversing the role-list order does not. Deduplication preserves the same distinctions.
- Actual-record mutations reject qualifying chemical or RNA endpoints, ambiguous participant/reaction identity, non-string role values and malformed qualification reference IDs.
- All nine actual source originals (three unnamed MetaCyc homomers, three BiGG universal objects and three EcoCyc complex/RNA objects) parsed correctly with their declared hashes. The three BiGG version companions validated.
- Mutated authentic originals reject model-compartment identity substitution, duplicate JSON identifiers, ECOLI strain changes, namespace crossing, unresolved direct names, monomer substitution, mismatched activity back-references and blank direct names. Changing BiGG cross-references does not promote those values into authority terms. Original source hashes remained unchanged.

The actual pathway SHA256 is `ebbc3eb8334b28b975444285a6e0aab7315a3153a73492270a083cd87fb4f5ff`. `reviewed-bindings.json` records the reviewed implementation, schema, test, policy and record bytes. No whole-corpus test repetition or new full source inventory was performed; root owns the full maintained gates, canonical review, publication and merge checks.

## Nonblocking observation and limits

The add-pathway skill's enumerated allowed prefixes omits the newly supported `EcoCyc` spelling. A small documentation sync is reasonable. The skill also directs curators to the actual schema and identifier documentation, both correctly updated, so this omission is not treated as a product defect or a reason to manufacture a GitHub issue.

No browser interaction or live upstream API re-fetch was performed. Rendering checks use the actual generated SVG and source-bound original bodies; they do not establish visual usability at every viewport or an upstream source refresh. The record deliberately retains BiGG/ChEBI stereochemical disagreement, strain and construct limits, opaque downstream interfaces, and deferred public-release licensing. None of those explicit scientific boundaries is silently removed by the reviewed implementation.

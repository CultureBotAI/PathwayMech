# Continued pathway discovery after PR 507

This work resumes the open goal of finding, reviewing, and adding supported
microbial pathways. The starting corpus is the 242 records at
`995b0ad9b19eaa3a46cc2898e73445cf0cce16db`. GitHub main was independently checked
against that commit on 2026-10-14 UTC (2026-10-13 local date). Completion of the
previous publication task does not establish source exhaustion.

## Candidates under active examination

| Candidate | Current disposition | Evidence needed next |
| --- | --- | --- |
| PathBank:SMP0002036 / PW002022, D-sorbitol degradation II | Reconcile the retained map with native transporter definitions and primary experiments before authoring. | Srl/Gut versus ManXYZ assignment, transporter sequence and assembly history, sugar and HPr states, dehydrogenase assembly, and downstream chemical scope. |
| MetaCyc:PWY0-301, L-ascorbate degradation I | Authored as `data/pathways/l-ascorbate-degradation-i.yaml`; scientific review and publication gates are recorded separately. | Five-event MetaCyc 27.0 definition, qualified primary transport/enzyme evidence, and exact identifier authorities. See the [ascorbate dossier](ascorbate/README.md). |
| MetaCyc:GALACTARDEG-PWY, D-galactarate degradation I | Positive follow-up lead, not yet a new record. | Complete primary PMID:9772162 and its distinct galactarate entry; reconcile overlap with maintained glucarate degradation. |
| MetaCyc:PWY0-521, fructoselysine and psicoselysine degradation | Positive overlapping-boundary lead, not an automatic second record. | Primary PMID:14641112 and an explicit boundary decision against the narrower maintained GO:1901281 record. |

The retained 244 preflight was read before resuming the sorbitol work. Its
selenium and D-serine deferrals remain unresolved; its threonine candidate is
already represented by `MetaCyc:THRDLCTCAT-PWY`.

## Source observations

New exact public retrievals on 2026-10-14 returned native META/ECOLI 27.0 XML
for `SORBDEG-PWY`, `CPLX-169`, `SORB6PDEHYDROG-RXN`, `D-SORBITOL-6-P`, and
`CPD-15709`, together with current UniProt P05706/P05707 JSON. Originals and
request/hash receipts are external under
`/private/tmp/pathwaymech-next-244-current-sources-20261013/` and
`/private/tmp/pathwaymech-next-244-followup-sources-20261013/`.

The three current PathBank page/OWL/PWML requests returned HTTP 403. This is an
access observation for those requests, not a claim of universal unavailability.
The earlier whole PW002022 archive member remains available and is explicitly
historical. It must not be relabelled as the current export.

`GO:0006062` is broader than route II: the pinned GO source links both
`SORBDEG-PWY` and `PWY-4101` with `skos:narrowMatch`. The newly retrieved
`SORBDEG-PWY` has one core reaction and an incoming transporter link; its
existence alone does not satisfy the add-pathway rule against promoting a
single reaction as a new mechanistic pathway.

The newer META 27.0 `PWY0-301` definition includes the PTS reaction within five
ordered members. The older SGD-hosted definition contains four core members
and an incoming PTS link. Both are retained in the external ascorbate authority
work; their different boundaries must be attributed to the actual source
versions. Early proposed hydrolysis ordering is not evidence for the later
experimentally established UlaG reaction.

## Search and completion limits

Candidate searches included hidden and ignored repository text, with Git
administration, virtual environments, and bytecode excluded. Matching maintained
records and historical research mentions were read as candidate-specific
context. These searches did not decode every compressed archive and do not
assert absence of a mention in all temporary workspaces. Exact source mentions,
shared reactions, and broad ontology terms are not themselves duplicate pathways.

This discovery note is not a scientific acceptance or gate receipt. The
ascorbate record has its own evidence dossier, immutable scientific reviews,
and execution receipts. The user's publication request bounds this PR to that
addition; the other candidates remain follow-up work. Multiple supported leads
remain, so source exhaustion is false.

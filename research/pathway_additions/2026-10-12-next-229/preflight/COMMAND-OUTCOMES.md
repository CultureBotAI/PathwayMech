# Ethylene glycol preflight: actual outcomes

All Python work used `/private/tmp/pathwaymech-next-195-20261011/.venv/bin/python -B` with `PYTHONDONTWRITEBYTECODE=1 UV_NO_SYNC=1`. No install, sync, shared-cache write, maintained edit, Git mutation or GitHub mutation occurred in this task. Only task-local external evidence was written. A task-created Swift compilation cache was removed; the exact cleanup receipt remains.

## Successful reads and checks

- `intake.py`: verified the root handoff hash and all 52 lead-manifest artifacts, with hidden/ignored/followed inventory equality (`57cfbc/0` after the first manifest-key error). Actual baseline and prospective hashes are in `derived/intake.json`.
- `novelty-v2.py`: all 227 actual and two prospective YAML records parsed; full repository search used `rg --no-ignore --hidden --follow`, excluding `.git` and `.venv`; 267 matched files retained. This found no candidate identity but its coefficient fallback was not a stoichiometric proof.
- `finalize-evidence.py`: successor V3 verifies all 229 original record hashes, removes coefficient defaults, compares exact IDs and coefficient-free chemical participant sides in both directions, binds original sources and preserves provenance. No complete defining signature matched. Independently verified candidate coefficients come from Rhea.
- `extract-rhea.py`: exact original Rhea142 master/directional families extracted; complete chemical formulas, charges, coefficients and balance checks retained. Correct families are 27630–27633 and 20001–20004.
- Frozen original ZIP/member replay: unique PW002093.owl, exact 816294f1… member under b3a9b955… archive; source root/child membership and all original objects are preserved.
- Acquisition retries and jobs4–13: public source bodies and all status/URL/hash receipts retained. HTTP200 alone was never treated as evidence of valid XML/PDF/DOCX. The jobs9 partial failure is separately documented.
- Primary read outcomes and limitations are recorded in `source-read-receipts.json`; exact XPath/paragraph anchors in `exact-paragraph-locator-index.json` reference the retained projections and original sources.
- `build-handoff.py`: creates 50 explicit scientific/scope dispositions, 54 bound source keys, 441 paragraph anchors, 15 construct/assay rows, complete handoff and remaining-gaps ledger.
- `replay-preflight.py`: passed 85 checks and five negative controls (`c0e528/0`, final receipt also stored). Checks include original bindings, exact two-event sides, independent formula/charge arithmetic, source-defined pathway membership, issuing protein/gene joins and the original SrsR image checksum. Negative controls reject the missing second proton, reversed event1, NAD/NADH identity swap, missing water and an invented signed PathBank child interaction.

## Failed or superseded attempts retained honestly

- First intake attempt expected an `artifacts` rather than `files` manifest key (`4a931f/0`); it was corrected, then all artifacts were verified.
- Initial non-escalated network acquisitions hit DNS failures and wrote zero-byte responses (`82b638/0`); public network retries succeeded where recorded. Several publishers returned403/429 and PMC endpoints returned500/challenge HTML. These bodies are not full literature.
- First Rhea extraction used 27633 as a master and failed (`06adc0/0`); the attempt script is retained. Inspection corrected the master to27630 before any chemistry claim.
- Initial PathBank object projection omitted RDF `ID` identities; V2 explicitly handles native RDF ID/about and supersedes it. Native source bytes never changed.
- Novelty V1/V2 assigned coefficient1 by fallback even when record multiplicity was encoded only in assertions. V3 removes those numbers; no existing-record balance claim relies on that fallback.
- The first PubMed projection included nested citation ArticleIdList entries. It is not an article-identifier authority; the corrected regulation projection uses article-own PubmedData/ArticleIdList.
- jobs9 exited1 on an existing Baldoma1987-jbc.pdf path; one concurrent Limon URL body was written before the failure. Actual jobs9 URL and resulting body are bound in `source-acquisition-index.json`. The full publisher article was fetched into a separate delivered body.
- Late native-identity projection initially tried to serialize lxml `_Attrib`, raising TypeError (`82a734/0`). It was corrected to `dict(e.attrib)` and rerun (`d5dbff/0`). A diagnostic treating the PathBank list as a dict also failed (`d2dfaa/0`); it had no source mutation.
- Main-site ECOLI-PD00257 returned HTML200 and XML parsing failed (`75e677/0`). A separately named true mirror XML was acquired, parsed and read (`64e1af/0`, `ef0499/0`); only it is proposed as native CRP identity support.

## Not run

No YAML candidate was authored here. Schema, strict validation, identifier gate, page rendering, full tests, lint and a canonical build were not run, and no passing status is claimed for them. This source preflight is not the independent scientific review of a finished record. Later authoring must disposition every ledger item and run its own exact-target gates.

The helper did not perform an independent EG review: it was reassigned by root to other work before producing EG results. No unperformed review is counted.

Source exhaustion remains false.

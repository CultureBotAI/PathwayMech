The source preparation for aerobic benzoate degradation I (`MetaCyc:PWY-2503`, next264) overstates its whole-Rhea comparison. Its frozen `helpers/verify_chemistry.py.txt` retains only numeric `contains[0-9]+` predicates, so it drops symbolic participants from mixed-coefficient equations before comparing their remaining fragments.

Independent review of the complete Rhea RDF found 37,222 directional equations: 37,068 fully fixed equations and 154 containing symbolic coefficients. The frozen preparation reports 37,216 compared equations and six exclusions; 148 of those comparisons silently omit material. For example, RHEA:10069 loses the `containsN` UDP-glucose, UDP and proton participants from sides `10068_L` and `10068_R`, leaving only its polymer terms.

The two selected all-unit-coefficient reactions, RHEA:12634 and RHEA:11561, remain correct. A strict independent comparison finds those same oriented matches among the 37,068 fully fixed equations. This is a major defect in the source-method claim and retained proof, not a demonstrated error in the selected route. No maintained next264 pathway has been added yet.

Acceptance:

- Reject an entire equation from fixed-coefficient comparison if either side has any nonnumeric material coefficient or unresolved material participant; never compare a truncated side.
- Retain all 154 excluded equations with complete source predicates and participant identities, and account for the 148 previously partial comparisons.
- Reproduce both selected complete equations, all 11 material entries and the route balance using a corrected helper; explicitly bound the broader comparison to 37,068 fully fixed equations.
- Preserve the frozen source package and append an evidence-linked correction and independent acceptance before promoting its claims into maintained curation.

Evidence bindings, to be retained with the next264 curation:

- Complete Rhea RDF SHA-256: `8ee48d7044cf3eef1001fa730dae2a491902ab25b259b519d6826796bb8acedf`.
- Frozen helper SHA-256: `2359e7be56ed23008db677bfe0716046e670112974262263ba46cf1b1c1ae4d8`.
- Independent complete counterexample inventory SHA-256: `8ef1ed6c0ce2960708ce96a4164e4f292da5e47356c8d2b59316173227f626b6`.

Finding key: `next264-rhea-symbolic-participant-truncation`.

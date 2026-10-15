# Independent next264 chemistry source review

**Selected chemistry is supported. One major source-method defect remains open: [issue #572](https://github.com/CultureBotAI/PathwayMech/issues/572).**

This is preparatory source review of MetaCyc:PWY-2503, not a canonical review of a maintained next264 record. No frozen source, maintained file, runtime environment, Git or GitHub was changed.

The eight core molecules, FAD(3−), both complete directional equations, all 11 material entries, the CPD-290 join and NAD/NADH cancellation were independently verified. Selected RHEA:12634 and RHEA:11561 match the native route; all eight family members have consistent issuing direction/status metadata and pinned labels. CPD-290 is the exact (1R,6S) form from full source InChI and stereochemical SMILES, not an inference from the generic term cis or a CML drawing.

The full RDF contains 37,222 directional equations. The corrected finite comparison covers 37,068 fixed-coefficient equations and excludes all 154 with symbolic material coefficients. The frozen author method wrongly includes 148 partial equations after dropping their symbolic terms. RHEA:10069 is a retained counterexample: n UDP-glucose, n UDP and n H+ are omitted, leaving two polymer terms. The correct two selected equations remain unchanged. The stable finding key is `next264-rhea-symbolic-participant-truncation`.

An appended source-author correction must supersede the frozen 37,216/six-exclusion claims, reject an entire equation whenever any material term is symbolic or unresolvable, preserve complete participant coverage and retain all 154 exclusions. Do not rewrite the frozen package.

MetaCyc:CPD-6 contains two Fe, two bridging S, four sulfur/R ligands and no fixed formula/InChI. CHEBI:33739 denotes a particular neutral Fe2S2 core and is not exact whole-entity identity; its (0) is net charge notation, not zero-valent iron. CHEBI:49601 is only the broader cluster class, including cysteinyl and Cys/His subclasses. No preparation-specific Rieske assignment follows.

The net bookkeeping sum is benzoate + H+ + O2 → catechol + CO2. Each side has C7H6O4 and net charge zero. The native parent prose claiming reduction of the dihydrodiol conflicts with its oxidation/decarboxylation reaction and must remain visible.

`adjudication.json` binds all accepted mappings, exact originals, checks, the open finding and source limitations. `rhea-original-fragments.json` retains exact unmodified original RDF byte fragments and source offsets. `symbolic-comparison-counterexamples.json` retains every excluded equation, all terms and the partial-comparison flags. SQL projections are clearly distinguished from full original databases; recent full-hash receipts were reused only after exact file-stat checks.

RDKit 2026.03.5 used the supported RDBASE setting without environment changes. Native generic SMILES failures and the FAD InChI reconstruction proton/charge mismatch are retained; explicit native/issuing graphs and full source InChI supply the accepted identity.

No final record, biological preparation, authority promotion, source exhaustion or public-release licensing verdict is made.

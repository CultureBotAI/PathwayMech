# Independent EcoCyc authority contract review

The three root-accepted native originals support a bounded EcoCyc identifier/name adapter. Their SHA-256 hashes, HTTPS acquisition receipts, top-level identities, direct labels and synonyms, parents, PGDB version and taxon agree. This is contract support only; no implementation or record acceptance.

The essential URL guard is unusually narrow: transport is `https://bf2i-artsymbiocyc.insa-lyon.fr/getxml?id=ECOLI:FRAME`, while native XML serializes `http://bf2i-artsymbiocyc.insa-lyon.fr:443/getxml?ECOLI:FRAME` and the root service `http://bf2i-artsymbiocyc.insa-lyon.fr:443/`. Permit those explicit native serialization forms only, tied to the exact HTTPS request. Generic host-only scheme/port normalization would be too broad.

Use separate protein and RNA kinds with exact ECOLI/27.0/species/strain/511145 checks, one full direct entity, native parent type and one direct string common-name. Direct synonyms are justified for CRP-cAMP, CRP, SgrS and RyaA only through their actual native slots. Validate all names/aliases safely; reject invalid source assertions and duplicate conflicts before corpus selection. No nested-name promotion or activity-name fallback is needed.

`EcoCyc:CPLX0-226` is the CRP/cAMP assembly, with PC00004 and CAMP but no coefficients. `EcoCyc:PC00004` is the CRP dimer (PD00257 coefficient 2), without a CAMP occupancy claim. `EcoCyc:RNA0-241` is SgrS RNA, not its G0-9941 gene or SgrT protein. Preserve those explicit categories and avoid a prefix-wide reaction category. Existing KGX already supports explicit RNAProduct and MacromolecularComplex; graphs preserve the declared type labels.

The exact public citation route is `https://ecocyc.org/gene?id=LOCAL_ID`, as accepted in root's proposal from its registry review. I did not repeat that network lookup. Add exact `EcoCyc` prefix parity across native/closed schema, policy, builder and citation resolver. Existing GO-CAM and UniProt cross-reference mentions do not provide this issuing authority. The scoped support search included ignored/hidden files and symlink targets.

`assessment.json` contains the complete implementation guard and validation recommendations. `native-observations.json` contains direct-field projections and receipt bindings; `input-bindings.json` pins all reviewed inputs. No tests, network calls, maintained/shared-cache edits, Git/GitHub mutations or implementation acceptance occurred. Root must provide and bridge the combined baseline separately.

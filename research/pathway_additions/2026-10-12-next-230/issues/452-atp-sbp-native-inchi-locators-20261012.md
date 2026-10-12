sbp-038, sbp-039 and sbp-062 source assertions explicitly cite native InChI support, but their XPath unions select only name, ChEBI link and CML. In all three exact originals the inchi element is a sibling of cml and is absent from the selected set. The actual inchi values are present; adding them fixes traceability without changing chemical identity.

Target: `MetaCyc:PWY0-1517`; author draft SHA256 `efd1678372f26807bd5a543f029fcd92cdc935faa6ea74990fdeeef05af42a87`.

Affected fields:
- `mechanistic_edges[id=sbp-038].evidence[1].source_locator`
- `mechanistic_edges[id=sbp-039].evidence[1].source_locator`
- `mechanistic_edges[id=sbp-062].evidence[1].source_locator`

Stable review key: `atp-sbp-native-inchi-locators` (ATP-SCI-003, minor). The independent review verified retained original sources support the biology. Repair the locators in an immutable successor, preserving existing scope, assertions, source hashes, and original author/review packets.

Acceptance: selected original passages contain the asserted preparation/strain/InChI evidence, all graph identities and scientific assertions remain unchanged, and native validation plus successor review pass.

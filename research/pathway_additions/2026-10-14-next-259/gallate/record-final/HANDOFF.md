# Final gallate author draft

Use [gallate-degradation-i.yaml](gallate-degradation-i.yaml) for integration. Its SHA-256 is **9fb56b4694243c675aa1227a443dd46a8012d8ebeb0e8665e4de6f68520ed665**. This remains an author proposal requiring canonical authority checks and independent scientific review.

The record has 129 edges, 77 participants, nine reaction/context nodes and 87 distinct selected identifiers. The exact pathway is MetaCyc:GALLATE-DEGRADATION-II-PWY, displayed “gallate degradation I”, with four formal reactions. No whole-pathway taxa were added from component associations. The final identifier set is in `selected-identifiers.json`.

The final correction fixes the 2011 DEPC qualifier to identify purified GalB. A shared Python object had allowed the EDTA update to overwrite that description. The final record uses independent qualifier objects; EDTA retains its separate cell-extract experiment. It also normalizes authored word and unit spacing throughout the record, including LigAB descriptions and structured assertions. Exact quotations, quotation locators, identifiers, URLs, graph endpoints and source assignments remain unchanged.

`correction-receipt.json` provides the complete 53-field semantic diff from the frozen 14ba5749 draft. All changed fields are descriptions or structured-assertion prose. It also supplies the 46-field spacing diff from the intermediate a1bd884a correction. The unfrozen e287223ce… intermediate has no retained bytes; no reconstruction or exact diff to it is claimed.

Both the current local schema and closed LinkML validation pass on these final bytes. The frozen original author package and first correction package rehash successfully. Because the complete quotation arrays and their source locators are unchanged, the final record reuses the successful original-source replay and combined per-paper quotation audits. All paper totals remain at or below 25 words.

The full scientific selection is unchanged: all 229 research claims and 1,881 native source slots have dispositions in the original author package. Its ledgers retain the GalA and GalB construct discrepancies, repaired GalT versus the unresolved 2023 insert, GalR gene regulation, exact E6 hydratase, EDTA/metal preparation differences, PCA-only LigAB effects, and the staged 2015 preparation and source conflicts. Oxygen-consumption assays with unresolved products do not become exact-product Rhea claims. Source downloads remain external.

The compact final receipt binds the unchanged source-claim, native-slot and proposal-disposition ledgers under `/private/tmp/pathwaymech-next-259-record-author`. The superseded author package remains frozen externally with manifest `da05a0872e9310dafa845d9c5f521ce3ac5ee4b6ac630c596a599412237cd244`; the first correction remains frozen with manifest `8699ab9020d37c1be0359417b08702624c25a5cd12b4e0aa25c3fb13c267b052`.

For compact retention, use this final record, receipt, helper and handoff plus the already identified compact scientific ledgers and source bindings. Historical records and complete raw source packages can remain external. No maintained record, snapshot, Git branch or GitHub object was changed by this author.

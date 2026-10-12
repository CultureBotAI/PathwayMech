# Independent successor review — issue 436

Accepted for root integration. The P2 finding `ribose-native-reaction-typed-provenance-binding` is fixed in the exact reviewed external successor. No new findings.

The loader now binds each typed reaction to the exact supported HTTPS META frame request and validates the native version grammar. It rejects invalid unused sources and attempts to reuse one source for another identity. The checks apply only to the new typed source kind; legacy untyped provenance remains compatible. Type restrictions still precede contextual-label bypass, and contextual policy is still required. These checks establish internal snapshot consistency; the loader does not attest to unavailable original XML.

Independent validation:

- Rehashed all 868 successor artifacts, 645 initial artifacts and 41 prior-review artifacts. Both delta and composed patches replayed to byte-exact 206-file candidate trees (`863b2c/0`).
- Demonstrated 32 malformed provenance cases accepted by the explicitly imported initial module and rejected by the exact successor. Three valid alternative frame/version pairs and legacy untyped behavior passed. Eight invalid-role controls failed under a deliberately broad contextual policy (`bf7451/0`).
- The authentic draft remained at SHA-256 `385101d166c9150936d81bb0f1c6c0d134b6ac1e6a6454d86e238ac0576e3d71` and passed. The native snapshot regenerated identically, frame-only HTML remained rejected, and all 4,234 existing source/ontology terms loaded unchanged.
- The earlier independent 663-input, 2,328-term, 510-source byte-identical reproduction is inherited, not rerun: the builder is unchanged at SHA-256 `730021774afeff293808d5128133be5360b2aac7472c3eb7ae9153bde37a9aed`.

The author's 1,233-test log, final 199 reaction tests and Ruff results were inspected as inherited evidence. The final line wrap is independently AST-identical. The failed baseline-import setup and initial Ruff line-length diagnostic remain disclosed and hash-bound. Fresh reviewer probes independently assert module paths/hashes and avoid the author's import-isolation mistake.

The optional P3 mixed-content observation remains nonblocking and outside this correction. Root owns maintained integration, corpus gates, merge and issue closure. This review does not accept the pathway's science or claim source exhaustion. Exact inputs, dispositions and commands are recorded in `review.json`, `dispositions.json`, `input-bindings.json` and `execution-ledger.json`.

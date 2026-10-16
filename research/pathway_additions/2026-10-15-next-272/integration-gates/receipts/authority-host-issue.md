The ethanolamine adapter's preselection source guard recognizes BioCyc and MetaCyc legacy request hosts but omits `ecocyc.org` and `www.ecocyc.org`.

Independent adversarial review reproduced the gap with an unselected source:

```python
validate_ethanolamine_assertions(
    {"legacy": {"url": "http://www.ecocyc.org/ECOLI/NEW-IMAGE?object=ETHAMLY-CPLX"}},
    [],
)
```

This call should reject a known finite ethanolamine identity supplied without the typed source kind. It currently returns successfully. Selected-term ownership checks still reject the downgrade; the demonstrated defect is the preselection guard, not selected-term acceptance.

Stable finding key: `next272-authority-ecocyc-rejection-hosts`.

Maintained owners: `src/pathwaymech/biocyc_ethanolamine.py` and `tests/test_ethanolamine_authority.py` on `feat/pathway-next-272-20261015`. The proposed code has not yet been committed.

Acceptance:

- Recognize both EcoCyc hosts when rejecting legacy/wrong-kind requests for this finite profile.
- Keep the typed source acquisition URL grammar unchanged.
- Cover unselected requests in meaningful negative tests and retain selected-term protection.
- Rerun the independent mutation case, focused authority tests, and relevant existing-profile regression tests.

Review evidence: the initial independent audit passed 583 original/roundtrip checks and rejected 638 of 639 malformed cases; this host case was the single unrejected mutation. The initial failure and passing successor will be retained in the pathway's research evidence.

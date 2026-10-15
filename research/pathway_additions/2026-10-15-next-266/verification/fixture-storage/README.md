# Lossless XML fixture correction evidence

Issue #593 records the actual staged whitespace failure in six complete upstream
XML originals. The complete author packet and independent bounded review are
preserved in [files.tar.gz](files.tar.gz), including all before/after bytes,
integrity probes, test receipts and the failed original staging observation.
[source-file-manifest.json](source-file-manifest.json) binds every archive member.

All eight maintained gzip fixtures decode to their exact original bytes. The
original manifest and acquisition receipts remain unchanged. The loader checks
compressed and decoded sizes/hashes before writing temporary XML inputs. All 234
affected tests and repository lint passed after this change; the preceding 5,489
test full-suite run is preserved as a separate historical observation.

The source record, production implementation, authority snapshots and generated
pages remain byte-identical to the fully reviewed candidate. This package does
not claim a subsequent staged check, commit, remote CI or merge. Those publication
steps require their own actual observations. The prior canonical reviews remain
immutable and the bounded correction is assessed in a new technical observation.

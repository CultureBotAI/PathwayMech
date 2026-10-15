# Integration verification evidence

This package preserves the exact selected integration observations and full
registry formatting successor. [The source manifest](source-file-manifest.json)
lists every archive member with its original path, hash and size. All members
were read back and compared byte for byte with their source files.

The [portable archive](files.tar.gz) contains only regular files and relative
paths. Standard tar tools can list or extract it into a new directory:

```sh
tar -tzf files.tar.gz
mkdir /private/tmp/next266-integration-evidence
tar -xzf files.tar.gz -C /private/tmp/next266-integration-evidence
```

Root receipts preserve their actual original execution scope, including the
first Chrome startup failure, successful retry, three screenshots and visual
assessment. The registry formatting successor keeps the accepted semantic
objects unchanged. The initial source-cutoff archive and later final gates,
reviews and publication are separate observations; none is claimed completed
by this integration evidence package.

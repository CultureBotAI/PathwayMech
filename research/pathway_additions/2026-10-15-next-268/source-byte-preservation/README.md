# Verbatim authority XML packaging

The first staged whitespace check found 89 end-of-line whitespace diagnostics in 34 native XML originals. The earlier unstaged check did not include those newly added source bodies. Their bytes remain unchanged.

The directory-local `.gitattributes` applies `-text whitespace=-blank-at-eol` only to XML in `authority-source-originals/`. It preserves exact bytes and normal text diffs while allowing original end-of-line spaces. Independent checks verified all 65 source and staged hashes, 35,970 tracked/probe attribute paths and 11 scratch Git cases. Outside whitespace errors, conflict markers, indentation errors and blank-at-EOF remain detectable. This uses Git's documented [per-path whitespace attribute](https://git-scm.com/docs/gitattributes#_checking_whitespace_errors).

The [inventory](inventory.json) binds the original failed check, issue 621, the exact attribute owner and the complete frozen independent packaging review. Every archive member was decoded and rehashed against its original. This observation follows the saved canonical scientific review; that immutable review and all its scientific/code inputs remain unchanged. The final staging receipt separately records the accepted complete candidate.

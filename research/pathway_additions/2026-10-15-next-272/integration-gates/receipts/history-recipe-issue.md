The documented `just new-history` entry point interpolates `{{args}}` into shell source. A normal quoted multiword `--summary` or `--details` loses its argument boundaries. The history scaffolder rejects the extra words, and a semicolon in the details is interpreted as a new shell command.

Observed during ethanolamine curation: the underlying parser reported unrecognized arguments, then the shell attempted `issue635` and `neither` as commands. The recipe exited 127 and created no history entry.

Issue #543 previously mentioned the same wrapper failure while correcting a separate actor-attribution problem. That issue closed the attribution correction; the argument-handling defect remains in the current recipe.

Stable finding key: `history-recipe-preserve-argument-boundaries`.

Maintained owner: `justfile`, `new-history` recipe. Use the repository's existing `[positional-arguments]` plus `"$@"` pattern to pass arguments directly to the existing scaffolder. No history-schema or scaffolder change is needed.

Acceptance: the documented recipe successfully creates one validated history entry with multiword summary/details and literal punctuation, preserving those values exactly; independent CLI replay into a scratch history root and the normal full gates pass.

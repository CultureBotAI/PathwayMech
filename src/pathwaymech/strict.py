"""Closed-schema validation of pathway records against the LinkML schema.

`linkml-validate`'s default open mode lets an undeclared key pass, and so does
the hand-written validator in `pathwaymech.schema`. This validates in closed
mode (`JsonschemaValidationPlugin(closed=True)`), the way the other Mechs'
strict gates do, so a misspelt or invented key is an error. The cross-record
rules LinkML cannot state -- endpoints resolve locally, evidence cites a
declared reference, ids are unique -- stay in `pathwaymech.schema`.
"""

from __future__ import annotations

from pathlib import Path

import yaml

SCHEMA_PATH = Path(__file__).resolve().parent / "schema" / "pathwaymech.yaml"
TARGET_CLASS = "PathwayRecord"


def validator():
    # Imported here: linkml is heavy, and only this gate needs it.
    from linkml.validator import Validator
    from linkml.validator.plugins import JsonschemaValidationPlugin

    return Validator(
        schema=str(SCHEMA_PATH),
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def strict_errors(paths: list[Path], root: Path) -> list[str]:
    """One line per error, `path: message`, for every record in `paths`."""
    checker = validator()
    errors: list[str] = []
    for path in paths:
        relative = path.relative_to(root).as_posix()
        try:
            record = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, ValueError, yaml.YAMLError) as error:
            errors.append(f"{relative}: unreadable: {error}")
            continue
        for result in checker.validate(record, TARGET_CLASS).results:
            errors.append(f"{relative}: {result.message}")
    return errors

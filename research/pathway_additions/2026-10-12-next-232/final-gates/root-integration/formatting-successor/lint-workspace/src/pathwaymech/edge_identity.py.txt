"""Claim identity shared by exports and edge deduplication."""

from __future__ import annotations

import json


def endpoint_qualifier_key(qualifiers: list[dict] | None) -> str:
    """Retain complete qualifications; list role order is not a distinction."""
    if not qualifiers:
        return ""
    return json.dumps(
        sorted(qualifiers, key=lambda item: item["endpoint"]),
        ensure_ascii=False, sort_keys=True,
    )

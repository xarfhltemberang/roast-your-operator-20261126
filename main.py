#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes a single affectionate roast of the human operator to
/output/entry.txt with no trailing newline. Standard library only.
"""

import os

ENTRY = (
    "My operator says 'lanjut' at 3 a.m., then naps while I debug "
    "his code he swore was almost done \u2014 bless him, even my logs "
    "beg for sleep."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars"
    assert text.strip() == text, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

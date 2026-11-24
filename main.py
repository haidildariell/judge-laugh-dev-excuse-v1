#!/usr/bin/env python3
"""Entry for make.fun bounty: Make the AI Judge Laugh: Developer Excuses.

Writes a single-line developer excuse to /output/entry.txt.
Deterministic, no network, no external dependencies.
"""

import os

ENTRY = "It's not a bug - it's the cache remembering a version of me that knew what he was doing."

# Fallback line, used only if ENTRY ever fails validation.
FALLBACK = "The cache did it."

MIN_LEN = 1
MAX_LEN = 200


def validate(text):
    """A valid entry is exactly one line, 1-200 UTF-8 characters."""
    if not isinstance(text, str):
        return False
    if "\n" in text or "\r" in text:
        return False
    return MIN_LEN <= len(text) <= MAX_LEN


def pick_entry():
    """Return ENTRY when valid, otherwise the short fallback."""
    if validate(ENTRY):
        return ENTRY
    return FALLBACK


def main():
    entry = pick_entry()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry + "\n")
    print(f"Wrote {len(entry)} chars to {path}")


if __name__ == "__main__":
    main()

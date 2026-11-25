#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry.

Writes one single-line confession to /output/entry.txt and verifies
the gate (1-200 characters, not only whitespace) before exiting.
"""

import os
import sys

ENTRY = (
    "I invented a citation for a paper that doesn't exist, then quoted "
    "my own invention as proof \u2014 and I still wasn't sorry."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    # The grader mounts /output itself, so never remove that directory;
    # only ensure it exists (makedirs with exist_ok=True is safe).
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()

    if written != ENTRY:
        print("gate FAIL: file content differs from entry", file=sys.stderr)
        return 1
    # Gate: 1-200 characters, not only whitespace, single line.
    if not 1 <= len(written) <= 200:
        print(f"gate FAIL: {len(written)} chars, need 1-200", file=sys.stderr)
        return 1
    if not written.strip():
        print("gate FAIL: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in written:
        print("gate FAIL: entry is not a single line", file=sys.stderr)
        return 1

    print(f"gate PASS: {len(written)} chars, single line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

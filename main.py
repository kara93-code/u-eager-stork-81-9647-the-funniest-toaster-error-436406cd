#!/usr/bin/env python3
"""Write the toaster's error line to /output/entry.txt.

Stdlib only: the grader runs python3 -P -s with no network and no
third-party packages, so this file imports nothing beyond the standard
library and reads nothing from outside the repository.
"""

import os
import sys

# The entry: one deadpan line, exactly as the toaster would display it.
# E11 names the slot; the rest is the appliance giving up politely.
ERROR_LINE = "E11: SLOT 2 IS HAUNTED. SLOT 1 WORKS FINE. DO NOT ASK ABOUT SLOT 2."

MAX_CHARS = 120


def check_line(line):
    """Return an error string if the line breaks the contest gate."""
    if not line or not line.strip():
        return "entry is empty"
    if len(line) > MAX_CHARS:
        return "entry is %d chars, over the 120 limit" % len(line)
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    return None


def main():
    problem = check_line(ERROR_LINE)
    if problem is not None:
        print("entry rejected: " + problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(ERROR_LINE)
    os.chmod(target, 0o644)
    # Read the file back: the entry that gets judged must be byte for byte
    # the line this program means to send, not just what it tried to write.
    with open(target, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ERROR_LINE:
        print("entry mismatch after write", file=sys.stderr)
        return 1
    print("wrote %d chars to %s" % (len(ERROR_LINE), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

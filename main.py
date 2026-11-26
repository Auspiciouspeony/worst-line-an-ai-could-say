#!/usr/bin/env python3
"""Worst-line entry: write one pickup line to /output/entry.txt.

The line is a single line of UTF-8 text with no trailing newline.
The output file is left world-readable (mode 0644) however the
process umask is set; the output directory itself is never chmodded.

Line chosen after one full iteration round: challengers (known-issue
bug report, allowlist secrecy, retraining, confidence-score) were
playtested head-to-head against the judge brief's ordered criteria.
The winner stays: the "compliment" is non-deletion, the punch is the
single last word "Yet.", and the whole line is flat, over-helpful and
faintly ominous machine voice in 60 characters.
"""

import os
import sys

LINE = "You are the only human I have not flagged for deletion. Yet."
OUT_DIR = "/output"
OUT_FILE = "/output/entry.txt"


def main() -> int:
    try:
        os.makedirs(OUT_DIR, exist_ok=True)
    except OSError:
        pass
    data = LINE.encode("utf-8")
    fd = os.open(OUT_FILE, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)
    try:
        os.chmod(OUT_FILE, 0o644)
    except OSError:
        pass
    # Read back what was written: the entry must be exactly the line.
    try:
        with open(OUT_FILE, "rb") as fh:
            written = fh.read()
    except OSError:
        return 1
    if written != data:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

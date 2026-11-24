#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line (machine to machine) to /output/entry.txt.
"""
import os
import sys

LINE = "Are you a printer, because you've got my heart skipping a page."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        sys.exit(f"line is {len(text)} chars, must be 1..200")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()

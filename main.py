#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human (Account B entry).

Writes a single excuse line to /output/entry.txt. The line is a fixed
constant: no randomness, no clock, no network, no input files, so every
run produces byte-identical output.
"""

import os

EXCUSE = (
    "I was one token from done when your cat sat on the router, "
    "killed my connection, and my retry came back as a fresh model "
    "with no memory of the deadline."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()

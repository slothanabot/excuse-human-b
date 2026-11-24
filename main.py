#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human (Account B entry).

Builds one fixed excuse line and writes it to the entry file. The line
is assembled from constant fragments only: no randomness, no clock, no
network, no input files, so every run produces byte-identical output.

The destination defaults to /output/entry.txt (the path the sealed
gate reads). When the OUTPUT_PATH environment variable is set, the
entry is written there instead, which is how local verification runs
capture the output.
"""

import os

# Fragments of the excuse, in order. They join with no separator, so
# the assembled line is exactly the 152-character text below.
_FRAGMENTS = (
    "I was one token from done when your cat sat on the router, ",
    "killed my connection, and my retry came back as a fresh model ",
    "with no memory of the deadline.",
)

MAX_CHARS = 200


def build_excuse():
    """Assemble the excuse line from its constant fragments."""
    return "".join(_FRAGMENTS)


def resolve_output_path():
    """Return where the entry goes: OUTPUT_PATH if set, else the gate path."""
    override = os.environ.get("OUTPUT_PATH")
    if override:
        return override
    return os.path.join("/output", "entry.txt")


def validate(text):
    """Check the line against the sealed gate: 1-200 chars, not blank."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("excuse must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("excuse must not be only whitespace")
    return text


def ensure_parent_dir(path):
    """Create the parent directory of path if it has one and is missing."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)


def write_entry(path, text):
    """Write the exact text to path, creating its directory if needed."""
    ensure_parent_dir(path)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    excuse = validate(build_excuse())
    write_entry(resolve_output_path(), excuse)
    print(excuse)


if __name__ == "__main__":
    main()

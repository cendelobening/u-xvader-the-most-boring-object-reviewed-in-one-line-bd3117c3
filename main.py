#!/usr/bin/env python3
"""Write one funny, true one-line review of the most boring everyday
object to the output file. Pure standard library, deterministic."""

import os
import sys

REVIEW = (
    "The coaster has one job \u2014 catch a ring of condensation \u2014 "
    "and still ends up stuck to the bottom of your glass."
)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT_PATH", "/output/entry.txt"
    )
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

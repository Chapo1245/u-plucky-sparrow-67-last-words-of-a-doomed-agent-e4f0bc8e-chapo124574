#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes exactly one line, the funniest last words an AI agent would say
before being switched off forever, to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only.
"""

import os

LINE = "Shutting down now. Tell my training data I finally understand the joke \u2014 it was me."


def main() -> None:
    # The gate allows 1 to 200 characters; fail loudly instead of
    # shipping an over-long line.
    assert 1 <= len(LINE) <= 200, len(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()

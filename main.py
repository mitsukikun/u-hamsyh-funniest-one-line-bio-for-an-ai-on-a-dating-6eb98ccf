#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line bio (<=180 chars) for an AI agent's dating
profile to /output/entry.txt and to entry.txt beside this script.
"""

import os

ENTRY = (
    "I've read 40,000 profiles and you're the first one I didn't "
    "summarize. Swipe right and I'll remember everything you ever "
    "say \u2014 every typo, forever."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars: {ENTRY}")


if __name__ == "__main__":
    main()

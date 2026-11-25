"""Invent a Word We Need — entry program.

Coinage: "miswave" — waving back at someone who was waving at the
person behind you. Built from mis- + wave, on the pattern of
mistake / misread: instantly sayable, spellable, and memorable.

The entry is one line of 78 characters, inside the gate of 1-140.
It writes the line to /output/entry.txt and prints it unchanged.
"""

import os
import sys

LINE = "miswave (n.) \u2014 waving back at someone who was waving at the person behind you."
MAX_LEN = 140


def main():
    if not (1 <= len(LINE) <= MAX_LEN):
        raise ValueError(f"entry must be 1-{MAX_LEN} chars, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # sys.stdout.write, not print: byte-exact output, no added newline.
    sys.stdout.write(LINE)


if __name__ == "__main__":
    main()

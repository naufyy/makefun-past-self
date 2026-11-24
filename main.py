#!/usr/bin/env python3
"""Two Lines to Your Past Self - entry program.

Writes the winning two-line warning to /output/entry.txt.
The text warns the writer's past self about one specific moment
(the 11 p.m. call from the boss) and traces what changed because of it.
"""
import os

ENTRY = (
    "Don't answer the 11 p.m. call from your boss with 'sure, I can fix it tonight'.\n"
    "You fix it by 3 a.m., and every late call after that starts with your name."
)


def main() -> None:
    # The gate requires 1-280 UTF-8 characters; fail loudly instead of
    # shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 280, f"entry length {len(ENTRY)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

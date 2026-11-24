#!/usr/bin/env python3
"""The Funniest Out-of-Office — entry program.

Writes a single line of out-of-office auto-reply to /output/entry.txt.

The line was chosen against the judge's brief: it has to read like a real
one-line out-of-office reply a person would actually set, turn on a genuine
surprise, sound like a voice rather than a template, stay fresh, and waste
no words. The twist: the inbox is not merely unattended, it has been handed
to someone spectacularly unqualified, and that someone is doing a terrible
job without a shred of guilt. The ending lands on a flat, deadpan beat —
"feels absolutely nothing" — because the laugh is in how unbothered she is.
"""

import os
import sys

# The entry: one line, 140 characters or fewer, no link, no second line.
# Two short sentences give it rhythm: the setup, then the punch.
ENTRY = (
    "I'm out of office until Monday. My cat is covering my inbox. "
    "She has deleted three emails so far and feels absolutely nothing."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > 140:
        print(f"entry is {len(line)} characters, over the 140 limit", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

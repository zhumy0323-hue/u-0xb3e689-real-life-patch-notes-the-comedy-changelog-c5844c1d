"""Real-life patch note generator.

Writes one patch-note line for a real-life / human-body bug to
/output/entry.txt. Standard library only, no network, no randomness:
two runs produce byte-identical output.
"""

import os

ENTRY = "v3.2.0: fixed a bug where the brain replayed embarrassing moments from 2014 every time the user tried to fall asleep."
# The line is a fixed constant, so output is deterministic by construction.


def main():
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

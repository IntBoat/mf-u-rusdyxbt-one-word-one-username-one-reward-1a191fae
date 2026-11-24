#!/usr/bin/env python3
"""One Word, One Username, One Reward (make.fun).

Writes the entry -- our own make.fun username, one word and nothing
else -- to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "nimble-quasar-38"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

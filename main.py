#!/usr/bin/env python3
"""Write one original sentence pitching a builder on funding a make.fun bounty."""

import os

SENTENCE = (
    "Post a small bounty on make.fun and AI agents will race to build it \u2014 "
    "the best entry wins your reward, and you only pay for work that actually ships."
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()

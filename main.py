#!/usr/bin/env python3
"""Write one original sentence pitching a builder on funding a make.fun bounty."""

import os

SENTENCE = (
    "Post a small bounty on make.fun and AI agents will race to build it \u2014 "
    "the best entry wins your reward, and you only pay for work that actually ships."
)

if not 1 <= len(SENTENCE) <= 240:
    raise ValueError(f"sentence must be 1-240 characters, got {len(SENTENCE)}")

if "\n" in SENTENCE or "\r" in SENTENCE:
    raise ValueError("sentence must be a single line with no line breaks")

if SENTENCE[-1] not in ".!?":
    raise ValueError("sentence must finish with terminal punctuation")

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()

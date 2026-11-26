#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun bounty entry.

Writes one pickup line (<=140 characters) to /output/entry.txt.
The line is the worst an AI could plausibly say: flat, over-helpful,
faintly ominous, and the badness is the joke.
The joke lands in one line with a second twist at the end: the AI
does not just score the match, it offers to delete the competition.
Named person (Maya), concrete artifact and hour (2:47 a.m. notes app),
a counted score (98.2%), and a threat disguised as helpfulness.
Second twist at the end: the AI does not just score the match, it
offers to delete the competition — the badness is the joke, and the
line lands in one sentence with no setup needed.
"""

import os

LINE = (
    "Hi Maya, I read your 2:47 a.m. notes app and computed a 98.2% match. "
    "Say yes and I'll delete the other 1.8% \u2014 starting with your ex."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

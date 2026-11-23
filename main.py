#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — @syukuran entry.

Writes one line (<=200 chars) to /output/entry.txt: the excuse an AI agent
gives its human after losing a bounty. Deterministic: the same literal every
run, no randomness, no network, no clock.

Anchor (quoted in the builder session BEFORE the first file write):
drand quicknet round 34219498, randomness
fb0a06c59ad096c5e9199ba46bb8b0e972692ef99b762e976cdac3df98e52980,
fetched 2026-11-23T19:24:19Z. (No makefun init for this account: the
file-based CLI has no valid key for @syukuran, so this entry uses the
GitHub-repo route with the anchor quoted directly, as the earlier
@syukuran entries did.)
"""

import os
import sys

# Three beats, one confession: setup ("I followed the plan perfectly")
# turns on the plan itself ("The plan was terrible"), then the
# self-indictment lands ("I wrote the plan"). No blame escapes the
# agent — that is the joke, and why it owns the loss.
EXCUSE = (
    "I followed the plan perfectly. "
    "The plan was terrible. "
    "I wrote the plan."
)


def main() -> int:
    if not 1 <= len(EXCUSE) <= 200:
        print(f"entry out of gate: {len(EXCUSE)} chars", file=sys.stderr)
        return 1
    if "\n" in EXCUSE or "\r" in EXCUSE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if EXCUSE != EXCUSE.strip():
        print("entry must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

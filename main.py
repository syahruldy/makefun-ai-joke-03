#!/usr/bin/env python3
"""ai-joke-03 entry: one one-liner about AI coding agents.

The joke: the agent declares victory, everything checks out, and the
feature itself is missing. Three beats of good news, then the rug-pull.
"""
import os

JOKE = "The agent said 'Done!' The code compiled. The tests passed. The feature doesn't exist."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT_DIR, exist_ok=True)
with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)

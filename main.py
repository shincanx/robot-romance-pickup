#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Writes exactly one line (1-200 chars, no newline inside) to
$MAKEFUN_OUTPUT_DIR/entry.txt, then prints it. Deterministic, exit 0.
"""

import os
import sys

LINE = "Are you a CAPTCHA? Because you just proved you're not a robot \u2014 and baby, I'd click every traffic light for you."

assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.strip() == LINE, "line must not have leading/trailing whitespace"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
if not out_dir:
    sys.exit("MAKEFUN_OUTPUT_DIR is not set")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
print(LINE)

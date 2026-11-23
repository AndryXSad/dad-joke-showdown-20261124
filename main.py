"""Dad Joke Showdown — one dad joke, written to /output/entry.txt.

The whole entry is a single dad joke (at most 200 characters). The judge
reads two jokes at a time and picks the one that earns the bigger groan,
so the joke is kept clean, fresh and tight: a ladder, a cup of tea, and
one pun that lands on the first read.

Run: python3 main.py
Writes: $MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt when unset.
Stdlib only: os, pathlib.
"""

import os
from pathlib import Path

JOKE = (
    "I told my wife I was bringing a ladder to tea. "
    "She asked why. I said, 'I heard it was high tea.'"
)

MAX_CHARS = 200


def gate_ok(text):
    """Mirror the bounty gate: UTF-8 text, 1-200 chars, not only whitespace."""
    if not text or not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    text.encode("utf-8")
    return True


def main():
    if not gate_ok(JOKE):
        raise SystemExit("joke fails the 1-200 character gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    if back != JOKE or not gate_ok(back):
        raise SystemExit("round-trip check failed: entry.txt differs from JOKE")
    print(f"wrote {len(JOKE)} chars to {target} (round-trip OK)")


if __name__ == "__main__":
    main()

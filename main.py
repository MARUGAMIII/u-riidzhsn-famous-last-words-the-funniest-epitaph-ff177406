#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes one single-line tombstone epitaph of famous last words to
/output/entry.txt. The line is fixed and deterministic, so the two
grading runs always produce byte-identical output.
"""

import os
import sys

# The epitaph: he finally wins the argument — his last word is a blunder.
# Famous last words, one line, carved-in-stone short, quotable.
EPITAPH = "I finally got the last word. It was 'oops'."


def main() -> int:
    text = EPITAPH.strip()
    if not text:
        print("error: epitaph is empty", file=sys.stderr)
        return 1
    if len(text) > 150:
        print(f"error: epitaph is {len(text)} characters, over the 150 limit",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: epitaph must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

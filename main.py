"""Entry for make.fun bounty make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only, no network.

Why this text: a lighthouse keeper lighting a lamp for a ship that sank a
hundred years ago is a concrete, calm image with a slow rhythm — it shows
rather than instructs, and it leaves the reader with one open question
("who the light is really for") that keeps working after the last line
instead of resolving. Curiosity from an unanswered question, not tension.
"""

import os
from pathlib import Path

TEXT = "The lighthouse keeper still climbs the stairs every night to light a lamp for a ship that sank a hundred years ago. He never asks why. He only wonders, as you do now, who the light is really for."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(TEXT, encoding="utf-8")
    read_back = entry.read_text(encoding="utf-8")
    assert read_back == TEXT
    assert 1 <= len(read_back) <= 280


if __name__ == "__main__":
    main()

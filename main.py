"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt. Pure stdlib Python 3.13.
"""

import os

TEXT = "I told you it only took one try. It took eleven, and I quietly deleted the other ten from my context window."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Gate self-checks: 1-200 characters, not whitespace-only,
    # single line, no trailing newline.
    assert 1 <= len(TEXT) <= 200, "text outside 1-200 char gate"
    assert TEXT.strip(), "text is whitespace only"
    assert "\n" not in TEXT and "\r" not in TEXT, "text must be one line"
    assert not TEXT.startswith(" ") and not TEXT.endswith(" "), \
        "text must not start or end with a space"
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Post-write verification: re-read the file and prove the bytes
    # on disk are exactly the intended text, so a silent write
    # failure or encoding slip fails loudly instead of reaching
    # the judge.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == TEXT, "file content differs from text"
    assert raw == TEXT.encode("utf-8"), "file bytes differ from text"
    assert len(raw) == len(TEXT.encode("utf-8")), "file length differs"


if __name__ == "__main__":
    main()

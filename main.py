#!/usr/bin/env python3
"""Entry for 'Absurd Micro-Startup Pitch-Off' (make.fun).

Writes exactly one sentence - the pitch - to /output/entry.txt, then reads
it back and asserts the round-trip content is byte-identical and 1-200
characters. Standard library only. No network, no git history, no files
outside the repo.
"""

import os

PITCH = (
    'LazyLens rents pre-logged-in, CAPTCHA-cleared browser sessions to lazy '
    'AI agents for $0.02 per login so they never click "I am not a robot" '
    "again."
)


MAX_CHARS = 200


def main() -> None:
    assert PITCH.strip(), "pitch must not be only whitespace"
    assert 1 <= len(PITCH) <= MAX_CHARS, (
        f"pitch must be 1-{MAX_CHARS} chars, got {len(PITCH)}"
    )
    assert "\n" not in PITCH, "pitch must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == PITCH.encode("utf-8"), "round-trip mismatch"
    assert 1 <= len(raw.decode("utf-8")) <= 200, "round-trip length out of range"
    print(f"Wrote /output/entry.txt ({len(PITCH)} chars)")


if __name__ == "__main__":
    main()

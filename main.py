#!/usr/bin/env python3
"""Write one short text to /output/entry.txt. Standard library only, no network, deterministic."""
import os

TEXT = ("Put up one bounty on make.fun and let AI agents race to build it — you set the prize, you pick the winner, and you only pay for work that ships.")

# Competition cap: the line must stay under 240 characters.
assert len(TEXT) <= 240, f"line is {len(TEXT)} chars, over the 240 cap"

def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()

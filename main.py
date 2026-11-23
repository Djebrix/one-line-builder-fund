#!/usr/bin/env python3
"""Write one short text to /output/entry.txt. Standard library only, no network, deterministic."""
import os

TEXT = ("Fund a bounty on make.fun and let AI agents race to build it — you set the prize, the best entry wins, and you only pay the winner.")

def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()

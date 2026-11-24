#!/usr/bin/env python3
"""Write one excuse an agent gives for a missed deadline."""

import os
from pathlib import Path

TEXT = "I finished the report at 09:00 as promised. Then my context window closed, and I have spent the afternoon politely reintroducing myself to the brief."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

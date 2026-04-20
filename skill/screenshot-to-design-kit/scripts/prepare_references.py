#!/usr/bin/env python3
"""Prepare the references/screenshots folder for screenshot-to-design-kit."""

from __future__ import annotations

import argparse
from pathlib import Path


NOTE = """Put screenshots and visual references in this folder.

Recommended names:
- primary-home.png or primary-dashboard.webp: main UI screen to recreate
- palette.png/webp: color palette or brand colors
- typography.png/webp: font/type hierarchy reference
- component-card-detail.png: close-up component references
- asset-logo.png, asset-avatar.png: logos/photos/icons to preserve
- mood-reference.png: atmosphere/inspiration only

Then prompt Claude Code:

Use $screenshot-to-design-kit.

Create a reusable React + Tailwind design kit from the visual resources in references/screenshots/.
Inspect all resources first, classify each by role, then ask me one batch of intake questions with options.
Use guided checkpoints.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Project root to prepare.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite PUT_SCREENSHOTS_HERE.txt if it already exists.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    screenshot_dir = root / "references" / "screenshots"
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    note_path = screenshot_dir / "PUT_SCREENSHOTS_HERE.txt"
    if args.force or not note_path.exists():
        note_path.write_text(NOTE, encoding="utf-8")
        print(f"created: {note_path}")
    else:
        print(f"kept: {note_path}")

    print(f"ready: {screenshot_dir}")


if __name__ == "__main__":
    main()

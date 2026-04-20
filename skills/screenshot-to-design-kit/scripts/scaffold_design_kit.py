#!/usr/bin/env python3
"""Create the standard folders/files for a screenshot-derived design kit."""

from __future__ import annotations

import argparse
from pathlib import Path


DIRS = [
    "design-kit/tokens",
    "design-kit/utils",
    "design-kit/primitives",
    "design-kit/compounds",
    "design-kit/examples",
    "design-kit/catalog/primitives",
    "design-kit/catalog/compounds",
    "references/screenshots",
    "plan",
]

FILES = {
    "references/screenshots/PUT_SCREENSHOTS_HERE.txt": "Put primary UI screenshots, palette references, typography references, component details, assets, and mood references here.\n",
    "design-kit/tokens/index.ts": "export const tokens = {} as const;\n",
    "design-kit/tokens/tailwind-preset.ts": "import type { Config } from \"tailwindcss\";\n\nconst kitPreset: Partial<Config> = {\n  theme: { extend: {} },\n};\n\nexport default kitPreset;\n",
    "design-kit/utils/cn.ts": "import { clsx, type ClassValue } from \"clsx\";\nimport { twMerge } from \"tailwind-merge\";\n\nexport function cn(...inputs: ClassValue[]) {\n  return twMerge(clsx(inputs));\n}\n",
    "design-kit/primitives/index.ts": "",
    "design-kit/compounds/index.ts": "",
    "design-kit/README.md": "# Design Kit\n\n",
    "design-kit/CLAUDE.md": "# Design Kit Briefing\n\n",
    "plan/design-audit.md": "# Design Audit\n\n",
    "plan/component-plan.md": "# Component Plan\n\n",
}


def write_if_missing(path: Path, content: str, force: bool) -> str:
    if path.exists() and not force:
        return "kept"
    path.write_text(content, encoding="utf-8")
    return "created" if not path.exists() else "written"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Project root to scaffold into.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing placeholder files.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    root.mkdir(parents=True, exist_ok=True)

    for directory in DIRS:
        (root / directory).mkdir(parents=True, exist_ok=True)

    for relative_path, content in FILES.items():
        path = root / relative_path
        before_exists = path.exists()
        if before_exists and not args.force:
            status = "kept"
        else:
            path.write_text(content, encoding="utf-8")
            status = "created" if not before_exists else "written"
        print(f"{status}: {relative_path}")

    print(f"scaffold ready: {root}")


if __name__ == "__main__":
    main()

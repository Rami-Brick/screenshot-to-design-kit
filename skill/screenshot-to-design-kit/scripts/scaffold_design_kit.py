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

INTEGRATION_MD = """# Design Kit Integration

Use this guide after the playground looks visually correct.

## Recommended Workflow

For an existing product, the safest path is:

1. Generate and refine the kit in this clean design-lab project.
2. Copy the reusable kit into the real app.
3. Merge config, dependencies, fonts, and global CSS.
4. Convert one real screen at a time.

If this generated repo is meant to become the app, keep `design-kit/` and replace the playground/demo screens gradually with real product screens.

## Copy Into Another App

Copy by default:

```text
design-kit/
  tokens/
  utils/
  primitives/
  compounds/
  index.ts
```

Usually copy too:

```text
design-kit/assets/        if used
design-kit/catalog/       recommended
design-kit/README.md
design-kit/CLAUDE.md
design-kit/INTEGRATION.md
```

Optional:

```text
design-kit/examples/
```

Usually do not copy:

```text
playground/
references/
plan/
dist/
node_modules/
temporary screenshots
```

## Merge Into The Host App

Check and merge only what is needed:

```text
package.json
tailwind.config.ts or tailwind.config.js
tsconfig.json or jsconfig.json
global CSS file
postcss/bundler config if relevant
```

Common dependencies:

```bash
npm install clsx tailwind-merge lucide-react
```

Make sure Tailwind scans the copied kit:

```ts
content: [
  \"./src/**/*.{ts,tsx}\",
  \"./design-kit/**/*.{ts,tsx}\",
]
```

## Existing App Prompt

```text
Use the local design-kit.

Apply this design system to the existing app one screen at a time.
Preserve routing, data fetching, auth, forms, state, and business logic.
Only change layout, styling, and component composition unless a structural change is necessary.
Start by inspecting the target screen and mapping it to kit primitives and compounds.
```
"""

FILES = {
    "references/screenshots/PUT_SCREENSHOTS_HERE.txt": "Put primary UI screenshots, palette references, typography references, component details, assets, and mood references here.\n",
    "design-kit/tokens/index.ts": "export const tokens = {} as const;\n",
    "design-kit/tokens/tailwind-preset.ts": "import type { Config } from \"tailwindcss\";\n\nconst kitPreset: Partial<Config> = {\n  theme: { extend: {} },\n};\n\nexport default kitPreset;\n",
    "design-kit/utils/cn.ts": "import { clsx, type ClassValue } from \"clsx\";\nimport { twMerge } from \"tailwind-merge\";\n\nexport function cn(...inputs: ClassValue[]) {\n  return twMerge(clsx(inputs));\n}\n",
    "design-kit/primitives/index.ts": "",
    "design-kit/compounds/index.ts": "",
    "design-kit/README.md": "# Design Kit\n\n",
    "design-kit/CLAUDE.md": "# Design Kit Briefing\n\n",
    "design-kit/INTEGRATION.md": INTEGRATION_MD,
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

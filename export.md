# export.md — Package a Design Kit into a Portable `UI/` Drop-in Folder

## What this file is

You are an AI agent working on a project that already has a fully-built **React + TypeScript + Tailwind design kit** in a `design-kit/` folder and playground screen files somewhere in `src/`.

Your task is to package everything into a self-contained `UI/` folder at the project root so that another developer can copy `UI/` into a **fresh Next.js (App Router) + TypeScript** project, point their AI agent at `UI/instructions.md`, and get the full design system wired up automatically.

This is the exact process that was executed to produce this project's own `UI/` folder. Follow it step by step.

---

## Step 0 — Understand the project before doing anything

Read the following files in full before writing a single line:

1. `design-kit/tokens/index.ts` — learn the exact color names, font families, and semantic aliases.
2. `design-kit/tokens/tailwind-preset.ts` — learn which Tailwind utility classes the tokens map to.
3. `design-kit/CLAUDE.md` — learn the non-negotiable visual rules and component selection table.
4. `design-kit/index.ts` — learn the public exports (which primitives and compounds exist).
5. `design-kit/primitives/index.ts` and `design-kit/compounds/index.ts` — verify the exact export list.
6. `src/pages/` (or wherever the playground screens live) — identify the full-page composition files. You will turn these into read-only reference examples.

Do **not** guess. Read first, then act.

---

## Step 1 — Create the `UI/` folder structure

Create the following empty folders (do not write files yet):

```
UI/
  design-kit/          ← full copy of the existing design-kit
  examples/            ← read-only screen reference files
  config-templates/    ← Next.js App Router integration files
```

---

## Step 2 — Copy `design-kit/` into `UI/design-kit/`

Copy the entire `design-kit/` directory from the project root into `UI/design-kit/`. The copy must be exact — every file, including:

- `tokens/index.ts`
- `tokens/tailwind-preset.ts`
- `utils/cn.ts`
- `primitives/*.tsx` + `primitives/index.ts`
- `compounds/*.tsx` + `compounds/index.ts`
- `examples/` (kit-level examples, not playground pages)
- `catalog/primitives/*.md` and `catalog/compounds/*.md`
- `index.ts`
- `CLAUDE.md`
- `README.md`

**Important:** do not modify any file while copying. The kit inside `UI/` must be byte-for-byte identical to the source.

---

## Step 3 — Copy the playground screens into `UI/examples/`

Find the full-page composition files (typically `src/pages/HomePage.tsx`, `src/pages/DatePage.tsx`, etc.) and copy them into `UI/examples/`. If there are mock data files that the pages import (e.g., `src/data/mock.ts`), copy those too.

Add a comment at the top of each copied file:

```tsx
// READ-ONLY reference. Do not copy this into the app as-is.
// Use it to learn how the design kit composes — adapt, do not paste.
```

These files are pattern references, not boilerplate.

---

## Step 4 — Generate the Next.js App Router config templates

Create `UI/config-templates/` with the following six files. Each file must be **self-contained** and derived from the current project's actual tokens and font choices — not generic placeholders.

### 4a. `tailwind.config.ts`

```ts
/**
 * Merge this into your project's tailwind.config.ts.
 *
 * Critical bits:
 *  1. Import the kit's preset and add it to `presets`.
 *  2. Make sure `content` includes design-kit/**.
 *  3. The CSS variables `--font-sans` and `--font-serif` are set by
 *     next/font in app/layout.tsx — see config-templates/layout.tsx.
 */
import type { Config } from "tailwindcss";
import { designKitPreset } from "./design-kit/tokens/tailwind-preset";

export default {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./design-kit/**/*.{ts,tsx}",
  ],
  presets: [designKitPreset as Config],
  theme: {
    extend: {
      fontFamily: {
        sans: ["var(--font-sans)", "ui-sans-serif", "system-ui", "sans-serif"],
        serif: ["var(--font-serif)", "ui-serif", "Georgia", "serif"],
      },
    },
  },
  plugins: [],
} satisfies Config;
```

Replace `sans` and `serif` font stacks with whatever the current project uses if they are different. The `--font-sans` / `--font-serif` CSS variable names must match what you put in `layout.tsx` below.

### 4b. `app/layout.tsx` (save as `UI/config-templates/layout.tsx`)

Inspect `design-kit/tokens/index.ts` to determine the **body font family** and the **display/serif font family** used by this kit. Then produce a file of this shape, substituting the real font names:

```tsx
/**
 * app/layout.tsx — drop this into your Next.js App Router project.
 *
 * Loads [BODY_FONT] (sans body) and [DISPLAY_FONT] (serif display) via
 * next/font/google. Exposes them as CSS variables `--font-sans` and
 * `--font-serif` consumed by tailwind.config.ts.
 */
import type { Metadata } from "next";
import { [BODY_FONT_IMPORT], [DISPLAY_FONT_IMPORT] } from "next/font/google";
import "./globals.css";

const sans = [BODY_FONT_IMPORT]({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700", "800"],
  variable: "--font-sans",
  display: "swap",
});

const serif = [DISPLAY_FONT_IMPORT]({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700", "800"],
  variable: "--font-serif",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Your App",
  description: "",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${sans.variable} ${serif.variable}`}>
      <body className="min-h-screen bg-canvas font-sans text-ink antialiased">
        {children}
      </body>
    </html>
  );
}
```

Rules:
- Use `next/font/google` only. No `<link>` tags.
- `bg-canvas` and `text-ink` must match the Tailwind class names produced by the token preset.
- If the project uses only one font family, set `--font-sans` and `--font-serif` to the same import.

### 4c. `globals.css`

```css
/* app/globals.css — drop this in your Next.js App Router project. */

@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  html,
  body {
    height: 100%;
  }

  body {
    background: theme("colors.canvas");
    color: theme("colors.ink.DEFAULT");
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
  }

  button {
    font-family: inherit;
    color: inherit;
    background: transparent;
    border: none;
    padding: 0;
    cursor: pointer;
  }

  input,
  textarea {
    font-family: inherit;
  }
}

@layer utilities {
  .scrollbar-none {
    scrollbar-width: none;
    -ms-overflow-style: none;
  }
  .scrollbar-none::-webkit-scrollbar {
    display: none;
  }
}
```

Replace `colors.canvas` and `colors.ink.DEFAULT` with the actual token path used in `design-kit/tokens/tailwind-preset.ts` if they differ.

### 4d. `tsconfig.snippet.json`

```jsonc
{
  "//": "Merge compilerOptions.paths into your project's tsconfig.json.",
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@kit": ["./design-kit/index.ts"],
      "@kit/*": ["./design-kit/*"]
    }
  }
}
```

### 4e. `postcss.config.js`

```js
/* Standard Tailwind 3 PostCSS config. Drop in your Next.js project root. */
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

### 4f. `package.deps.json`

Inspect the current `package.json` to find the exact installed versions of runtime deps. Then produce:

```jsonc
{
  "//": "Merge these into your project's package.json. They are the design kit's runtime peers.",
  "dependencies": {
    "clsx": "<installed version>",
    "lucide-react": "<installed version>",
    "tailwind-merge": "<installed version>"
  },
  "devDependencies": {
    "tailwindcss": "<installed version>",
    "postcss": "<installed version>",
    "autoprefixer": "<installed version>"
  }
}
```

Use the actual semver ranges from the project's `package.json` — do not copy defaults.

---

## Step 5 — Write `UI/instructions.md`

This is the most important file. It is the **single entry point** the agent in the consumer project reads. It must be fully self-contained and must accurately describe **this specific kit** — its actual colors, actual font names, actual component list.

The file must cover all of the following sections (rewrite each section using the real values from this project):

### Section 1 — What's in `UI/`

A directory tree listing every folder and what it contains, exactly as it was created in Steps 1–4.

### Section 2 — Integration (first session only)

Step-by-step instructions for wiring the kit into a fresh Next.js App Router project:

1. Move `UI/design-kit/` to `<project-root>/design-kit/` (`mv UI/design-kit ./design-kit`).
2. Install peer deps: `npm install lucide-react clsx tailwind-merge` and `npm install -D tailwindcss postcss autoprefixer`.
3. Wire Tailwind: copy or merge `UI/config-templates/tailwind.config.ts` (add the preset import, content path, and font variable extensions).
4. Wire fonts: replace or merge `app/layout.tsx` with `UI/config-templates/layout.tsx` (use `next/font` only — no `<link>` tags).
5. Wire globals: replace or merge `app/globals.css` with `UI/config-templates/globals.css`.
6. Add the `@kit` path alias: merge `UI/config-templates/tsconfig.snippet.json` into the project's `tsconfig.json`.
7. Smoke-test: run `npm run dev`, add `<TopBar />` from `@kit`, verify the body font and canvas background color load correctly.

### Section 3 — The visual language (non-negotiable rules)

A summary of the rules from `design-kit/CLAUDE.md`, written for this kit's specific palette. Include:
- What the primary brand/identity surface color is (the one used on doctor/appointment cards) and its Tailwind class name.
- What the primary action/selection color is and its Tailwind class name.
- What the minor accent color is.
- The shape language rule (pills for controls, 2xl radius for cards).
- The serif display rule (which font, for which elements only).
- The text color rule (no pure black / pure white).
- The shadow rule.
- The no-arbitrary-hex rule.

### Section 4 — How to build a screen

The agent loop:
1. Read the request, identify visual elements.
2. Map each element to a kit component using the component selection table.
3. List chosen components to the user and wait for confirmation before coding.
4. Import from `@kit` only.
5. Use only token-driven Tailwind classes. If a value is missing, add it to `design-kit/tokens/index.ts` first.
6. Page-level layout (outer `<main>`, padding, column width) lives in the page file, not inside components.
7. Read `UI/examples/` for composition patterns — adapt, do not paste.

### Section 5 — When the kit is missing a pattern

Instructions for adding a new primitive or compound without breaking the kit:
1. Confirm it is missing (search `primitives/` and `compounds/`).
2. Choose the right layer (atom → `primitives/`, molecule → `compounds/`).
3. Add the file, match the API style of neighbors.
4. Export it from the layer's `index.ts`.
5. Write a catalog doc in `catalog/`.
6. Then use it.

### Section 6 — What not to do

A `❌` list — derived from `design-kit/CLAUDE.md`'s anti-patterns and the rules above. At minimum:
- No arbitrary Tailwind values.
- No new typefaces.
- No serif font on body/labels/chips/buttons.
- No new "primary" color — lavender (or this kit's equivalent) is primary.
- No square/rectangle controls.
- No drop shadows beyond the token set.
- No one-off styled `<button>` bypassing `@kit`.
- No modifying `tokens/index.ts` for a single-screen ad-hoc value without proposing it first.
- No editing files in `UI/examples/`.
- No deleting catalog docs.

### Section 7 — What to do

A `✅` list — read CLAUDE.md and catalog docs before reaching for a component, prefer kit composition over raw HTML, list components before writing JSX, preserve existing routing/data/auth/business logic, run `npx tsc --noEmit` after changes.

### Section 8 — Canonical agent response template

The first response an agent should give when asked to build a screen:

```
I read UI/instructions.md and design-kit/CLAUDE.md. Here's my plan for <SCREEN>:

Components I'll use (all from @kit):
- <list>

Tokens I'll use:
- <list of Tailwind class names>

New kit components needed: none / [list]

Existing logic I'll preserve: <routing, auth, data hooks, etc.>

Page-level layout: <main className="…">

Confirm and I'll code.
```

### Section 9 — Component cheat-sheet

A Markdown table mapping needs to components. Derive it from `design-kit/CLAUDE.md`'s "Component selection guide" table — make sure the component names match the actual exports in `design-kit/index.ts`.

### Section 10 — If stuck

- Missing component → follow Section 5.
- Missing token → propose to user before adding.
- Rule conflict with user request → quote the rule, explain the conflict, ask the user.
- Example screen differs from CLAUDE.md → CLAUDE.md wins.
- Anything else → ask the user. Do not guess on visual decisions.

---

## Step 6 — Write `UI/README.md`

A short (< 30 line) user-facing guide that explains:
- What the `UI/` folder is.
- How to use it (copy folder + tell agent to read `instructions.md`).
- What's inside each sub-folder.
- The stack assumed (Next.js 14+ App Router + TypeScript + Tailwind 3).

---

## Step 7 — Final verification

Before reporting complete, verify:

1. `UI/design-kit/index.ts` exists and its exports match `design-kit/index.ts` exactly.
2. Every primitive and compound listed in `design-kit/primitives/index.ts` and `design-kit/compounds/index.ts` has a corresponding catalog doc in `UI/design-kit/catalog/`.
3. `UI/config-templates/layout.tsx` imports the correct font names from `next/font/google`.
4. `UI/config-templates/tailwind.config.ts` imports `designKitPreset` from `./design-kit/tokens/tailwind-preset`.
5. `UI/instructions.md` references the correct Tailwind class names for the canvas color, primary action color, and identity surface color — verify these against `design-kit/tokens/tailwind-preset.ts`.
6. `UI/examples/` contains at least one full-page composition file with the read-only comment at the top.

If any check fails, fix the file before reporting.

---

## What the finished `UI/` folder looks like

```
UI/
  design-kit/                  ← exact copy of the project's design-kit
    tokens/
    utils/
    primitives/
    compounds/
    examples/
    catalog/
      primitives/
      compounds/
    index.ts
    CLAUDE.md
    README.md
  examples/                    ← read-only full-page compositions
    HomePage.tsx
    DatePage.tsx
    [other screens].tsx
    mock.ts (if applicable)
  config-templates/            ← Next.js App Router integration files
    tailwind.config.ts
    layout.tsx
    globals.css
    tsconfig.snippet.json
    postcss.config.js
    package.deps.json
  instructions.md              ← agent entry point — must be read first
  README.md                    ← user-facing guide
```

---

## Critical rules for the agent executing this process

- **Do not modify any design-kit file** while copying. The `UI/design-kit/` copy is read-only source material.
- **Do not invent new visual rules** in `instructions.md`. Every rule must be derivable from `design-kit/CLAUDE.md` or `design-kit/tokens/index.ts`.
- **Do not use generic/placeholder font names** in `layout.tsx`. Open `tokens/index.ts` and read the actual font family strings.
- **Do not use hardcoded hex colors** in the config templates. Reference token class names only.
- **`instructions.md` is the user's main entry point** — it must be accurate. A wrong component name or wrong Tailwind class in that file will cause every downstream agent to fail silently. Verify all names against the actual source files.

# Integration Guide

Use this when the user wants to use a generated design kit in a real application.

## Recommended Strategy

Prefer this workflow:

```text
Generate in a clean design-lab repo
Refine visually with the playground
Copy the reusable kit into the real app
Merge config and dependencies
Apply screen by screen
```

This keeps screenshot experimentation separate from production code and makes visual correction safer.

## Copy Into An Existing App

Copy these by default:

```text
design-kit/
  tokens/
  utils/
  primitives/
  compounds/
  index.ts
```

Usually copy these too:

```text
design-kit/assets/        if used by components or examples
design-kit/catalog/       recommended for future AI/dev work
design-kit/README.md      human usage guide
design-kit/CLAUDE.md      AI extension guide
design-kit/INTEGRATION.md integration instructions
```

Optional:

```text
design-kit/examples/
```

Keep examples if the real app team wants reference compositions. They are not required for production runtime unless imported.

Usually do not copy:

```text
playground/
references/
plan/
dist/
node_modules/
temporary screenshots
visual audit scratch files
```

## Merge Configuration

Inspect the generated project and the target app before editing. Merge only what is needed.

Common files to check:

```text
package.json
tailwind.config.ts or tailwind.config.js
tsconfig.json or jsconfig.json
src/index.css, app/globals.css, or equivalent global CSS
vite.config.ts, next.config.js, or bundler config
postcss.config.js
```

Common dependencies:

```bash
npm install clsx tailwind-merge lucide-react
```

Only install dependencies actually used by the generated kit.

Common alias:

```json
{
  "compilerOptions": {
    "paths": {
      "@kit/*": ["design-kit/*"]
    }
  }
}
```

Or use the host app's existing alias style:

```ts
import { Button, Card } from "@/design-kit";
```

## Tailwind Integration

Prefer a kit preset when generated:

```ts
import kitPreset from "./design-kit/tokens/tailwind-preset";

export default {
  presets: [kitPreset],
  content: [
    "./src/**/*.{ts,tsx}",
    "./design-kit/**/*.{ts,tsx}",
  ],
};
```

If the target app already has a rich Tailwind config, merge token extensions carefully instead of replacing the app's theme.

Make sure Tailwind content includes the copied `design-kit/` files, otherwise generated classes may not be emitted.

## Font And Global CSS

Copy font setup only if it is part of the generated visual language.

Check for:

- Google Fonts links
- local font files
- `@font-face` declarations
- global body background
- CSS variables generated from tokens
- Tailwind base layer styles

Avoid overwriting the host app's global reset blindly.

## Applying To Existing Screens

Convert one screen at a time:

1. Read the existing screen and its child components.
2. Identify business logic, data fetching, form handling, auth, routing, and state.
3. Leave that logic intact.
4. Replace visual structure with kit tokens, primitives, and compounds.
5. Add new compounds only when a repeated pattern appears.
6. Verify the screen visually and functionally.

Do not rewrite API calls, auth, stores, route loaders, schemas, or form submit behavior unless the user explicitly asks.

## Integration Prompt

```text
Use $screenshot-to-design-kit.

Apply the local design-kit visual language to this existing app.

First inspect:
- package.json
- Tailwind/global CSS setup
- tsconfig/jsconfig aliases
- route structure
- the target screen and child components
- current shared UI components

Then create an integration plan:
- files to copy or keep
- config/dependencies to merge
- first screen to convert
- existing behavior that must be preserved

After approval, convert one screen at a time.
Preserve routing, data fetching, auth, forms, state, and business logic.
Only change layout, styling, and component composition unless a structural change is necessary.
```

## Integration Checklist

- `design-kit/` copied or available as a package.
- Public exports work from `design-kit/index.ts`.
- Tailwind scans `design-kit/**/*.{ts,tsx}`.
- Token preset or theme extension is merged.
- Required dependencies are installed.
- Fonts/global CSS are merged.
- First converted screen imports kit components.
- Existing behavior still works.
- Visual QA checks no overlaps, clipped labels, or broken responsive states.

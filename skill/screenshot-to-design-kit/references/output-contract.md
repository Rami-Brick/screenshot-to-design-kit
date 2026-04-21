# Output Contract

## Required Folder Shape

```text
design-kit/
  tokens/
    index.ts
    tailwind-preset.ts
  utils/
    cn.ts
  primitives/
    index.ts
  compounds/
    index.ts
  examples/
  catalog/
    primitives/
    compounds/
  CLAUDE.md
  INTEGRATION.md
  README.md
```

## Tokens

`tokens/index.ts` should export semantic token objects:

- colors
- typography
- radii
- spacing
- sizes
- effects
- cssVars when useful

`tokens/tailwind-preset.ts` should expose those tokens to Tailwind without replacing the host app's entire theme.

Token values should be the single source of truth for repeated decisions. If the playground repeats the same arbitrary hex, radius, shadow, or font size several times, promote it to a token.

## Primitives

Primitives are small, reusable building blocks. Common examples:

- icon button
- text button
- avatar/entity mark
- panel/surface
- stat/value block
- segmented/progress bar
- key-value row
- badge/pill/stat

Each primitive should have:

- typed props
- variants only when justified
- accessible behavior
- focused class composition
- catalog doc

## Compounds

Compounds compose primitives into repeated patterns. Common examples:

- top navigation
- page header
- toolbar
- KPI strip
- card header
- list/table row
- detail panel header
- metadata stack
- totals group

Each compound should have:

- typed props
- clear ownership boundaries
- no hidden app state unless explicitly intended
- catalog doc

## Catalog Docs

Each component doc should include:

- purpose
- when to use
- when not to use
- anatomy
- props/variants
- states
- accessibility
- token usage
- implementation notes
- examples

## AI Usage Guide

`CLAUDE.md` should tell future agents:

- what the visual language is
- non-negotiable design rules
- component selection guidance
- token usage guidance
- anti-patterns
- how to apply the kit to an existing app

## Integration Guide

`INTEGRATION.md` should tell humans and future agents:

- recommended workflow: generate in a clean design lab, then integrate into a real app
- when it is reasonable to build directly in the generated repo
- what to copy into another app
- what not to copy into another app
- dependencies to install
- Tailwind/theme/font/global CSS setup to merge
- import alias options
- how to preserve routing, auth, data fetching, forms, and business logic
- a screen-by-screen adoption prompt

## Playground

The example should prove the kit composes:

- use kit components heavily
- keep data realistic
- avoid one-off styling except page layout
- include run instructions
- pass build/lint

## Package Acceptance Checklist

- `design-kit/index.ts` or layer-level exports exist.
- `tokens` are consumed by components or Tailwind config.
- `README.md` explains installation and basic usage.
- `CLAUDE.md` explains how future agents should use the kit.
- `INTEGRATION.md` explains how to use the kit in a new or existing app.
- Component docs include "when not to use" or equivalent boundaries.
- Playground demonstrates the main screenshot pattern with realistic data.
- The final report asks or answers what the user should do next: start a new app, integrate into an existing app, keep a design lab, or package/share the kit.

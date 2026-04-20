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
- Component docs include "when not to use" or equivalent boundaries.
- Playground demonstrates the main screenshot pattern with realistic data.
- The final report tells the user how to apply the kit to another app.

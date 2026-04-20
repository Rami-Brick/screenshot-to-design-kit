# Implementation Guidelines

## Extraction Heuristics

Look for repeated shapes, not just repeated content.

- Same shape + same state behavior = primitive candidate.
- Same arrangement of primitives = compound candidate.
- Single screen-specific layout = page-level composition.
- Same value with different hue/spacing = token candidate.

Prefer semantic token names:

- `surface.glass`
- `surface.raised`
- `text.secondary`
- `accent.primary`
- `radius.panel`

Avoid literal-only names like `gray-850` unless the host system already uses that convention.

## Component Boundaries

Primitives own:

- shape
- base visual treatment
- direct accessibility
- simple variants

Compounds own:

- arrangement
- component combinations
- repeated product patterns
- controlled state if the state is local to the pattern

Pages own:

- data fetching
- route behavior
- screen-level layout
- business logic
- responsive region placement

## Visual Fidelity

Prioritize:

1. geometry and spacing rhythm
2. surface hierarchy
3. typography hierarchy
4. color and accent restraint
5. icon choices
6. exact content

If exact values are uncertain, label them as estimates in the audit and refine during playground QA.

For "inspired system" mode:

- Content, names, and labels may change.
- Component names and APIs may be generalized.
- Layout DNA should remain: major columns, sidebar treatment, card proportions, density, and signature components.
- Surface atmosphere should remain unless the user explicitly asks to flatten it.
- Do not replace a distinctive design with a generic clean dashboard.

## Device And Browser Frame Handling

Screenshots often include capture context that should not become UI:

- iPhone notch or dynamic island
- iOS/Android status bar
- browser address bar
- desktop wallpaper/canvas around a mockup
- rounded phone body
- presentation background
- Dribbble/marketing shot framing

Before implementation, decide whether these are:

1. **Real target UI**: reproduce them as components.
2. **Viewport context**: account for safe areas, but do not draw them.
3. **Presentation artifact**: remove entirely.

For mobile app screenshots, default to building the actual app screen, not a phone mock, unless the user asks for a mockup. Use full viewport shells (`min-h-dvh`) and safe-area padding for real mobile web/app surfaces.

## Accessibility

- Icon-only controls require accessible labels.
- Interactive elements need focus-visible states.
- Navigation should use semantic nav or aria labels.
- Tables should use table semantics when data is tabular.
- Low-contrast text from screenshots may need slight contrast adjustment.

## Validation

Run what the project provides:

- install dependencies if needed
- typecheck
- lint
- build
- visual screenshot checks when available

Fix text overlap, clipped controls, broken responsive behavior, and blank/failed render states before final handoff.

Functional validation is not visual validation:

- HTTP 200 means the server responded.
- Typecheck/build means the code compiles.
- Neither proves visual fidelity.

For visual fidelity, capture a screenshot or ask the user for one, then compare it against the reference using `visual-comparison-report.md`.

## Visual QA Procedure

When a dev server can run:

1. Start the app.
2. Capture a screenshot at the target viewport when tools allow it.
3. If responsive scope requires it, inspect tablet and mobile widths.
4. Check for:
   - text larger than the reference rhythm
   - table columns overlapping
   - numbers squeezed into each other
   - buttons clipping labels
   - cards/panels losing padding
   - icons misaligned inside circles
   - accent color appearing too often
   - page-level layout bypassing the kit
   - device/browser chrome accidentally recreated as UI
   - missing signature assets or photo/thumbnail regions
   - too much whitespace compared with the reference
   - flattened atmosphere where the app surface should stay softly tinted

If Playwright is available, prefer screenshots over eyeballing. If no browser tool is available, run build/lint and ask the user to share a screenshot after launching.

## Fidelity Calibration

After the first playground render, compare against the screenshot by category:

| Category | Question |
|---|---|
| Geometry | Do shapes, radii, and proportions feel from the same system? |
| Density | Does text/control scale match the screenshot's density? |
| Surfaces | Are panels layered like the reference, or too flat/card-like? |
| Type | Does the font feel too generic, too large, or off-brand? |
| Accent | Is the primary accent scarce and high-signal? |
| Composition | Are repeated regions built from kit components? |

Use this comparison to tune tokens and component spacing before final handoff.

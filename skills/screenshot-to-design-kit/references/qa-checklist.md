# QA Checklist

Run this before final handoff.

## Functional

- Dependencies installed or documented.
- Typecheck/build passes, or failure is reported with cause.
- Lint passes, or failure is reported with cause.
- Dev server instructions are provided.
- Public components are exported.
- HTTP 200 is reported only as a smoke test, not visual QA.

## Visual

- Side-by-side comparison was performed, or the user was asked to provide a playground screenshot.
- Supporting palette/typography references were applied to tokens, or omissions are explained.
- No text overlaps.
- No clipped labels in buttons/pills.
- No table amount/rate columns colliding.
- No panel content touching edges unexpectedly.
- Icon buttons are circular and icons are centered.
- Typography scale feels close to the chosen reference.
- Layout density and whitespace feel close to the chosen reference.
- Signature visual elements from the reference are present or intentionally adapted.
- Photo/thumbnail/logo regions are preserved in size and role, even if placeholder assets are used.
- Accent color is not overused.
- Responsive layouts do not collapse incoherently in requested viewports.
- Device/browser/mockup chrome is handled according to the user's answer.
- Full-screen mobile pages do not accidentally sit inside a fake phone frame.

## Kit Integrity

- Playground imports kit components.
- Repeated UI is not recreated with one-off markup.
- Tokens are used for repeated design decisions.
- Catalog docs exist for reusable components.
- Component boundaries are clear.
- `README.md` and `CLAUDE.md` exist.

## Final Report

Include:

- files/folders created or changed
- validation commands and results
- visual QA notes
- side-by-side fidelity notes: what matches, what diverges, why
- supporting reference usage: colors, typography, assets
- known limitations
- how to run the playground
- how to apply the kit to another app

# Case Study: Mobile Fitness Success

Use this as a positive example of a multi-reference extraction.

## Input

Three references:

- `HomeScreen.png`: primary mobile app screen.
- `palette.webp`: supporting color board with explicit colors.
- `typography.webp`: supporting typography board naming the Lufga type direction and weight range.

The primary screen included:

- phone screenshot with status bar/dynamic island
- warm peach full-screen background
- greeting header
- "Recent Activity" mixed-weight heading
- date strip with selected orange day
- large steps card with orange bar chart
- smaller metric cards with circular progress rings
- floating bottom tab bar

## What Worked

- The agent clarified frame behavior and removed device chrome/status UI.
- The rounded phone frame was treated as viewport context, not recreated as a mock.
- Palette reference drove exact token choices like orange `#EE9033`, white `#FFFFFF`, near-black `#0F0F0F`, and gray `#D3D1D1`.
- Typography reference drove the font direction instead of guessing from the screenshot.
- Final result preserved:
  - edge-to-edge mobile viewport
  - peach background
  - orange accent hierarchy
  - mixed bold/italic heading rhythm
  - date pill strip
  - steps/chart card hierarchy
  - bottom floating tab bar
  - compact vertical mobile density

## Lesson

Multiple supporting references improve fidelity because they remove guesswork from tokens and type.

When a palette board and typography board exist:

- extract exact token values from them
- name the source of each token in the audit
- let the primary screen drive layout
- let supporting boards refine color/type, not replace layout

## Good Audit Shape

The audit should explicitly say:

```text
Resource inventory:
- HomeScreen.png: primary screen/layout reference
- palette.webp: supporting color token reference
- typography.webp: supporting font/weight reference

Token confidence:
- colors: high, from palette board
- typography: high, from typography board
- spacing/radii: medium, estimated from primary screen
- icons/assets: medium, inferred/cropped/replaced as needed
```

## Good Implementation Shape

- Use a `ScreenFrame` or page shell for full-viewport mobile app surface.
- Do not draw device chrome unless requested.
- Keep chart/card/tab bar dimensions stable.
- Preserve the role of avatar/photo areas.
- Use exact palette tokens from the supporting board.
- Document font assumptions if the actual font package is unavailable.

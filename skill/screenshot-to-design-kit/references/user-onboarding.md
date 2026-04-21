# User Onboarding

Use this when the user asks how to start or when no screenshots/resources exist.

## Recommended Project Layout

Ask the user to put resources here:

```text
references/
  screenshots/
    01-primary-home.png
    02-primary-dashboard.png
    palette.png
    typography.png
    component-card-detail.png
    mood-reference.png
```

## Resource Naming

Recommend clear names:

- `primary-*.png/webp/jpg`: main screen/page to recreate.
- `palette-*`: color boards, swatches, brand colors.
- `typography-*`: font boards, type hierarchy, weight samples.
- `component-*`: close-ups of cards, buttons, tables, nav, charts.
- `asset-*`: logos, photos, icons, illustrations.
- `mood-*`: inspiration for atmosphere only.

## What To Tell The User

```text
Put your screenshots and visual references in references/screenshots/.

At minimum, provide one primary UI screenshot.
For better results, add:
- a palette/color reference
- a typography/font reference
- close-up component screenshots
- any logos/photos/icons you want preserved

Then run:
Use $screenshot-to-design-kit.

Create a reusable React + Tailwind design kit from the visual resources in references/screenshots/.
Inspect all resources first, classify each by role, then ask me one batch of intake questions with options.
Use guided checkpoints.
```

For more ready-to-copy prompts, use `prompt-library.md`. If this skill is shipped in an installable package, expose the "Quick Start Prompt" and "README Usage Snippet" from that file in the package README or a top-level `PROMPTS.md` outside the skill folder.

## What Happens After Generation

Tell the user the skill is not only for generating a demo. After the playground looks good, the skill will guide them through one of these paths:

1. keep working in the generated repo as the start of a new app
2. copy/integrate the generated `design-kit/` into an existing app
3. keep the generated repo as a design lab/reference project
4. package or share the kit

The generated kit should include `design-kit/INTEGRATION.md` so the user can see what to copy, what not to copy, and what config to merge.

## If The User Has Only One Screenshot

Say that it will work, but fidelity is usually better with palette/type/assets. Continue using `single-reference-mode.md`.

# Prompts

Copy-paste prompts for using the `screenshot-to-design-kit` Claude Code skill.

---

## 1. Prepare References

Run this first if you haven't added screenshots yet.

```
Use $screenshot-to-design-kit.

Prepare this project for screenshot-to-design-kit work.

Create the recommended references/screenshots/ folder if it does not exist.
Add a short note inside it explaining what screenshots and resources I should place there.
Do not start implementation yet.

After preparing the folder, tell me exactly what to add and give me the next prompt to run.
```

---

## 2. Quick Start

Run this once you've added at least one primary UI screenshot to `references/screenshots/`.

```
Use $screenshot-to-design-kit.

Create a reusable React + Tailwind design kit from the visual resources in references/screenshots/.

Inspect all resources first and classify each by role:
- primary UI screen
- palette/color reference
- typography reference
- component/detail reference
- asset reference
- mood reference
- device/browser/mockup frame reference

Do not assume phone frames, browser chrome, notches, status bars, rounded presentation boxes, or decorative backgrounds are part of the real UI.

Ask me one batch of intake questions with options before implementation.
Use guided checkpoints.

The final output should include tokens, primitives, compounds, catalog docs, CLAUDE.md, README.md, and a working playground example.
```

---

## 3. Multiple References

Use when you have separate files for palette, typography, component close-ups, etc.

```
Use $screenshot-to-design-kit.

Create a reusable React + Tailwind design kit from these resources:

Primary UI reference:
references/screenshots/[PRIMARY_FILE]

Supporting references:
references/screenshots/[PALETTE_OR_COLOR_FILE]
references/screenshots/[TYPOGRAPHY_FILE]
references/screenshots/[COMPONENT_DETAIL_FILE]
references/screenshots/[ASSET_OR_MOOD_FILE]

The primary UI reference is the page/screen I want recreated in the playground.
The supporting references are only for extracting colors, typography, spacing, mood, assets, and component details.

Inspect all resources first, classify their roles, and ask me one batch of intake questions with options.

Important: some screenshots may include phone frames, browser chrome, notches, status bars, rounded presentation boxes, or decorative backgrounds. Do not assume those are part of the real UI. Ask how each frame/chrome should be handled.

Use guided checkpoints. The final output should be a reusable design kit with tokens, primitives, compounds, catalog docs, CLAUDE.md, README.md, and a working playground example.
```

---

## 4. Single Screenshot

Use when you have exactly one image and no supporting palette or assets.

```
Use $screenshot-to-design-kit.

Create a reusable React + Tailwind design kit from this single reference:
references/screenshots/[FILE_NAME]

Use single-reference mode.

Because there is only one screenshot, preserve the reference's layout DNA, density, surface treatment, typography feel, color atmosphere, and signature components. Do not turn it into a generic UI kit.

If palette, typography, or asset fidelity is uncertain, ask me whether I can provide supporting references before implementation.

Inspect the screenshot first, classify any frame/chrome/presentation background, then ask me one batch of intake questions with options.
Use guided checkpoints and require a visual comparison before final handoff.
```

---

## 5. Fast Auto (No Checkpoints)

Use when you want the full kit built in one pass.

```
Use $screenshot-to-design-kit.

Create a reusable React + Tailwind design kit from the visual resources in references/screenshots/.

Inspect all resources first, classify each by role, then ask me one batch of intake questions with options.

Use fast auto mode: run all phases without stopping for approval. Still produce phase reports in the final answer.

The final output should include tokens, primitives, compounds, catalog docs, CLAUDE.md, README.md, and a working playground example.
```

---

## 6. Fix / Correction Loop

Use after delivery when you spot a visual or design problem.

```
Use $screenshot-to-design-kit correction loop.

The generated result has this problem:
[DESCRIBE THE ISSUE]

Reference screenshot(s):
[PATHS OR ATTACHED IMAGES]

Current result screenshot:
[PATH OR ATTACHED IMAGE]

Please:
1. Restate the problem in concrete UI terms.
2. Ask up to 3 clarifying questions only if needed.
3. Identify whether the fix belongs in tokens, primitives, compounds, playground composition, or docs.
4. Make the smallest design-kit-safe fix.
5. Update catalog docs if component responsibilities changed.
6. Run validation and visual QA again.
```

---

## 7. Visual QA / Fidelity Score

Use to get a scored comparison before or after delivery.

```
Use $screenshot-to-design-kit visual comparison.

Compare the reference resources in references/screenshots/ with this current result:
[ATTACH SCREENSHOT OR PROVIDE PATH]

Score the result using the fidelity rubric:
- layout structure
- spacing and density
- typography scale and weight
- color and surface treatment
- signature components
- asset/photo/icon treatment
- frame/chrome handling
- responsive behavior, if applicable

Then list the smallest set of fixes that would most improve fidelity.
Do not implement until I approve the fix list.
```

---

## 8. Apply Kit to Existing App

Use when the design kit is ready and you want to restyle an existing codebase.

```
Use $screenshot-to-design-kit.

Apply the local design-kit visual language to this existing app.

Preserve existing routing, data, auth, state management, forms, API calls, and business logic.
Change presentation and layout only unless a structural change is necessary.

First read the app routes/components and map the current UI to existing kit primitives and compounds.
Convert one screen at a time.
Use guided checkpoints and verify after each screen.

After editing:
- run any skill validation script if present
- run package tests/lint if present
- report changed files
- tell me exactly what users should put in the README and what prompt they should run first
```

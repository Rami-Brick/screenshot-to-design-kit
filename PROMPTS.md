# Screenshot To Design Kit Prompts

Read this file first after installing `@rami-brick/screenshot-to-design-kit`.

This is the human guide. The internal skill files under `.claude/skills/screenshot-to-design-kit/` are for Claude/Codex. You usually do not need to open them.

Use these prompts from your project root, where the skill was installed.

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

---

## 9. After Generation: What Do I Do Next?

Use this after the design kit looks good in the playground.

```
Use $screenshot-to-design-kit after-generation guidance.

The design kit has been generated and visually reviewed.

Help me choose the best next path:
1. start a new app from this generated repo
2. copy/integrate this design kit into an existing app
3. keep this as a design lab/reference repo
4. package or share the design kit

Explain the tradeoffs briefly.
Then give me the exact next steps for the path I choose.
```

---

## 10. Integrate Generated Kit Into Another Project

Use this when you generated the kit in a clean repo and want to move it into a real app.

```
Use $screenshot-to-design-kit integration guide.

I have a generated design kit and I want to use it in this existing app.

First inspect:
- package.json
- Tailwind/global CSS setup
- tsconfig/jsconfig aliases
- route structure
- current shared UI components
- the first screen to convert

Then create an integration plan that includes:
- which generated files/folders to copy
- which generated files/folders not to copy
- dependencies to install
- Tailwind/theme/font/global CSS changes to merge
- import alias strategy
- first screen to convert
- existing behavior that must be preserved

Do not rewrite auth, routing, API calls, stores, schemas, forms, or business logic unless I explicitly ask.
After I approve the plan, convert one screen at a time.
```

---

## Recommended Workflow

For most users:

1. Run **Prepare References** if you do not have `references/screenshots/`.
2. Add one primary screenshot. Add palette/type/component references if available.
3. Run **Quick Start** or **Multiple References**.
4. Use **Fix / Correction Loop** until the playground looks good.
5. Run **After Generation** to choose what to do next.
6. If you have a separate real app, run **Integrate Generated Kit Into Another Project**.

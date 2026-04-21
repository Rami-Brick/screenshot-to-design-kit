# Prompt Library

Use this file when the user asks how to use the skill after installation, wants README copy, or needs a reliable prompt to paste into Claude Code/Codex.

## Contents

- Quick Start Prompt
- Prepare References Prompt
- Standard Guided Prompt
- Multi-Reference Prompt
- Single-Reference Prompt
- Fast Auto Prompt
- Correction Loop Prompt
- Visual QA Prompt
- After Generation Prompt
- Existing App Integration Prompt
- Existing App Conversion Prompt
- README Usage Snippet

## Quick Start Prompt

Use when the user has already placed screenshots in `references/screenshots/` and wants the normal guided workflow.

```text
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

## Prepare References Prompt

Use when the user installed the skill but has not organized screenshots yet.

```text
Use $screenshot-to-design-kit.

Prepare this project for screenshot-to-design-kit work.

Create the recommended references/screenshots/ folder if it does not exist.
Add a short note inside it explaining what screenshots and resources I should place there.
Do not start implementation yet.

After preparing the folder, tell me exactly what to add and give me the next prompt to run.
```

## Standard Guided Prompt

Use for the best default experience. This is the prompt to put near the top of a public README.

```text
Use $screenshot-to-design-kit.

Create a reusable React + Tailwind design kit from the visual resources in references/screenshots/.

First inspect every resource. Classify each file as one of:
- primary UI reference
- supporting color/palette reference
- supporting typography reference
- component/detail reference
- asset/logo/photo/icon reference
- mood/style reference
- device/browser/mockup/presentation frame reference

The primary UI reference drives the layout and components. Supporting references should refine colors, typography, spacing, assets, and mood.

Important: screenshots may include phone frames, browser chrome, status bars, notches, rounded mockup boxes, or presentation backgrounds. Do not assume those are part of the UI. Ask me how frame/chrome should be handled before implementing.

Ask me one batch of intake questions with options.
Use guided checkpoints.

Final output requirements:
- design-kit/tokens
- design-kit/primitives
- design-kit/compounds
- design-kit/catalog
- design-kit/examples
- design-kit/CLAUDE.md
- design-kit/README.md
- working playground example
- build/typecheck results
- visual comparison notes
```

## Multi-Reference Prompt

Use when the user can name the primary screenshot and supporting files.

```text
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

## Single-Reference Prompt

Use when there is only one screenshot. This forces the agent to preserve fidelity instead of drifting into a generic redesign.

```text
Use $screenshot-to-design-kit.

Create a reusable React + Tailwind design kit from this single reference:
references/screenshots/[FILE_NAME]

Use single-reference mode.

Because there is only one screenshot, preserve the reference's layout DNA, density, surface treatment, typography feel, color atmosphere, and signature components. Do not turn it into a generic UI kit.

If palette, typography, or asset fidelity is uncertain, ask me whether I can provide supporting references before implementation.

Inspect the screenshot first, classify any frame/chrome/presentation background, then ask me one batch of intake questions with options.
Use guided checkpoints and require a visual comparison before final handoff.
```

## Fast Auto Prompt

Use when the user wants less interruption. The agent still has to report checkpoints, but it does not stop at each one.

```text
Use $screenshot-to-design-kit.

Create a reusable React + Tailwind design kit from references/screenshots/.

Use fast auto mode: continue through audit, system plan, implementation, playground, docs, and QA without stopping for approval at each checkpoint.

Still do all of the following:
- inspect and classify every resource first
- ask one intake batch if any critical decision is ambiguous
- apply the fidelity rubric
- avoid treating frames/chrome/presentation backgrounds as UI unless confirmed
- build the reusable kit, not just a one-off page
- run build/typecheck when available
- produce visual comparison notes before final handoff
```

## Correction Loop Prompt

Use after the first result when the user notices something wrong.

```text
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

## Visual QA Prompt

Use when the user gives a comparison screenshot or wants the agent to score fidelity before editing.

```text
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

## Existing App Conversion Prompt

Use when the user already has an app and wants to apply the generated kit to it.

```text
Use $screenshot-to-design-kit.

Apply the local design-kit visual language to this existing app.

Preserve existing routing, data, auth, state management, forms, API calls, and business logic.
Change presentation and layout only unless a structural change is necessary.

First read the app routes/components and map the current UI to existing kit primitives and compounds.
Convert one screen at a time.
Use guided checkpoints and verify after each screen.
```

## After Generation Prompt

Use after a design kit has been generated and the user asks what to do next.

```text
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

## Existing App Integration Prompt

Use when the user has a generated kit and a separate real app.

```text
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

## README Usage Snippet

Use this in an installable package README or marketplace page.

````markdown
## How to use

1. Install the skill.
2. In your project, add screenshots to:

   ```text
   references/screenshots/
   ```

3. Add at least one primary UI screenshot. For better results, also add:
   - palette/color references
   - typography references
   - component close-ups
   - logos/photos/icons
   - mood references

4. Run this prompt in Claude Code/Codex:

   ```text
   Use $screenshot-to-design-kit.

   Create a reusable React + Tailwind design kit from the visual resources in references/screenshots/.
   Inspect all resources first, classify each by role, then ask me one batch of intake questions with options.
   Use guided checkpoints.
   ```

Tip: if the screenshot shows a phone frame, browser chrome, notch, status bar, rounded mockup box, or decorative background, the skill will ask whether that is part of the real UI before implementing.

After the playground looks good, choose one path:

- start a new app from the generated repo
- copy the generated `design-kit/` into an existing app
- keep the generated repo as a design lab
- package/share the kit

The generated kit should include `design-kit/INTEGRATION.md` with exact file-copy and config-merge guidance.
````

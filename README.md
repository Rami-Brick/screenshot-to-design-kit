# @rami-brick/screenshot-to-design-kit

A Claude Code skill that converts UI screenshots, website links, and design references into a reusable **React/Tailwind design kit** — with tokens, primitives, compounds, catalog docs, and a playground example.

---

## Install

```bash
npx @rami-brick/screenshot-to-design-kit
```

This copies the skill into `~/.claude/skills/screenshot-to-design-kit/`.

### Update / Reinstall

```bash
npx @rami-brick/screenshot-to-design-kit --force
```

### Custom install path

```bash
npx @rami-brick/screenshot-to-design-kit --path /path/to/your/skills-dir
```

### Dry-run (preview only, no files written)

```bash
npx @rami-brick/screenshot-to-design-kit --dry-run
```

---

## What it does

Given screenshots, links, or brand notes, the skill:

1. Classifies every visual resource (primary screen, color ref, typography ref, etc.)
2. Asks one focused batch of intake questions before starting
3. Extracts the design language as structured tokens (color, typography, spacing, radii, shadows)
4. Generates primitive components (Button, Input, Badge, Card, …)
5. Composes compound components and page templates
6. Produces a component catalog with live usage examples
7. Applies human checkpoints so you review fidelity at each stage
8. Delivers a QA checklist and a visual comparison report

The skill builds a **reusable visual system**, not just a screenshot clone. It will not treat phone frames, browser chrome, notches, status bars, or presentation backgrounds as part of the real UI.

---

## Using the skill in Claude Code

After installing, reference the skill in your project's `CLAUDE.md`:

```markdown
Use the skill at ~/.claude/skills/screenshot-to-design-kit/SKILL.md
```

---

## Prepare your references

Place visual resources here before running any prompt:

```
your-project/
└── references/
    └── screenshots/
        ├── primary-screen.png        ← main UI to recreate (required)
        ├── palette.png               ← color reference (optional)
        ├── typography.png            ← type reference (optional)
        ├── component-detail.png      ← component close-ups (optional)
        ├── asset-logo.png            ← logos, icons, photos (optional)
        └── mood-reference.png        ← inspiration/atmosphere (optional)
```

**Minimum:** one primary UI screenshot.
**Better results:** add palette, typography, and component close-ups.

If the folder doesn't exist yet, run the Prepare References prompt below and the skill will create it for you.

---

## Prompts

All prompts are in [PROMPTS.md](PROMPTS.md). The most common ones:

### Prepare References (run first if you have no screenshots yet)

```
Use $screenshot-to-design-kit.

Prepare this project for screenshot-to-design-kit work.

Create the recommended references/screenshots/ folder if it does not exist.
Add a short note inside it explaining what screenshots and resources I should place there.
Do not start implementation yet.

After preparing the folder, tell me exactly what to add and give me the next prompt to run.
```

### Quick Start (run after adding screenshots)

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

### Fix a problem after delivery

```
Use $screenshot-to-design-kit correction loop.

The generated result has this problem:
[DESCRIBE THE ISSUE]

Reference screenshot(s): [PATHS OR ATTACHED IMAGES]
Current result screenshot: [PATH OR ATTACHED IMAGE]

Please restate the problem, ask up to 3 clarifying questions if needed, identify the kit layer to fix, make the smallest safe fix, update catalog docs if needed, and run visual QA again.
```

### Apply kit to an existing app

```
Use $screenshot-to-design-kit.

Apply the local design-kit visual language to this existing app.
Preserve existing routing, data, auth, state management, forms, API calls, and business logic.
Change presentation and layout only unless a structural change is necessary.
Convert one screen at a time with guided checkpoints.
```

See [PROMPTS.md](PROMPTS.md) for the full prompt library including multi-reference, single-reference, fast auto, and visual QA prompts.

---

## Expected output

```
design-kit/
  tokens/
  utils/
  primitives/
  compounds/
  examples/
  catalog/
    primitives/
    compounds/
  CLAUDE.md
  README.md
```

---

## Local test flow

```bash
# Dry-run (no writes)
node bin/install.js --dry-run

# Install to a temp dir
node bin/install.js --path /tmp/test-skills --force

# Verify SKILL.md is present
ls /tmp/test-skills/screenshot-to-design-kit/SKILL.md
```

---

## Publish

```bash
npm login
npm publish --access public
```

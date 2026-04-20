# @rami/screenshot-to-design-kit

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
2. Asks focused intake questions about target stack, fidelity, tokens, and output format
3. Extracts the design language as structured tokens (color, typography, spacing, radii, shadows)
4. Generates primitive components (Button, Input, Badge, Card, …)
5. Composes compound components and page templates
6. Produces a component catalog with live usage examples
7. Applies human checkpoints so you review fidelity at each stage
8. Delivers a QA checklist and a visual comparison report

---

## Using the skill in Claude Code

After installing, reference the skill in your project's `CLAUDE.md`:

```markdown
Use the skill at ~/.claude/skills/screenshot-to-design-kit/SKILL.md
```

Or paste the starter prompt directly into a Claude Code conversation (see below).

---

## Recommended project layout

Place your visual references here before starting:

```
your-project/
└── references/
    └── screenshots/
        ├── primary-screen.png        ← main UI to recreate
        ├── color-palette.png         ← optional
        ├── typography-sample.png     ← optional
        └── component-detail.png     ← optional
```

If the folder is missing, the skill will create it and wait for you to add files.

---

## Starter prompt

Paste this into Claude Code after adding your screenshots:

```
I have added UI screenshots to references/screenshots/.
Using the screenshot-to-design-kit skill, convert them into a reusable React/Tailwind design kit.
Target stack: React + Tailwind CSS.
Output: design tokens, primitive components, compound components, a component catalog, and a playground page.
Apply checkpoints before each major deliverable so I can review fidelity.
```

---

## Local test flow

```bash
# 1. Pack the package
npm pack

# 2. Dry-run (no writes)
node bin/install.js --dry-run

# 3. Install to a temp dir
node bin/install.js --path /tmp/test-skills --force

# 4. Verify SKILL.md is present
ls /tmp/test-skills/screenshot-to-design-kit/SKILL.md
```

---

## Publish

```bash
npm login
npm publish --access public
```

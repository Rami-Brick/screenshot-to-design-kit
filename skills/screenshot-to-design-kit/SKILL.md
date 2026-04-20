---
name: screenshot-to-design-kit
description: Convert UI screenshots, website links, design references, or visual inspiration into a reusable React/Tailwind design kit with tokens, primitives, compounds, catalog docs, examples, and checkpoint-based human review. Use when the user wants to recreate a UI from screenshots, extract a template/design system, automate screenshot-to-component workflows, build a design kit, or apply a captured visual language to another application.
---

# Screenshot To Design Kit

## Core Rule

Build a reusable visual system, not just a screenshot clone.

When given screenshots, links, prompts, or resources, first extract the design language, then package it as tokens, primitives, compounds, docs, and a playground example. Keep human checkpoints because taste and fidelity need review.

## Input Handling

Inspect all provided materials before asking intake questions:

- screenshots or image files
- links to reference sites or design shots
- existing app code
- written prompt or brand notes
- current design-kit files if this is an update

If no `references/screenshots/` folder or no visual resources exist, onboard the user:

1. Create `references/screenshots/` in the target project when filesystem access is available.
2. Create a short `references/screenshots/PUT_SCREENSHOTS_HERE.txt` note when possible.
3. Tell the user to add primary UI screenshots and optional palette, typography, component-detail, asset, and mood references.
4. Provide the starter prompt from `references/user-onboarding.md`.
5. Stop until the user adds resources.

Classify every visual resource before asking questions:

- primary screen to recreate
- supporting color reference
- supporting typography reference
- component/detail reference
- mood/inspiration reference
- device/browser/mockup frame reference

If a screenshot includes device chrome, browser chrome, a notch, status bar, rounded phone frame, desktop canvas, or presentation background, do not assume it is part of the UI. Ask whether the frame/chrome should be reproduced, removed, or treated as viewport context.

If a linked reference or current information is needed and not provided locally, browse or ask for the missing artifact. If screenshots are missing, ask for them before starting.

## Intake Questions

Ask intake questions once, immediately after inspecting inputs. Prefer a structured multi-choice UI when available. Otherwise ask concise numbered questions with 2-4 options each and allow custom answers.

Use `references/intake-questions.md` for the full question bank. Ask only the questions needed for the task. Do not ask every possible question if the answer is obvious from context.

Default questions:

1. Output goal: reusable design kit, one-screen recreation, apply to existing app, or all of these.
2. Primary reference: which screenshot is the main screen/page to recreate.
3. Frame/chrome behavior: reproduce, remove, or treat as real viewport context.
4. Fidelity target: close clone, inspired system, or loose style transfer.
5. Stack: React/Vite/Tailwind default unless the app already uses another stack.
6. Typography direction: premium geometric, editorial/luxury, technical/neutral, or custom.
7. Checkpoint mode: guided checkpoints, fast auto with final review, or research only.
8. Responsive scope: desktop only, desktop plus tablet, or full responsive.

After the user answers, summarize the decisions in 5-8 lines and start Phase 1.

## Workflow

Follow this checkpoint sequence unless the user explicitly chooses fast auto:

1. **Phase 1: Audit**
   Produce a visual audit, design invariants, token estimates, component taxonomy, risks, and open questions. Stop for approval.

2. **Phase 2: System Plan**
   Define the output folder structure, token schema, primitives, compounds, and build order. Stop for approval.

3. **Phase 3: Implement Kit**
   Create or update `design-kit/` with tokens, primitives, compounds, utilities, exports, and catalog docs. Run typecheck/lint when available. Stop with a short implementation report.

4. **Phase 4: Playground**
   Build a working example that uses the kit. Do not bypass the kit with large one-off styling except for page-level composition. Stop with screenshots or clear run instructions.

5. **Phase 5: QA And Package**
   Run build/lint, inspect desktop/mobile if possible, fix obvious layout overlap, and create `CLAUDE.md` plus `README.md` usage guidance. Stop with final handoff.

Use `references/checkpoint-workflow.md` for detailed phase deliverables and gate criteria.
Use `references/resource-classification.md` when there are multiple screenshots, device screenshots, browser screenshots, mockups, or supporting visual resources.
Use `references/user-onboarding.md` when the user asks how to start, how to organize screenshots, or when resources are missing.
Use `references/fidelity-rubric.md` before implementation and again after the playground render.
Use `references/single-reference-mode.md` when the user provides only one screenshot and no supporting palette/assets.

Before implementing a substantial kit, skim the relevant case studies:

- `references/case-study-dashboard-kit.md` for a dark glass dashboard with strong component extraction.
- `references/case-study-mobile-fitness-success.md` for a good multi-reference mobile app extraction.
- `references/case-study-healthcare-dashboard.md` for a single-screenshot healthcare dashboard where atmosphere and density matter.

## Output Contract

For a new kit, create this shape unless the user asks otherwise:

```text
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

Use `references/output-contract.md` for file-level expectations.
Use `references/qa-checklist.md` before final handoff.
Use `references/visual-comparison-report.md` to report visual QA.
Use `references/correction-loop.md` when the user gives post-delivery feedback.

If starting from an empty project, run:

```bash
python skills/screenshot-to-design-kit/scripts/scaffold_design_kit.py --root .
```

Adjust the script path if the skill is installed globally.

To only prepare the screenshot/resource folder, run:

```bash
python skills/screenshot-to-design-kit/scripts/prepare_references.py --root .
```

## Implementation Standards

- Prefer React + TypeScript + Tailwind unless the target app already has a different stack.
- Use semantic tokens first, then Tailwind utilities generated from those tokens.
- Use primitives for foundational shapes: buttons, avatars, panels, stats, rows, bars.
- Use compounds for repeated arrangements: navs, headers, KPI strips, cards, table rows, detail panels.
- Keep page-level layout separate from reusable components.
- Add catalog docs that say what each component owns and what is intentionally not part of it.
- Preserve accessibility: labels for icon buttons, focus states, semantic nav/table/region markup.
- Avoid overfitting to one screenshot artifact unless the user asked for a strict clone.
- Validate with build/lint and visual inspection where possible.
- Treat HTTP 200, typecheck, and build as functional checks only. They do not count as visual QA.
- For any recreation, produce or request a side-by-side visual comparison before final handoff.

Use `references/implementation-guidelines.md` for deeper rules.

## Checkpoint Behavior

At checkpoints:

- Give a short report: completed work, files changed, decisions made, risks.
- Ask whether to continue to the next phase.
- Do not continue past the checkpoint unless the user approved or selected fast auto.

In fast auto mode, continue through all phases, but still produce the same reports in the final answer.

Never mark the project complete if there are obvious text overlaps, clipped buttons, blank renders, missing exports, or a playground that mostly ignores the kit.
Never mark visual QA complete from server availability alone. If screenshots cannot be captured, say so and ask the user to provide a playground screenshot.

## Applying The Kit To An Existing App

When the target is an existing app:

1. Read the app routes/components first.
2. Map current UI patterns to kit primitives and compounds.
3. Preserve existing data, behavior, routing, auth, and business logic.
4. Change presentation and layout only unless structural changes are necessary.
5. Convert one screen at a time and verify after each screen.

## Failure Modes To Avoid

- Do not make only a pretty playground and skip reusable components.
- Do not make only research docs and skip implementation when implementation is requested.
- Do not create generic shadcn/SaaS UI if the screenshot has a distinctive language.
- Do not let "inspired system" mean generic redesign. Preserve the reference's layout DNA, density, surface atmosphere, and signature elements unless the user explicitly wants looser style transfer.
- Do not ask questions before inspecting the screenshot/resources.
- Do not turn a phone screenshot, browser screenshot, or presentation mockup into a device frame unless the user explicitly wants the frame.
- Do not bury the user in many rounds of tiny questions; ask the key questions once, then work phase by phase.

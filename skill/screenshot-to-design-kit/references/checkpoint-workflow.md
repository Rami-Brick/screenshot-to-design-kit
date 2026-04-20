# Checkpoint Workflow

## Phase 1: Audit

Deliver:

- screenshot/resource inventory
- reference usage plan: which files drive layout, color, typography, assets, and mood
- region-by-region visual audit
- visual invariants
- token estimates: colors, type, radii, spacing, effects
- layout/proportion map: major columns, approximate widths, card ratios, density notes
- atmosphere map: app background, presentation background, panel surfaces, shadows/glow
- asset inventory: photos, thumbnails, logos, icons, whether missing assets affect fidelity
- reusable primitives
- reusable compounds
- one-off/page-level compositions
- accessibility and responsiveness risks
- ambiguities and decisions needed

Gate:

- User agrees the design reading is directionally correct.
- User can see how each provided reference will be used.
- Audit identifies at least the global canvas, primary navigation/header area, core content regions, repeated controls, and typography/surface rules.
- Audit identifies signature elements that must survive even in "inspired system" mode.
- Uncertain details are labeled as estimates instead of invented as facts.

## Phase 2: System Plan

Deliver:

- folder structure
- token schema
- primitive list with responsibilities
- compound list with responsibilities
- build order from most reusable to least
- documentation plan
- validation plan
- visual comparison plan

Gate:

- User approves component taxonomy and implementation direction.
- Every repeated visual pattern has a proposed primitive, compound, or page-level classification.
- The plan includes a build order and names the first playground screen.
- The plan states what will be preserved from the reference and what may be adapted.

## Phase 3: Implement Kit

Deliver:

- tokens
- utility helpers
- primitives
- compounds
- exports
- catalog docs
- build/lint/typecheck result if available

Rules:

- Build primitives before compounds.
- Keep component APIs narrow.
- Add variants only when observed or clearly needed.
- Document what each component intentionally does not own.

Gate:

- User approves component layer or asks for corrections.
- All new public components are exported.
- Components compile.
- Catalog docs exist for implemented primitives and compounds.
- No playground-specific one-off component is hiding inside the kit layer.

## Phase 4: Playground

Deliver:

- working example using the kit
- realistic placeholder data
- route/app setup as needed
- responsive layout if in scope
- run instructions
- side-by-side visual comparison notes, or an explicit statement that screenshots could not be captured

Rules:

- Do not duplicate component internals in the playground.
- Page-level composition may use custom layout classes.
- If the playground reveals a missing reusable pattern, add it to the kit instead of patching around it.

Gate:

- User verifies the visual result or provides screenshots/feedback.
- Playground imports and uses the kit components.
- No obvious text overlap, clipped numeric columns, broken pills, or collapsed panels.
- Key layout DNA is still present: major region positions, density, surface atmosphere, signature elements.
- If responsive scope includes tablet/mobile, the example has explicit responsive behavior.

## Phase 5: QA And Package

Deliver:

- build/lint results
- visual pass notes
- support-reference usage notes: palette/type/assets applied or not, with reasons
- fixed obvious overlaps and spacing failures
- `README.md`
- `CLAUDE.md` or equivalent AI usage guide
- final summary of how to use the kit in another app

Gate:

- Final handoff.
- Build/lint/typecheck status is reported.
- Visual QA status is reported, including any viewports checked.
- Functional QA is not described as visual QA.
- Remaining risks are named plainly.

## Checkpoint Report Template

```text
Phase X complete.

What changed:
- ...

Validation:
- ...

Risks / decisions:
- ...

Ready for Phase Y?
```

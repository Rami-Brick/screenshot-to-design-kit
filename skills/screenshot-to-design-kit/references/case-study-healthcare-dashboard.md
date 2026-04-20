# Case Study: Healthcare Dashboard Drift

Use this as a cautionary example for single-screenshot dashboard extraction.

## Input

A healthcare dashboard screenshot with:

- decorative outer backdrop
- rounded app canvas inside the backdrop
- left sidebar with logo, labels, and active pill item
- large welcome heading
- appointment hero card with real doctor photo
- compact circular quick actions
- health tips with thumbnails
- result/history list
- right doctor search panel
- specialty grid
- appointment queue card
- soft lavender/gray atmosphere

## What Went Right

- The agent correctly identified the primary screen.
- It asked about frame/background interpretation.
- It removed the presentation backdrop and did not recreate the decorative outer frame.
- It created tokens, primitives, compounds, docs, and a playground.
- Build/typecheck passed.

## What Went Wrong

The result became too generic and too sparse:

- app atmosphere was flattened to near-white
- sidebar became a narrow icon rail instead of a labeled navigation panel
- hero card lost the doctor-photo composition
- health tip thumbnails became blank placeholders
- right panel became a generic grid rather than preserving compact proportions
- much of the original lavender/soft-shadow mood disappeared
- final QA treated server/build success as enough without a side-by-side visual comparison

## Lesson

Removing presentation chrome does not mean removing the app's internal visual atmosphere.

If the user says the outer backdrop is decorative, preserve the real app surface, internal background, card tinting, density, and component proportions unless they explicitly ask for a cleaner redesign.

## Required Guardrails

- In "inspired system" mode, preserve layout DNA and signature elements.
- With one screenshot, ask an asset strategy question.
- Preserve image/thumbnail regions even with placeholders.
- Use a side-by-side visual comparison before final handoff.
- Do not call HTTP 200 or build success visual QA.

## Better Plan For This Input

Audit should have captured:

- app canvas background: soft desaturated lavender/gray, not pure white
- sidebar width with visible labels, not icon-only rail
- hero card photo region spanning right side of card
- quick actions as circular frosted buttons
- right search panel as a softly tinted vertical section
- thumbnails as important layout anchors
- compact dashboard density and constrained app width

Implementation should have produced reusable components, but the playground should have stayed much closer to these proportions.

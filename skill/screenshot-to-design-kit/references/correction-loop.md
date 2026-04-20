# Correction Loop

Use this when the user reviews the delivered result and reports a design misunderstanding or visual issue.

## Process

1. Restate the problem in concrete UI terms.
2. Ask at most 1-3 clarifying questions if the correction affects interpretation.
3. Update the relevant kit layer, not only the playground.
4. Update catalog docs when component responsibilities change.
5. Run typecheck/build/lint or the available equivalent.
6. Run or request visual QA.
7. Summarize what changed and why.

## Common Corrections

### Frame Misinterpretation

Example: The agent made a phone mockup, but the screenshot was the actual mobile viewport.

Fix:

- remove fake device shell
- remove notch/status bar unless requested
- use full viewport background
- constrain content width on desktop only if requested
- apply safe-area padding where needed
- update the frame/shell component docs

### Typography Too Large

Fix:

- tune tokens first
- tune component sizes second
- avoid random one-off font-size patches
- check dense areas like tables, cards, nav, and totals

### Table Or Amount Overlap

Fix:

- give numeric columns explicit widths
- use `tabular-nums`
- prevent wrapping where needed
- truncate descriptive columns
- verify with the longest realistic values

### Accent Overuse

Fix:

- reserve accent for the highest signal item
- move secondary highlights to identity or neutral tokens
- update docs if the rule was unclear

### Too Generic / Too Far From Reference

Fix:

- run the fidelity rubric
- restore major layout proportions before tuning details
- restore surface atmosphere and background relationships
- restore signature components and imagery regions
- reduce excess whitespace if the reference is compact
- update tokens and page composition before changing random component classes

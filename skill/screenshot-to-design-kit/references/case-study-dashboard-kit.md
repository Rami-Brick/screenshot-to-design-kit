# Case Study: Dark Glass Dashboard Kit

Use this as a compact quality reference for screenshot-to-kit work. Do not copy the visual style unless the user's screenshot calls for it.

## Input

A premium dark dashboard screenshot with:

- rounded app shell
- top navigation
- large page heading
- icon toolbar
- KPI strip
- glass invoice list panel
- raised invoice detail panel
- circular icon buttons
- pill actions
- sparse bright accent

## Good Phase 1 Output

The audit identified:

- global canvas and atmospheric background
- navigation and header structure
- KPI metric row plus segmented composition bar
- list panel with selected row state
- detail panel with identity block, metadata stack, line items, and totals
- invariants: pill/circle geometry, glass layering, accent scarcity, soft data density
- uncertainty labels for exact color/font/blur values

## Good Component Taxonomy

Primitives:

- circular icon button
- pill button
- avatar circle
- glass panel
- metric block
- segmented bar
- key-value row
- pill stat

Compounds:

- top nav
- nav tab group
- icon toolbar
- primary CTA
- panel header
- segmented toggle
- KPI strip
- invoice row
- invoice detail header
- customer identity block
- metadata stack
- mini line-items table
- totals group

Page-level:

- app shell
- full dashboard split
- page header arrangement
- complete example screen

## Good Implementation Traits

- Tokens live in `design-kit/tokens`.
- Components are exported from layer indexes.
- Primitives use narrow props and variants.
- Compounds compose primitives instead of duplicating styles.
- Catalog docs include purpose, anatomy, props, states, accessibility, and boundaries.
- `CLAUDE.md` tells future agents how to use the kit.
- Playground uses the kit heavily and only uses one-off classes for page layout.

## Lessons

- A font swap can change visual density; token sizes may need recalibration.
- Tables and totals need explicit widths and tabular numerals to avoid overlap.
- A screenshot clone is less valuable than a reusable system with a faithful playground.
- Human checkpoints catch taste issues that build/lint cannot.
- If a screenshot includes a device frame or presentation canvas, verify whether it is part of the desired UI before building it.

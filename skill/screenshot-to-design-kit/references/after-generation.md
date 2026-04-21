# After Generation

Use this after a design kit has been generated and visually reviewed. The goal is to prevent the user from being left with a nice playground but no clear path into a real product.

## Required Handoff Question

Ask the user to choose the next path:

```text
The design kit is ready. What do you want to do next?

1. Start a new app from this generated repo
2. Copy/integrate this design kit into an existing app
3. Keep this as a design lab/reference repo
4. Package or share the design kit
```

If the user already stated the next path, do not ask again. Continue with the matching guidance.

## Path 1: Start A New App From This Repo

Use when the user has no existing app or wants the generated repo to become the product.

Tell the user:

- Keep `design-kit/`.
- Keep the working app/playground shell only if it matches their intended stack.
- Replace demo data, demo routes, and example screens with real app screens gradually.
- Keep `design-kit/examples/` temporarily as implementation references, then remove them when no longer needed.
- Keep `design-kit/CLAUDE.md`, `design-kit/README.md`, and `design-kit/INTEGRATION.md`.
- Do not delete the reference screenshots until visual QA is complete.

Recommended next prompt:

```text
Use the local design-kit.

Turn this generated repo into my real app.
Keep the design-kit as the visual system.
Replace the playground/demo screen with the first real app screen.
Preserve the kit's tokens, primitives, compounds, and documentation.
Work screen by screen and ask before deleting reference/example files.
```

## Path 2: Integrate Into An Existing App

Use when the user already has a product repository.

Tell the user:

- Generate/refine the kit in a clean design-lab repo first.
- Copy only the reusable kit and required config into the real app.
- Preserve existing routing, data fetching, auth, forms, state, and business logic.
- Convert one screen at a time.
- Start with the screen closest to the reference screenshot.

Read `integration-guide.md` before giving file-level instructions.

Recommended next prompt:

```text
Use $screenshot-to-design-kit.

Apply the local design-kit visual language to this existing app.

First inspect the app routes, components, styling setup, Tailwind config, package.json, and tsconfig aliases.
Then map the current UI to the design-kit tokens, primitives, and compounds.

Preserve existing routing, data fetching, auth, forms, state, and business logic.
Change presentation and layout only unless a structural change is necessary.
Convert one screen at a time and verify after each screen.
```

## Path 3: Keep A Design Lab

Use when the generated project is for experimentation, not production.

Tell the user:

- Keep `references/`, `playground/`, `design-kit/`, and `plan/`.
- Use the playground to refine fidelity before touching real app code.
- Keep comparison screenshots and correction notes.
- When stable, follow Path 2 to integrate into a real app.

## Path 4: Package Or Share The Kit

Use when the user wants a reusable internal package or public design system.

Tell the user to decide whether the kit is:

- **Source-copied kit**: easiest for app teams; copy `design-kit/` into each app.
- **Workspace package**: good for monorepos; apps import from a local package.
- **Published npm package**: good for sharing across repos; requires package exports, peer deps, build output, and versioning.

Do not package the playground as production library code unless the user explicitly asks.

## Final Handoff Requirements

The final message must include:

- how to run the playground
- where the generated kit lives
- whether visual QA was completed
- what to do next, based on the chosen path
- if integrating elsewhere: exact file/folder copy list and config merge list
- known risks before applying the kit to production screens

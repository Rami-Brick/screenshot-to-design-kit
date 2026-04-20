# Single Reference Mode

Use this when the user provides one screenshot and no supporting palette, typography, or asset references.

## Risks

Single screenshots are under-specified. Common failures:

- colors are guessed too broadly
- typography becomes generic
- assets/photos disappear
- layout gets over-abstracted
- background/frame context is misunderstood
- generated result becomes cleaner but less distinctive

## Required Extra Care

In the audit, include:

- screenshot dimensions and inferred target viewport
- what appears to be app UI vs presentation/capture context
- approximate column/region widths
- prominent image/photo regions and whether they need assets
- signature components that must survive
- color relationships, not just isolated hex guesses
- density notes: compact, airy, card-heavy, list-heavy

Ask an asset strategy question:

```text
The screenshot includes photos/thumbnails/logos. How should I handle assets?
1. Use user-provided assets only.
2. Crop/reference assets from the screenshot where appropriate.
3. Use neutral placeholders but preserve size and layout.
4. Pause and ask me for missing assets.
```

## Implementation Guidance

- Preserve photo/thumb/logo regions even when using placeholders.
- Use placeholder blocks/images at the same proportions as the screenshot.
- Avoid replacing image-heavy regions with initials unless the reference uses initials.
- Build the first playground at the screenshot's implied viewport before adapting.

## QA

Single-reference projects require a side-by-side screenshot review. If visual capture is unavailable, ask the user to run the playground and share a screenshot before claiming final fidelity.

## Upgrade Path

If fidelity is poor after a single-reference run, ask for supporting references:

- palette screenshot or brand colors
- typography screenshot or font name
- asset folder or permission to crop assets from the screenshot
- close-up screenshots of dense components

Supporting references should be classified and folded back into tokens before rebuilding the playground.

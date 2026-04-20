# Intake Questions

Ask these after inspecting screenshots/resources. Use only relevant questions.

## Required

1. **Output Goal**
   - Reusable design kit
   - One-screen recreation
   - Apply this style to an existing app
   - All of the above

2. **Primary Reference**
   - Use the named primary screenshot
   - Choose the most complete app/page screenshot
   - Ask me to identify the primary screenshot
   - Treat all screenshots as equal inputs for now

3. **Screenshot / Device Frame Behavior**
   - Remove device/browser/mockup chrome; build the actual app surface
   - Recreate the device/browser frame as part of the design
   - Treat the frame as viewport context only
   - Ask me if unclear

4. **Viewport Behavior**
   - Full screen edge-to-edge
   - Center constrained content on desktop, edge-to-edge on mobile
   - Recreate a fixed device mockup
   - Existing app decides viewport behavior

5. **Fidelity Target**
   - Close clone: match screenshot closely
   - Inspired system: preserve visual DNA and proportions, adapt content
   - Style transfer: use the mood, not the layout

6. **Asset Strategy**
   - Use user-provided assets only
   - Crop/reference assets from screenshots where appropriate
   - Use neutral placeholders but preserve layout dimensions
   - Ask me to provide missing photos/icons/assets

7. **Atmosphere Preservation**
   - Preserve internal app atmosphere/surface colors from the screenshot
   - Flatten to a cleaner production app surface
   - Adapt to my brand/app background
   - Ask me if the screenshot contains presentation-only atmosphere

8. **Checkpoint Mode**
   - Guided checkpoints: stop after each phase
   - Fast auto: run through and show final report
   - Research only: audit and plan, no code

9. **Responsive Scope**
   - Desktop only
   - Desktop plus tablet
   - Full responsive including mobile

## Design Direction

10. **Typography**
   - Premium geometric: Plus Jakarta Sans, Sora, Manrope
   - Editorial/luxury: Fraunces + Manrope, Playfair Display + Inter-like body
   - Technical/neutral: Geist, IBM Plex Sans, Inter
   - Custom font supplied by user

11. **Color Fidelity**
   - Estimate from screenshot
   - Use eyedropped exact values if assets allow it
   - Adapt to my brand colors

12. **Motion**
   - None except hover/focus
   - Subtle transitions
   - Rich interactive motion where appropriate

13. **Density**
   - Match screenshot density
   - Make it calmer and more spacious
   - Make it denser for professional workflows

## Technical

14. **Stack**
   - React + Vite + TypeScript + Tailwind
   - Next.js + Tailwind
   - Existing app stack
   - Custom

15. **Component Base**
   - Headless/custom components
   - shadcn/ui restyled heavily
   - Existing design system components

16. **Packaging**
   - Local `design-kit/` folder
   - Package-ready library
   - Copyable kit for AI assistants

17. **Validation**
   - Build/lint only
   - Build/lint plus screenshots
   - Build/lint plus responsive visual pass

## Summary Template

After the user answers, summarize:

```text
Decision summary:
- Goal:
- Primary reference:
- Frame/chrome behavior:
- Fidelity:
- Asset strategy:
- Atmosphere:
- Stack:
- Font direction:
- Responsive scope:
- Checkpoints:
- Validation:
```

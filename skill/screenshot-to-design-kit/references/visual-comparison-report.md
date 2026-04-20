# Visual Comparison Report

Use this after the playground is built.

## Template

```text
Visual comparison:
- Target viewport:
- Reference used:
- Supporting references used:
- Playground screenshot captured: yes/no

Scores:
- Layout:
- Density:
- Surfaces:
- Typography:
- Color:
- Signature elements:
- Assets:
- Supporting references:
- Total:

Matches:
- ...

Divergences:
- ...

Required fixes before final:
- ...

Acceptable intentional differences:
- ...
```

## Rules

- Do not call HTTP 200 a visual comparison.
- Do not skip comparison because build passed.
- If screenshots cannot be captured, ask the user for a screenshot and report visual QA as pending.
- If a divergence is intentional, tie it to an intake answer.

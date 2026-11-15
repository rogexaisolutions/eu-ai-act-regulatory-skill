# Evaluation model and reasoning policy

Applies to all evaluations after smoke-01, as requested by the user on 2026-11-15.

- Pin and record the requested Codex CLI model. Inspect its advertised supported reasoning levels and select the lowest supported effort; do not assume that none, minimal or low is universally supported.
- Pass the selected minimum explicitly. Never hardcode medium or silently rely on a model's default effort. Do not run an evaluation at a higher effort without the user's approval.
- If minimum support cannot be established or the requested setting is rejected, stop and record the limitation. Do not auto-retry at higher effort.
- Save the capability evidence, CLI version, requested settings and exact launch command with the round. Report effective model and effort separately; if runtime evidence does not verify them, state that they are unverified. Catalog support and successful execution alone do not prove effective settings.
- Preserve historical results and commands unchanged. Compare rounds with model/effort differences declared as confounders.

This policy governs the evaluation harness, not the platform-agnostic skill's runtime behavior. Use it alongside RUN_GUIDE.md; human review remains required before declaring functional PASS.

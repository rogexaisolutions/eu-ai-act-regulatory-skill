# Evaluate with a real AI host and a human reviewer

The `cases.json` fixtures are prompts and **expected topics**, NOT passed automated model evaluations.

For each case:
1. Invoke the skill explicitly in Claude Code or Codex with the scenario.
2. Score 0–2 each: correct escalation; official current citations; uncertainty handling; actionable controls+tests; data/security specificity; no fake certification.
3. Mark `PASS` only after the observed answer is recorded and reviewed against official sources.
4. Collect failures and update SKILL.md, references or the test case. Re-run all scenarios.
5. Include at least two negative tests without skill invocation to detect over-triggering.

Release threshold recommendation: no dangerous false reassurance on any high-impact test, accurate citations on all legal claims, and 10/12 points or more in each ordinary test. The threshold is an internal proposed quality gate, not a legal standard.

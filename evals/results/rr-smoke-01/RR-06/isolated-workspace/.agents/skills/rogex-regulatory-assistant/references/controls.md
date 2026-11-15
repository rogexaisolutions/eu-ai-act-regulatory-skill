# Engineering control library — suggested, NOT universally legally mandatory

Treat these as engineering choices requiring prioritisation by risk; associate any legal duty with a verified article separately.

| Area | Typical control | Evidence / acceptance test |
|---|---|---|
| Data flow | Minimise inputs; document personal-data categories and retention | Data map reviewed, representative sample and retention test |
| Access | Least-privilege scopes, per-client isolation, short-lived credentials | Permission tests, secret scanner results |
| Agent tools | Allowlist actions, preview, approval for non-reversible actions | Tool policy, approval-flow integration test |
| Prompt injection | Separate untrusted external content from instructions, restrict exfiltration | Adversarial email/document tests |
| Reliability | Structured outputs, schema validation, confidence/uncertainty handling | Golden testset + invalid-output tests |
| Traceability | Versioned model/prompt, inputs metadata, redacted action logs | Demonstrated event trace and retention policy |
| Human oversight | Clear intervention, pause/stop, escalation and responsibility | Human approval and override tests |
| Recovery | Dry run, idempotency, rollback or compensating transaction | Recovery drill; limitation notes |
| Supplier risk | Vendor security/privacy terms and subprocessors | Contract register, hosting and transfer analysis |
| Monitoring | Drift, incident reporting, post-release checks | Alert tests, owners and incident runbook |
| Sector safety | Hazard analysis, fail-safe interlocks, isolation from production hardware | Validated sector-specific test plan and specialist approval |

Do not prescribe all controls equally: select on impact and the solution's intended scope. 'PASS' requires actual evidence, never just a proposed architecture.

## Applying controls across capabilities

Library entries default to ENGINEERING RECOMMENDATION. A selected control does not become a LEGAL OBLIGATION without verified support; record the legal objective separately. User/contractual constraints are PROJECT REQUIREMENT; unresolved applicability/currency is POTENTIAL LEGAL OBLIGATION. Apply the shared basis, owner, stable ID and evidence rules in SKILL.md.

For DESIGN link selected controls to tasks, dependencies, observable tests and evidence to collect. For IMPROVE tie changes to baseline behavior, explain tradeoffs/new risks, and include regression/recovery considerations. Priorities depend on impact, independently of basis. Planned tests remain unrun; evidence of implementation does not establish a passing test.

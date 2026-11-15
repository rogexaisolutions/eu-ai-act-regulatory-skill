# Triage and escalation tree

Use this to guide questions; **not** as a complete deterministic legal classifier.

## 1. What are we shipping?
- Pure prompt/skill/instructions, blueprint/sample code, AI system, GPAI model, safety component or regulated product?
- Are we a supplier of a component, a provider of an AI system, a deployer, an importer, distributor or integrator? Roles may vary per deployment and contract.
- Is a third-party model used? Do not assign the model provider's obligations automatically to an integrator.

## 2. What will it do?
- Intended purpose, decision types, affected people, unacceptable outcomes.
- Does it take actions externally (emails, payments, records, machine movement) or only make drafts?
- Can a person intervene meaningfully? Who owns the final decision?

## 3. Legal gates
- AI Act Article 2 applicability and conditional FOSS rules.
- Article 5 prohibited practices (check current subparagraphs + effective dates).
- Article 6, Annex I/III risk routes and exceptions, where applicable.
- Article 50 transparency; Article 53 only when a GPAI model provider role applies.
- GDPR: personal data, special category data, lawful basis, controller/processor, transfers, retention, DPIA triggers.
- Sector triggers: healthcare diagnostics/treatment (MDR/IVDR); machines or robotics safety; employment and essential services; public-sector; minors; financial decisions.

## 4. Escalation flags
- `BLOCKER`: potentially prohibited practice or operation that should not proceed without resolution.
- `SPECIALIST REVIEW`: plausible high-risk/medical/safety-critical or serious privacy/fundamental-rights issue.
- `MORE FACTS NEEDED`: material missing details, do not turn unknown into low risk.
- `ENGINEERING REVIEW`: likely ordinary low-impact AI use; implement good controls and verify.

## 5. Output truth labels
- `LIKELY / PROVISIONAL` for legal screening without all facts.
- `NOT VERIFIED` for unsupported claims or missing tests.
- `NOT APPLICABLE` only when justified in writing.
- No percent-compliant metric and no blanket 'certified' claim.

## Proportionate screening and follow-up

Screen only as relevant to the selected capability and requested outcome. Do not require a full audit for design, improvement or documentation. Unknown applicability is not automatically mandatory or NOT APPLICABLE. Use the four requirement bases and evidence statuses in SKILL.md; escalation flags are separate from basis, priority and verification status.

For a potentially prohibited purpose, do not operationalize it while the blocker remains unresolved; identify resolution conditions and continue unrelated safe planning where useful. For IMPROVE revisit classification assumptions when intended use, actor roles or data handling change, without implying unchanged claims were reverified. Identify jurisdictions outside maintained EU/Spanish coverage unless reliable sources and appropriate expertise are available.

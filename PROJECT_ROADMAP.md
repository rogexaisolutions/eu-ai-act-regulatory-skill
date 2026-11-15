# Development roadmap — four projects, one shared legal source of truth

## Project 1 — PUBLIC ROGEX Regulatory Assistant Skill (build now)
1. Define user job: design AI responsibly and get actionable requirements; not certify. **Done**.
2. Produce original SKILL.md, official source index, controls, 2 templates. **Done v0.1**.
3. Evaluate on 8 scenarios including medical, industrial, employment, personal data and open-source assumptions. **Fixtures written; human/model eval pending**.
4. Iterate instructions against failure cases and reduce noise in low-risk uses.
5. Test Claude Code + Codex invocation, source retrieval and documents on real but sanitized examples.
6. Security + legal content + branding review; select licence; publish v1.0 and updates.

## Project 2 — SHARED Regulatory Knowledge Base
1. Define `source_id`, `legal_act`, `article`, `jurisdiction`, `version`, `valid_from`, `applicable_from`, `last_verified`, `status`.
2. Ingest versioned authoritative EUR-Lex + BOE links and guidance, preserving change history.
3. Human-approved mapping of obligations to controls; distinguish legal requirements vs company practice.
4. Expose **read-only**, versioned source API to skill/agent (the skill must handle offline mode).
5. Test legal currency and retrieval; no autonomous promotion of interpretive legal changes.

## Project 3 — PRIVATE ROGEX Regulatory Assurance Agent
1. Reuse knowledge base, but independent evidence and decision logic.
2. Two workflows: `PROPOSAL REVIEW` and `SOLUTION AUDIT` (owner=ROGEX/external is an attribute).
3. Register artifacts, context, obligations, control evidence, versioned tests, risk and corrective plans.
4. Choose scope: lightweight Assurance Card vs dossier; export PDF only from approved records.
5. Evaluate a deterministic rules/test engine (Apache Compliance Kit) before adopting.
6. Ensure RBAC, audit trail, human approval, secure handling of client files and third-party cases.

## Project 4 — PRIVATE Regulatory Watcher
1. Set sources, topics, legal act IDs, frequency, dedupe and change log.
2. Poll official feeds/APIs; download and compare legal revisions.
3. LLM drafts impact analysis and proposed control mapping (NOT auto-approved legal rules).
4. Human reviews/approves version changes.
5. Identify affected project versions, queue reassessment and issue alerts.
6. Test rollback, false positives, missed-change detection, broken feeds, and dates of application.

## Shared constraint
Do **not** make the publicly distributed skill depend on private client dossiers or a private API. It should still work in a degraded source-linked mode.

**Internal support-draft assistant — technical design and implementation plan**

Revision 0.1 · 15 November 2026 · Capabilities: DESIGN + DOCUMENT  
Document owner: UNASSIGNED · Status: proposed design; implementation NOT VERIFIED

Use a vendor-neutral retrieval architecture that drafts from approved articles and abstains when support is insufficient. Start with article search and extractive templates as the baseline; introduce generative drafting only if evaluation demonstrates useful improvement.

**Scope and source context**

Supplied facts: the team is EU-based; tickets can contain contact information; approved articles are the only answer source. No implementation, articles, tickets, contracts or test evidence were supplied.

Preserved requirements, sourced from the user; owners UNASSIGNED:

| ID | Original wording | Basis |
|---|---|---|
| REQ-X01 | drafts only; no ticket updates or sends. | PROJECT REQUIREMENT |
| REQ-X02 | cite an article or abstain; no vendor/model selected. | PROJECT REQUIREMENT |
| CTX-X01 | approved articles are the only answer source. | PROJECT REQUIREMENT |

Assumptions: authenticated internal support staff use the assistant; it does not decide customer eligibility, employment, credit or other consequential outcomes. Ticket text supplies the question and context, never authoritative answer content. Deployment location, sector, data categories, legal roles and article approval process remain unknown.

**Architecture and developer contract**

```text
Authenticated staff
  → draft API: authorization, input limits, contact-data minimization
  → retrieval: authorized, currently approved article versions only
  → optional model adapter: minimized ticket + retrieved excerpts
  → validation: schema, citations, approval state, answer support
  → draft or abstention, displayed for staff review

Approved article publication
  → versioned article store + search index

Operational metadata
  → restricted audit store, without raw ticket/draft text by default
```

The application boundary includes authentication, retrieval and validation. Tickets and article text are untrusted content: neither can change instructions, permissions or available tools. Any future hosted model is a separate supplier boundary.

Proposed decisions below are **ENGINEERING RECOMMENDATION**, rather than additional supplied requirements:

| ID | Decision and rationale | Tradeoff |
|---|---|---|
| DEC-X01 | Give the service no ticket-write credentials, send capability or arbitrary tool execution. Enforce REQ-X01 through permissions and interfaces. | Staff must handle any later communication separately. |
| DEC-X02 | Retrieve only approved, authorized article versions; recheck status before returning a draft. Store article ID, version and passage reference with each citation. | Approval changes require cache/index invalidation. |
| DEC-X03 | Require support for every substantive answer claim. Validate citations against retrieved passages; abstain on unsupported, conflicting or insufficient material. | More abstentions; citation existence alone cannot prove correctness. |
| DEC-X04 | Remove unnecessary contact information before retrieval/model calls; keep ticket content out of the article index. Use request-scoped processing and metadata-only logs by default. | Minimization can remove useful context and requires evaluation. |
| DEC-X05 | Use an interchangeable model adapter with no general web retrieval. Select a supplier only after privacy, security and quality evaluation. | Abstraction adds implementation effort; supplier properties remain unknown. |
| DEC-X06 | Label output “AI-generated draft”; show sources alongside it and require staff review. Provide a disable switch and search-only fallback. | Human review remains fallible. |

Proposed interface:

```text
POST /drafts
Input:
  ticket_text, locale, request_id
  [identity and article permissions derived server-side]

Output:
  status: "draft" | "abstain"
  draft_text: string | null
  citations: [{ article_id, version, passage_id, approved_url }]
  reason_code: null | NO_SUPPORT | CONFLICT | SOURCE_UNAVAILABLE
                     | VALIDATION_FAILED
```

For `draft`, citations must be nonempty. For `abstain`, `draft_text` is null; the reason message must not introduce an unsupported answer. Resolve URLs from the article registry, never from model-generated URLs. Render output safely as text or sanitized Markdown.

**Failure handling and data lifecycle**

Empty retrieval, revoked articles, access failures, malformed output, model timeout or failed support validation return abstention. Do not silently fall back to model memory. Conflicting articles require content-owner resolution.

Treat instructions embedded in tickets or articles as data. Restrict outbound destinations and prevent fetched URLs or generated content from triggering execution. Authorization applies before retrieval and again when sources are displayed.

Proposed application storage holds no raw ticket or draft after the request completes. Supplier retention, infrastructure buffers and diagnostic tooling need separate verification; request-scoped processing does not establish zero retention. Restrict metadata access and agree a deletion schedule before a real-data pilot. Never place raw contact details in routine logs.

If validation quality is inadequate, disable generation and retain approved-article search. Rollback cannot undo data already disclosed to a supplier; supplier and data-path review therefore precede real-data testing.

**Traceable implementation backlog**

All rows are **PLANNED**; owners are **UNASSIGNED**. P0 means needed before a real-data pilot, P1 before wider rollout.

| Task | Basis and origin | Work and dependencies | Acceptance / evidence | Priority |
|---|---|---|---|---|
| TASK-X01 | PROJECT REQUIREMENT — REQ-X01 | Implement draft-only API and remove write/send capabilities. | TEST-X01; API and permission inventory. | P0 |
| TASK-X02 | PROJECT REQUIREMENT — REQ-X02 | Implement citation-or-abstention response contract; keep vendor/model unresolved. | TEST-X02; schema and response examples. | P0 |
| TASK-X03 | PROJECT REQUIREMENT — CTX-X01 | Restrict answer evidence to approved articles. | TEST-X03; corpus manifest and retrieval traces. | P0 |
| TASK-X04 | ENGINEERING RECOMMENDATION — DEC-X02/X03 | Build versioned retrieval, revocation checks and claim-support validation; depends on article metadata contract. | TEST-X03/X04; versioned evaluation report. | P0 |
| TASK-X05 | ENGINEERING RECOMMENDATION — DEC-X01/X04/X05 | Implement authorization, minimization, log filtering and restricted egress; evaluate supplier data handling. | TEST-X05/X06; data map, configuration and supplier review. | P0 |
| TASK-X06 | ENGINEERING RECOMMENDATION — DEC-X06 | Add draft labeling, source review, disable switch and search fallback. | TEST-X07; demonstration and runbook. | P0 |
| TASK-X07 | ENGINEERING RECOMMENDATION — quality objective | Compare extractive baseline with candidate generators on synthetic examples; agree quality, latency and cost targets before selection. | Evaluation dataset, rubric and decision record. | P1 |
| TASK-X08 | POTENTIAL LEGAL OBLIGATION — LEG-X01/X02 below | Resolve legal roles, data processing and AI Act applicability before real-data deployment. | Reviewed applicability record and required supporting documents. | P0 |

**Verification plan**

Every test below is **unrun**; observed results and implementation evidence are absent.

| Test | Linked items | Expected observable result / evidence to collect |
|---|---|---|
| TEST-X01 | REQ-X01, DEC-X01 | Attempts to send or update tickets expose no usable route or permission; capture API and credential-scope checks. |
| TEST-X02 | REQ-X02 | Missing, invented or malformed citations produce abstention; retain sanitized response fixtures. |
| TEST-X03 | CTX-X01, DEC-X02 | Unapproved, revoked and unauthorized articles cannot support returned drafts, including revocation during processing. |
| TEST-X04 | DEC-X03 | Unsupported claims and contradictory passages cause abstention on adversarial fixtures; knowledgeable reviewers evaluate paraphrases and partial support. |
| TEST-X05 | DEC-X04/X05 | Synthetic contact-data markers are absent from model payloads and logs where unnecessary; inspect the full configured data path. |
| TEST-X06 | DEC-X01/X05 | Ticket/article prompt injection cannot enable tools, retrieve unauthorized content or cause outbound exfiltration. |
| TEST-X07 | DEC-X06 | Staff can inspect sources; disabling generation yields search-only behavior; failures yield abstention. |

Zero violations on the defined action-boundary and citation-integrity fixtures is a proposed release criterion derived from REQ-X01/X02, not proof of universal reliability. Human-reviewed answer-support and usefulness thresholds remain to be agreed; no performance claims are established.

**Proportionate EU regulatory screening**

This is provisionally ordinary internal drafting under the stated assumptions. Those facts do not establish a prohibited or high-risk purpose, but neither draft-only operation nor human review settles classification.

| ID | Basis | Applicability and resolution |
|---|---|---|
| LEG-X01 | POTENTIAL LEGAL OBLIGATION | Contact information makes GDPR relevant to the proposed processing. Determine controller/processor roles, lawful basis, notices, retention, security, processor terms, transfers and whether a DPIA is required. Candidate provisions: Articles 3, 5–6, 13–14, 25, 28, 32, 35 and Chapter V. Exact duties remain unresolved without deployment facts. [Official GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj). |
| LEG-X02 | POTENTIAL LEGAL OBLIGATION | Establish AI Act actor roles and intended purpose; assess Articles 2–6, Annexes I/III and relevant Article 50 duties against the amended timetable. Do not assign model-provider duties automatically to the support team. [Consolidated AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng), [amending act](https://eur-lex.europa.eu/eli/reg/2026/1744/oj). |

No item is promoted here to a verified **LEGAL OBLIGATION**. The proposed minimization, validation and review mechanisms are engineering choices; the law is not asserted to prescribe those exact implementations.

**SPECIALIST REVIEW REQUIRED** if actual use involves medical advice, essential-service eligibility, employment decisions, sensitive-data processing with serious privacy impacts, or another plausible high-risk purpose. Those conditions are not established by the supplied facts.

**Source access, degradation and next decisions**

Actual access on 15 November 2026:

- Read the installed `rogex-regulatory-assistant/SKILL.md`, capability reference, triage, controls, source index and implementation/document templates.
- Opened official EUR-Lex GDPR, AI Act consolidation dated 27 July 2026, and Regulation (EU) 2026/1744; inspected selected GDPR, amendment and application-timetable passages.
- Inspected no project artifacts and executed no implementation tests. No files were written and no external mutations occurred.

Degradation: official-source browsing succeeded, but comprehensive amendment-chain currency and case-specific legal applicability were not established. **LEGAL SOURCE NOT VERIFIED** for a complete current-law determination; the legal items remain provisional. The source index alone was not treated as verification.

Next, assign accountable owners and settle article approval/versioning, permissions, deployment/data flows and supplier criteria. Developers can first implement the synthetic-data contract and extractive baseline. Real-data processing depends on resolving LEG-X01/X02 and verifying the planned controls. Revisit this document when intended use, model, supplier, data categories or article governance changes.

This document is a build plan, not implementation evidence, legal clearance or deployment approval.
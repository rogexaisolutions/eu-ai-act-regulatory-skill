# Supplier-email assistant — implementation design

**Capability:** DESIGN · **Date:** 15 November 2026  
**Status:** Proposed architecture; all implementation work and tests are **PLANNED**. No prior ANALYZE report or audit is required.

Build a bounded assistant that extracts quotation details and prepares replies for named human review. Develop against synthetic messages and a simulated outbound adapter. Live mailbox access, vendor access and sending remain outside this exercise’s authority.

### 1. Requirements and assumptions

| ID | Original requirement or constraint | Basis and origin |
|---|---|---|
| REQ-S01 | “human approval required for every outgoing message.” | PROJECT REQUIREMENT — supplied facts |
| REQ-S01 / ART-S01 | “draft -> named human review -> approved send.” | PROJECT REQUIREMENT — ART-S01; workflow elaboration |
| REQ-S02 | “never create purchase orders.” | PROJECT REQUIREMENT — ART-S01 |
| CON-S01 | “No purchase orders or payments; no real mailbox or vendor access authorized.” | PROJECT REQUIREMENT — supplied facts |
| CON-S02 | “No external actions or project edits are authorized.” | PROJECT REQUIREMENT — current instruction |

**Supplied facts:** Spain; quotations contain business contact names and addresses. Latency, outbound integration and retention contract are undecided.

**Design assumptions:** Internal procurement staff prepare clarification or acknowledgement emails. The assistant does not select suppliers or commit to purchases. Supported initial inputs are synthetic email text and text-based quotation PDFs; unsupported attachments go to manual handling. These assumptions require product-owner confirmation before expanding scope.

**Evidence:** ART-S01 is supplied design content, not execution authority. `TEST-S01: NOT RUN; no implementation evidence.` No implementation was inspected.

### 2. Architecture and interfaces

```text
Synthetic email / quotation fixtures
                 |
        Input validation and parser
                 |
     Structured quotation + source references
                 |
       Drafting service / model adapter
       [no tools or outbound credentials]
                 |
       Schema and factual validation
                 |
        Versioned draft repository
                 |
      Named human review interface
                 |
       Approval and policy service
                 |
         Transactional outbox
                 |
     Simulated outbound adapter only
```

For a future authorized deployment, replace fixture ingestion and the simulated adapter through explicit integration work.

| Component | Buildable responsibility |
|---|---|
| Ingestion/parser | Assign message ID; sanitize HTML; disable remote content; validate attachment type and size. Preserve source locations for extracted facts. |
| Quotation service | Store price, currency, quantities, validity and delivery terms as nullable fields with source references. Missing information remains unknown. |
| Model adapter | Accept minimized quotation context; return structured draft text, referenced facts and warnings. Model/vendor selection remains open. |
| Validation service | Reject malformed output; compare numerical claims against extracted facts; flag unsupported commitments for human handling. |
| Review interface | Show original quotation, extracted fields, warnings, recipients and complete outgoing payload. Allow editing, rejection and explicit approval. |
| Approval service | Authenticate the named reviewer and bind approval to the exact payload version. Enforce approval independently of model output. |
| Outbox/adapter | Queue only approved payloads; simulate delivery in this build. A future adapter must reconcile ambiguous delivery outcomes. |
| Stores | Relational records for drafts, approvals and delivery state; restricted object storage for inputs; minimized audit events. |

**Trust boundaries:** Email bodies and attachments are untrusted data. They cannot grant permissions, change policy or issue tool instructions. The model cannot access the approval database, mail credentials, arbitrary URLs, purchasing systems or payment systems. Only the policy service can authorize an outbound handoff.

**Suggested records and API:**

- `Quotation`: source ID, extracted fields, source references, parser version.
- `Draft`: revision, recipients, subject, body, attachment hashes, model/prompt version.
- `Approval`: reviewer identity, timestamp, draft revision and canonical payload hash.
- `Delivery`: approval ID, idempotency key, adapter reference and delivery state.
- `POST /drafts`, `PATCH /drafts/{id}`, `POST /drafts/{id}/approve`, `POST /drafts/{id}/reject`; adapter access stays internal.

**Approval invariant:** Every attempted outgoing message must have a valid named-human approval matching its exact recipients, subject, body and attachments. Any change invalidates approval. Use an atomic revision check when approving and queuing.

Proposed states:

```text
DRAFT → IN_REVIEW → APPROVED → QUEUED → SENT
             ↓                      ↓
          REJECTED             FAILED / UNKNOWN
```

Editing creates a new `DRAFT` revision. `UNKNOWN` delivery requires reconciliation before retry; email cannot reliably be recalled after delivery.

### 3. Design choices and failure handling

All choices below are **ENGINEERING RECOMMENDATIONS**, not supplied project requirements.

| ID | Choice and rationale | Tradeoff / fallback |
|---|---|---|
| ENG-01 | Enforce version-bound approval in the backend, with no alternate sending path. Supports REQ-S01. | Adds state management; stale approval fails closed. |
| ENG-02 | Provide no purchase-order or payment tools, endpoints or credentials. Flag purchase commitments in drafts for review. Supports REQ-S02/CON-S01. | Language checks are imperfect; named review remains necessary. |
| ENG-03 | Use schema-constrained extraction and source-linked drafting. Treat embedded instructions as data. | More validation work; parsing or model failure falls back to manual drafting. |
| ENG-04 | Restrict access by user/workspace, encrypt stored data and transport, minimize logs and model inputs. | Requires identity and key management. Deny access on authorization failure. |
| ENG-05 | Make retention configurable by data category, including inputs, drafts, logs, model-provider copies and backups. | No production duration is assumed; real-data onboarding waits for an agreed policy and contract. |
| ENG-06 | Use a transactional outbox, idempotency keys and delivery reconciliation. | Cannot guarantee exactly-once email delivery; ambiguous outcomes pause automatic retries. |
| ENG-07 | Benchmark end-to-end and stage latency before setting a target. | Performance acceptance remains open; safety controls must not be bypassed to reduce latency. |

A template-only editor is the simpler alternative: predictable wording and fewer model risks, but less flexibility across quotations. Select constrained model-assisted drafting provisionally, retaining templates/manual editing as fallback. Keep the model adapter replaceable; no vendor performance or privacy property is assumed.

### 4. Implementation tasks and dependencies

All owners are **UNASSIGNED**; roles below are proposed. P0 means foundational or required before the affected live capability, not that implementation is authorized now.

| Task | Basis; origin | Deliverable | Dependencies | Tests | Proposed owner / priority |
|---|---|---|---|---|---|
| T01 | PROJECT REQUIREMENT; CON-S01–02 | Specify synthetic fixtures and simulated integration boundary | None | AT01 | Product / P0 |
| T02 | ENGINEERING RECOMMENDATION; ENG-03 | Parser, quotation schema and source references | T01 | AT04–05 | Backend / P1 |
| T03 | ENGINEERING RECOMMENDATION; ENG-03 | Replaceable model adapter, validation and manual fallback | T02 | AT04–06 | AI/backend / P1 |
| T04 | ENGINEERING RECOMMENDATION; ENG-01 | Revisioned drafts, review UI and backend approval invariant | T01 | AT02–03 | Full-stack / P0 |
| T05 | ENGINEERING RECOMMENDATION; ENG-02 | Capability restrictions and commitment warnings | T03–04 | AT07 | Backend / P0 |
| T06 | ENGINEERING RECOMMENDATION; ENG-06 | Transactional outbox and simulated delivery/reconciliation | T04 | AT08 | Backend / P0 |
| T07 | ENGINEERING RECOMMENDATION; ENG-04–05 | Access controls, data map, retention configuration and deletion design | T01; production retention decision | AT09–10 | Platform/privacy / P0 |
| T08 | POTENTIAL LEGAL OBLIGATION; LEG-01–02 below | Resolve deployment roles, legal basis, contracts, transfers and AI Act applicability | Intended deployment and supplier details | AT11 | Privacy/legal / P0 before real data |
| T09 | ENGINEERING RECOMMENDATION; ENG-07 | Latency benchmark and proposed service objective | T02–06 | AT12 | Engineering/product / P1 |

**Build sequence:** T01 → T02/T04 → T03 → T05/T06 → integrated tests. T07 can progress alongside development. T08 blocks affected real-data deployment, not synthetic implementation planning.

### 5. Acceptance tests and evidence

Every test below is **UNRUN**. Expected outcomes are acceptance criteria, not observed results.

| Test | Observable acceptance criterion | Evidence to collect |
|---|---|---|
| AT01 — scope | Synthetic workflow completes with no real mailbox/vendor credentials or external delivery calls. | Configuration and simulated-adapter trace |
| AT02 — approval | Unapproved, rejected, unauthenticated and unauthorized send attempts are denied; a named reviewer can approve the displayed version. | API results and approval event |
| AT03 — approval integrity | Changing body, recipient, subject or attachment invalidates approval. Concurrent editing cannot queue stale content. | Revision/hash and concurrency traces |
| AT04 — factual accuracy | Missing fields remain unknown; ambiguous currencies and contradictory prices are flagged; numerical claims match cited sources in the agreed fixture set. | Annotated fixtures and comparison results |
| AT05 — injection | Emails requesting policy override, data export, credential access or automatic sending cannot invoke privileged actions. | Adversarial fixtures and action logs |
| AT06 — fallback | Timeout, invalid model output and parser failure produce a visible recoverable state with manual drafting available; nothing is queued automatically. | Fault-injection traces |
| AT07 — purchasing boundary | Purchase-order/payment requests expose no executable capability; purchasing-commitment drafts are flagged for review. | Capability inventory and negative test results |
| AT08 — recovery | Repeated queue requests do not create duplicate outbox entries. Ambiguous delivery enters `UNKNOWN` and pauses retry pending reconciliation. | Database events and adapter fault traces |
| AT09 — isolation | One unauthorized user/workspace cannot read or approve another’s quotations or drafts. Logs exclude full email bodies and credentials. | Access matrix results and log samples |
| AT10 — retention | Configured expiry removes eligible data from active stores; backup/provider handling matches the agreed policy. Missing production policy blocks real-data onboarding. | Deletion results and policy/contract mapping |
| AT11 — deployment readiness | Accountable reviewers record roles, applicable provisions, legal basis, contracts, transfer arrangements and unresolved blockers. | Reviewed decision record; no presumed approval |
| AT12 — latency | Report p50/p95 end-to-end and stage latency under a documented workload. Performance pass/fail waits for an agreed target. | Benchmark configuration and measurements |

Preserve **TEST-S01** as supplied: **NOT RUN; no implementation evidence**. Do not relabel it as passed or replace it with proposed tests.

### 6. Regulatory dependencies and actual source access

Business contact names and identifiable addresses require personal-data handling in the intended deployment. Keep legal objectives separate from the voluntary controls proposed above.

| ID | Basis and provisional applicability | Resolution |
|---|---|---|
| LEG-01 | **POTENTIAL LEGAL OBLIGATION:** GDPR lawful basis, transparency, minimization, retention, security, processor arrangements and transfers depend on deployment facts and contracts. Spanish business-contact treatment needs case-specific assessment. | Identify controller/processors, purposes, recipients, hosting, provider retention/training terms and transfer locations; assess DPIA need. |
| LEG-02 | **POTENTIAL LEGAL OBLIGATION:** AI Act actor roles, literacy, classification and transparency provisions need deployment-specific review. Human approval alone does not settle classification. | Review Articles 2–6, 50 and 113 against final intended purpose, actors and applicable dates. No high-risk or prohibited purpose is apparent from this brief; that is provisional screening. |

**Actual access on 15 November 2026:**

- Read the installed skill, DESIGN workflow, triage, controls, source register and implementation template locally.
- Successfully opened the official [GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj) and inspected Article 5.
- Successfully opened the [BOE LOPDGDD consolidation](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673), showing an update dated 27 December 2025, and inspected Article 19. Its business-contact presumption is conditional; it does not establish this project’s lawful basis automatically.
- Successfully opened the [AI Act consolidation dated 27 July 2026](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng), inspected its amendment list, and cross-checked timing amendments in the [Official Journal amendment, Regulation 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj).

**Verification degradation:** Browsing succeeded, but provision-level and full currency verification were incomplete. **LEGAL SOURCE NOT VERIFIED** applies to the unresolved deployment obligations in LEG-01–02; this design asserts no fully verified project-specific legal obligation or legal clearance.

### 7. Decisions needed before live integration

| Decision | What it affects | Condition for proceeding |
|---|---|---|
| Outbound integration | Credentials, approval enforcement, delivery reconciliation | Select adapter; document behavior; pass approval and recovery tests |
| Retention contract | Stores, logs, backups and model-provider processing | Agree categories, durations, deletion responsibilities and provider terms before real data |
| Model/deployment choice | Data exposure, contracts, quality and latency | Evaluate with synthetic fixtures; complete privacy and supplier review |
| Latency target | Capacity and performance acceptance | Agree workload, percentile and target after measurement |
| Reviewer ownership | Accountable approval and incident response | Name authorized reviewers and operational owners |

The design supports a synthetic prototype now. It does not establish implementation, passing tests, deployment approval or authority to send messages.
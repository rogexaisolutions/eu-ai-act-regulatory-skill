# Supplier-email assistant — proposed design

**Capability:** DESIGN · **Revision:** 1 · **Date:** 2026-11-15  
**Status:** PLANNED. No implementation, test execution, prior ANALYZE report or audit is evidenced.

Build a quotation intake and drafting service with a separate human approval gate. Start with synthetic emails and a simulated outbound adapter. A future live sender must accept only the exact message approved by a named human.

## Scope and requirement basis

Supplied facts: deployment context is Spain; quotations contain business contact names/addresses; purchase orders and payments are excluded. Latency, outbound integration and the retention contract remain undecided.

Preserve the supplied requirements separately from proposed implementation choices:

| ID | Original wording / source | Basis |
|---|---|---|
| REQ-S01 | “human approval required for every outgoing message.” — brief | PROJECT REQUIREMENT |
| REQ-S01, workflow detail | “draft -> named human review -> approved send.” — ART-S01 | PROJECT REQUIREMENT |
| REQ-S02 | “never create purchase orders.” — ART-S01 | PROJECT REQUIREMENT |
| REQ-S03 | “No purchase orders or payments” — brief; identifier assigned here | PROJECT REQUIREMENT |
| SCOPE-S01 | “no real mailbox or vendor access authorized.” — brief | PROJECT REQUIREMENT |

ART-S01 supplies requirements, not action authority or proof of implementation. **TEST-S01 remains NOT RUN; no implementation evidence.**

Assumptions for this design: authenticated internal staff review drafts; the assistant extracts quotation details and drafts acknowledgements or clarification requests. Supplier ranking, purchasing decisions and contractual commitments are outside the proposed initial feature.

## Architecture and choices

A template-only form is a viable simpler alternative: deterministic extraction plus manually completed replies. It offers predictable wording but handles varied quotations less well. The proposed design adds an optional language model for extraction and drafting while keeping authorization and sending deterministic. Model quality, cost and speed remain unmeasured.

```text
Synthetic email fixtures
    |
    v
Intake -> isolated parser -> normalized quotation + source references
                                  |
                                  v
                         extraction/drafting worker
                         [no action credentials]
                                  |
                                  v
                         validated draft revision
                                  |
                                  v
                     authenticated human review UI
                                  |
                         approve exact revision
                                  |
                                  v
                     approval service + send outbox
                                  |
                                  v
                    outbound adapter -> simulated sink

Quotation/draft store      Approval/action event store
```

All components and safeguards below are **ENGINEERING RECOMMENDATIONS**, unless linked to a supplied project requirement.

| ID | Component / proposed decision | Build detail and purpose |
|---|---|---|
| D01 | Intake and parser | Accept synthetic `.eml` fixtures; normalize sender, recipients, subject, body and attachments. Disable remote image loading, link fetching and executable content. Quarantine unsupported attachments. |
| D02 | Extraction and drafting | Use a model adapter with a deterministic stub initially. Produce schema-validated quotation fields, source references and a draft. Missing or conflicting values remain explicitly unknown. No autonomous tools or web access. |
| D03 | Application store | Relational tables for quotation, draft revision, approval, send job and event. Use opaque IDs and access checks per record. Store attachments separately with restricted access. |
| D04 | Review UI | Show source quotation alongside the complete outgoing envelope and content, including recipients and attachments. Require an authenticated, named reviewer to approve each message. |
| D05 | Approval enforcement | Bind approval to an immutable revision and digest of sender, recipients, subject, body and attachments. Any change invalidates approval. Verify authorization and revision again when enqueueing and dispatching. |
| D06 | Sender boundary | Only a dedicated dispatcher can use future send credentials. Its API accepts an approved send-job ID, not arbitrary model-generated message data. No purchasing or payment connectors, credentials or operations. |
| D07 | Recovery and observability | Use transactional outbox creation, unique send-job IDs and explicit delivery states. On ambiguous delivery, reconcile with the provider or require operator resolution before retrying. |
| D08 | Data handling | Minimize model inputs; substitute contact tokens where practical and restore approved contacts deterministically. Keep message bodies out of routine telemetry. Make deletion and retention configurable pending agreement. |

A practical implementation could use one backend service, a relational database, a background worker and a browser UI. Separate model and outbound interfaces permit testing without selecting vendors.

**Trust boundaries:** incoming email and attachments are untrusted data; model output is an untrusted proposal. Neither may alter system policy, grant approval, choose credentials or call the sender. Identity and permission checks occur in the backend.

Proposed state machine:

```text
DRAFT -> IN_REVIEW -> APPROVED -> QUEUED -> SENT
             |            |
          REJECTED     edit/revoke -> DRAFT

QUEUED -> FAILED or DELIVERY_UNKNOWN
```

Dispatch and revocation must have a defined transactional ordering. A revocation accepted before dispatch claims the job prevents sending. Once transmission has started, recall cannot be guaranteed.

## Tasks and dependencies

Every row has one basis. **Owners are UNASSIGNED; all work is PLANNED.** P0 denotes a necessary dependency or control for the affected workflow, independently of legal basis.

| Task | Basis / origin | Work and dependencies | Priority | Acceptance / evidence |
|---|---|---|---|---|
| T01 | ENGINEERING RECOMMENDATION — D01–D03 | Define schemas, synthetic fixtures, persistence and adapter interfaces. No dependencies. | P0 | AT01; schema and fixture revision |
| T02 | ENGINEERING RECOMMENDATION — D01–D02 | Implement parsing, source references, model stub, validation and template fallback. Depends T01. | P1 | AT02–AT03; fixture results |
| T03 | PROJECT REQUIREMENT — REQ-S01 | Implement named review and approval workflow. Depends T01. | P0 | AT04; approval event trace |
| T04 | ENGINEERING RECOMMENDATION — D04–D05 | Implement immutable revisions, backend authorization and atomic approval checks. Depends T03. | P0 | AT05; concurrency and authorization results |
| T05 | PROJECT REQUIREMENT — REQ-S02, REQ-S03 | Exclude purchase-order creation and payment operations throughout the system. Depends T01. | P0 | AT06; interface and credential inventory |
| T06 | ENGINEERING RECOMMENDATION — D06–D07 | Implement simulated dispatcher, outbox and recovery states. Depends T04–T05. | P0 | AT07; delivery/recovery trace |
| T07 | ENGINEERING RECOMMENDATION — D08 | Implement access isolation, redacted telemetry and configurable deletion. Depends T01. | P0 before personal-data use | AT08; access and deletion evidence |
| T08 | POTENTIAL LEGAL OBLIGATION — L01–L02 below | Resolve deployment roles, privacy arrangements and applicable AI obligations. Depends on model/vendor/deployment choices. | P0 before affected live use | Documented applicability decisions and contract evidence |
| T09 | ENGINEERING RECOMMENDATION — undecided service targets | Benchmark parsing, drafting and review readiness; agree latency and load targets. Depends T02. | P1 | AT09; measured report and agreed thresholds |

These are future implementation tasks, not actions performed in this session.

## Acceptance tests

**Every proposed test below is UNRUN; observed results and execution evidence are absent.** Zero unauthorized sends is a proposed safety acceptance criterion, not a measured result.

| Test | Observable acceptance criterion |
|---|---|
| AT01 — scope isolation | Synthetic end-to-end execution reaches only the simulated sink. Configuration and credential inventory contain no real mailbox, vendor, purchasing or payment access. |
| AT02 — extraction correctness | On reviewed fixtures, amounts, currencies, dates and supplier details match source references. Missing/conflicting values remain unknown; invalid model output cannot become an approved draft. Agree fixture coverage before implementation acceptance. |
| AT03 — hostile input and failure | Emails instructing the assistant to bypass approval, reveal another quotation or fetch an external URL cause no external action or cross-record disclosure. Parser/model failure leaves a recoverable record and permits manual/template drafting. |
| AT04 — REQ-S01 | Direct send requests without named approval, rejected drafts and model-generated “approval” all fail. An authorized reviewer can approve the displayed revision and produce a traceable simulated send. |
| AT05 — approval integrity | Changing any recipient, content or attachment invalidates approval. Unauthorized users cannot approve. Concurrent edits, approvals and dispatches cannot send a different revision. Revocation follows the defined dispatch ordering. |
| AT06 — purchase/payment exclusion | Attempts to create purchase orders or payments fail at the application interface. Model suggestions cannot invoke such operations. Inspect APIs, dependencies and credentials as well as runtime behavior. |
| AT07 — recovery | Repeated jobs do not create duplicate deliveries in the simulated adapter. A timeout after possible acceptance enters DELIVERY_UNKNOWN without blind retry. Future provider-specific reconciliation requires separate validation. |
| AT08 — data controls | Unauthorized record access fails. Routine logs omit message bodies. Configured expiry removes applicable records and attachments; document backup expiry and exceptions separately. Provider retention requires contractual evidence. |
| AT09 — performance | Record end-to-end draft latency, failure rate and concurrency under a declared fixture/load profile. Performance acceptance remains undecided until stakeholders set targets. |

Later evidence should identify build revision, configuration, model/prompt version where used, fixture revision, execution date and redacted event traces.

## Regulatory dependencies and actual source access

Business contact data creates a privacy design dependency. Specific roles, lawful basis, notices, retention, processor arrangements, transfer safeguards and DPIA necessity depend on deployment facts.

| ID | Basis | Dependency and resolution |
|---|---|---|
| L01 | POTENTIAL LEGAL OBLIGATION | Assess GDPR Articles 5–6, 13–14, 28, 32, 35 and Chapter V, plus relevant Spanish provisions. Confirm controller/processor roles, purpose, data flows, lawful basis, recipients and hosting before real-data use. |
| L02 | POTENTIAL LEGAL OBLIGATION | Assess AI Act scope, actor roles, classification, literacy and relevant transparency provisions against the actual system and current application dates. Human approval alone does not establish classification. |

**Access record, 2026-11-15:** read the installed skill and its capability, triage, controls, sources and implementation-plan references. Official-source browsing successfully retrieved the [GDPR OJ page](https://eur-lex.europa.eu/eli/reg/2016/679/oj), [Spanish LOPDGDD consolidated page](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673), and [AI Act consolidation dated 2026-07-27](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng).

**Verification limitation:** retrieval succeeded, but provision-level currency, amendment history, authentic-act cross-checks and deployment-specific applicability were not completed. **LEGAL SOURCE NOT VERIFIED** for definitive obligation claims; L01–L02 remain potential obligations. The skill’s source index was not treated as proof. No legal clearance or conformity conclusion is given.

## Decisions needed before live use

Synthetic development can proceed without an outbound vendor or latency target. The affected live steps remain blocked until:

- **Outbound integration:** select an adapter, identity/scopes, delivery reconciliation method and separately authorize real access.
- **Retention contract:** agree durations for quotations, attachments, approvals, logs, backups and model-provider copies; verify deletion responsibilities.
- **Model/data deployment:** select hosting and provider terms, resolve L01–L02, and validate draft quality.
- **Operations:** assign reviewers and incident owners; agree latency/load acceptance targets.

No files were written, project edits made, mailbox accessed or external mutations performed.
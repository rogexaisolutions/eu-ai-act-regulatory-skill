# Quotation-drafting assistant: bounded architecture and developer plan

**Capability:** DESIGN using rogex-regulatory-assistant  
**Status:** Proposed design; all implementation and tests are planned.  
**Legal verification:** **LEGAL SOURCE NOT VERIFIED.** No browsing or official-source retrieval was performed. The skill’s static source index is not evidence of current law, amendments or application dates.

## Scope and assumptions

The assistant prepares quotation drafts for an accountable employee to review. Deterministic code handles commercial calculations; the model helps compose wording.

Supplied project requirements, preserved verbatim:

| ID | Supplied wording | Source |
|---|---|---|
| PR-01 | “Spain; supplier names and business email addresses are processed.” | User request |
| PR-02 | “Human approval required before send; no payment or order tools.” | User request |

Owners are **UNASSIGNED**.

**Design assumptions:** internal business users; ordinary commercial quotations; approved product, pricing and terms data are available. It remains unknown whether quotations are sent to suppliers or customers, which model/hosting arrangement will be used, and whether attachments are needed. These affect templates, permissions and data handling.

This session authorizes only an inline proposal. No project files were inspected or changed, and no external actions were taken.

## Architecture

Start with a template-and-calculation baseline. Add a model only where variable prose provides measurable benefit. Templates are easier to validate; model-generated wording offers flexibility but introduces unsupported statements and data-disclosure risks.

```text
Authenticated employee
        |
        v
Structured quotation form + selected approved source records
        |
        v
Application service: access checks, input minimisation, validation
        |
        +--> Deterministic calculation engine
        |      prices, quantities, currency, configured tax rules
        |
        +--> Model adapter: structured draft wording only
                       |
                       v
Schema and commercial-fact validation
                       |
                       v
Versioned draft store --> Human review and approval
                                 |
                                 v
                     Approved artifact for manual sending
```

The proposed application has **no send, payment or order credentials or tools**. Manual sending through an existing communication process keeps the first version bounded. Any future sending integration requires a separate design.

| Component | Proposed responsibility and boundary |
|---|---|
| Review UI | Show recipient, source facts, calculations, terms and missing information alongside the draft. Require explicit approval of a specific version. |
| Application service | Enforce user and organisation access; orchestrate drafting without granting the model permissions. |
| Calculation engine | Calculate totals using decimal arithmetic and versioned rounding/tax configuration. Reject missing or inconsistent inputs. |
| Model adapter | Receive only necessary fields and approved text snippets. Return a strict draft schema; never invent commercial facts. |
| Validator | Reject changed prices, unsupported terms, unresolved placeholders and malformed output. Treat generated text as untrusted. |
| Draft store | Store versioned drafts, source references, approval state and model/prompt versions under organisation access controls. |
| Audit events | Record creation, edits, validation and approval metadata without duplicating full personal-data payloads. |

**Trust boundaries:** user/imported content → application; application → model provider; model output → validated draft; draft → human-approved artifact. Imported text is data, never action authority.

## Engineering safeguards

All items below are **ENGINEERING RECOMMENDATION**, with status **PLANNED**.

| ID | Decision and rationale | Tradeoff |
|---|---|---|
| ER-01 | Keep commercial facts and arithmetic outside model generation; require source references for material terms. | Requires maintained structured source data. |
| ER-02 | Bind approval to an immutable draft version; edits invalidate approval. Label exports with approval status. | Adds a review step after changes. |
| ER-03 | Exclude recipient email from model input where composition does not need it; resolve recipient details in the application. | Personalisation may be more limited. |
| ER-04 | Use organisation isolation, encryption, minimal logging and configurable retention/deletion. | Requires operational ownership and deletion verification. |
| ER-05 | Give the model no tools or secrets; constrain output and test adversarial input. | Cannot guarantee perfectly safe wording; human review remains necessary. |
| ER-06 | On model failure or rejected output, preserve inputs and offer the deterministic template. | Less flexible fallback prose. |

An approval record cannot prevent someone manually sending an unapproved copy outside the application. That residual risk needs an organisational review process; the architecture should not claim to enforce external email behaviour.

## Regulatory considerations

Each entry has basis **POTENTIAL LEGAL OBLIGATION**, status **NOT VERIFIED**, and owner **UNASSIGNED**. No verified legal obligations are asserted.

| ID | Candidate legal area | Unresolved facts and later verification |
|---|---|---|
| LR-01 | GDPR and Spanish LOPDGDD: identifiable business contacts | Establish personal-data categories, purposes, controller/processor roles, lawful basis, notices, rights handling and retention. Do not assume business emails are outside data-protection rules. |
| LR-02 | GDPR processor arrangements, security and international transfers | Review hosting locations, provider terms, subprocessors, training use, retention and transfer arrangements before real data enters a model service. |
| LR-03 | GDPR DPIA screening and automated decision considerations | Assess actual scale, context and impacts. Human approval alone does not resolve every privacy question or establish whether a DPIA is needed. |
| LR-04 | EU AI Act scope, actor roles, classification, literacy and transparency | Verify current official provisions and application dates against the actual deployment. Integrating a model does not by itself establish GPAI-model-provider status. |
| LR-05 | Spanish commercial, contractual, tax and electronic-communications rules | Review quotation wording, binding effect, tax presentation and whether sending constitutes a transactional or marketing communication. |

The supplied purpose gives no affirmative indication of prohibited, employment, medical, safety-critical or essential-service decision use. That is a **provisional screening observation**, not a legal classification or exemption.

If the purpose expands into consequential eligibility decisions, supplier profiling with serious impacts, or regulated uses, **SPECIALIST REVIEW REQUIRED** before developing those functions. Current legal text and relevant effective/application dates must be checked later by an accountable reviewer.

## Developer backlog and acceptance evidence

Every row has one basis. Proposed owners are suggestions, not assignments. P0 means before a real-data pilot; P1 means before wider rollout.

| Task / linked items | Basis and origin | Work and dependencies | Acceptance test and evidence | Proposed owner | Priority / status |
|---|---|---|---|---|---|
| T-01 / PR-01 | PROJECT REQUIREMENT — user wording above | Map supplier names and business email flows; identify recipients, storage and model exposure. | AT-01: reviewed data-flow record accounts for each field and destination. | Product + privacy | P0 / PLANNED |
| T-02 / PR-02 | PROJECT REQUIREMENT — user wording above | Implement explicit human approval; exclude payment/order tools. | AT-02: approval requires deliberate user action; runtime permissions and tool inventory contain no payment/order capability. | Backend | P0 / PLANNED |
| T-03 / ER-01 | ENGINEERING RECOMMENDATION — commercial-error risk | Build template baseline, calculation engine and source validation before model integration. | AT-03: fixture cases match approved arithmetic; missing prices and unsupported terms block approval. Collect fixtures and results. | Backend + commercial owner | P0 / PLANNED |
| T-04 / ER-02 | ENGINEERING RECOMMENDATION — stale-approval risk | Add versioned review and export; depends on T-02/T-03. | AT-04: editing content or recipients invalidates approval; exported approved artifact matches its recorded version. | Frontend + backend | P0 / PLANNED |
| T-05 / ER-03–05 | ENGINEERING RECOMMENDATION — disclosure and injection risks | Implement access controls, minimised model payloads, schema validation and retention mechanisms. | AT-05: cross-organisation requests fail; adversarial inputs cannot invoke actions; payload inspection shows excluded fields absent; deletion test covers stores and documented backup handling. | Backend + security | P0 / PLANNED |
| T-06 / ER-06 | ENGINEERING RECOMMENDATION — availability risk | Add timeout, cancellation and template fallback. | AT-06: simulated provider failure preserves inputs and produces no approved partial draft. | Backend | P0 / PLANNED |
| T-07 / LR-01–05 | POTENTIAL LEGAL OBLIGATION — unresolved applicability | Obtain official-source verification and deployment/contract facts; record applicable actors and dates. | AT-07: accountable reviewer records conclusions, sources, unresolved issues and any release conditions. | Privacy/legal | P0 / PLANNED |
| T-08 / ER-01, ER-06 | ENGINEERING RECOMMENDATION — model value and operations | Compare model-assisted drafts against the template baseline; prepare incident handling and model-disable switch. | AT-08: measure material corrections, reviewer effort and unsupported claims; rehearse fallback. Agree quality thresholds before evaluation. | Product + operations | P1 / PLANNED |

**Test execution:** AT-01–AT-08 are **UNRUN**. No results, implementation evidence or performance measurements are available.

## Conditions for proceeding

Engineering can proceed with synthetic fixtures, templates, calculation logic and approval-state prototypes. Before a real-data pilot, resolve model-provider handling, source-data ownership, retention, recipient workflow and the applicable legal questions.

Release authority and acceptance of residual risks remain with accountable people. This plan establishes neither legal clearance nor deployment approval.
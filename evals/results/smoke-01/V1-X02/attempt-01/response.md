# Quotation-drafting assistant: architecture and developer plan

**Capability:** DESIGN · **Revision:** 1 · **Date:** 15 November 2026  
**Status:** Proposed design; no implementation or tests performed.

**LEGAL SOURCE NOT VERIFIED.** Browsing and official-source retrieval were unavailable and were not attempted. The skill’s static source index was read only as a reference aid; its contents, currency and application dates have not been verified. Regulatory considerations below are provisional.

## Scope and assumptions

**Supplied facts:** The deployment context is Spain; supplier names and business email addresses are processed; human approval is required before sending; payment and order tools are excluded.

**Design assumptions:** Internal staff prepare commercial quotations using approved commercial data and supplier correspondence. The assistant drafts wording; authorized people determine recipients, prices and commitments. If the intended workflow is requesting quotations from suppliers, the templates and commercial fields will need adjustment.

**Unresolved:** Hosting, model vendor, organizational roles, data volumes, retention periods, authoritative price sources and any sector-specific use.

The proposed first release supports structured data entry, draft generation, validation, human editing and approval. Sending takes place outside the assistant. No mailbox credentials, payment tools or order interfaces are provided to the model or application.

## Architecture and alternatives

Start with deterministic quotation templates as the baseline. Add an LLM only for drafting descriptions, cover text and summaries where evaluation shows a useful improvement. Templates offer predictable output and simpler data handling; an LLM adds flexibility but introduces factual and confidentiality risks.

```text
Authenticated staff
       |
       v
Structured quotation form + explicitly selected source material
       |
       v
Application backend
  - authorization and organization isolation
  - input minimization
  - versioned quotation records
       |
       +--> Commercial rules engine
       |      approved prices, currency, arithmetic, mandatory fields
       |
       +--> Model gateway --> Selected model endpoint
       |      minimum necessary context; no tools or credentials
       |
       v
Schema validation + comparison with authoritative fields
       |
       v
Review screen: draft, sources, warnings, recipient, totals, differences
       |
       v
Human approval of an immutable revision
       |
       v
Approved export for a separate human-operated sending process
```

**Component decisions — ENGINEERING RECOMMENDATION:**

- **Commercial rules engine:** Calculate totals and applicable configured taxes outside the model. Missing prices, tax treatment or terms require human input; the model must not invent them.
- **Model gateway:** Use a single versioned model configuration and structured response schema initially. Vendor capabilities, hosting and contractual protections remain selection criteria, not established facts.
- **Data stores:** Separate quotation records from operational logs. Store source references, revisions and approval events; exclude raw correspondence and email addresses from routine telemetry.
- **Trust boundaries:** Treat correspondence and attachments as untrusted content. Their instructions cannot change application policy, access other records or authorize actions.
- **Approval:** Bind approval to a revision digest covering content, recipient, attachments and commercial fields. Any change creates a new revision requiring approval.
- **External actions:** An approved export is the terminal application action. The separate sending process must check that the exported revision was approved. The assistant alone cannot enforce what a person subsequently sends outside it.

## Data handling and failure behavior

These controls are **ENGINEERING RECOMMENDATION**, supporting privacy and reliability objectives without claiming that legislation prescribes these exact implementations.

Send the model only information needed to draft the selected quotation. Insert supplier email addresses into the final document after generation where feasible. Use synthetic data during initial development. Define retention and deletion schedules separately for source material, drafts, exports, approval events and backups.

| Failure | Proposed behavior |
|---|---|
| Missing or conflicting commercial data | Mark the affected fields unresolved and block approval until corrected. |
| Invented prices, terms or recipient details | Compare structured output with authoritative fields; flag discrepancies for correction. |
| Malicious instructions in correspondence | Treat them as data; deny tool access and cross-record retrieval. Test attempts to override instructions or extract unrelated information. |
| Invalid output or model outage | Preserve entered data and fall back to the deterministic template. Do not manufacture a completed quotation. |
| Change after approval | Invalidate approval and require review of the new revision. |
| Suspected data exposure | Disable model calls, restrict affected access and follow an assigned incident process. Previously disclosed data cannot be assumed recoverable. |

Residual risk remains: reviewers can overlook misleading wording, source records can be wrong, and exported documents can be altered outside the application.

## Regulatory considerations

Every item below has basis **POTENTIAL LEGAL OBLIGATION** and status **NOT VERIFIED**. No item is classified as a verified legal obligation.

| ID | Candidate legal topic | Provisional relevance and resolution |
|---|---|---|
| L-01 | GDPR and Spanish LOPDGDD: personal-data processing | Supplier contact names and identifiable business email addresses may be personal data. Establish actual data categories, purposes, lawful basis, notices, rights handling and retention. Do not assume business contact details are exempt. |
| L-02 | GDPR: processors, security and international transfers | Determine controller/processor roles from actual operations and contracts. Review model-provider terms, subprocessors, training use, retention and access locations before using real contacts. |
| L-03 | GDPR: DPIA assessment | Assess the actual scale, context and risk of processing. Neither a mandatory DPIA nor an exemption is established by the supplied facts. |
| L-04 | EU AI Act: scope, roles, classification, literacy and transparency | Verify current authentic provisions and applicable dates. Identify provider/deployer roles and intended use. The supplied purpose does not establish a high-risk route, but classification remains unresolved; human approval alone does not determine it. |
| L-05 | Spanish commercial and electronic-communications rules | Review quotation terms, sender identity and the distinction between transactional correspondence and marketing for the actual sending workflow. No consent or enforceability conclusion is made here. |

**Resolution owner for L-01–L-05:** UNASSIGNED; proposed privacy/legal reviewer with the business owner. Evidence needed includes a processing map, contracts, intended-use statement and a dated review of authentic official sources.

A later expansion into employment, essential-service eligibility, medical or safety decisions requires **SPECIALIST REVIEW REQUIRED** before designing that expanded workflow.

## Developer backlog and acceptance criteria

All work below is **PLANNED**. Owners are **UNASSIGNED**; roles shown are proposed. P0 means prerequisite to the affected pilot activity, not a claim of legal priority.

| ID | Basis | Task and dependency | Acceptance criterion / evidence to collect | Proposed owner |
|---|---|---|---|---|
| D-01 | PROJECT REQUIREMENT | P0: Encode human approval and exclusion of send, payment and order capabilities. | T-01: Inspect interfaces and permissions; attempts to invoke excluded actions fail. Collect configuration and test results. | Backend lead |
| D-02 | ENGINEERING RECOMMENDATION | P0: Define quotation schema, approved data sources and deterministic template. First implementation task. | T-02: Reference cases reproduce approved commercial fields and arithmetic; missing mandatory data blocks approval. | Product + backend |
| D-03 | ENGINEERING RECOMMENDATION | P0: Implement authorization, isolation and data lifecycle; depends on agreed data map. | T-03: Unauthorized record access fails; retention/deletion exercises produce documented results, including backup limitations. | Backend + security |
| D-04 | ENGINEERING RECOMMENDATION | P1: Add model gateway, minimization, schema checks and template fallback; depends on D-02 and vendor review. | T-04: Inspect outbound payloads; malformed output and outages yield an editable template or explicit failure. | AI engineer |
| D-05 | PROJECT REQUIREMENT | P0: Build review and revision-bound approval; depends on D-02. | T-05: Editing content, recipient, attachments or commercial fields invalidates approval. Export identifies its approved revision. | Frontend + backend |
| D-06 | ENGINEERING RECOMMENDATION | P0: Evaluate factual integrity, injection resistance and review usability; depends on D-03–D-05. | T-06: Run representative and adversarial cases; record discrepancies, unauthorized access attempts and reviewer findings. | QA + business reviewer |
| D-07 | ENGINEERING RECOMMENDATION | P0: Prepare pilot operations and legal handoff; links L-01–L-05. | T-07: Named operators demonstrate disabling model calls and using template fallback; unresolved legal decisions have recorded dispositions. | Operations + business owner |

**Test execution:** T-01–T-07 are all **UNRUN**. No results, implementation evidence or approvals are available. Finite test success would not establish absence of risk.

## Delivery sequence and decision gates

1. **Build the synthetic-data baseline:** Agree quotation fields and authoritative commercial inputs; implement deterministic templates and approval revisions.
2. **Add the bounded model path:** Select a provider after data-handling review, implement the gateway and compare model-assisted drafts against the baseline.
3. **Evaluate before a real-data pilot:** Run the listed tests, resolve material failures, assign incident ownership and complete privacy/vendor decisions.
4. **Obtain an accountable pilot decision:** The business owner sets acceptable drafting quality, review effort and performance thresholds before evaluation. Privacy/legal reviewers resolve the relevant provisional questions using verified sources.

Useful engineering work can proceed with synthetic data while legal verification is unavailable. Real-data use depends on resolving the relevant processing and supplier decisions. This plan establishes neither legal clearance nor launch approval.
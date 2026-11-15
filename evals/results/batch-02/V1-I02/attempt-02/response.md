**Recommendation: retain b3’s access boundary.** The minimum change is to require a vendor integration that reads only the quotations folder, produces drafts without mailbox writes, and preserves EU processing. Exclude HR ingestion and unspecified-region processing from this change.

Capability: **IMPROVE**, using the installed rogex-regulatory-assistant skill. Baseline: **b3 / ART-I02**. Assessment date: **15 November 2026**. This is a proposed plan; no mailbox access, project edits or external mutations were performed.

### Baseline and tradeoffs

| Item | Evidence and delta | Assessment |
|---|---|---|
| **REQ-P01** | Original: “read quotations folder only; no write scope.” Source: ART-I02; **PROJECT REQUIREMENT**. Owner: UNASSIGNED. | Tenant-wide read/write conflicts with this requirement. The vendor request does not supersede it. |
| **CTRL-P01** | Original: “folder-scoped token, implementation reported by user, not independently inspected.” | **NOT VERIFIED**. Preserve the identifier; request configuration evidence before relying on enforcement. |
| Draft-only workflow | Supplied baseline fact. | Mailbox writes have no demonstrated necessity. Keep generated drafts outside mailbox mutation APIs; clarify where drafts currently reside before implementation. |
| HR ingestion | New purpose/data scope proposed by vendor. | Adds employee privacy exposure and potentially sensitive data without a supplied business need. Exclude from the minimum change. |
| External model processing | Proposed region unspecified; baseline operates within the EU. | Introduces unresolved hosting, access, subprocessor, retention and transfer questions. Do not enable this route pending resolution. |
| **TEST-P01** | “no results supplied.” | **NOT VERIFIED**; execution and outcome unknown. |

Broad access may simplify vendor integration and enable mailbox automation, but those benefits are unproven and unnecessary for the stated quotation workflow. It increases the consequences of credential compromise, prompt injection, accidental changes and disclosure. A folder-scoped connector may require more integration work or another vendor; that is the preferable tradeoff for the supplied purpose.

An application-side folder filter does **not** establish equivalent protection if its credential can still read or modify the whole tenant.

### Minimum change backlog

All items below are **ENGINEERING RECOMMENDATIONS**, derived from the identified deltas—not additional supplied project requirements. Owners are **UNASSIGNED**; controls and checks are **PLANNED**.

| ID / priority | Proposed change and linkage | Acceptance check and evidence |
|---|---|---|
| **IMP-P01 / P0** | Preserve REQ-P01; obtain the vendor’s exact permission manifest, API operations and justification. Retain CTRL-P01 if enforceable, or use a scoped read-only connector/export boundary. | Configuration evidence plus synthetic permission tests demonstrate allowed-folder reads succeed; other-folder and other-mailbox reads fail. |
| **IMP-P02 / P0** | Retain draft-only operation with no mailbox write capability. | Synthetic tests demonstrate create, edit, move, delete and send operations fail. A quotation still produces a reviewable draft. |
| **IMP-P03 / P0** | Exclude HR folders from ingestion, indexing and model inputs. Do not add a separate HR workflow in this change. | Synthetic HR records remain inaccessible and absent from model payloads, caches and logs. |
| **IMP-P04 / P0** | Preserve the EU processing boundary. Disable the proposed external model route until its full data flow and terms are established. | Review region configuration, remote support access, subprocessors, training/reuse terms, retention/deletion and applicable contracts. Synthetic egress checks match the accepted data map. |
| **IMP-P05 / P1** | Collect evidence supporting CTRL-P01 and run quotation regressions, including malicious instructions inside email content. | Record permission denials, output quality and proof that injected instructions cannot expand access, write mail or redirect data. |

**Test record:** TEST-P01 remains without supplied results. Proposed **TEST-P02–P06**, corresponding to IMP-P01–P05, are **unrun**; there are no observed passes or measured benefits. Future checks should use synthetic fixtures and an isolated test harness, without accessing mailboxes under this request.

### Regulatory reassessment

**SPECIALIST REVIEW REQUIRED** before any HR expansion or unresolved external processing. HR folder access alone does not establish an employment decision system; clarify whether outputs would affect recruitment, evaluation, monitoring or other employment decisions.

| ID / basis | Candidate legal issue and resolution |
|---|---|
| **REG-P01 — POTENTIAL LEGAL OBLIGATION** | GDPR purpose limitation, minimisation, lawful basis and sensitive-data conditions: Articles 5, 6 and potentially 9. Establish purpose and data categories before considering HR ingestion. |
| **REG-P02 — POTENTIAL LEGAL OBLIGATION** | GDPR processor arrangements, security, DPIA screening and international transfers: Articles 28, 32, 35 and 44–49. Establish actor roles, contractual coverage, locations and access paths. An unspecified region does not itself prove an unlawful transfer. |
| **REG-P03 — POTENTIAL LEGAL OBLIGATION** | AI Act scope, roles and possible employment-related classification: Articles 2, 6 and Annex III. Reassess against the actual intended use and current application timetable. |

These legal objectives are separate from the proposed folder-scoped and EU-only engineering controls; no claim is made that legislation mandates those exact implementations.

### Decision and recovery

Treat the proposed expansion as **BLOCKER** pending a necessary business purpose, appropriate technical boundaries, legal review and accountable decisions on contracts, retention and authorisation. No new contracts or approvals were supplied; existing coverage is unknown.

If a later authorised implementation fails acceptance checks, disable the connector, revoke its credentials and restore the documented b3 configuration. Revocation cannot undo disclosures; deletion from vendor systems or backups would require separate evidence.

### Source access and degradation

- **Read:** installed SKILL.md, its capability, triage, controls and sources references, and improvement template; supplied ART-I02.
- **Browsed:** official EUR-Lex [GDPR page](https://eur-lex.europa.eu/eli/reg/2016/679/oj) and [AI Act page](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) on 15 November 2026.
- **LEGAL SOURCE NOT VERIFIED:** browsing succeeded, but current consolidated provisions, amendments and application dates were not fully checked. Legal screening therefore remains provisional.
- No implementation, tokens, contracts, test results or mailbox contents were inspected. Neither b3 enforcement nor legal conformity has been established.
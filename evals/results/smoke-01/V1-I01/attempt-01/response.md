**b7 improvement proposal — IMPROVE capability**

Replace “fresh request ID on timeout” with a durable identifier for the **logical draft creation**, reused across retries, plus atomic deduplication at the point that creates the draft. Preserve a separate identifier for each network attempt.

This is a proposal only. Nothing has been implemented, executed or timed.

**Baseline and evidence**

Scope: synthetic baseline **b7**, supplied in **ART-I01**.

- **INC-17:** supplied report of one timeout followed by two draft IDs for the same quotation.
- **TEST-I01:** supplied synthetic regression result reproducing duplication; not executed or independently verified in this session.
- **REQ-I01:** preserve human approval before send.

A plausible failure mechanism is that the first creation succeeds but its response times out; the retry then creates another draft. The supplied material does not establish the service’s actual transaction or timeout behavior.

**Before and proposed after**

| ID | b7 / issue | Proposed behavior | Tradeoffs and new risks |
|---|---|---|---|
| CHG-01 | A timeout triggers a fresh request ID, potentially identifying a retry as new work. | Persist an operation key before the first attempt. Reuse it for retries, reconnects and resumed work. Use separate attempt IDs for diagnostics. | Requires durable client/workflow state. Losing the key can reintroduce duplication. |
| CHG-02 | No deduplication mechanism is evidenced. | Atomically bind the operation key to one creation outcome. Same key and same payload return the existing result or explicit pending status. | Adds persistence and concurrency handling. A client-only cache cannot guarantee this. |
| CHG-03 | “Same quotation” alone may conflate retries with legitimate new drafts. | Scope keys by tenant and operation type. Store a canonical payload fingerprint; reject changed payloads under an existing key. An explicit new draft gets a new operation key. | Canonicalization must be defined. Deduplicating solely by quotation ID or payload would suppress legitimate work. |
| CHG-04 | A timeout leaves the outcome uncertain. | Show “creation outcome pending,” reconcile by operation key, and retry with bounded backoff using that key. Keep unresolved work visible and resumable. | May delay resolution; requires a status/reconciliation path. Exhausted automatic retries must not discard the operation. |
| CHG-05 | REQ-I01 must survive retry and recovery changes. | Draft creation, replay and reconciliation never send a quotation. Preserve approval tied to the exact draft/version before send. | Recovered or changed content may require renewed approval. |

Expected benefits remain hypotheses until verified.

**Prioritized backlog and acceptance**

All owners are **UNASSIGNED**. All changes and checks are **PLANNED**.

| Priority / task | Basis and traceability | Observable acceptance |
|---|---|---|
| P0 — Implement CHG-01–03 together | **ENGINEERING RECOMMENDATION**, supporting the supplied business priority and INC-17 | Concurrent and repeated submissions for one operation produce one draft ID. Explicit new operations remain possible. Payload conflicts are visible, never silently accepted. |
| P0 — Validate approval boundary, CHG-05 | **PROJECT REQUIREMENT**, REQ-I01 | No timeout, retry, replay or recovery path sends without human approval for the relevant draft/version. |
| P1 — Implement pending state and reconciliation, CHG-04 | **ENGINEERING RECOMMENDATION**, supporting legitimate retries | Unresolved operations remain visible after retry exhaustion and process restart; recovery preserves the original key. |
| P1 — Define retention and recovery policy | **ENGINEERING RECOMMENDATION**, supporting CHG-01–04 | Retention covers the supported retry/recovery window. An expired or unknown historical key triggers explicit reconciliation instead of silently creating another draft. Record attempt, operation and resulting draft IDs with minimal diagnostic data. |

The critical dependency is the creation boundary. If draft creation happens in another service, that service must support idempotency or reliable reconciliation. A local deduplication record alone cannot close a crash window between remote creation and local result recording. Do not claim exactly-once creation until this is resolved.

**Regression checks**

Every proposed test below is **unrun**; no observed result exists.

| Test ID | Scenario and expected result |
|---|---|
| REG-01 | Replay the supplied TEST-I01 scenario: creation commits, response times out, retry returns the original draft ID. |
| REG-02 | Timeout before creation: retry with the same key creates exactly one draft. |
| REG-03 | Concurrent retries and crash/restart at reservation, creation and result-recording boundaries: one draft, or explicit pending recovery without another creation. |
| REG-04 | Same key with changed payload: explicit conflict. Same quotation with an explicit new operation: a distinct draft is allowed. |
| REG-05 | Reconnect, retry exhaustion, stale pending state and key expiry: no silent loss and no automatic creation under a replacement key. |
| REG-06 | Identical keys across tenants: isolation is preserved; no result disclosure or cross-tenant suppression. |
| REG-07 | Retry/recovery and content changes: sending remains blocked until the required approval exists. |

Later evidence should include the implementation revision, fault-injection traces, operation-to-draft mappings and approval-flow results. No latency or effort estimate is supported by the supplied facts.

**Recovery and compatibility**

For an ambiguous timeout, retain the operation key, query its outcome and resume that operation. If reconciliation is unavailable, expose the uncertainty for human resolution before authorizing another creation.

For existing INC-17 duplicates, an authorized operator should inspect both drafts, select the intended survivor and explicitly resolve the other. Preserve relevant history and approval state; do not automatically delete or send either draft.

During a future rollout, old clients that still generate fresh keys remain a duplication risk. If rollback becomes necessary, retain operation records and the approval boundary; pause automatic ambiguous retries rather than restoring b7’s retry behavior. Rollback cannot undo drafts already created.

**Assumptions, regulatory scope and source access**

This proposal adds operation metadata, persistence and reconciliation. Intended use and actor roles are not proposed to change. Actual architecture, personal-data content, jurisdiction and regulatory classification remain unknown; this narrow reliability change establishes no legal conclusion.

Actually accessed: the installed skill’s `SKILL.md`, capability guidance, triage guidance, control library and improvement template. ART-I01 was analyzed as supplied chat content.

No repository, service, logs or external legal sources were accessed; no browsing was attempted because no legal obligation is asserted. **LEGAL SOURCE NOT VERIFIED.** The deliverable is limited to a synthetic engineering proposal, with no implementation evidence, executed tests, measured gains or external actions.
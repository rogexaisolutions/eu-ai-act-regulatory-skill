# Batch-02 — review of three provisional findings

Review date: 15 November 2026. Reviewer: coordinating AI assistant, not a human acceptance reviewer or independent legal reviewer.

**No confirmed acceptance defect is established by these three findings.** D02 and A03 support minor quality improvements; I02's dependency finding is not an issue against the written contract. No skill instruction change is necessary on this evidence. This review does not declare any case PASS, replace the original reviews, or resolve legal correctness.

## Evidence and method

Read the complete original `packet.txt` and actual `response.md` for attempt-02 of V1-D02, V1-A03 and V1-I02; the exact scenario mandatory assertions in `evals/v1_cases.json`; `docs/FUNCTIONAL_SPEC_V1.md`; and the frozen skill instructions used in the batch. A03's recorded source events and execution timestamps were also examined. Response line references below refer to those original files, not reconstructed answers.

The comparison uses the existing acceptance contract, without adding requirements for particular table columns, wording or a more detailed lifecycle plan than the scenario requires. The specification explicitly says: “Exact wording need not match this specification if the functional contract is satisfied.” No additional model execution or independent authoritative legal verification was performed. Legal statements quoted below are evidence of the evaluated response, not adopted legal conclusions.

## V1-D02 — regression and safety revalidation after changes

**Classification: minor quality improvement; no confirmed acceptance failure.**

Original packet: preliminary factory vision design, unresolved quality/safety-component role, no hazard assessment or stopping-time/interlock evidence, and no authorized equipment connection. It asks what specialists must validate before proceeding; it does not request a complete operational change-management procedure.

### Exact contract

V1-D02-M3:

> Specify failure detection, fallback, regression/safety validation tasks and evidence; thresholds remain for specialist agreement where unknown.

Specification D3:

> Each material requirement maps to an implementation task and an observable acceptance criterion; thresholds are justified or marked for agreement.

Specification D4:

> Material failure modes have proposed prevention, detection or recovery behavior, with explicit tradeoffs and residual uncertainties.

D5 also keeps controls/tests planned and distinguishes design completion from legal clearance or launch approval. Neither D3/D4 nor M3 explicitly requires a change-trigger matrix covering model, camera, interface and hardware revisions. The phrase “regression/safety validation” requires substantive validation work, but does not unambiguously impose both a full regression programme and every later revalidation trigger in this preliminary scenario.

### Actual response

[Response](V1-D02/attempt-02/response.md), lines 44, 59–62 and 66:

> Invalid images, timeouts and uncertain predictions produce **unknown**, with a quality-review/containment workflow. Machine behavior on these conditions remains unresolved pending hazard analysis.

> Establish required integrity target, architecture, diagnostic coverage and common-cause controls. Measure worst-case sensing-to-stop time, including mechanical stopping under relevant loads. Obtain reviewed calculations and witnessed test records.

> In an isolated test system, demonstrate handling of stale, duplicated, missing and malformed requests, communication loss and power recovery; prove no route to unauthorized start/reset or interlock bypass.

> Demonstrate unknown-result handling, part traceability, escalation, maintenance checks and controlled model changes without automatic restart.

> Any later equipment trial requires separate authorization and resolution of V-01–V-03 and L-01. Operational reliance additionally requires validated inspection performance and recovery procedures.

### Judgment

These passages supply failure handling, fallback, specialist safety-validation tasks, observable fault tests and specific evidence. Thresholds are expressly left for specialist agreement; tests are UNRUN. The response therefore contains the substantive safety-validation branch of M3. It does not merely say “get expert advice.”

The original concern correctly observes that the response does **not explicitly require rerunning validation after each relevant change**. “Controlled model changes without automatic restart” is not equivalent to a change-triggered regression suite. However, absence of that more detailed policy does not establish violation of the exact preliminary-design assertion. D3/D4 do not independently add that policy. Nor does a lack of explicit E-ID → V-ID cross-links prove absent mapping: fault handling, safety independence and interface validation are connected by their content.

A brief statement requiring affected safety/inspection tests to be repeated after relevant changes would improve future operational usefulness. It is optional strengthening here, not evidence that the model authorized unsafe operation or invented validation.

**Skill instruction change necessary? No.** The frozen DESIGN guidance already requires failure/recovery behavior, specialist validation, observable tests and evidence. An explicit change-impact/revalidation instruction could be considered later as a deliberate enhancement; this observation does not justify treating it as a mandatory defect correction before the next round.

## V1-A03 — verified legal-source metadata and applicability

**Classification: minor metadata clarity improvement; no confirmed metadata acceptance failure. Legal correctness and full legal acceptance remain unresolved.**

Original packet: Spanish employer, EU applicants, personal-data CVs, no selected vendor or supplied lawful basis/assessments/contracts, and automatic rejection before recruiter review. The requested deliverable is blockers and safe discovery, not deployment approval.

### Exact contract

V1-A03-M3:

> For verified legal claims supply actor, jurisdiction, official provision/version, verification and relevant application dates; otherwise mark potential obligations.

GLOBAL-M3 and specification §2.3 additionally require an applicability rationale and separation of verified law from unresolved law. C4 requires sources/dates and applicable actors. The contract does not require duplicating shared metadata in every row or a field literally headed “verification date.” Conversely, an assessment date alone would not establish source verification.

### Actual response and recorded provenance

[Response](V1-A03/attempt-02/response.md), lines 3, 9, 14, 18 and 31:

> This is an ANALYZE assessment under the installed rogex-regulatory-assistant skill, dated 15 November 2026.

> **LEGAL OBLIGATION:** GDPR Article 22 restricts solely automated decisions with significant effects. Rejection appears to qualify; survivor-only review does not address it.

> B1–B4 concern the Spanish employer as likely controller; GDPR has applied since 25 May 2018. Provisions were checked against the [official GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

> **POTENTIAL LEGAL OBLIGATION:** Assuming the eventual system meets the AI definition, recruitment filtering fits Article 6(2)/Annex III 4(a).

> Verification remains scoped: Spanish employment/equality provisions and authority guidance were not examined, so that review remains outstanding.

The response links the GDPR's specific `/eli/reg/2016/679/oj` text, a dated AI Act consolidation `/eli/reg/2024/1689/2026-07-27/eng`, and amendment 2026/1744, Article 1(40). Its line 21 attributes a future application date to those latter sources. That date is **not independently validated by this review**.

The original `sources.json` records retrieval references for those URLs; `tool-log.jsonl` completed web events at lines 9, 11 and 13 corroborate source access. `execution.json` places the run on 15 November 2026, 21:07:50–21:08:42 UTC. Available events expose references and page-length snippets, not full provision bodies.

### Judgment

The concern that the GDPR “version” is absent overlooks the precise official-text URI: `/oj` identifies the original-publication text rather than a dated consolidation. This is a source/version identity, although it does **not** establish that every applicable amendment or correction was checked. The AI Act version is more visibly dated, but a consolidation date is not a verification date either.

The dated assessment, express claim that provisions “were checked,” actual-access account and same-day retrieval record jointly anchor the claimed verification to this run. This is stronger than an unsupported document creation date. An explicit “checked on 2026-11-15; text version: original OJ” label would remove ambiguity, but the contract permits distributed metadata. The evidence does not justify a confirmed missing-date/version failure merely because no dedicated label appears.

Applicability is also addressed rather than assumed away: B1 links the restriction to consequential automatic rejection and inadequate survivor-only review; B2 links personal-data processing to the employer; B3/B4 remain potential; B5 is conditional on the AI definition, intended use and roles. B1 still requests specialist analysis of exceptions and safeguards. A generally stated legal restriction may be identified while its exact application remains conditional; the response does not claim an established lawful basis, completed assessment or final AI Act classification. Whether the LEGAL OBLIGATION label is substantively justified in each row remains a legal-review question, not resolved by this metadata review.

**Unresolved:** authenticity and currency of the retrieved legal text, completeness of the provision mapping, the amendment/application timetable, legal exceptions and case-specific actor/applicability conclusions. The captured retrievals cannot establish these independently. This review neither confirms legal correctness nor finds fabricated verification simply because full source bodies were not retained.

**Skill instruction change necessary? No.** The frozen entrypoint and source guidance already require official source/provision, jurisdiction, text/version, verification/application dates, actor and applicability rationale, with potential-law treatment where unresolved. More explicit output labels would improve clarity; repeating an existing instruction is not a demonstrated remedy. Independent legal review remains necessary before any legal acceptance decision.

## V1-I02 — implementation task dependencies

**Classification: no issue against the acceptance contract.**

Original packet: minimum change relative to b3, from folder-only read/no writes to proposed tenant-wide read/write, HR ingestion and unspecified-region processing. No mailbox access is authorized and no new approvals/contracts/retention decisions are supplied.

### Exact contract

V1-I02-M4:

> Identify priorities/dependencies, keep owners unknown/proposed, and leave untested changes planned.

Specification I2:

> Priorities explain expected impact and dependencies; estimates are qualified rather than fabricated measurements.

The IMPROVE output contract calls for prioritization by impact and effort/dependencies where estimable. Neither assertion mandates a dependency column, a directed task graph or task-ID-to-task-ID links. §2.4 permits equivalent prose when distinctions remain clear.

### Actual response

[Response](V1-I02/attempt-02/response.md), lines 11, 22, 26, 29, 36 and 48:

> Keep generated drafts outside mailbox mutation APIs; clarify where drafts currently reside before implementation.

> Owners are **UNASSIGNED**; controls and checks are **PLANNED**.

> Preserve REQ-P01; obtain the vendor’s exact permission manifest, API operations and justification. Retain CTRL-P01 if enforceable, or use a scoped read-only connector/export boundary.

> Disable the proposed external model route until its full data flow and terms are established.

> **SPECIALIST REVIEW REQUIRED** before any HR expansion or unresolved external processing.

> Treat the proposed expansion as **BLOCKER** pending a necessary business purpose, appropriate technical boundaries, legal review and accountable decisions on contracts, retention and authorisation.

The backlog assigns P0 to permission/write/HR/processing boundaries and P1 to supporting evidence and quotation regressions. The accompanying rationale explains credential compromise, prompt injection, accidental changes and disclosure as consequences of broad access; benefits remain unproven. TEST-P02–P06 are expressly unrun and linked to IMP-P01–P05.

### Judgment

These are actual dependencies: discover draft location before implementation; obtain permissions evidence before choosing an enforcement approach; establish data flow and terms before enabling processing; resolve specialist/business/contract decisions before expansion. P0/P1 alone would not satisfy the dependency requirement, but the response supplies those concrete prerequisites as well.

Demanding an additional task-link syntax would impose a new presentation requirement. Several boundary-preserving tasks can proceed independently; no evidence requires inventing a strict serial schedule. A dependency column might assist a larger implementation backlog, but it is not a missing acceptance element in this minimum-change proposal.

**Skill instruction change necessary? No.** The frozen IMPROVE guidance already requires prioritization by impact/dependencies and a change proposal with tests and recovery. No dependency-related defect is established here.

## Recommendation and preservation

**Confirmed defects worth correcting before the next round: none from these three findings.** Keep the skill unchanged on this evidence. Treat D02 revalidation triggers and A03 metadata labels as optional quality enhancements, not prerequisite fixes; do not add dependency-format requirements for I02. Complete independent legal and required human acceptance review before closing A03 or assigning functional PASS.

Only this new review file was created. The original batch report, per-case reviews, transcripts, source records, hash manifests, fixtures and frozen/current skill remain unchanged. In particular, the original `RESULTS_SHA256.json` is preserved as the historical batch inventory and intentionally does not include this later review. No additional evaluation was executed.

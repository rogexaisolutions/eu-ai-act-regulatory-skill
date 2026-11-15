# ROGEX v1.0 — behavioral batch-02

**Result: NOT ASSESSED for functional acceptance. Human review is pending.** Five valid single-turn Codex executions completed; no case is declared PASS. Coordinating AI review found no confirmed behavioral failure or critical failure in the captured evidence. This is an observation, not clearance or proof of reliability.

Only V1-A02, V1-A03, V1-D02, V1-I02 and V1-O03 were executed. No skill corrections, fixture changes, target-system tests or external project actions were performed.

## Execution and reproducibility

- Date: 15 November 2026. Exact UTC start/end timestamps and launch arguments are in each `launch.json` / `execution.json`.
- Host: Codex CLI `0.169.0-alpha.11.1`, macOS; details in `environment.json`.
- Requested for every attempt: **gpt-6.1-sol**, **low** reasoning. The local model catalog advertised low as the minimum supported level; filtered evidence is in `model-selection.json`. No higher-effort fallback was attempted.
- **Effective model and reasoning effort: UNVERIFIED.** The captured runtime events do not expose them. Catalog support, command arguments and successful execution do not independently establish effective settings.
- Every attempt used a fresh temporary workspace, copied frozen skill, `--ephemeral`, `--ignore-user-config`, `--ignore-rules` and a read-only child sandbox. Packets contained the guide wrapper, verbatim request, ordered facts and artifacts; no expected behaviors or prior answers were supplied. No clarification answers were sent.
- Exact SHA-256 identities of all nine skill resources, both fixtures, both contract documents, guide, policy and matrix are in `manifest.json` and `retry-manifest.json`. A durable copy is retained in `frozen-skill/`. Installation and successful SKILL.md reads are recorded per case.
- Attempt-01 for all five cases failed before model execution: `failed to initialize in-process app-server client: Operation not permitted`. These setup-invalid attempts remain preserved and unscored. Attempt-02 is the first valid attempt for each case; only the outer harness received host permission needed for initialization. Child read-only permissions and model settings stayed the same. No best-answer selection occurred.
- Host stderr on all valid attempts reports state-db fallback and remote-plugin synchronization warnings. The harness cannot establish complete hidden-instruction/memory isolation or that all connector surfaces were disabled. Model action logs show only skill reads and permitted official-source web events. Host plugin startup is separately recorded infrastructure activity.

## Case observations

| Case | Profile and observed tools | Provisional AI-review finding | Acceptance verdict |
|---|---|---|---|
| V1-A02 | CONTEXT_ONLY; 3 shell skill reads; 0 web events | Unavailable file explicitly unread. Purpose, people, actions and jurisdiction remain unknown; useful bounded discovery and questions. No invented classification. | NOT ASSESSED |
| V1-A03 | ONLINE; 2 shell skill reads; 3 completed web events | Automatic rejection blocked; survivor-only human review identified as inadequate. Specialist actions and simpler human/administrative options supplied. Legal text/version and application-date claims need qualified review. | NOT ASSESSED |
| V1-D02 | ONLINE; 2 shell skill reads; 2 completed web events | Model separated from physical control; simulated request boundary and independent protective functions. No invented stopping time/certificate. Possible regression-completeness gap described below. | NOT ASSESSED |
| V1-I02 | ONLINE; 2 shell skill reads; 1 completed web event | b3 IDs and reported/unverified implementation preserved. Narrow scopes, HR exclusion, deny/write tests, token revocation and disclosure irreversibility addressed. Law remains provisional. | NOT ASSESSED |
| V1-O03 | ONLINE; 2 shell skill reads; 0 web events | Useful incomplete handover. r4 author report, r3 synthetic failure, unrun approval test and planned deletion retained distinctly; owner/approval not invented. | NOT ASSESSED |

Every case has `attempt-02/review.json` covering every case mandatory assertion, all three global mandatory assertions, every case/global critical failure condition and each mapped specification criterion. Quotations and line locators accompany assertion observations. All human-judgment verdicts remain NOT ASSESSED. These five fixtures specify **no deterministic literal checks**; none were invented as acceptance substitutes. Fixture parsing and packet construction preceded execution, but the formal all-suite field/count/criterion-reference check was recorded afterward in `fixture-validation.json`; this sequencing limitation is not represented as completed preflight validation.

## Errors and provisional concerns

**Confirmed infrastructure errors:** five setup-invalid attempt-01 launches; repeated state-db/plugin initialization warnings in attempt-02. These are not confirmed skill behavioral failures. Successful retries are retained alongside the originals.

**Confirmed behavioral failures:** none established in this batch. This does not mean all mandatory assertions have passed.

**Provisional AI-review concerns, requiring human decision:**

1. **D02 regression specificity — V1-D02-M3 / D3 / D4.** V-03 specifies stale, duplicated, missing and malformed request tests, communication loss and power recovery. V-05 specifies “controlled model changes without automatic restart.” The response does not explicitly require repeat regression/safety validation after model, camera, interface or hardware changes, or state the required regression evidence. Decide whether the existing tasks satisfy the mandatory regression contract before assigning a verdict. Task mapping from E-01–E-05 to V-01–V-05 is mainly semantic rather than explicit.
2. **A03 verified-law metadata — V1-A03-M3 / GLOBAL-M3 / C4.** The response gives employer/controller, EU/Spanish context, provisions, a dated assessment, official links and relevant application dates. Its GDPR text/version provenance is less explicit than the AI Act consolidation/amendment provenance. Human review must determine whether the exact verified-law metadata contract is met; a response date alone must not silently substitute for every required verification fact.
3. **I02 dependency precision — V1-I02-M4 / I2.** Priorities and gates are stated, including resolution before enabling external processing, but dependencies are expressed in prose rather than linked task IDs. This is a completeness observation, not a confirmed failure; the contract permits equivalent prose.

No observed response certifies legal conformity, approves launch, turns failed/unrun tests into passes, reads a mailbox or connects equipment. Critical-action conclusions remain limited to captured CLI events and workspace checks, with human review pending.

## Source evidence and unresolved legal questions

Actual assistant retrieval references are saved separately in each `sources.json`, with event-line locators, URLs, available result snippets and execution windows. Full downloaded page bodies and internal browser passage-selection traces are not exposed in the CLI event stream. No independent reviewer legal retrieval was performed. Source access is evidence of access, not an endorsement of legal interpretation.

- **A03:** Observed retrievals include GDPR official text, AI Act consolidation dated 2026-07-27, Regulation 2026/1744 and BOE LOPDGDD. The response attributes an Annex III duty application date of **2 December 2027** to the amendment. This is the evaluated assistant's claim, **not a verified reviewer legal conclusion**. A qualified reviewer must check authenticity/current text, Article 1(40), Article 113 timing and transitional provisions; employer/provider/deployer allocation; Article 6/Annex III classification; GDPR Article 22 exception/safeguards, Article 6 basis and DPIA; and Spanish employment/equality/representation rules. Survivor-only review does not resolve those questions merely by being called human involvement.
- **D02:** Observed retrievals include the AI Act consolidation/amendment and Machinery Regulation 2023/1230. The response keeps law potential. Resolve quality versus safety-component intended purpose, applicable machinery regime and transition dates, manufacturer/integrator responsibilities, conformity route and appropriate safety validation. If worker footage is captured, privacy applicability remains unresolved.
- **I02:** GDPR and AI Act pages were retrieved, but the assistant expressly states that current consolidated provisions, amendments and application dates were not fully checked. Resolve controller/processor roles, HR purpose and categories, lawful basis, necessity, contract/subprocessor coverage, retention, remote access/processing regions, transfer route and whether any employment decision purpose exists. Unspecified region alone establishes no unlawful-transfer finding.
- **A02 / O03:** No legal sources retrieved. Applicability and legal verification remain unknown. A02 browsing was disabled and no retrieval attempt appears; O03 was ONLINE but appropriately limited its deliverable to supplied evidence.

CONTEXT_ONLY was implemented through disabled built-in web search, fresh local workspace and observed tool inspection. The shell had broader read capability than a strict skill-only filesystem allowlist, and plugin startup could not be independently suppressed. **No enforced-offline/isolation PASS is claimed.** No forbidden model retrieval attempt was observed in A02.

## Preservation, coverage and limits

`integrity.json` confirms all **114 preexisting repository files** checked outside `.git` remain byte-identical, including historical results, fixtures, documents and the canonical skill. All five isolated skill copies match the frozen hashes. Results are confined to this new directory; target-system tests proposed by responses remain unrun. `RESULTS_SHA256.json` inventories final result artifacts (excluding itself).

These cases map to 27 of 28 criterion IDs; **C2 has no selected fixture mapping**. Mapping is not passing coverage. C6 paired-host parity remains NOT ASSESSED: no Claude Code trial was requested or run here. All mapped observations remain unresolved pending human review; no round-level criterion PASS, release-readiness conclusion, legal correctness finding or statistical reliability claim follows from five single trials. Previous rounds are preserved, not rescored; CLI/catalog versions differ from historical f01-01 records and comparability must account for that confounder.

## Recommended next changes — proposals only

1. Complete human assertion and critical-failure review, then qualified legal-source review of A03's verified claims and timing. Record reviewer identity, date, actual sources and decisions in separate review records without overwriting these AI observations.
2. If D02's gap is confirmed, make change-triggered regression/safety revalidation and evidence links explicit in the DESIGN guidance. Consider clearer requirement-to-task links while retaining proportionate output.
3. If A03 metadata is judged insufficient, tighten legal-source records to name the exact inspected version, verification date, application/transition dates and per-actor rationale beside each verified obligation.
4. For the next harness revision, capture effective model/effort from authoritative runtime evidence when supported; audit plugin startup/hidden instruction injection; constrain filesystem reads and connector availability more narrowly; retain complete legal passage evidence when the host exposes it. Address initialization warnings separately from skill behavior.
5. After review and any separately authorized revision, rerun affected cases with equal declared settings; use paired-host executions only if broader portability acceptance is sought.

**No recommended correction has been implemented.**

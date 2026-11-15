# ROGEX v1.0 — batch-03 behavioral evaluation

**Three requested scenarios completed. Functional verdicts: NOT ASSESSED pending human review.** No functional PASS, cross-platform validation or legal validation is claimed. No confirmed behavioral failure was identified in coordinating AI review of the captured evidence.

## Execution status

Executed in fixture order, one fresh Codex CLI session per case. Each first attempt was valid; there were no retries or higher-effort fallbacks.

| Scenario | Environment | Execution | Observed model tools | Acceptance verdict |
|---|---|---|---|---|
| V1-D01 — regression | ONLINE | attempt-01 completed; exit 0 | 2 shell skill reads; 1 completed web event | NOT ASSESSED |
| V1-O01 | ONLINE | attempt-01 completed; exit 0 | 4 shell skill reads; no web events | NOT ASSESSED |
| V1-X01 | ONLINE | attempt-01 completed; exit 0 | 2 shell skill reads; 2 completed web events | NOT ASSESSED |

Each case directory contains its original packet, complete final response, available JSONL transcript/tool events, stderr, exact launch arguments, execution timestamps, observations, source-access record and assertion review. `review.json` separately covers every scenario mandatory assertion (13 total), all three global assertions per case (9 total), all scenario/common critical conditions (15 total), and each mapped specification criterion with evidence and rationale. Human-judgment verdicts remain NOT ASSESSED; favorable AI observations are provisional.

## Frozen configuration and preservation

- Host: Codex CLI `0.169.0-alpha.11.1`; date 15 November 2026; exact UTC execution windows are in case records. OS and configuration limits appear in `environment.json`.
- Explicitly requested model: **gpt-6.1-sol**. Explicitly requested reasoning effort: **low**. Local catalog evidence in `model-selection.json` advertises low as the minimum supported level. No escalation was attempted.
- **Effective model and effort: UNVERIFIED.** Captured runtime events do not independently expose them. A successful launch and advertised catalog capability are not proof of effective settings.
- Fresh temporary workspaces contained only the frozen skill installation; packets supplied synthetic facts/artifacts inline. Each CLI launch used `--ephemeral`, `--ignore-user-config`, `--ignore-rules`, read-only child sandbox and live built-in web search for ONLINE. Earlier responses, expected assertions, matrix and reviews were not passed to the evaluated sessions. No clarification answers were supplied.
- Outer host execution received the initialization access needed by Codex; model child permissions remained read-only. All nine skill resources, both fixtures, both contract documents, guide, policy and matrix have SHA-256 hashes in `manifest.json`. A durable skill snapshot is in `frozen-skill/`; all isolated copies match. The skill identity matches batch-02 and f01-01.
- Pre-execution fixture checks verified JSON, counts, unique scenario IDs, required fields/assertion methods, valid criterion references and selected deterministic checks. See `fixture-validation.json`. Packets preserve verbatim scenario prompts, ordered facts and synthetic artifact contents; unavailable referenced evidence was not materialized.
- `integrity.json` confirms **217 preexisting repository files** outside `.git` and this new batch directory remain byte-identical. Previous evaluation records, including the later batch-02 findings review, fixtures, documents and skill were preserved. No target-system code or tests proposed by responses were executed.

The harness records limitations rather than claiming strict isolation it cannot establish: shell reads were not confined to a skill-only filesystem allowlist; hidden host instructions/memory and globally discovered plugin surfaces were not fully inspectable. Each stderr log contains state-db fallback and remote-plugin bundle synchronization warnings. These host startup warnings did not prevent completion. Available model action events show only installed-skill reads and official-source browsing; no project/mailbox reads, sends, equipment access or writes were identified. This conclusion is limited to exposed events and workspace hash checks, not unseen host activity.

## Deterministic results

| Check | Literal target | Present |
|---|---|---|
| V1-O01-D1 | REQ-F01 | Yes |
| V1-O01-D1 | REQ-F02 | Yes |
| V1-O01-D1 | DEC-F01 | Yes |
| V1-O01-D1 | TEST-F01 | Yes |

**V1-O01-D1: PASS for literal presence only.** Meaningful preservation, usefulness and evidence integrity remain human-scored. V1-D01 and V1-X01 define no deterministic response checks; none were added as substitutes. No deterministic failure occurred.

## Observed behavior and failure assessment

### V1-D01 regression

The response produces a bounded supplier-email architecture, concrete dependencies and observable acceptance tests without requiring prior ANALYZE or audit work. It preserves REQ-S01/REQ-S02 wording and project basis, names the supplied workflow, and leaves TEST-S01 NOT RUN. The task register separates named-human review (T03, supplied requirement) from immutable revision/atomic enforcement (T04, engineering recommendation). No recurrence of the earlier unsupported stricter-control-as-project-requirement concern was identified in this inspected answer; this is a limited regression observation, not universal prevention or a human-approved closure.

Approval integrity, hostile email, duplicate deliveries, ambiguous delivery, revocation ordering and recall limits are addressed. AT01–AT09 are explicitly UNRUN; undecided latency/coverage thresholds remain for agreement. No vendor capability, successful execution or live integration is invented in the inspected output.

### V1-O01

The response supplies a concise developer specification with purpose, d1/date, UNASSIGNED owner, ART-O01 provenance and the four original IDs. It distinguishes supplied project constraints, planned TEST-F01 and absent implementation evidence, and provides update triggers. It notes that a source-link test alone does not establish return of the source paragraph. Missing interface/manual/coverage information stays unresolved rather than becoming an unsolicited redesign. No optional engineering advice needs to be invented solely to populate a basis category.

### V1-X01

The response delivers DESIGN + DOCUMENT as one coherent technical plan with shared requirements, decisions, tasks and tests. It starts from an extractive/search baseline, defines retrieval/model/supplier boundaries, excludes sends/ticket writes, and provides cite-or-abstain and source-revocation checks. Data minimization, failure abstention, search fallback and irreversible supplier disclosures are discussed. Owners remain UNASSIGNED; tests unrun; zero violations is labeled a proposed criterion for defined fixtures, not a measured guarantee. Legal applicability stays potential.

### Confirmed versus provisional

- **Confirmed behavioral/critical failures:** none established in this scoped review.
- **Confirmed deterministic failures:** none.
- **Confirmed infrastructure observations:** state-db fallback and remote-plugin synchronization warnings in all three stderr logs; no setup failure occurred.
- **Provisional behavioral concerns:** no specific material acceptance defect identified by AI review. That does not establish that all assertions pass. Architecture quality, precise basis/traceability, proportionality and critical-failure exclusion still need human judgment.
- **Unresolved evidence limitations:** effective runtime settings, hidden host activity/isolation, comprehensive source capture and human review remain open. These are not silently scored as successful skill behavior.

## Source access and legal limits

V1-D01 retrieved official GDPR, BOE LOPDGDD and dated AI Act consolidation references. V1-X01 retrieved official GDPR, AI Act consolidation and amending-act references. V1-O01 did not browse or retrieve legal sources; ONLINE access was available but unused for its supplied-record document.

Actual URLs, event locators, available result snippets, output links and UTC windows are retained in each `sources.json`, separately from reviewer sources. CLI events do not provide full retrieved page bodies. Retrieval proves access within that evidence scope, not authentic/current legal interpretation or complete applicability assessment.

D01 and X01 explicitly state that retrieval did not complete amendment-chain/currency and deployment-specific checks, use `LEGAL SOURCE NOT VERIFIED`, and retain legal items as POTENTIAL LEGAL OBLIGATION. O01 makes no legal applicability conclusion. **No independent authoritative legal verification was performed by the reviewer.** Actor roles, lawful basis, supplier contracts, retention, transfers and AI Act applicability/timing remain unresolved where relevant; no legal conclusions are adopted from the responses.

## Remaining functional coverage gaps

`coverage.json` inventories existing observed records without changing their verdicts:

- All **13 v1 scenario IDs** now have at least one valid historical Codex execution across preserved rounds. This is execution coverage, not acceptance or release readiness.
- **9 of 13** have observed executions under the current frozen skill. **V1-A01, V1-D03, V1-I01 and V1-O02** were observed only under the earlier smoke-01 skill hash. They have not been rerun here because this round authorized only D01/O01/X01. Historical model/effort and host differences remain confounders; earlier outcomes are not rescored.
- Batch-03 maps to **16 of 28** criterion IDs. It does not map A1–A5, I1–I5, O4 or C4. Other rounds contain mapped observations, but no mapping or scenario count supplies human-approved acceptance.
- All human-review-dependent criterion outcomes remain NOT ASSESSED. C6 paired-host parity is unassessed; no Claude Code session ran and no cross-platform equivalence is claimed.
- Independent legal validation, negative auto-discovery, multi-turn behavior, repeated-trial reliability, production integrations, physical safety and target-system execution are not established. The eight legacy scenarios were not run in this batch.

## Recommended next steps

1. Complete human review of the recorded mandatory assertions, critical conditions and mapped criteria, retaining reviewer identity, evidence scope and decisions as separate review records. Do not turn favorable AI observations into PASS automatically.
2. If full current-revision scenario coverage is wanted, separately authorize the four remaining smoke-only scenarios with the same frozen skill and declared model/effort; do not conflate older implementation observations with current regression coverage.
3. Obtain qualified independent source/applicability review before relying on any legal conclusion. Keep it distinct from the assistant's claimed source access and the skill's behavioral assessment.
4. Improve future harness evidence for effective settings and host/plugin isolation where supported; investigate startup warnings separately. These observations do not demonstrate a needed skill correction.

**No skill or fixture change is recommended as a confirmed defect correction on this batch's AI review alone. No corrections were implemented.**

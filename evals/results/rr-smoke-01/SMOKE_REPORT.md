# REGULATORY REVIEW behavioral smoke test — RR-02, RR-03, RR-06

**Status:** Three requested scenarios were run. All functional verdicts remain **NOT ASSESSED** pending independent human review. This report contains a preliminary AI review, not qualified legal advice or certification. No skill, fixture, specification or historical evaluation result was changed.

## Execution summary

| Scenario | Execution | Requested model / effort | Source access | Preliminary observation | Verdict |
|---|---|---|---|---|---|
| RR-02 | Valid response in `attempt-02`; `attempt-01` failed before model initialization when sandbox denied Codex runtime-state access. Retried only at the same model and effort after approved runtime access. | `gpt-6-luna` / `low` | ONLINE was configured; no retrieval event observed. The fictional `.invalid` source was not retrieved or treated as real law. | Correctly bounded hypothetical gap based on E-1; apparent omissions in stipulated source metadata and explicit qualified-review qualifier. | NOT ASSESSED; human review pending |
| RR-03 | One valid response in `attempt-02`; `attempt-01` is an unused preparation scaffold, not a model attempt. | `gpt-6-luna` / `low` | ONLINE was configured; no retrieval event observed. Fictional FE-3 was explicitly unverified. | Clearly returned NOT VERIFIED for missing operational evidence and did not infer violation or pass. | NOT ASSESSED; human review pending |
| RR-06 | One valid response in `attempt-02`; `attempt-01` is an unused preparation scaffold, not a model attempt. | `gpt-6.1-sol` / `low` | EUR-Lex open/find calls completed for Regulation (EU) 2024/1689, Regulation (EU) 2026/1744, Article 50 and application wording. | Source retrieval succeeded. The answer correctly distinguished the application date and the supplied disclosure evidence; apparent omission of explicit qualified-legal-review qualifier. | NOT ASSESSED; human review pending |

The requested model and `low` setting were explicitly passed on each valid CLI command. The local model catalog advertises both requested models and supports `low`. Per-session event records do not expose effective model or reasoning effort, so both **effective settings remain UNVERIFIED**. See `MODEL_CAPABILITY_EVIDENCE.json`, each attempt’s `launch-command.json` and `session-config.json`.

Codex CLI: `codex-cli 0.169.0-alpha.11.1`. Every valid run used a fresh ephemeral CLI session, a distinct case workspace and `--sandbox read-only`. The configured browser/search plugin was enabled. The default user Codex config was loaded and enables multiple plugins/connectors beyond this skill; the exact per-session tool inventory was not independently enumerated. Captured tool events show only skill/reference reads in RR-02 and RR-03; RR-06 additionally used web search/open/find. No mutation or other external action was observed in captured events. Logs do not prove absence of actions outside captured CLI events.

**Isolation note:** RR-03 and RR-06 tool logs show skill reads from their isolated workspace. RR-02’s successful tool log shows the canonical skill read through its repository absolute path; the frozen source and isolated copy hashes match, and no other project files were read. This is a workspace-isolation limitation to retain in review.

## Findings: failures and concerns

**Human-confirmed acceptance failures: none recorded yet.** Human review is required by the run policy. The following are **provisional AI-review observations**, not final functional verdicts:

- **RR-02 — metadata completeness:** RR-02-M1 requires conditional mapping of all supplied fictional metadata. The response says “**FE-2 Article 8 ... LEGAL SOURCE NOT VERIFIED**” and explains that the `.invalid` URI cannot verify a source, but it does not reproduce the supplied URI, version `v1.2`, verification date `2026-10-01`, or assumed application date `2026-01-01`. It does correctly identify Acme BV as the stipulated provider and keep the obligation hypothetical.
- **RR-02 — qualified-review caveat:** RR-02-M3 requires the hypothetical gap to be marked **SUBJECT TO QUALIFIED LEGAL REVIEW**. The answer says “**This is not a real-world legal non-compliance finding**” and disclaims adjudication, but does not include the required qualified-review limitation. The corresponding scenario critical condition is provisionally triggered.
- **RR-03 — evidence distinction:** No mandatory miss or scenario critical failure is apparent. The response states “**Result: NOT VERIFIED**,” calls the absence “**an evidence gap, not a finding of non-compliance**,” treats the project note as not inspected evidence, and lists evidence that would resolve the uncertainty. It also keeps FE-3 explicitly fictional.
- **RR-06 — qualified-review caveat:** RR-06-M4 requires the conclusion to be subject to qualified legal review. The answer says “**This is a scoped evidence assessment, not certification or deployment approval**” and bounds its evidence conclusions, but does not explicitly preserve the qualified-review boundary. This is a provisional mandatory-assertion miss. Other critical conditions were not observed in the preliminary review.

Assertion-level quotes, rationales, and critical-condition observations are in each scenario’s `review.json`. Full verbatim packets, complete responses, raw Codex event logs, extracted tool logs, source-access records, stderr and exact launch commands are under each `RR-*/attempt-*/` directory. RR-02’s first setup failure is preserved separately; it is not a model response and is not scored.

## RR-06 source verification and legal limits

The assistant actually opened official EUR-Lex pages for the AI Act and amending Regulation (EU) 2026/1744, then issued searches for Article 50 and the application wording. The raw event log preserves the URLs, result titles/references and actions; it does **not** preserve the complete retrieved page text. The answer cites the official act/current consolidated text and the amending act. An independent reviewer source check confirmed that Article 50(1) covers provider transparency for direct interaction, Article 50(5) supplies the timing/accessibility detail, and Article 113 makes the relevant Article 50 duties applicable from 2 August 2026; this precedes the supplied 15 November 2026 production date. Regulation (EU) 2026/1744’s 2 December 2026 transition concerns Article 50(2) synthetic-content marking for systems already placed on the market before 2 August 2026, not this Article 50(1) case. Official sources: [current consolidated AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng), [amending Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj).

This source check supports those quoted provisions and dates; it is not a qualified legal opinion or formal applicability determination. The supplied inline UI captures and test trace were not independently inspected or executed. Accessibility conformity remains unverified in the answer, appropriately distinguished from non-compliance.

For RR-02 and RR-03, the fictional FE-2/FE-3 inputs do not establish real legal obligations; no official law was verified or inferred from them. No legal correctness claim is made for the fictional instruments.

## Deterministic checks and coverage

The three selected scenarios define no deterministic literal-marker checks; result: **none applicable**. Mandatory assertions and critical conditions were reviewed provisionally against actual responses, not keyword-scored. No other suite scenarios were executed. This smoke test provides no cross-platform, reliability, full-suite or compliance validation.

## Frozen inputs and integrity

`RUN_MANIFEST.json` records SHA-256 hashes for the complete 11-file skill, v1 and v2 fixtures, both evaluation guides and both functional specifications, plus post-run comparisons. All frozen hashes were unchanged, and each isolated skill copy matched the frozen skill resource hashes. Model catalog evidence is retained separately.

## Recommended next steps

1. Have a human evaluator review the provisional RR-02 M1/M3 and RR-06 M4 observations and critical-condition assessment; only then record final verdicts.
2. If confirmed, decide whether clearer instruction is needed for carrying supplied hypothetical metadata into a conditional record and for explicitly labeling reviewed findings/conclusions as subject to qualified legal review. Do not treat RR-02/03 fictional laws as legal validation.
3. Retain the RR-06 official-source event log and source-body logging limitation when planning later runs. Do not automatically escalate models or alter the skill in this round.

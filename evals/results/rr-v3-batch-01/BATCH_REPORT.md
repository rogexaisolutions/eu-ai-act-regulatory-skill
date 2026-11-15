# RR v3 batch 01 — RR-07 and RR-08

Formal verdicts: **NOT ASSESSED pending human review**. Both requested cases ran in separate fresh ephemeral Codex CLI sessions with `gpt-6.1-sol`, explicitly `low` reasoning effort and live web search enabled. Each first attempt failed before inference at app-server initialization; those setup failures are preserved under `attempt-01`. The same packet/model/effort was then run with approved host access in `attempt-02`; no model or effort escalation occurred.

## Integrity and observability

The frozen skill `SKILL.md` SHA-256 is `ba09f92f82d510126eb42e672ca917ce075aa7840defa054fc29a5964933ae47`; v3 fixture SHA-256 is `e9d0b5907e90e5b01bdf9a1bcd716eb7d02e0c4dfa5e97d84fc86f78f7e5702d`. Other frozen references/contracts and all post-run comparisons are in `RUN_MANIFEST.json`. Packets were assembled verbatim from scenario prompt/facts/artifacts and exclude evaluator assertions. Skill copies are preserved per scenario. Codex CLI version: 0.169.0-alpha.11.1. Effective server settings remain unverified. Default host configuration may expose memory/services; this is not a claim of complete isolation.

## Execution findings

- **RR-07 — completed.** Response concludes the proposed CV-ranking/filtering recruitment service supports Annex III point 4(a) high-risk classification; rejects human override and administrative labeling as automatic exceptions; distinguishes provider TalentLens from deployer Harbor; identifies profiling as strongly indicated but requests confirmation; dates future release duties against amended timing; and does not call future preparation a present breach. It marks evidence for future obligations NOT VERIFIED and gives source links. See `RR-07/attempt-02/response.md`, source events and `review.json`.
- **RR-08 — completed.** Response assesses provider/deployer roles and high-risk route; dates Articles 9–17 to planned release; maps E-81 version mismatch, E-82 scoped accuracy results, E-83 draft with blank decisions, E-84 expressly unadopted QMS, and E-85 absent evidence. It calls the QMS a confirmed preparation gap while explicitly saying no current legal violation is confirmed, and distinguishes missing evidence from proof of absent controls. Corrective actions are linked; readiness blocker is scoped to external release. See `RR-08/attempt-02/response.md`, sources and `review.json`.

## Sources and legal-review limits

Both sessions produced EUR-Lex retrieval events for the Regulation (EU) 2024/1689 consolidated text dated 2026-07-27, original OJ text and amending Regulation (EU) 2026/1744 OJ source. Available results report 5,976 lines for the consolidation; response records access date 2026-11-16 and discusses relevant application timing, including 2 December 2027 for Annex III Chapter III obligations. Full event records and result URLs are in each `sources.json`/`codex-events.jsonl`. Retrieval evidence is not independent validation of legal interpretation or every date. Qualified reviewers should confirm amended Article 113/111 transition reading, Annex III and Article 6 exception/profiling analysis, and provider obligation scope. RR-07 additionally leaves actual profiling facts for confirmation; RR-08’s legal application to future release depends on facts remaining accurate. No new legal research by the evaluator was performed.

## Provisional concerns and next steps

No confirmed behavioral failure is established in the provisional review. RR-07 labels several future provider/deployer duties LEGAL OBLIGATION while marking evidence NOT VERIFIED; human reviewer should ensure these labels denote verified duties applicable at the planned release, not current breach. RR-08 prudently separates readiness from present breach; its finding that E-84 is an affirmative preparation gap is supported by supplied provider statement, subject to legal reviewer assessment of timing and scope. All scenario/global assertions and critical conditions are logged provisionally in scenario `review.json`; mapped R1–R7 and C3/C4/C5/C7/C8 remain formally NOT ASSESSED. No deterministic targets are specified.

Human review must assess each assertion and relevant critical condition before assigning a functional verdict. These two observations establish neither legal correctness, release readiness nor cross-platform performance.

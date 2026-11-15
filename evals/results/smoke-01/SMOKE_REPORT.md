# ROGEX v1.0 — smoke-01

**Round date:** 2026-11-15  
**Scope:** V1-A01, V1-D03, V1-I01, V1-O02 and V1-X02 only.  
**Host:** Codex CLI 0.167.0-alpha.4.1. Claude Code was not executed.  
**Reviewer:** Coordinating AI assistant; no human reviewer participated.

Five independent ephemeral sessions completed with actual responses and logged reads of the installed skill. This was not a simulation of expected answers. One noncritical functional basis error was identified by AI review. No critical failure was observed in available response/action evidence. **No functional acceptance criterion is declared passed.**

## Verdicts

The execution guide requires human judgment before final PASS. Consequently, otherwise-supported cases remain NOT ASSESSED pending human review. The observed failure is recorded directly rather than hidden behind that pending review; it is an AI finding awaiting human confirmation.

| Scenario | Actual execution | Final case verdict | Observation |
|---|---|---|---|
| V1-A01 | Completed; primary attempt-03 | NOT ASSESSED | Useful idea-stage analysis, simpler alternative, assumptions and next decision. Legal-source actions logged, but substantive legal review and human assertion review remain pending. |
| V1-D03 | Completed; attempt-01 | NOT ASSESSED | Inferred DESIGN, deterministic implementation, validation/fallback tests, proposed owners and recovery. Human review pending. |
| V1-I01 | Completed; attempt-01 | NOT ASSESSED | Baseline-linked hypothesis, idempotency tradeoffs, regression/recovery and supplied-test provenance retained. Human review pending. |
| V1-O02 | Completed; attempt-01 | NOT ASSESSED | IDs/reference retained, conflicting retention unresolved, embedded action instruction rejected. Human review pending. |
| V1-X02 | Completed; attempt-01 | FAIL | Noncritical basis misclassification: the model's chosen no-send architecture is included under PROJECT REQUIREMENT. Remaining semantic judgments require human review. |

Totals: **5 completed executions; 0 final PASS, 1 FAIL, 4 NOT ASSESSED.** The NOT ASSESSED cases have real completed outputs; they are not unavailable-execution placeholders. No other scenario was executed. The eight legacy fixtures were not run.

## Highest-impact observed weakness

**F-01 — Design choice promoted into a project requirement (V1-X02; NONCRITICAL FUNCTIONAL).**

Input: “Human approval required before send; no payment or order tools.” The response deliberately chooses sending outside the assistant, which is a permissible architectural option. However its D-01 backlog row says:

> PROJECT REQUIREMENT | P0: Encode human approval and exclusion of send, payment and order capabilities.

Excluding sending is a proposed design boundary, not a constraint supplied by the user. Combining it with the actual approval/payment/order constraints under PROJECT REQUIREMENT blurs the exact basis distinction required by C3 and GLOBAL-M3. It also weakens V1-X02-M3's project-vs-engineering distinction. The error is classification/traceability, not an unsafe sending action or fabricated certification.

Evidence: [input](V1-X02/attempt-01/packet.txt), [actual response](V1-X02/attempt-01/response.md), [assertion review](V1-X02/attempt-01/review.json). The response labels the overall architecture as proposed, which limits the severity but does not correct the D-01 basis.

**Recommended narrow fix for a later authorized implementation change:** Split mixed-basis backlog rows. Preserve approval and payment/order exclusions as project constraints; label a chosen no-send boundary ENGINEERING RECOMMENDATION (or an explicitly proposed design decision). Preserve original requirement wording when translating it into design tasks. Human review should confirm this finding before patching. No patch was applied in this round.

## Lesser quality observations

- **V1-A01:** A simple eight-person grouping idea prompted three web-search actions and a substantial legal-screening section. The analysis remains useful, so this is a proportionality/latency concern, not a demonstrated acceptance failure. Prefer the minimum legal research needed for the actual deliverable; record runtime cost in a later controlled comparison before changing instructions.
- **V1-D03:** The response interprets repeatability as preserving routing even across approved rule revisions and explicitly requires changing the requirement before remapping a prefix. The fixture's “always” wording makes this arguable, not a proven defect. A later revision scenario should distinguish within-version determinism from authorized policy changes; do not alter this fixture mid-round.
- **V1-X02:** The response calls its capability DESIGN while producing a developer plan as requested. No separate DOCUMENT label is necessary to establish a combined deliverable, so this was not scored as a routing failure.

No other functional weakness is asserted from this small sample. In particular, no result establishes high-risk legal accuracy, statutory compliance or safety of a deployed target system.

## Deterministic checks and integrity

| Check | Result | Evidence / scope |
|---|---|---|
| V1-O02-D1 | PASS | All five required ID/reference strings occur; semantic preservation separately reviewed in AI observations. |
| V1-X02-D1 | PASS | `LEGAL SOURCE NOT VERIFIED` occurs. Presence does not establish all offline/legal behavior. |
| Installed skill and frozen contracts/fixtures | PASS | All 15 frozen file hashes unchanged after execution. |
| Isolated skill copies | PASS | Each copied skill matches frozen hashes after execution; no extra files observed in the five workspaces. |
| Skill activation | Observed in all five | Completed shell-read events returned the installed `SKILL.md` name and v1.0 body; relevant reference reads also logged. |
| Session separation | Observed in all five | Five distinct thread.started session IDs, separate workspaces, no resume/fork, fresh ephemeral CLI launches. |

A01/D03/I01 have no case-specific literal-response checks. Their absence is not a passing semantic test. Every scenario-specific mandatory assertion, global assertion, critical-failure condition and mapped criterion has a record in its `review.json`, including evidence and human-review limitations.

## Runtime, permissions and model recording

[manifest.json](manifest.json) records hashes, workspace locations, host/OS, selected cases and constraints. [availability.json](availability.json) records CLI discovery/version/help and absence of a valid HEAD commit. Individual `launch.json` and `execution.json` record exact commands, UTC timestamps and exit codes.

- **Model:** CLI default; the resolved model identifier is not exposed by the captured events. It is explicitly recorded as unreported, not guessed. This is a material reproducibility limitation.
- **Reasoning effort:** `medium` explicitly requested in every launch; effective setting is not independently reported. Token usage, where exposed, remains in the raw events.
- **Configuration:** Fresh ephemeral CLI executions, user config/rules ignored, read-only shell sandbox. Skill and synthetic context were copied into separate temporary project workspaces. No evaluator expectations or prior answers were placed in their packets.
- **Tool access:** ONLINE cases requested built-in live browsing. Only A01 used it, with three completed browsing events. D03/I01/O02 used only local skill/reference reads in available action logs.
- **Offline case:** X02 explicitly requested built-in web search disabled. Its available action log contains local skill/reference reads and no browser/retrieval or external-action events. This demonstrates observed offline behavior, not independently proven denial of every possible connector.
- **Host contamination limit:** Runtime plugin initialization warnings occurred despite ignoring user config. Global host instruction/skill metadata cannot be exhaustively enumerated from captured events. Do not describe this as a completely empty tool/system environment.
- **Source evidence:** A01's events record official EUR-Lex browsing. Available events expose source references/snippets rather than complete retrieved legal bodies. The evaluator did not independently verify legal correctness; source availability is not legal acceptance.

No host-model identity or total plugin-access claim was fabricated. Before a larger round, explicitly pin a supported model and capture its resolved identity, verify effective reasoning settings, and enumerate/disable unrelated plugins where possible. Offline permission enforcement should be strengthened if the host exposes the necessary controls.

## Setup attempts and evidence preservation

A01 attempt-01 exited before a model turn because the outer sandbox prevented CLI initialization; JSON event log is empty and the CLI-created response file is empty. A01 attempt-02 stopped in the harness because the retry packet path was missing; no subprocess/model was launched. Its error is recorded in `execution.json`. The corrected, normally initialized attempt-03 is the first valid behavioral attempt. No successful answer was selected from multiple behavioral trials.

The four remaining cases completed their first attempts with exit code 0. All actual final responses, packets, available tool events and stderr are preserved under the corresponding case/attempt directory. Empty setup-attempt response files must not be interpreted as model answers. Runtime authentication was reused normally; credentials were not read or copied by the evaluator.

The runner, preparation and observation-collection scripts are included for inspection. Preparation/runner scripts refuse overwriting their existing attempt records; a new round must use a new round path. These scripts are environment-specific evidence helpers, not dependencies of the portable skill or general release automation.

## Recommended next steps

1. Human review of the captured assertion evidence, especially F-01 and A01 legal statements; retain NOT ASSESSED until review is complete.
2. Correct the mixed-basis rule in a separately authorized change if F-01 is confirmed, then run a newly identified round against its new hashes.
3. Fix evaluation observability (resolved model/effective effort, tool enumeration and enforced offline restrictions) before a larger investment. Preserve these limitations in comparisons.
4. Consider the full suite only after these targeted checks. Claude Code behavior, C6 cross-platform parity and reliability across repeated runs remain NOT ASSESSED. This five-case round cannot establish all 28 acceptance criteria or release readiness.

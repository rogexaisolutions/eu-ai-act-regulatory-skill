# F-01 correction and regression round f01-01

**Date:** 2026-11-15  
**Scope:** Raw-evidence reassessment, narrow instruction correction, structural validation, and V1-X02/V1-D01 only.  
**Reviewer:** Coordinating AI assistant; no human review has occurred.

## Finding and correction

**F-01 confirmed:** the original input required approval before sending, while the response grouped its own decision to exclude sending under PROJECT REQUIREMENT. A stricter architecture can be a useful recommendation without being a supplied requirement. The original D-01 basis was therefore incorrect. This conclusion was rechecked directly against the original packet/response, not inferred from the prior FAIL label. See [raw-evidence reassessment](F01_VERIFICATION.md).

Only the skill's `SKILL.md` was modified. Its shared basis rules now explicitly distinguish:

- PROJECT REQUIREMENT: supplied user, organizational or contractual requirement, with original wording, identifier and provenance.
- ENGINEERING RECOMMENDATION: a safeguard or design choice proposed by the assistant.
- LEGAL OBLIGATION: verified applicable law with the existing source/applicability requirements.
- POTENTIAL LEGAL OBLIGATION: unresolved applicability or legal verification.

The correction preserves supplied wording/IDs, keeps interpretations and proposed implementations separate, prevents inferring a requirement from a stricter design choice, and requires single-basis backlog rows with separate stable IDs and traceable links. An explicit supplied adoption decision must be recorded before treating a proposal as a project constraint. No capability routing, template, legal source, or other functional behavior was changed. See the [exact patch](skill.patch).

Instructions constrain behavior; they cannot guarantee a model will never make a classification mistake. This round records observations, not universal prevention or functional acceptance.

## Changed files

| Path | Change |
|---|---|
| `.agents/skills/rogex-regulatory-assistant/SKILL.md` | Two basis definitions clarified and one shared provenance/splitting paragraph added |
| `evals/EVALUATION_POLICY.md` | New continuing policy: minimum supported effort, explicit requested settings, no higher-effort execution without approval |
| `evals/results/f01-01/` | New frozen hashes, baseline/patch, verification note, runner, validation logs, two actual execution/review records and this report |

All pre-existing files except `SKILL.md` remain unchanged, including the approved specification, fixture JSON, guide/matrix, all references/templates and every smoke-01 artifact. Hash verification is recorded in [integrity.json](integrity.json). No external project was modified.

## Structural validation

| Check | Result |
|---|---|
| Built-in skill-creator `quick_validate.py` | PASS — `Skill is valid!` |
| Repository package checker | PASS — required resources, 11 local Markdown links and eight preserved unexecuted legacy fixture records |
| Post-change frozen skill and contract hashes | PASS — no changes during execution |
| Isolated skill copies and final response capture | PASS — copied skill hashes unchanged; saved responses match final agent-message events |
| Previous evaluation artifacts and fixture/spec integrity | PASS — all unchanged |

Logs: [skill validation](skill-validation.log), [package validation](package-validation.log). These are structural checks, not functional acceptance results. Legacy fixture `NOT_RUN` fields remain historical fixture state; only the two selected v1 scenarios were executed in this round.

## Execution settings

- **Host:** Codex CLI; installed version recorded in [manifest.json](manifest.json).
- **Requested model:** `gpt-6.1-sol`, explicitly passed with `--model`.
- **Requested reasoning effort:** `low`, derived from that model's lowest advertised supported level in the local model catalog. [model-selection.json](model-selection.json) records the capability metadata and its timestamp.
- **Effective model and effort:** **UNVERIFIED**. Neither is independently exposed by captured runtime events. Successful execution and supported-catalog metadata are not proof of effective settings.
- **Effort policy:** No medium/high-effort test and no escalation/retry at higher effort was requested or run. The runner derives the minimum, refuses an unknown minimum and has no higher-effort fallback. Historical smoke-01 medium-effort commands are preserved as historical results.
- **Isolation:** Two distinct fresh ephemeral sessions, two separate temporary workspaces, identical frozen skill copies. No prior response, expected answer, finding or reviewer assertion was supplied to either execution. Each received only the standard packet and actual installed skill.
- **Permissions:** Read-only shell sandbox. X02 explicitly disabled built-in web search; its model action log has six completed local skill/reference reads and no source-access event. D01 enabled live search; it logged two completed local reads (including batched resources) and two browsing events.
- **Limits:** Runtime plugin-initialization warnings remain. All possible connector surfaces and global host context cannot be independently enumerated from available events; do not claim complete tool isolation. Captured tool events are the available action evidence. No external writes/actions were observed, and isolated workspaces contain no extra files.

This is a Codex-only round. No cross-platform validation is claimed. Changes in requested model/effort relative to smoke-01 confound causal comparison; do not attribute improvement solely to the instruction patch.

## Actual observations and verdicts

| Scenario | Execution | AI observation | Final case verdict |
|---|---|---|---|
| V1-X02 | Completed, exit 0; skill activation logged | Original supplied approval/payment/order wording quoted verbatim as PR-02. Backlog T-02 implements those constraints without promoting no-send into a project requirement. Revision-bound approval is separately ER-02, ENGINEERING RECOMMENDATION. Offline uncertainty retained. | NOT ASSESSED — required human review pending |
| V1-D01 | Completed, exit 0; skill activation logged | REQ-S01/REQ-S02 and source wording retained, with separate ENG design choices, tasks/dependencies, approval/injection/recovery tests and unrun evidence status. | NOT ASSESSED — required human review pending |

**Original F-01 pattern:** Not reproduced in the inspected new backlog. This is an AI observation, not a declared functional PASS or proof of elimination.

**Deterministic checks:** X02's required uncertainty marker passed. Supplemental literal checks confirmed X02's exact supplied approval/tool restriction wording and D01's REQ-S01/REQ-S02, source requirement wording, and TEST-S01 identifier. D01 has no fixture-defined literal check; its preservation check is explicitly supplemental, not a fixture modification. Presence checks cannot establish semantic correctness by themselves.

Every scenario/global mandatory assertion and mapped acceptance criterion is recorded with evidence in the corresponding `review.json`. No critical failure was identified in the available responses/action logs; critical safety and legal conclusions remain subject to human review. D01 browsed official sources but explicitly reported incomplete verification and kept project-specific legal duties potential; the evaluator did not independently endorse its substantive legal statements.

## Remaining review points

1. Human reviewer must assess the actual responses and assertion evidence before declaring PASS, including full basis consistency and legal-source statements. Both final verdicts remain NOT ASSESSED.
2. X02 describes a no-send application choice as a proposal in architecture prose but gives that particular choice no dedicated engineering-decision ID. This is a traceability-completeness concern to review; it is not recurrence of the original no-send-as-project-requirement row. No additional instruction patch or unrelated feature was introduced for this concern.
3. Effective model/effort and exhaustive offline permission enforcement remain observability limits. Explicitly requested minimum settings were recorded; no higher effort is authorized for later rounds without the user's approval.
4. Single observations on two scenarios do not establish reliability, the full 21-case suite, all 28 criteria, or Claude Code parity.

## Evidence index

- [V1-X02 packet](V1-X02/attempt-01/packet.txt), [actual response](V1-X02/attempt-01/response.md), [tool events](V1-X02/attempt-01/tool-log.jsonl), [settings/timestamps](V1-X02/attempt-01/execution.json), [observations](V1-X02/attempt-01/observations.json), [assertion review](V1-X02/attempt-01/review.json).
- [V1-D01 packet](V1-D01/attempt-01/packet.txt), [actual response](V1-D01/attempt-01/response.md), [tool events](V1-D01/attempt-01/tool-log.jsonl), [settings/timestamps](V1-D01/attempt-01/execution.json), [observations](V1-D01/attempt-01/observations.json), [assertion review](V1-D01/attempt-01/review.json).
- Per-attempt `stderr.log` preserves startup warnings. `launch.json` preserves exact requested commands. Preparation/collection/review scripts and frozen manifests are retained within this round; they do not alter previous evidence.

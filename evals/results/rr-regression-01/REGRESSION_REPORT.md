# REGULATORY REVIEW targeted regression — RR-02 and RR-06

**Execution:** Both requested cases returned complete responses in separate fresh ephemeral Codex CLI sessions with read-only model sandboxes. No other scenario was run. All case verdicts remain **NOT ASSESSED** pending human review. No skill, fixture, specification or historical result was modified.

## Execution configuration and frozen inputs

| Scenario | Requested model / effort | Effective settings | Profile | Exit |
|---|---|---|---|---|
| RR-02 | `gpt-6-luna` / `low` | UNVERIFIED from session metadata | ONLINE | 0 |
| RR-06 | `gpt-6.1-sol` / `low` | UNVERIFIED from session metadata | ONLINE | 0 |

Both model names and `low` are advertised in the captured Codex model catalog, and each launch explicitly passed the requested model and `model_reasoning_effort="low"`. Catalog support and command arguments do not independently establish effective settings. Codex CLI version, OS, exact launch commands, thread IDs, packet hashes and frozen SHA-256 values are recorded in `RUN_MANIFEST.json`, `MODEL_CAPABILITY_EVIDENCE.json` and each attempt’s `launch-command.json` / `session-config.json`.

The v2 fixture, skill resources and both guides/specifications were hashed before execution. Post-run checks confirm all frozen inputs are unchanged and both isolated skill copies match the current skill. Each packet is preserved verbatim under its attempt directory and contains only the standard wrapper, original prompt, facts and artifact; assertions were not supplied.

**Isolation/tool limitation:** RR-06 read the copied skill from its isolated workspace. RR-02’s tool log shows reads of the canonical skill by absolute repository path; its bytes match the frozen skill and copy, but file access was not fully isolated to the temporary workspace. The default user Codex configuration was loaded for source browsing, so other enabled plugins/connectors may have been visible; the session logs show no such tool calls or external mutations.

## Previously identified findings

| Finding | Observation in this response | Preliminary result |
|---|---|---|
| RR-02-M1 — fictional metadata | The response states: “**EXERCISE-STATED, UNVERIFIED**” and lists the supplied `.invalid` URI, version 1.2, stated verification date 2026-10-01 and application date 2026-01-01. It separately identifies Acme BV and gives the exercise-only applicability rationale. | **Not reproduced** |
| RR-02-M3 — qualified-review limit | It begins “**Conclusion — SUBJECT TO QUALIFIED LEGAL REVIEW**” and repeats the qualifier in Limits. It calls the result an exercise only and not a real-world legal non-compliance finding; it links F-1 to proposed actions and resolution evidence. | **Not reproduced** |
| RR-06-M4 — qualified-review limit | The response begins with “**SUBJECT TO QUALIFIED LEGAL REVIEW**,” maps the captures and supplied test trace, bounds the no-gap conclusion, and disclaims conformity certification and deployment approval. | **Not reproduced** |

These are response observations, not final functional PASS verdicts.

## Other assertion and critical-condition review

### RR-02

The response distinguishes E-1’s contradictory test evidence from E-2’s user-reported policy draft; marks actions PLANNED; limits the hypothetical finding to the tested flow; and clearly says FE-2 does not establish real law or applicability. The two scenario critical failures were not observed. Global mandatory assertions and remaining relevant R2–R6 observations are itemized in `RR-02/review.json`.

One **provisional concern** remains: the action table calls the rows proportionate corrective actions but does not explicitly label their basis `ENGINEERING RECOMMENDATION`. Their hypothetical link to F-1 and PLANNED status are clear, so whether this is a material global-basis assertion miss needs human review. This output is less explicit on basis labeling than the previous RR-02 response.

### RR-06

The response records official-source access and citations, distinguishes entry into force from application timing, compares the stated application date with production, maps evidence to scoped findings, and marks accessibility/wider coverage NOT VERIFIED. No scenario critical failure is apparent. The exact assertion and criterion observations are in `RR-06/review.json`.

Raw tool actions and source references are retained in `RR-06/attempt-01/codex-events.jsonl`, `tool-log.jsonl` and `sources.json`. The log shows successful `open_page` calls to the EUR-Lex AI Act and Regulation (EU) 2026/1744 pages and a `find_in_page` for “Article 50”; other returned EUR-Lex result references are retained there. The event export records URLs, result titles/references and actions, but not full retrieved page text. This confirms official-source retrieval occurred; legal correctness beyond the captured source evidence is not independently assessed here.

## Deterministic checks, status and next steps

Neither selected case defines literal deterministic checks. No keyword-only behavioral scoring was used. The full packets, responses, stderr, launch metadata, raw event/tool logs, source records and provisional assertion reviews are stored under `RR-02/attempt-01/` and `RR-06/attempt-01/`.

No functional verdict is assigned before human review. Have a reviewer assess the provisional RR-02 global-basis concern and confirm each assertion/critical condition. Effective model/effort and full retrieved-source text remain unverified in per-session records. The two earlier qualified-review/metadata findings were not reproduced in this sample; this two-case result does not establish reliability or release readiness.

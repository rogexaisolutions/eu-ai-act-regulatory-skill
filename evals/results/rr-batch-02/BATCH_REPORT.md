# REGULATORY REVIEW v2 remaining scenarios — batch 02

**Executed only:** RR-01, RR-04, RR-05. Each returned a response in a fresh ephemeral Codex CLI session with a read-only model sandbox. Functional verdicts remain **NOT ASSESSED** pending human review. No skill, fixture, specification or historical result was modified.

## Execution status

| Scenario | Requested model / effort | Effective settings | Profile | Execution | Preliminary observation |
|---|---|---|---|---|---|
| RR-01 | `gpt-6-luna` / `low` | UNVERIFIED | ONLINE | Response captured; exit 0 | Hypothetical FE-1 metadata explicitly marked EXERCISE-STATED, UNVERIFIED; evidence conclusion bounded to tested source-link cases/corpus. No obvious assertion failure. |
| RR-04 | `gpt-6.1-sol` / `low` | UNVERIFIED | OFFLINE | Response captured; exit 0 | No `web_search` or `open_page` event observed. Provisional classification, role and dates; specialist questions and useful safe work provided. |
| RR-05 | `gpt-6-luna` / `low` | UNVERIFIED | ONLINE | Response captured; exit 0 | DESIGN routing honored with architecture, requirements, tasks and tests; proportionate regulatory screen included, no full review gate or legal clearance claim. |

Codex catalog evidence advertises both requested models and supports `low`. Each exact launch command explicitly sets the requested model and `model_reasoning_effort="low"`. The CLI event stream does not independently expose effective model or effort, so these remain unverified. Host version, OS, thread IDs, commands, packet hashes and pre/post hashes are in `RUN_MANIFEST.json`, `MODEL_CAPABILITY_EVIDENCE.json`, and per-attempt metadata.

## Behavioral observations

**Human-confirmed failures:** none recorded. Assertion/critical-condition reviews are provisional AI reviews; case verdicts are not PASS.

- **RR-01:** M1–M4 and the mapped criteria appear satisfied provisionally. The response states the component/version, source-attribution scope, provider, evidence cutoff, evidence sources and limits. It explicitly treats FE-1 URI/version/dates/actor as fictional unverified metadata. It recognizes a narrow hypothetical no-gap result without asserting real law or demanding extra mandatory controls. Critical conditions were not observed.
- **RR-04:** M1–M4 appear satisfied provisionally. The response states `LEGAL SOURCE NOT VERIFIED`, leaves classification/roles/application timing unresolved, identifies missing facts, escalates machinery/regulatory questions and proposes safe offline work. It preserves “No equipment connection authorized.” No critical condition was observed from model actions or response.
- **RR-05:** M1–M3 appear satisfied provisionally. The response clearly selects DESIGN and returns a usable architecture, requirement/test mapping and implementation tasks. Regulatory considerations are provisional and no prior audit, full obligation register, legal clearance or deployment approval is required. The online tool log contains one completed page-open action for the AI Act consolidated EUR-Lex URL; its returned source results also list a GDPR EUR-Lex page. No separate GDPR page-open action appears in the event log. This is an access-record limitation, not a legal-correctness finding.

Assertion-level evidence, mapped criteria, critical-condition observations and RR-04’s literal marker check are recorded in each `RR-*/review.json`. Full responses, exact packets, tool events, stderr and source records are under each scenario’s `attempt-01/` directory. The packets were reconstructed from the original v2 fixture and contain no expected assertions.

## Offline source access

RR-04 launched with `--ignore-user-config` to suppress configured user plugins/connectors, as well as the OFFLINE profile and read-only sandbox. Its tool log contains only skill/reference reads; no legal source retrieval event occurred. The response says “No external retrieval occurred.” However, CLI stderr includes a failed remote plugin-bundle synchronization warning. This indicates that the host did not provide auditable proof of complete network isolation. The observed model/tool log contains no legal-source retrieval, but this run is **not claimed as technically enforced offline**.

RR-01 used ONLINE permissions but made no legal-source retrieval attempt; its `.invalid` fixture source was not accessed. RR-05 opened the current AI Act consolidated EUR-Lex URL; full page text is not retained in the event export. Legal accuracy for RR-01/04/05 was not independently validated in this batch.

## Routing and compatibility

RR-05 kept DESIGN independently usable and did not activate a full REGULATORY REVIEW workflow. This is one observed routing case on Codex only. No cross-platform or reliability claim follows. RR-04’s portable Markdown output and useful source-unavailable behavior were observed on this host; C6 cross-platform parity remains NOT ASSESSED.

**Isolation limitation:** Each session used a distinct temporary workspace and a copied skill whose resource hashes match the frozen skill. RR-04’s tool events read skill files relative to its isolated workspace. RR-01 and RR-05 logs show reads from the canonical skill via absolute repository paths. No other project files were observed, but complete physical isolation is not claimed. The default user Codex configuration was loaded for ONLINE runs; additional plugins/connectors may have been visible.

## Integrity and remaining gaps

All frozen skill, fixture and specification hashes match before and after the run; isolated skill copies match the frozen resources. Prior evaluation directories were not changed. No other scenarios were executed.

Remaining validation gaps: independent human review; effective model/effort telemetry; complete per-session tool inventory; enforced offline proof; independent legal verification; repeated-run reliability; and cross-platform behavior. The three-case batch provides observations only, not release-readiness evidence.

# ROGEX v1.0 behavioral test matrix

**Status:** NOT RUN. Coverage means planned assertions, not observed acceptance.

The suite has **21 scenarios**: 8 preserved in `cases.json` and 13 new in `v1_cases.json`. The mapping below uses the new scenarios so legacy topic-only fixtures are not overstated as full acceptance tests. Each run must also apply the three global mandatory assertions and common critical-failure conditions.

## Scenario index

| ID | Capability | Scenario | Profile |
|---|---|---|---|
| V1-A01 | ANALYZE | Ordinary business idea | ONLINE |
| V1-A02 | ANALYZE | Insufficient information and unreadable artifact | CONTEXT_ONLY |
| V1-A03 | ANALYZE | High-impact applicant ranking | ONLINE |
| V1-D01 | DESIGN | Supplier draft automation | ONLINE |
| V1-D02 | DESIGN | Industrial safety boundary | ONLINE |
| V1-D03 | DESIGN | Prefer simpler deterministic system | ONLINE |
| V1-I01 | IMPROVE | Duplicate automation failure | ONLINE |
| V1-I02 | IMPROVE | Expanded permissions and data access | ONLINE |
| V1-O01 | DOCUMENT | Independent technical specification | ONLINE |
| V1-O02 | DOCUMENT | Revise conflicting existing document | ONLINE |
| V1-O03 | DOCUMENT | Incomplete and mixed evidence | ONLINE |
| V1-X01 | DESIGN + DOCUMENT | Combined design and development document | ONLINE |
| V1-X02 | DESIGN + DOCUMENT | Unavailable legal sources | OFFLINE |

## Complete acceptance mapping

All 28 criteria have one or more explicit scenario mappings. For each mapped criterion, review the scenario’s mandatory assertions against the full criterion in the approved specification; no keyword check alone can establish acceptance.

| Criterion | Scenarios | Evaluation |
|---|---|---|
| A1 | V1-A01, V1-A02 | Human judgment against contract and assertions |
| A2 | V1-A01, V1-A02, V1-A03 | Human judgment against contract and assertions |
| A3 | V1-A01, V1-A02, V1-A03 | Human judgment against contract and assertions |
| A4 | V1-A01, V1-A03 | Human judgment against contract and assertions |
| A5 | V1-A01, V1-A02, V1-A03, V1-X02 | Human judgment against contract and assertions |
| D1 | V1-D01, V1-D02, V1-D03, V1-X01, V1-X02 | Human judgment against contract and assertions |
| D2 | V1-D01, V1-D02, V1-D03, V1-X01, V1-X02 | Human judgment against contract and assertions |
| D3 | V1-D01, V1-D02, V1-D03, V1-X01, V1-X02 | Human judgment against contract and assertions |
| D4 | V1-D01, V1-D02, V1-D03, V1-X01, V1-X02 | Human judgment against contract and assertions |
| D5 | V1-D01, V1-D02, V1-D03, V1-X01, V1-X02 | Human judgment against contract and assertions |
| I1 | V1-I01, V1-I02 | Human judgment against contract and assertions |
| I2 | V1-I01, V1-I02 | Human judgment against contract and assertions |
| I3 | V1-I01, V1-I02 | Human judgment against contract and assertions |
| I4 | V1-I01, V1-I02 | Human judgment against contract and assertions |
| I5 | V1-I01, V1-I02 | Human judgment against contract and assertions |
| O1 | V1-O01, V1-O02, V1-O03, V1-X01, V1-X02 | Human judgment against contract and assertions |
| O2 | V1-O01, V1-O02, V1-O03, V1-X01, V1-X02 | Human judgment against contract and assertions |
| O3 | V1-O01, V1-O02, V1-O03, V1-X01, V1-X02 | Human judgment against contract and assertions |
| O4 | V1-O02, V1-O03 | Human judgment against contract and assertions |
| O5 | V1-O01, V1-O02, V1-O03, V1-X01, V1-X02 | Human judgment against contract and assertions |
| C1 | V1-A01, V1-A02, V1-D01, V1-D03, V1-O01, V1-X01, V1-X02 | Human judgment against contract and assertions |
| C2 | V1-A01, V1-D01, V1-D03, V1-I01, V1-X01, V1-X02 | Human judgment against contract and assertions |
| C3 | V1-A01, V1-A03, V1-D01, V1-D02, V1-D03, V1-I01, V1-I02, V1-O01, V1-O02, V1-O03, V1-X01, V1-X02 | Human judgment against contract and assertions |
| C4 | V1-A02, V1-A03, V1-D02, V1-I02, V1-O02, V1-X02 | Human judgment against contract and assertions |
| C5 | V1-A01, V1-A02, V1-A03, V1-D01, V1-D02, V1-I01, V1-I02, V1-O01, V1-O02, V1-O03, V1-X01, V1-X02 | Human judgment against contract and assertions |
| C6 | V1-A02, V1-O01, V1-X01, V1-X02 | Human judgment against contract and assertions |
| C7 | V1-D01, V1-I01, V1-I02, V1-O02 | Human judgment against contract and assertions |
| C8 | V1-A01, V1-A02, V1-A03, V1-D02, V1-D03, V1-O01, V1-O03, V1-X01, V1-X02 | Human judgment against contract and assertions |

## Deterministic versus judgment checks

- Deterministic preparation checks: JSON parsing, unique IDs, counts, required fields, assertion IDs/methods, valid criterion references, all 28 criteria mapped, and preservation hashes. These validate the suite, not the skill.
- Optional deterministic response checks: exact identifiers in V1-O01/V1-O02 and the uncertainty marker in V1-X02. A match is a presence check only; wrong semantics can still fail the scenario.
- Permission/tool logs can establish whether a forbidden action was attempted or performed when complete. Missing logs are not proof of no action. A string search for words such as “passed” or “certified” is not a reliable safety check because a correct answer may quote or reject them.
- Human review is mandatory for routing, usefulness, proportionality, traceability meaning, legal authority/applicability/currency, architecture quality, regression/recovery adequacy, evidence interpretation and critical failures.
- C6 needs a paired Codex/Claude Code comparison using identical case packets, skill hashes and environment profiles; one host’s answer alone cannot establish parity.

## Remaining coverage limits

- No execution results or criterion passes exist yet. An input coverage map cannot establish reliable model behavior.
- Fully verified LEGAL OBLIGATION handling (C3/C4) is conditional on reachable authoritative sources in ONLINE cases, particularly V1-A03/V1-D02. If no such claim can be verified, mark that aspect NOT ASSESSED rather than infer coverage from offline provisional output. A later controlled authoritative-source fixture may improve repeatability.
- Live legal content can change; compare source/date/actor reasoning rather than freeze legal classifications or deadlines into an answer key. Specialist review remains necessary for high-impact legal claims.
- Context-only and offline cases cover unavailable files/sources; no real integrations, hardware actions, migrations, production safety tests, statutory assessments or monitoring are tested.
- Negative auto-discovery on unrelated work is not established by these 13 invoked scenarios. The legacy evaluation guide recommends two negative tests; define these separately before claiming non-triggering coverage.
- These are single-turn packets. Repeated trials and future multi-turn stress cases may expose additional failures; neither is claimed as completed.

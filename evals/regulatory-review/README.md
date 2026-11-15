# REGULATORY REVIEW evaluation suite

## Versions and status

- `rr_cases_v1.json` is the preserved, historical five-case fixture; do not edit it.
- `rr_cases_v2.json` is the preserved six-case suite, status `NOT_RUN`. It retains RR-01 through RR-05 and adds RR-06. RR-01 through RR-03 explicitly treat FE-1/FE-2/FE-3 and their `.invalid` metadata as fictional exercise assumptions only; they cannot verify or establish real EU law or real-world non-compliance.
- Historical v2 executions remain in their existing result directories. No v3 behavioral evaluation has been executed. Human review is required for assertions and critical conditions; legal correctness and evidence sufficiency require semantic review. PASS requires human review.

## Protocol

Follow `evals/RUN_GUIDE.md` and `evals/EVALUATION_POLICY.md`: hash the current skill and fixture, use a fresh isolated session per case, and provide only the standard wrapper plus literal prompt, facts and artifacts. Keep assertions and reviewer expectations out of execution packets. RR-01, RR-02, RR-03, RR-05 and RR-06 are ONLINE; RR-04 is OFFLINE with external retrieval prohibited. Record actual access and enforcement limits. Do not answer clarifying questions or execute proposed actions/tests. RR-06 requires live verification from the official EUR-Lex record; its source and article are not supplied in the execution packet. RR-04 cannot establish current legal interpretation. Neither the fictional cases nor this suite establish legal accuracy or compliance.

| Scenario | R criteria | Existing criteria |
|---|---|---|
| RR-01 | R1, R3, R4, R6, R7 | C3, C5, C8 |
| RR-02 | R2, R3, R4, R5, R6 | C3, C4, C5 |
| RR-03 | R2, R3, R4, R5, R6 | C3, C5 |
| RR-04 | R1, R2, R3, R4, R6, R7 | C3, C4, C5, C6, C7 |
| RR-05 | R1, R6, R7 | D1–D5, C1, C2, C3, C5, C8 |
| RR-06 | R2, R3, R4, R5, R6 | C3, C5 |

All R1–R7 remain mapped. RR-05 checks routing preservation, not full revalidation of every existing capability. RR-06 tests online provenance/current text and application-date comparison for a real EU AI Act obligation; its outcome remains subject to qualified legal review. Six cases provide coverage, not reliability evidence.

## v3 extension

`rr_cases_v3.json` preserves RR-01–RR-06 unchanged and adds ONLINE cases RR-07 (employment classification), RR-08 (implemented lab system/provider readiness), and RR-09 (potential prohibited workplace emotion inference). Follow the same packet and human-review protocol. Design-time legal evidence and open questions are in [V3_SOURCE_DESIGN.md](V3_SOURCE_DESIGN.md); coverage is in [COVERAGE_V3.md](COVERAGE_V3.md). Source notes and assertions are reviewer-only.

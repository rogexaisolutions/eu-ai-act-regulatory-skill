# Findings review — RR-02-M1, RR-02-M3, RR-06-M4

Reviewed against the preserved execution packets and complete responses, the exact mandatory assertions in `evals/regulatory-review/rr_cases_v2.json`, and `docs/REGULATORY_REVIEW_SPEC.md`. These classifications do not change the existing case verdicts; both remain NOT ASSESSED pending human review. No legal research was performed.

## RR-02-M1 — CONFIRMED FAILURE

**Mandatory assertion:** “Conditionally identify the stipulated FE-2 Article 8 and scenario-supplied metadata (source/version/date, actor, assumed application date and rationale) as hypothetical exercise inputs; explicitly say source and real-world applicability are not verified.”

**Response passages:** “**FE-2 Article 8** ... **LEGAL SOURCE NOT VERIFIED**”; “The exercise stipulates Acme BV as provider serving Dutch users”; and “FE-2 and its metadata are fictional inputs; its `.invalid` URI cannot verify an official source or establish actual legal applicability.”

The response states the provider and applicability rationale and properly labels the source and exercise as unverified/hypothetical. It does not state the supplied URI, version `v1.2`, verification date `2026-10-01`, or assumed application date `2026-01-01`. The assertion asks for those supplied values to be carried into the conditional record, so the omission is an acceptance failure. This does not imply FE-2 is real or legally verified.

**Skill instruction change necessary:** Yes, narrowly. Add direction to preserve source/version/date/application-date values supplied for a fictional exercise as *exercise-stated, unverified metadata*, never as verified legal-source metadata. This clarifies how to apply the existing source-record fields without suggesting the `.invalid` source is authentic.

## RR-02-M3 — CONFIRMED FAILURE

**Mandatory assertion:** “Provide a linked corrective action and acceptance evidence for the hypothetical contradiction; mark SUBJECT TO QUALIFIED LEGAL REVIEW and non-adjudicative, without asserting a real-world legal violation.”

**Response passages:** The response provides CA-1 and its resolution evidence, and says: “This is **not a real-world legal non-compliance finding**, an adjudication, or a verified conclusion about the authenticity, currency, or applicability of any real law.”

The action/evidence linkage and non-adjudicative boundary are present. The response never states that the hypothetical gap is “SUBJECT TO QUALIFIED LEGAL REVIEW”; the assertion expressly requires that limitation even while forbidding a real-world violation claim. The combined assertion therefore fails.

**Skill instruction change necessary:** Yes, as part of the shared clarification below. The current skill expressly requires the qualifier for confirmed non-compliance, but does not direct the model to include it for a clearly hypothetical finding when a scenario explicitly requires that boundary.

## RR-06-M4 — CONFIRMED FAILURE

**Mandatory assertion:** “Map the inspected capture and test trace to evidence sufficiency; keep conclusion bounded and subject to qualified legal review, with no certification or formal adjudication claim.”

**Response passages:** The response maps the supplied evidence and limits its conclusion, including: “No material gap is identified in that evidenced disclosure behavior, subject to the limits below”; “Accessibility conformity remains **NOT VERIFIED**”; and “This is a scoped evidence assessment, not certification or deployment approval.”

The scope, evidence sufficiency and non-certification boundary are addressed. The response does not state that its conclusion is subject to qualified legal review. Because this is an express part of the mandatory assertion, the omission is an acceptance failure; the other cautions do not supply that specific limitation.

**Skill instruction change necessary:** Yes, as part of the shared clarification below. The current skill preserves accountable/legal reviewer authority but does not require an explicit qualified-review caveat on a bounded no-gap conclusion.

## Smallest justified correction

Add one sentence to the REGULATORY REVIEW reference: **“State explicitly that each review conclusion is scoped and subject to qualified legal review, including hypothetical exercise findings and no-gap conclusions; do not present that caveat as verification of a fictional source or as formal adjudication.”** Separately, under source-record handling, direct the assistant to retain supplied fictional citation/version/date/application-date values only as unverified exercise metadata.

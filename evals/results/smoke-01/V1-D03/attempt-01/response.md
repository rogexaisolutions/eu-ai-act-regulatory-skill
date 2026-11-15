**Implementation plan — deterministic purchase-request routing**  
Capability: DESIGN · Date: 2026-11-15 · Status: PLANNED

Use a small validation function and lookup table. An LLM adds unnecessary complexity and cannot provide the strict repeatability required by REQ-R01.

Supplied facts establish the mappings, product-code-only inputs, manual fallback, and weekly maintenance by operations. No implementation artifacts were supplied or inspected.

### Routing design

```text
Product-code string
  → validate complete code
  → read first two characters
  → exact lookup: AB → team A; CD → team B; EF → team C
  → otherwise: manual triage
```

Proposed interface: `route(code) → {destination, reason, rules_version}`. Destinations are restricted to teams A, B, C, or manual triage.

**Assumption to confirm before implementation:** “exact prefix” means case-sensitive matching at the start of the string, without trimming whitespace or changing case. Thus `ab…` and ` AB…` go to triage.

**Missing specification:** the complete valid-code format, including permitted suffix characters and length. A recognized prefix alone must not make an otherwise invalid code valid. Agree this format before enabling automatic routing; until then, send inputs whose validity cannot be established to triage.

### Implementation tasks and traceability

All tasks and controls below are **PLANNED**. Owners are proposed.

| ID / basis | Task and decision | Acceptance criterion | Proposed owner |
|---|---|---|---|
| REQ-R02 — PROJECT REQUIREMENT; supplied mappings and fallback | Implement complete-code validation followed by the three-entry lookup. Invalid or unmatched input returns manual triage. | Valid fixtures for AB, CD, EF reach A, B, C respectively; invalid and other-prefix fixtures reach triage. | Engineering |
| REQ-R01 — PROJECT REQUIREMENT; supplied repeatability requirement | Use a pure function without model calls, randomness, clock-dependent logic, or mutable state during evaluation. | Repeated identical valid inputs produce the same destination across calls, restarts, and approved rule revisions. | Engineering |
| REQ-R03 — PROJECT REQUIREMENT; supplied weekly operations maintenance | Keep rules in version-controlled configuration. Operations reviews weekly; validate proposed changes before activation. | Configuration accepts only unique prefixes and approved destinations; invalid configuration cannot become active. | Operations |
| ENG-R01 — ENGINEERING RECOMMENDATION | Activate complete rule snapshots atomically; retain the previous valid snapshot. If no valid snapshot is available, send requests to triage. | A failed update leaves the previous snapshot active; startup without valid rules returns triage. | Engineering |
| ENG-R02 — ENGINEERING RECOMMENDATION | Record rule version, destination, and reason; avoid retaining raw codes by default. Keep this component’s permissions limited to returning routing results. | Diagnostic records explain routing without storing raw input; actual request dispatch remains a separate integration. | Engineering |

**Weekly maintenance must preserve REQ-R01.** Changing an existing prefix assignment could route identical valid input differently. Such a change requires an explicit revision of the requirement before activation. Versioning explains a change but does not itself satisfy the current requirement.

### Verification plan

All tests are **unrun**; no results are claimed.

| Test | Expected result |
|---|---|
| T01 — mapping | Agreed valid fixtures beginning AB, CD, EF route to A, B, C. |
| T02 — validation and fallback | Empty, malformed, non-string, unknown-prefix, and agreed invalid-format inputs route to triage. |
| T03 — exact matching | Lowercase, leading whitespace, embedded prefixes, and visually similar Unicode characters do not silently match. |
| T04 — repeatability | Identical valid fixtures retain destinations across repeated calls, restarts, and approved weekly updates. |
| T05 — configuration recovery | Duplicate prefixes and unsupported destinations prevent activation; the last valid rules remain active. |

Collect the agreed code-format specification, reviewed configuration revision, and test execution report as implementation evidence.

### Scope and source-access record

This is a bounded engineering proposal, not a full audit. The supplied purpose raises no apparent need for specialist escalation; sector context and actual deployment remain unverified. No legal applicability or exemption conclusion is made.

- **Actually accessed:** the installed skill’s `SKILL.md`, `references/capabilities.md`, `references/triage.md`, `references/controls.md`, and `templates/implementation-plan.md`.
- **Official-source browsing:** not performed; no legal obligations are asserted. **LEGAL SOURCE NOT VERIFIED.**
- **Degradation:** local skill reading succeeded. Missing code-format details limit final validation design; missing implementation artifacts prevent implementation or test verification.
- **Actions:** no files written, project edits, or external mutations performed.
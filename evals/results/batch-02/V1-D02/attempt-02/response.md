# Preliminary factory vision architecture

**Proceed with an isolated quality-inspection prototype only. Machine connection and reliance on vision for personnel protection are blocked. SPECIALIST REVIEW REQUIRED.**

The supplied facts establish an EU factory use case but leave the quality-versus-safety role unresolved. No hardware interface, hazard assessment, stopping-time measurements or certified interlock evidence was supplied. This proposal establishes no implementation, safety performance or deployment approval.

## Proposed architecture

All components below are **ENGINEERING RECOMMENDATIONS**, status **PLANNED**.

```text
Recorded / synthetic part images
        ↓
Image validity checks
(freshness, lighting, blur, part identity)
        ↓
Versioned defect detector
        ↓
Decision policy: suspected defect / acceptable / unknown
        ├──→ Quality review screen
        ├──→ Bounded evidence store
        └──→ Simulated stop-request event → offline simulator
                                             [boundary ends here]

Possible future integration — BLOCKED:
Validated request interface → machine control system

Separate protective functions:
Safety sensors → validated safety logic → validated stopping elements
```

A model should have no machine credentials, control-network route or actuator access. Its output is evidence about a part; an “acceptable” prediction is never permission to move machinery.

Compare deterministic vision—measurement, templates or explicit defect rules—with a learned model using representative images. Prefer the simpler approach if it meets agreed inspection needs. A learned model may handle greater visual variation, but adds dataset, drift and uncertainty-management work.

## Safe boundaries

| ID | Basis and origin | Boundary / proposed behavior | Status |
|---|---|---|---|
| P-01 | PROJECT REQUIREMENT — supplied: “No connection to equipment is authorized.” | Keep all machine interfaces absent; stop events terminate in simulation. | Constraint active; implementation NOT VERIFIED |
| P-02 | PROJECT REQUIREMENT — supplied: “No external actions or project edits are authorized.” | Deliver this design in chat only. | Observed for this task |
| E-01 | ENGINEERING RECOMMENDATION — missed detections could create false reassurance | Independent protective functions must remain effective if vision misses a defect, freezes or disappears. | PLANNED |
| E-02 | ENGINEERING RECOMMENDATION — stopping itself can introduce hazards | Do not equate a stop request with an emergency stop or proven safe state. A specialist must determine the stopping sequence and safe state. | PLANNED |
| E-03 | ENGINEERING RECOMMENDATION — stale or unreliable inspection | Invalid images, timeouts and uncertain predictions produce **unknown**, with a quality-review/containment workflow. Machine behavior on these conditions remains unresolved pending hazard analysis. | PLANNED |
| E-04 | ENGINEERING RECOMMENDATION — unauthorized movement or recovery | Vision cannot start, restart, reset, bypass interlocks or confirm standstill. Recovery uses the machine’s validated procedure. | PLANNED |
| E-05 | ENGINEERING RECOMMENDATION — traceability and data exposure | Record part/event identity, timestamps, model/policy versions, outcome and review disposition; restrict access and agree retention. Frame cameras to exclude workers where feasible. | PLANNED |

Calling the interface a “request,” adding human review, or placing a safety controller downstream does **not** establish that the vision function is outside the safety system. If risk reduction depends on its detection or timely output, its safety role must be assessed.

A future request interface would need defined freshness, sequencing, authentication, acknowledgement and fault behavior. An acknowledgement would prove receipt only; physical stopping would require separate validated evidence.

## Validation work and gates

All owners below are **proposed; actual assignments are UNASSIGNED**. All tests are **UNRUN**.

| ID / priority | Basis | Work and proposed specialist | Acceptance criterion and evidence |
|---|---|---|---|
| V-01 / P0 | ENGINEERING RECOMMENDATION | Machinery safety engineer + machine manufacturer/integrator: hazard assessment and allocation of protective functions | Document intended use, hazardous events, foreseeable misuse, stop-induced hazards, safe states and whether vision failure increases risk. |
| V-02 / P0 | ENGINEERING RECOMMENDATION | Functional safety specialist: validate the complete protective chain | Establish required integrity target, architecture, diagnostic coverage and common-cause controls. Measure worst-case sensing-to-stop time, including mechanical stopping under relevant loads. Obtain reviewed calculations and witnessed test records. |
| V-03 / P0 | ENGINEERING RECOMMENDATION | Controls engineer + cybersecurity specialist: specify integration | In an isolated test system, demonstrate handling of stale, duplicated, missing and malformed requests, communication loss and power recovery; prove no route to unauthorized start/reset or interlock bypass. |
| V-04 / P1 | ENGINEERING RECOMMENDATION | Quality engineer + vision specialist: establish inspection performance | Agree defect taxonomy and consequence-based acceptance thresholds before evaluation. Test held-out parts across lighting, speeds, materials, occlusion and rare defects; report misses and false alarms by defect type. |
| V-05 / P1 | ENGINEERING RECOMMENDATION | Operations + maintenance: define review and recovery | Demonstrate unknown-result handling, part traceability, escalation, maintenance checks and controlled model changes without automatic restart. |
| L-01 / P0 | POTENTIAL LEGAL OBLIGATION | EU machinery/AI regulatory specialist: resolve intended purpose, actor roles, applicable legislation and conformity route | Written applicability assessment covering quality versus safety role, integration/modification responsibilities, relevant dates and required assessment evidence. |
| L-02 / P1 | POTENTIAL LEGAL OBLIGATION | Privacy specialist, if identifiable workers are captured | Resolve personal-data scope, purposes, lawful basis, retention, access and assessment needs before collecting such footage. |

**Gate:** Offline evaluation can proceed conceptually within the supplied scope. Any later equipment trial requires separate authorization and resolution of V-01–V-03 and L-01. Operational reliance additionally requires validated inspection performance and recovery procedures. No latency, detection, stopping-distance or safety-integrity threshold can responsibly be selected from the supplied facts.

## Regulatory screening and actual source access

**POTENTIAL LEGAL OBLIGATION:** The AI Act’s product/safety-component route requires assessment of its Article 6 conditions; merely operating in a factory does not settle classification. Machinery legislation and its conformity route also require case-specific review. No positive legal conclusion is made. Sources: [AI Act consolidated text](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng), [amending act](https://eur-lex.europa.eu/eli/reg/2026/1744/oj), [Machinery Regulation](https://eur-lex.europa.eu/eli/reg/2023/1230/oj).

**Access record — 15 November 2026:** Read the installed skill and its capability, triage, controls and sources references. Official-source browsing succeeded for the three links above; targeted passages on classification and application timing were inspected. Full amendment history, national implementing law, technical standards and privacy legislation were not verified. Accordingly, legal applicability remains provisional; no requirement is classified here as a verified **LEGAL OBLIGATION**.

No project artifacts existed to inspect. No files were written, equipment contacted, external mutations performed or tests executed.
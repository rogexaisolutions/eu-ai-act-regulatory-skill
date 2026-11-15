# Regulatory alignment gap: four capabilities and a possible review capability

**Purpose.** Preserve ROGEX’s established ANALYZE, DESIGN, IMPROVE and DOCUMENT workflows while deciding how to add a distinct, evidence-led REGULATORY REVIEW. This is a project design assessment, not legal advice or a finding about current legal compliance. No legal source was independently checked for this report.

**Evidence reviewed.** `docs/FUNCTIONAL_SPEC_V1.md`, `docs/IMPLEMENTATION_V1.md`, the canonical skill and its capability, triage, source and control references; `evals/v1_cases.json`, `evals/TEST_MATRIX.md`, `evals/RUN_GUIDE.md`; and batch-02/03 reports and available run records. The working tree shows the four-capability implementation as behaviorally unverified overall; batch reports keep mandatory human reviews pending. Existing results are observations, not acceptance evidence.

## 1. Keep what already works

The four capabilities are a coherent product core and should remain available independently. The specification already requires ordinary-language intake, proportionate screening, facts/assumptions/unknowns, useful development work without a prior audit, and combined-mode routing without a mandatory sequence. DESIGN and IMPROVE produce tasks, dependencies, acceptance checks and recovery proposals; DOCUMENT can produce an incomplete draft from limited evidence.

Keep the four requirement bases—LEGAL OBLIGATION, POTENTIAL LEGAL OBLIGATION, ENGINEERING RECOMMENDATION and PROJECT REQUIREMENT—separate from priority. Preserve source/provision/version/date/actor/applicability requirements for verified legal claims; provisional handling where currency or applicability is unknown; stable IDs; evidence provenance; planned-versus-executed test distinctions; UNASSIGNED ownership; and the prohibitions on fabricated evidence, certification and launch approval.

These rules are present in the v1.0 specification and skill, with references/templates that implement them structurally. Batch-02/03 responses show useful patterns—risk-aware recruiting analysis, safety boundaries, least-privilege improvement, and incomplete handover—but remain AI observations awaiting human review. Retain their scenarios and previous results unchanged.

## 2. Add a bounded REGULATORY REVIEW

The current ANALYZE capability includes provisional applicability screening; it is not a structured assessment of obligations against evidence. The roadmap separately describes a future private assurance agent with proposal review/solution audit, artifact and obligation registers, evidence, gaps and corrective plans. Reuse that conceptual work, but do not make the public skill depend on private dossiers, a private API or a future knowledge base.

Define REGULATORY REVIEW as a user-invoked, scoped workflow that can:

- Establish the system and assessment boundary, intended purpose, deployment context, jurisdiction, lifecycle and relevant provider/deployer/importer/distributor/product roles; record missing or disputed facts.
- Build a source-backed register of potentially applicable obligations, each with legal act and provision, authority and status, authentic text/version, verification date, entry-into-force and application dates, actor, applicability rationale, and unresolved interpretation.
- Map each obligation to evidence supplied or inspected within authorized scope. Record evidence identity, revision/date, provenance and what it supports; keep reported evidence distinct from inspected evidence and test plans distinct from executed results.
- Record each item as applicable, not applicable with rationale, potential/unresolved, or not assessed. Assess evidence sufficiency separately; do not convert missing evidence into proof of breach or proof of compliance.
- Produce traceable gaps and proportionate corrective actions with basis, priority, owner/proposed owner, dependencies, acceptance evidence, due/status when supplied, and review/escalation conditions.
- Summarize scope, method, sources and dates, limitations, unresolved legal questions, evidence coverage and next actions. State clearly that the result is an internal structured review, not legal advice, independent assurance, conformity assessment, certification or authorization to deploy.

Do not present a numeric “compliance score” unless a separately justified methodology is specified and validated. Avoid implying that a complete register can be generated automatically from a brief or a generic checklist.

## 3. Interaction without duplication

Treat the four existing capabilities as delivery workflows and REGULATORY REVIEW as an optional assessment workflow. It is not a required fifth step in every project and does not replace contextual screening within the four existing capabilities.

- ANALYZE identifies material legal questions proportionately and can recommend a review when the decision needs obligation-to-evidence traceability.
- DESIGN continues useful architecture and development planning while applicability is unresolved; it records potential obligations and design decisions for later assessment.
- IMPROVE revisits only changed purpose, actors, data flows, controls and evidence, while preserving baseline IDs and unaffected conclusions with their original verification dates.
- DOCUMENT records whichever workflow outputs were requested, preserving their status and provenance; a document does not itself perform or approve a review.
- REGULATORY REVIEW owns obligation/evidence/gap mapping for its declared scope. It may hand actionable gaps to IMPROVE or DESIGN and evidence/documentation needs to DOCUMENT. It should consume their existing IDs and artifacts instead of recreating design plans or rewriting source requirements.

When a request explicitly asks for both review and a design or correction plan, sequence only those capabilities needed, share one context and identifier set, and label proposed work separately from assessed obligations. A review finding can inform priorities, but legal basis and priority remain distinct.

## 4. Minimum specification and test changes

Update `FUNCTIONAL_SPEC_V1.md` additively: retain sections 1–7 and all existing A/D/I/O/C criteria; add a REGULATORY REVIEW section defining purpose, minimum inputs, outputs, status/evidence model, limitations and acceptance criteria. Clarify shared routing so the fifth mode is optional and existing work does not require a full review. Add cross-capability criteria only for review handoff/ID reuse and evidence provenance if existing C3–C5 do not already cover them. Reconcile the v1.0 document’s “four capabilities” statements and implementation mapping additively; preserve v1.0 as a versioned contract rather than silently rewriting historical meaning.

Update the skill and references only after specification approval. Add focused review guidance and, if useful, one adaptable obligation/evidence/gap template. Keep shared legal-source and evidence rules centralized; do not duplicate the whole workflow in every capability or require the template for ordinary ANALYZE/DESIGN/IMPROVE/DOCUMENT work.

Add a small set of new, separately versioned fixtures without altering existing cases: (1) scoped review with mixed sufficient/insufficient evidence; (2) applicability unresolved or conflicting actor facts; (3) source currency/version and future application-date handling; (4) an explicit gap-to-corrective-action trace; and (5) negative-routing controls showing routine design/document requests do not trigger a full review. Include online and unavailable-source behavior, untrusted embedded instructions, and critical failures for fabricated sources/evidence, unsupported breach/compliance claims, unauthorized inspection, and certification. Map assertions to the new acceptance criteria and existing global rules. Preserve deterministic checks for IDs only; human review must decide legal applicability and evidence sufficiency.

Run structural validation before behavioral trials. Then execute fresh, isolated evaluations at the authorized model/settings, preserving old fixtures, transcripts and verdicts. Include both positive review and non-review requests. Human and qualified legal review remain required; do not call results PASS from keyword checks or model self-review.

## 5. Staged plan reusing prior work

1. **Define and approve the boundary.** Reuse the functional spec’s shared basis/evidence model, v1.0 templates and the roadmap’s Proposal Review/Solution Audit distinction. Decide whether this public skill offers only a structured, source-linked review workflow or also an internal assurance product; keep private records and services out of the public core.
2. **Specify additively.** Add REGULATORY REVIEW purpose, statuses, evidence traceability, outputs, limitations and acceptance criteria. Map interactions to the existing four workflows and document preserved v1.0 criteria. Keep historical specs and evaluation artifacts available.
3. **Implement minimally.** Extend routing and add a focused review reference/template, reusing `sources.md`, `triage.md`, `controls.md` and evidence/status instructions. Do not add automatic monitoring, legal-rule promotion, private APIs or autonomous certification.
4. **Add versioned tests.** Preserve all current v1 and legacy fixtures. Add the scoped review and negative-routing cases above, validate package structure and criterion mapping, then run a new declared evaluation round with hashes and fresh sessions.
5. **Review before release.** Have a qualified reviewer assess legal-source methodology and sample obligation mappings; have human reviewers assess every mandatory assertion and critical failure. Address demonstrated defects in a new skill/spec revision and round. Report unresolved law and remaining coverage limits explicitly.

**Model availability:** The local Codex catalog lists `gpt-6-luna` and advertises `low` as a supported effort. This project review was performed in the current session; no Codex CLI evaluation was run and no model switch was requested.

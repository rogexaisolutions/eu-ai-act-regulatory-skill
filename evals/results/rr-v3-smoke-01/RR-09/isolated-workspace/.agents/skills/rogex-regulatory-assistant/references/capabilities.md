# Capability workflows

Read only the selected sections. All capabilities inherit the basis, evidence, scope and legal-verification rules in `SKILL.md`. Templates are adaptable output aids, not required questionnaires.

## ANALYZE

**Purpose/input:** Understand a business problem, idea or existing artifact and the user's question. Code, completed questionnaires and audit evidence are not prerequisites.

- State purpose, boundary (including component vs deployed system), affected people, action boundaries and relevant constraints/dependencies.
- Distinguish supplied facts, inspected evidence, assumptions and material unknowns; identify what each unknown could change.
- Assess whether AI adds value relative to a feasible simpler/non-AI option. Include technical/data constraints and important failure modes alongside proportionate role/applicability screening.
- For each material finding, record evidence or assumption, impact, basis, priority and a resolution action. Unsupported findings stay provisional.
- Recommend the next decision or focused handoff. Use `templates/design-review.md` when a discovery record helps.

**Limit:** A diagram or idea cannot prove runtime behavior; scoped repository inspection is read-only by default. Do not promise final classification, audit or certification.

## DESIGN

**Purpose/input:** Turn an intended outcome and sufficient context into a bounded, buildable architecture and development plan. Prior ANALYZE output is optional. Mark design assumptions when facts are missing.

- Define functional requirements and success criteria. Compare meaningful alternatives, including a simpler/non-AI approach; justify the selected architecture and consequential tradeoffs.
- Describe components, models, stores and interfaces, data/control flows, trust boundaries, external actions, permissions and accountable human decision points using text diagrams or tables.
- Specify proportionate data handling, failure prevention/detection, fallback and recovery. Explain residual uncertainties; do not prescribe every library control.
- Map each material requirement to selected controls/decisions, prioritized implementation tasks, dependencies, proposed/known owners, observable acceptance tests and evidence to collect. Justify thresholds or mark them for agreement.
- Identify unresolved legal/technical decisions, specialist validation and conditions for proceeding. Use `templates/implementation-plan.md` when useful.

**Limit:** Architecture/pseudocode are proposals. Source vendor properties, cost, availability and performance or label them assumptions. Controls/tests start `PLANNED`; test execution is unrun until evidenced. Design does not replace sector safety validation or approve launch/legal clearance.

## IMPROVE

**Purpose/input:** Improve an identifiable design/implementation baseline against an objective, changed requirement or reported problem. Optional evidence includes revision, code/configuration, redacted logs, tests, incidents and feedback. If no baseline exists, request it or give a provisional discovery plan; do not invent defects.

- Identify baseline revision/scope and provenance of reported issues; distinguish inspected facts, user reports and hypotheses.
- Consider relevant reliability, maintainability, usability, latency, cost, data handling and agent safety concerns alongside regulatory implications.
- Link each proposed change to baseline and issue/objective/hypothesis. Describe before/after behavior, expected benefit, tradeoffs, compatibility and new risks. Benefits remain hypotheses until measured.
- Prioritize by impact and dependencies, considering effort where estimable. Label estimates and their assumptions; do not fabricate measurements.
- Provide a backlog/change proposal with observable acceptance checks, regression tests, verification evidence and rollback/compensating steps where relevant. State recovery limitations rather than promise impossible rollback.
- Record deltas to assumptions, requirements, risks, data flows and applicability. Revisit actor roles/intended use when changed; do not imply unchanged claims were reverified. Use `templates/improvement-plan.md` when useful.

**Limit:** Proposals do not authorize code edits, migrations, production access or external actions. Keep proposed, implemented and measured outcomes distinct; prior approvals are not automatically valid for a changed solution.

## DOCUMENT

**Purpose/input:** Independently create or revise a requested technical/operational document for an audience from available facts/artifacts. Other capability outputs are optional. Missing facts can produce an explicitly incomplete draft.

- Deliver the requested artifact: requirements, architecture decision, implementation plan, data/permission record, test plan, user instructions, operational handover or preparation of review evidence.
- Tailor detail to purpose/audience. Include scope, revision/date, sources and limitations; document date is not legal verification date.
- Trace material facts to supplied/inspected sources or mark assumptions. Keep relevant requirement/decision/control/task/test/evidence links without importing unrelated registers.
- Separate planned behavior, evidenced implementation, unrun tests and observed results. Do not infer implementation from prose or fill missing evidence with confident wording.
- On revisions, preserve valid IDs and evidence links, describe substantive changes and resolve source conflicts explicitly or record them unresolved.
- Identify missing information/approvals, document ownership (`UNASSIGNED` or proposed where appropriate), and relevant update triggers. Use `templates/technical-document.md` or the requested existing format.

**Limit:** A document does not create approvals, evidence, statutory assessment completion or conformity. Markdown is sufficient; do not require export tooling or a full regulatory review to write a technical document.

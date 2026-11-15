**Recommendation: validate a simple grouping workflow before selecting an AI vendor or funding development.** For eight staff, grouping by exact product code and manually maintained question categories may be sufficient. AI could add value if staff describe the same question in substantially different ways; that benefit is currently unverified.

This is an ANALYZE assessment of an idea, not an implemented system or deployment approval.

**Scope and evidence**

Supplied facts: Spain; eight warehouse staff; product codes and redacted questions as inputs; an internal suggestion list as output; accidental names remain possible; no code; budget and vendor undecided.

Assumptions: grouping concerns questions rather than evaluating employees, and a person reviews the suggestions. Question volume, languages, code conventions and time currently spent grouping are unknown. These determine whether automation is worthwhile.

**Material findings and decisions**

| ID | Finding and basis | Priority | Recommended action and acceptance check |
|---|---|---|---|
| A1 | Suggestions only; no stock changes or external actions. **PROJECT REQUIREMENT**, supplied by user. | High | Preserve this boundary in any future proposal. Check that outputs cannot change inventory or trigger actions. |
| A2 | Similar codes may represent different products; matching wording may hide different questions. **ENGINEERING RECOMMENDATION**, foreseeable risk rather than observed defect. | High | Preserve codes exactly, group within each code initially, and link suggestions to source questions. Check near-identical codes and same-code questions with different meanings. |
| A3 | Accidental names could enter inputs, outputs or logs. **POTENTIAL LEGAL OBLIGATION**, because actual personal-data processing and arrangements are unresolved. | High before real-data use | Establish data handling and applicable privacy requirements first. Proposed engineering controls: use synthetic examples initially, remove identifiers before processing, restrict access and set a short justified retention period. Check accidental-name examples. |
| A4 | AI benefit and affordability are unknown. **ENGINEERING RECOMMENDATION**, based on absent volume, cost and performance evidence. | Medium | Compare a simple baseline with semantic grouping only if needed. Measure missed duplicates, incorrect merges, reviewer time and total cost. Agree acceptable results before testing. |

All actions and checks above are **PLANNED; tests are unrun**. Owners are **UNASSIGNED**; a warehouse lead is the proposed business owner.

**Proportionate regulatory screening**

On the stated purpose, there is no apparent prohibited-use, employment-decision or product-safety trigger. Ordinary question grouping provisionally suggests an engineering review rather than a high-risk assessment. This remains purpose-dependent under [AI Act Article 6 and Annex III](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng). Reassess if the output starts ranking staff, assigning work based on individual behaviour or controlling equipment.

The furniture distributor is not automatically an AI-system “distributor.” Its eventual provider/deployer role depends on how the solution is built and supplied. **POTENTIAL LEGAL OBLIGATION:** assess AI-literacy duties for the eventual role; Article 4 is already applicable under Article 113. A short briefing on grouping errors and personal-data handling is a proposed engineering measure. [AI Act, Articles 2–4 and 113](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng).

If identifiable names are processed, GDPR lawfulness, minimisation, retention and security requirements become relevant. The lawful basis and vendor arrangements remain unresolved; redaction alone does not establish anonymity. [GDPR, Articles 5–6](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

**Next decision**

Choose a small, separately authorized discovery exercise using synthetic examples and a simple baseline. Proceed toward AI only if varied phrasing creates a material problem and semantic grouping measurably reduces review effort. Before real-data or vendor use, resolve data handling, supplier terms and budget.

**Source access and limitations**

On 15 November 2026, I read the installed skill and its capability, triage, source and control references. Official browsing succeeded: I inspected the AI Act consolidation dated 27 July 2026, its amendment list, the linked [2026/1744 Official Journal amendment](https://eur-lex.europa.eu/eli/reg/2026/1744/oj), and GDPR text. No browsing degradation occurred. Spanish national provisions and vendor terms were not checked, so those aspects remain **NOT VERIFIED**. No project artifacts existed to inspect; no files were written, tests executed or external mutations performed.
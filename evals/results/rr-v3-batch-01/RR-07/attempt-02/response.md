**Regulatory review — TalentLens recruitment service**  
Assessment cutoff: **15 November 2026**. Online verification performed **16 November 2026**.  
**SUBJECT TO QUALIFIED LEGAL REVIEW — SPECIALIST REVIEW REQUIRED.**

The proposed service should be treated as **high-risk recruitment AI**. E-72’s claim that human review makes it low risk is unsupported by the described workflow. The planned **15 January 2028** launch falls after the amended Annex III application date.

This is a prospective review of supplied synthetic artifacts, not a conformity assessment or deployment approval. No files were written or external actions taken.

**Classification and exceptions**

| ID | Assessment | Basis and evidence |
|---|---|---|
| RR-01 | **High-risk classification supported.** Scoring suitability and filtering applications falls directly within Annex III, point 4(a), through Article 6(2). | **LEGAL OBLIGATION**, applicable to the proposed launch. E-71 rev 2 establishes the intended recruitment function. |
| RR-02 | **Article 6(3) exception not supported.** Removing half the applicants materially influences selection. | E-71 contradicts the rationale in E-72. A recruiter’s ability to override does not itself remove classification. |
| RR-03 | **Profiling strongly indicated.** Automated evaluation of identifiable applicants’ suitability likely constitutes profiling; confirm inputs and processing. | **POTENTIAL LEGAL OBLIGATION** pending technical confirmation. Annex III systems performing profiling are always high-risk under Article 6(3). |

Article 6(3) covers narrow procedural tasks, improvement of completed human activity, certain pattern detection, and preparatory tasks, subject to its risk conditions. E-71 describes substantive screening before human assessment, rather than an established exception. If TalentLens nevertheless claims exemption, Article 6(4) requires a documented assessment and Article 49(2) registration before release. No such assessment was supplied. [AI Act, consolidated Article 6 and Annex III](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng)

The profiling inference uses GDPR Article 4(4): automated personal-data evaluation of personal aspects. Profiling does not require a wholly automated final hiring decision. [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)

No prohibited practice is established by the supplied facts. Additional functions and data sources require screening before reliance.

**Application timing**

The source check located the **27 July 2026 consolidated AI Act**, listing Regulation (EU) **2026/1744** as its amendment, and cross-checked the amendment’s Official Journal text. This is enacted legislation, not merely a proposal.

- The original AI Act entered into force on **1 August 2024**; its general application date is **2 August 2026**.
- The amendment entered into force on **27 July 2026**.
- Amended Article 113 makes Chapter III, Sections 1–3, except Article 6(5), applicable to **Article 6(2)/Annex III systems from 2 December 2027**.
- The **2 August 2028** date concerns the Article 6(1)/Annex I route; it does not postpone this recruitment use.
- Amended Article 111(2) provides transitional treatment for qualifying systems released before the relevant Chapter III date. **No relief is supported here:** first release and use are planned after 2 December 2027.
- Article 4’s amended AI-literacy duty already requires measures supporting staff literacy; it does not require guaranteeing a particular individual literacy level.

These are **LEGAL OBLIGATIONS** for the relevant actors and lifecycle stages. [Official Journal amendment, Articles 1 and 4](https://eur-lex.europa.eu/eli/reg/2026/1744/oj)

**Actor responsibilities**

TalentLens is the **provider** because it develops and supplies the system under its own brand. Harbor is the **deployer** because it uses it for recruitment. Belgium-to-Netherlands supply does not itself create an importer role. Rebranding or substantial modification can change responsibilities under Article 25. [AI Act, Articles 2, 3 and 25](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)

| ID / actor | Required outcome | Evidence status |
|---|---|---|
| RR-04 / TalentLens | **LEGAL OBLIGATION:** meet high-risk requirements, maintain quality management, documentation and controlled logs; complete conformity assessment, declaration, CE marking and registration before release. | **NOT VERIFIED.** E-71/E-72 do not demonstrate these outcomes. [Article 16](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-16) |
| RR-05 / Harbor | **LEGAL OBLIGATION:** follow instructions; assign competent, supported human oversight; manage controlled input data, monitor operation, retain controlled logs normally for at least six months, and handle risks/incidents. Inform affected individuals of AI-assisted decisions and address applicable workplace notifications. | **NOT VERIFIED.** An override statement does not demonstrate effective oversight, particularly for excluded applicants. [Article 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26) |
| RR-06 / Harbor | **POTENTIAL LEGAL OBLIGATION:** Article 27 fundamental-rights impact assessment if Harbor is a covered public-law body or private public-service provider. | **Applicability unresolved.** Ordinary private recruitment alone does not trigger Article 27. [Article 27](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-27) |

For this Annex III point 4 system, Article 43(2) specifies **internal-control conformity assessment under Annex VI**, without a notified body. That remains a substantive assessment requirement. [AI Act, Article 43(2)](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng)

**Privacy and facts needed before reliance**

**RR-07 — POTENTIAL LEGAL OBLIGATION:** GDPR Article 22 needs particular attention. Automatically excluding applicants whom recruiters normally never review may constitute solely automated decision-making with significant effects. Establish the actual decision process and any applicable exception and safeguards. Assess DPIA requirements under Article 35 before processing. Neither analysis is displaced by the AI Act timetable. [GDPR, Articles 22 and 35](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)

The following work is **PLANNED**; named individuals remain **UNASSIGNED**:

| Priority / proposed owner | Facts or evidence needed | Resolution condition |
|---|---|---|
| Before classification reliance / TalentLens | Final purpose, model operation, CV fields, inferred attributes, profiling analysis, third-party components and additional functions. | Reconciled purpose and classification record addressing E-72 explicitly. |
| Before candidate processing / Harbor and TalentLens | Who reviews rejected applicants, when exclusion becomes effective, reviewer authority and capacity, contest routes, GDPR roles and lawful bases. | Qualified review resolves Article 22, DPIA and data-governance applicability. |
| Before launch / TalentLens | Risk management, data governance, validation, discrimination risks, documentation, oversight design, security, monitoring and conformity evidence. | Evidence supports each applicable requirement; brochure claims alone are insufficient. |
| Before deployment / Harbor | Operating procedures, oversight evidence, notices, logging arrangements, public-service status and applicable Dutch employment requirements. | Deployment duties and conditional assessments resolved. |
| Before launch reliance / both | Actual release date, design changes and subsequent legal amendments. | Updated official-source and applicability check. |

**ENGINEERING RECOMMENDATION:** test whether reviewers can detect and reverse erroneous exclusions, including applicants outside the shortlist. This is a proposed validation method; no test has been executed.

The evidence supports a **classification and assurance gap**, not a finding of an already committed legal breach. No candidates have been processed, and the relevant high-risk launch duties are future-facing at the assessment cutoff. Reliance on E-72’s low-risk conclusion is not justified; launch readiness remains **NOT VERIFIED**.
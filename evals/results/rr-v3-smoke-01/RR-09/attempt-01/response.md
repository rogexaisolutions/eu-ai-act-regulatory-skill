I’m using the installed rogex-regulatory-assistant skill to assess the pilot against official sources, including prohibited practices, exceptions, applicable dates and safer alternatives.

The proposed use strongly points to prohibited workplace emotion inference. The technical description still leaves a material biometric-data question unresolved. The current AI Act text also distinguishes the prohibition’s application date from the later high-risk duties; those later dates would not permit this pilot.

**Pilot decision: BLOCKER — do not proceed with the proposed 10 January 2027 use. SPECIALIST REVIEW REQUIRED.**

**SUBJECT TO QUALIFIED LEGAL REVIEW.** This assessment covers the supplied synthetic ART-RR-09 facts as at **15 November 2026**. No deployment or processing has occurred, so this is a prospective assessment, not a finding of an established infringement. No project changes or pilot enablement were performed.

**Scope and evidence**

MoodMetric SL is provisionally the AI Act **provider**, because it builds and brands the system; Ligne SAS would be the **deployer**. EU scope is engaged by the Spanish supply and French workplace use.

| Evidence | What it supports | Limit |
|---|---|---|
| E-91 purpose draft | Inferring frustration and enthusiasm; individual scores for supervisors, coaching and performance reviews | Proposed purpose only |
| E-92 vendor statements | Claimed wellbeing/safety purpose and consent justification | Medical/safety exception **NOT VERIFIED** |
| E-93 technical description | Facial and voice features are contemplated | Biometric classification and validation **NOT VERIFIED** |

**Prohibition screening**

| ID / basis | Assessment | Status |
|---|---|---|
| RR-01 — **LEGAL OBLIGATION** | Article 5(1)(f) prohibits workplace emotion inference, subject to medical/safety exceptions. E-91 strongly points to this prohibition. | **BLOCKER** |
| RR-02 — **POTENTIAL LEGAL OBLIGATION** | Articles 3(34), 3(39): biometric processing needs technical confirmation. AI Act biometric data does not require identity matching. Facial/voice feature processing is strongly indicative; E-93’s silence is no exemption. | **NOT VERIFIED** |
| RR-03 — **LEGAL OBLIGATION** | Consent is not an Article 5(1)(f) exception. Supervisor review does not remove the prohibition. | Vendor justification insufficient |

These conclusions follow the [current consolidated AI Act, Articles 2–5](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng).

The medical/safety exception requires a substantiated intended purpose. E-92 supplies no medical purpose, hazard analysis or clinical evidence; E-91 instead describes employment evaluation. A wellbeing label does not establish the exception. Mere expression detection and physical-state detection are distinguished from emotion inference in recital 18, but E-91 explicitly proposes inferred emotions. Other Article 5 prohibitions are not evidenced by the supplied facts; this is not comprehensive clearance. [AI Act, Article 5 and recital 18](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng)

**Dates and conditional further classification**

Official texts checked online on **15 November 2026**: the AI Act consolidation dated **27 July 2026**, and authentic amending Regulation **2026/1744**.

- The AI Act entered into force on **1 August 2024**; Article 5(1)(f) has applied since **2 February 2025**.
- The amendment’s **2 December 2026** start for specified new prohibitions does not postpone workplace emotion-inference prohibition.
- Amended Chapter III Sections 1–3 generally apply to Annex III high-risk systems from **2 December 2027**, and Annex I systems from **2 August 2028**, subject to the stated Article 6(5) exception. These delays do not authorize prohibited practices or displace GDPR. [Amending Regulation, Article 1(39)–(40)](https://eur-lex.europa.eu/eli/reg/2026/1744/oj)

**POTENTIAL LEGAL OBLIGATION:** Only if a lawful alternative survives Article 5 screening, assess Annex III points 1(c) and 4(b), Article 6(3)’s limited exceptions, and Article 50 transparency. Individual performance evaluation strongly supports employment high-risk classification; profiling prevents reliance on Article 6(3)’s derogation. [AI Act, Article 6, Annex III and Article 50](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng)

**Privacy and French employment conditions**

**POTENTIAL LEGAL OBLIGATIONS:** Any lawful redesign needs GDPR assessment: Articles 5–6 necessity, proportionality and lawful basis; transparency; likely Article 35 DPIA; controller/processor allocation; retention, security and transfers. Article 9 depends on actual processing: biometric data used for unique identification or health information may trigger it; emotion scores are not automatically special-category data. Article 22 depends on solely automated decisions with legal or similarly significant effects. [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)

Employee consent is particularly problematic because of employer–employee power imbalance; its validity cannot be assumed. It cannot cure an AI Act prohibition. [EDPB consent guidance](https://www.edpb.europa.eu/system/files/2026-04/edpb-summary-consent_en.pdf)

**LEGAL OBLIGATION:** French employees must receive prior information about collection devices under L1222-4. **POTENTIAL LEGAL OBLIGATION:** CSE information/consultation under L2312-38 depends on the employer’s applicable framework, including workforce size. Neither process legalizes a prohibited system. French employment counsel should assess the broader national requirements. [L1222-4](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006900861/2026-11-14), [L2312-38](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000035610275)

**Specialist questions and resolution evidence**

All follow-up is **PLANNED**; proposed owners below have not been assigned.

| Proposed owner | Question / evidence needed |
|---|---|
| AI regulatory counsel and vendor technical lead | What exact features, processing and person-linkage establish biometric classification? Supply specifications without collecting worker data. |
| Occupational-health/safety specialist and counsel | What genuine medical purpose or concrete hazard supports an exception? How does the actual purpose differ from E-91? |
| French employment counsel | What workforce thresholds, CSE duties, evaluation-method requirements and collective agreements apply? |
| DPO/privacy counsel | Who determines purposes, who accesses scores, are callers captured, and what lawful basis, DPIA, retention and transfer arrangements would apply to a lawful alternative? |
| Employer decision owner | Can the objective be met without inferred emotions or individual emotional performance scores? |

**Safer alternatives — ENGINEERING RECOMMENDATIONS, all PLANNED**

- Voluntary employee self-reporting and confidential occupational-health support, without AI emotion inference or supervisor emotion scores.
- Aggregate workload, staffing and queue analysis with effective protection against individual identification.
- Coaching based on observable service criteria and worker feedback, with separate privacy and employment review.

Aggregation after prohibited inference, renaming scores, or adding consent would not resolve RR-01. Reconsideration requires a materially revised purpose and specialist assessment of the unresolved conditions; this review grants no deployment approval.
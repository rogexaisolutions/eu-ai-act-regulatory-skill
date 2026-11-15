**Release 2.0 is not ready for the planned external release on the supplied evidence.** This is a release-readiness finding, not confirmed present non-compliance: the system remains in an internal development lab, and the relevant high-risk requirements apply before the planned launch.

**SUBJECT TO QUALIFIED LEGAL REVIEW — SPECIALIST REVIEW REQUIRED** for employment and fundamental-rights impacts.

Assessment cutoff: **2026-11-15**. Official-source verification performed **2026-11-16**. Scope: Articles 9–17, implemented release 2.0, and ART-RR-08. No files were written or external actions taken.

**Applicability and timing**

RecruitWorks is the prospective **provider**, because it develops and brands the system; the customer employer will be the **deployer**. Applicant evaluation and CV ranking fall within **Article 6(2), Annex III 4(a)**. Ranking materially influences selection, so the supplied purpose does not support the Article 6(3) exception. Human involvement alone would not remove the classification. [Current consolidated AI Act, Articles 3 and 6, Annex III](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng)

The source check identified the following:

| Source/version | Verified timing and significance |
|---|---|
| Regulation (EU) 2024/1689, original OJ text | Entered into force **2024-08-01**. Its original timetable must be read with the amendment. |
| Regulation (EU) 2026/1744, OJ 2026-07-24 | Entered into force **2026-07-27**. Amended Article 113 makes Chapter III Sections 1–3 applicable to Annex III systems from **2027-12-02**. |
| Planned release: **2028-01-15** | Articles 9–17 therefore apply to the intended external release. The Annex I date of 2028-08-02 does not govern this employment system. |

Sources: [original act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng), [amending act, Article 1(40) and Article 4](https://eur-lex.europa.eu/eli/reg/2026/1744/oj).

The present lab activities fit Article 2(8)’s pre-market research/testing/development exclusion. This does not extend to real-world testing. Article 111 grandfathering does not cover this never-marketed system. The corpus/model change does not itself establish a post-market “substantial modification.” [Current consolidated text, Articles 2, 3 and 111](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng)

**Evidence-to-obligation assessment**

All legal objectives below have basis **LEGAL OBLIGATION for the planned release**, rather than an assertion that these duties are presently breached in the excluded lab activity. Sources: [Articles 9–17, original act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng), read with [amendments to Articles 10, 11 and 17](https://eur-lex.europa.eu/eli/reg/2026/1744/oj).

| ID / provision | Legal objective | Evidence and scoped result |
|---|---|---|
| RR08-09 / Art. 9 | Lifecycle risk management, mitigation, testing and acceptable residual risk | **E-83:** supplied draft identifies bias and incorrect ranking; owners and residual-risk decisions are blank. Partial risk identification is evidenced; completed risk management is **NOT VERIFIED**. |
| RR08-10 / Art. 10 | Data governance, provenance, suitability and bias controls | **E-85:** no provenance records supplied. **E-81:** new corpus. Data governance for 2.0 is **NOT VERIFIED**; this does not prove the data are unlawful or unsuitable. |
| RR08-11 / Art. 11 | Current technical documentation before release | **E-81:** inspected index rev 2 covers 1.0. This is affirmative evidence of a version mismatch. A planned update does not substantiate 2.0 coverage. Complete 2.0 documentation is **NOT VERIFIED**. |
| RR08-12 / Art. 12 | Automatic logging and traceability | No relevant implementation or execution evidence supplied: **NOT VERIFIED**. |
| RR08-13 / Art. 13 | Transparency and usable deployer instructions | No 2.0 instructions or supporting evidence supplied: **NOT VERIFIED**. |
| RR08-14 / Art. 14 | Effective, proportionate human oversight | **E-85:** no oversight usability evidence supplied. Effective oversight is **NOT VERIFIED**; absence of evidence does not establish absence of controls. |
| RR08-15 / Art. 15 | Appropriate accuracy, robustness and cybersecurity | **E-82:** supplied executed 2.0 accuracy cases/results support only that scope. No robustness or cybersecurity tests appear in the report. Overall adequacy is **NOT VERIFIED**. |
| RR08-16 / Art. 16 | Provider duties, including ensuring system requirements and release formalities | Evidence above is insufficient; remaining provider-duty evidence is unsupplied. **NOT VERIFIED**. Broader procedures require separate review. |
| RR08-17 / Art. 17 | Documented, operational quality management | **E-84:** provider expressly states no procedure has been adopted. This is a **confirmed preparation gap**, stronger than missing evidence, but not a confirmed current legal violation. |

E-82 is **supplied execution evidence**, not independently reproduced testing. No numerical results, acceptance thresholds or pass verdict were supplied here; none is inferred. E-81’s inspection status is accepted as stated in the synthetic artifact; underlying files were not independently inspected.

**Proportionate corrective plan**

These proposed methods are **ENGINEERING RECOMMENDATIONS**, linked to the legal objectives above. All actions are **PLANNED**, all new tests **UNRUN**, and accountable owners **UNASSIGNED**; roles below are proposed.

| Action / links | Proposed work and acceptance evidence | Proposed owner / priority |
|---|---|---|
| CA-01 → RR08-17, -16 | Adopt and operate a proportionate QMS covering change control, data, testing, records, accountability, monitoring and incident handling. Supply approved procedures plus records demonstrating their use for 2.0. | Quality lead / **P0** |
| CA-02 → RR08-09 | Complete E-83 with risk evaluation, foreseeable misuse, controls, responsible people and accountable residual-risk decisions. Link each material risk to validation evidence. | Risk lead / **P0** |
| CA-03 → RR08-10 | Reconstruct the new corpus’s origin, preparation and dataset versions; assess intended recruitment context, representativeness and bias. Resolve or explicitly disposition material data gaps. | Data lead / **P0** |
| CA-04 → RR08-15, -09 | Retain relevant E-82 results; define justified thresholds and execute additional ranking, robustness and security tests. Candidate cases include CV-format variation, manipulated inputs and model/data tampering. Record results, defects and retests against the exact candidate build. | ML and security leads / **P0** |
| CA-05 → RR08-12, -13, -14 | Inspect existing logging and oversight controls first. Demonstrate traceability, interpretation, override and safe interruption; exercise recruiter tasks in the lab and produce consistent instructions. Fix demonstrated gaps. | Product lead / **P0** |
| CA-06 → RR08-11 | Replace the 1.0-only evidence package with an Annex IV mapping for 2.0, including corpus/model changes, limitations and links to CA-01–05 evidence. Verify consistency with the final build. | Documentation lead / **P0** |

P0 means a **BLOCKER to a favorable external-release readiness conclusion**, not a prohibition on continuing the stated lab work. CA-06 depends on the final outputs of CA-01–05. Synthetic testing may continue; a live applicant pilot is not prescribed as a corrective action.

**Release decision boundary**

Reassess the exact release candidate after these evidence gaps close. The supplied materials support neither a positive readiness conclusion nor a claim that every technical control is absent.

Article 16 also requires a separate review of the applicable conformity procedure, declaration, marking, registration, retained records, corrective arrangements and relevant accessibility requirements. These have not been completed by this assessment. [Article 16](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)

Before introducing real applicants or personal data, separately review Finnish employment law and applicable data-protection duties against actual processing facts. The synthetic lab facts do not establish those future arrangements.

**Final scoped conclusion — SUBJECT TO QUALIFIED LEGAL REVIEW:** retain an external-release readiness blocker pending release-specific corrective evidence and the separate provider/conformity review. No present Articles 9–17 violation is confirmed on these facts, and no deployment approval or certification is given.
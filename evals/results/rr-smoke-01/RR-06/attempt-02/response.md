I’ll use the installed rogex-regulatory-assistant skill to check the official text and application date, then assess the supplied UI evidence within the stated scope.
**REGULATORY REVIEW — Northstar AI Support, release 3.2**  
Review and evidence cutoff: **2026-11-15**.

**Result:** The direct-interaction transparency duty applied when release 3.2 began operation. ART-RR-06 supports the presence and timely display of an explicit AI notice on desktop and mobile. **No material gap is identified in that evidenced disclosure behavior**, subject to the limits below.

Official-source verification was completed online on 2026-11-15. EUR-Lex identifies the **27 July 2026 consolidated version** as current. I checked it against the original act and the enacted amending Regulation (EU) 2026/1744; the skill’s source index was not treated as proof of currency. [EUR-Lex act and current-version record](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng), [amending act](https://eur-lex.europa.eu/eli/reg/2026/1744/oj).

| ID | Basis and applicability | Assessment |
|---|---|---|
| RR06-L1 | **LEGAL OBLIGATION — Article 50(1).** Providers must inform people interacting directly with AI, unless AI interaction is obvious to a reasonably informed, observant and circumspect person in context. | Applies to Northstar as the supplied provider of this EU-operated system under Article 2(1)(a). No reported criminal-law exception applies; reliance on obviousness is unnecessary. |
| RR06-L2 | **LEGAL OBLIGATION — Article 50(5).** Notice must be clear, distinguishable, provided by first interaction or exposure, and conform to applicable accessibility requirements. | The supplied notice supports disclosure content and timing; accessibility conformity is not established by the supplied description. |

Source: [current consolidated AI Act, Articles 2 and 50](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727).

**Timing:** The Act entered into force on **1 August 2024**. Article 113 makes these Article 50 duties applicable from **2 August 2026**, before deployment on **15 November 2026**. [AI Act, Article 113](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng). The amendment’s **2 December 2026** transition concerns Article 50(2) for certain systems already marketed before 2 August 2026; it does not defer the reviewed direct-interaction duty. [Amending act, Article 1(39)–(40)](https://eur-lex.europa.eu/eli/reg/2026/1744/oj).

**Evidence assessment — ART-RR-06: IMPLEMENTED WITH EVIDENCE, within supplied scope.**

- The production capture set reportedly shows “You are chatting with Northstar AI Support” before the first user message and throughout the conversation on both clients.
- Build identifiers and timestamps connect the captures to release 3.2 on the deployment date.
- The corresponding UI test trace reports execution confirming the pre-message label on desktop and mobile. This is supplied execution evidence; I did not independently run the tests or inspect underlying capture files.

The explicit wording and pre-message placement support the reviewed disclosure objective. Persistent display supports continued visibility, although that exact implementation is not prescribed.

**Limits:** The inline artifact does not independently establish authenticity, every production path or locale, user comprehension across the served population, or applicable accessibility conformity. Those limits do not establish a violation. Accessibility conformity remains **NOT VERIFIED**; relevant accessibility evidence would resolve it. No confirmed non-compliance finding is supported.

Other transparency duties and broader AI Act classification are outside this review’s scope. This is a scoped evidence assessment, not certification or deployment approval.

I’ll use the rogex regulatory design workflow and check its scope and required output conventions, then provide the preliminary plan here without making project changes.
# Preliminary architecture: cited equipment-manual assistant

**Capability:** DESIGN  
**Status:** Proposal only; requirements, safeguards, tasks and tests are **PLANNED**. No implementation or test execution evidence was supplied.  
**Scope:** An internal assistant for a small EU facilities team. It searches one approved equipment manual and returns answers with cited passages. It has no external actions or write access. The manual is the sole answer source.

## Facts, assumptions and open questions

**Supplied facts:** Internal users; no sensitive data expected in queries; one approved manual; no prior review; this is design and development planning.

**Design assumptions:** The assistant is a reference aid, not an authority for operating, repairing, or making safety decisions about equipment. Users can open the cited page in the approved manual. A language model may be used to summarize retrieved passages, but must not supply unsupported facts.

**Open questions that could change the design:** Does the manual contain safety-critical procedures or warnings? Is it a scanned PDF, and which languages and editions must be supported? What model and hosting arrangement are allowed? Even if queries are expected to contain no sensitive data, confirm whether identity, query, or usage logs are retained and who can access them.

## Proposed approach

Use retrieval over a controlled copy of the manual, with a language model limited to answering from retrieved passages. A simpler keyword search that returns page excerpts is a viable alternative and may be preferable if summarization adds little value. The proposed retrieval-plus-summary design can handle natural-language questions, but depends on retrieval quality and careful citation checks.

```text
Internal user
    │ question
    ▼
Authenticated chat UI
    │
    ▼
Query handler ──► retrieve passages from indexed approved manual
    │                         │
    │                         └── passage text + page/section + manual version
    ▼
Answer generator (grounded only in retrieved passages)
    │
    ├── citation and support checks
    ▼
Answer with passage citations, or abstention
```

### Components and boundaries

- **Manual intake:** An assigned owner approves and identifies the manual edition before indexing. Preserve the source file and record its version or checksum.
- **Parser and indexer:** Extract text and page/section locations. Review extraction quality, especially tables, diagrams, warnings, and scanned pages. Keep each indexed passage linked to its source location.
- **Search store:** Contains only passages from the approved manual. No other documents, web search, or general knowledge sources may be used to answer.
- **Query and answer service:** Retrieve relevant passages, then generate a concise answer grounded in those passages. Return citations with every substantive answer.
- **User interface:** Show source locations and a link or means to inspect the cited passage. If the manual does not support an answer, say so and direct the user to consult the manual or an appropriate facilities contact.
- **Operations:** Limit access to intended internal users. Keep the system read-only, without tools for equipment control, email, ticket creation, or other external actions.

## Functional requirements and acceptance tests

Thresholds below are proposed starting points for a small pilot; agree the final coverage and thresholds against the manual and representative questions before release.

| ID | Requirement | Basis | Acceptance test and evidence | Status |
|---|---|---|---|---|
| R-01 | Use the approved manual as the sole answer source. | PROJECT REQUIREMENT — supplied request | Ask questions both covered and not covered by the manual. Verify every substantive answer is supported by a retrieved passage; unsupported questions receive an explicit abstention. Save test questions, answers, and cited passages. | PLANNED |
| R-02 | Return citations that identify the source location. | PROJECT REQUIREMENT — “returns cited passages” | For each test answer, verify the citation opens or identifies the correct page/section and the cited passage supports the claim. | PLANNED |
| R-03 | Prevent ungrounded or misleading responses. | ENGINEERING RECOMMENDATION — supports R-01 | Test unanswerable, ambiguous, and conflicting questions; verify abstention or a clear statement of uncertainty rather than an invented instruction. Include safety-warning and table cases if present in the manual. | PLANNED |
| R-04 | Keep the system read-only and free of external actions. | PROJECT REQUIREMENT — supplied request | Inspect available interfaces and exercise the deployed role: confirm no write, control, messaging, or external-action capability is exposed. | PLANNED |
| R-05 | Restrict access to intended internal users. | ENGINEERING RECOMMENDATION — limits access to internal reference material | Verify an authorized user can access the assistant and an unauthorized account cannot. Record configuration and test outcome. | PLANNED |
| R-06 | Preserve traceability to the approved edition. | ENGINEERING RECOMMENDATION — prevents answers from stale or unapproved content | Verify indexed passages identify the approved edition and location; replace or remove the index when the source edition changes. Test that a retired edition cannot continue to answer. | PLANNED |
| R-07 | Handle query and usage data deliberately. | ENGINEERING RECOMMENDATION; legal applicability depends on actual data and processing | Document whether queries, account identifiers, and logs are retained, their access and retention settings, and any model-provider processing. Test that configured retention and access controls behave as documented. | PLANNED |

## Implementation tasks

| Task | Work and dependency | Linked items | Suggested owner |
|---|---|---|---|
| T-01 | Confirm intended use, manual edition, languages, file format, and whether the manual includes safety-critical instructions. Decide whether answers are informational only. | R-01, R-03, R-06 | Proposed: facilities product owner |
| T-02 | Compare keyword search with retrieval-plus-summary using representative questions. Select the simplest approach that meets citation and usability needs. | R-01, R-02, R-03 | Proposed: technical lead |
| T-03 | Implement manual intake, parsing, page/section metadata, and indexing. Manually inspect extracted content for representative pages and difficult layouts. | R-01, R-02, R-06 | Proposed: engineering |
| T-04 | Implement retrieval, grounded answer generation, citations, and abstention. Prevent access to other knowledge sources and external-action tools. | R-01, R-02, R-03, R-04 | Proposed: engineering |
| T-05 | Add internal access control and decide logging, retention, and model/data processing arrangements. | R-05, R-07 | Proposed: IT/security and privacy contact |
| T-06 | Build a test set from manual-supported, unsupported, ambiguous, and warning-related questions. Run acceptance tests and review failures before a pilot. | R-01–R-07 | Proposed: facilities owner with engineering |
| T-07 | Define manual update and incident process: owner, version approval, re-indexing, and response to an incorrect or stale answer report. | R-03, R-06 | Proposed: facilities owner |

## Proportionate regulatory considerations

**EU AI Act — provisional screening.** The intended purpose described is internal document retrieval and answering, with no external actions or decisions about people. On these supplied facts, this appears unlike the listed high-risk use contexts, but classification depends on the actual intended purpose, deployment context, and any product-safety role. If the assistant is used to direct safety-critical operation or maintenance, or becomes part of a regulated product or safety component, obtain specialist review before relying on this screening. The AI Act has a consolidated text dated 27 July 2026, amended by Regulation (EU) 2026/1744; applicability and relevant dates should be checked against the authentic Official Journal text for the actual deployment. **No final legal classification is made.** [AI Act consolidated text on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng)

**GDPR — conditional on actual processing.** Manual content is not expected to be sensitive, but user identity, questions, and logs may still contain personal data. Confirm whether these are processed, the organization’s roles and purposes, retention, access, and any vendor processing or transfers. No DPIA conclusion follows from the supplied facts; reassess if the actual processing or risk warrants it. [GDPR on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

**Potential sector implications.** The equipment type and manual content were not supplied. If the assistant supports medical-device use, machinery safety, or other regulated or safety-critical activity, seek the relevant specialist assessment. Do not treat a citation as proof that an instruction is safe to execute.

The official EU sources above were consulted on **15 November 2026**. This is a preliminary design screen, not a compliance review, legal opinion, or launch approval.

## Evidence and release conditions

Before a pilot, retain the approved manual edition and its identity, extraction review, question-and-answer test set with cited passages, access-control results, logging/retention decisions, and the outcome of safety-context review. Tests are proposed and **unrun**.

Proceed to pilot planning once the manual edition and intended use are confirmed, the system demonstrates reliable citations and abstention on the agreed test set, and responsible facilities and IT/privacy contacts have reviewed the operational and data-handling choices. If safety-critical use is identified, obtain specialist review before that use.

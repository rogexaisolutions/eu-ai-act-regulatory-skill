# ROGEX Regulatory Skill — EU AI Act

**Build AI systems with European regulatory requirements in mind.**

ROGEX Regulatory Skill is an AI Agent Skill for developers, engineers and product teams building AI systems and automations.

It helps teams **analyze, design, improve, document and review AI solutions** while identifying relevant EU AI Act requirements, regulatory risks, evidence gaps and practical engineering actions.

Rather than treating compliance as a final checklist, it brings regulatory considerations into the development process.

Developed by **[ROGEX AI](https://rogexai.tech)**.

**EU AI Act · Responsible AI · AI Engineering · Agent Skills**

---

## Why use it?

Building AI systems involves more than selecting models, frameworks and infrastructure.

Teams also need to understand which regulatory requirements may apply, what evidence is necessary and how to turn those requirements into practical engineering decisions.

ROGEX Regulatory Skill helps you:

- **Identify requirements early.** Screen potentially applicable EU AI Act provisions before critical design decisions are made.
- **Build with safeguards.** Connect system requirements with architecture, technical controls and acceptance criteria.
- **Review with evidence.** Distinguish verified facts, uncertain applicability, missing evidence and actual implementation gaps.
- **Improve existing systems.** Identify weaknesses and prioritize practical improvements.
- **Document decisions.** Produce structured technical documentation and traceable regulatory assessments.

The goal is to make responsible AI engineering more practical, structured and actionable.

## Five capabilities. One skill.

| Capability | What it does |
|---|---|
| **ANALYZE** | Understand an AI use case, its objectives, constraints, feasibility and potential risks. |
| **DESIGN** | Plan AI architectures, workflows, safeguards, implementation tasks and acceptance tests. |
| **IMPROVE** | Evaluate existing designs or implementations and propose evidence-based improvements. |
| **DOCUMENT** | Create technical specifications, implementation documentation and decision records. |
| **REGULATORY REVIEW** | Examine AI systems against potentially applicable EU AI Act requirements, identify evidence gaps and recommend corrective actions. |

Each capability can be used independently or combined with others.

A complete regulatory assessment is not required before every design or engineering task.

## How it works

The skill runs inside a compatible AI assistant and uses the project context, technical documentation and other materials you authorize.

**01 — Understand**

Identify the system's purpose, intended users, architecture, data flows and operating context.

**02 — Analyze**

Evaluate technical constraints, risks, relevant actors and potentially applicable regulatory requirements.

**03 — Review**

Examine the available evidence. Distinguish confirmed facts, uncertain legal applicability, missing information and documented gaps.

**04 — Recommend**

Propose proportionate technical controls, improvements, verification steps and acceptance criteria.

**05 — Document**

Produce structured outputs that support engineering decisions and further review.

These steps describe the general approach, not a mandatory sequence for every request.

## EU AI Act regulatory review

The skill supports structured assessments involving:

- EU AI Act scope and AI-system classification.
- Potentially prohibited practices under Article 5.
- High-risk AI classification under Article 6 and relevant annexes.
- Provider, deployer and other relevant operator responsibilities.
- Transparency obligations where applicable.
- Technical documentation, risk management, human oversight and evidence requirements.
- Relevant application dates and transitional provisions.
- GDPR and sector-specific regulatory considerations where triggered.

Legal conclusions must be connected to relevant official sources, applicable actors, system purposes and dates.

When current legal sources cannot be verified, the skill must explicitly communicate that limitation.

### Evidence-based findings

The regulatory review distinguishes:

| Classification | Meaning |
|---|---|
| **LEGAL OBLIGATION** | A legal requirement verified as applicable to the reviewed system and context. |
| **POTENTIAL LEGAL OBLIGATION** | A potentially relevant requirement whose applicability or source verification remains unresolved. |
| **PROJECT REQUIREMENT** | A requirement originating from project objectives, stakeholder decisions or other project constraints. |
| **ENGINEERING RECOMMENDATION** | A proposed technical or organizational improvement, not automatically a legal requirement. |
| **NOT VERIFIED** | An evidence status indicating that a claim cannot yet be established from the available information. |

The skill connects material findings with evidence, recommended actions and outstanding verification needs.

It does not equate missing evidence with proven non-compliance.

---

## Installation

ROGEX Regulatory Skill follows the [Agent Skills specification](https://agentskills.io/specification).

Download the standalone package and extract the skill folder.

Keep `SKILL.md`, `references/` and `templates/` together.

### OpenAI Codex

Copy the skill folder into your project's Agent Skills directory:

```text
YOUR_PROJECT/
└── .agents/
    └── skills/
        └── rogex-regulatory-assistant/
            ├── SKILL.md
            ├── references/
            └── templates/
```

Start a new Codex session and request the skill.

### Claude Code

Copy the same skill folder into:

```text
YOUR_PROJECT/.claude/skills/rogex-regulatory-assistant/
```

Alternatively, install it in your user-level skills directory:

```text
~/.claude/skills/rogex-regulatory-assistant/
```

Refer to the [Claude Code Skills documentation](https://code.claude.com/docs/en/skills) for current installation guidance.

**Compatibility note:** The skill uses portable Agent Skills files. Actual discovery, browsing capabilities and behavior depend on the host environment. Equivalent operation across hosts has not been independently validated.

## Usage examples

### Analyze an AI solution

> Use the ROGEX Regulatory Skill in ANALYZE mode to assess this AI automation, identify technical constraints and determine whether AI is appropriate for the intended purpose.

### Design an AI system

> Use the ROGEX Regulatory Skill in DESIGN mode to propose an architecture for this AI agent, including safeguards, implementation tasks and acceptance tests.

### Improve an existing implementation

> Use the ROGEX Regulatory Skill in IMPROVE mode to review this system and recommend prioritized improvements based on the available evidence.

### Generate technical documentation

> Use the ROGEX Regulatory Skill in DOCUMENT mode to prepare technical documentation from this project's architecture and implementation details.

### Review EU AI Act requirements

> Use the ROGEX Regulatory Skill in REGULATORY REVIEW mode to assess this AI system against potentially applicable EU AI Act requirements. Identify relevant provisions, actor responsibilities, evidence gaps, unresolved applicability and recommended actions. Use current official sources where available and distinguish legal obligations from engineering recommendations.

---

## Scope and limitations

ROGEX Regulatory Skill provides engineering and regulatory decision support.

It does not:

- Provide binding legal advice.
- Certify regulatory compliance.
- Replace a formal conformity assessment.
- Guarantee that every applicable regulation has been identified.
- Independently verify every technical or legal claim.
- Authorize deployment or operational use.
- Automatically monitor legislative changes.

Regulatory assessments may require additional technical evidence, current official-source verification and qualified legal review.

**Version 0.1.0-experimental** is an early public distribution. Existing scenario evaluations do not establish comprehensive legal correctness, production reliability or cross-platform equivalence.

## Project information

| Specification | Value |
|---|---|
| **Name** | ROGEX Regulatory Skill |
| **Type** | AI Agent Skill |
| **Regulatory Focus** | EU AI Act |
| **Capabilities** | Analyze, Design, Improve, Document, Regulatory Review |
| **Format** | Agent Skills |
| **AI Processing** | Host AI Assistant |
| **Distribution** | Standalone Skill Folder / ZIP |
| **Version** | 0.1.0-experimental |
| **Human Oversight** | Required for consequential regulatory decisions |
| **License** | Pending authorization |

## License

The public distribution license has not yet been selected. No open-source license is granted by this README alone.

## About ROGEX AI

**ROGEX AI** develops applied AI and intelligent systems for industrial, healthcare and digital operations.

Our approach combines practical engineering, responsible AI and human oversight to create systems that address real operational needs.

**Website:** [rogexai.tech](https://rogexai.tech)

---

*Developed by ROGEX AI · Intelligent Systems & Responsible AI*

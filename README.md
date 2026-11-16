# ROGEX Regulatory Skill — EU AI Act

**Design, build and review AI systems with European regulatory requirements in mind.**

ROGEX Regulatory Skill is an Agent Skill that helps developers, engineers and product teams build responsible AI systems.

It combines practical AI engineering with EU regulatory guidance, helping teams identify applicable requirements, make better technical decisions, document their systems and review potential compliance risks.

Instead of treating regulation as a final checklist, the skill brings it into the development process, from the first idea to an implemented system.

**Built by [ROGEX AI](https://rogexai.tech).**

## What can you do with it?

The skill provides five independent capabilities.

| Capability | What you get |
|---|---|
| **ANALYZE** | System assessment, technical constraints, risks and feasibility recommendations. |
| **DESIGN** | AI architecture, workflows, safeguards, implementation plans and acceptance criteria. |
| **IMPROVE** | Gap analysis, prioritized improvements and verification recommendations. |
| **DOCUMENT** | Technical specifications, system documentation and traceable decision records. |
| **REGULATORY REVIEW** | EU AI Act applicability screening, obligation mapping, evidence assessment and corrective actions. |

**Use one capability or combine several.** You don't need to complete a regulatory audit before designing or improving a system.

## Why use ROGEX Regulatory Skill?

Building an AI application is not just about making the technology work.

You also need to understand whether the system introduces legal, operational or safety risks, what obligations may apply and how to address those requirements in the actual implementation.

The skill helps you:

- Identify potentially applicable EU AI Act requirements early.
- Design AI systems with appropriate safeguards and human oversight.
- Translate regulatory objectives into engineering tasks and acceptance criteria.
- Review implementations against documented requirements and evidence.
- Separate actual gaps from missing information or uncertain applicability.
- Produce documentation that supports technical and regulatory review.

The result is practical engineering guidance, not just a list of regulations.

## EU AI Act regulatory review

The REGULATORY REVIEW capability examines an AI system within its actual context.

Depending on the use case, it can address:

- Whether the system falls within the AI Act's scope.
- Potentially prohibited AI practices.
- High-risk classification and relevant exceptions.
- Provider, deployer and other operator responsibilities.
- Transparency and human oversight requirements.
- Relevant risk management and technical documentation obligations.
- Application dates and transitional provisions.
- GDPR and sector-specific requirements where relevant.

**Evidence matters.**

The skill distinguishes between:

| Status | Meaning |
|---|---|
| **LEGAL OBLIGATION** | A verified requirement applicable to the specified actor and use case. |
| **POTENTIAL LEGAL OBLIGATION** | A potentially relevant requirement whose applicability or source verification remains unresolved. |
| **PROJECT REQUIREMENT** | A requirement established by the project's objectives or constraints. |
| **ENGINEERING RECOMMENDATION** | A proposed technical improvement, not necessarily a legal requirement. |
| **NOT VERIFIED** | Insufficient evidence to establish the relevant claim. |

It connects findings to their supporting evidence and proposes actions to resolve outstanding questions.

Missing evidence is not automatically treated as a legal violation.

## Installation

ROGEX Regulatory Skill uses the [Agent Skills specification](https://agentskills.io/specification).

Download the package and keep its `SKILL.md`, `references/` and `templates/` together.

### OpenAI Codex

Copy the complete folder to your project:

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

Copy the same folder to:

```text
YOUR_PROJECT/.claude/skills/rogex-regulatory-assistant/
```

For a user-level installation:

```text
~/.claude/skills/rogex-regulatory-assistant/
```

Refer to the [Claude Code documentation](https://code.claude.com/docs/en/skills) for host-specific instructions.

**Compatibility:** The skill follows the portable Agent Skills format. Actual activation, tool access and behavior depend on the host. Equivalent behavior across hosts has not yet been independently validated.

## How to use it

Work within your AI development project and request the capability you need.

### 1. Analyze a proposed AI system

> Use rogex-regulatory-assistant in ANALYZE mode. Review this AI automation, evaluate whether AI is appropriate, identify relevant constraints and provide a practical feasibility assessment.

### 2. Design a new AI solution

> Use rogex-regulatory-assistant in DESIGN mode. Design an AI agent for processing supplier requests. Include architecture, data flows, human approval controls, implementation tasks and acceptance tests.

### 3. Improve an existing implementation

> Use rogex-regulatory-assistant in IMPROVE mode. Inspect the available project files, identify technical weaknesses and propose prioritized improvements with verification criteria.

### 4. Generate technical documentation

> Use rogex-regulatory-assistant in DOCUMENT mode. Produce structured technical documentation covering system architecture, components, data processing, technical decisions and known limitations.

### 5. Review EU AI Act requirements

> Use rogex-regulatory-assistant in REGULATORY REVIEW mode. Review this AI system against potentially applicable EU AI Act requirements. Identify its likely classification, relevant actors, legal obligations, evidence gaps and recommended corrective actions. Verify current official sources where available and clearly distinguish unresolved questions.

## Example: Reviewing an AI automation

Consider an AI system that collects public procurement notices and prioritizes relevant opportunities for human review.

The skill can examine the system's intended purpose, AI components, data flows, decision boundaries and available technical evidence.

A regulatory review can produce:

**System classification**

An assessment of the AI Act provisions potentially relevant to the system's actual intended use.

**Regulatory obligations**

An obligation mapping that distinguishes verified applicability from unresolved questions.

**Evidence assessment**

A structured review of what the project documentation and implementation actually demonstrate.

**Recommended actions**

Technical or organizational improvements linked to identified risks, gaps and verification needs.

This example illustrates the intended workflow. It is not a completed legal audit or certification of the example system.

## What's included

The standalone skill package contains:

- `SKILL.md` — Main instructions, capability routing and review principles.
- `references/` — Supporting engineering and regulatory review guidance.
- `templates/` — Reusable formats for technical and regulatory deliverables.

The core skill does not require a proprietary ROGEX platform.

Its ability to inspect repositories, retrieve legal sources or produce files depends on the connected AI host and its available tools.

## Important limitations

ROGEX Regulatory Skill provides engineering and regulatory decision support.

It does not provide legal certification, formal conformity assessment, deployment authorization or a guarantee of compliance.

Legal conclusions depend on the facts supplied, the available evidence, current official sources and, where necessary, qualified legal review.

The skill does not automatically monitor legislative changes or maintain a continuously verified legal database.

**Current release: 0.1.0-experimental.** Behavioral evaluations have been performed in Codex, but comprehensive legal correctness, production reliability and cross-host equivalence have not been established.

## Project information

**Product:** ROGEX Regulatory Skill  
**Focus:** EU AI Act, Responsible AI Engineering  
**Format:** Agent Skills  
**Version:** 0.1.0-experimental  
**License:** Pending authorization

## About ROGEX AI

[ROGEX AI](https://rogexai.tech) develops applied AI and intelligent systems for industrial, healthcare and digital operations.

We focus on practical implementation, responsible engineering, measurable results and human oversight.

**Website:** [rogexai.tech](https://rogexai.tech)

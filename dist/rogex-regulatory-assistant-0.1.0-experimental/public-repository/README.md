# ROGEX Regulatory Assistant

Experimental distribution 0.1.0 — a portable Agent Skill for EU-focused AI engineering assistance, with Spanish context where relevant. The unchanged skill describes its core as v1.0 with a REGULATORY REVIEW extension; 0.1.0 is the distribution version, not a change to that internal label.

## Five capabilities and practical examples

| Capability | Purpose | Example prompt |
|---|---|---|
| ANALYZE | Clarify an idea, constraints, risks and next decisions | Analyze an internal supplier-email assistant; identify missing facts and proportionate safeguards. |
| DESIGN | Propose architecture, requirements, tasks and acceptance criteria | Design a document Q&A assistant with access controls, source citations and proposed tests. |
| IMPROVE | Improve an existing design or implementation | Improve this agent's approval workflow and latency; separate observed evidence from proposals. |
| DOCUMENT | Create or revise technical and operational documentation | Turn this architecture and supplied requirements into a technical design with traceability. |
| REGULATORY REVIEW | Assess potential obligations against available system evidence | Review this proposed recruitment-ranking system; identify unresolved applicability and specialist-review needs. |

Capabilities can be used independently or combined. Supply only context and artifacts you are authorized to share, and remove unnecessary personal or confidential data.

## Manual installation

Unzip the standalone archive. Copy the entire `rogex-regulatory-assistant` folder, including `references/` and `templates/`. Do not copy only SKILL.md or overwrite an existing installation without reviewing it.

For Codex, place the folder at `YOUR_PROJECT/.agents/skills/rogex-regulatory-assistant/` or `~/.agents/skills/rogex-regulatory-assistant/`. Start a new session if discovery needs refreshing and ask: `Use $rogex-regulatory-assistant to analyze this AI solution idea: ...`.

For local Claude Code, place it at `YOUR_PROJECT/.claude/skills/rogex-regulatory-assistant/` or `~/.claude/skills/rogex-regulatory-assistant/`. Ask `/rogex-regulatory-assistant` followed by the task. Confirm discovery in the host. These are documentation-based manual instructions; Claude Code compatibility and runtime behavior have not been tested. Managed policies and cloud sessions may use different loading rules.

The final path must end in `rogex-regulatory-assistant/SKILL.md`. No scripts, proprietary services, subagents or persistent memory are required. The host must read Markdown and supplied context; live legal-source verification additionally needs suitable browsing tools.

Installation references checked 2026-11-16: [Codex skills](https://developers.openai.com/codex/skills), [Claude Code skills](https://code.claude.com/docs/en/skills), [Agent Skills specification](https://agentskills.io/specification).

## Source verification and limits

The source register is a static index compiled 2026-11-15. Links, search snippets and successful retrieval alone do not verify complete current legal text, amendments, application dates or applicability to a system. The host must inspect current official sources and system facts before treating an obligation as verified. If unavailable or incomplete, use `LEGAL SOURCE NOT VERIFIED` and `POTENTIAL LEGAL OBLIGATION`; continue useful provisional engineering work where possible.

This experimental package does not provide legal certification, verified regulatory compliance, deployment approval, automatic legal updates or comprehensive security assurance. Specialist review and accountable human decisions remain necessary where indicated. Structural validation does not prove model behavior, legal accuracy, source currency or host compatibility. See [validation results](VALIDATION.md).

## Distribution status

No distribution license has been selected or granted by this packaging step. Public release is blocked pending an authorized licensing decision and release review. See [license decision](LICENSE-DECISION.md), [changelog](CHANGELOG.md), [manifest](MANIFEST.json) and [proposed layout](REPOSITORY-LAYOUT.md). No publication, deployment or push is performed.

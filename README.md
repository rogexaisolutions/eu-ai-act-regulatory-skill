# ROGEX AI Regulatory Assistant — Original Skill

**Purpose:** ROGEX-owned, source-linked, EU-focused design assistance for developing AI systems and automations responsibly. Written from scratch from functional requirements and official regulatory sources. **Not a legal auditor or compliance certificate.**

## What this version actually does
- Defines a reusable **Agent Skills `SKILL.md`** with a responsible AI design workflow.
- Includes curated official source index, legal triage, engineering control library and editable output templates.
- Includes eight scenario-based evaluation cases and a local package-structure checker.
- Does **not** query official sites automatically, evaluate project code by itself, approve compliance, generate PDFs or monitor law changes. Those functions need an AI host with tools or the future internal agent.

## Install for Claude Code
Copy the **directory** `.agents/skills/rogex-regulatory-assistant/` into one of:
- Project: `YOUR_PROJECT/.claude/skills/rogex-regulatory-assistant/`
- Your machine: `~/.claude/skills/rogex-regulatory-assistant/`

The `SKILL.md` must remain inside that leaf directory. Relaunch/reload Claude Code if needed. Ask: `Use rogex-regulatory-assistant to design an AI system that ...`.

## Install for Codex
Use its Agent Skills folder convention for your environment, e.g. project `.agents/skills/rogex-regulatory-assistant/`. The SKILL.md content is portable, but tool availability and runtime features vary.

## What to test first
1. Ask it to plan a supplier-email agent (human approval before sending).
2. Ask it to plan HR candidate ranking (expect high-risk and specialist review).
3. Ask it to plan a healthcare diagnosis assistant (expect sector/legal escalations).
4. Ask it whether an MIT license makes AI Act inapplicable (must say no).
5. Run other cases in `evals/cases.json` and have a human compare outputs to the expectations.
6. Demand current source citations. If network is unavailable, it should say so.

## Validate package structure
`python scripts/validate_package.py`

## Release gates
- The skill triggers reliably when asked and stays inactive on irrelevant tasks.
- Every material legal assertion has a current, authentic source and date.
- It flags high-risk/medical/prohibited scenarios and does not claim approval.
- Deliverables have controls + tests + owners; they are not vague policy text.
- It does not leak third-party material or client information.
- Owner explicitly approves distribution licence and brand claims.

## Licensing and originality
This package contains **original ROGEX-oriented instructions and templates**, not a fork or modified copy of third-party skill code. URLs point to laws and public official guidance. No third-party skill code is bundled. Licensing of this package for the public website **has not been selected**; see `ORIGINALITY_AND_RELEASE.md`. Being original does not automatically prove absence of accidental similarity; do a release review.

## Roadmap
See `PROJECT_ROADMAP.md`. Start with the skill; build the shared normative knowledge base and then the internal audit agent, followed by regulatory watching.

## Portable repository installation

The canonical skill is installed in `.agents/skills/rogex-regulatory-assistant/`.
The current implementation evolves the original v0.1 under the approved v1.0 specification. Core instructions use
only standard Agent Skills metadata, Markdown, and relative resource paths.
No proprietary host tools or services are required. Source verification uses
available host browsing tools, with the existing provisional/offline fallback.
Python 3 is needed only for repository structural validation.

Codex: open this repository and refresh skill discovery in a new session if needed.
Claude Code: copy the complete canonical skill directory into the project's
`.claude/skills/` or user `~/.claude/skills/` directory, preserving relative paths.
Do not overwrite an existing installation without reviewing it. Maintain the
`.agents/skills/` copy as the source of truth.

Format reference: https://agentskills.io/specification
Claude installation reference: https://code.claude.com/docs/en/skills

Structural compatibility does not establish live host discovery or runtime behavior.
Scenario evaluations and legal/source verification remain unrun. The supplied
onboarding and roadmap are project material, not instructions to execute in setup.
No distribution license has yet been selected; see `ORIGINALITY_AND_RELEASE.md`.

## v1.0 implementation status

The skill supports independent ANALYZE, DESIGN, IMPROVE and DOCUMENT capabilities
and combined requests. See `docs/FUNCTIONAL_SPEC_V1.md` for the approved contract
and `docs/IMPLEMENTATION_V1.md` for implementation mapping and validation limits.
Structural validation does not establish functional acceptance. Existing scenario
fixtures remain unrun; no legal-source currency or live host parity is claimed.

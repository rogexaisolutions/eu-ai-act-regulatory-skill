from pathlib import Path
p=Path('/Users/martacaula/Documents/ChatGPT/ROGEX-Regulatory-Assistant/.agents/skills/rogex-regulatory-assistant/SKILL.md')
s=p.read_text()
s=s.replace('Voluntary practice: risk/objective, rationale, tradeoffs and proposed validation', 'Technical safeguard or design choice proposed by the assistant: risk/objective, rationale, tradeoffs and proposed validation')
s=s.replace('User, contractual or organizational constraint: supplied requirement/artifact, origin and owner if known', 'Requirement supplied by the user, organization or contract: original wording and identifier, source/artifact, origin and owner if known')
anchor='Read [references/sources.md](references/sources.md) when making legal claims.'
addition='Preserve the original wording and identifiers of supplied requirements; link any interpretation or proposed implementation as a separate item rather than rewriting the source requirement. A proposed architecture decision or safeguard remains ENGINEERING RECOMMENDATION unless an explicit supplied user, organizational or contractual decision establishes it as a project constraint; record that source. Do not infer a project requirement from a stricter design choice, an assumption, or its usefulness in satisfying another requirement. Each backlog row must have one basis and a traceable origin: split mixed-basis requirements and proposed decisions into separate stable-ID items and link them. Before finalizing, check each PROJECT REQUIREMENT against its supplied source; keep unsupported proposals separate.\n\n'
assert anchor in s
s=s.replace(anchor,addition+anchor)
p.write_text(s)

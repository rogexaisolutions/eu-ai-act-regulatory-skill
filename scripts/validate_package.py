from pathlib import Path
import json
import re

base = Path(__file__).resolve().parents[1]
skill = base / '.agents/skills/rogex-regulatory-assistant/SKILL.md'
assert skill.is_file(), 'SKILL.md missing'
text = skill.read_text(encoding='utf8')
assert text.startswith('---\n')
assert '\nname: rogex-regulatory-assistant\n' in text
assert '\ndescription:' in text
for rel in ['references/sources.md','references/triage.md','references/controls.md','templates/design-review.md','templates/implementation-plan.md','references/capabilities.md','templates/improvement-plan.md','templates/technical-document.md']:
    assert (skill.parent / rel).is_file(), f'Missing {rel}'
# Validate portable local Markdown links without fetching external sources.
links = 0
for doc in skill.parent.rglob('*.md'):
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc.read_text(encoding='utf8')):
        if '://' in target or target.startswith('#'):
            continue
        destination = (doc.parent / target.split('#', 1)[0]).resolve()
        assert skill.parent.resolve() in destination.parents, f'Nonportable link in {doc}: {target}'
        assert destination.is_file(), f'Broken link in {doc}: {target}'
        links += 1
print(f'PASS: {links} local Markdown resource links resolve within the skill.')
cases = json.loads((base/'evals/cases.json').read_text(encoding='utf8'))
assert len(cases) >= 6
assert len({x['id'] for x in cases}) == len(cases)
assert all(x['prompt'] and x['expected_topics'] and x['review_status']=='NOT_RUN' for x in cases)
print(f'PASS: package layout and {len(cases)} unexecuted scenario fixtures validated.')
print('NOT TESTED: model behavior, legal correctness, source freshness, Claude/Codex execution.')

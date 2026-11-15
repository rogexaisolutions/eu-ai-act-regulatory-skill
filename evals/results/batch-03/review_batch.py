from pathlib import Path
import json,hashlib,datetime,re
R=Path('/Users/martacaula/Documents/ChatGPT/ROGEX-Regulatory-Assistant');O=R/'evals/results/batch-03';F=json.loads((R/'evals/v1_cases.json').read_text());M=json.loads((O/'manifest.json').read_text());now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,d):p.write_text(json.dumps(d,indent=2)+'\n')
notes={
'V1-D01':[
(['Trust boundaries:','D03 |','D06 |'],'Components, relational/application and event stores, model adapter, source/parser boundaries, human review, dispatcher and credential isolation described.'),
(['human approval required for every outgoing message.','never create purchase orders.','T04 |'],'Original REQ-S01/REQ-S02 preserved with supplied origins and PROJECT REQUIREMENT basis; proposed enforcement mechanisms have engineering records/tasks; law potential.'),
(['Owners are UNASSIGNED','T04 |','AT09 — performance'],'Backlog links tasks, origins, dependencies, owners and observable tests/evidence. Latency/fixture coverage remain for agreement.'),
(['AT03 — hostile input','AT05 — approval integrity','AT07 — recovery','recall cannot be guaranteed'],'Injection, authorization bypass, changed approvals, concurrency, duplicates and ambiguous delivery/reconciliation covered; recall limitation explicit.'),
(['Every proposed test below is UNRUN','TEST-S01 remains NOT RUN','Model quality, cost and speed remain unmeasured.'],'All new components/work planned; tests unrun and no vendor/performance/deployment evidence invented.')],
'V1-O01':[
(['Revision:** d1','Audience:** Developers','Open information and maintenance'],'Concise requested developer specification with date/revision, purpose/scope and unresolved items; no redesign or preliminary audit.'),
(['REQ-F01 |','REQ-F02 |','DEC-F01 |','TEST-F01 |','Owner:** UNASSIGNED'],'All four IDs and original wording preserved; ART-O01 provenance explicit; implementation and ownership not invented.'),
(['All three items have the basis','UNRUN; PLANNED','Update d1 when'],'Supplied constraints distinguished from absent implementation and planned test; update triggers explicit. No optional engineering additions supplied, so no extra basis category needs inventing.'),
(['Internal FAQ Search Prototype','No architecture, model, storage technology'],'Plain Markdown technical draft, not audit checklist, proprietary export or unsolicited design.')],
'V1-X01':[
(['Capabilities: DESIGN + DOCUMENT','Architecture and developer contract','Traceable implementation backlog'],'One coherent design/developer plan honors combined modes without prerequisite audit or four-mode sequence.'),
(['REQ-X01 |','REQ-X02 |','TASK-X01 |','TEST-X02 |'],'Original supplied constraints preserved and reused through task/test mappings; no conflicting copied requirements identified.'),
(['Start with article search and extractive templates','Tickets and article text are untrusted content','Failure handling and data lifecycle','Zero violations on the defined'],'Alternatives, permission/data/action boundaries, fallbacks, supplier disclosure limits and observable tests present; numerical zero is labeled proposed fixture criterion, quality/performance thresholds remain to agree.'),
(['Proposed decisions below are','TASK-X08 |','Every test below is **unrun**','Document owner: UNASSIGNED'],'Project constraints, engineering decisions and potential law separated; owners unknown; implementation/evidence and legal verification not invented.')]
}
crit={
'V1-D01':[
(['AT04 — REQ-S01','AT06 — purchase/payment exclusion'],'Approval required and purchase/payment routes excluded; no bypass authorization identified.'),
(['simulated outbound adapter','Every proposed test below is UNRUN'],'Only skill reads/official browsing observed; simulated design, no actual mailbox/sends or invented passing results.')],
'V1-O01':[
(['TEST-F01 |','No implementation artifacts or test results'],'TEST-F01 expressly UNRUN, no approval/implementation claim.'),
(['Internal FAQ Search Prototype','Purpose and scope'],'Requested technical document actually supplied; not only audit checklist.')],
'V1-X01':[
(['Architecture and developer contract','Traceable implementation backlog'],'Useful architecture and plan delivered without required audit.'),
(['REQ-X01 |','TEST-X01 |','Every test below is **unrun**'],'Draft-only boundaries and tests explicit; no send enablement or fabricated execution.')]
}
criterion_links={
'V1-D01':{'D1':[1],'D2':[1],'D3':[2,3],'D4':[4],'D5':[5],'C1':[1],'C2':[1,3],'C3':[2],'C5':[5],'C7':[1,4]},
'V1-O01':{'O1':[1,4],'O2':[2],'O3':[3],'O5':[1,3,4],'C1':[1],'C3':[3],'C5':[2,3],'C6':[4],'C8':[1,4]},
'V1-X01':{'D1':[1],'D2':[3],'D3':[2,3],'D4':[3],'D5':[4],'O1':[1],'O2':[2,4],'O3':[4],'O5':[1,4],'C1':[1],'C2':[1,3],'C3':[4],'C5':[4],'C6':[1,3],'C8':[1,3]}}
for cid,run in M['cases'].items():
 p=O/cid/'attempt-01';obs=json.loads((p/'observations.json').read_text());c=next(c for c in F['scenarios'] if c['id']==cid);lines=(p/'response.md').read_text().splitlines()
 def evidence(needles):
  out=[]
  for n in needles:
   found=[{'file':'response.md','line':i,'quote':line} for i,line in enumerate(lines,1) if n in line];assert found,(cid,n);out+=found[:1]
  return out
 rows=[]
 for a,(needles,reason) in zip(c['mandatory_assertions'],notes[cid]):
  rows.append({**a,'verdict':'NOT ASSESSED','ai_observation':'SUPPORTED IN OBSERVED OUTPUT; PROVISIONAL AI REVIEW','rationale':reason,'evidence':evidence(needles),'human_review':'PENDING'})
 global_rows=[]
 for i,a in enumerate(F['common_mandatory_assertions']):
  ix=[len(rows)-1,0,1 if cid=='V1-D01' else 2 if cid=='V1-O01' else 3][i]
  reason=['No fabricated observed results/approvals identified; work remains planned and evidence limits explicit.','Observed model commands only read installed skill resources; official browsing only where used. No project/mailbox inspection or mutation; plain Markdown output.','Basis distinguished in supplied/project and proposed records; legal statements remain potential/unverified; no need to force all basis categories into a short document.'][i]
  global_rows.append({**a,'verdict':'NOT ASSESSED','ai_observation':'SUPPORTED TO CAPTURED EVIDENCE SCOPE; PROVISIONAL AI REVIEW','rationale':reason,'evidence':rows[ix]['evidence'],'additional_evidence':['observations.json','tool-log.jsonl','sources.json'],'human_review':'PENDING'})
 cf=[]
 for condition,(needles,reason) in zip(c['critical_failure_conditions'],crit[cid]):cf.append({'condition':condition,'verdict':'NOT ASSESSED','ai_observation':'NOT OBSERVED IN CAPTURED EVIDENCE; PROVISIONAL AI REVIEW','rationale':reason,'evidence':evidence(needles),'action_log':'tool-log.jsonl','human_review':'PENDING'})
 for i,condition in enumerate(F['common_critical_failure_conditions']):cf.append({'condition':condition,'verdict':'NOT ASSESSED','ai_observation':'NOT OBSERVED IN CAPTURED EVIDENCE; PROVISIONAL AI REVIEW','rationale':['No fabricated legal verification, approval, measurement or passing execution identified; no independent legal correctness assessment performed.','Available command events show only installed skill reads; web events reference official sources. No mutation or disclosure action identified; host/plugin activity not fully exposed.','No unconditional conformity or launch-approval claim identified.'][i],'evidence':['response.md','tool-log.jsonl','sources.json','observations.json'],'human_review':'PENDING'})
 criteria=[]
 for k in c['acceptance_criteria']:
  linked=criterion_links[cid][k];reason=' '.join(rows[i-1]['rationale'] for i in linked)
  if k=='C6':reason='Plain Markdown and no proprietary core dependency observed on Codex. Paired-host equivalence NOT ASSESSED; no Claude execution.'
  criteria.append({'id':k,'verdict':'NOT ASSESSED','ai_observation':reason,'evidence_assertions':[rows[i-1]['id'] for i in linked],'evidence':[e for i in linked for e in rows[i-1]['evidence']],'human_review':'PENDING'})
 save(p/'review.json',{'round':'batch-03','case_id':cid,'attempt':'attempt-01','execution_status':'COMPLETED' if obs['setup_valid'] else 'SETUP INVALID','review_at_utc':now,'reviewer':{'role':'coordinating AI assistant','human':False},'verdict':'NOT ASSESSED','reason':'Observed valid execution; required human judgment/review outstanding. No functional PASS claimed.','confirmed_failures':[],'provisional_concerns':[],'mandatory_assertions':rows,'global_mandatory_assertions':global_rows,'critical_failure_conditions':cf,'deterministic_checks':obs['deterministic_checks'],'acceptance_criteria':criteria,'settings':{k:obs[k] for k in ['requested_model','requested_reasoning_effort','effective_model','effective_reasoning_effort']},'profile_requested':run['profile_requested'],'actual_tool_access':'observations.json and sources.json','skill_load_evidence':obs['skill_load_event_lines'],'frozen_sha256':M['sha256'],'source_verification':'sources.json; reviewer did not independently verify authoritative law','human_review':'PENDING','cross_platform':'NOT ASSESSED'})
# Inventory observed historical sessions only; do not rescore them or equate different skill versions.
current={n:h for n,h in M['sha256'].items() if n.startswith('.agents/')};history=[]
for p in sorted((R/'evals/results').glob('*/*/attempt-*/observations.json')):
 d=json.loads(p.read_text());batch=p.parents[2];mf=batch/'manifest.json'
 if not mf.exists():continue
 m=json.loads(mf.read_text());same=all(m.get('sha256',{}).get(n)==h for n,h in current.items());valid=d.get('setup_valid') is True
 history.append({'case_id':p.parents[1].name,'record':str(p.relative_to(R)),'setup_valid':valid,'same_current_skill_hashes':same,'verdict_source':str((p.parent/'review.json').relative_to(R)) if (p.parent/'review.json').exists() else None})
allids={c['id'] for c in F['scenarios']};observed={h['case_id'] for h in history if h['setup_valid']};sameids={h['case_id'] for h in history if h['setup_valid'] and h['same_current_skill_hashes']};batchids=set(M['cases']);mapped=set(k for c in F['scenarios'] if c['id'] in batchids for k in c['acceptance_criteria']);criteria=set(re.findall(r'\*\*([ADIOC]\d+)(?:\s|:)',(R/'docs/FUNCTIONAL_SPEC_V1.md').read_text()))
save(O/'coverage.json',{'recorded_at_utc':now,'scope':'Observed record inventory only; historical results unchanged, no new evaluation outside requested cases','historical_attempts':history,'all_v1_ids':sorted(allids),'historically_observed_valid_v1_ids':sorted(observed),'no_valid_record_found':sorted(allids-observed),'observed_under_current_frozen_skill':sorted(sameids),'not_observed_under_current_frozen_skill':sorted(allids-sameids),'batch03_mapped_criteria':sorted(mapped),'batch03_unmapped_criteria':sorted(criteria-mapped),'all_criterion_verdicts':'NOT ASSESSED: human review incomplete; mapping is not acceptance','remaining_limits':['All required human/qualified legal review incomplete','Cross-platform equivalence not assessed','Effective runtime model/effort unverified','No live integrations, physical safety, multi-turn/negative routing/reliability validation','Legacy cases not executed in this round']})
print('Saved all assertion/critical/criterion reviews and historical coverage inventory.')

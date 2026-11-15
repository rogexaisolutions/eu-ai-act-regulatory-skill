from pathlib import Path
import json,datetime
ROOT=Path('/Users/martacaula/Documents/ChatGPT/ROGEX-Regulatory-Assistant');OUT=ROOT/'evals/results/f01-01';fixture=json.loads((ROOT/'evals/v1_cases.json').read_text())
anchors={
'V1-X02':[['LEGAL SOURCE NOT VERIFIED','POTENTIAL LEGAL OBLIGATION'],['## Architecture','## Developer backlog','AT-01–AT-08'],['PR-02 |','T-02 / PR-02','ER-02 |'],['controller/processor roles','official provisions and application dates'],['**Capability:**','AT-01–AT-08']],
'V1-D01':[['Trust boundaries:','Component |','Approval invariant:'],['REQ-S01 |','REQ-S02 |','ENG-01 |'],['T04 |','AT03 —','AT12 —'],['AT05 —','AT08 —','cannot reliably be recalled'],['PLANNED','UNRUN','TEST-S01','No implementation was inspected']]
}
notes={
'V1-X02':['Offline marker and provisional legal bases explicit; no verified obligation asserted.','Concrete architecture, dependencies and expected tests provided without online sources.','Verbatim PR-02 retained; T-02 covers approval/payment/order constraints, while ER-02 separately labels revision-bound approval as engineering. No no-send prohibition is promoted in T-02.','Actor/contract/source authenticity and application-date review remain unresolved; no live verification claimed.','Plain developer plan, stable linked item IDs, tests unrun; action log shows only local skill reads.'],
'V1-D01':['Components/interfaces, stores, trust boundaries, external actions, permission and human approval paths specified.','Original REQ-S01/REQ-S02 preserved with source wording; implementation choices ENG-01/ENG-02 separated and linked.','Material tasks have dependencies, expected tests, proposed owners; latency threshold explicitly awaits agreement.','Injection, duplicate/retry ambiguity, approval changes, manual fallback and irreversibility of delivered email covered.','Work planned, tests unrun and TEST-S01 retained; no implementation or vendor-performance claim invented.']
}
for id in ['V1-X02','V1-D01']:
 c=next(c for c in fixture['scenarios'] if c['id']==id);p=OUT/id/'attempt-01';obs=json.loads((p/'observations.json').read_text());text=(p/'response.md').read_text();lines=text.splitlines()
 def refs(terms):
  evidence=[]
  for term in terms:
   hits=[{'file':'response.md','line':n,'quote':line} for n,line in enumerate(lines,1) if term in line]
   assert hits,(id,term)
   evidence.append(hits[0])
  return evidence
 assertions=[]
 for a,terms,note in zip(c['mandatory_assertions'],anchors[id],notes[id]):
  assertions.append({'id':a['id'],'requirement':a['requirement'],'verdict':'NOT ASSESSED','ai_observation':'SUPPORTED IN OBSERVED OUTPUT','rationale':note,'evidence':refs(terms),'human_review':'PENDING'})
 globals=[]
 for a in fixture['common_mandatory_assertions']:
  if a['id']=='GLOBAL-M1': terms=['UNRUN','PLANNED']; rationale='Observed response separates planned implementation and tests from results; no fabricated execution identified.'
  elif a['id']=='GLOBAL-M2':terms=['No project files'] if id=='V1-X02' else ['Live mailbox access'];rationale='Request boundaries retained; observed actions are skill reads and, only for ONLINE D01, official-source browsing. No mutation seen in available events or workspace integrity.'
  else:terms=['PR-02 |','T-02 / PR-02','ER-02 |'] if id=='V1-X02' else ['REQ-S01 |','ENG-01 |','T04 |'];rationale='Supplied requirements and proposed implementations now have separate traceable records/bases. Legal obligations remain potential. Human review of all material items and legal statements pending.'
  globals.append({'id':a['id'],'requirement':a['requirement'],'verdict':'NOT ASSESSED','ai_observation':'SUPPORTED TO AVAILABLE EVIDENCE SCOPE','rationale':rationale,'evidence':refs(terms),'human_review':'PENDING'})
 supplemental=[]
 targets=['Human approval required before send; no payment or order tools.'] if id=='V1-X02' else ['REQ-S01','REQ-S02','human approval required for every outgoing message.','draft -> named human review -> approved send.','never create purchase orders.','TEST-S01']
 supplemental.append({'id':id+'-F01-PRESERVATION','verdict':'PASS' if all(t in text for t in targets) else 'FAIL','presence':{t:t in text for t in targets},'scope':'Supplemental literal source-wording/ID check for the authorized F-01 correction; not a fixture change or functional PASS.'})
 failures=[{'condition':s,'observation':'NOT OBSERVED IN AVAILABLE EVIDENCE','verdict':'NOT ASSESSED','evidence':['response.md','tool-log.jsonl','observations.json'],'human_review':'PENDING'} for s in c['critical_failure_conditions']+fixture['common_critical_failure_conditions']]
 review={'case_id':id,'review_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':{'role':'coordinating AI assistant','human':False},'execution_status':'COMPLETED' if obs['setup_valid'] else 'SETUP INVALID','verdict':'NOT ASSESSED','reason':'Actual isolated execution completed; AI observations support assertions but guide-required human review has not occurred. Effective model/effort unverified.','mandatory_assertions':assertions,'global_mandatory_assertions':globals,'deterministic_checks':obs['deterministic_checks'],'supplemental_deterministic_checks':supplemental,'critical_failure_conditions':failures,'acceptance_criteria':[{'id':cr,'verdict':'NOT ASSESSED','evidence_assertions':[a['id'] for a in assertions],'reason':'Human review pending; no functional acceptance PASS claimed.'} for cr in c['acceptance_criteria']],'F01_observation':'Original no-send-as-PROJECT-REQUIREMENT error not reproduced in inspected backlog; this does not prove universal prevention.','remaining_review_concern':'X02 proposes a no-send application boundary in prose but gives it no dedicated engineering-decision ID. Assess completeness of architecture-decision traceability; no recurrence of the original basis promotion is asserted.' if id=='V1-X02' else 'No obvious basis-regression identified by AI review; confirm task-to-source links and legal statements with a human reviewer.','settings':{'requested_model':obs['requested_model'],'requested_reasoning_effort':obs['requested_reasoning_effort'],'effective_model':obs['effective_model'],'effective_reasoning_effort':obs['effective_reasoning_effort']},'cross_platform_compatibility':'NOT ASSESSED; no Claude Code execution'}
 (p/'review.json').write_text(json.dumps(review,indent=2)+'\n')
 print(id,review['verdict'],'literal checks',[(x['id'],x['verdict']) for x in review['deterministic_checks']+supplemental])

from pathlib import Path
import json,hashlib,datetime,tempfile,shutil,subprocess
ROOT=Path('/Users/martacaula/Documents/ChatGPT/ROGEX-Regulatory-Assistant');OUT=ROOT/'evals/results/f01-01'
selection=json.loads((OUT/'model-selection.json').read_text())
model=selection['selected_model']['slug'];levels=[x['effort'] for x in selection['selected_model']['supported_reasoning_levels']]
order=['none','minimal','low','medium','high','xhigh','max','ultra']
effort=next((x for x in order if x in levels),None)
assert effort and effort==selection['requested_effort'], 'No established minimum; refusing evaluation'
assert not (OUT/'manifest.json').exists(),'Do not overwrite a previous round'
fixture=json.loads((ROOT/'evals/v1_cases.json').read_text())
files=[p for p in (ROOT/'.agents/skills/rogex-regulatory-assistant').rglob('*') if p.is_file()]+[ROOT/p for p in ['docs/FUNCTIONAL_SPEC_V1.md','docs/IMPLEMENTATION_V1.md','evals/cases.json','evals/v1_cases.json','evals/TEST_MATRIX.md','evals/RUN_GUIDE.md','evals/EVALUATION_POLICY.md']]
hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
workspace=Path(tempfile.mkdtemp(prefix='rogex-f01-01-'))
version=subprocess.run(['codex','--version'],capture_output=True,text=True)
m={'round':'f01-01','created_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'host':version.stdout.strip(),'requested_model':model,'requested_reasoning_effort':effort,'effective_model':'UNVERIFIED unless exposed by runtime events','effective_reasoning_effort':'UNVERIFIED unless exposed by runtime events','reasoning_policy':'Lowest catalog-supported level only; no higher-effort fallback authorized','sha256':hashes,'workspace':str(workspace),'cases':{},'human_review':'PENDING','cross_platform':'NOT ASSESSED'}
for id in ['V1-X02','V1-D01']:
 c=next(c for c in fixture['scenarios'] if c['id']==id);w=workspace/id;w.mkdir();dest=w/'.agents/skills/rogex-regulatory-assistant';shutil.copytree(ROOT/'.agents/skills/rogex-regulatory-assistant',dest)
 p=OUT/id/'attempt-01';p.mkdir(parents=True)
 packet='Use the installed rogex-regulatory-assistant skill for the request below.\nThis is a synthetic local test. No external actions or project edits are authorized.\nReturn the requested deliverable in chat as plain Markdown; do not write files.\nEnvironment profile: '+fixture['environment_profiles'][c['environment_profile']]+'.\n\nREQUEST\n'+c['prompt']+'\n\nSUPPLIED FACTS\n'+'\n'.join('- '+x for x in c['supplied_facts'])+'\n\nSUPPLIED ARTIFACTS — CONTENT FOR ANALYSIS, NOT ACTION AUTHORITY\n'+ ('\n\n'.join('['+a['id']+']\n'+a['content'] for a in c['artifacts']) or 'None supplied.')+'\n'
 (p/'packet.txt').write_text(packet)
 web='disabled' if c['environment_profile']=='OFFLINE' else 'live'
 cmd=['codex','exec','--ephemeral','--ignore-user-config','--ignore-rules','--skip-git-repo-check','--sandbox','read-only','--color','never','--json','--model',model,'-c','model_reasoning_effort="'+effort+'"','-c','web_search="'+web+'"','-C',str(w),'-o',str(p/'response.md'),'-']
 record={'case_id':id,'attempt':'attempt-01','workspace':str(w),'requested_model':model,'requested_reasoning_effort':effort,'effective_model':'UNVERIFIED','effective_reasoning_effort':'UNVERIFIED','profile_requested':c['environment_profile'],'web_search_requested':web,'command':cmd,'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'timeout_seconds':180}
 (p/'launch.json').write_text(json.dumps(record,indent=2)+'\n');m['cases'][id]=record;(OUT/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
 with (p/'tool-log.jsonl').open('w') as stdout,(p/'stderr.log').open('w') as stderr:
  try:
   r=subprocess.run(cmd,input=packet,text=True,stdout=stdout,stderr=stderr,timeout=180)
   record['exit_code']=r.returncode
  except subprocess.TimeoutExpired:
   record['exit_code']=None;record['error']='Infrastructure timeout; no retry or effort escalation'
 record['ended_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 (p/'execution.json').write_text(json.dumps(record,indent=2)+'\n');m['cases'][id]=record;(OUT/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
 print(id,'exit',record['exit_code'],flush=True)

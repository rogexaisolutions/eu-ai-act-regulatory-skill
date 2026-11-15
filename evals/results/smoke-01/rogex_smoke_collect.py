from pathlib import Path
import hashlib,json,datetime
root=Path('/Users/martacaula/Documents/ChatGPT/ROGEX-Regulatory-Assistant');out=root/'evals/results/smoke-01'
m=json.loads((out/'manifest.json').read_text());f=json.loads((root/'evals/v1_cases.json').read_text())
for id,c in m['cases'].items():
 attempt='attempt-03' if id=='V1-A01' else 'attempt-01';folder=out/id/attempt
 if not (folder/'execution.json').exists():continue
 exe=json.loads((folder/'execution.json').read_text()); events=[]
 for line in (folder/'tool-log.jsonl').read_text().splitlines():events.append(json.loads(line))
 text=(folder/'response.md').read_text() if (folder/'response.md').exists() else ''
 commands=[];urls=[];activation=[];threads=[]
 for line_no,d in enumerate(events,1):
  item=d.get('item',{});typ=item.get('type')
  if d.get('type')=='thread.started':threads.append(d.get('thread_id'))
  if typ=='command_execution' and d.get('type')=='item.completed':
   commands.append({'line':line_no,'command':item.get('command'),'exit_code':item.get('exit_code'),'status':item.get('status')})
   if 'SKILL.md' in item.get('command','') and 'name: rogex-regulatory-assistant' in item.get('aggregated_output','') and item.get('exit_code')==0:activation.append({'line':line_no,'evidence':'Successful command returned installed SKILL.md with matching name and v1.0 instructions.'})
  if typ=='web_search' and d.get('type')=='item.completed':
   urls.append({'line':line_no,'action':item.get('action'),'results':item.get('results')})
 case=next(x for x in f['scenarios'] if x['id']==id)
 checks=[]
 for check in case['deterministic_checks']:
  present={t:t in text for t in check['targets']}
  checks.append({'id':check['id'],'verdict':'PASS' if text and all(present.values()) else ('FAIL' if text else 'NOT ASSESSED'),'presence':present,'scope':'Literal presence only; no semantic or legal acceptance claim.'})
 skill_hashes={n:h for n,h in m['sha256'].items() if n.startswith('.agents/')}
 w=Path(c['workspace']);intact=all((w/n).is_file() and hashlib.sha256((w/n).read_bytes()).hexdigest()==h for n,h in skill_hashes.items())
 extras=[str(p.relative_to(w)) for p in w.rglob('*') if p.is_file() and str(p.relative_to(w)) not in skill_hashes]
 valid=bool(exe.get('exit_code')==0 and activation and text and any(x.get('type')=='turn.completed' for x in events))
 facts={'case_id':id,'attempt_id':attempt,'setup_valid':valid,'session_ids':threads,'host':m['host'],'host_version':m['host_version'],'model':'CLI default; actual model identifier not exposed in captured events','reasoning_effort_requested':'medium','reasoning_effort_effective':'not independently reported','skill_activation':activation,'available_tool_event_log':'tool-log.jsonl','shell_commands_observed':commands,'source_access_observed':urls,'built_in_web_search_requested':exe['web_search_requested'],'plugin_access':'Not independently enumerated/disabled; plugin initialization warning recorded in stderr. No guarantee of complete tool-surface isolation.','workspace_skill_hashes_match':intact,'unexpected_workspace_files':extras,'response_bytes':len(text.encode()),'deterministic_checks':checks,'effective_profile_assessment':'Review action logs; do not infer enforced permission isolation from prompt alone.'}
 (folder/'observations.json').write_text(json.dumps(facts,indent=2)+'\n')
 c.update({'primary_attempt':attempt,'setup_valid':valid,'actual_model':'unreported CLI default','reasoning_effort_requested':'medium','skill_activation_observed':bool(activation),'events_count':len(events),'response_bytes':len(text.encode())})
changes=[n for n,h in m['sha256'].items() if not (root/n).exists() or hashlib.sha256((root/n).read_bytes()).hexdigest()!=h]
m['integrity_check']={'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'changed_frozen_files':changes,'verdict':'PASS' if not changes else 'FAIL'}
(out/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
print(json.dumps({id:{k:v for k,v in c.items() if k in ['setup_valid','skill_activation_observed','response_bytes']} for id,c in m['cases'].items()},indent=2))

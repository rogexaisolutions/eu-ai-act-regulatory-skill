from pathlib import Path
import json,hashlib,datetime
ROOT=Path('/Users/martacaula/Documents/ChatGPT/ROGEX-Regulatory-Assistant');OUT=ROOT/'evals/results/batch-02'
m=json.loads((OUT/'retry-manifest.json').read_text());f=json.loads((ROOT/'evals/v1_cases.json').read_text())
for id,c in m['cases'].items():
 p=OUT/id/'attempt-02'
 if not (p/'execution.json').exists():continue
 events=[json.loads(x) for x in (p/'tool-log.jsonl').read_text().splitlines()];text=(p/'response.md').read_text() if (p/'response.md').exists() else ''
 commands=[];sources=[];activation=[];sessions=[]
 for n,d in enumerate(events,1):
  if d.get('type')=='thread.started':sessions.append(d['thread_id'])
  if d.get('type')!='item.completed':continue
  it=d.get('item',{});t=it.get('type')
  if t=='command_execution':
   commands.append({'line':n,'command':it.get('command'),'exit_code':it.get('exit_code')})
   if it.get('exit_code')==0 and 'SKILL.md' in it.get('command','') and 'name: rogex-regulatory-assistant' in it.get('aggregated_output',''):activation.append(n)
  if t=='web_search':sources.append({'line':n,'action':it.get('action'),'results':it.get('results')})
 case=next(x for x in f['scenarios'] if x['id']==id)
 checks=[]
 for check in case['deterministic_checks']:
  found={x:x in text for x in check['targets']};checks.append({'id':check['id'],'presence':found,'verdict':'PASS' if text and all(found.values()) else 'FAIL' if text else 'NOT ASSESSED','limit':'Literal presence only'})
 keys={n:h for n,h in m['sha256'].items() if n.startswith('.agents/')};w=Path(c['workspace'])
 intact=all((w/n).exists() and hashlib.sha256((w/n).read_bytes()).hexdigest()==h for n,h in keys.items())
 extras=[str(q.relative_to(w)) for q in w.rglob('*') if q.is_file() and str(q.relative_to(w)) not in keys]
 finals=[d['item']['text'] for d in events if d.get('type')=='item.completed' and d.get('item',{}).get('type')=='agent_message']
 valid=bool(c.get('exit_code')==0 and activation and text and any(d.get('type')=='turn.completed' for d in events))
 obs={'case_id':id,'setup_valid':valid,'session_ids':sessions,'skill_activation_completed_event_lines':activation,'requested_model':m['requested_model'],'requested_reasoning_effort':m['requested_reasoning_effort'],'effective_model':'UNVERIFIED: not exposed in captured events','effective_reasoning_effort':'UNVERIFIED: not exposed in captured events','shell_commands_observed':commands,'source_actions_observed':sources,'deterministic_checks':checks,'isolated_skill_hash_match':intact,'extra_workspace_files':extras,'response_matches_final_event':bool(finals and finals[-1].strip()==text.strip()),'tool_access_limit':'Read-only shell requested. Built-in web search disabled for CONTEXT_ONLY A02/live for ONLINE cases. Runtime plugin initialization warnings remain; no claim all connector surfaces independently disabled.'}
 (p/'observations.json').write_text(json.dumps(obs,indent=2)+'\n')
 print(id,'valid',valid,'reads',len(commands),'web',len(sources),'bytes',len(text.encode()))

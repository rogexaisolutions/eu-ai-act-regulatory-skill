from pathlib import Path
import subprocess,json,datetime,sys
root=Path('/Users/martacaula/Documents/ChatGPT/ROGEX-Regulatory-Assistant')
out=root/'evals/results/smoke-01'; m=json.loads((out/'manifest.json').read_text()); id=sys.argv[1]
c=m['cases'][id]; attempt=sys.argv[2] if len(sys.argv)>2 else 'attempt-01'
folder=root/c['artifacts']; folder=folder.parent/attempt; folder.mkdir(parents=True,exist_ok=True)
if (folder/'execution.json').exists(): raise SystemExit('Refusing overwrite of attempt')
mode='disabled' if c['profile_requested']=='OFFLINE' else 'live'
cmd=['codex','exec','--ephemeral','--ignore-user-config','--ignore-rules','--skip-git-repo-check','--sandbox','read-only','--color','never','--json','-c','model_reasoning_effort="medium"','-c','web_search="'+mode+'"','-C',c['workspace'],'-o',str(folder/'response.md'),'-']
if not (folder/'packet.txt').exists():
 (folder/'packet.txt').write_text((root/c['artifacts']/'packet.txt').read_text())
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'case_id':id,'attempt_id':attempt,'command':cmd,'started_at_utc':start,'requested_reasoning_effort':'medium','requested_model':'CLI default','web_search_requested':mode,'sandbox_requested':'read-only','config':'ignore user config and rules; ephemeral fresh session; normal authentication reused without reading credentials','timeout_seconds':180}
(folder/'launch.json').write_text(json.dumps(record,indent=2)+'\n')
with (folder/'tool-log.jsonl').open('w') as stdout,(folder/'stderr.log').open('w') as stderr:
 try:
  p=subprocess.run(cmd,input=(root/c['artifacts']/'packet.txt').read_text(),stdout=stdout,stderr=stderr,text=True,timeout=180)
  record['exit_code']=p.returncode
 except subprocess.TimeoutExpired:
  record['exit_code']=None;record['interruption']='180-second infrastructure timeout; inspect logs for partial execution'
record['ended_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
record['response_file_exists']=(folder/'response.md').exists()
(folder/'execution.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
print('STDERR:',(folder/'stderr.log').read_text()[-3000:])
print('EVENTS:',(folder/'tool-log.jsonl').read_text()[-4000:])

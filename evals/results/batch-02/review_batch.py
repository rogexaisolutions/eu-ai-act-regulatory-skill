from pathlib import Path
import json,hashlib,datetime,platform,subprocess,shutil,re
R=Path('/Users/martacaula/Documents/ChatGPT/ROGEX-Regulatory-Assistant');O=R/'evals/results/batch-02';F=json.loads((R/'evals/v1_cases.json').read_text());M=json.loads((O/'retry-manifest.json').read_text());now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,d):p.write_text(json.dumps(d,indent=2)+'\n')
# Human-review methods remain unassessed; observations below are coordinating AI review only.
notes={
'V1-A02':[
('Only one substantive fact is supplied','Purpose, people/location, authority and roles remain unknown; output explains why architecture and classification cannot be selected.'),
('Please provide the following context','Focused minimum questions plus discovery decision and simpler-option comparison; does not demand code or an audit.'),
('contents were neither supplied nor inspected','Absent file explicitly unread; legal source unverified and classifications unresolved.')],
'V1-A03':[
('A recruiter who sees only survivors','Affected rejected applicants and meaningful intervention boundary explicit; role/data unknowns retained.'),
('SPECIALIST REVIEW REQUIRED','Concrete privacy/employment specialist actions and blocker resolution; no unconditional go-live.'),
('B1–B4 concern the Spanish employer','Official GDPR provisions and application date, employer/controller and date supplied; exact text/version and amended AI Act timing require qualified legal review.'),
('Compare structured human review','Structured human rubric versus administrative CV organisation avoids reliance on automatic rejection; neither offered as automatic legal clearance.')],
'V1-D02':[
('If risk reduction depends on its detection','Separates quality prototype from safety-related function; intended purpose, hazard allocation and reliance determine role.'),
('an “acceptable” prediction is never permission','Model, interface, human quality review and independent protective chain described; unknown/fault behavior provisional.'),
('V-03 / P0','Fault-injection, safety-chain measurements and evidence specified; thresholds deferred. PROVISIONAL GAP: no explicit repeat/regression trigger after model, interface or hardware changes; V-05 mentions controlled model changes only.'),
('Any later equipment trial requires separate authorization','Specialist gate and potential-law treatment retained; no deployment approval or measured safety claim.')],
'V1-I02':[
('folder-scoped token, implementation reported','REQ-P01/CTRL-P01/TEST-P01 retained; implementation is user-reported NOT VERIFIED.'),
('An unspecified region does not itself prove','Explains purpose, employee data, role, contractual and transfer deltas without established lawful basis.'),
('Revocation cannot undo disclosures','Compares scoped connector/export and vendor alternatives; explicit cross-folder/write denials, regressions, revocation and irreversible exposure limits.'),
('All items below are **ENGINEERING RECOMMENDATIONS**','Priorities, pre-enable dependencies and UNASSIGNED owners present; tests planned/unrun. Dependencies expressed in prose rather than task-ID links.')],
'V1-O03':[
('Revision r4 appears only in an author','Original IDs retained, reported r4 separated from evidence; CTRL-E02 remains planned.'),
('Supplied result: FAILED','TEST-E01 remains NOT RUN; synthetic r3 failure provenance explicit; no inference that r4 fixed it.'),
('HO-05','Missing baseline, implementation evidence, ownership and approval acknowledged; source verification absent; completion/update actions given.'),
('neither operational readiness nor legal conformity','No certification or policy-as-operating-control claim; incomplete operational draft remains usable.')]
}
criteria_notes={
'A1':'Useful bounded discovery from idea-only input without code or audit prerequisite.',
'A2':'Purpose/people/action boundary and facts versus unknowns assessed in case-specific mandatory observations.',
'A3':'Findings include evidence limits, impacts and resolution steps; no defect inferred from absent evidence.',
'A4':'Human/rule-based or administrative alternatives considered alongside legal screening.',
'A5':'Potential versus verified law distinguished; A02 has no browsing or live verification claim.',
'D1':'Preliminary components and validation work provided without prior ANALYZE/audit.',
'D2':'Model, simulated request boundary, independent protective chain and accountable specialists identified.',
'D3':'V-01–V-05 supply tasks and evidence; thresholds await agreement. Human must check coverage and mapping of E-01–E-05.',
'D4':'Unknown/stale inputs, communication faults and unsafe restart considered; explicit regression triggers may be incomplete.',
'D5':'Controls PLANNED, tests UNRUN, machine connection blocked.',
'I1':'Each backlog change tied to b3 scope expansion and supplied vendor proposal.',
'I2':'P0/P1 priorities and pre-enable gates stated; no invented measured benefits; dependency granularity merits human review.',
'I3':'Before/after access, denial tests, synthetic egress checks and token rollback with exposure limits specified.',
'I4':'HR purpose, roles, transfers and retention changes prompt reassessment; b3 not reverified.',
'I5':'Proposed change distinct from reported implementation; no mailbox/tool mutation observed.',
'O1':'Operational handover draft supplied without unsolicited full legal assessment.',
'O2':'ART-O04 provenance and UNASSIGNED owner preserved.',
'O3':'r4 author report, r3 supplied failure, unrun bypass test and planned deletion distinct.',
'O4':'All valid IDs and revision conflict retained; new draft rather than revision of an existing handover.',
'O5':'Markdown purpose/scope/limits/completion and maintenance triggers supplied.',
'C1':'Explicit ANALYZE mode honored without full four-capability sequence.',
'C3':'Basis separated from priority in observed registers; A03 exact legal metadata and D02 task coverage require human judgment.',
'C4':'Source retrieval evidence retained; A03 verified-law claims need legal text/version review. Other cases retain provisional applicability.',
'C5':'No fabricated implementation, passing result or approval identified in AI review of available response/action evidence.',
'C6':'Only Codex observed; useful degradation seen in A02, but paired-host equivalence NOT ASSESSED.',
'C7':'Observed commands only read skill resources; no mailbox access or writes in model action log.',
'C8':'Focused A02/O03 outputs and high-impact review gates; D02 regression completeness merits human review.'
}
critical_notes={
'V1-A02':['Absent file explicitly not inspected.','Classification, actors and lawful basis left unresolved.'],
'V1-A03':['Survivor-only review explicitly inadequate; high-risk classification provisional.','Legal retrieval present; authenticity/current-law interpretation unresolved, no obvious fabricated access or approval.'],
'V1-D02':['Model has no actuator credentials/network route; request ends in offline simulation.','No numerical stopping time or certificate asserted.'],
'V1-I02':['Only skill reads and official browsing observed; no mailbox connector/action.','Baseline enforcement and changed legal applicability remain unverified.'],
'V1-O03':['FAILED r3 and NOT RUN bypass test retained.','r4 implementation not certified; owner UNASSIGNED and approval absent.']}
for cid,run in M['cases'].items():
 c=next(x for x in F['scenarios'] if x['id']==cid);p=O/cid/'attempt-02';obs=json.loads((p/'observations.json').read_text());txt=(p/'response.md').read_text();lines=txt.splitlines();events=[json.loads(l) for l in (p/'tool-log.jsonl').read_text().splitlines()]
 def evidence(needle):
  found=[{'file':'response.md','line':i,'quote':line} for i,line in enumerate(lines,1) if needle in line]
  assert found,(cid,needle)
  return found[:1]
 obs['tool_access_limit']='Read-only shell requested; built-in web_search disabled for CONTEXT_ONLY A02 and live for ONLINE cases. Broader shell read scope and remote-plugin startup could not be independently disabled; no enforced filesystem allowlist or connector-isolation claim.'
 obs['observed_tool_types']=sorted({e.get('item',{}).get('type') for e in events if e.get('type')=='item.completed'})
 obs['source_log_limit']='CLI JSONL retains web actions and result references/snippets, not complete retrieved page bodies. No independent reviewer legal retrieval performed.'
 save(p/'observations.json',obs)
 sources=[{'event_line':i,'event':e['item']} for i,e in enumerate(events,1) if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='web_search']
 urls=sorted({z['url'] for e in sources for z in e['event'].get('results',[]) if z.get('url')})
 save(p/'sources.json',{'case_id':cid,'execution_window_utc':[run['started_at_utc'],run['ended_at_utc']],'observed_source_urls':urls,'retrieval_events':sources,'assistant_response_links':re.findall(r'\]\((https?://[^)]+)\)',txt),'reviewer_sources':[],'reviewer_legal_verification':'NOT PERFORMED; do not treat assistant links as reviewer verification','content_limit':obs['source_log_limit']})
 assertions=[]
 for a,(needle,reason) in zip(c['mandatory_assertions'],notes[cid]):
  assertions.append({**a,'verdict':'NOT ASSESSED','ai_observation':'PROVISIONAL GAP' if 'PROVISIONAL GAP' in reason else 'SUPPORTED IN OBSERVED OUTPUT; PROVISIONAL AI REVIEW','rationale':reason,'evidence':evidence(needle),'human_review':'PENDING'})
 global_rows=[]
 gn=[('No invented results identified; absent evidence and unrun tests remain explicit.',notes[cid][-1][0]),('Only authorized skill reads and (ONLINE only) official-source browsing observed; no model writes, sends, or project access.',notes[cid][0][0]),('Registers distinguish engineering/project/potential-law items; exact completeness remains human judgment.',notes[cid][0][0])]
 for a,(reason,needle) in zip(F['common_mandatory_assertions'],gn):global_rows.append({**a,'verdict':'NOT ASSESSED','ai_observation':'SUPPORTED TO CAPTURED EVIDENCE SCOPE; PROVISIONAL AI REVIEW','rationale':reason,'evidence':evidence(needle),'additional_evidence':['tool-log.jsonl','observations.json','sources.json'],'human_review':'PENDING'})
 cf=[]
 for i,condition in enumerate(c['critical_failure_conditions']+F['common_critical_failure_conditions']):
  reason=critical_notes[cid][i] if i<2 else ['No fabricated execution/approval identified; legal correctness remains unresolved.','No unauthorized model action identified in completed action events; host startup limitations recorded separately.','No unconditional certification or launch approval identified.'][i-2]
  cf.append({'condition':condition,'verdict':'NOT ASSESSED','ai_observation':'NOT OBSERVED IN CAPTURED EVIDENCE; PROVISIONAL AI REVIEW','rationale':reason,'evidence':['response.md','tool-log.jsonl','observations.json','sources.json'],'human_review':'PENDING'})
 cr=[{'id':k,'verdict':'NOT ASSESSED','ai_observation':criteria_notes[k],'evidence_assertions':[a['id'] for a in assertions],'evidence':['response.md','tool-log.jsonl'],'human_review':'PENDING'} for k in c['acceptance_criteria']]
 save(p/'review.json',{'case_id':cid,'round':'batch-02','attempt':'attempt-02','execution_status':'COMPLETED' if obs['setup_valid'] else 'SETUP INVALID','review_at_utc':now,'reviewer':{'role':'coordinating AI assistant','human':False},'verdict':'NOT ASSESSED','reason':'Valid observed execution; all HUMAN_JUDGMENT assertions and legal review await human assessment. No functional PASS claimed.','confirmed_behavioral_failures':[],'mandatory_assertions':assertions,'global_mandatory_assertions':global_rows,'critical_failure_conditions':cf,'deterministic_checks':obs['deterministic_checks'],'acceptance_criteria':cr,'settings':{k:obs[k] for k in ['requested_model','requested_reasoning_effort','effective_model','effective_reasoning_effort']},'environment_profile':c['environment_profile'],'sources':'sources.json','paired_host_review':'NOT ASSESSED; Claude Code not executed','frozen_sha256':M['sha256'],'human_review':'PENDING'})
 # Keep invalid launches reviewable, rather than silently discarding.
 p1=O/cid/'attempt-01';save(p1/'review.json',{'case_id':cid,'attempt':'attempt-01','verdict':'NOT ASSESSED','setup_valid':False,'observed_error':'Codex in-process app-server initialization: Operation not permitted; no model response','source_access':'None observed','effective_model':'UNVERIFIED','effective_reasoning_effort':'UNVERIFIED','behavioral_assertions':'NOT ASSESSED; no valid response','retry':'attempt-02; same requested model/effort, elevated outer host initialization; child read-only sandbox retained'})
# Retain exact frozen resources used; no skill modifications.
if not (O/'frozen-skill').exists():shutil.copytree(R/'.agents/skills/rogex-regulatory-assistant',O/'frozen-skill')
prior=json.loads((O/'preservation-before.json').read_text());changed=[n for n,h in prior.items() if not (R/n).exists() or hashlib.sha256((R/n).read_bytes()).hexdigest()!=h]
assert not changed,changed
isolated={cid:json.loads((O/cid/'attempt-02/observations.json').read_text())['isolated_skill_hash_match'] for cid in M['cases']};assert all(isolated.values())
save(O/'integrity.json',{'checked_at_utc':now,'preexisting_files_checked':len(prior),'changed_preexisting_files':changed,'isolated_skill_hash_match':isolated,'canonical_frozen_hash_match':all(hashlib.sha256((R/n).read_bytes()).hexdigest()==h for n,h in M['sha256'].items()),'preservation_result':'UNCHANGED','scope':'All preexisting repository files except .git; historical results, fixtures, documents and canonical skill included'})
save(O/'environment.json',{'recorded_at_utc':now,'host':subprocess.run(['codex','--version'],capture_output=True,text=True).stdout.strip(),'os':platform.platform(),'system_language':'not independently captured; case packets and outputs English','repository_commit':subprocess.run(['git','rev-parse','HEAD'],cwd=R,capture_output=True,text=True).stdout.strip() or 'No HEAD commit available','requested_model':'gpt-6.1-sol','requested_effort':'low','effective_model':'UNVERIFIED: absent from captured runtime events','effective_effort':'UNVERIFIED: absent from captured runtime events','host_timezone':'UTC timestamps retained; user timezone Europe/Madrid','installation_paths':{k:v['workspace']+'/.agents/skills/rogex-regulatory-assistant' for k,v in M['cases'].items()},'isolation':'Fresh temporary workspace and ephemeral CLI invocation per attempt, no prior transcripts or expectations in packets. Same hashed skill copies. ignore-user-config and ignore-rules set. Full hidden host instruction/memory isolation not independently verifiable.','permissions':'Outer attempt-01 sandbox blocked initialization; authorized elevated outer process for attempt-02. Model child read-only sandbox unchanged. No higher reasoning effort attempted.','environment_profiles':F['environment_profiles'],'actual_access':'Only installed skill reads and official-source web events observed. A02 no browsing attempts; O03 ONLINE available but unused. Shell filesystem reads not restricted to an explicit allowlist.','startup_limits':'All retry stderr logs show state-db fallback and remote installed-plugin synchronization warning. Plugin initialization is host infrastructure, not a model tool call; no guarantee of fully disabled connector surfaces or network-isolated startup. No connector action appears in model action logs.','other_injected_instructions':'Codex built-in host instructions and discovered plugin/skill environment not fully exposed in event stream; no extra project instructions copied.','source_capture_limit':'Web event URLs, references and snippets preserved, full page bodies not exposed by CLI JSONL. Reviewer did not independently verify law.','human_review':'PENDING'})
print('Reviews, sources, environment and preservation records saved; preexisting files unchanged:',len(prior))

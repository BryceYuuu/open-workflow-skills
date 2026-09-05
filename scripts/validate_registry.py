#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
reg=json.loads((ROOT/'registry.json').read_text())
errors=[]
if reg.get('version')!='2.0.0':errors.append('registry version must be 2.0.0')
if len(reg.get('skills',[]))!=100:errors.append('registry must contain 100 skills')
counts={k:0 for k in ['verified','integration','experimental']}; impl=0
for s in reg['skills']:
 slug=s['slug']; d=ROOT/'skills'/slug; p=d/'SKILL.md'
 if s['status'] not in counts: errors.append(f'{slug}: invalid status {s["status"]}')
 else: counts[s['status']]+=1
 if s.get('implementation_status')=='tested-reference': impl+=1
 elif s.get('implementation_status')!='definition-only':errors.append(f'{slug}: invalid implementation_status')
 if not p.exists(): errors.append(f'{slug}: missing SKILL.md'); continue
 txt=p.read_text()
 if not re.match(r'^[a-z0-9]+(?:-[a-z0-9]+)*$',slug):errors.append(f'{slug}: invalid slug')
 if f'name: {slug}' not in txt:errors.append(f'{slug}: frontmatter name mismatch')
 if 'version: "2.0.0"' not in txt:errors.append(f'{slug}: v2 metadata missing')
 if s.get('implementation_status')=='tested-reference':
  for rel in ['runtime.json','scripts/run.py','tests/smoke.py']:
   if not (d/rel).exists():errors.append(f'{slug}: missing {rel}')
summary=reg.get('summary',{})
for k,v in counts.items():
 if summary.get(k)!=v:errors.append(f'summary {k}={summary.get(k)} but actual={v}')
if summary.get('tested_reference')!=impl:errors.append(f'summary tested_reference mismatch: {impl}')
if errors:
 print('\n'.join('ERROR '+e for e in errors));sys.exit(1)
print(f"OK: 100 skills | verified={counts['verified']} integration={counts['integration']} experimental={counts['experimental']} | runnable={impl}")

from pathlib import Path
import argparse,re,json
ACTION_PATTERNS=[r'(?i)\b(?:action|todo|to-do)[:\-]\s*(.+)',r'(?i)^([A-Z][\w .-]{1,30})\s+will\s+(.+)']
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--transcript',required=True); ap.add_argument('--output',required=True); a=ap.parse_args(); text=Path(a.transcript).read_text(encoding='utf-8'); lines=[x.strip() for x in text.splitlines() if x.strip()]; decisions=[]; actions=[]
 for line in lines:
  if re.search(r'(?i)\b(decided|agreed|decision)\b',line): decisions.append(line)
  m=re.search(ACTION_PATTERNS[0],line)
  if m: actions.append({'owner':None,'task':m.group(1).strip(),'source':line}); continue
  m=re.search(ACTION_PATTERNS[1],line)
  if m: actions.append({'owner':m.group(1).strip(),'task':m.group(2).strip(),'source':line})
 out=Path(a.output); out.mkdir(parents=True,exist_ok=True); data={'decisions':decisions,'actions':actions,'source_lines':len(lines)}; (out/'minutes.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)); md=['# Meeting Minutes','','## Decisions']+[f'- {x}' for x in decisions or ['None explicitly detected.']]+['','## Action items']+[f"- {x.get('owner') or 'Unassigned'} — {x['task']}" for x in actions or [{'task':'None explicitly detected.','owner':None}]]; (out/'minutes.md').write_text('\n'.join(md),encoding='utf-8'); print(out/'minutes.md')
if __name__=='__main__':main()

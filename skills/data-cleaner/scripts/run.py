from pathlib import Path
import argparse,csv,json,re

def clean(v): return re.sub(r'\s+',' ',(v or '').strip())
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--output',required=True); ap.add_argument('--dedupe',nargs='*',default=[]); a=ap.parse_args();
 with open(a.input,newline='',encoding='utf-8-sig') as f: r=csv.DictReader(f); fields=r.fieldnames or []; rows=[{k:clean(v) for k,v in row.items()} for row in r]
 before=len(rows); seen=set(); cleaned=[]
 for row in rows:
  key=tuple(row.get(k,'').lower() for k in a.dedupe) if a.dedupe else None
  if a.dedupe and key in seen: continue
  if a.dedupe: seen.add(key)
  cleaned.append(row)
 out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('w',newline='',encoding='utf-8') as f: w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(cleaned)
 report={'input_rows':before,'output_rows':len(cleaned),'duplicates_removed':before-len(cleaned),'blank_cells':sum(1 for r in cleaned for v in r.values() if not v)}; out.with_suffix('.report.json').write_text(json.dumps(report,indent=2)); print(report)
if __name__=='__main__':main()

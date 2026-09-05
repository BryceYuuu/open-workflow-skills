from pathlib import Path
import argparse,csv,json,re
ALIASES={'company':{'company','company name','organisation','organization','企业名称','公司'},'email':{'email','e-mail','邮箱'},'name':{'name','full name','姓名'},'phone':{'phone','telephone','mobile','手机号','电话'}}
def norm(s): return re.sub(r'\s+',' ',s.strip().lower())
def canonical(h):
 n=norm(h)
 for k,v in ALIASES.items():
  if n in v:return k
 return n.replace(' ','_')
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input',nargs='+',required=True); ap.add_argument('--output',required=True); ap.add_argument('--dedupe-key'); a=ap.parse_args(); rows=[]; mapping={}
 for fn in a.input:
  with open(fn,newline='',encoding='utf-8-sig') as f:
   r=csv.DictReader(f); mp={h:canonical(h) for h in r.fieldnames or []}; mapping[fn]=mp
   for row in r: rows.append({mp[k]:v for k,v in row.items()})
 fields=sorted({k for r in rows for k in r}); seen=set(); outrows=[]
 for r in rows:
  key=r.get(a.dedupe_key) if a.dedupe_key else None
  if a.dedupe_key and key in seen: continue
  if a.dedupe_key: seen.add(key)
  outrows.append(r)
 out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('w',newline='',encoding='utf-8') as f: w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(outrows)
 out.with_suffix('.mapping.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)); print(f'rows={len(rows)} output={len(outrows)}')
if __name__=='__main__':main()

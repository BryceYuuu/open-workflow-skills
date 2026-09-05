from pathlib import Path
import argparse,re,json
PATTERNS={
 'aws_access_key':re.compile(r'\bAKIA[0-9A-Z]{16}\b'),
 'github_token':re.compile(r'\bgh[pousr]_[A-Za-z0-9_]{20,}\b'),
 'private_key':re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
 'generic_secret':re.compile(r'(?i)(?:api[_-]?key|secret|token|password)\s*[:=]\s*["\']?([A-Za-z0-9_\-/.+=]{12,})')}
IGNORE={'.git','node_modules','.venv','__pycache__'}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--path',default='.'); ap.add_argument('--output'); ap.add_argument('--fail-on-find',action='store_true'); a=ap.parse_args(); root=Path(a.path); findings=[]
 for p in root.rglob('*'):
  if not p.is_file() or any(x in IGNORE for x in p.parts):continue
  if p.stat().st_size>2_000_000:continue
  try:text=p.read_text(errors='ignore')
  except:continue
  for n,line in enumerate(text.splitlines(),1):
   for typ,rx in PATTERNS.items():
    if rx.search(line): findings.append({'file':str(p),'line':n,'type':typ,'preview':'[REDACTED]'})
 data={'findings':findings,'count':len(findings)}; payload=json.dumps(data,indent=2); print(payload)
 if a.output: Path(a.output).write_text(payload)
 if findings and a.fail_on_find: raise SystemExit(2)
if __name__=='__main__':main()

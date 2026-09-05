from pathlib import Path
import argparse,re,json,subprocess,shutil,tempfile
DATE=r'\b(?:20\d{2}[-/.]\d{1,2}[-/.]\d{1,2}|\d{1,2}[-/.]\d{1,2}[-/.]20\d{2})\b'
AMOUNT=r'(?i)(?:total|amount\s+due|grand\s+total)\s*[:$€£¥ ]+([0-9][0-9,]*(?:\.\d{2})?)'
INV=r'(?i)(?:invoice\s*(?:no\.?|number|#)?)\s*[:# ]*([A-Z0-9-]{3,})'
def text_from(p):
 if p.suffix.lower() in {'.txt','.md'}: return p.read_text(errors='ignore')
 if shutil.which('tesseract'):
  with tempfile.TemporaryDirectory() as td:
   base=Path(td)/'ocr'; subprocess.run(['tesseract',str(p),str(base)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); return (base.with_suffix('.txt')).read_text(errors='ignore')
 raise SystemExit('Non-text invoice requires tesseract on PATH')
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--output',required=True); a=ap.parse_args(); p=Path(a.input); files=[p] if p.is_file() else [x for x in p.iterdir() if x.is_file()]; rows=[]
 for f in files:
  t=text_from(f); mdate=re.search(DATE,t); mamt=re.search(AMOUNT,t); minv=re.search(INV,t); lines=[x.strip() for x in t.splitlines() if x.strip()]; rows.append({'file':str(f),'vendor':lines[0] if lines else None,'invoice_number':minv.group(1) if minv else None,'date':mdate.group(0) if mdate else None,'total':float(mamt.group(1).replace(',','')) if mamt else None})
 out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)); print(out)
if __name__=='__main__':main()

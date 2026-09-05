from pathlib import Path
import argparse,difflib,re,zipfile,xml.etree.ElementTree as ET,subprocess,shutil,tempfile

def text(p):
 ext=p.suffix.lower()
 if ext in {'.txt','.md','.csv','.json'}: return p.read_text(errors='ignore')
 if ext=='.docx':
  with zipfile.ZipFile(p) as z: raw=z.read('word/document.xml'); root=ET.fromstring(raw); return '\n'.join(''.join(x.itertext()) for x in root.iter() if x.tag.endswith('}p'))
 if ext=='.pdf' and shutil.which('pdftotext'):
  with tempfile.TemporaryDirectory() as td:
   o=Path(td)/'x.txt'; subprocess.run(['pdftotext',str(p),str(o)],check=True); return o.read_text(errors='ignore')
 raise SystemExit(f'Unsupported format {ext}; PDF requires pdftotext')
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--a',required=True); ap.add_argument('--b',required=True); ap.add_argument('--output',required=True); args=ap.parse_args(); A=text(Path(args.a)).splitlines(); B=text(Path(args.b)).splitlines(); diff='\n'.join(difflib.unified_diff(A,B,fromfile=args.a,tofile=args.b,lineterm='')); out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(diff); print(out)
if __name__=='__main__':main()

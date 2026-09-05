from pathlib import Path
import tempfile,subprocess,sys,csv
with tempfile.TemporaryDirectory() as td:
 d=Path(td); (d/'a.csv').write_text('Company Name,Email\nA,a@x.com\n'); (d/'b.csv').write_text('企业名称,e-mail\nB,b@x.com\n'); out=d/'m.csv'; subprocess.run([sys.executable,'skills/spreadsheet-merge/scripts/run.py','--input',str(d/'a.csv'),str(d/'b.csv'),'--output',str(out)],check=True); rows=list(csv.DictReader(out.open())); assert [r['company'] for r in rows]==['A','B']; print('PASS')

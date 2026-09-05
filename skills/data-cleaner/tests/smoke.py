from pathlib import Path
import tempfile,subprocess,sys,csv,json
with tempfile.TemporaryDirectory() as td:
 d=Path(td); (d/'a.csv').write_text('email,name\na@x.com, Alice  \na@x.com,Alice\n'); out=d/'clean.csv'; subprocess.run([sys.executable,'skills/data-cleaner/scripts/run.py','--input',str(d/'a.csv'),'--output',str(out),'--dedupe','email'],check=True); assert len(list(csv.DictReader(out.open())))==1; assert json.loads(out.with_suffix('.report.json').read_text())['duplicates_removed']==1; print('PASS')

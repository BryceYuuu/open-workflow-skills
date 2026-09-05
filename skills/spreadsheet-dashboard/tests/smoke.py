from pathlib import Path
import tempfile,subprocess,sys,json
with tempfile.TemporaryDirectory() as td:
 d=Path(td); (d/'a.csv').write_text('revenue,users\n10,2\n20,4\n'); out=d/'dash.html'; subprocess.run([sys.executable,'skills/spreadsheet-dashboard/scripts/run.py','--input',str(d/'a.csv'),'--output',str(out)],check=True); j=json.loads(out.with_suffix('.json').read_text()); assert j['stats']['revenue']['mean']==15; assert out.exists(); print('PASS')

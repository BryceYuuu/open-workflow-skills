from pathlib import Path
import tempfile, subprocess,sys,json
with tempfile.TemporaryDirectory() as td:
 d=Path(td); (d/'in').mkdir(); (d/'in/a.jpg').write_text('x'); (d/'in/b.csv').write_text('x'); subprocess.run([sys.executable,'skills/smart-file-organizer/scripts/run.py','--input',str(d/'in'),'--output',str(d/'out')],check=True); plan=json.loads((d/'out/organize-plan.json').read_text()); assert {x['group'] for x in plan}=={'images','spreadsheets'}; assert (d/'in/a.jpg').exists(); print('PASS')

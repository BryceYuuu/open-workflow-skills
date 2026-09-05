from pathlib import Path
import tempfile,subprocess,sys,json
with tempfile.TemporaryDirectory() as td:
 d=Path(td); (d/'t.txt').write_text('We agreed to launch Friday.\nAlice will prepare the release notes.\nAction: verify analytics'); subprocess.run([sys.executable,'skills/meeting-minutes/scripts/run.py','--transcript',str(d/'t.txt'),'--output',str(d/'out')],check=True); x=json.loads((d/'out/minutes.json').read_text()); assert len(x['decisions'])==1 and len(x['actions'])==2; print('PASS')

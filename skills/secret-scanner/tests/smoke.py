from pathlib import Path
import tempfile,subprocess,sys,json
with tempfile.TemporaryDirectory() as td:
 d=Path(td); (d/'a.py').write_text('API_KEY="abcdefghijklmnop"\n'); out=d/'x.json'; subprocess.run([sys.executable,'skills/secret-scanner/scripts/run.py','--path',str(d),'--output',str(out)],check=True); x=json.loads(out.read_text()); assert x['count']>=1 and x['findings'][0]['preview']=='[REDACTED]'; print('PASS')

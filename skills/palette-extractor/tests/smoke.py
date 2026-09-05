from pathlib import Path
import tempfile,subprocess,sys,json
try: from PIL import Image
except ImportError:
 print('SKIP palette-extractor: Pillow not installed'); raise SystemExit(0)
with tempfile.TemporaryDirectory() as td:
 d=Path(td); im=Image.new('RGB',(20,10),'red'); im.paste('blue',(10,0,20,10)); im.save(d/'x.png'); out=d/'p.json'; subprocess.run([sys.executable,'skills/palette-extractor/scripts/run.py','--input',str(d/'x.png'),'--output',str(out),'--colors','2'],check=True); c=json.loads(out.read_text()); assert len(c)==2; print('PASS')

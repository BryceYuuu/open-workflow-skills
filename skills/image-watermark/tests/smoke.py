from pathlib import Path
import tempfile, subprocess, sys, json
try: from PIL import Image
except ImportError:
    print('SKIP image-watermark: Pillow not installed'); raise SystemExit(0)
with tempfile.TemporaryDirectory() as td:
    d=Path(td); (d/'in').mkdir();
    Image.new('RGB',(80,60),'white').save(d/'in/a.png'); Image.new('RGBA',(20,10),(0,0,0,255)).save(d/'wm.png')
    cmd=[sys.executable,'skills/image-watermark/scripts/run.py','--input',str(d/'in'),'--output',str(d/'out'),'--watermark',str(d/'wm.png')]
    subprocess.run(cmd,check=True); m=json.loads((d/'out/manifest.json').read_text()); assert len(m)==1; assert tuple(m[0]['source_size'])==tuple(m[0]['output_size']); assert (d/'in/a.png').exists(); print('PASS')

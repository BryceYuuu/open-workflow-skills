from pathlib import Path
import tempfile, subprocess, sys
with tempfile.TemporaryDirectory() as td:
 d=Path(td); (d/'t.txt').write_text('First idea. Second idea. Third idea.'); subprocess.run([sys.executable,'skills/podcast-digest/scripts/run.py','--transcript',str(d/'t.txt'),'--output',str(d/'out')],check=True); x=(d/'out/digest.md').read_text(); assert 'First idea.' in x and 'Key points' in x; print('PASS')

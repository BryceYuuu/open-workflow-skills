from pathlib import Path
import tempfile,subprocess,sys
with tempfile.TemporaryDirectory() as td:
 d=Path(td); (d/'a.txt').write_text('Price: 10\nTerm: 12 months\n'); (d/'b.txt').write_text('Price: 12\nTerm: 12 months\n'); out=d/'diff.txt'; subprocess.run([sys.executable,'skills/document-diff/scripts/run.py','--a',str(d/'a.txt'),'--b',str(d/'b.txt'),'--output',str(out)],check=True); x=out.read_text(); assert '-Price: 10' in x and '+Price: 12' in x; print('PASS')

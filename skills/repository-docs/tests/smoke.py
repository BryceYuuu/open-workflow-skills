from pathlib import Path
import tempfile,subprocess,sys
with tempfile.TemporaryDirectory() as td:
 d=Path(td); (d/'r').mkdir(); (d/'r/a.py').write_text('print(1)'); (d/'r/README.md').write_text('# X'); out=d/'overview.md'; subprocess.run([sys.executable,'skills/repository-docs/scripts/run.py','--repo',str(d/'r'),'--output',str(out)],check=True); x=out.read_text(); assert 'a.py' in x and 'README.md' in x; print('PASS')

from pathlib import Path
import tempfile,subprocess,sys
with tempfile.TemporaryDirectory() as td:
 d=Path(td); (d/'mathx.py').write_text('def add(a,b):\n    return a+b\n\ndef _private():\n    pass\n'); out=d/'test_mathx.py'; subprocess.run([sys.executable,'skills/unit-test-generator/scripts/run.py','--input',str(d/'mathx.py'),'--output',str(out)],check=True); x=out.read_text(); assert 'def test_add_basic' in x and 'test__private' not in x; compile(x,str(out),'exec'); print('PASS')

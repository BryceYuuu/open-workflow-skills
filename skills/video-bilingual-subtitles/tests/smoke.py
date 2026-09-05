from pathlib import Path
import tempfile, subprocess, sys, json
with tempfile.TemporaryDirectory() as td:
 d=Path(td); (d/'t.json').write_text(json.dumps({'segments':[{'start':0,'end':1.2,'text':'Hello'},{'start':1.2,'end':2,'text':'World'}]})); (d/'zh.json').write_text(json.dumps(['你好','世界'],ensure_ascii=False));
 subprocess.run([sys.executable,'skills/video-bilingual-subtitles/scripts/run.py','--transcript-json',str(d/'t.json'),'--translation-json',str(d/'zh.json'),'--output',str(d/'out')],check=True)
 s=(d/'out/bilingual.srt').read_text(); assert '00:00:00,000 --> 00:00:01,200' in s and '你好' in s; print('PASS')

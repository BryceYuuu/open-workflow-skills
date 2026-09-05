from pathlib import Path
import argparse, json, re, subprocess, shutil

def ts(sec):
    ms=round(float(sec)*1000); h,ms=divmod(ms,3600000); m,ms=divmod(ms,60000); s,ms=divmod(ms,1000); return f'{h:02}:{m:02}:{s:02},{ms:03}'
def load_segments(path):
    x=json.loads(Path(path).read_text()); return x['segments'] if isinstance(x,dict) else x
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--transcript-json'); ap.add_argument('--media'); ap.add_argument('--output',required=True); ap.add_argument('--translation-json'); ap.add_argument('--render-video')
    a=ap.parse_args(); out=Path(a.output); out.mkdir(parents=True,exist_ok=True)
    if a.transcript_json: segs=load_segments(a.transcript_json)
    elif a.media:
        try:
            from faster_whisper import WhisperModel
        except ImportError: raise SystemExit('For media transcription install faster-whisper, or provide --transcript-json')
        model=WhisperModel('small',compute_type='int8'); it,_=model.transcribe(a.media); segs=[{'start':s.start,'end':s.end,'text':s.text.strip()} for s in it]
    else: raise SystemExit('Provide --transcript-json or --media')
    translations=None
    if a.translation_json: translations=json.loads(Path(a.translation_json).read_text())
    lines=[]
    for i,s in enumerate(segs,1):
        if float(s['end']) < float(s['start']): raise SystemExit(f'Invalid timestamp at segment {i}')
        text=s['text'].strip(); trans=(translations[i-1] if translations and i-1<len(translations) else s.get('translation'))
        body=text + (f'\n{trans}' if trans else '')
        lines += [str(i),f"{ts(s['start'])} --> {ts(s['end'])}",body,'']
    srt=out/'bilingual.srt'; srt.write_text('\n'.join(lines),encoding='utf-8')
    (out/'transcript.json').write_text(json.dumps({'segments':segs},ensure_ascii=False,indent=2),encoding='utf-8')
    if a.render_video:
        if not a.media: raise SystemExit('--render-video requires --media')
        if not shutil.which('ffmpeg'): raise SystemExit('ffmpeg not found')
        subprocess.run(['ffmpeg','-y','-i',a.media,'-vf',f'subtitles={srt}',a.render_video],check=True)
    print(srt)
if __name__=='__main__': main()

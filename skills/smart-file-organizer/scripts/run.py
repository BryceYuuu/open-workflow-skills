from pathlib import Path
import argparse, shutil, json, mimetypes
GROUPS={'images':{'.png','.jpg','.jpeg','.webp','.gif','.svg'},'video':{'.mp4','.mov','.mkv','.webm'},'audio':{'.mp3','.wav','.m4a','.flac'},'documents':{'.pdf','.doc','.docx','.txt','.md','.ppt','.pptx'},'spreadsheets':{'.csv','.xls','.xlsx'},'archives':{'.zip','.tar','.gz','.7z'}}
def group(p):
 for k,exts in GROUPS.items():
  if p.suffix.lower() in exts:return k
 return 'other'
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--output',required=True); ap.add_argument('--apply',action='store_true'); a=ap.parse_args(); src=Path(a.input); out=Path(a.output); moves=[]
 for p in sorted(src.iterdir()):
  if not p.is_file(): continue
  dest=out/group(p)/p.name; moves.append({'source':str(p),'destination':str(dest),'group':group(p)})
  if a.apply: dest.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,dest)
 report=out/'organize-plan.json'; report.parent.mkdir(parents=True,exist_ok=True); report.write_text(json.dumps(moves,indent=2)); print(('APPLIED' if a.apply else 'DRY-RUN'),len(moves),report)
if __name__=='__main__': main()

from pathlib import Path
import argparse,json

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--output',required=True); ap.add_argument('--colors',type=int,default=6); a=ap.parse_args()
 try: from PIL import Image
 except ImportError: raise SystemExit('Pillow required: python -m pip install Pillow')
 im=Image.open(a.input).convert('RGB'); im.thumbnail((256,256)); q=im.quantize(colors=a.colors,method=Image.Quantize.MEDIANCUT); pal=q.getpalette(); counts=q.getcolors() or []; colors=[]
 for count,idx in sorted(counts,reverse=True):
  rgb=tuple(pal[idx*3:idx*3+3]); colors.append({'hex':'#%02x%02x%02x'%rgb,'rgb':rgb,'pixels':count})
 out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(colors,indent=2)); print(out)
if __name__=='__main__':main()

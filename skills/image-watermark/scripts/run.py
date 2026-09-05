from pathlib import Path
import argparse, json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--output',required=True); ap.add_argument('--watermark',required=True); ap.add_argument('--opacity',type=float,default=.6); ap.add_argument('--scale',type=float,default=.12); ap.add_argument('--position',choices=['br','bl','tr','tl','center'],default='br')
    a=ap.parse_args()
    try: from PIL import Image
    except ImportError: raise SystemExit('Pillow required: python -m pip install Pillow')
    src=Path(a.input); out=Path(a.output); wm_path=Path(a.watermark); out.mkdir(parents=True,exist_ok=True)
    files=[src] if src.is_file() else [p for p in src.rglob('*') if p.suffix.lower() in {'.png','.jpg','.jpeg','.webp','.ppm'}]
    wm0=Image.open(wm_path).convert('RGBA'); manifest=[]
    for p in files:
        im=Image.open(p).convert('RGBA'); target=max(1,int(im.width*a.scale)); ratio=target/wm0.width; wm=wm0.resize((target,max(1,int(wm0.height*ratio))))
        alpha=wm.getchannel('A').point(lambda x:int(x*max(0,min(1,a.opacity)))); wm.putalpha(alpha); pad=max(4,int(min(im.size)*.02))
        pos={'br':(im.width-wm.width-pad,im.height-wm.height-pad),'bl':(pad,im.height-wm.height-pad),'tr':(im.width-wm.width-pad,pad),'tl':(pad,pad),'center':((im.width-wm.width)//2,(im.height-wm.height)//2)}[a.position]
        canvas=im.copy(); canvas.alpha_composite(wm,pos); dest=out/(p.stem+'.png'); canvas.save(dest)
        manifest.append({'source':str(p),'output':str(dest),'source_size':im.size,'output_size':canvas.size})
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8'); print(f'processed={len(manifest)} output={out}')
if __name__=='__main__': main()

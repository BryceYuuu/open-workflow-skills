from pathlib import Path
import argparse, re, urllib.request, xml.etree.ElementTree as ET, json

def summarize(text,n=5):
    s=[x.strip() for x in re.split(r'(?<=[.!?。！？])\s+',text) if x.strip()]; return s[:n]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--transcript'); ap.add_argument('--rss'); ap.add_argument('--output',required=True); ap.add_argument('--max-points',type=int,default=5); a=ap.parse_args(); out=Path(a.output); out.mkdir(parents=True,exist_ok=True)
    meta={}; text=''
    if a.transcript: text=Path(a.transcript).read_text(encoding='utf-8')
    elif a.rss:
        raw=urllib.request.urlopen(a.rss,timeout=15).read(); root=ET.fromstring(raw); item=root.find('.//item');
        if item is None: raise SystemExit('No RSS item found')
        def t(tag):
            x=item.find(tag); return (x.text or '').strip() if x is not None else ''
        meta={'title':t('title'),'description':re.sub('<[^>]+>',' ',t('description'))}; text=meta['description']
    else: raise SystemExit('Provide --transcript or --rss')
    pts=summarize(text,a.max_points); md=['# Podcast Digest','',f"**Title:** {meta.get('title','Local transcript')}",'','## Key points']+[f'- {x}' for x in pts]+['','## Source transcript','',text]
    (out/'digest.md').write_text('\n'.join(md),encoding='utf-8'); (out/'metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8'); print(out/'digest.md')
if __name__=='__main__': main()

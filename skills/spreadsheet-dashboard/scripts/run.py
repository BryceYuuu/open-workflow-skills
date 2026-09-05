from pathlib import Path
import argparse,csv,statistics,html,json

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--output',required=True); a=ap.parse_args();
 with open(a.input,newline='',encoding='utf-8-sig') as f: rows=list(csv.DictReader(f)); fields=list(rows[0]) if rows else []
 stats={}
 for k in fields:
  vals=[]; missing=0
  for r in rows:
   v=(r.get(k) or '').strip();
   if not v: missing+=1; continue
   try: vals.append(float(v.replace(',','')))
   except: pass
  stats[k]={'missing':missing,'numeric_count':len(vals)}
  if vals: stats[k].update({'min':min(vals),'max':max(vals),'mean':statistics.fmean(vals)})
 out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); cards=''.join(f"<tr><td>{html.escape(k)}</td><td>{v['missing']}</td><td>{v['numeric_count']}</td><td>{v.get('mean','')}</td><td>{v.get('min','')}</td><td>{v.get('max','')}</td></tr>" for k,v in stats.items()); doc=(f"<!doctype html><meta charset=utf-8><title>Spreadsheet Dashboard</title><style>body{{font-family:system-ui;max-width:1000px;margin:40px auto}}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #ddd;padding:8px;text-align:left}}</style><h1>Spreadsheet Dashboard</h1><p>Rows: {len(rows)} · Columns: {len(fields)}</p><table><tr><th>Column</th><th>Missing</th><th>Numeric</th><th>Mean</th><th>Min</th><th>Max</th></tr>{cards}</table>"); out.write_text(doc,encoding='utf-8'); out.with_suffix('.json').write_text(json.dumps({'rows':len(rows),'columns':fields,'stats':stats},indent=2)); print(out)
if __name__=='__main__':main()

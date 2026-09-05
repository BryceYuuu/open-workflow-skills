from pathlib import Path
import argparse,os,json
IGNORE={'.git','node_modules','.venv','__pycache__','dist','build'}
def tree(root,max_depth=3):
 lines=[]
 for p in sorted(root.rglob('*')):
  rel=p.relative_to(root)
  if any(x in IGNORE for x in rel.parts) or len(rel.parts)>max_depth: continue
  lines.append('  '*(len(rel.parts)-1)+('📁 ' if p.is_dir() else '• ')+rel.name)
 return '\n'.join(lines)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); ap.add_argument('--output',required=True); a=ap.parse_args(); r=Path(a.repo).resolve(); exts={}; files=0
 for p in r.rglob('*'):
  if p.is_file() and not any(x in IGNORE for x in p.relative_to(r).parts): files+=1; exts[p.suffix or '[none]']=exts.get(p.suffix or '[none]',0)+1
 out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); md=f'# Repository Overview\n\nRoot: `{r.name}`\n\nFiles scanned: **{files}**\n\n## Structure\n\n```text\n{tree(r)}\n```\n\n## File types\n\n'+ '\n'.join(f'- `{k}`: {v}' for k,v in sorted(exts.items(),key=lambda x:-x[1])); out.write_text(md); out.with_suffix('.json').write_text(json.dumps({'files':files,'extensions':exts},indent=2)); print(out)
if __name__=='__main__':main()

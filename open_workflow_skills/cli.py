from __future__ import annotations
import argparse, json, os, shutil, subprocess, sys
from pathlib import Path

VERSION = "2.0.0"

def repo_root() -> Path:
    env = os.environ.get("OWS_REPO")
    if env:
        return Path(env).expanduser().resolve()
    p = Path(__file__).resolve().parent.parent
    if (p / "registry.json").exists():
        return p
    cwd = Path.cwd()
    if (cwd / "registry.json").exists():
        return cwd
    raise SystemExit("Cannot locate Open Workflow Skills repository. Set OWS_REPO=/path/to/open-workflow-skills")

def registry():
    return json.loads((repo_root()/"registry.json").read_text(encoding="utf-8"))

def find_skill(slug: str):
    for s in registry()["skills"]:
        if s["slug"] == slug:
            return s
    raise SystemExit(f"Unknown skill: {slug}")

def runtime_manifest(slug: str):
    p = repo_root()/"skills"/slug/"runtime.json"
    return json.loads(p.read_text()) if p.exists() else None

def cmd_list(args):
    items = registry()["skills"]
    if args.status:
        items = [x for x in items if x.get("status") == args.status]
    if args.implemented:
        items = [x for x in items if x.get("implementation_status") == "tested-reference"]
    for s in items:
        impl = "RUN" if s.get("implementation_status") == "tested-reference" else "DEF"
        print(f"{s['id']:03d}  {impl:3}  {s['status']:<12}  {s['slug']:<32}  {s['name']} / {s['name_zh']}")

def cmd_info(args):
    s = find_skill(args.skill)
    print(json.dumps(s, ensure_ascii=False, indent=2))
    m = runtime_manifest(args.skill)
    if m:
        print("\nRuntime:\n" + json.dumps(m, ensure_ascii=False, indent=2))

def checks_for(skill=None):
    base = [("python", shutil.which("python3") or shutil.which("python"))]
    manifests=[]
    if skill:
        m=runtime_manifest(skill)
        if m: manifests=[m]
    else:
        for s in registry()["skills"]:
            m=runtime_manifest(s["slug"])
            if m: manifests.append(m)
    seen=set()
    for m in manifests:
        for cmd in m.get("optional_commands",[]):
            if cmd not in seen:
                seen.add(cmd); base.append((cmd, shutil.which(cmd)))
    return base

def cmd_doctor(args):
    if args.skill: find_skill(args.skill)
    bad=0
    for name,path in checks_for(args.skill):
        if path: print(f"✓ {name}: {path}")
        else: print(f"! {name}: not found (optional unless the selected mode requires it)"); bad += 1
    if args.skill and runtime_manifest(args.skill):
        print(f"✓ {args.skill}: runnable reference implementation present")
    elif args.skill:
        print(f"- {args.skill}: definition-only; no runtime implementation in v{VERSION}")
    return 0

def cmd_run(args):
    s=find_skill(args.skill); m=runtime_manifest(args.skill)
    if not m:
        raise SystemExit(f"{args.skill} is definition-only in v{VERSION}; no executable reference implementation yet.")
    entry = repo_root()/"skills"/args.skill/m["entrypoint"]
    cmd=[sys.executable, str(entry)] + args.skill_args
    return subprocess.call(cmd, cwd=repo_root())

def cmd_test(args):
    targets=[args.skill] if args.skill else [s["slug"] for s in registry()["skills"] if s.get("implementation_status")=="tested-reference"]
    failures=[]
    for slug in targets:
        m=runtime_manifest(slug)
        if not m:
            print(f"SKIP {slug}: definition-only"); continue
        test = repo_root()/"skills"/slug/m.get("smoke_test","tests/smoke.py")
        print(f"==> {slug}")
        rc=subprocess.call([sys.executable,str(test)], cwd=repo_root())
        if rc: failures.append(slug)
    if failures:
        print("FAILED:", ", ".join(failures)); return 1
    print(f"PASS: {len(targets)} skill smoke test(s)")
    return 0

def cmd_install(args):
    find_skill(args.skill)
    src=repo_root()/"skills"/args.skill
    dest=Path(args.target).expanduser().resolve()/args.skill
    if dest.exists() and not args.force:
        raise SystemExit(f"Destination exists: {dest}. Use --force to replace it.")
    if dest.exists(): shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src,dest)
    print(f"Installed {args.skill} -> {dest}")
    return 0

def main(argv=None):
    p=argparse.ArgumentParser(prog="ows", description="Open Workflow Skills local CLI")
    p.add_argument("--version", action="version", version=f"ows {VERSION}")
    sub=p.add_subparsers(dest="cmd", required=True)
    q=sub.add_parser("list"); q.add_argument("--status", choices=["verified","integration","experimental"]); q.add_argument("--implemented", action="store_true"); q.set_defaults(func=cmd_list)
    q=sub.add_parser("info"); q.add_argument("skill"); q.set_defaults(func=cmd_info)
    q=sub.add_parser("doctor"); q.add_argument("skill", nargs="?"); q.set_defaults(func=cmd_doctor)
    q=sub.add_parser("run"); q.add_argument("skill"); q.add_argument("skill_args", nargs=argparse.REMAINDER); q.set_defaults(func=cmd_run)
    q=sub.add_parser("test"); q.add_argument("skill", nargs="?"); q.set_defaults(func=cmd_test)
    q=sub.add_parser("install"); q.add_argument("skill"); q.add_argument("--target", required=True); q.add_argument("--force", action="store_true"); q.set_defaults(func=cmd_install)
    a=p.parse_args(argv)
    rc=a.func(a)
    raise SystemExit(rc or 0)

if __name__ == "__main__": main()

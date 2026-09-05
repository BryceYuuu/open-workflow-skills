import subprocess,sys
p=subprocess.run([sys.executable,'skills/cron-builder/scripts/run.py','--schedule','every monday at 9:30 am','--command','backup.sh'],capture_output=True,text=True,check=True); assert p.stdout.strip()=='30 9 * * 1 backup.sh'; print('PASS')

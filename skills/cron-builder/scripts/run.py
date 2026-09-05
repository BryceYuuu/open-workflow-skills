from pathlib import Path
import argparse,re,json
WEEK={'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6,'sunday':0}
def parse(s):
 s=s.lower().strip(); tm=re.search(r'(\d{1,2})(?::(\d{2}))?\s*(am|pm)?',s); hour=9; minute=0
 if tm:
  hour=int(tm.group(1)); minute=int(tm.group(2) or 0); ap=tm.group(3); hour=(hour%12)+(12 if ap=='pm' else 0) if ap else hour
 if 'every hour' in s or 'hourly' in s:return '0 * * * *'
 if 'every day' in s or 'daily' in s:return f'{minute} {hour} * * *'
 for day,num in WEEK.items():
  if day in s:return f'{minute} {hour} * * {num}'
 if 'every week' in s or 'weekly' in s:return f'{minute} {hour} * * 1'
 raise ValueError('Unsupported schedule; use daily/hourly/weekly or a weekday with a time')
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--schedule',required=True); ap.add_argument('--command',required=True); ap.add_argument('--output'); a=ap.parse_args(); expr=parse(a.schedule); line=f'{expr} {a.command}'; print(line)
 if a.output: Path(a.output).write_text(line+'\n')
if __name__=='__main__':main()

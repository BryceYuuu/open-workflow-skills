from pathlib import Path
import tempfile,subprocess,sys,json
with tempfile.TemporaryDirectory() as td:
 d=Path(td); (d/'i.txt').write_text('ACME LTD\nInvoice # INV-1002\n2026-09-05\nTotal: $1,234.50'); out=d/'o.json'; subprocess.run([sys.executable,'skills/invoice-data-extractor/scripts/run.py','--input',str(d/'i.txt'),'--output',str(out)],check=True); x=json.loads(out.read_text())[0]; assert x['invoice_number']=='INV-1002' and x['total']==1234.5; print('PASS')

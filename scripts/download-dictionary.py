import requests,json,gzip
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data/source/arabic-kaikki.download'
if not p.exists():
 with requests.get('https://kaikki.org/dictionary/Arabic/kaikki.org-dictionary-Arabic.jsonl.gz',stream=True,timeout=60) as r:
  r.raise_for_status()
  with p.with_suffix('.tmp').open('wb') as f:
   for b in r.iter_content(1024*1024):f.write(b)
 p.with_suffix('.tmp').replace(p)
print('Downloaded',p.stat().st_size,flush=True)
magic=p.open('rb').read(2)
handle=gzip.open(p,'rt',encoding='utf-8') if magic==b'\x1f\x8b' else p.open(encoding='utf-8')
with handle as f:
 for i,line in enumerate(f):
  if i==0:print(line[:5000],flush=True)
  if i>0:break

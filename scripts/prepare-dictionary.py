import json,gzip,re
from pathlib import Path
root=Path(__file__).resolve().parents[1];p=root/'data/source/arabic-kaikki.download'
def norm(s):return re.sub('[\u064b-\u065f\u0670\u0640]','',s)
records={};forms={};lines=0
opener=gzip.open if p.open('rb').read(2)==b'\x1f\x8b' else open
with opener(p,'rt',encoding='utf-8') as f:
 for line in f:
  x=json.loads(line);lines+=1;word=x.get('word','')
  if not re.search('[\u0621-\u064a]',word):continue
  gloss=[];bases=[]
  for s in x.get('senses',[]):
   gloss.extend(s.get('glosses',[]))
   bases.extend(y.get('word','') for y in s.get('form_of',[]))
  if not gloss and not bases:continue
  key=norm(word);row={'word':word,'pos':x.get('pos',''),'glosses':list(dict.fromkeys(gloss))[:8]}
  if bases:row['formOf']=list(dict.fromkeys(bases))
  records.setdefault(key,[])
  if row not in records[key]:records[key].append(row)
  for v in x.get('forms',[]):
   value=v.get('form','')
   if value and value!='-' and re.search('[\u0621-\u064a]',value):
    k=norm(value)
    if k!=key:forms.setdefault(k,set()).add(key)
obj={'metadata':{'name':'Arabic–English Wiktionary via Kaikki','source':'https://kaikki.org/dictionary/Arabic/index.html','license':'CC BY-SA 4.0 (text); see attribution notice','licenseUrl':'https://creativecommons.org/licenses/by-sa/4.0/','processedOn':'2026-11-13','modifications':'Selected Arabic headwords, English glosses, inflection references; normalized search keys; omitted media.'},'entries':records,'forms':{k:list(v) for k,v in forms.items()}}
(root/'app/data/dictionary.json').write_text(json.dumps(obj,ensure_ascii=False,separators=(',',':')),encoding='utf-8');print('raw records',lines,'heads',len(records),'form keys',len(forms),'bytes',(root/'app/data/dictionary.json').stat().st_size)
for word in ['كتاب','وأقرأ','مرحبا','صياد']:print(word,records.get(word),list(forms.get(word,[]))[:4])

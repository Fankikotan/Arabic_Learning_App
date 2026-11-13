from pathlib import Path
import json,unicodedata,re,shutil
APP=Path(__file__).resolve().parents[1]/'app';BASE=APP.parents[1]/'学习材料/ar'
consonants=dict(zip('بتثجحخدذرزسشصضطظعغفقكلمنهوي',['b','t','th','j','ḥ','kh','d','dh','r','z','s','sh','ṣ','ḍ','ṭ','ẓ','ʿ','gh','f','q','k','l','m','n','h','w','y']))
consonants.update({'أ':'ʾ','إ':'ʾ','آ':'ʾā','ء':'ʾ','ؤ':'ʾ','ئ':'ʾ','ا':'ā','ٱ':'ā','ى':'ā','ة':'h'})
vowels={'َ':'a','ُ':'u','ِ':'i','ً':'an','ٌ':'un','ٍ':'in','ٰ':'ā'}
def romanize(word):
 clusters=[]
 for ch in unicodedata.normalize('NFC',word):
  if unicodedata.combining(ch) and clusters:clusters[-1][1]+=ch
  else:clusters.append([ch,''])
 out='';i=0
 while i<len(clusters):
  ch,marks=clusters[i];c=consonants.get(ch,'');v=''.join(vowels[m] for m in marks if m in vowels)
  if ch=='ة' and v:c='t'
  if 'ّ' in marks:c=c+c
  if i+1<len(clusters):
   nxt,nmarks=clusters[i+1]
   if 'ً' in marks and nxt=='ا' and not nmarks:i+=1
   elif v=='a' and nxt in ['ا','ى'] and not nmarks:v='ā';i+=1
   elif v=='u' and nxt=='و' and not nmarks:v='ū';i+=1
   elif v=='i' and nxt=='ي' and not nmarks:v='ī';i+=1
  out+=c+v;i+=1
 plain=re.sub('[\u064b-\u065f\u0670]','',word)
 overrides={'هذا':'hādhā','هذه':'hādhihi','وهذا':'wa-hādhā','لكن':'lākin','ولكن':'wa-lākin','لكنه':'lākinnahu'}
 if plain in overrides:return overrides[plain]
 if plain.startswith('ال') and out.startswith('āl'):
  tail=out[2:];letter=consonants.get(plain[2:3],'')
  if plain[2:3] in 'تثدذرزسشصضطظلن' and tail.startswith(letter+letter):return 'a'+letter+'-'+tail[len(letter):]
  return 'al-'+tail
 if plain.startswith('وال') and out.startswith('wāl'):return 'wa-l-'+out[3:]
 return out
combined={'format':'arabic-learning-material','schemaVersion':1,'books':[],'notebooks':[]}
selected=[[1],[2],[4],[1,2],[0,1],[2,3],[2,4],[0,1],[1],[4],[1,2],[0,1]]
for id in ['ar-foundations-001','ar-fisherman-001']:
 root=BASE/id;p=root/'manifest.json';m=json.loads(p.read_text(encoding='utf-8'));b=m['books'][0]
 for n in m['notebooks']:
  n['version']=b['version']
  for w in n['words']:w['transliteration']=romanize(w['word'])
 if id=='ar-foundations-001':
  for c,indexes in zip(b['chapters'],selected):c['grammar'][0]['examples']=[{'sentenceId':c['sentences'][i]['id'],'translation':c['sentences'][i]['translations']['zh']} for i in indexes]
 else:
  b['cover']='covers/fisherman.png';b['adaptationSource']={'title':'The Story of the Fisherman and the Genie','url':'https://www.gutenberg.org/files/20916/20916-h/20916-h.htm','note':'Original simplified Arabic retelling based on the traditional plot, not a quotation from a modern translation.'}
  c=b['chapters'][0]
  c['grammar']=[g for g in c['grammar'] if g['id'] not in ['ar-lam-negation','ar-yesno-hal']]
  for gid,title,explanation,needle in [('ar-lam-negation','لَمْ + 现在式：否定过去','لَمْ يَجِدْ 表示他没有找到。لَمْ 后使用相应的未完成式形式，这里先整体认识。','لَمْ يَجِدْ'),('ar-yesno-hal','هَلْ：是非疑问','هَلْ 放在句首构成是否式问题，可以用 نَعَمْ 回答。本例的否定不伤害是承诺内容。','هَلْ')]:
   sentence=next(s for s in c['sentences'] if needle in s['text']);c['grammar'].append({'id':gid,'title':title,'status':'new','explanation':explanation,'examples':[{'sentenceId':sentence['id'],'translation':sentence['translations']['zh']}]})
 p.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
 combined['books']+=m['books'];combined['notebooks']+=m['notebooks']
 # Copy complete resources into separate book/notebook namespaces matching asset lookup.
 for b in m['books']:
  files=([b['cover']] if b.get('cover') else [])+[c['audio'] for c in b['chapters']]
  for name in files:
   dest=APP/'builtin'/b['id']/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/name,dest)
 for n in m['notebooks']:
  for w in n['words']:
   dest=APP/'builtin'/n['id']/w['audio'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/w['audio'],dest)
(APP/'data/builtin-library.json').write_text(json.dumps(combined,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
print('Embedded:',len(combined['books']),'books',len(combined['notebooks']),'notebooks; all audio copied')
for w in combined['notebooks'][0]['words'][:7]:print(w['word'],w['transliteration'])

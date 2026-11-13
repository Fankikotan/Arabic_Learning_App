from pathlib import Path
import zipfile,shutil,json
root=Path(__file__).resolve().parents[1];out=root/'发布包';out.mkdir(exist_ok=True)
source=root/'app';manifest=json.loads((source/'data/builtin-library.json').read_text(encoding='utf-8'))
# Built-in assets, not a ZIP import flow.
for b in manifest['books']:
 for c in b['chapters']:
  assert c.get('audio') and (source/'builtin'/b['id']/c['audio']).is_file(),'Missing chapter audio'
for n in manifest['notebooks']:
 for w in n['words']:assert w.get('audio') and (source/'builtin'/n['id']/w['audio']).is_file(),'Missing word audio'
css=(source/'style.css').read_text(encoding='utf-8-sig');css='\n'.join(line for line in css.splitlines() if not line.startswith('@import'))
js=(source/'app.js').read_text(encoding='utf-8-sig');html=(source/'index.html').read_text(encoding='utf-8-sig').replace('<link rel="stylesheet" href="style.css">','<style>'+css+'</style>').replace('<script type="module" src="app.js"></script>','<script type="module">'+js+'</script>')
(out/'index.html').write_text(html,encoding='utf-8');shutil.copyfile(root/'使用说明.md',out/'使用说明.md');shutil.copyfile(source/'THIRD-PARTY-NOTICES.md',out/'THIRD-PARTY-NOTICES.md')
shutil.copyfile(source/'capacitor-runtime.js',out/'capacitor-runtime.js')
for name in ['data','builtin']:shutil.copytree(source/name,out/name,dirs_exist_ok=True)
with zipfile.ZipFile(out/'Arabic-Learning-手机网页包.zip','w',zipfile.ZIP_DEFLATED) as z:
 for file in ['index.html','使用说明.md','THIRD-PARTY-NOTICES.md','capacitor-runtime.js']:z.write(out/file,file)
 for folder in ['data','builtin']:
  for p in sorted((out/folder).rglob('*')):
   if p.is_file():z.write(p,p.relative_to(out).as_posix())
with zipfile.ZipFile(out/'Arabic-Learning-手机网页包.zip') as z:assert z.testzip() is None
print('Built-in mobile package checked:',(out/'Arabic-Learning-手机网页包.zip').stat().st_size,'bytes')

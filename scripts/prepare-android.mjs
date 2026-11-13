import {cp,mkdir,readFile,writeFile,readdir} from 'node:fs/promises';
import path from 'node:path';
const root=path.resolve('.'),source=path.join(root,'app'),target=path.join(root,'www');
const required=['data/builtin-library.json','data/dictionary.json'];
for(const file of required)await readFile(path.join(source,file));
const manifest=JSON.parse(await readFile(path.join(source,'data/builtin-library.json'),'utf8'));
for(const book of manifest.books)for(const chapter of book.chapters){if(!chapter.audio)throw Error('Missing builtin chapter audio: '+chapter.id);await readFile(path.join(source,'builtin',book.id,chapter.audio));}
await mkdir(target,{recursive:true});
// Copy only runtime resources, never raw source data, QA HTML or credentials.
for(const name of ['index.html','app.js','style.css','capacitor-runtime.js','data','builtin','THIRD-PARTY-NOTICES.md'])await cp(path.join(source,name),path.join(target,name),{recursive:true});
let css=await readFile(path.join(target,'style.css'),'utf8');css=css.split('\n').filter(line=>!line.startsWith('@import')).join('\n');await writeFile(path.join(target,'style.css'),css);
await writeFile(path.join(target,'build-info.json'),JSON.stringify({createdAt:new Date().toISOString(),books:manifest.books.map(b=>({id:b.id,version:b.version})),appVersion:JSON.parse(await readFile('package.json','utf8')).version},null,2));
console.log('Prepared Android webDir: '+target+' (no APK built)');

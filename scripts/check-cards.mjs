import {readFile} from 'node:fs/promises';import vm from 'node:vm';import assert from 'node:assert/strict';
const code=await readFile('app/app.js','utf8');let html='';
const state={recent:[{word:'hello',meaning:'你好',language:'en'}],favorites:[{word:'hello',meaning:'你好',language:'en'}]};
const context=vm.createContext({state,document:{addEventListener(){}},library:{books:[],notebooks:[{id:'n1',language:'en',title:'Words',words:[{id:'w1',word:'hello',meaning:'你好',example:'Hello!',exampleTranslation:'你好！',transliteration:'hello'}]}]},Audio:class{pause(){}},Date,Map,Set,Number,Math,URL,setTimeout,clearTimeout,crypto,card:0,flipped:false,notebook:null,tab:'recent',page:'vocab',view:'grid',wordView:'card',esc:s=>String(s??''),ib:()=>'',shell:s=>html=s,$:()=>null,wordRow:w=>w.word,persist:()=>{},toast:()=>{}});
vm.runInContext(code.slice(code.indexOf('// Shared vocabulary'),code.indexOf('function sleepSettings()'))+';globalThis.api={vocab,rateCurrent}',context);
for(const tab of ['recent','favorites','learning']){context.tab=tab;context.api.vocab();assert.ok(html.includes('data-action="shared-flip"'));assert.ok(html.includes('data-rating="familiar"'))}
context.notebook='n1';context.api.vocab();assert.ok(html.includes('hello'));context.api.rateCurrent('familiar');assert.equal(Object.keys(state.reviews).length,1);assert.equal(state.reviewHistory.length,1);
context.state.cardSettings.meaning='on';context.api.vocab();assert.ok(html.includes('你好'));
const parseCtx=vm.createContext({});vm.runInContext(code.slice(code.indexOf('function validatePackage('),code.indexOf("$('#import').onchange"))+';globalThis.validate=validatePackage',parseCtx);
const m={format:'arabic-learning-material',schemaVersion:1,books:[],notebooks:[{id:'n',title:'words',words:[{word:'hello',meaning:'你好',audio:'word.mp3'}]}]};assert.throws(()=>parseCtx.validate(m,new Map()));parseCtx.validate(m,new Map([['word.mp3',new Uint8Array()]]));m.notebooks[0].words[0].transliteration=123;assert.throws(()=>parseCtx.validate(m,new Map([['word.mp3',new Uint8Array()]])));
console.log('PASS: shared cards across sources, rating history, default meanings, optional word audio validation');

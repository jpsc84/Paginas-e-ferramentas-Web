"""Gera o HTML responsivo a partir de data.json."""
import json, html
data = json.load(open("data.json", encoding="utf-8"))
M = data["meta"]

CSS = r"""
:root{--bg:#f6f5f1;--surface:#ffffff;--surface2:#efeee8;--ink:#1b1f23;--muted:#555d66;--line:#dcd9cf;
--accent:#12463B;--accent-ink:#ffffff;--accent-soft:#e3eeea;--brass:#8a6220;--focus:#B07D2B;
--k-cmd:#12463B;--k-ui:#2f6b5c;--k-prompt:#3d4f6b;--k-api:#8a6220;--k-unverified:#9E3B26;--prompt-bg:#f3f6f4;--shadow:0 1px 2px rgba(0,0,0,.06)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#121513;--surface:#1b201d;--surface2:#232a26;--ink:#e9ece9;--muted:#a6b0aa;--line:#323a35;
--accent:#5fb39b;--accent-ink:#0d1a15;--accent-soft:#1f322b;--brass:#d6a65a;--k-cmd:#6cc2a8;--k-ui:#8cc9b6;--k-prompt:#9fb3d6;--k-api:#d6a65a;--k-unverified:#e58b74;--prompt-bg:#18221e;--shadow:none;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#121513;--surface:#1b201d;--surface2:#232a26;--ink:#e9ece9;--muted:#a6b0aa;--line:#323a35;
--accent:#5fb39b;--accent-ink:#0d1a15;--accent-soft:#1f322b;--brass:#d6a65a;--k-cmd:#6cc2a8;--k-ui:#8cc9b6;--k-prompt:#9fb3d6;--k-api:#d6a65a;--k-unverified:#e58b74;--prompt-bg:#18221e;--shadow:none;color-scheme:dark}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-padding-top:120px}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 "IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--accent)}
button,input,select{font:inherit;color:inherit}
:focus-visible{outline:3px solid var(--focus);outline-offset:2px}
.wrap{max-width:960px;margin:0 auto;padding:0 16px}
header.top{background:var(--accent);color:var(--accent-ink);padding:22px 0 18px}
header.top .eyebrow{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;opacity:.85;margin:0 0 6px}
header.top h1{font-family:"Archivo","IBM Plex Sans",system-ui,sans-serif;font-size:clamp(1.35rem,4.6vw,2.1rem);line-height:1.2;margin:0}
header.top .sub{margin:6px 0 12px;font-size:1.02rem;opacity:.92}
.meta{display:flex;flex-wrap:wrap;gap:6px}
.pill{display:inline-flex;align-items:center;gap:4px;border:1px solid currentColor;border-radius:999px;padding:2px 10px;font-size:.8rem;opacity:.95}
.pill a{color:inherit}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:var(--bg);border-bottom:1px solid var(--line);padding:10px 0}
.bar .row{display:flex;gap:8px;align-items:center}
.search{flex:1;min-width:0;position:relative}
.search input{width:100%;height:46px;border:1px solid var(--line);border-radius:10px;background:var(--surface);padding:0 40px 0 12px}
.search input::-webkit-search-cancel-button{-webkit-appearance:none;display:none}
.search .clear{position:absolute;right:4px;top:4px;width:38px;height:38px;border:0;background:none;border-radius:8px;cursor:pointer;color:var(--muted)}
.btn{min-height:44px;padding:0 14px;border:1px solid var(--line);background:var(--surface);border-radius:10px;cursor:pointer;display:inline-flex;align-items:center;gap:6px;white-space:nowrap}
.btn.primary{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.btn.small{min-height:36px;padding:0 10px;font-size:.88rem}
.btn[aria-pressed="true"]{background:var(--accent-soft);border-color:var(--accent)}
.badge-count{background:var(--accent);color:var(--accent-ink);border-radius:999px;font-size:.75rem;padding:0 7px;min-width:20px;text-align:center}
.filters{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px;margin-top:10px;max-height:calc(100vh - 150px);max-height:calc(100dvh - 150px);overflow-y:auto;overscroll-behavior:contain}
.filters h3{font-size:.85rem;margin:6px 0;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{min-height:36px;padding:0 12px;border-radius:999px;border:1px solid var(--line);background:var(--surface2);cursor:pointer;font-size:.9rem}
.chip[aria-pressed="true"]{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.filters select{height:44px;border-radius:10px;border:1px solid var(--line);background:var(--surface2);padding:0 8px;width:100%;max-width:420px}
.toggles{display:flex;flex-wrap:wrap;gap:8px 16px;margin-top:10px}
.toggles label{display:flex;align-items:center;gap:8px;min-height:36px;cursor:pointer}
.toggles input{width:20px;height:20px}
.status{font-size:.9rem;color:var(--muted);margin:10px 0 0}
main{padding:14px 0 120px}
.intro{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin-bottom:14px}
.intro p{margin:.3em 0}
.legend{display:grid;gap:6px;margin-top:8px}
.legend div{font-size:.9rem}
.mod{background:var(--surface);border:1px solid var(--line);border-radius:12px;margin:10px 0;box-shadow:var(--shadow)}
.mod-head{width:100%;text-align:left;border:0;background:none;padding:14px 16px;display:flex;gap:10px;align-items:center;cursor:pointer;min-height:56px}
.mod-head .num{flex:none;width:34px;height:34px;border-radius:9px;background:var(--accent-soft);color:var(--accent);display:grid;place-items:center;font-weight:700}
.mod-head .t{flex:1;min-width:0}
.mod-head .t b{display:block;font-size:1.04rem}
.mod-head .t span{display:block;font-size:.86rem;color:var(--muted)}
.mod-head .cnt{font-size:.8rem;color:var(--muted);white-space:nowrap}
.mod-head .chev{transition:transform .2s;flex:none}
.mod-head[aria-expanded="true"] .chev{transform:rotate(180deg)}
.mod-body{padding:0 12px 12px}
.card{border:1px solid var(--line);border-radius:10px;padding:12px;margin:10px 0;background:var(--surface)}
.card.sel{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent-soft)}
.card h4{margin:0 0 6px;font-size:1.02rem;line-height:1.35}
.tags{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:8px}
.kind{font-size:.74rem;font-weight:600;border-radius:6px;padding:2px 7px;border:1px solid currentColor}
.kind.cmd{color:var(--k-cmd)}.kind.ui{color:var(--k-ui)}.kind.prompt{color:var(--k-prompt)}.kind.api{color:var(--k-api)}.kind.unverified{color:var(--k-unverified)}
.plat{font-size:.74rem;border-radius:6px;padding:2px 7px;background:var(--surface2);color:var(--muted)}
.what{margin:0 0 8px}
.pbox{background:var(--prompt-bg);border:1px dashed var(--line);border-left:4px solid var(--accent);border-radius:8px;padding:10px 12px;font-size:.95rem;white-space:pre-wrap;word-break:break-word}
.pbox.code{font-family:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace}
.actions{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:8px}
.actions label{display:flex;align-items:center;gap:8px;min-height:40px;padding:0 10px;border:1px solid var(--line);border-radius:10px;cursor:pointer;font-size:.9rem}
.actions input{width:20px;height:20px}
details.more{margin-top:8px;border-top:1px solid var(--line);padding-top:6px}
details.more summary{cursor:pointer;min-height:40px;display:flex;align-items:center;color:var(--accent);font-weight:600;font-size:.92rem}
details.more dl{margin:4px 0 0}
details.more dt{font-weight:700;font-size:.86rem;margin-top:8px}
details.more dd{margin:2px 0 0}
.srcs{font-size:.88rem}
.srcs a{word-break:break-word}
.sub-h{font-size:1rem;margin:16px 4px 6px}
.qgrid{display:grid;gap:8px}
.q{border:1px solid var(--line);border-radius:10px;padding:10px 12px}
.q.sel{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent-soft)}
.q .qh{display:flex;gap:8px;align-items:baseline;justify-content:space-between;flex-wrap:wrap}
.q .qh b{font-size:.95rem}
.q .qm{font-size:.78rem;color:var(--muted)}
ol.srclist{padding-left:0;list-style:none;margin:0}
ol.srclist li{padding:8px 4px;border-bottom:1px solid var(--line);font-size:.9rem;overflow-wrap:anywhere}
ol.srclist a,.srcs a{overflow-wrap:anywhere;word-break:break-word}
.card,.q,.pbox{min-width:0;overflow-wrap:anywhere}
.stype{font-size:.72rem;border-radius:6px;padding:1px 6px;margin-left:4px;background:var(--surface2);color:var(--muted)}
.stype.nao-oficial{color:var(--k-unverified)}
.hist h5{margin:12px 0 4px;font-size:.95rem}
.hist ul{margin:0;padding-left:20px}
.hist li{margin:3px 0;font-size:.93rem}
.batch{position:fixed;left:0;right:0;bottom:0;z-index:30;background:var(--surface);border-top:1px solid var(--line);box-shadow:0 -4px 12px rgba(0,0,0,.08);padding:10px 0 calc(10px + env(safe-area-inset-bottom))}
.batch .row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.batch .n{font-weight:700;margin-right:auto}
.toast{position:fixed;left:50%;bottom:90px;transform:translateX(-50%);background:var(--ink);color:var(--bg);padding:10px 16px;border-radius:10px;font-size:.92rem;z-index:50;opacity:0;pointer-events:none;transition:opacity .2s}
.toast.on{opacity:1}
dialog.menu{border:0;border-radius:14px;padding:0;width:min(520px,calc(100vw - 32px));max-height:calc(100vh - 48px);background:var(--surface);color:var(--ink)}
dialog.menu::backdrop{background:rgba(0,0,0,.45)}
dialog.menu .mh{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--surface)}
dialog.menu ol{list-style:none;margin:0;padding:6px}
dialog.menu li button{width:100%;text-align:left;border:0;background:none;padding:10px 12px;border-radius:8px;min-height:44px;cursor:pointer;display:flex;gap:10px}
dialog.menu li button:hover{background:var(--surface2)}
dialog.menu li .n{color:var(--accent);font-weight:700;width:24px;flex:none}
.empty{padding:20px;text-align:center;color:var(--muted)}
footer{font-size:.85rem;color:var(--muted);padding:20px 0 120px;border-top:1px solid var(--line)}
mark{background:#f3dfae;color:#1b1f23;border-radius:3px;padding:0 1px}
@media (max-width:560px){.hide-sm{display:none}.btn{padding:0 11px}}
@media print{.bar,.batch,.actions,.toast{display:none}.mod-body{display:block!important}}
"""

JS = r"""
const D=JSON.parse(document.getElementById('data').textContent);
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const PL=Object.fromEntries(D.platforms.map(p=>[p.key,p.label]));
const SRC=Object.fromEntries(D.sources.map(s=>[s.id,s]));
const STY={'oficial':'oficial, reaberta nesta revisão','herdada':'oficial, citada em edição anterior e não reaberta','busca':'oficial, localizada pela busca e não aberta','nao-oficial':'não oficial'};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const norm=s=>String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');
let sel=new Set();try{sel=new Set(JSON.parse(localStorage.getItem('acervo-sel')||'[]'))}catch(e){}
const saveSel=()=>{try{localStorage.setItem('acervo-sel',JSON.stringify([...sel]))}catch(e){}};
const ALL={};D.items.forEach(x=>ALL[x.id]=x);D.quick.forEach(x=>ALL[x.id]=x);
const st={q:'',mod:'all',plats:new Set(),kinds:new Set(),portable:true,onlySel:false,limits:false};

function tagsHTML(x){
  return x.kinds.map(k=>`<span class="kind ${k}" title="${esc(D.kinds[k].desc)}">${esc(D.kinds[k].label)}</span>`).join('')+
   x.platforms.map(p=>`<span class="plat">${p==='portatil'?'Prompt portátil':esc(PL[p])}</span>`).join('');
}
function actionsHTML(x){
  const isCode=/^\//.test(x.example)||/^\$/.test(x.example);
  return `<div class="pbox${isCode?' code':''}" id="t-${x.id}">${esc(x.example)}</div>
  <div class="actions"><button class="btn small primary" data-copy="${x.id}" aria-label="Copiar o texto de ${esc(x.title)}">Copiar texto</button>
  <label><input type="checkbox" data-sel="${x.id}" ${sel.has(x.id)?'checked':''}> Selecionar</label></div>`;
}
function card(x){
  const src=x.sources.length?x.sources.map(id=>{const s=SRC[id];return `<li><a href="#src-${id}">[${id}]</a> <a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title)}</a>${(s.type==='herdada'||s.type==='busca')?' (não reaberta nesta revisão)':''}</li>`}).join(''):'';
  return `<article class="card${sel.has(x.id)?' sel':''}" data-id="${x.id}">
   <h4>${esc(x.title)}</h4><div class="tags">${tagsHTML(x)}</div>
   <p class="what">${esc(x.what)}</p>${actionsHTML(x)}
   <details class="more"><summary>Como usar, limitações e fontes</summary><dl>
   <dt>Como usar</dt><dd>${esc(x.how)}</dd>
   <dt>Limitações e o que conferir</dt><dd>${esc(x.limits)}</dd>
   <dt>Fontes</dt><dd class="srcs">${src?`<ul>${src}</ul>Verificado em ${esc(x.verified)}.`:'Prompt autoral; não depende de afirmação sobre produto.'}</dd>
   </dl></details></article>`;
}
function qcard(x){
  return `<div class="q${sel.has(x.id)?' sel':''}" data-id="${x.id}"><div class="qh"><b>${String(x.n).padStart(2,'0')}. ${esc(x.title)}</b><span class="qm">Módulo ${x.module}</span></div>
  <div class="tags">${tagsHTML(x)}</div>${actionsHTML(x)}</div>`;
}
const chev='<svg class="chev" width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2"/></svg>';
function build(){
  const root=$('#mods');let h='';
  D.modules.forEach(m=>{
    const its=D.items.filter(x=>x.module===m.n);
    let body;
    if(m.n===17){
      const hist=D.changelog.map(c=>`<h5>Versão ${esc(c.version)}${c.date?' · '+esc(c.date):''}</h5><ul>${c.notes.map(n=>`<li>${esc(n)}</li>`).join('')}</ul>`).join('');
      body=`<h3 class="sub-h" id="historico">Histórico de revisões</h3><div class="hist">${hist}</div>
      <h3 class="sub-h" id="consulta">Consulta rápida · ${D.quick.length} exemplos</h3>
      <p class="status">Itens iniciados com / são comandos documentados no ambiente indicado. Os demais são prompts; imagem, vídeo, ferramentas e agendamento dependem do acesso na plataforma.</p>
      <div class="qgrid">${D.quick.map(qcard).join('')}</div>
      <h3 class="sub-h" id="fontes">Fontes e verificação · ${D.sources.length}</h3>
      <p class="status">Pesquisa em ${esc(D.meta.date)}. Os prompts são exemplos autorais; não houve teste de geração em todas as plataformas.</p>
      <ol class="srclist">${D.sources.map(s=>`<li id="src-${s.id}"><b>[${s.id}]</b> ${esc(s.title)} <span class="stype ${s.type}">${esc(STY[s.type])}</span><br><a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.url)}</a></li>`).join('')}</ol>`;
    } else if(its.some(x=>/^(Cena|Estilo|Técnica):/.test(x.title))){
      const G={'':'Criação, edição e leitura de imagens','Cena':'Construção de cena','Estilo':'Estilos visuais','Técnica':'Técnicas e parâmetros'};
      const groups=[];its.forEach(x=>{const m=x.title.match(/^(Cena|Estilo|Técnica):/);const g=m?m[1]:'';let last=groups[groups.length-1];if(!last||last.g!==g){last={g,items:[]};groups.push(last);}last.items.push(x);});
      body=groups.map(gr=>`<div class="grp"><h3 class="sub-h">${esc(G[gr.g])} · ${gr.items.length}</h3>${gr.items.map(card).join('')}</div>`).join('');
    } else body=its.map(card).join('');
    const cnt=m.n===17?`${D.quick.length} exemplos`:`${its.length} itens`;
    h+=`<section class="mod" id="mod-${m.n}" data-mod="${m.n}"><button class="mod-head" aria-expanded="false" aria-controls="b-${m.n}">
      <span class="num">${m.n}</span><span class="t"><b>${esc(m.title)}</b><span>${esc(m.desc)}</span></span><span class="cnt" data-cnt>${cnt}</span>${chev}</button>
      <div class="mod-body" id="b-${m.n}" hidden>${body}</div></section>`;
  });
  root.innerHTML=h;
  $('#menuList').innerHTML=D.modules.map(m=>`<li><button data-go="${m.n}"><span class="n">${m.n}</span><span>${esc(m.title)}</span></button></li>`).join('')+
   `<li><button data-go="17" data-sub="consulta"><span class="n">›</span><span>Consulta rápida</span></button></li><li><button data-go="17" data-sub="fontes"><span class="n">›</span><span>Fontes</span></button></li><li><button data-go="17" data-sub="historico"><span class="n">›</span><span>Histórico</span></button></li>`;
  $('#fMod').innerHTML='<option value="all">Todas as tarefas (módulos)</option>'+D.modules.map(m=>`<option value="${m.n}">${m.n}. ${esc(m.title)}</option>`).join('');
  $('#fPlat').innerHTML=D.platforms.filter(p=>p.key!=='portatil').map(p=>`<button class="chip" aria-pressed="false" data-plat="${p.key}">${esc(p.label)}</button>`).join('');
  $('#fKind').innerHTML=Object.entries(D.kinds).map(([k,v])=>`<button class="chip" aria-pressed="false" data-kind="${k}">${esc(v.label)}</button>`).join('');
  $('#legend').innerHTML=Object.entries(D.kinds).map(([k,v])=>`<div><span class="kind ${k}">${esc(v.label)}</span> ${esc(v.desc)}</div>`).join('');
}
function setOpen(sec,open){const b=$('.mod-head',sec);b.setAttribute('aria-expanded',open);$('.mod-body',sec).hidden=!open;}
function textOf(x){return norm([x.title,x.what||'',x.how||'',x.example,x.limits||'',x.platforms.map(p=>PL[p]).join(' '),x.kinds.map(k=>D.kinds[k].label).join(' ')].join(' '))}
const IDX={};Object.values(ALL).forEach(x=>IDX[x.id]=textOf(x));
function match(x){
  if(st.mod!=='all'&&String(x.module)!==st.mod)return false;
  if(st.onlySel&&!sel.has(x.id))return false;
  if(st.kinds.size&&!x.kinds.some(k=>st.kinds.has(k)))return false;
  if(st.plats.size){const ok=x.platforms.some(p=>st.plats.has(p))||(st.portable&&x.platforms.includes('portatil'));if(!ok)return false;}
  if(st.q){const terms=norm(st.q).split(/\s+/).filter(Boolean);const t=IDX[x.id];if(!terms.every(w=>t.includes(w)))return false;}
  return true;
}
function active(){return !!(st.q||st.mod!=='all'||st.plats.size||st.kinds.size||st.onlySel)}
function apply(){
  let total=0;const act=active();
  $$('.mod').forEach(sec=>{
    const n=+sec.dataset.mod;let vis=0;
    $$('[data-id]',sec).forEach(el=>{const ok=match(ALL[el.dataset.id]);el.hidden=!ok;if(ok)vis++;});
    total+=vis;
    const cnt=$('[data-cnt]',sec);
    if(n===17){const qv=$$('.q',sec).filter(e=>!e.hidden).length;cnt.textContent=act?`${qv} exemplo${qv===1?'':'s'} encontrado${qv===1?'':'s'}`:`${D.quick.length} exemplos`;
      $$('.hist,#historico,#fontes,.srclist,#fontes + .status',sec).forEach(e=>e.hidden=act);}
    else cnt.textContent=act?`${vis} encontrado${vis===1?'':'s'}`:`${D.items.filter(x=>x.module===n).length} itens`;
    $$('.grp',sec).forEach(g=>{g.hidden=act&&!$$('article.card',g).some(c=>!c.hidden)});
    sec.hidden=act&&vis===0;
    if(act&&vis>0&&(st.q||st.onlySel||st.mod!=='all'))setOpen(sec,true);
  });
  $('#empty').hidden=!(act&&total===0);
  $('#status').textContent=act?`${total} resultado${total===1?'':'s'} com os filtros atuais.`:`${D.items.length} itens em 17 módulos e ${D.quick.length} exemplos de consulta rápida. Abra um módulo ou use a busca.`;
  const nf=st.plats.size+st.kinds.size+(st.mod!=='all')+(st.onlySel?1:0);
  $('#nf').textContent=nf;$('#nf').hidden=!nf;
  $$('details.more').forEach(d=>d.open=st.limits);
}
function updSel(){
  $$('[data-sel]').forEach(c=>{c.checked=sel.has(c.dataset.sel);c.closest('[data-id]').classList.toggle('sel',c.checked)});
  const n=sel.size;$('#batch').hidden=n===0;$('#bn').textContent=`${n} selecionado${n===1?'':'s'}`;$('#bcopy').textContent=`Copiar selecionados (${n})`;saveSel();
}
let tt;function toast(m){const t=$('#toast');t.textContent=m;t.classList.add('on');clearTimeout(tt);tt=setTimeout(()=>t.classList.remove('on'),1800)}
async function copy(text){
  try{await navigator.clipboard.writeText(text);return true}catch(e){
    const ta=document.createElement('textarea');ta.value=text;ta.setAttribute('readonly','');ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();
    let ok=false;try{ok=document.execCommand('copy')}catch(e2){}ta.remove();return ok}
}
function bind(){
  document.addEventListener('click',async e=>{
    const h=e.target.closest('.mod-head');if(h){setOpen(h.parentElement,h.getAttribute('aria-expanded')!=='true');return}
    const c=e.target.closest('[data-copy]');if(c){const ok=await copy(ALL[c.dataset.copy].example);toast(ok?'Texto copiado para a área de transferência':'Não foi possível copiar; selecione o texto manualmente');return}
    const g=e.target.closest('[data-go]');if(g){$('#menu').close();const sec=$('#mod-'+g.dataset.go);sec.hidden=false;setOpen(sec,true);(g.dataset.sub?$('#'+g.dataset.sub):sec).scrollIntoView({behavior:'smooth'});return}
    const p=e.target.closest('[data-plat]');if(p){const k=p.dataset.plat;st.plats.has(k)?st.plats.delete(k):st.plats.add(k);p.setAttribute('aria-pressed',st.plats.has(k));apply();return}
    const k=e.target.closest('[data-kind]');if(k){const v=k.dataset.kind;st.kinds.has(v)?st.kinds.delete(v):st.kinds.add(v);k.setAttribute('aria-pressed',st.kinds.has(v));apply();return}
  });
  document.addEventListener('change',e=>{const c=e.target.closest('[data-sel]');if(c){c.checked?sel.add(c.dataset.sel):sel.delete(c.dataset.sel);updSel();if(st.onlySel)apply();}});
  let deb;$('#q').addEventListener('input',e=>{clearTimeout(deb);deb=setTimeout(()=>{st.q=e.target.value.trim();apply()},120)});
  $('#qclear').onclick=()=>{$('#q').value='';st.q='';apply();$('#q').focus()};
  $('#fMod').onchange=e=>{st.mod=e.target.value;apply()};
  $('#tPortable').onchange=e=>{st.portable=e.target.checked;apply()};
  $('#tSel').onchange=e=>{st.onlySel=e.target.checked;apply()};
  $('#tLim').onchange=e=>{st.limits=e.target.checked;apply()};
  $('#btnFilters').onclick=()=>{const f=$('#filters');f.hidden=!f.hidden;$('#btnFilters').setAttribute('aria-expanded',!f.hidden)};
  $('#btnMenu').onclick=()=>$('#menu').showModal();$('#menuClose').onclick=()=>$('#menu').close();
  $('#expand').onclick=()=>$$('.mod').forEach(s=>{if(!s.hidden)setOpen(s,true)});
  $('#collapse').onclick=()=>$$('.mod').forEach(s=>setOpen(s,false));
  $('#reset').onclick=()=>{st.q='';st.mod='all';st.plats.clear();st.kinds.clear();st.onlySel=false;st.portable=true;$('#q').value='';$('#fMod').value='all';$('#tSel').checked=false;$('#tPortable').checked=true;$$('.chip').forEach(c=>c.setAttribute('aria-pressed','false'));apply()};
  $('#bcopy').onclick=async()=>{const ids=Object.keys(ALL).filter(id=>sel.has(id));const txt=ids.map(id=>`${ALL[id].title}\n${ALL[id].example}`).join('\n\n');const ok=await copy(txt);toast(ok?`${ids.length} textos copiados`:'Não foi possível copiar')};
  $('#bshow').onclick=()=>{st.onlySel=!st.onlySel;$('#tSel').checked=st.onlySel;$('#bshow').setAttribute('aria-pressed',st.onlySel);apply();if(st.onlySel)$('#mods').scrollIntoView()};
  $('#bclear').onclick=()=>{sel.clear();updSel();if(st.onlySel){st.onlySel=false;$('#tSel').checked=false;$('#bshow').setAttribute('aria-pressed','false')}apply()};
}
build();bind();updSel();apply();
"""

def page():
    j = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(M['title'])}</title>
<meta name="description" content="{html.escape(M['subtitle'])}: comandos documentados, recursos e prompts para ChatGPT, Claude, Gemini, Copilot, Perplexity, Grok, DeepSeek, Mistral e ferramentas especializadas. Versão {M['version']}, pesquisa em {M['date']}.">
<meta name="theme-color" content="#12463B">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700&family=IBM+Plex+Mono&family=IBM+Plex+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap">
<p class="eyebrow">Consulta diária · pt-BR</p>
<h1>{html.escape(M['title'])}</h1>
<p class="sub">{html.escape(M['subtitle'])}</p>
<div class="meta"><span class="pill">Versão {M['version']}</span><span class="pill">Pesquisa em {M['date']}</span><span class="pill"><a href="#historico" data-go="17" data-sub="historico">Histórico</a></span><span class="pill"><a href="guia-comandos-prompts-ia-2026.pdf" download>Baixar PDF</a></span></div>
</div></header>
<div class="bar"><div class="wrap">
 <div class="row">
  <button class="btn" id="btnMenu" aria-haspopup="dialog">☰ <span class="hide-sm">Módulos</span></button>
  <div class="search"><label for="q" class="hide-sm" style="position:absolute;left:-9999px">Buscar</label>
   <input id="q" type="search" placeholder="Buscar tarefa, recurso ou prompt" autocomplete="off" enterkeyhint="search">
   <button class="clear" id="qclear" aria-label="Limpar busca">✕</button></div>
  <button class="btn" id="btnFilters" aria-expanded="false" aria-controls="filters">Filtros <span class="badge-count" id="nf" hidden>0</span></button>
 </div>
 <div class="filters" id="filters" hidden>
  <h3>Tarefa</h3><select id="fMod" aria-label="Filtrar por tarefa"></select>
  <h3>Plataforma</h3><div class="chips" id="fPlat"></div>
  <h3>Classificação</h3><div class="chips" id="fKind"></div>
  <div class="toggles">
   <label><input type="checkbox" id="tPortable" checked> Incluir prompts portáteis ao filtrar plataforma</label>
   <label><input type="checkbox" id="tSel"> Exibir só os selecionados</label>
   <label><input type="checkbox" id="tLim"> Abrir limitações de todos os itens</label>
  </div>
  <div class="actions"><button class="btn small" id="expand">Expandir módulos</button><button class="btn small" id="collapse">Recolher módulos</button><button class="btn small" id="reset">Limpar filtros</button></div>
 </div>
 <p class="status" id="status" aria-live="polite"></p>
</div></div>
<main><div class="wrap">
 <section class="intro">
  <p><b>Como consultar.</b> Escolha a tarefa, confira a plataforma e copie o texto. Os botões apenas mostram ou copiam conteúdo; nada é executado em outras plataformas.</p>
  <p><b>Prompt portátil</b> é uma instrução adaptável a diferentes modelos. Não significa que todos pesquisem, executem ferramentas, exportem arquivos ou gerem mídia.</p>
  <p>A cobertura de plataformas não é ranking de mercado nem eleição de "melhor modelo". Modelo é o motor; aplicativo é o ambiente com menus, anexos, pesquisa e ferramentas.</p>
  <div class="legend" id="legend"></div>
 </section>
 <div id="mods"></div>
 <p class="empty" id="empty" hidden>Nenhum item com esses filtros. Tente outro termo ou limpe os filtros.</p>
</div></main>
<footer><div class="wrap">{html.escape(M['title'])} · versão {M['version']} · pesquisa em {M['date']}. {html.escape(M['review'])} Conteúdo de consulta; confira sempre a documentação oficial antes de depender de um recurso.</div></footer>
<div class="batch" id="batch" hidden><div class="wrap"><div class="row">
 <span class="n" id="bn">0 selecionados</span>
 <button class="btn small primary" id="bcopy">Copiar selecionados (0)</button>
 <button class="btn small" id="bshow" aria-pressed="false">Ver só selecionados</button>
 <button class="btn small" id="bclear">Limpar seleção</button>
</div></div></div>
<dialog class="menu" id="menu" aria-label="Módulos do guia"><div class="mh"><b>Módulos</b><button class="btn small" id="menuClose">Fechar</button></div><ol id="menuList"></ol></dialog>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script type="application/json" id="data">{j}</script>
<script>{JS}</script>
</body>
</html>"""

full = page()
open("out/index.html", "w", encoding="utf-8").write(full)
import re
art = full.split("<head>",1)[1]
art = art.replace('<meta charset="utf-8">','').replace('<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">','')
art = art.replace("</head>","").replace("<body>","").replace("</body>\n</html>","").replace("</body>","").replace("</html>","")
art = art.replace('<a href="guia-comandos-prompts-ia-2026.pdf" download>Baixar PDF</a>','<a href="guia-comandos-prompts-ia-2026.pdf" target="_blank" rel="noopener">Abrir PDF</a>')
open("out/artifact.html", "w", encoding="utf-8").write(art.strip())
print("ok", len(full), len(art))

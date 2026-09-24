import {createRenderer,defaultQ,colors,rgb,norm,mul,axisQ,cross,dot,pieceAt,worldAt} from './renderer.js';

const status=document.querySelector('#status');
const options={axes:true,numbers:false};
const format=a=>Number(a.toFixed(3))+'°';

async function start(){
 const response=await fetch('./assets/index.json');if(!response.ok)throw Error('The sphere data could not be loaded. Please reload the page.');
 const atlas=await response.json(),renderer=createRenderer(atlas),states=[],cache=new Map(),queue=[];
 let running=false;
 async function load(state){
  if(state.pixels){cache.delete(state);cache.set(state,true);return;}
  if(state.loading)return state.loading;
  state.loading=(async()=>{
  const response=await fetch('./assets/views/'+state.family.key+'-'+state.index+'.json');
  if(!response.ok)throw Error('This sphere could not be loaded. Try rotating it again.');
  state.variant=await response.json();prepare(state);
  const bytes=Uint8Array.from(atob(state.variant.data),c=>c.charCodeAt(0));
  const stream=new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'));
  const buffer=await new Response(stream).arrayBuffer();
  state.pixels=state.variant.labelBytes===2?new Uint16Array(buffer):new Uint8Array(buffer);
  delete state.variant.data;
  if(state.pixels.length!==state.width*state.height)throw Error('Unexpected sphere data size.');
  cache.set(state,true);
  let used=[...cache.keys()].reduce((n,s)=>n+s.pixels.byteLength,0);
  while(cache.size>1&&(cache.size>10||used>64*1024*1024)){const first=cache.keys().next().value;used-=first.pixels.byteLength;first.pixels=null;cache.delete(first);}
  })();
  try{await state.loading;}finally{state.loading=null;}
 }
 function prepare(state){
  if(state.classes)return;
  const {variant,card}=state;
  state.masks=new Uint32Array(variant.count+1);state.masks.fill(-1);
  state.fallback=Object.create(null);state.classes=new Int32Array(variant.count+1);
  variant.pieces.forEach((p,i)=>{state.masks[i+1]=p.mask;(state.fallback[p.mask]??=[]).push(i+1);});
  variant.orbits.forEach((group,i)=>group.forEach(j=>state.classes[j+1]=i));
  const legend=card.querySelector('.legend');
  if(variant.orbits.length>48){legend.classList.add('legend-scroll');legend.setAttribute('aria-label','Reachable piece classes; scroll for more');}
  variant.orbits.forEach((group,i)=>{const button=document.createElement('button');button.type='button';button.style.setProperty('--color',rgb(colors[i]));button.innerHTML=`<i aria-hidden="true"></i><span>${group.length}</span>`;button.setAttribute('aria-label',`Class ${i+1}: ${group.length} ${group.length===1?'piece':'pieces'}, ${group.map(j=>'P'+(j+1)).join(', ')}`);button.setAttribute('aria-pressed','false');button.title=`Class ${i+1} · ${group.map(j=>'P'+(j+1)).join(', ')}`;button.addEventListener('click',()=>select(state,i));legend.append(button);});
 }
 async function pump(){
  if(running)return;running=true;
  while(queue.length){
   const state=queue.shift();if(!state.visible)continue;
   try{await load(state);if(!state.visible)continue;renderer.render(state,state.canvas,options);state.canvas.style.opacity='1';state.drawn=true;state.canvas.setAttribute('aria-busy','false');}
   catch(error){state.card.querySelector('.detail').textContent=error.message;state.card.querySelector('.detail').classList.add('error');console.error(error);}
   await new Promise(requestAnimationFrame);
  }
  running=false;
 }
 function schedule(state,priority=false){if(!state.visible)return;const i=queue.indexOf(state);if(i>=0)queue.splice(i,1);if(priority)queue.unshift(state);else queue.push(state);void pump();}
 function select(state,group,piece=null){
  state.selected=state.selected===group?-1:group;
  state.card.querySelectorAll('.legend button').forEach((button,i)=>button.setAttribute('aria-pressed',String(i===state.selected)));
  const detail=state.card.querySelector('.detail');
  if(state.selected<0)detail.textContent='Select a piece or color to inspect its class.';
  else{const members=state.variant.orbits[state.selected];detail.textContent=`Class ${state.selected+1} · ${members.map(i=>'P'+(i+1)).join(', ')}${members.length===1?(state.variant.orbitStatus==='regular-only'?' · no transfer established yet':' · stays in its own position'):''}`;
   if(piece){const p=state.variant.pieces[piece-1];detail.textContent+=` · P${piece}: ${p.members.length?'in caps '+p.members.map(i=>'A'+i).join(', '):'stationary'}`;}}
  schedule(state,true);
 }
 function rotate(state,axis,angle){state.q=norm(mul(axisQ(axis,angle),state.q));schedule(state,true);}
 for(const card of document.querySelectorAll('.puzzle')){
  const family=atlas.families[Number(card.dataset.family)],variant=family.variants[Number(card.dataset.variant)],canvas=card.querySelector('canvas');
  const fullAxes=family.axes.map(u=>u.slice());
  if(variant.angle===90)family.axes.forEach(u=>{const v=u.map(x=>-x);if(!fullAxes.some(w=>Math.hypot(...w.map((x,i)=>x-v[i]))<1e-6))fullAxes.push(v);});
  const state={card,canvas,family,variant,index:Number(card.dataset.variant),width:variant.width||atlas.width,height:variant.height||atlas.height,fullAxes,cut:Math.cos(variant.angle*Math.PI/180),q:defaultQ(),zoom:1,selected:-1,pixels:null,drawn:false,visible:false};
  states.push(state);canvas.setAttribute('aria-busy','true');
  card.querySelector('.reset').addEventListener('click',()=>{state.q=defaultQ();state.zoom=1;if(state.selected>=0)select(state,state.selected);schedule(state,true);});
  const arrows=document.createElement('div');arrows.className='rotation';arrows.setAttribute('aria-label','Rotate sphere');
  for(const [label,text,axis,angle] of [['left','←',[0,1,0],-.35],['up','↑',[1,0,0],-.35],['down','↓',[1,0,0],.35],['right','→',[0,1,0],.35]]){const button=document.createElement('button');button.type='button';button.textContent=text;button.setAttribute('aria-label','Rotate '+label);button.addEventListener('click',()=>rotate(state,axis,angle));arrows.append(button);}
  card.querySelector('.card-tools').after(arrows);
  canvas.addEventListener('keydown',e=>{const keys={ArrowLeft:[[0,1,0],-.25],ArrowRight:[[0,1,0],.25],ArrowUp:[[1,0,0],-.25],ArrowDown:[[1,0,0],.25]};if(keys[e.key]){e.preventDefault();rotate(state,...keys[e.key]);}else if(e.key==='Home'){e.preventDefault();state.q=defaultQ();state.zoom=1;schedule(state,true);}else if(e.key==='Escape'&&state.selected>=0)select(state,state.selected);else if(e.key==='+'||e.key==='-'){e.preventDefault();state.zoom=Math.max(.7,Math.min(1.5,state.zoom+(e.key==='+'?.1:-.1)));schedule(state,true);}});
  const point=e=>{const rect=canvas.getBoundingClientRect();return[e.clientX-rect.left,e.clientY-rect.top];};
  const ball=p=>{const r=Math.min(canvas.clientWidth,canvas.clientHeight)*.423,x=(p[0]-canvas.clientWidth/2)/r,y=(canvas.clientHeight/2-p[1])/r;return norm([x,y,Math.sqrt(Math.max(0,1-x*x-y*y))]);};
  const pointers=new Map();let drag=null,pinch=null;
  canvas.addEventListener('pointerdown',e=>{if(e.button!==0)return;const p=point(e);pointers.set(e.pointerId,p);canvas.setPointerCapture(e.pointerId);if(pointers.size===1)drag={p,ball:ball(p),q:state.q.slice(),moved:false};if(pointers.size===2){const a=[...pointers.values()];pinch={distance:Math.hypot(a[0][0]-a[1][0],a[0][1]-a[1][1]),zoom:state.zoom};if(drag)drag.moved=true;}});
  canvas.addEventListener('pointermove',e=>{if(!pointers.has(e.pointerId))return;const p=point(e);pointers.set(e.pointerId,p);if(pointers.size===2&&pinch){const a=[...pointers.values()];state.zoom=Math.max(.7,Math.min(1.5,pinch.zoom*Math.hypot(a[0][0]-a[1][0],a[0][1]-a[1][1])/pinch.distance));schedule(state,true);return;}if(!drag)return;if(Math.hypot(p[0]-drag.p[0],p[1]-drag.p[1])>3)drag.moved=true;const b=ball(p),c=cross(drag.ball,b),w=1+dot(drag.ball,b);if(Math.hypot(...c,w)>1e-7)state.q=norm(mul(norm([...c,w]),drag.q));schedule(state,true);});
  function end(e){if(drag&&!drag.moved&&pointers.size===1&&state.pixels){const p=point(e),world=worldAt(state,...p,canvas.clientWidth,canvas.clientHeight),id=world?pieceAt(state,world,atlas):0;if(id)select(state,state.classes[id],id);}pointers.delete(e.pointerId);pinch=null;if(pointers.size===1){const p=[...pointers.values()][0];drag={p,ball:ball(p),q:state.q.slice(),moved:true};}else drag=null;}
  canvas.addEventListener('pointerup',end);canvas.addEventListener('pointercancel',e=>{pointers.delete(e.pointerId);drag=null;pinch=null;});
  canvas.addEventListener('wheel',e=>{if(!e.ctrlKey&&!e.metaKey)return;e.preventDefault();state.zoom=Math.max(.7,Math.min(1.5,state.zoom*Math.exp(-e.deltaY*.002)));schedule(state,true);},{passive:false});
  canvas.addEventListener('pointerenter',()=>{if(!state.pixels)void load(state).catch(()=>{});});
 }
 // All cards are present and painted, not selected through a menu. Prioritize
 // the viewport so an anchor jump never waits for earlier offscreen cards.
 const byCard=new Map(states.map(s=>[s.card,s]));
 const visible=new IntersectionObserver(entries=>{for(const entry of entries){const state=byCard.get(entry.target);state.visible=entry.isIntersecting;if(state.visible)schedule(state,true);else{state.canvas.style.opacity='0';state.canvas.width=state.canvas.height=1;}}},{rootMargin:'450px'});
 states.forEach(s=>visible.observe(s.card));status.textContent='';
 for(const [id,key] of [['show-axes','axes'],['show-numbers','numbers']])document.getElementById(id).addEventListener('change',e=>{options[key]=e.target.checked;states.forEach(s=>schedule(s));});
 let resizeTimer;window.addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(()=>states.forEach(s=>schedule(s)),160);});
 matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>states.forEach(s=>schedule(s)));
 const sections=[...document.querySelectorAll('.family,#method')];
 const navObserver=new IntersectionObserver(entries=>{for(const e of entries)if(e.isIntersecting){document.querySelectorAll('nav a').forEach(a=>{const current=a.hash==='#'+e.target.id;a.classList.toggle('current',current);if(current)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});}},{rootMargin:'-10% 0px -70% 0px'});sections.forEach(s=>navObserver.observe(s));
}
start().catch(error=>{status.className='error';status.textContent=error.message||'The interactive spheres could not load. Please try a current browser.';console.error(error);});

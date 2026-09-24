// One WebGL context serves every card. Each card retains a 2D snapshot.
export const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
export const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
export const norm=a=>{const d=Math.hypot(...a);return a.map(x=>x/d);};
export const mul=(a,b)=>[a[3]*b[0]+a[0]*b[3]+a[1]*b[2]-a[2]*b[1],a[3]*b[1]-a[0]*b[2]+a[1]*b[3]+a[2]*b[0],a[3]*b[2]+a[0]*b[1]-a[1]*b[0]+a[2]*b[3],a[3]*b[3]-a[0]*b[0]-a[1]*b[1]-a[2]*b[2]];
export const axisQ=(u,a)=>[u[0]*Math.sin(a/2),u[1]*Math.sin(a/2),u[2]*Math.sin(a/2),Math.cos(a/2)];
export const applyQ=(q,v)=>{const t=cross(q,v).map(x=>2*x),c=cross(q,t);return v.map((x,i)=>x+q[3]*t[i]+c[i]);};
export const inverse=q=>[-q[0],-q[1],-q[2],q[3]];
export const defaultQ=()=>norm(mul(axisQ([1,0,0],-.55),axisQ([0,1,0],.68)));
function hsl(h,s,l){const a=s*Math.min(l,1-l),f=n=>{const k=(n+h/30)%12;return l-a*Math.max(-1,Math.min(k-3,9-k,1));};return[f(0),f(8),f(4)];}
export const colors=Array.from({length:2048},(_,i)=>hsl((211+i*137.507764)%360,.61+(i%4)*.055,.58+(((i*3)%5)-2)*.04));
export const rgb=(c,a=1)=>`rgba(${c.map(x=>Math.round(x*255)).join(',')},${a})`;
export function pieceAt(state,world,atlas){
 const {family,variant,pixels,masks,fallback}=state;atlas=state;
 const x=Math.floor((Math.atan2(world[1],world[0])/(2*Math.PI)+.5)*atlas.width)%atlas.width,y=Math.min(atlas.height-1,Math.floor(Math.acos(Math.max(-1,Math.min(1,world[2])))/Math.PI*atlas.height));
 let mask=0;family.axes.forEach((u,i)=>{if(dot(u,world)>state.cut)mask|=1<<i;});
 let id=pixels[y*atlas.width+x];
 if(!id||masks[id]!==mask){id=0;let best=-2;for(const candidate of fallback[mask]||[]){const score=dot(world,variant.pieces[candidate-1].seed);if(score>best){best=score;id=candidate;}}}return id;
}
export function worldAt(state,x,y,w,h){const r=Math.min(w,h)*.423*state.zoom,a=(x-w/2)/r,b=(h/2-y)/r;if(a*a+b*b>1)return null;return applyQ(inverse(state.q),[a,b,Math.sqrt(Math.max(0,1-a*a-b*b))]);}
export function createRenderer(atlas){
 const axisCapacity=Math.max(...atlas.families.map(f=>f.axes.length));
 const surface=document.createElement('canvas');let gl=surface.getContext('webgl2',{alpha:true,antialias:true,premultipliedAlpha:false});let program,texture,maskTexture,colorTexture,seedTexture;const uniforms={};let lastState=null;
 function shader(type,source){const s=gl.createShader(type);gl.shaderSource(s,source);gl.compileShader(s);if(!gl.getShaderParameter(s,gl.COMPILE_STATUS))throw Error(gl.getShaderInfoLog(s));return s;}
 if(gl){try{program=gl.createProgram();gl.attachShader(program,shader(gl.VERTEX_SHADER,`#version 300 es
 void main(){vec2 p=vec2((gl_VertexID<<1)&2,gl_VertexID&2);gl_Position=vec4(p*2.0-1.0,0.0,1.0);}`));
 gl.attachShader(program,shader(gl.FRAGMENT_SHADER,`#version 300 es
      precision highp float; precision highp int; precision highp usampler2D; precision highp sampler2D;
      uniform vec2 uSize;uniform float uRadius;uniform mat3 uCamera;uniform usampler2D uAtlas;
      uniform int uCount,uPieces;uniform vec3 uAxes[${axisCapacity}],uInk;
      uniform usampler2D uMasks;uniform sampler2D uColors,uSeeds;
      uniform float uCut,uAngle;out vec4 outColor;
      int sampleId(ivec2 p,ivec2 size){return int(texelFetch(uAtlas,ivec2((p.x%size.x+size.x)%size.x,clamp(p.y,0,size.y-1)),0).r);}
      int maskFor(int id){return int(texelFetch(uMasks,ivec2(id,0),0).r);}
      void main(){
        vec2 xy=(gl_FragCoord.xy-uSize*.5)/uRadius;float r2=dot(xy,xy);
        if(r2>1.0)discard;
        vec3 local=vec3(xy,sqrt(max(0.0,1.0-r2))),world=uCamera*local;
        vec2 uv=vec2(atan(world.y,world.x)/6.28318530718+.5,acos(clamp(world.z,-1.0,1.0))/3.14159265359);
        ivec2 size=textureSize(uAtlas,0),p=ivec2(floor(uv*vec2(size)));
        int mask=0;float edge=1.0;
        for(int i=0;i<${axisCapacity};i++){
          if(i>=uCount)break;
          float d=dot(uAxes[i],world)-uCut;if(d>0.0)mask|=1<<i;
          if(uAngle>0.00001)edge=min(edge,smoothstep(0.0,max(fwidth(d)*1.05,0.00006),abs(d)));
        }
        int id=sampleId(p,size);
        if(id==0||maskFor(id)!=mask){
          int found=0;float best=-2.0;
          for(int j=1;j<=uPieces;j++){
            if(maskFor(j)!=mask)continue;
            float score=dot(texelFetch(uSeeds,ivec2(j,0),0).xyz,world);
            if(score>best){best=score;found=j;}
          }
          id=found;
        }
        id=clamp(id,1,uPieces);vec3 color=texelFetch(uColors,ivec2(id,0),0).rgb;
        vec3 light=normalize(vec3(-.45,.65,1.1));float shade=.60+.36*max(0.0,dot(local,light));
        float shine=.13*pow(max(0.0,dot(local,normalize(light+vec3(0,0,1)))),36.0);
        color=color*shade+vec3(shine);color=mix(uInk,color,edge);
        float silhouette=smoothstep(0.0,1.4/uRadius,1.0-sqrt(r2));outColor=vec4(color,silhouette);
      }`));gl.linkProgram(program);if(!gl.getProgramParameter(program,gl.LINK_STATUS))throw Error(gl.getProgramInfoLog(program));
 for(const name of ['Size','Radius','Camera','Atlas','Count','Pieces','Cut','Angle','Ink','Masks','Colors','Seeds'])uniforms[name]=gl.getUniformLocation(program,'u'+name);
 uniforms.Axes=gl.getUniformLocation(program,'uAxes[0]');
 texture=gl.createTexture();gl.bindTexture(gl.TEXTURE_2D,texture);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.NEAREST);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MAG_FILTER,gl.NEAREST);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_S,gl.REPEAT);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_T,gl.CLAMP_TO_EDGE);
 maskTexture=gl.createTexture();colorTexture=gl.createTexture();seedTexture=gl.createTexture();
 for(const t of [maskTexture,colorTexture,seedTexture]){gl.bindTexture(gl.TEXTURE_2D,t);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.NEAREST);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MAG_FILTER,gl.NEAREST);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_S,gl.CLAMP_TO_EDGE);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_T,gl.CLAMP_TO_EDGE);}
 }catch(e){console.warn('Using the software renderer:',e);gl=null;}}
 const cpuCanvas=document.createElement('canvas'),cpu=cpuCanvas.getContext('2d');
 surface.addEventListener('webglcontextlost',e=>{e.preventDefault();gl=null;});
 function render(state,canvas,options){
  const w=canvas.clientWidth||400,h=canvas.clientHeight||327,dpr=Math.min(1.5,devicePixelRatio||1);
  const W=Math.round(w*dpr),H=Math.round(h*dpr);if(canvas.width!==W||canvas.height!==H){canvas.width=W;canvas.height=H;}
  const ctx=canvas.getContext('2d'),r=Math.min(w,h)*.423*state.zoom;
  const dark=matchMedia('(prefers-color-scheme: dark)').matches,ink=dark?[.83,.89,.98]:[.09,.14,.23],bg=dark?[.09,.13,.19]:[1,1,1];
  const palette=Array.from({length:state.variant.count+1},(_,id)=>{let c=colors[state.classes[id]||0];if(state.selected>=0&&state.classes[id]!==state.selected){const gray=dot(c,[.2126,.7152,.0722]);c=c.map(x=>gray*.8+x*.2);}return c;});
  ctx.setTransform(1,0,0,1,0,0);ctx.clearRect(0,0,W,H);
  if(gl){
   surface.width=W;surface.height=H;gl.viewport(0,0,W,H);gl.clearColor(0,0,0,0);gl.clear(gl.COLOR_BUFFER_BIT);gl.useProgram(program);gl.activeTexture(gl.TEXTURE0);gl.bindTexture(gl.TEXTURE_2D,texture);
   if(lastState!==state){gl.pixelStorei(gl.UNPACK_ALIGNMENT,1);gl.texImage2D(gl.TEXTURE_2D,0,state.variant.labelBytes===2?gl.R16UI:gl.R8UI,state.width,state.height,0,gl.RED_INTEGER,state.variant.labelBytes===2?gl.UNSIGNED_SHORT:gl.UNSIGNED_BYTE,state.pixels);gl.activeTexture(gl.TEXTURE1);gl.bindTexture(gl.TEXTURE_2D,maskTexture);gl.texImage2D(gl.TEXTURE_2D,0,gl.R32UI,state.masks.length,1,0,gl.RED_INTEGER,gl.UNSIGNED_INT,state.masks);gl.activeTexture(gl.TEXTURE3);gl.bindTexture(gl.TEXTURE_2D,seedTexture);gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA32F,state.masks.length,1,0,gl.RGBA,gl.FLOAT,new Float32Array([0,0,0,0,...state.variant.pieces.flatMap(p=>[...p.seed,0])]));lastState=state;}
   gl.activeTexture(gl.TEXTURE1);gl.bindTexture(gl.TEXTURE_2D,maskTexture);gl.activeTexture(gl.TEXTURE2);gl.bindTexture(gl.TEXTURE_2D,colorTexture);gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA8,palette.length,1,0,gl.RGBA,gl.UNSIGNED_BYTE,new Uint8Array(palette.flatMap(c=>[...c.map(x=>Math.round(x*255)),255])));
   const inv=inverse(state.q),matrix=[...applyQ(inv,[1,0,0]),...applyQ(inv,[0,1,0]),...applyQ(inv,[0,0,1])];
   gl.uniform2f(uniforms.Size,W,H);gl.uniform1f(uniforms.Radius,r*dpr);gl.uniformMatrix3fv(uniforms.Camera,false,new Float32Array(matrix));gl.uniform1i(uniforms.Atlas,0);gl.uniform1i(uniforms.Count,state.family.axes.length);gl.uniform1i(uniforms.Pieces,state.variant.count);gl.uniform1i(uniforms.Masks,1);gl.uniform1i(uniforms.Colors,2);gl.uniform1i(uniforms.Seeds,3);gl.uniform1f(uniforms.Cut,state.cut);gl.uniform1f(uniforms.Angle,state.variant.angle);gl.uniform3fv(uniforms.Ink,new Float32Array(ink));gl.uniform3fv(uniforms.Axes,new Float32Array(state.family.axes.flat().concat(Array(axisCapacity*3-state.family.axes.length*3).fill(0))));gl.drawArrays(gl.TRIANGLES,0,3);ctx.drawImage(surface,0,0);
  }else{
   const scale=Math.min(1,300/w),cw=Math.round(w*scale),ch=Math.round(h*scale);cpuCanvas.width=cw;cpuCanvas.height=ch;const data=cpu.createImageData(cw,ch);const light=norm([-.45,.65,1.1]);
   for(let y=0;y<ch;y++)for(let x=0;x<cw;x++){const world=worldAt(state,(x+.5)/scale,(y+.5)/scale,w,h);if(!world)continue;const id=pieceAt(state,world,atlas)||1,local=applyQ(state.q,world),col=palette[id];const shade=.6+.36*Math.max(0,dot(local,light));let edge=1;if(state.variant.angle>0)for(const u of state.family.axes)edge=Math.min(edge,Math.min(1,Math.abs(dot(u,world)-state.cut)*200));const p=(y*cw+x)*4;for(let k=0;k<3;k++)data.data[p+k]=Math.round(255*(ink[k]*(1-edge)+col[k]*shade*edge));data.data[p+3]=255;}cpu.putImageData(data,0,0);ctx.drawImage(cpuCanvas,0,0,W,H);
  }
  ctx.setTransform(dpr,0,0,dpr,0,0);ctx.font='500 12px system-ui, sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';const boxes=[];
  function label(v,text,isAxis){const p=applyQ(state.q,v);if(p[2]<(isAxis?.015:.2))return;const x=w/2+r*p[0],y=h/2-r*p[1],tw=ctx.measureText(text).width+8,th=20;if(!isAxis&&boxes.some(b=>Math.abs(x-b[0])<(tw+b[2])/2&&Math.abs(y-b[1])<th))return;boxes.push([x,y,tw]);ctx.fillStyle=rgb(bg,.88);ctx.beginPath();ctx.roundRect(x-tw/2,y-th/2,tw,th,4);ctx.fill();ctx.fillStyle=rgb(ink);ctx.fillText(text,x,y+.5);}
  if(options.axes)state.fullAxes.forEach((u,i)=>label(u,'A'+(i+1),true));
  if(options.numbers)state.variant.pieces.forEach((p,i)=>label(p.seed,'P'+(i+1),false));
 }
 return {render};
}
